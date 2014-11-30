from collections import OrderedDict

class AirTerminalSingleDuctUncontrolled(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:Uncontrolled`
        Central air system terminal unit, single duct, constant volume, no controls other than
        on/off schedule.
    
    """
    internal_name = "AirTerminal:SingleDuct:Uncontrolled"
    field_count = 4
    required_fields = ["Name", "Zone Supply Air Node Name", "Maximum Air Flow Rate"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirTerminal:SingleDuct:Uncontrolled`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Supply Air Node Name"] = None
        self._data["Maximum Air Flow Rate"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `zone_supply_air_node_name`

        Args:
            value (str): value for IDD Field `zone_supply_air_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_supply_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_supply_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_supply_air_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

        self._data["Maximum Air Flow Rate"] = value

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

class AirTerminalSingleDuctConstantVolumeReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:Reheat`
        Central air system terminal unit, single duct, constant volume, with reheat coil (hot
        water, electric, gas, or steam).
    
    """
    internal_name = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
    field_count = 12
    required_fields = ["Name", "Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Reheat Coil Object Type", "Reheat Coil Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

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
        """  Corresponds to IDD Field `hot_water_or_steam_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_or_steam_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_or_steam_inlet_node_name`')

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
        """  Corresponds to IDD Field `reheat_coil_object_type`

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reheat_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `reheat_coil_name`

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
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
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_hot_water_or_steam_flow_rate`')

        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')

        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_tolerance`

        Args:
            value (float): value for IDD Field `convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `convergence_tolerance`')

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
        """  Corresponds to IDD Field `maximum_reheat_air_temperature`
        Specifies the maximum allowable supply air temperature leaving the reheat coil.
        If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.

        Args:
            value (float): value for IDD Field `maximum_reheat_air_temperature`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_reheat_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_reheat_air_temperature`')

        self._data["Maximum Reheat Air Temperature"] = value

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

class AirTerminalSingleDuctVavNoReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:NoReheat`
        Central air system terminal unit, single duct, variable volume, with no reheat coil.
    
    """
    internal_name = "AirTerminal:SingleDuct:VAV:NoReheat"
    field_count = 10
    required_fields = ["Name", "Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Input Method"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

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
        """  Corresponds to IDD Field `zone_minimum_air_flow_input_method`
        Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate)
        FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate)
        Scheduled = Scheduled Minimum Air Flow Fraction (a fraction of Maximum Air Flow

        Args:
            value (str): value for IDD Field `zone_minimum_air_flow_input_method`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_minimum_air_flow_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_minimum_air_flow_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_minimum_air_flow_input_method`')
            vals = {}
            vals["constant"] = "Constant"
            vals["fixedflowrate"] = "FixedFlowRate"
            vals["scheduled"] = "Scheduled"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `zone_minimum_air_flow_input_method`'.format(value))
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
        """  Corresponds to IDD Field `constant_minimum_air_flow_fraction`
        This field is used if the field Zone Minimum Air Flow Input Method is Constant
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the following field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `constant_minimum_air_flow_fraction`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `constant_minimum_air_flow_fraction`'.format(value))

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
        """  Corresponds to IDD Field `fixed_minimum_air_flow_rate`
        This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate.
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the previous field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `fixed_minimum_air_flow_rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fixed_minimum_air_flow_rate`'.format(value))

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
        """  Corresponds to IDD Field `minimum_air_flow_fraction_schedule_name`
        This field is used if the field Zone Minimum Air Flow Input Method is Scheduled
        Schedule values are fractions, 0.0 to 1.0.
        If the field Constant Minimum Air Flow Fraction is blank, then the average of the
        minimum and maximum schedule values is used for sizing normal-action reheat coils.

        Args:
            value (str): value for IDD Field `minimum_air_flow_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_air_flow_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_air_flow_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_air_flow_fraction_schedule_name`')

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
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based on the current number of occupants in the zone.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name`')

        self._data["Design Specification Outdoor Air Object Name"] = value

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

class AirTerminalSingleDuctVavReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:Reheat`
        Central air system terminal unit, single duct, variable volume, with reheat coil (hot
        water, electric, gas, or steam).
    
    """
    internal_name = "AirTerminal:SingleDuct:VAV:Reheat"
    field_count = 20
    required_fields = ["Name", "Damper Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Input Method", "Reheat Coil Object Type", "Reheat Coil Name", "Air Outlet Node Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `damper_air_outlet_node_name`
        the outlet node of the damper and the inlet node of the reheat coil
        this is an internal node to the terminal unit and connects the damper and reheat coil

        Args:
            value (str): value for IDD Field `damper_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `damper_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `damper_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `damper_air_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`
        the inlet node to the terminal unit and the damper

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

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
        """  Corresponds to IDD Field `zone_minimum_air_flow_input_method`
        Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate)
        FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate)
        Scheduled = Scheduled Minimum Air Flow Fraction (a fraction of Maximum Air Flow

        Args:
            value (str): value for IDD Field `zone_minimum_air_flow_input_method`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_minimum_air_flow_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_minimum_air_flow_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_minimum_air_flow_input_method`')
            vals = {}
            vals["constant"] = "Constant"
            vals["fixedflowrate"] = "FixedFlowRate"
            vals["scheduled"] = "Scheduled"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `zone_minimum_air_flow_input_method`'.format(value))
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
        """  Corresponds to IDD Field `constant_minimum_air_flow_fraction`
        This field is used if the field Zone Minimum Air Flow Input Method is Constant
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the following field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `constant_minimum_air_flow_fraction`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `constant_minimum_air_flow_fraction`'.format(value))

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
        """  Corresponds to IDD Field `fixed_minimum_air_flow_rate`
        This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate.
        If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        If both this field and the previous field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `fixed_minimum_air_flow_rate`
                Units: m3/s
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fixed_minimum_air_flow_rate`'.format(value))

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
        """  Corresponds to IDD Field `minimum_air_flow_fraction_schedule_name`
        This field is used if the field Zone Minimum Air Flow Input Method is Scheduled
        Schedule values are fractions, 0.0 to 1.0.
        If the field Constant Minimum Air Flow Fraction is blank, then the average of the
        minimum and maximum schedule values is used for sizing normal-action reheat coils.

        Args:
            value (str): value for IDD Field `minimum_air_flow_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_air_flow_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_air_flow_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_air_flow_fraction_schedule_name`')

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
        """  Corresponds to IDD Field `reheat_coil_object_type`

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reheat_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `reheat_coil_name`

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
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
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_hot_water_or_steam_flow_rate`')

        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        The outlet node of the terminal unit and the reheat coil.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_tolerance`

        Args:
            value (float): value for IDD Field `convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `convergence_tolerance`')

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
        """  Corresponds to IDD Field `damper_heating_action`

        Args:
            value (str): value for IDD Field `damper_heating_action`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `damper_heating_action`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `damper_heating_action`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `damper_heating_action`')
            vals = {}
            vals["normal"] = "Normal"
            vals["reverse"] = "Reverse"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `damper_heating_action`'.format(value))
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
        """  Corresponds to IDD Field `maximum_flow_per_zone_floor_area_during_reheat`
        Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse
        When autocalculating, the maximum flow per zone is set to 0.002032 m3/s-m2 (0.4 cfm/sqft)
        This optional field limits the maximum flow allowed in reheat mode.
        If this field and the following field are left blank, the maximum flow will not be limited.
        At no time will the maximum flow rate calculated here exceed the value of
        Maximum Air Flow Rate.

        Args:
            value (float): value for IDD Field `maximum_flow_per_zone_floor_area_during_reheat`
                Units: m3/s-m2
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_flow_per_zone_floor_area_during_reheat`'.format(value))

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
        """  Corresponds to IDD Field `maximum_flow_fraction_during_reheat`
        Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse
        When autocalculating, the maximum flow fraction is set to the ratio of
        0.002032 m3/s-m2 (0.4 cfm/sqft) multiplied by the zone floor area and the
        Maximum Air Flow Rate.
        This optional field limits the maximum flow allowed in reheat mode.
        If this field and the previous field are left blank, the maximum flow will not be limited.
        At no time will the maximum flow rate calculated here exceed the value of
        Maximum Air Flow Rate.

        Args:
            value (float): value for IDD Field `maximum_flow_fraction_during_reheat`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_flow_fraction_during_reheat`'.format(value))

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
        """  Corresponds to IDD Field `maximum_reheat_air_temperature`
        Specifies the maximum allowable supply air temperature leaving the reheat coil.
        If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.

        Args:
            value (float): value for IDD Field `maximum_reheat_air_temperature`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_reheat_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_reheat_air_temperature`')

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
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based on the current number of occupants in the zone.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name`')

        self._data["Design Specification Outdoor Air Object Name"] = value

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `maximum_cooling_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_cooling_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_cooling_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_cooling_air_flow_rate`')

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
        """  Corresponds to IDD Field `maximum_heating_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_heating_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_heating_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_heating_air_flow_rate`')

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
        """  Corresponds to IDD Field `zone_minimum_air_flow_fraction`
        fraction of cooling air flow rate

        Args:
            value (float): value for IDD Field `zone_minimum_air_flow_fraction`
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
                                 'for field `zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `zone_minimum_air_flow_fraction`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `heating_coil_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `heating_coil_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `hot_water_or_steam_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_or_steam_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_or_steam_inlet_node_name`')

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
        """  Corresponds to IDD Field `fan_object_type`

        Args:
            value (str): value for IDD Field `fan_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_object_type`')
            vals = {}
            vals["fan:variablevolume"] = "Fan:VariableVolume"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `fan_object_type`'.format(value))
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
        """  Corresponds to IDD Field `fan_name`

        Args:
            value (str): value for IDD Field `fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_name`')

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
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heating_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `heating_coil_name`

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))

        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')

        self._data["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence_tolerance`

        Args:
            value (float): value for IDD Field `heating_convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence_tolerance`')

        self._data["Heating Convergence Tolerance"] = value

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

class AirTerminalSingleDuctVavHeatAndCoolNoReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat`
        Central air system terminal unit, single duct, variable volume for both cooling and
        heating, with no reheat coil.
    
    """
    internal_name = "AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"
    field_count = 6
    required_fields = ["Name", "Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Fraction"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_air_flow_rate`')

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
        """  Corresponds to IDD Field `zone_minimum_air_flow_fraction`
        fraction of maximum air flow

        Args:
            value (float): value for IDD Field `zone_minimum_air_flow_fraction`
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
                                 'for field `zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `zone_minimum_air_flow_fraction`')

        self._data["Zone Minimum Air Flow Fraction"] = value

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

class AirTerminalSingleDuctVavHeatAndCoolReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat`
        Central air system terminal unit, single duct, variable volume for both cooling and
        heating, with reheat coil (hot water, electric, gas, or steam).
    
    """
    internal_name = "AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"
    field_count = 14
    required_fields = ["Name", "Damper Air Outlet Node Name", "Air Inlet Node Name", "Maximum Air Flow Rate", "Zone Minimum Air Flow Fraction", "Reheat Coil Object Type", "Reheat Coil Name", "Air Outlet Node Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `damper_air_outlet_node_name`
        the outlet node of the damper and the inlet node of the reheat coil
        this is an internal node to the terminal unit and connects the damper and reheat coil

        Args:
            value (str): value for IDD Field `damper_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `damper_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `damper_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `damper_air_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_inlet_node_name`
        the inlet node to the terminal unit and the damper

        Args:
            value (str): value for IDD Field `air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_air_flow_rate`')

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
        """  Corresponds to IDD Field `zone_minimum_air_flow_fraction`
        fraction of maximum air flow

        Args:
            value (float): value for IDD Field `zone_minimum_air_flow_fraction`
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
                                 'for field `zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `zone_minimum_air_flow_fraction`')

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
        """  Corresponds to IDD Field `hot_water_or_steam_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_or_steam_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_or_steam_inlet_node_name`')

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
        """  Corresponds to IDD Field `reheat_coil_object_type`

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reheat_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `reheat_coil_name`

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
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
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_hot_water_or_steam_flow_rate`')

        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        The outlet node of the terminal unit and the reheat coil.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

        self._data["Air Outlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_tolerance`

        Args:
            value (float): value for IDD Field `convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `convergence_tolerance`')

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
        """  Corresponds to IDD Field `maximum_reheat_air_temperature`
        Specifies the maximum allowable supply air temperature leaving the reheat coil.
        If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.

        Args:
            value (float): value for IDD Field `maximum_reheat_air_temperature`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_reheat_air_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_reheat_air_temperature`')

        self._data["Maximum Reheat Air Temperature"] = value

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

class AirTerminalSingleDuctSeriesPiuReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:SeriesPIU:Reheat`
        Central air system terminal unit, single duct, variable volume, series powered
        induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).
    
    """
    internal_name = "AirTerminal:SingleDuct:SeriesPIU:Reheat"
    field_count = 17
    required_fields = ["Name", "Maximum Air Flow Rate", "Maximum Primary Air Flow Rate", "Minimum Primary Air Flow Fraction", "Reheat Coil Object Type", "Reheat Coil Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

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
        """  Corresponds to IDD Field `maximum_primary_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_primary_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_primary_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_primary_air_flow_rate`')

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
        """  Corresponds to IDD Field `minimum_primary_air_flow_fraction`

        Args:
            value (float): value for IDD Field `minimum_primary_air_flow_fraction`
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
                                 'for field `minimum_primary_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_primary_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_primary_air_flow_fraction`')

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
        """  Corresponds to IDD Field `supply_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `secondary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `secondary_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

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
        """  Corresponds to IDD Field `reheat_coil_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `reheat_coil_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `zone_mixer_name`

        Args:
            value (str): value for IDD Field `zone_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_mixer_name`')

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
        """  Corresponds to IDD Field `fan_name`
        Fan type must be Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_name`')

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
        """  Corresponds to IDD Field `reheat_coil_object_type`

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reheat_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `reheat_coil_name`

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))

        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')

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
        """  Corresponds to IDD Field `hot_water_or_steam_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_or_steam_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_or_steam_inlet_node_name`')

        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_tolerance`

        Args:
            value (float): value for IDD Field `convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `convergence_tolerance`')

        self._data["Convergence Tolerance"] = value

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

class AirTerminalSingleDuctParallelPiuReheat(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ParallelPIU:Reheat`
        Central air system terminal unit, single duct, variable volume, parallel powered
        induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).
    
    """
    internal_name = "AirTerminal:SingleDuct:ParallelPIU:Reheat"
    field_count = 18
    required_fields = ["Name", "Maximum Primary Air Flow Rate", "Maximum Secondary Air Flow Rate", "Minimum Primary Air Flow Fraction", "Fan On Flow Fraction", "Reheat Coil Object Type", "Reheat Coil Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `maximum_primary_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_primary_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_primary_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_primary_air_flow_rate`')

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
        """  Corresponds to IDD Field `maximum_secondary_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_secondary_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_secondary_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_secondary_air_flow_rate`')

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
        """  Corresponds to IDD Field `minimum_primary_air_flow_fraction`

        Args:
            value (float): value for IDD Field `minimum_primary_air_flow_fraction`
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
                                 'for field `minimum_primary_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_primary_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_primary_air_flow_fraction`')

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
        """  Corresponds to IDD Field `fan_on_flow_fraction`
        the fraction of the primary air flow at which fan turns on

        Args:
            value (float): value for IDD Field `fan_on_flow_fraction`
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
                                 'for field `fan_on_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fan_on_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fan_on_flow_fraction`')

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
        """  Corresponds to IDD Field `supply_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `secondary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `secondary_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outlet_node_name`')

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
        """  Corresponds to IDD Field `reheat_coil_air_inlet_node_name`
        mixer outlet node

        Args:
            value (str): value for IDD Field `reheat_coil_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `zone_mixer_name`

        Args:
            value (str): value for IDD Field `zone_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_mixer_name`')

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
        """  Corresponds to IDD Field `fan_name`
        Fan type must be Fan:ConstantVolume

        Args:
            value (str): value for IDD Field `fan_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fan_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fan_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fan_name`')

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
        """  Corresponds to IDD Field `reheat_coil_object_type`

        Args:
            value (str): value for IDD Field `reheat_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            vals["coil:heating:electric"] = "Coil:Heating:Electric"
            vals["coil:heating:gas"] = "Coil:Heating:Gas"
            vals["coil:heating:steam"] = "Coil:Heating:Steam"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `reheat_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `reheat_coil_name`

        Args:
            value (str): value for IDD Field `reheat_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `reheat_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `reheat_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `reheat_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_or_steam_flow_rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_or_steam_flow_rate`'.format(value))

        self._data["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """Get minimum_hot_water_or_steam_flow_rate

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_or_steam_flow_rate`
        Not used when reheat coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_or_steam_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_or_steam_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_or_steam_flow_rate`')

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
        """  Corresponds to IDD Field `hot_water_or_steam_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_or_steam_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_or_steam_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_or_steam_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_or_steam_inlet_node_name`')

        self._data["Hot Water or Steam Inlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """Get convergence_tolerance

        Returns:
            float: the value of `convergence_tolerance` or None if not set
        """
        return self._data["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `convergence_tolerance`

        Args:
            value (float): value for IDD Field `convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `convergence_tolerance`')

        self._data["Convergence Tolerance"] = value

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

class AirTerminalSingleDuctConstantVolumeFourPipeInduction(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction`
        Central air system terminal unit, single duct, variable volume, induction unit with
        hot water reheat coil and chilled water recool coil.
    
    """
    internal_name = "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"
    field_count = 20
    required_fields = ["Name", "Maximum Total Air Flow Rate", "Induction Ratio", "Supply Air Inlet Node Name", "Induced Air Inlet Node Name", "Air Outlet Node Name", "Heating Coil Object Type", "Heating Coil Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `maximum_total_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_total_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_total_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_total_air_flow_rate`')

        self._data["Maximum Total Air Flow Rate"] = value

    @property
    def induction_ratio(self):
        """Get induction_ratio

        Returns:
            float: the value of `induction_ratio` or None if not set
        """
        return self._data["Induction Ratio"]

    @induction_ratio.setter
    def induction_ratio(self, value=2.5 ):
        """  Corresponds to IDD Field `induction_ratio`
        ratio of induced air flow rate to primary air flow rate

        Args:
            value (float): value for IDD Field `induction_ratio`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `induction_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `induction_ratio`')

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
        """  Corresponds to IDD Field `supply_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `induced_air_inlet_node_name`
        should be a zone exhaust node, also the heating coil inlet node

        Args:
            value (str): value for IDD Field `induced_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `induced_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `induced_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `induced_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        should be a zone inlet node

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `hot_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_water_inlet_node_name`')

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
        """  Corresponds to IDD Field `cold_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `cold_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cold_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_water_inlet_node_name`')

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
        """  Corresponds to IDD Field `heating_coil_object_type`

        Args:
            value (str): value for IDD Field `heating_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_object_type`')
            vals = {}
            vals["coil:heating:water"] = "Coil:Heating:Water"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heating_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `heating_coil_name`

        Args:
            value (str): value for IDD Field `heating_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_coil_name`')

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
        """  Corresponds to IDD Field `maximum_hot_water_flow_rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float): value for IDD Field `maximum_hot_water_flow_rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_hot_water_flow_rate`'.format(value))

        self._data["Maximum Hot Water Flow Rate"] = value

    @property
    def minimum_hot_water_flow_rate(self):
        """Get minimum_hot_water_flow_rate

        Returns:
            float: the value of `minimum_hot_water_flow_rate` or None if not set
        """
        return self._data["Minimum Hot Water Flow Rate"]

    @minimum_hot_water_flow_rate.setter
    def minimum_hot_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_hot_water_flow_rate`
        Not used when heating coil type is gas or electric

        Args:
            value (float): value for IDD Field `minimum_hot_water_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_hot_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_hot_water_flow_rate`')

        self._data["Minimum Hot Water Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """Get heating_convergence_tolerance

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set
        """
        return self._data["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `heating_convergence_tolerance`

        Args:
            value (float): value for IDD Field `heating_convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `heating_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_convergence_tolerance`')

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
        """  Corresponds to IDD Field `cooling_coil_object_type`

        Args:
            value (str): value for IDD Field `cooling_coil_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_object_type`')
            vals = {}
            vals["coil:cooling:water"] = "Coil:Cooling:Water"
            vals["coil:cooling:water:detailedgeometry"] = "Coil:Cooling:Water:DetailedGeometry"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `cooling_coil_object_type`'.format(value))
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
        """  Corresponds to IDD Field `cooling_coil_name`

        Args:
            value (str): value for IDD Field `cooling_coil_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_coil_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_coil_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_coil_name`')

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
        """  Corresponds to IDD Field `maximum_cold_water_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_cold_water_flow_rate`
                Units: m3/s
                IP-Units: gal/min
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_cold_water_flow_rate`'.format(value))

        self._data["Maximum Cold Water Flow Rate"] = value

    @property
    def minimum_cold_water_flow_rate(self):
        """Get minimum_cold_water_flow_rate

        Returns:
            float: the value of `minimum_cold_water_flow_rate` or None if not set
        """
        return self._data["Minimum Cold Water Flow Rate"]

    @minimum_cold_water_flow_rate.setter
    def minimum_cold_water_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_cold_water_flow_rate`

        Args:
            value (float): value for IDD Field `minimum_cold_water_flow_rate`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_cold_water_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_cold_water_flow_rate`')

        self._data["Minimum Cold Water Flow Rate"] = value

    @property
    def cooling_convergence_tolerance(self):
        """Get cooling_convergence_tolerance

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set
        """
        return self._data["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001 ):
        """  Corresponds to IDD Field `cooling_convergence_tolerance`

        Args:
            value (float): value for IDD Field `cooling_convergence_tolerance`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `cooling_convergence_tolerance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_convergence_tolerance`')

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
        """  Corresponds to IDD Field `zone_mixer_name`

        Args:
            value (str): value for IDD Field `zone_mixer_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_mixer_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_mixer_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_mixer_name`')

        self._data["Zone Mixer Name"] = value

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

class AirTerminalSingleDuctConstantVolumeCooledBeam(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:CooledBeam`
        Central air system terminal unit, single duct, constant volume, with cooled beam
        (active or passive).
    
    """
    internal_name = "AirTerminal:SingleDuct:ConstantVolume:CooledBeam"
    field_count = 23
    required_fields = ["Name", "Cooled Beam Type", "Supply Air Inlet Node Name", "Supply Air Outlet Node Name", "Chilled Water Inlet Node Name", "Chilled Water Outlet Node Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `cooled_beam_type`

        Args:
            value (str): value for IDD Field `cooled_beam_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooled_beam_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooled_beam_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooled_beam_type`')
            vals = {}
            vals["active"] = "Active"
            vals["passive"] = "Passive"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `cooled_beam_type`'.format(value))
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
        """  Corresponds to IDD Field `supply_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `supply_air_outlet_node_name`

        Args:
            value (str): value for IDD Field `supply_air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_outlet_node_name`')

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
        """  Corresponds to IDD Field `chilled_water_inlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chilled_water_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `chilled_water_inlet_node_name`')

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
        """  Corresponds to IDD Field `chilled_water_outlet_node_name`

        Args:
            value (str): value for IDD Field `chilled_water_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `chilled_water_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chilled_water_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `chilled_water_outlet_node_name`')

        self._data["Chilled Water Outlet Node Name"] = value

    @property
    def supply_air_volumetric_flow_rate(self):
        """Get supply_air_volumetric_flow_rate

        Returns:
            float: the value of `supply_air_volumetric_flow_rate` or None if not set
        """
        return self._data["Supply Air Volumetric Flow Rate"]

    @supply_air_volumetric_flow_rate.setter
    def supply_air_volumetric_flow_rate(self, value=None):
        """  Corresponds to IDD Field `supply_air_volumetric_flow_rate`

        Args:
            value (float): value for IDD Field `supply_air_volumetric_flow_rate`
                Units: m3/s
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
                                 'for field `supply_air_volumetric_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_volumetric_flow_rate`')

        self._data["Supply Air Volumetric Flow Rate"] = value

    @property
    def maximum_total_chilled_water_volumetric_flow_rate(self):
        """Get maximum_total_chilled_water_volumetric_flow_rate

        Returns:
            float: the value of `maximum_total_chilled_water_volumetric_flow_rate` or None if not set
        """
        return self._data["Maximum Total Chilled Water Volumetric Flow Rate"]

    @maximum_total_chilled_water_volumetric_flow_rate.setter
    def maximum_total_chilled_water_volumetric_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_total_chilled_water_volumetric_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_total_chilled_water_volumetric_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_total_chilled_water_volumetric_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_total_chilled_water_volumetric_flow_rate`')

        self._data["Maximum Total Chilled Water Volumetric Flow Rate"] = value

    @property
    def number_of_beams(self):
        """Get number_of_beams

        Returns:
            int: the value of `number_of_beams` or None if not set
        """
        return self._data["Number of Beams"]

    @number_of_beams.setter
    def number_of_beams(self, value=None):
        """  Corresponds to IDD Field `number_of_beams`
        Number of individual beam units in the zone

        Args:
            value (int): value for IDD Field `number_of_beams`
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
                                 'for field `number_of_beams`'.format(value))
            if value <= 0:
                raise ValueError('value need to be greater 0 '
                                 'for field `number_of_beams`')

        self._data["Number of Beams"] = value

    @property
    def beam_length(self):
        """Get beam_length

        Returns:
            float: the value of `beam_length` or None if not set
        """
        return self._data["Beam Length"]

    @beam_length.setter
    def beam_length(self, value=None):
        """  Corresponds to IDD Field `beam_length`
        Length of an individual beam unit

        Args:
            value (float): value for IDD Field `beam_length`
                Units: m
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
                                 'for field `beam_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `beam_length`')

        self._data["Beam Length"] = value

    @property
    def design_inlet_water_temperature(self):
        """Get design_inlet_water_temperature

        Returns:
            float: the value of `design_inlet_water_temperature` or None if not set
        """
        return self._data["Design Inlet Water Temperature"]

    @design_inlet_water_temperature.setter
    def design_inlet_water_temperature(self, value=15.0 ):
        """  Corresponds to IDD Field `design_inlet_water_temperature`

        Args:
            value (float): value for IDD Field `design_inlet_water_temperature`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_inlet_water_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_inlet_water_temperature`')

        self._data["Design Inlet Water Temperature"] = value

    @property
    def design_outlet_water_temperature(self):
        """Get design_outlet_water_temperature

        Returns:
            float: the value of `design_outlet_water_temperature` or None if not set
        """
        return self._data["Design Outlet Water Temperature"]

    @design_outlet_water_temperature.setter
    def design_outlet_water_temperature(self, value=17.0 ):
        """  Corresponds to IDD Field `design_outlet_water_temperature`

        Args:
            value (float): value for IDD Field `design_outlet_water_temperature`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_outlet_water_temperature`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_outlet_water_temperature`')

        self._data["Design Outlet Water Temperature"] = value

    @property
    def coil_surface_area_per_coil_length(self):
        """Get coil_surface_area_per_coil_length

        Returns:
            float: the value of `coil_surface_area_per_coil_length` or None if not set
        """
        return self._data["Coil Surface Area per Coil Length"]

    @coil_surface_area_per_coil_length.setter
    def coil_surface_area_per_coil_length(self, value=5.422 ):
        """  Corresponds to IDD Field `coil_surface_area_per_coil_length`

        Args:
            value (float): value for IDD Field `coil_surface_area_per_coil_length`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coil_surface_area_per_coil_length`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `coil_surface_area_per_coil_length`')

        self._data["Coil Surface Area per Coil Length"] = value

    @property
    def model_parameter_a(self):
        """Get model_parameter_a

        Returns:
            float: the value of `model_parameter_a` or None if not set
        """
        return self._data["Model Parameter a"]

    @model_parameter_a.setter
    def model_parameter_a(self, value=15.3 ):
        """  Corresponds to IDD Field `model_parameter_a`

        Args:
            value (float): value for IDD Field `model_parameter_a`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_a`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_a`')

        self._data["Model Parameter a"] = value

    @property
    def model_parameter_n1(self):
        """Get model_parameter_n1

        Returns:
            float: the value of `model_parameter_n1` or None if not set
        """
        return self._data["Model Parameter n1"]

    @model_parameter_n1.setter
    def model_parameter_n1(self, value=0.0 ):
        """  Corresponds to IDD Field `model_parameter_n1`

        Args:
            value (float): value for IDD Field `model_parameter_n1`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_n1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_n1`')

        self._data["Model Parameter n1"] = value

    @property
    def model_parameter_n2(self):
        """Get model_parameter_n2

        Returns:
            float: the value of `model_parameter_n2` or None if not set
        """
        return self._data["Model Parameter n2"]

    @model_parameter_n2.setter
    def model_parameter_n2(self, value=0.84 ):
        """  Corresponds to IDD Field `model_parameter_n2`

        Args:
            value (float): value for IDD Field `model_parameter_n2`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_n2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_n2`')

        self._data["Model Parameter n2"] = value

    @property
    def model_parameter_n3(self):
        """Get model_parameter_n3

        Returns:
            float: the value of `model_parameter_n3` or None if not set
        """
        return self._data["Model Parameter n3"]

    @model_parameter_n3.setter
    def model_parameter_n3(self, value=0.12 ):
        """  Corresponds to IDD Field `model_parameter_n3`

        Args:
            value (float): value for IDD Field `model_parameter_n3`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_n3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_n3`')

        self._data["Model Parameter n3"] = value

    @property
    def model_parameter_a0(self):
        """Get model_parameter_a0

        Returns:
            float: the value of `model_parameter_a0` or None if not set
        """
        return self._data["Model Parameter a0"]

    @model_parameter_a0.setter
    def model_parameter_a0(self, value=0.171 ):
        """  Corresponds to IDD Field `model_parameter_a0`
        Free area of the coil in plan view per unit beam length

        Args:
            value (float): value for IDD Field `model_parameter_a0`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_a0`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_a0`')

        self._data["Model Parameter a0"] = value

    @property
    def model_parameter_k1(self):
        """Get model_parameter_k1

        Returns:
            float: the value of `model_parameter_k1` or None if not set
        """
        return self._data["Model Parameter K1"]

    @model_parameter_k1.setter
    def model_parameter_k1(self, value=0.0057 ):
        """  Corresponds to IDD Field `model_parameter_k1`

        Args:
            value (float): value for IDD Field `model_parameter_k1`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_k1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_k1`')

        self._data["Model Parameter K1"] = value

    @property
    def model_parameter_n(self):
        """Get model_parameter_n

        Returns:
            float: the value of `model_parameter_n` or None if not set
        """
        return self._data["Model Parameter n"]

    @model_parameter_n.setter
    def model_parameter_n(self, value=0.4 ):
        """  Corresponds to IDD Field `model_parameter_n`

        Args:
            value (float): value for IDD Field `model_parameter_n`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `model_parameter_n`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `model_parameter_n`')

        self._data["Model Parameter n"] = value

    @property
    def coefficient_of_induction_kin(self):
        """Get coefficient_of_induction_kin

        Returns:
            float: the value of `coefficient_of_induction_kin` or None if not set
        """
        return self._data["Coefficient of Induction Kin"]

    @coefficient_of_induction_kin.setter
    def coefficient_of_induction_kin(self, value=None):
        """  Corresponds to IDD Field `coefficient_of_induction_kin`

        Args:
            value (float): value for IDD Field `coefficient_of_induction_kin`
                value >= 0.0
                value <= 4.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_of_induction_kin`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `coefficient_of_induction_kin`')
            if value > 4.0:
                raise ValueError('value need to be smaller 4.0 '
                                 'for field `coefficient_of_induction_kin`')

        self._data["Coefficient of Induction Kin"] = value

    @property
    def leaving_pipe_inside_diameter(self):
        """Get leaving_pipe_inside_diameter

        Returns:
            float: the value of `leaving_pipe_inside_diameter` or None if not set
        """
        return self._data["Leaving Pipe Inside Diameter"]

    @leaving_pipe_inside_diameter.setter
    def leaving_pipe_inside_diameter(self, value=0.0145 ):
        """  Corresponds to IDD Field `leaving_pipe_inside_diameter`

        Args:
            value (float): value for IDD Field `leaving_pipe_inside_diameter`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `leaving_pipe_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `leaving_pipe_inside_diameter`')

        self._data["Leaving Pipe Inside Diameter"] = value

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

class AirTerminalSingleDuctInletSideMixer(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:InletSideMixer`
        Mix 2 inlet air streams into one outlet stream.
    
    """
    internal_name = "AirTerminal:SingleDuct:InletSideMixer"
    field_count = 6
    required_fields = ["Name", "ZoneHVAC Terminal Unit Object Type", "ZoneHVAC Terminal Unit Name", "Terminal Unit Outlet Node Name", "Terminal Unit Primary Air Inlet Node Name", "Terminal Unit Secondary Air Inlet Node Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `zonehvac_terminal_unit_object_type`

        Args:
            value (str): value for IDD Field `zonehvac_terminal_unit_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zonehvac_terminal_unit_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zonehvac_terminal_unit_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zonehvac_terminal_unit_object_type`')

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
        """  Corresponds to IDD Field `zonehvac_terminal_unit_name`

        Args:
            value (str): value for IDD Field `zonehvac_terminal_unit_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zonehvac_terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zonehvac_terminal_unit_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zonehvac_terminal_unit_name`')

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
        """  Corresponds to IDD Field `terminal_unit_outlet_node_name`

        Args:
            value (str): value for IDD Field `terminal_unit_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_outlet_node_name`')

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
        """  Corresponds to IDD Field `terminal_unit_primary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `terminal_unit_primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_primary_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `terminal_unit_secondary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `terminal_unit_secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_secondary_air_inlet_node_name`')

        self._data["Terminal Unit Secondary Air Inlet Node Name"] = value

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

class AirTerminalSingleDuctSupplySideMixer(object):
    """ Corresponds to IDD object `AirTerminal:SingleDuct:SupplySideMixer`
        Mix 2 inlet air streams into one outlet stream.
    
    """
    internal_name = "AirTerminal:SingleDuct:SupplySideMixer"
    field_count = 6
    required_fields = ["Name", "ZoneHVAC Terminal Unit Object Type", "ZoneHVAC Terminal Unit Name", "Terminal Unit Outlet Node Name", "Terminal Unit Primary Air Inlet Node Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `zonehvac_terminal_unit_object_type`

        Args:
            value (str): value for IDD Field `zonehvac_terminal_unit_object_type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zonehvac_terminal_unit_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zonehvac_terminal_unit_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zonehvac_terminal_unit_object_type`')

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
        """  Corresponds to IDD Field `zonehvac_terminal_unit_name`

        Args:
            value (str): value for IDD Field `zonehvac_terminal_unit_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zonehvac_terminal_unit_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zonehvac_terminal_unit_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zonehvac_terminal_unit_name`')

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
        """  Corresponds to IDD Field `terminal_unit_outlet_node_name`

        Args:
            value (str): value for IDD Field `terminal_unit_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_outlet_node_name`')

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
        """  Corresponds to IDD Field `terminal_unit_primary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `terminal_unit_primary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_primary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_primary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_primary_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `terminal_unit_secondary_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `terminal_unit_secondary_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `terminal_unit_secondary_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `terminal_unit_secondary_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `terminal_unit_secondary_air_inlet_node_name`')

        self._data["Terminal Unit Secondary Air Inlet Node Name"] = value

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

class AirTerminalDualDuctConstantVolume(object):
    """ Corresponds to IDD object `AirTerminal:DualDuct:ConstantVolume`
        Central air system terminal unit, dual duct, constant volume.
    
    """
    internal_name = "AirTerminal:DualDuct:ConstantVolume"
    field_count = 6
    required_fields = ["Name", "Air Outlet Node Name", "Hot Air Inlet Node Name", "Cold Air Inlet Node Name", "Maximum Air Flow Rate"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `hot_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `cold_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `cold_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cold_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_air_flow_rate`')

        self._data["Maximum Air Flow Rate"] = value

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

class AirTerminalDualDuctVav(object):
    """ Corresponds to IDD object `AirTerminal:DualDuct:VAV`
        Central air system terminal unit, dual duct, variable volume.
    
    """
    internal_name = "AirTerminal:DualDuct:VAV"
    field_count = 8
    required_fields = ["Name", "Air Outlet Node Name", "Hot Air Inlet Node Name", "Cold Air Inlet Node Name", "Maximum Damper Air Flow Rate", "Zone Minimum Air Flow Fraction"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `hot_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `hot_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `hot_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `hot_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `hot_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `cold_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `cold_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cold_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cold_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cold_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_damper_air_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_damper_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_damper_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_damper_air_flow_rate`')

        self._data["Maximum Damper Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """Get zone_minimum_air_flow_fraction

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=0.2 ):
        """  Corresponds to IDD Field `zone_minimum_air_flow_fraction`
        fraction of maximum air flow

        Args:
            value (float): value for IDD Field `zone_minimum_air_flow_fraction`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_minimum_air_flow_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `zone_minimum_air_flow_fraction`')

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
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based on the current number of occupants in the zone.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name`')

        self._data["Design Specification Outdoor Air Object Name"] = value

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

class AirTerminalDualDuctVavOutdoorAir(object):
    """ Corresponds to IDD object `AirTerminal:DualDuct:VAV:OutdoorAir`
        Central air system terminal unit, dual duct, variable volume with special controls.
        One VAV duct is controlled to supply ventilation air and the other VAV duct is
        controlled to meet the zone cooling load.
    
    """
    internal_name = "AirTerminal:DualDuct:VAV:OutdoorAir"
    field_count = 8
    required_fields = ["Name", "Air Outlet Node Name", "Outdoor Air Inlet Node Name", "Maximum Terminal Air Flow Rate", "Design Specification Outdoor Air Object Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

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
        """  Corresponds to IDD Field `air_outlet_node_name`
        The outlet node of the terminal unit.
        This is also the zone inlet node.

        Args:
            value (str): value for IDD Field `air_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_outlet_node_name`')

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
        """  Corresponds to IDD Field `outdoor_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `outdoor_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `recirculated_air_inlet_node_name`

        Args:
            value (str): value for IDD Field `recirculated_air_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `recirculated_air_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `recirculated_air_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `recirculated_air_inlet_node_name`')

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
        """  Corresponds to IDD Field `maximum_terminal_air_flow_rate`
        If autosized this is the sum of flow needed for cooling and maximum required outdoor air

        Args:
            value (float): value for IDD Field `maximum_terminal_air_flow_rate`
                Units: m3/s
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
                                 'for field `maximum_terminal_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_terminal_air_flow_rate`')

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
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name`
        When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        unit will increase flow as needed to meet this outdoor air requirement.
        If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        be computed based mode selected in the next field.
        At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name`')

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
        """  Corresponds to IDD Field `per_person_ventilation_rate_mode`
        CurrentOccupancy models demand controlled ventilation using the current number of people
        DesignOccupancy uses the total Number of People in the zone and is constant

        Args:
            value (str): value for IDD Field `per_person_ventilation_rate_mode`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `per_person_ventilation_rate_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `per_person_ventilation_rate_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `per_person_ventilation_rate_mode`')
            vals = {}
            vals["currentoccupancy"] = "CurrentOccupancy"
            vals["designoccupancy"] = "DesignOccupancy"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `per_person_ventilation_rate_mode`'.format(value))
            value = vals[value_lower]

        self._data["Per Person Ventilation Rate Mode"] = value

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

class ZoneHvacAirDistributionUnit(object):
    """ Corresponds to IDD object `ZoneHVAC:AirDistributionUnit`
        Central air system air distribution unit, serves as a wrapper for a specific type of
        air terminal unit. This object is referenced in a ZoneHVAC:EquipmentList.
    
    """
    internal_name = "ZoneHVAC:AirDistributionUnit"
    field_count = 6
    required_fields = ["Name", "Air Distribution Unit Outlet Node Name", "Air Terminal Object Type", "Air Terminal Name"]

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
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

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
        """  Corresponds to IDD Field `air_distribution_unit_outlet_node_name`

        Args:
            value (str): value for IDD Field `air_distribution_unit_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_distribution_unit_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_distribution_unit_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_distribution_unit_outlet_node_name`')

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
        """  Corresponds to IDD Field `air_terminal_object_type`

        Args:
            value (str): value for IDD Field `air_terminal_object_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_terminal_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_terminal_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_terminal_object_type`')
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
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `air_terminal_object_type`'.format(value))
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
        """  Corresponds to IDD Field `air_terminal_name`

        Args:
            value (str): value for IDD Field `air_terminal_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_terminal_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_terminal_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_terminal_name`')

        self._data["Air Terminal Name"] = value

    @property
    def nominal_upstream_leakage_fraction(self):
        """Get nominal_upstream_leakage_fraction

        Returns:
            float: the value of `nominal_upstream_leakage_fraction` or None if not set
        """
        return self._data["Nominal Upstream Leakage Fraction"]

    @nominal_upstream_leakage_fraction.setter
    def nominal_upstream_leakage_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `nominal_upstream_leakage_fraction`
        fraction at system design Flow; leakage Flow constant, leakage fraction
        varies with variable system Flow Rate.

        Args:
            value (float): value for IDD Field `nominal_upstream_leakage_fraction`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `nominal_upstream_leakage_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_upstream_leakage_fraction`')
            if value > 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `nominal_upstream_leakage_fraction`')

        self._data["Nominal Upstream Leakage Fraction"] = value

    @property
    def constant_downstream_leakage_fraction(self):
        """Get constant_downstream_leakage_fraction

        Returns:
            float: the value of `constant_downstream_leakage_fraction` or None if not set
        """
        return self._data["Constant Downstream Leakage Fraction"]

    @constant_downstream_leakage_fraction.setter
    def constant_downstream_leakage_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `constant_downstream_leakage_fraction`

        Args:
            value (float): value for IDD Field `constant_downstream_leakage_fraction`
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
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `constant_downstream_leakage_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `constant_downstream_leakage_fraction`')
            if value > 0.3:
                raise ValueError('value need to be smaller 0.3 '
                                 'for field `constant_downstream_leakage_fraction`')

        self._data["Constant Downstream Leakage Fraction"] = value

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