from collections import OrderedDict

class RoomAirModelType(object):
    """ Corresponds to IDD object `RoomAirModelType`
        Selects the type of room air model to be used in a given zone. If no RoomAirModelType
        object is specified then the default Mixing model (all zone air at the same
        temperature) will be used.
    
    """
    internal_name = "RoomAirModelType"
    field_count = 4
    required_fields = ["Name", "Zone Name", "Room-Air Modeling Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAirModelType`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Room-Air Modeling Type"] = None
        self._data["Air Temperature Coupling Strategy"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.roomair_modeling_type = None
        else:
            self.roomair_modeling_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.air_temperature_coupling_strategy = None
        else:
            self.air_temperature_coupling_strategy = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        
        {u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def roomair_modeling_type(self):
        """Get roomair_modeling_type

        Returns:
            str: the value of `roomair_modeling_type` or None if not set
        """
        return self._data["Room-Air Modeling Type"]

    @roomair_modeling_type.setter
    def roomair_modeling_type(self, value="Mixing"):
        """  Corresponds to IDD Field `Room-Air Modeling Type`
        Complete mixing air model
        UserDefined Room Air Temperature Patterns
        needs RoomAir:TemperaturePattern:UserDefined object referencing this Zone
        Mundt roomair model for displacement ventilation with single floor air node
        needs RoomAirSettings:OneNodeDisplacementVentilation object referencing this Zone
        (UCSD three-node displacement ventilation model)
        needs RoomAirSettings:ThreeNodeDisplacementVentilation object referencing this Zone
        (UCSD two-zone cross ventilation model)
        needs RoomAirSettings:CrossVentilation object referencing this Zone
        2-Node UFAD model for interior zones
        needs RoomAirSettings:UnderFloorAirDistributionInterior object referencing this Zone
        (2-Node UFAD model for exterior zones)
        needs RoomAirSettings:UnderFloorAirDistributionExterior object referencing this Zone
        
        {'pytype': 'str', u'default': u'Mixing', u'required-field': True, u'note': [u'Complete mixing air model', u'UserDefined Room Air Temperature Patterns', u'needs RoomAir:TemperaturePattern:UserDefined object referencing this Zone', u'Mundt roomair model for displacement ventilation with single floor air node', u'needs RoomAirSettings:OneNodeDisplacementVentilation object referencing this Zone', u'(UCSD three-node displacement ventilation model)', u'needs RoomAirSettings:ThreeNodeDisplacementVentilation object referencing this Zone', u'(UCSD two-zone cross ventilation model)', u'needs RoomAirSettings:CrossVentilation object referencing this Zone', u'2-Node UFAD model for interior zones', u'needs RoomAirSettings:UnderFloorAirDistributionInterior object referencing this Zone', u'(2-Node UFAD model for exterior zones)', u'needs RoomAirSettings:UnderFloorAirDistributionExterior object referencing this Zone'], u'key': [u'Mixing', u'UserDefined', u'OneNodeDisplacementVentilation', u'ThreeNodeDisplacementVentilation', u'CrossVentilation', u'UnderFloorAirDistributionInterior', u'UnderFloorAirDistributionExterior'], u'type': u'choice'}

        Args:
            value (str): value for IDD Field `Room-Air Modeling Type`
                Accepted values are:
                      - Mixing
                      - UserDefined
                      - OneNodeDisplacementVentilation
                      - ThreeNodeDisplacementVentilation
                      - CrossVentilation
                      - UnderFloorAirDistributionInterior
                      - UnderFloorAirDistributionExterior
                Default value: Mixing
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `roomair_modeling_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roomair_modeling_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `roomair_modeling_type`')
            vals = {}
            vals["mixing"] = "Mixing"
            vals["userdefined"] = "UserDefined"
            vals["onenodedisplacementventilation"] = "OneNodeDisplacementVentilation"
            vals["threenodedisplacementventilation"] = "ThreeNodeDisplacementVentilation"
            vals["crossventilation"] = "CrossVentilation"
            vals["underfloorairdistributioninterior"] = "UnderFloorAirDistributionInterior"
            vals["underfloorairdistributionexterior"] = "UnderFloorAirDistributionExterior"
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
                                     'field `roomair_modeling_type`'.format(value))
            value = vals[value_lower]
        self._data["Room-Air Modeling Type"] = value

    @property
    def air_temperature_coupling_strategy(self):
        """Get air_temperature_coupling_strategy

        Returns:
            str: the value of `air_temperature_coupling_strategy` or None if not set
        """
        return self._data["Air Temperature Coupling Strategy"]

    @air_temperature_coupling_strategy.setter
    def air_temperature_coupling_strategy(self, value="Direct"):
        """  Corresponds to IDD Field `Air Temperature Coupling Strategy`
        
        {u'default': u'Direct', u'type': u'choice', u'key': [u'Direct', u'Indirect'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Air Temperature Coupling Strategy`
                Accepted values are:
                      - Direct
                      - Indirect
                Default value: Direct
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_temperature_coupling_strategy`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_temperature_coupling_strategy`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `air_temperature_coupling_strategy`')
            vals = {}
            vals["direct"] = "Direct"
            vals["indirect"] = "Indirect"
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
                                     'field `air_temperature_coupling_strategy`'.format(value))
            value = vals[value_lower]
        self._data["Air Temperature Coupling Strategy"] = value

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

class RoomAirTemperaturePatternUserDefined(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:UserDefined`
        Used to explicitly define temperature patterns that are to be applied to the mean air
        temperature within a thermal zone.  Used with RoomAirModelType = UserDefined.
    
    """
    internal_name = "RoomAir:TemperaturePattern:UserDefined"
    field_count = 4
    required_fields = ["Name", "Zone Name", "Pattern Control Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAir:TemperaturePattern:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Pattern Control Schedule Name"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
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
            self.pattern_control_schedule_name = None
        else:
            self.pattern_control_schedule_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        
        {u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

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
        Availability schedule name for this model. Schedule value > 0 means the model is
        active. Schedule value = 0 means the model is inactive and the zone will be modeled
        as fully mixed (Mixing). If this field is blank, the model is always active.
        
        {u'note': [u'Availability schedule name for this model. Schedule value > 0 means the model is', u'active. Schedule value = 0 means the model is inactive and the zone will be modeled', u'as fully mixed (Mixing). If this field is blank, the model is always active.'], u'type': u'object-list', u'object-list': u'ScheduleNames', 'pytype': 'str'}

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
    def pattern_control_schedule_name(self):
        """Get pattern_control_schedule_name

        Returns:
            str: the value of `pattern_control_schedule_name` or None if not set
        """
        return self._data["Pattern Control Schedule Name"]

    @pattern_control_schedule_name.setter
    def pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Pattern Control Schedule Name`
        The schedule should contain integer values that
        correspond to unique Control Integer fields in
        one of the RoomAir:TemperaturePattern:* objects.
        
        {u'note': [u'The schedule should contain integer values that', u'correspond to unique Control Integer fields in', u'one of the RoomAir:TemperaturePattern:* objects.'], u'type': u'object-list', u'object-list': u'ScheduleNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `pattern_control_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `pattern_control_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `pattern_control_schedule_name`')
        self._data["Pattern Control Schedule Name"] = value

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

class RoomAirTemperaturePatternConstantGradient(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:ConstantGradient`
        Used to model room air with a fixed temperature gradient in the vertical direction.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    
    """
    internal_name = "RoomAir:TemperaturePattern:ConstantGradient"
    field_count = 6
    required_fields = ["Name", "Control Integer for Pattern Control Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAir:TemperaturePattern:ConstantGradient`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Offset"] = None
        self._data["Return Air Offset"] = None
        self._data["Exhaust Air Offset"] = None
        self._data["Temperature Gradient"] = None
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
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_offset = None
        else:
            self.thermostat_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_offset = None
        else:
            self.return_air_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_offset = None
        else:
            self.exhaust_air_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_gradient = None
        else:
            self.temperature_gradient = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        reference this entry in Schedule Name
        
        {u'note': [u'reference this entry in Schedule Name'], u'type': u'integer', u'required-field': True, 'pytype': 'int'}

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))
        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self._data["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `Thermostat Offset`
        = (Temp at thermostat- Mean Air Temp)
        
        {u'note': [u'= (Temp at thermostat- Mean Air Temp)'], u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Thermostat Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_offset`'.format(value))
        self._data["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self._data["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `Return Air Offset`
        = (Tleaving - Mean Air Temp )
        
        {u'note': [u'= (Tleaving - Mean Air Temp )'], u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Return Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_offset`'.format(value))
        self._data["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self._data["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Offset`
        = (Texhaust - Mean Air Temp) deg C
        
        {u'note': [u'= (Texhaust - Mean Air Temp) deg C'], u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Exhaust Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_offset`'.format(value))
        self._data["Exhaust Air Offset"] = value

    @property
    def temperature_gradient(self):
        """Get temperature_gradient

        Returns:
            float: the value of `temperature_gradient` or None if not set
        """
        return self._data["Temperature Gradient"]

    @temperature_gradient.setter
    def temperature_gradient(self, value=None):
        """  Corresponds to IDD Field `Temperature Gradient`
        Slope of temperature change in vertical direction
        
        {u'note': [u'Slope of temperature change in vertical direction'], u'units': u'K/m', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Temperature Gradient`
                Units: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_gradient`'.format(value))
        self._data["Temperature Gradient"] = value

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

class RoomAirTemperaturePatternTwoGradient(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:TwoGradient`
        Used to model room air with two temperature gradients in the vertical direction.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    
    """
    internal_name = "RoomAir:TemperaturePattern:TwoGradient"
    field_count = 12
    required_fields = ["Name", "Control Integer for Pattern Control Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAir:TemperaturePattern:TwoGradient`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Height"] = None
        self._data["Return Air Height"] = None
        self._data["Exhaust Air Height"] = None
        self._data["Temperature Gradient Lower Bound"] = None
        self._data["Temperature Gradient Upper  Bound"] = None
        self._data["Gradient Interpolation Mode"] = None
        self._data["Upper Temperature Bound"] = None
        self._data["Lower Temperature Bound"] = None
        self._data["Upper Heat Rate Bound"] = None
        self._data["Lower Heat Rate Bound"] = None
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
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_height = None
        else:
            self.return_air_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_height = None
        else:
            self.exhaust_air_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_gradient_lower_bound = None
        else:
            self.temperature_gradient_lower_bound = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_gradient_upper_bound = None
        else:
            self.temperature_gradient_upper_bound = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gradient_interpolation_mode = None
        else:
            self.gradient_interpolation_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.upper_temperature_bound = None
        else:
            self.upper_temperature_bound = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lower_temperature_bound = None
        else:
            self.lower_temperature_bound = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.upper_heat_rate_bound = None
        else:
            self.upper_heat_rate_bound = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.lower_heat_rate_bound = None
        else:
            self.lower_heat_rate_bound = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        reference this entry in Schedule Name
        
        {u'note': [u'reference this entry in Schedule Name'], u'type': u'integer', u'required-field': True, 'pytype': 'int'}

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))
        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=None):
        """  Corresponds to IDD Field `Thermostat Height`
        = Distance from floor of zone
        
        {u'note': [u'= Distance from floor of zone'], u'units': u'm', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_height`'.format(value))
        self._data["Thermostat Height"] = value

    @property
    def return_air_height(self):
        """Get return_air_height

        Returns:
            float: the value of `return_air_height` or None if not set
        """
        return self._data["Return Air Height"]

    @return_air_height.setter
    def return_air_height(self, value=None):
        """  Corresponds to IDD Field `Return Air Height`
        = Distance from floor of zone
        
        {u'note': [u'= Distance from floor of zone'], u'units': u'm', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Return Air Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_height`'.format(value))
        self._data["Return Air Height"] = value

    @property
    def exhaust_air_height(self):
        """Get exhaust_air_height

        Returns:
            float: the value of `exhaust_air_height` or None if not set
        """
        return self._data["Exhaust Air Height"]

    @exhaust_air_height.setter
    def exhaust_air_height(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Height`
        = Distance from floor of zone
        
        {u'note': [u'= Distance from floor of zone'], u'units': u'm', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Exhaust Air Height`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_height`'.format(value))
        self._data["Exhaust Air Height"] = value

    @property
    def temperature_gradient_lower_bound(self):
        """Get temperature_gradient_lower_bound

        Returns:
            float: the value of `temperature_gradient_lower_bound` or None if not set
        """
        return self._data["Temperature Gradient Lower Bound"]

    @temperature_gradient_lower_bound.setter
    def temperature_gradient_lower_bound(self, value=None):
        """  Corresponds to IDD Field `Temperature Gradient Lower Bound`
        Slope of temperature change in vertical direction
        
        {u'note': [u'Slope of temperature change in vertical direction'], u'units': u'K/m', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Temperature Gradient Lower Bound`
                Units: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_gradient_lower_bound`'.format(value))
        self._data["Temperature Gradient Lower Bound"] = value

    @property
    def temperature_gradient_upper_bound(self):
        """Get temperature_gradient_upper_bound

        Returns:
            float: the value of `temperature_gradient_upper_bound` or None if not set
        """
        return self._data["Temperature Gradient Upper  Bound"]

    @temperature_gradient_upper_bound.setter
    def temperature_gradient_upper_bound(self, value=None):
        """  Corresponds to IDD Field `Temperature Gradient Upper  Bound`
        Slope of temperature change in vertical direction
        
        {u'note': [u'Slope of temperature change in vertical direction'], u'units': u'K/m', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Temperature Gradient Upper  Bound`
                Units: K/m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_gradient_upper_bound`'.format(value))
        self._data["Temperature Gradient Upper  Bound"] = value

    @property
    def gradient_interpolation_mode(self):
        """Get gradient_interpolation_mode

        Returns:
            str: the value of `gradient_interpolation_mode` or None if not set
        """
        return self._data["Gradient Interpolation Mode"]

    @gradient_interpolation_mode.setter
    def gradient_interpolation_mode(self, value=None):
        """  Corresponds to IDD Field `Gradient Interpolation Mode`
        
        {u'type': u'choice', u'key': [u'OutdoorDryBulbTemperature', u'ZoneDryBulbTemperature', u'ZoneAndOutdoorTemperatureDifference', u'SensibleCoolingLoad', u'SensibleHeatingLoad'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Gradient Interpolation Mode`
                Accepted values are:
                      - OutdoorDryBulbTemperature
                      - ZoneDryBulbTemperature
                      - ZoneAndOutdoorTemperatureDifference
                      - SensibleCoolingLoad
                      - SensibleHeatingLoad
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `gradient_interpolation_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gradient_interpolation_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `gradient_interpolation_mode`')
            vals = {}
            vals["outdoordrybulbtemperature"] = "OutdoorDryBulbTemperature"
            vals["zonedrybulbtemperature"] = "ZoneDryBulbTemperature"
            vals["zoneandoutdoortemperaturedifference"] = "ZoneAndOutdoorTemperatureDifference"
            vals["sensiblecoolingload"] = "SensibleCoolingLoad"
            vals["sensibleheatingload"] = "SensibleHeatingLoad"
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
                                     'field `gradient_interpolation_mode`'.format(value))
            value = vals[value_lower]
        self._data["Gradient Interpolation Mode"] = value

    @property
    def upper_temperature_bound(self):
        """Get upper_temperature_bound

        Returns:
            float: the value of `upper_temperature_bound` or None if not set
        """
        return self._data["Upper Temperature Bound"]

    @upper_temperature_bound.setter
    def upper_temperature_bound(self, value=None):
        """  Corresponds to IDD Field `Upper Temperature Bound`
        
        {u'units': u'C', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Upper Temperature Bound`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `upper_temperature_bound`'.format(value))
        self._data["Upper Temperature Bound"] = value

    @property
    def lower_temperature_bound(self):
        """Get lower_temperature_bound

        Returns:
            float: the value of `lower_temperature_bound` or None if not set
        """
        return self._data["Lower Temperature Bound"]

    @lower_temperature_bound.setter
    def lower_temperature_bound(self, value=None):
        """  Corresponds to IDD Field `Lower Temperature Bound`
        
        {u'units': u'C', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Lower Temperature Bound`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `lower_temperature_bound`'.format(value))
        self._data["Lower Temperature Bound"] = value

    @property
    def upper_heat_rate_bound(self):
        """Get upper_heat_rate_bound

        Returns:
            float: the value of `upper_heat_rate_bound` or None if not set
        """
        return self._data["Upper Heat Rate Bound"]

    @upper_heat_rate_bound.setter
    def upper_heat_rate_bound(self, value=None):
        """  Corresponds to IDD Field `Upper Heat Rate Bound`
        
        {u'units': u'W', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Upper Heat Rate Bound`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `upper_heat_rate_bound`'.format(value))
        self._data["Upper Heat Rate Bound"] = value

    @property
    def lower_heat_rate_bound(self):
        """Get lower_heat_rate_bound

        Returns:
            float: the value of `lower_heat_rate_bound` or None if not set
        """
        return self._data["Lower Heat Rate Bound"]

    @lower_heat_rate_bound.setter
    def lower_heat_rate_bound(self, value=None):
        """  Corresponds to IDD Field `Lower Heat Rate Bound`
        
        {u'units': u'W', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Lower Heat Rate Bound`
                Units: W
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `lower_heat_rate_bound`'.format(value))
        self._data["Lower Heat Rate Bound"] = value

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

class RoomAirTemperaturePatternNondimensionalHeight(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:NondimensionalHeight`
        Defines a distribution pattern for air temperatures relative to the current mean air
        temperature as a function of height. The height, referred to as Zeta, is non-dimensional
        by normalizing with the zone ceiling height.
        Used in combination with RoomAir:TemperaturePattern:UserDefined.
    
    """
    internal_name = "RoomAir:TemperaturePattern:NondimensionalHeight"
    field_count = 43
    required_fields = ["Name", "Control Integer for Pattern Control Schedule Name", "Pair 1 Zeta Nondimensional Height", "Pair 1 Delta Adjacent Air Temperature", "Pair 2 Zeta Nondimensional Height", "Pair 2 Delta Adjacent Air Temperature"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAir:TemperaturePattern:NondimensionalHeight`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Offset"] = None
        self._data["Return Air Offset"] = None
        self._data["Exhaust Air Offset"] = None
        self._data["Pair 1 Zeta Nondimensional Height"] = None
        self._data["Pair 1 Delta Adjacent Air Temperature"] = None
        self._data["Pair 2 Zeta Nondimensional Height"] = None
        self._data["Pair 2 Delta Adjacent Air Temperature"] = None
        self._data["Pair 3 Zeta Nondimensional Height"] = None
        self._data["Pair 3 Delta Adjacent Air Temperature"] = None
        self._data["Pair 4 Zeta Nondimensional Height"] = None
        self._data["Pair 4 Delta Adjacent Air Temperature"] = None
        self._data["Pair 5 Zeta Nondimensional Height"] = None
        self._data["Pair 5 Delta Adjacent Air Temperature"] = None
        self._data["Pair 6 Zeta Nondimensional Height"] = None
        self._data["Pair 6 Delta Adjacent Air Temperature"] = None
        self._data["Pair 7 Zeta Nondimensional Height"] = None
        self._data["Pair 7 Delta Adjacent Air Temperature"] = None
        self._data["Pair 8 Zeta Nondimensional Height"] = None
        self._data["Pair 8 Delta Adjacent Air Temperature"] = None
        self._data["Pair 9 Zeta Nondimensional Height"] = None
        self._data["Pair 9 Delta Adjacent Air Temperature"] = None
        self._data["Pair 10 Zeta Nondimensional Height"] = None
        self._data["Pair 10 Delta Adjacent Air Temperature"] = None
        self._data["Pair 11 Zeta Nondimensional Height"] = None
        self._data["Pair 11 Delta Adjacent Air Temperature"] = None
        self._data["Pair 12 Zeta Nondimensional Height"] = None
        self._data["Pair 12 Delta Adjacent Air Temperature"] = None
        self._data["Pair 13 Zeta Nondimensional Height"] = None
        self._data["Pair 13 Delta Adjacent Air Temperature"] = None
        self._data["Pair 14 Zeta Nondimensional Height"] = None
        self._data["Pair 14 Delta Adjacent Air Temperature"] = None
        self._data["Pair 15 Zeta Nondimensional Height"] = None
        self._data["Pair 15 Delta Adjacent Air Temperature"] = None
        self._data["Pair 16 Zeta Nondimensional Height"] = None
        self._data["Pair 16 Delta Adjacent Air Temperature"] = None
        self._data["Pair 17 Zeta Nondimensional Height"] = None
        self._data["Pair 17 Delta Adjacent Air Temperature"] = None
        self._data["Pair 18 Zeta Nondimensional Height"] = None
        self._data["Pair 18 Delta Adjacent Air Temperature"] = None
        self._data["Pair 19 Zeta Nondimensional Height"] = None
        self._data["Pair 19 Delta Adjacent Air Temperature"] = None
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
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_offset = None
        else:
            self.thermostat_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_offset = None
        else:
            self.return_air_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_offset = None
        else:
            self.exhaust_air_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_1_zeta_nondimensional_height = None
        else:
            self.pair_1_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_1_delta_adjacent_air_temperature = None
        else:
            self.pair_1_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_2_zeta_nondimensional_height = None
        else:
            self.pair_2_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_2_delta_adjacent_air_temperature = None
        else:
            self.pair_2_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_3_zeta_nondimensional_height = None
        else:
            self.pair_3_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_3_delta_adjacent_air_temperature = None
        else:
            self.pair_3_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_4_zeta_nondimensional_height = None
        else:
            self.pair_4_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_4_delta_adjacent_air_temperature = None
        else:
            self.pair_4_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_5_zeta_nondimensional_height = None
        else:
            self.pair_5_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_5_delta_adjacent_air_temperature = None
        else:
            self.pair_5_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_6_zeta_nondimensional_height = None
        else:
            self.pair_6_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_6_delta_adjacent_air_temperature = None
        else:
            self.pair_6_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_7_zeta_nondimensional_height = None
        else:
            self.pair_7_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_7_delta_adjacent_air_temperature = None
        else:
            self.pair_7_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_8_zeta_nondimensional_height = None
        else:
            self.pair_8_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_8_delta_adjacent_air_temperature = None
        else:
            self.pair_8_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_9_zeta_nondimensional_height = None
        else:
            self.pair_9_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_9_delta_adjacent_air_temperature = None
        else:
            self.pair_9_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_10_zeta_nondimensional_height = None
        else:
            self.pair_10_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_10_delta_adjacent_air_temperature = None
        else:
            self.pair_10_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_11_zeta_nondimensional_height = None
        else:
            self.pair_11_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_11_delta_adjacent_air_temperature = None
        else:
            self.pair_11_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_12_zeta_nondimensional_height = None
        else:
            self.pair_12_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_12_delta_adjacent_air_temperature = None
        else:
            self.pair_12_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_13_zeta_nondimensional_height = None
        else:
            self.pair_13_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_13_delta_adjacent_air_temperature = None
        else:
            self.pair_13_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_14_zeta_nondimensional_height = None
        else:
            self.pair_14_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_14_delta_adjacent_air_temperature = None
        else:
            self.pair_14_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_15_zeta_nondimensional_height = None
        else:
            self.pair_15_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_15_delta_adjacent_air_temperature = None
        else:
            self.pair_15_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_16_zeta_nondimensional_height = None
        else:
            self.pair_16_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_16_delta_adjacent_air_temperature = None
        else:
            self.pair_16_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_17_zeta_nondimensional_height = None
        else:
            self.pair_17_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_17_delta_adjacent_air_temperature = None
        else:
            self.pair_17_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_18_zeta_nondimensional_height = None
        else:
            self.pair_18_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_18_delta_adjacent_air_temperature = None
        else:
            self.pair_18_delta_adjacent_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_19_zeta_nondimensional_height = None
        else:
            self.pair_19_zeta_nondimensional_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.pair_19_delta_adjacent_air_temperature = None
        else:
            self.pair_19_delta_adjacent_air_temperature = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        this value should appear in as a schedule value
        
        {u'note': [u'this value should appear in as a schedule value'], u'type': u'integer', u'required-field': True, 'pytype': 'int'}

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))
        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self._data["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `Thermostat Offset`
        = (Temp at thermostat- Mean Air Temp)
        
        {u'note': [u'= (Temp at thermostat- Mean Air Temp)'], u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Thermostat Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_offset`'.format(value))
        self._data["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self._data["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `Return Air Offset`
        = (Temp leaving - Mean Air Temp ) deg C
        
        {u'note': [u'= (Temp leaving - Mean Air Temp ) deg C'], u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Return Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_offset`'.format(value))
        self._data["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self._data["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Offset`
        = (Temp exhaust - Mean Air Temp) deg C
        the remaining fields have pairs that describe the relative
        temperature pattern in the vertical direction of a zone
        Zeta is the nondimensional height (in z-direction). on [0..1]
        DeltaTai =  (Tai - MAT) in units of deg. C
        relative deg C on [-10.0 .. 20.0 ]
        
        {u'note': [u'= (Temp exhaust - Mean Air Temp) deg C', u'the remaining fields have pairs that describe the relative', u'temperature pattern in the vertical direction of a zone', u'Zeta is the nondimensional height (in z-direction). on [0..1]', u'DeltaTai =  (Tai - MAT) in units of deg. C', u'relative deg C on [-10.0 .. 20.0 ]'], u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Exhaust Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_offset`'.format(value))
        self._data["Exhaust Air Offset"] = value

    @property
    def pair_1_zeta_nondimensional_height(self):
        """Get pair_1_zeta_nondimensional_height

        Returns:
            float: the value of `pair_1_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 1 Zeta Nondimensional Height"]

    @pair_1_zeta_nondimensional_height.setter
    def pair_1_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 1 Zeta Nondimensional Height`
        
        {'pytype': 'float', u'type': u'real', u'required-field': True, u'begin-extensible': u''}

        Args:
            value (float): value for IDD Field `Pair 1 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_1_zeta_nondimensional_height`'.format(value))
        self._data["Pair 1 Zeta Nondimensional Height"] = value

    @property
    def pair_1_delta_adjacent_air_temperature(self):
        """Get pair_1_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_1_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 1 Delta Adjacent Air Temperature"]

    @pair_1_delta_adjacent_air_temperature.setter
    def pair_1_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 1 Delta Adjacent Air Temperature`
        
        {'pytype': 'float', u'maximum': '20.0', u'required-field': True, u'minimum': '-10.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Pair 1 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_1_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_1_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_1_delta_adjacent_air_temperature`')
        self._data["Pair 1 Delta Adjacent Air Temperature"] = value

    @property
    def pair_2_zeta_nondimensional_height(self):
        """Get pair_2_zeta_nondimensional_height

        Returns:
            float: the value of `pair_2_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 2 Zeta Nondimensional Height"]

    @pair_2_zeta_nondimensional_height.setter
    def pair_2_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 2 Zeta Nondimensional Height`
        
        {u'type': u'real', u'required-field': True, 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 2 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_2_zeta_nondimensional_height`'.format(value))
        self._data["Pair 2 Zeta Nondimensional Height"] = value

    @property
    def pair_2_delta_adjacent_air_temperature(self):
        """Get pair_2_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_2_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 2 Delta Adjacent Air Temperature"]

    @pair_2_delta_adjacent_air_temperature.setter
    def pair_2_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 2 Delta Adjacent Air Temperature`
        
        {'pytype': 'float', u'maximum': '20.0', u'required-field': True, u'minimum': '-10.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Pair 2 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_2_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_2_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_2_delta_adjacent_air_temperature`')
        self._data["Pair 2 Delta Adjacent Air Temperature"] = value

    @property
    def pair_3_zeta_nondimensional_height(self):
        """Get pair_3_zeta_nondimensional_height

        Returns:
            float: the value of `pair_3_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 3 Zeta Nondimensional Height"]

    @pair_3_zeta_nondimensional_height.setter
    def pair_3_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 3 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 3 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_3_zeta_nondimensional_height`'.format(value))
        self._data["Pair 3 Zeta Nondimensional Height"] = value

    @property
    def pair_3_delta_adjacent_air_temperature(self):
        """Get pair_3_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_3_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 3 Delta Adjacent Air Temperature"]

    @pair_3_delta_adjacent_air_temperature.setter
    def pair_3_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 3 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 3 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_3_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_3_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_3_delta_adjacent_air_temperature`')
        self._data["Pair 3 Delta Adjacent Air Temperature"] = value

    @property
    def pair_4_zeta_nondimensional_height(self):
        """Get pair_4_zeta_nondimensional_height

        Returns:
            float: the value of `pair_4_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 4 Zeta Nondimensional Height"]

    @pair_4_zeta_nondimensional_height.setter
    def pair_4_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 4 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 4 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_4_zeta_nondimensional_height`'.format(value))
        self._data["Pair 4 Zeta Nondimensional Height"] = value

    @property
    def pair_4_delta_adjacent_air_temperature(self):
        """Get pair_4_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_4_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 4 Delta Adjacent Air Temperature"]

    @pair_4_delta_adjacent_air_temperature.setter
    def pair_4_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 4 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 4 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_4_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_4_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_4_delta_adjacent_air_temperature`')
        self._data["Pair 4 Delta Adjacent Air Temperature"] = value

    @property
    def pair_5_zeta_nondimensional_height(self):
        """Get pair_5_zeta_nondimensional_height

        Returns:
            float: the value of `pair_5_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 5 Zeta Nondimensional Height"]

    @pair_5_zeta_nondimensional_height.setter
    def pair_5_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 5 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 5 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_5_zeta_nondimensional_height`'.format(value))
        self._data["Pair 5 Zeta Nondimensional Height"] = value

    @property
    def pair_5_delta_adjacent_air_temperature(self):
        """Get pair_5_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_5_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 5 Delta Adjacent Air Temperature"]

    @pair_5_delta_adjacent_air_temperature.setter
    def pair_5_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 5 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 5 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_5_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_5_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_5_delta_adjacent_air_temperature`')
        self._data["Pair 5 Delta Adjacent Air Temperature"] = value

    @property
    def pair_6_zeta_nondimensional_height(self):
        """Get pair_6_zeta_nondimensional_height

        Returns:
            float: the value of `pair_6_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 6 Zeta Nondimensional Height"]

    @pair_6_zeta_nondimensional_height.setter
    def pair_6_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 6 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 6 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_6_zeta_nondimensional_height`'.format(value))
        self._data["Pair 6 Zeta Nondimensional Height"] = value

    @property
    def pair_6_delta_adjacent_air_temperature(self):
        """Get pair_6_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_6_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 6 Delta Adjacent Air Temperature"]

    @pair_6_delta_adjacent_air_temperature.setter
    def pair_6_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 6 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 6 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_6_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_6_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_6_delta_adjacent_air_temperature`')
        self._data["Pair 6 Delta Adjacent Air Temperature"] = value

    @property
    def pair_7_zeta_nondimensional_height(self):
        """Get pair_7_zeta_nondimensional_height

        Returns:
            float: the value of `pair_7_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 7 Zeta Nondimensional Height"]

    @pair_7_zeta_nondimensional_height.setter
    def pair_7_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 7 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 7 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_7_zeta_nondimensional_height`'.format(value))
        self._data["Pair 7 Zeta Nondimensional Height"] = value

    @property
    def pair_7_delta_adjacent_air_temperature(self):
        """Get pair_7_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_7_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 7 Delta Adjacent Air Temperature"]

    @pair_7_delta_adjacent_air_temperature.setter
    def pair_7_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 7 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 7 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_7_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_7_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_7_delta_adjacent_air_temperature`')
        self._data["Pair 7 Delta Adjacent Air Temperature"] = value

    @property
    def pair_8_zeta_nondimensional_height(self):
        """Get pair_8_zeta_nondimensional_height

        Returns:
            float: the value of `pair_8_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 8 Zeta Nondimensional Height"]

    @pair_8_zeta_nondimensional_height.setter
    def pair_8_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 8 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 8 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_8_zeta_nondimensional_height`'.format(value))
        self._data["Pair 8 Zeta Nondimensional Height"] = value

    @property
    def pair_8_delta_adjacent_air_temperature(self):
        """Get pair_8_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_8_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 8 Delta Adjacent Air Temperature"]

    @pair_8_delta_adjacent_air_temperature.setter
    def pair_8_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 8 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 8 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_8_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_8_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_8_delta_adjacent_air_temperature`')
        self._data["Pair 8 Delta Adjacent Air Temperature"] = value

    @property
    def pair_9_zeta_nondimensional_height(self):
        """Get pair_9_zeta_nondimensional_height

        Returns:
            float: the value of `pair_9_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 9 Zeta Nondimensional Height"]

    @pair_9_zeta_nondimensional_height.setter
    def pair_9_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 9 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 9 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_9_zeta_nondimensional_height`'.format(value))
        self._data["Pair 9 Zeta Nondimensional Height"] = value

    @property
    def pair_9_delta_adjacent_air_temperature(self):
        """Get pair_9_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_9_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 9 Delta Adjacent Air Temperature"]

    @pair_9_delta_adjacent_air_temperature.setter
    def pair_9_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 9 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 9 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_9_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_9_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_9_delta_adjacent_air_temperature`')
        self._data["Pair 9 Delta Adjacent Air Temperature"] = value

    @property
    def pair_10_zeta_nondimensional_height(self):
        """Get pair_10_zeta_nondimensional_height

        Returns:
            float: the value of `pair_10_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 10 Zeta Nondimensional Height"]

    @pair_10_zeta_nondimensional_height.setter
    def pair_10_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 10 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 10 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_10_zeta_nondimensional_height`'.format(value))
        self._data["Pair 10 Zeta Nondimensional Height"] = value

    @property
    def pair_10_delta_adjacent_air_temperature(self):
        """Get pair_10_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_10_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 10 Delta Adjacent Air Temperature"]

    @pair_10_delta_adjacent_air_temperature.setter
    def pair_10_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 10 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 10 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_10_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_10_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_10_delta_adjacent_air_temperature`')
        self._data["Pair 10 Delta Adjacent Air Temperature"] = value

    @property
    def pair_11_zeta_nondimensional_height(self):
        """Get pair_11_zeta_nondimensional_height

        Returns:
            float: the value of `pair_11_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 11 Zeta Nondimensional Height"]

    @pair_11_zeta_nondimensional_height.setter
    def pair_11_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 11 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 11 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_11_zeta_nondimensional_height`'.format(value))
        self._data["Pair 11 Zeta Nondimensional Height"] = value

    @property
    def pair_11_delta_adjacent_air_temperature(self):
        """Get pair_11_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_11_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 11 Delta Adjacent Air Temperature"]

    @pair_11_delta_adjacent_air_temperature.setter
    def pair_11_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 11 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 11 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_11_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_11_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_11_delta_adjacent_air_temperature`')
        self._data["Pair 11 Delta Adjacent Air Temperature"] = value

    @property
    def pair_12_zeta_nondimensional_height(self):
        """Get pair_12_zeta_nondimensional_height

        Returns:
            float: the value of `pair_12_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 12 Zeta Nondimensional Height"]

    @pair_12_zeta_nondimensional_height.setter
    def pair_12_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 12 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 12 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_12_zeta_nondimensional_height`'.format(value))
        self._data["Pair 12 Zeta Nondimensional Height"] = value

    @property
    def pair_12_delta_adjacent_air_temperature(self):
        """Get pair_12_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_12_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 12 Delta Adjacent Air Temperature"]

    @pair_12_delta_adjacent_air_temperature.setter
    def pair_12_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 12 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 12 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_12_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_12_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_12_delta_adjacent_air_temperature`')
        self._data["Pair 12 Delta Adjacent Air Temperature"] = value

    @property
    def pair_13_zeta_nondimensional_height(self):
        """Get pair_13_zeta_nondimensional_height

        Returns:
            float: the value of `pair_13_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 13 Zeta Nondimensional Height"]

    @pair_13_zeta_nondimensional_height.setter
    def pair_13_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 13 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 13 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_13_zeta_nondimensional_height`'.format(value))
        self._data["Pair 13 Zeta Nondimensional Height"] = value

    @property
    def pair_13_delta_adjacent_air_temperature(self):
        """Get pair_13_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_13_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 13 Delta Adjacent Air Temperature"]

    @pair_13_delta_adjacent_air_temperature.setter
    def pair_13_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 13 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 13 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_13_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_13_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_13_delta_adjacent_air_temperature`')
        self._data["Pair 13 Delta Adjacent Air Temperature"] = value

    @property
    def pair_14_zeta_nondimensional_height(self):
        """Get pair_14_zeta_nondimensional_height

        Returns:
            float: the value of `pair_14_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 14 Zeta Nondimensional Height"]

    @pair_14_zeta_nondimensional_height.setter
    def pair_14_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 14 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 14 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_14_zeta_nondimensional_height`'.format(value))
        self._data["Pair 14 Zeta Nondimensional Height"] = value

    @property
    def pair_14_delta_adjacent_air_temperature(self):
        """Get pair_14_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_14_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 14 Delta Adjacent Air Temperature"]

    @pair_14_delta_adjacent_air_temperature.setter
    def pair_14_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 14 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 14 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_14_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_14_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_14_delta_adjacent_air_temperature`')
        self._data["Pair 14 Delta Adjacent Air Temperature"] = value

    @property
    def pair_15_zeta_nondimensional_height(self):
        """Get pair_15_zeta_nondimensional_height

        Returns:
            float: the value of `pair_15_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 15 Zeta Nondimensional Height"]

    @pair_15_zeta_nondimensional_height.setter
    def pair_15_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 15 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 15 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_15_zeta_nondimensional_height`'.format(value))
        self._data["Pair 15 Zeta Nondimensional Height"] = value

    @property
    def pair_15_delta_adjacent_air_temperature(self):
        """Get pair_15_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_15_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 15 Delta Adjacent Air Temperature"]

    @pair_15_delta_adjacent_air_temperature.setter
    def pair_15_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 15 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 15 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_15_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_15_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_15_delta_adjacent_air_temperature`')
        self._data["Pair 15 Delta Adjacent Air Temperature"] = value

    @property
    def pair_16_zeta_nondimensional_height(self):
        """Get pair_16_zeta_nondimensional_height

        Returns:
            float: the value of `pair_16_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 16 Zeta Nondimensional Height"]

    @pair_16_zeta_nondimensional_height.setter
    def pair_16_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 16 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 16 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_16_zeta_nondimensional_height`'.format(value))
        self._data["Pair 16 Zeta Nondimensional Height"] = value

    @property
    def pair_16_delta_adjacent_air_temperature(self):
        """Get pair_16_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_16_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 16 Delta Adjacent Air Temperature"]

    @pair_16_delta_adjacent_air_temperature.setter
    def pair_16_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 16 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 16 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_16_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_16_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_16_delta_adjacent_air_temperature`')
        self._data["Pair 16 Delta Adjacent Air Temperature"] = value

    @property
    def pair_17_zeta_nondimensional_height(self):
        """Get pair_17_zeta_nondimensional_height

        Returns:
            float: the value of `pair_17_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 17 Zeta Nondimensional Height"]

    @pair_17_zeta_nondimensional_height.setter
    def pair_17_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 17 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 17 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_17_zeta_nondimensional_height`'.format(value))
        self._data["Pair 17 Zeta Nondimensional Height"] = value

    @property
    def pair_17_delta_adjacent_air_temperature(self):
        """Get pair_17_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_17_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 17 Delta Adjacent Air Temperature"]

    @pair_17_delta_adjacent_air_temperature.setter
    def pair_17_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 17 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 17 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_17_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_17_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_17_delta_adjacent_air_temperature`')
        self._data["Pair 17 Delta Adjacent Air Temperature"] = value

    @property
    def pair_18_zeta_nondimensional_height(self):
        """Get pair_18_zeta_nondimensional_height

        Returns:
            float: the value of `pair_18_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 18 Zeta Nondimensional Height"]

    @pair_18_zeta_nondimensional_height.setter
    def pair_18_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 18 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 18 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_18_zeta_nondimensional_height`'.format(value))
        self._data["Pair 18 Zeta Nondimensional Height"] = value

    @property
    def pair_18_delta_adjacent_air_temperature(self):
        """Get pair_18_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_18_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 18 Delta Adjacent Air Temperature"]

    @pair_18_delta_adjacent_air_temperature.setter
    def pair_18_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 18 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 18 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_18_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_18_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_18_delta_adjacent_air_temperature`')
        self._data["Pair 18 Delta Adjacent Air Temperature"] = value

    @property
    def pair_19_zeta_nondimensional_height(self):
        """Get pair_19_zeta_nondimensional_height

        Returns:
            float: the value of `pair_19_zeta_nondimensional_height` or None if not set
        """
        return self._data["Pair 19 Zeta Nondimensional Height"]

    @pair_19_zeta_nondimensional_height.setter
    def pair_19_zeta_nondimensional_height(self, value=None):
        """  Corresponds to IDD Field `Pair 19 Zeta Nondimensional Height`
        
        {u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 19 Zeta Nondimensional Height`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_19_zeta_nondimensional_height`'.format(value))
        self._data["Pair 19 Zeta Nondimensional Height"] = value

    @property
    def pair_19_delta_adjacent_air_temperature(self):
        """Get pair_19_delta_adjacent_air_temperature

        Returns:
            float: the value of `pair_19_delta_adjacent_air_temperature` or None if not set
        """
        return self._data["Pair 19 Delta Adjacent Air Temperature"]

    @pair_19_delta_adjacent_air_temperature.setter
    def pair_19_delta_adjacent_air_temperature(self, value=None):
        """  Corresponds to IDD Field `Pair 19 Delta Adjacent Air Temperature`
        
        {u'units': u'deltaC', u'minimum': '-10.0', u'type': u'real', u'maximum': '20.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Pair 19 Delta Adjacent Air Temperature`
                Units: deltaC
                value >= -10.0
                value <= 20.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `pair_19_delta_adjacent_air_temperature`'.format(value))
            if value < -10.0:
                raise ValueError('value need to be greater or equal -10.0 '
                                 'for field `pair_19_delta_adjacent_air_temperature`')
            if value > 20.0:
                raise ValueError('value need to be smaller 20.0 '
                                 'for field `pair_19_delta_adjacent_air_temperature`')
        self._data["Pair 19 Delta Adjacent Air Temperature"] = value

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

class RoomAirTemperaturePatternSurfaceMapping(object):
    """ Corresponds to IDD object `RoomAir:TemperaturePattern:SurfaceMapping`
        Defines a distribution pattern for the air temperatures adjacent to individual surfaces.
        This allows controlling the adjacent air temperature on a surface-by-surface basis
        rather than by height. This allows modeling different adjacent air temperatures on
        the opposite sides of the zone. Used in combination with
        RoomAir:TemperaturePattern:UserDefined.
    
    """
    internal_name = "RoomAir:TemperaturePattern:SurfaceMapping"
    field_count = 47
    required_fields = ["Name", "Control Integer for Pattern Control Schedule Name", "Surface Name Pair 1", "Delta Adjacent Air Temperature Pair 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAir:TemperaturePattern:SurfaceMapping`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Integer for Pattern Control Schedule Name"] = None
        self._data["Thermostat Offset"] = None
        self._data["Return Air Offset"] = None
        self._data["Exhaust Air Offset"] = None
        self._data["Surface Name Pair 1"] = None
        self._data["Delta Adjacent Air Temperature Pair 1"] = None
        self._data["Surface Name Pair 2"] = None
        self._data["Delta Adjacent Air Temperature Pair 2"] = None
        self._data["Surface Name Pair 3"] = None
        self._data["Delta Adjacent Air Temperature Pair 3"] = None
        self._data["Surface Name Pair 4"] = None
        self._data["Delta Adjacent Air Temperature Pair 4"] = None
        self._data["Surface Name Pair 5"] = None
        self._data["Delta Adjacent Air Temperature Pair 5"] = None
        self._data["Surface Name Pair 6"] = None
        self._data["Delta Adjacent Air Temperature Pair 6"] = None
        self._data["Surface Name Pair 7"] = None
        self._data["Delta Adjacent Air Temperature Pair 7"] = None
        self._data["Surface Name Pair 8"] = None
        self._data["Delta Adjacent Air Temperature Pair 8"] = None
        self._data["Surface Name Pair 9"] = None
        self._data["Delta Adjacent Air Temperature Pair 9"] = None
        self._data["Surface Name Pair 10"] = None
        self._data["Delta Adjacent Air Temperature Pair 10"] = None
        self._data["Surface Name Pair 11"] = None
        self._data["Delta Adjacent Air Temperature Pair 11"] = None
        self._data["Surface Name Pair 12"] = None
        self._data["Delta Adjacent Air Temperature Pair 12"] = None
        self._data["Surface Name Pair 13"] = None
        self._data["Delta Adjacent Air Temperature Pair 13"] = None
        self._data["Surface Name Pair 14"] = None
        self._data["Delta Adjacent Air Temperature Pair 14"] = None
        self._data["Surface Name Pair 15"] = None
        self._data["Delta Adjacent Air Temperature Pair 15"] = None
        self._data["Surface Name Pair 16"] = None
        self._data["Delta Adjacent Air Temperature Pair 16"] = None
        self._data["Surface Name Pair 17"] = None
        self._data["Delta Adjacent Air Temperature Pair 17"] = None
        self._data["Surface Name Pair 18"] = None
        self._data["Delta Adjacent Air Temperature Pair 18"] = None
        self._data["Surface Name Pair 19"] = None
        self._data["Delta Adjacent Air Temperature Pair 19"] = None
        self._data["Surface Name Pair 20"] = None
        self._data["Delta Adjacent Air Temperature Pair 20"] = None
        self._data["Surface Name Pair 21"] = None
        self._data["Delta Adjacent Air Temperature Pair 21"] = None
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
            self.control_integer_for_pattern_control_schedule_name = None
        else:
            self.control_integer_for_pattern_control_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_offset = None
        else:
            self.thermostat_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_offset = None
        else:
            self.return_air_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.exhaust_air_offset = None
        else:
            self.exhaust_air_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_1 = None
        else:
            self.surface_name_pair_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_1 = None
        else:
            self.delta_adjacent_air_temperature_pair_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_2 = None
        else:
            self.surface_name_pair_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_2 = None
        else:
            self.delta_adjacent_air_temperature_pair_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_3 = None
        else:
            self.surface_name_pair_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_3 = None
        else:
            self.delta_adjacent_air_temperature_pair_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_4 = None
        else:
            self.surface_name_pair_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_4 = None
        else:
            self.delta_adjacent_air_temperature_pair_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_5 = None
        else:
            self.surface_name_pair_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_5 = None
        else:
            self.delta_adjacent_air_temperature_pair_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_6 = None
        else:
            self.surface_name_pair_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_6 = None
        else:
            self.delta_adjacent_air_temperature_pair_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_7 = None
        else:
            self.surface_name_pair_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_7 = None
        else:
            self.delta_adjacent_air_temperature_pair_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_8 = None
        else:
            self.surface_name_pair_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_8 = None
        else:
            self.delta_adjacent_air_temperature_pair_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_9 = None
        else:
            self.surface_name_pair_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_9 = None
        else:
            self.delta_adjacent_air_temperature_pair_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_10 = None
        else:
            self.surface_name_pair_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_10 = None
        else:
            self.delta_adjacent_air_temperature_pair_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_11 = None
        else:
            self.surface_name_pair_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_11 = None
        else:
            self.delta_adjacent_air_temperature_pair_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_12 = None
        else:
            self.surface_name_pair_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_12 = None
        else:
            self.delta_adjacent_air_temperature_pair_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_13 = None
        else:
            self.surface_name_pair_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_13 = None
        else:
            self.delta_adjacent_air_temperature_pair_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_14 = None
        else:
            self.surface_name_pair_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_14 = None
        else:
            self.delta_adjacent_air_temperature_pair_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_15 = None
        else:
            self.surface_name_pair_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_15 = None
        else:
            self.delta_adjacent_air_temperature_pair_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_16 = None
        else:
            self.surface_name_pair_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_16 = None
        else:
            self.delta_adjacent_air_temperature_pair_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_17 = None
        else:
            self.surface_name_pair_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_17 = None
        else:
            self.delta_adjacent_air_temperature_pair_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_18 = None
        else:
            self.surface_name_pair_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_18 = None
        else:
            self.delta_adjacent_air_temperature_pair_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_19 = None
        else:
            self.surface_name_pair_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_19 = None
        else:
            self.delta_adjacent_air_temperature_pair_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_20 = None
        else:
            self.surface_name_pair_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_20 = None
        else:
            self.delta_adjacent_air_temperature_pair_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_name_pair_21 = None
        else:
            self.surface_name_pair_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.delta_adjacent_air_temperature_pair_21 = None
        else:
            self.delta_adjacent_air_temperature_pair_21 = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'alpha', u'required-field': True, 'pytype': 'str'}

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
    def control_integer_for_pattern_control_schedule_name(self):
        """Get control_integer_for_pattern_control_schedule_name

        Returns:
            int: the value of `control_integer_for_pattern_control_schedule_name` or None if not set
        """
        return self._data["Control Integer for Pattern Control Schedule Name"]

    @control_integer_for_pattern_control_schedule_name.setter
    def control_integer_for_pattern_control_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Control Integer for Pattern Control Schedule Name`
        reference this entry in schedule
        
        {u'note': [u'reference this entry in schedule'], u'type': u'integer', u'required-field': True, 'pytype': 'int'}

        Args:
            value (int): value for IDD Field `Control Integer for Pattern Control Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                raise ValueError('value {} need to be of type int '
                                 'for field `control_integer_for_pattern_control_schedule_name`'.format(value))
        self._data["Control Integer for Pattern Control Schedule Name"] = value

    @property
    def thermostat_offset(self):
        """Get thermostat_offset

        Returns:
            float: the value of `thermostat_offset` or None if not set
        """
        return self._data["Thermostat Offset"]

    @thermostat_offset.setter
    def thermostat_offset(self, value=None):
        """  Corresponds to IDD Field `Thermostat Offset`
        = (Temp at thermostat- Mean Air Temp)
        
        {u'note': [u'= (Temp at thermostat- Mean Air Temp)'], u'units': u'deltaC', 'type': 'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Thermostat Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_offset`'.format(value))
        self._data["Thermostat Offset"] = value

    @property
    def return_air_offset(self):
        """Get return_air_offset

        Returns:
            float: the value of `return_air_offset` or None if not set
        """
        return self._data["Return Air Offset"]

    @return_air_offset.setter
    def return_air_offset(self, value=None):
        """  Corresponds to IDD Field `Return Air Offset`
        = (Tleaving - Mean Air Temp ) deg C
        
        {u'note': [u'= (Tleaving - Mean Air Temp ) deg C'], u'units': u'deltaC', 'type': 'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Return Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `return_air_offset`'.format(value))
        self._data["Return Air Offset"] = value

    @property
    def exhaust_air_offset(self):
        """Get exhaust_air_offset

        Returns:
            float: the value of `exhaust_air_offset` or None if not set
        """
        return self._data["Exhaust Air Offset"]

    @exhaust_air_offset.setter
    def exhaust_air_offset(self, value=None):
        """  Corresponds to IDD Field `Exhaust Air Offset`
        = (Texhaust - Mean Air Temp) deg C
        
        {u'note': [u'= (Texhaust - Mean Air Temp) deg C'], u'units': u'deltaC', 'type': 'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Exhaust Air Offset`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `exhaust_air_offset`'.format(value))
        self._data["Exhaust Air Offset"] = value

    @property
    def surface_name_pair_1(self):
        """Get surface_name_pair_1

        Returns:
            str: the value of `surface_name_pair_1` or None if not set
        """
        return self._data["Surface Name Pair 1"]

    @surface_name_pair_1.setter
    def surface_name_pair_1(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 1`
        
        {'pytype': 'str', u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', u'required-field': True, u'begin-extensible': u''}

        Args:
            value (str): value for IDD Field `Surface Name Pair 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_1`')
        self._data["Surface Name Pair 1"] = value

    @property
    def delta_adjacent_air_temperature_pair_1(self):
        """Get delta_adjacent_air_temperature_pair_1

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_1` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 1"]

    @delta_adjacent_air_temperature_pair_1.setter
    def delta_adjacent_air_temperature_pair_1(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 1`
        
        {u'units': u'deltaC', u'type': u'real', u'required-field': True, 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 1`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_1`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 1"] = value

    @property
    def surface_name_pair_2(self):
        """Get surface_name_pair_2

        Returns:
            str: the value of `surface_name_pair_2` or None if not set
        """
        return self._data["Surface Name Pair 2"]

    @surface_name_pair_2.setter
    def surface_name_pair_2(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 2`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_2`')
        self._data["Surface Name Pair 2"] = value

    @property
    def delta_adjacent_air_temperature_pair_2(self):
        """Get delta_adjacent_air_temperature_pair_2

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_2` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 2"]

    @delta_adjacent_air_temperature_pair_2.setter
    def delta_adjacent_air_temperature_pair_2(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 2`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 2`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_2`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 2"] = value

    @property
    def surface_name_pair_3(self):
        """Get surface_name_pair_3

        Returns:
            str: the value of `surface_name_pair_3` or None if not set
        """
        return self._data["Surface Name Pair 3"]

    @surface_name_pair_3.setter
    def surface_name_pair_3(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 3`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_3`')
        self._data["Surface Name Pair 3"] = value

    @property
    def delta_adjacent_air_temperature_pair_3(self):
        """Get delta_adjacent_air_temperature_pair_3

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_3` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 3"]

    @delta_adjacent_air_temperature_pair_3.setter
    def delta_adjacent_air_temperature_pair_3(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 3`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 3`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_3`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 3"] = value

    @property
    def surface_name_pair_4(self):
        """Get surface_name_pair_4

        Returns:
            str: the value of `surface_name_pair_4` or None if not set
        """
        return self._data["Surface Name Pair 4"]

    @surface_name_pair_4.setter
    def surface_name_pair_4(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 4`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_4`')
        self._data["Surface Name Pair 4"] = value

    @property
    def delta_adjacent_air_temperature_pair_4(self):
        """Get delta_adjacent_air_temperature_pair_4

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_4` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 4"]

    @delta_adjacent_air_temperature_pair_4.setter
    def delta_adjacent_air_temperature_pair_4(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 4`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 4`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_4`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 4"] = value

    @property
    def surface_name_pair_5(self):
        """Get surface_name_pair_5

        Returns:
            str: the value of `surface_name_pair_5` or None if not set
        """
        return self._data["Surface Name Pair 5"]

    @surface_name_pair_5.setter
    def surface_name_pair_5(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 5`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_5`')
        self._data["Surface Name Pair 5"] = value

    @property
    def delta_adjacent_air_temperature_pair_5(self):
        """Get delta_adjacent_air_temperature_pair_5

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_5` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 5"]

    @delta_adjacent_air_temperature_pair_5.setter
    def delta_adjacent_air_temperature_pair_5(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 5`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 5`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_5`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 5"] = value

    @property
    def surface_name_pair_6(self):
        """Get surface_name_pair_6

        Returns:
            str: the value of `surface_name_pair_6` or None if not set
        """
        return self._data["Surface Name Pair 6"]

    @surface_name_pair_6.setter
    def surface_name_pair_6(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 6`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_6`')
        self._data["Surface Name Pair 6"] = value

    @property
    def delta_adjacent_air_temperature_pair_6(self):
        """Get delta_adjacent_air_temperature_pair_6

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_6` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 6"]

    @delta_adjacent_air_temperature_pair_6.setter
    def delta_adjacent_air_temperature_pair_6(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 6`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 6`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_6`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 6"] = value

    @property
    def surface_name_pair_7(self):
        """Get surface_name_pair_7

        Returns:
            str: the value of `surface_name_pair_7` or None if not set
        """
        return self._data["Surface Name Pair 7"]

    @surface_name_pair_7.setter
    def surface_name_pair_7(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 7`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_7`')
        self._data["Surface Name Pair 7"] = value

    @property
    def delta_adjacent_air_temperature_pair_7(self):
        """Get delta_adjacent_air_temperature_pair_7

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_7` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 7"]

    @delta_adjacent_air_temperature_pair_7.setter
    def delta_adjacent_air_temperature_pair_7(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 7`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 7`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_7`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 7"] = value

    @property
    def surface_name_pair_8(self):
        """Get surface_name_pair_8

        Returns:
            str: the value of `surface_name_pair_8` or None if not set
        """
        return self._data["Surface Name Pair 8"]

    @surface_name_pair_8.setter
    def surface_name_pair_8(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 8`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_8`')
        self._data["Surface Name Pair 8"] = value

    @property
    def delta_adjacent_air_temperature_pair_8(self):
        """Get delta_adjacent_air_temperature_pair_8

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_8` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 8"]

    @delta_adjacent_air_temperature_pair_8.setter
    def delta_adjacent_air_temperature_pair_8(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 8`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 8`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_8`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 8"] = value

    @property
    def surface_name_pair_9(self):
        """Get surface_name_pair_9

        Returns:
            str: the value of `surface_name_pair_9` or None if not set
        """
        return self._data["Surface Name Pair 9"]

    @surface_name_pair_9.setter
    def surface_name_pair_9(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 9`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_9`')
        self._data["Surface Name Pair 9"] = value

    @property
    def delta_adjacent_air_temperature_pair_9(self):
        """Get delta_adjacent_air_temperature_pair_9

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_9` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 9"]

    @delta_adjacent_air_temperature_pair_9.setter
    def delta_adjacent_air_temperature_pair_9(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 9`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 9`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_9`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 9"] = value

    @property
    def surface_name_pair_10(self):
        """Get surface_name_pair_10

        Returns:
            str: the value of `surface_name_pair_10` or None if not set
        """
        return self._data["Surface Name Pair 10"]

    @surface_name_pair_10.setter
    def surface_name_pair_10(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 10`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_10`')
        self._data["Surface Name Pair 10"] = value

    @property
    def delta_adjacent_air_temperature_pair_10(self):
        """Get delta_adjacent_air_temperature_pair_10

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_10` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 10"]

    @delta_adjacent_air_temperature_pair_10.setter
    def delta_adjacent_air_temperature_pair_10(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 10`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 10`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_10`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 10"] = value

    @property
    def surface_name_pair_11(self):
        """Get surface_name_pair_11

        Returns:
            str: the value of `surface_name_pair_11` or None if not set
        """
        return self._data["Surface Name Pair 11"]

    @surface_name_pair_11.setter
    def surface_name_pair_11(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 11`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_11`')
        self._data["Surface Name Pair 11"] = value

    @property
    def delta_adjacent_air_temperature_pair_11(self):
        """Get delta_adjacent_air_temperature_pair_11

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_11` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 11"]

    @delta_adjacent_air_temperature_pair_11.setter
    def delta_adjacent_air_temperature_pair_11(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 11`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 11`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_11`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 11"] = value

    @property
    def surface_name_pair_12(self):
        """Get surface_name_pair_12

        Returns:
            str: the value of `surface_name_pair_12` or None if not set
        """
        return self._data["Surface Name Pair 12"]

    @surface_name_pair_12.setter
    def surface_name_pair_12(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 12`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_12`')
        self._data["Surface Name Pair 12"] = value

    @property
    def delta_adjacent_air_temperature_pair_12(self):
        """Get delta_adjacent_air_temperature_pair_12

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_12` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 12"]

    @delta_adjacent_air_temperature_pair_12.setter
    def delta_adjacent_air_temperature_pair_12(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 12`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 12`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_12`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 12"] = value

    @property
    def surface_name_pair_13(self):
        """Get surface_name_pair_13

        Returns:
            str: the value of `surface_name_pair_13` or None if not set
        """
        return self._data["Surface Name Pair 13"]

    @surface_name_pair_13.setter
    def surface_name_pair_13(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 13`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_13`')
        self._data["Surface Name Pair 13"] = value

    @property
    def delta_adjacent_air_temperature_pair_13(self):
        """Get delta_adjacent_air_temperature_pair_13

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_13` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 13"]

    @delta_adjacent_air_temperature_pair_13.setter
    def delta_adjacent_air_temperature_pair_13(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 13`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 13`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_13`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 13"] = value

    @property
    def surface_name_pair_14(self):
        """Get surface_name_pair_14

        Returns:
            str: the value of `surface_name_pair_14` or None if not set
        """
        return self._data["Surface Name Pair 14"]

    @surface_name_pair_14.setter
    def surface_name_pair_14(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 14`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_14`')
        self._data["Surface Name Pair 14"] = value

    @property
    def delta_adjacent_air_temperature_pair_14(self):
        """Get delta_adjacent_air_temperature_pair_14

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_14` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 14"]

    @delta_adjacent_air_temperature_pair_14.setter
    def delta_adjacent_air_temperature_pair_14(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 14`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 14`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_14`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 14"] = value

    @property
    def surface_name_pair_15(self):
        """Get surface_name_pair_15

        Returns:
            str: the value of `surface_name_pair_15` or None if not set
        """
        return self._data["Surface Name Pair 15"]

    @surface_name_pair_15.setter
    def surface_name_pair_15(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 15`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_15`')
        self._data["Surface Name Pair 15"] = value

    @property
    def delta_adjacent_air_temperature_pair_15(self):
        """Get delta_adjacent_air_temperature_pair_15

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_15` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 15"]

    @delta_adjacent_air_temperature_pair_15.setter
    def delta_adjacent_air_temperature_pair_15(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 15`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 15`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_15`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 15"] = value

    @property
    def surface_name_pair_16(self):
        """Get surface_name_pair_16

        Returns:
            str: the value of `surface_name_pair_16` or None if not set
        """
        return self._data["Surface Name Pair 16"]

    @surface_name_pair_16.setter
    def surface_name_pair_16(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 16`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_16`')
        self._data["Surface Name Pair 16"] = value

    @property
    def delta_adjacent_air_temperature_pair_16(self):
        """Get delta_adjacent_air_temperature_pair_16

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_16` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 16"]

    @delta_adjacent_air_temperature_pair_16.setter
    def delta_adjacent_air_temperature_pair_16(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 16`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 16`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_16`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 16"] = value

    @property
    def surface_name_pair_17(self):
        """Get surface_name_pair_17

        Returns:
            str: the value of `surface_name_pair_17` or None if not set
        """
        return self._data["Surface Name Pair 17"]

    @surface_name_pair_17.setter
    def surface_name_pair_17(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 17`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_17`')
        self._data["Surface Name Pair 17"] = value

    @property
    def delta_adjacent_air_temperature_pair_17(self):
        """Get delta_adjacent_air_temperature_pair_17

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_17` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 17"]

    @delta_adjacent_air_temperature_pair_17.setter
    def delta_adjacent_air_temperature_pair_17(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 17`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 17`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_17`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 17"] = value

    @property
    def surface_name_pair_18(self):
        """Get surface_name_pair_18

        Returns:
            str: the value of `surface_name_pair_18` or None if not set
        """
        return self._data["Surface Name Pair 18"]

    @surface_name_pair_18.setter
    def surface_name_pair_18(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 18`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_18`')
        self._data["Surface Name Pair 18"] = value

    @property
    def delta_adjacent_air_temperature_pair_18(self):
        """Get delta_adjacent_air_temperature_pair_18

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_18` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 18"]

    @delta_adjacent_air_temperature_pair_18.setter
    def delta_adjacent_air_temperature_pair_18(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 18`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 18`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_18`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 18"] = value

    @property
    def surface_name_pair_19(self):
        """Get surface_name_pair_19

        Returns:
            str: the value of `surface_name_pair_19` or None if not set
        """
        return self._data["Surface Name Pair 19"]

    @surface_name_pair_19.setter
    def surface_name_pair_19(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 19`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_19`')
        self._data["Surface Name Pair 19"] = value

    @property
    def delta_adjacent_air_temperature_pair_19(self):
        """Get delta_adjacent_air_temperature_pair_19

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_19` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 19"]

    @delta_adjacent_air_temperature_pair_19.setter
    def delta_adjacent_air_temperature_pair_19(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 19`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 19`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_19`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 19"] = value

    @property
    def surface_name_pair_20(self):
        """Get surface_name_pair_20

        Returns:
            str: the value of `surface_name_pair_20` or None if not set
        """
        return self._data["Surface Name Pair 20"]

    @surface_name_pair_20.setter
    def surface_name_pair_20(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 20`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_20`')
        self._data["Surface Name Pair 20"] = value

    @property
    def delta_adjacent_air_temperature_pair_20(self):
        """Get delta_adjacent_air_temperature_pair_20

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_20` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 20"]

    @delta_adjacent_air_temperature_pair_20.setter
    def delta_adjacent_air_temperature_pair_20(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 20`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 20`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_20`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 20"] = value

    @property
    def surface_name_pair_21(self):
        """Get surface_name_pair_21

        Returns:
            str: the value of `surface_name_pair_21` or None if not set
        """
        return self._data["Surface Name Pair 21"]

    @surface_name_pair_21.setter
    def surface_name_pair_21(self, value=None):
        """  Corresponds to IDD Field `Surface Name Pair 21`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface Name Pair 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_name_pair_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_name_pair_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_name_pair_21`')
        self._data["Surface Name Pair 21"] = value

    @property
    def delta_adjacent_air_temperature_pair_21(self):
        """Get delta_adjacent_air_temperature_pair_21

        Returns:
            float: the value of `delta_adjacent_air_temperature_pair_21` or None if not set
        """
        return self._data["Delta Adjacent Air Temperature Pair 21"]

    @delta_adjacent_air_temperature_pair_21.setter
    def delta_adjacent_air_temperature_pair_21(self, value=None):
        """  Corresponds to IDD Field `Delta Adjacent Air Temperature Pair 21`
        
        {u'units': u'deltaC', u'type': u'real', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Delta Adjacent Air Temperature Pair 21`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `delta_adjacent_air_temperature_pair_21`'.format(value))
        self._data["Delta Adjacent Air Temperature Pair 21"] = value

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

class RoomAirNode(object):
    """ Corresponds to IDD object `RoomAir:Node`
        Define an air node for some types of nodal room air models
    
    """
    internal_name = "RoomAir:Node"
    field_count = 25
    required_fields = ["Node Type", "Zone Name", "Height of Nodal Control Volume Center"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAir:Node`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Node Type"] = None
        self._data["Zone Name"] = None
        self._data["Height of Nodal Control Volume Center"] = None
        self._data["Surface 1 Name"] = None
        self._data["Surface 2 Name"] = None
        self._data["Surface 3 Name"] = None
        self._data["Surface 4 Name"] = None
        self._data["Surface 5 Name"] = None
        self._data["Surface 6 Name"] = None
        self._data["Surface 7 Name"] = None
        self._data["Surface 8 Name"] = None
        self._data["Surface 9 Name"] = None
        self._data["Surface 10 Name"] = None
        self._data["Surface 11 Name"] = None
        self._data["Surface 12 Name"] = None
        self._data["Surface 13 Name"] = None
        self._data["Surface 14 Name"] = None
        self._data["Surface 15 Name"] = None
        self._data["Surface 16 Name"] = None
        self._data["Surface 17 Name"] = None
        self._data["Surface 18 Name"] = None
        self._data["Surface 19 Name"] = None
        self._data["Surface 20 Name"] = None
        self._data["Surface 21 Name"] = None
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
            self.node_type = None
        else:
            self.node_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.height_of_nodal_control_volume_center = None
        else:
            self.height_of_nodal_control_volume_center = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_1_name = None
        else:
            self.surface_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_2_name = None
        else:
            self.surface_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_3_name = None
        else:
            self.surface_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_4_name = None
        else:
            self.surface_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_5_name = None
        else:
            self.surface_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_6_name = None
        else:
            self.surface_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_7_name = None
        else:
            self.surface_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_8_name = None
        else:
            self.surface_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_9_name = None
        else:
            self.surface_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_10_name = None
        else:
            self.surface_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_11_name = None
        else:
            self.surface_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_12_name = None
        else:
            self.surface_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_13_name = None
        else:
            self.surface_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_14_name = None
        else:
            self.surface_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_15_name = None
        else:
            self.surface_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_16_name = None
        else:
            self.surface_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_17_name = None
        else:
            self.surface_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_18_name = None
        else:
            self.surface_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_19_name = None
        else:
            self.surface_19_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_20_name = None
        else:
            self.surface_20_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.surface_21_name = None
        else:
            self.surface_21_name = vals[i]
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
        """  Corresponds to IDD Field `Name`
        
        {u'type': u'Alpha', 'pytype': 'str'}

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
    def node_type(self):
        """Get node_type

        Returns:
            str: the value of `node_type` or None if not set
        """
        return self._data["Node Type"]

    @node_type.setter
    def node_type(self, value=None):
        """  Corresponds to IDD Field `Node Type`
        
        {u'type': u'choice', u'key': [u'Inlet', u'Floor', u'Control', u'Ceiling', u'MundtRoom', u'Return'], u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Node Type`
                Accepted values are:
                      - Inlet
                      - Floor
                      - Control
                      - Ceiling
                      - MundtRoom
                      - Return
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `node_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `node_type`')
            vals = {}
            vals["inlet"] = "Inlet"
            vals["floor"] = "Floor"
            vals["control"] = "Control"
            vals["ceiling"] = "Ceiling"
            vals["mundtroom"] = "MundtRoom"
            vals["return"] = "Return"
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
                                     'field `node_type`'.format(value))
            value = vals[value_lower]
        self._data["Node Type"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        
        {u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def height_of_nodal_control_volume_center(self):
        """Get height_of_nodal_control_volume_center

        Returns:
            float: the value of `height_of_nodal_control_volume_center` or None if not set
        """
        return self._data["Height of Nodal Control Volume Center"]

    @height_of_nodal_control_volume_center.setter
    def height_of_nodal_control_volume_center(self, value=None):
        """  Corresponds to IDD Field `Height of Nodal Control Volume Center`
        
        {u'units': u'm', u'type': u'real', u'required-field': True, 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Height of Nodal Control Volume Center`
                Units: m
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `height_of_nodal_control_volume_center`'.format(value))
        self._data["Height of Nodal Control Volume Center"] = value

    @property
    def surface_1_name(self):
        """Get surface_1_name

        Returns:
            str: the value of `surface_1_name` or None if not set
        """
        return self._data["Surface 1 Name"]

    @surface_1_name.setter
    def surface_1_name(self, value=None):
        """  Corresponds to IDD Field `Surface 1 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_1_name`')
        self._data["Surface 1 Name"] = value

    @property
    def surface_2_name(self):
        """Get surface_2_name

        Returns:
            str: the value of `surface_2_name` or None if not set
        """
        return self._data["Surface 2 Name"]

    @surface_2_name.setter
    def surface_2_name(self, value=None):
        """  Corresponds to IDD Field `Surface 2 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 2 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_2_name`')
        self._data["Surface 2 Name"] = value

    @property
    def surface_3_name(self):
        """Get surface_3_name

        Returns:
            str: the value of `surface_3_name` or None if not set
        """
        return self._data["Surface 3 Name"]

    @surface_3_name.setter
    def surface_3_name(self, value=None):
        """  Corresponds to IDD Field `Surface 3 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 3 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_3_name`')
        self._data["Surface 3 Name"] = value

    @property
    def surface_4_name(self):
        """Get surface_4_name

        Returns:
            str: the value of `surface_4_name` or None if not set
        """
        return self._data["Surface 4 Name"]

    @surface_4_name.setter
    def surface_4_name(self, value=None):
        """  Corresponds to IDD Field `Surface 4 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 4 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_4_name`')
        self._data["Surface 4 Name"] = value

    @property
    def surface_5_name(self):
        """Get surface_5_name

        Returns:
            str: the value of `surface_5_name` or None if not set
        """
        return self._data["Surface 5 Name"]

    @surface_5_name.setter
    def surface_5_name(self, value=None):
        """  Corresponds to IDD Field `Surface 5 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 5 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_5_name`')
        self._data["Surface 5 Name"] = value

    @property
    def surface_6_name(self):
        """Get surface_6_name

        Returns:
            str: the value of `surface_6_name` or None if not set
        """
        return self._data["Surface 6 Name"]

    @surface_6_name.setter
    def surface_6_name(self, value=None):
        """  Corresponds to IDD Field `Surface 6 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 6 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_6_name`')
        self._data["Surface 6 Name"] = value

    @property
    def surface_7_name(self):
        """Get surface_7_name

        Returns:
            str: the value of `surface_7_name` or None if not set
        """
        return self._data["Surface 7 Name"]

    @surface_7_name.setter
    def surface_7_name(self, value=None):
        """  Corresponds to IDD Field `Surface 7 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 7 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_7_name`')
        self._data["Surface 7 Name"] = value

    @property
    def surface_8_name(self):
        """Get surface_8_name

        Returns:
            str: the value of `surface_8_name` or None if not set
        """
        return self._data["Surface 8 Name"]

    @surface_8_name.setter
    def surface_8_name(self, value=None):
        """  Corresponds to IDD Field `Surface 8 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 8 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_8_name`')
        self._data["Surface 8 Name"] = value

    @property
    def surface_9_name(self):
        """Get surface_9_name

        Returns:
            str: the value of `surface_9_name` or None if not set
        """
        return self._data["Surface 9 Name"]

    @surface_9_name.setter
    def surface_9_name(self, value=None):
        """  Corresponds to IDD Field `Surface 9 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 9 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_9_name`')
        self._data["Surface 9 Name"] = value

    @property
    def surface_10_name(self):
        """Get surface_10_name

        Returns:
            str: the value of `surface_10_name` or None if not set
        """
        return self._data["Surface 10 Name"]

    @surface_10_name.setter
    def surface_10_name(self, value=None):
        """  Corresponds to IDD Field `Surface 10 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 10 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_10_name`')
        self._data["Surface 10 Name"] = value

    @property
    def surface_11_name(self):
        """Get surface_11_name

        Returns:
            str: the value of `surface_11_name` or None if not set
        """
        return self._data["Surface 11 Name"]

    @surface_11_name.setter
    def surface_11_name(self, value=None):
        """  Corresponds to IDD Field `Surface 11 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 11 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_11_name`')
        self._data["Surface 11 Name"] = value

    @property
    def surface_12_name(self):
        """Get surface_12_name

        Returns:
            str: the value of `surface_12_name` or None if not set
        """
        return self._data["Surface 12 Name"]

    @surface_12_name.setter
    def surface_12_name(self, value=None):
        """  Corresponds to IDD Field `Surface 12 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 12 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_12_name`')
        self._data["Surface 12 Name"] = value

    @property
    def surface_13_name(self):
        """Get surface_13_name

        Returns:
            str: the value of `surface_13_name` or None if not set
        """
        return self._data["Surface 13 Name"]

    @surface_13_name.setter
    def surface_13_name(self, value=None):
        """  Corresponds to IDD Field `Surface 13 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 13 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_13_name`')
        self._data["Surface 13 Name"] = value

    @property
    def surface_14_name(self):
        """Get surface_14_name

        Returns:
            str: the value of `surface_14_name` or None if not set
        """
        return self._data["Surface 14 Name"]

    @surface_14_name.setter
    def surface_14_name(self, value=None):
        """  Corresponds to IDD Field `Surface 14 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 14 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_14_name`')
        self._data["Surface 14 Name"] = value

    @property
    def surface_15_name(self):
        """Get surface_15_name

        Returns:
            str: the value of `surface_15_name` or None if not set
        """
        return self._data["Surface 15 Name"]

    @surface_15_name.setter
    def surface_15_name(self, value=None):
        """  Corresponds to IDD Field `Surface 15 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 15 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_15_name`')
        self._data["Surface 15 Name"] = value

    @property
    def surface_16_name(self):
        """Get surface_16_name

        Returns:
            str: the value of `surface_16_name` or None if not set
        """
        return self._data["Surface 16 Name"]

    @surface_16_name.setter
    def surface_16_name(self, value=None):
        """  Corresponds to IDD Field `Surface 16 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 16 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_16_name`')
        self._data["Surface 16 Name"] = value

    @property
    def surface_17_name(self):
        """Get surface_17_name

        Returns:
            str: the value of `surface_17_name` or None if not set
        """
        return self._data["Surface 17 Name"]

    @surface_17_name.setter
    def surface_17_name(self, value=None):
        """  Corresponds to IDD Field `Surface 17 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 17 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_17_name`')
        self._data["Surface 17 Name"] = value

    @property
    def surface_18_name(self):
        """Get surface_18_name

        Returns:
            str: the value of `surface_18_name` or None if not set
        """
        return self._data["Surface 18 Name"]

    @surface_18_name.setter
    def surface_18_name(self, value=None):
        """  Corresponds to IDD Field `Surface 18 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 18 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_18_name`')
        self._data["Surface 18 Name"] = value

    @property
    def surface_19_name(self):
        """Get surface_19_name

        Returns:
            str: the value of `surface_19_name` or None if not set
        """
        return self._data["Surface 19 Name"]

    @surface_19_name.setter
    def surface_19_name(self, value=None):
        """  Corresponds to IDD Field `Surface 19 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 19 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_19_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_19_name`')
        self._data["Surface 19 Name"] = value

    @property
    def surface_20_name(self):
        """Get surface_20_name

        Returns:
            str: the value of `surface_20_name` or None if not set
        """
        return self._data["Surface 20 Name"]

    @surface_20_name.setter
    def surface_20_name(self, value=None):
        """  Corresponds to IDD Field `Surface 20 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 20 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_20_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_20_name`')
        self._data["Surface 20 Name"] = value

    @property
    def surface_21_name(self):
        """Get surface_21_name

        Returns:
            str: the value of `surface_21_name` or None if not set
        """
        return self._data["Surface 21 Name"]

    @surface_21_name.setter
    def surface_21_name(self, value=None):
        """  Corresponds to IDD Field `Surface 21 Name`
        
        {u'type': u'object-list', u'object-list': u'AllHeatTranSurfNames', 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Surface 21 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `surface_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `surface_21_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `surface_21_name`')
        self._data["Surface 21 Name"] = value

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

class RoomAirSettingsOneNodeDisplacementVentilation(object):
    """ Corresponds to IDD object `RoomAirSettings:OneNodeDisplacementVentilation`
        The Mundt model for displacement ventilation
    
    """
    internal_name = "RoomAirSettings:OneNodeDisplacementVentilation"
    field_count = 3
    required_fields = ["Zone Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAirSettings:OneNodeDisplacementVentilation`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Fraction of Convective Internal Loads Added to Floor Air"] = None
        self._data["Fraction of Infiltration Internal Loads Added to Floor Air"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_convective_internal_loads_added_to_floor_air = None
        else:
            self.fraction_of_convective_internal_loads_added_to_floor_air = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_infiltration_internal_loads_added_to_floor_air = None
        else:
            self.fraction_of_infiltration_internal_loads_added_to_floor_air = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        
        {u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def fraction_of_convective_internal_loads_added_to_floor_air(self):
        """Get fraction_of_convective_internal_loads_added_to_floor_air

        Returns:
            float: the value of `fraction_of_convective_internal_loads_added_to_floor_air` or None if not set
        """
        return self._data["Fraction of Convective Internal Loads Added to Floor Air"]

    @fraction_of_convective_internal_loads_added_to_floor_air.setter
    def fraction_of_convective_internal_loads_added_to_floor_air(self, value=None):
        """  Corresponds to IDD Field `Fraction of Convective Internal Loads Added to Floor Air`
        
        {u'minimum': '0.0', u'type': u'real', u'maximum': '1.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Fraction of Convective Internal Loads Added to Floor Air`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_convective_internal_loads_added_to_floor_air`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_convective_internal_loads_added_to_floor_air`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_convective_internal_loads_added_to_floor_air`')
        self._data["Fraction of Convective Internal Loads Added to Floor Air"] = value

    @property
    def fraction_of_infiltration_internal_loads_added_to_floor_air(self):
        """Get fraction_of_infiltration_internal_loads_added_to_floor_air

        Returns:
            float: the value of `fraction_of_infiltration_internal_loads_added_to_floor_air` or None if not set
        """
        return self._data["Fraction of Infiltration Internal Loads Added to Floor Air"]

    @fraction_of_infiltration_internal_loads_added_to_floor_air.setter
    def fraction_of_infiltration_internal_loads_added_to_floor_air(self, value=None):
        """  Corresponds to IDD Field `Fraction of Infiltration Internal Loads Added to Floor Air`
        
        {u'minimum': '0.0', u'type': u'real', u'maximum': '1.0', 'pytype': 'float'}

        Args:
            value (float): value for IDD Field `Fraction of Infiltration Internal Loads Added to Floor Air`
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
                raise ValueError('value {} need to be of type float '
                                 'for field `fraction_of_infiltration_internal_loads_added_to_floor_air`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_infiltration_internal_loads_added_to_floor_air`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_infiltration_internal_loads_added_to_floor_air`')
        self._data["Fraction of Infiltration Internal Loads Added to Floor Air"] = value

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

class RoomAirSettingsThreeNodeDisplacementVentilation(object):
    """ Corresponds to IDD object `RoomAirSettings:ThreeNodeDisplacementVentilation`
        The UCSD model for Displacement Ventilation
    
    """
    internal_name = "RoomAirSettings:ThreeNodeDisplacementVentilation"
    field_count = 6
    required_fields = ["Zone Name", "Gain Distribution Schedule Name", "Number of Plumes per Occupant", "Temperature Difference Threshold for Reporting"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAirSettings:ThreeNodeDisplacementVentilation`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Gain Distribution Schedule Name"] = None
        self._data["Number of Plumes per Occupant"] = None
        self._data["Thermostat Height"] = None
        self._data["Comfort Height"] = None
        self._data["Temperature Difference Threshold for Reporting"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gain_distribution_schedule_name = None
        else:
            self.gain_distribution_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_plumes_per_occupant = None
        else:
            self.number_of_plumes_per_occupant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.comfort_height = None
        else:
            self.comfort_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_difference_threshold_for_reporting = None
        else:
            self.temperature_difference_threshold_for_reporting = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone being described. Any existing zone name
        
        {u'note': [u'Name of Zone being described. Any existing zone name'], u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def gain_distribution_schedule_name(self):
        """Get gain_distribution_schedule_name

        Returns:
            str: the value of `gain_distribution_schedule_name` or None if not set
        """
        return self._data["Gain Distribution Schedule Name"]

    @gain_distribution_schedule_name.setter
    def gain_distribution_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Gain Distribution Schedule Name`
        Distribution of the convective heat gains between the occupied and mixed zones.
        0<= Accepted Value <= 1.
        In the DV model 1 means all convective gains in the lower layer.
        
        {u'note': [u'Distribution of the convective heat gains between the occupied and mixed zones.', u'0<= Accepted Value <= 1.', u'In the DV model 1 means all convective gains in the lower layer.'], u'type': u'object-list', u'object-list': u'ScheduleNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Gain Distribution Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `gain_distribution_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gain_distribution_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `gain_distribution_schedule_name`')
        self._data["Gain Distribution Schedule Name"] = value

    @property
    def number_of_plumes_per_occupant(self):
        """Get number_of_plumes_per_occupant

        Returns:
            float: the value of `number_of_plumes_per_occupant` or None if not set
        """
        return self._data["Number of Plumes per Occupant"]

    @number_of_plumes_per_occupant.setter
    def number_of_plumes_per_occupant(self, value=1.0 ):
        """  Corresponds to IDD Field `Number of Plumes per Occupant`
        Used only in the UCSD displacement ventilation model.
        Effective number of separate plumes per occupant in the occupied zone.
        Plumes that merge together in the occupied zone count as one.
        
        {'pytype': 'float', u'default': '1.0', u'minimum>': '0.0', u'required-field': True, u'note': [u'Used only in the UCSD displacement ventilation model.', u'Effective number of separate plumes per occupant in the occupied zone.', u'Plumes that merge together in the occupied zone count as one.'], u'type': u'real'}

        Args:
            value (float): value for IDD Field `Number of Plumes per Occupant`
                Default value: 1.0
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
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_plumes_per_occupant`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_plumes_per_occupant`')
        self._data["Number of Plumes per Occupant"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.1 ):
        """  Corresponds to IDD Field `Thermostat Height`
        Height of thermostat/temperature control sensor above floor
        
        {'pytype': 'float', u'default': '1.1', u'minimum>': '0.0', u'note': [u'Height of thermostat/temperature control sensor above floor'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                Default value: 1.1
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
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermostat_height`')
        self._data["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self._data["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1 ):
        """  Corresponds to IDD Field `Comfort Height`
        Height at which air temperature is calculated for comfort purposes
        
        {'pytype': 'float', u'default': '1.1', u'minimum>': '0.0', u'note': [u'Height at which air temperature is calculated for comfort purposes'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Comfort Height`
                Units: m
                Default value: 1.1
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
                raise ValueError('value {} need to be of type float '
                                 'for field `comfort_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `comfort_height`')
        self._data["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self._data["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4 ):
        """  Corresponds to IDD Field `Temperature Difference Threshold for Reporting`
        Minimum temperature difference between predicted upper and lower layer
        temperatures above which DV auxilliary outputs are calculated.
        These outputs are 'DV Transition Height', 'DV Fraction Min Recommended Flow Rate'
        'DV Average Temp Gradient' and 'DV Maximum Temp Gradient'.  They
        are set to negative values when the temperature difference is less than the
        threshold and the output 'DV Zone Is Mixed' is set to 1
        
        {'pytype': 'float', u'default': '0.4', u'required-field': True, u'note': [u'Minimum temperature difference between predicted upper and lower layer', u'temperatures above which DV auxilliary outputs are calculated.', u"These outputs are 'DV Transition Height', 'DV Fraction Min Recommended Flow Rate'", u"'DV Average Temp Gradient' and 'DV Maximum Temp Gradient'.  They", u'are set to negative values when the temperature difference is less than the', u"threshold and the output 'DV Zone Is Mixed' is set to 1"], u'minimum': '0.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Temperature Difference Threshold for Reporting`
                Units: deltaC
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
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_difference_threshold_for_reporting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_difference_threshold_for_reporting`')
        self._data["Temperature Difference Threshold for Reporting"] = value

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

class RoomAirSettingsCrossVentilation(object):
    """ Corresponds to IDD object `RoomAirSettings:CrossVentilation`
        This UCSD Cross Ventilation Room Air Model provides a simple model for heat transfer
        and vertical temperature profile prediction in cross ventilated rooms. The model
        distinguishes two regions in the room, the main jet region and the recirculations,
        and predicts characteristic airflow velocities and average air temperatures.
        Used with RoomAirModelType = CrossVentilation.
    
    """
    internal_name = "RoomAirSettings:CrossVentilation"
    field_count = 3
    required_fields = ["Zone Name", "Gain Distribution Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAirSettings:CrossVentilation`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Gain Distribution Schedule Name"] = None
        self._data["Airflow Region Used for Thermal Comfort Evaluation"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gain_distribution_schedule_name = None
        else:
            self.gain_distribution_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.airflow_region_used_for_thermal_comfort_evaluation = None
        else:
            self.airflow_region_used_for_thermal_comfort_evaluation = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone being described. Any existing zone name
        
        {u'note': [u'Name of Zone being described. Any existing zone name'], u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def gain_distribution_schedule_name(self):
        """Get gain_distribution_schedule_name

        Returns:
            str: the value of `gain_distribution_schedule_name` or None if not set
        """
        return self._data["Gain Distribution Schedule Name"]

    @gain_distribution_schedule_name.setter
    def gain_distribution_schedule_name(self, value=None):
        """  Corresponds to IDD Field `Gain Distribution Schedule Name`
        Distribution of the convective heat gains between the jet and recirculation zones.
        0<= Accepted Value <= 1.
        In the CV model 1 means all convective gains in the jet region.
        
        {u'note': [u'Distribution of the convective heat gains between the jet and recirculation zones.', u'0<= Accepted Value <= 1.', u'In the CV model 1 means all convective gains in the jet region.'], u'type': u'object-list', u'object-list': u'ScheduleNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Gain Distribution Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `gain_distribution_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `gain_distribution_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `gain_distribution_schedule_name`')
        self._data["Gain Distribution Schedule Name"] = value

    @property
    def airflow_region_used_for_thermal_comfort_evaluation(self):
        """Get airflow_region_used_for_thermal_comfort_evaluation

        Returns:
            str: the value of `airflow_region_used_for_thermal_comfort_evaluation` or None if not set
        """
        return self._data["Airflow Region Used for Thermal Comfort Evaluation"]

    @airflow_region_used_for_thermal_comfort_evaluation.setter
    def airflow_region_used_for_thermal_comfort_evaluation(self, value=None):
        """  Corresponds to IDD Field `Airflow Region Used for Thermal Comfort Evaluation`
        Required field whenever thermal comfort is predicted
        defines Air temperature and Airflow velocity that will be used in the Fanger model
        conditions must refer to one of the two regions: jet or recirculation
        
        {u'note': [u'Required field whenever thermal comfort is predicted', u'defines Air temperature and Airflow velocity that will be used in the Fanger model', u'conditions must refer to one of the two regions: jet or recirculation'], u'type': u'choice', u'key': [u'Jet', u'Recirculation'], 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Airflow Region Used for Thermal Comfort Evaluation`
                Accepted values are:
                      - Jet
                      - Recirculation
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `airflow_region_used_for_thermal_comfort_evaluation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airflow_region_used_for_thermal_comfort_evaluation`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airflow_region_used_for_thermal_comfort_evaluation`')
            vals = {}
            vals["jet"] = "Jet"
            vals["recirculation"] = "Recirculation"
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
                                     'field `airflow_region_used_for_thermal_comfort_evaluation`'.format(value))
            value = vals[value_lower]
        self._data["Airflow Region Used for Thermal Comfort Evaluation"] = value

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

class RoomAirSettingsUnderFloorAirDistributionInterior(object):
    """ Corresponds to IDD object `RoomAirSettings:UnderFloorAirDistributionInterior`
        This Room Air Model is applicable to interior spaces that are served by an underfloor
        air distribution system. The dominant sources of heat gain should be from people,
        equipment, and other localized sources located in the occupied part of the room.
        The model should be used with caution in zones which have large heat gains or losses
        through exterior walls or windows or which have considerable direct solar gain.
        Used with RoomAirModelType = UnderFloorAirDistributionInterior.
    
    """
    internal_name = "RoomAirSettings:UnderFloorAirDistributionInterior"
    field_count = 15
    required_fields = ["Zone Name", "Temperature Difference Threshold for Reporting", "Floor Diffuser Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAirSettings:UnderFloorAirDistributionInterior`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Number of Diffusers"] = None
        self._data["Power per Plume"] = None
        self._data["Design Effective Area of Diffuser"] = None
        self._data["Diffuser Slot Angle from Vertical"] = None
        self._data["Thermostat Height"] = None
        self._data["Comfort Height"] = None
        self._data["Temperature Difference Threshold for Reporting"] = None
        self._data["Floor Diffuser Type"] = None
        self._data["Transition Height"] = None
        self._data["Coefficient A"] = None
        self._data["Coefficient B"] = None
        self._data["Coefficient C"] = None
        self._data["Coefficient D"] = None
        self._data["Coefficient E"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_diffusers = None
        else:
            self.number_of_diffusers = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.power_per_plume = None
        else:
            self.power_per_plume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_effective_area_of_diffuser = None
        else:
            self.design_effective_area_of_diffuser = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diffuser_slot_angle_from_vertical = None
        else:
            self.diffuser_slot_angle_from_vertical = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.comfort_height = None
        else:
            self.comfort_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_difference_threshold_for_reporting = None
        else:
            self.temperature_difference_threshold_for_reporting = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_diffuser_type = None
        else:
            self.floor_diffuser_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_height = None
        else:
            self.transition_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_a = None
        else:
            self.coefficient_a = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_b = None
        else:
            self.coefficient_b = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_c = None
        else:
            self.coefficient_c = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_d = None
        else:
            self.coefficient_d = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_e = None
        else:
            self.coefficient_e = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone with underfloor air distribution
        
        {u'note': [u'Name of Zone with underfloor air distribution'], u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def number_of_diffusers(self):
        """Get number_of_diffusers

        Returns:
            float: the value of `number_of_diffusers` or None if not set
        """
        return self._data["Number of Diffusers"]

    @number_of_diffusers.setter
    def number_of_diffusers(self, value="autocalculate" ):
        """  Corresponds to IDD Field `Number of Diffusers`
        Total number of diffusers in this zone
        
        {'pytype': 'float', u'default': '"autocalculate"', u'minimum>': '0.0', u'note': [u'Total number of diffusers in this zone'], u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Diffusers`
                Default value: "autocalculate"
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Diffusers"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_diffusers`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_diffusers`')
        self._data["Number of Diffusers"] = value

    @property
    def power_per_plume(self):
        """Get power_per_plume

        Returns:
            float: the value of `power_per_plume` or None if not set
        """
        return self._data["Power per Plume"]

    @power_per_plume.setter
    def power_per_plume(self, value="autocalculate" ):
        """  Corresponds to IDD Field `Power per Plume`
        
        {'pytype': 'float', u'default': '"autocalculate"', u'minimum': '0.0', u'units': u'W', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Power per Plume`
                Units: W
                Default value: "autocalculate"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Power per Plume"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `power_per_plume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_plume`')
        self._data["Power per Plume"] = value

    @property
    def design_effective_area_of_diffuser(self):
        """Get design_effective_area_of_diffuser

        Returns:
            float: the value of `design_effective_area_of_diffuser` or None if not set
        """
        return self._data["Design Effective Area of Diffuser"]

    @design_effective_area_of_diffuser.setter
    def design_effective_area_of_diffuser(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Design Effective Area of Diffuser`
        
        {'pytype': 'float', u'default': '"Autocalculate"', u'minimum>': '0.0', u'units': u'm2', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Effective Area of Diffuser`
                Units: m2
                Default value: "Autocalculate"
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Design Effective Area of Diffuser"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_effective_area_of_diffuser`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_effective_area_of_diffuser`')
        self._data["Design Effective Area of Diffuser"] = value

    @property
    def diffuser_slot_angle_from_vertical(self):
        """Get diffuser_slot_angle_from_vertical

        Returns:
            float: the value of `diffuser_slot_angle_from_vertical` or None if not set
        """
        return self._data["Diffuser Slot Angle from Vertical"]

    @diffuser_slot_angle_from_vertical.setter
    def diffuser_slot_angle_from_vertical(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Diffuser Slot Angle from Vertical`
        
        {'pytype': 'float', u'default': '"Autocalculate"', u'maximum': '90.0', u'minimum': '0.0', u'units': u'deg', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Diffuser Slot Angle from Vertical`
                Units: deg
                Default value: "Autocalculate"
                value >= 0.0
                value <= 90.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Diffuser Slot Angle from Vertical"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `diffuser_slot_angle_from_vertical`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')
        self._data["Diffuser Slot Angle from Vertical"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.2 ):
        """  Corresponds to IDD Field `Thermostat Height`
        Height of thermostat/temperature control sensor above floor
        
        {'pytype': 'float', u'default': '1.2', u'minimum>': '0.0', u'note': [u'Height of thermostat/temperature control sensor above floor'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                Default value: 1.2
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
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermostat_height`')
        self._data["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self._data["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1 ):
        """  Corresponds to IDD Field `Comfort Height`
        Height at which air temperature is calculated for comfort purposes
        
        {'pytype': 'float', u'default': '1.1', u'minimum>': '0.0', u'note': [u'Height at which air temperature is calculated for comfort purposes'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Comfort Height`
                Units: m
                Default value: 1.1
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
                raise ValueError('value {} need to be of type float '
                                 'for field `comfort_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `comfort_height`')
        self._data["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self._data["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4 ):
        """  Corresponds to IDD Field `Temperature Difference Threshold for Reporting`
        Minimum temperature difference between predicted upper and lower layer
        temperatures above which UFAD auxilliary outputs are calculated.
        These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They
        are set to zero values when the temperature difference is less than the
        threshold and the output 'UF Zone Is Mixed' is set to 1
        
        {'pytype': 'float', u'default': '0.4', u'required-field': True, u'note': [u'Minimum temperature difference between predicted upper and lower layer', u'temperatures above which UFAD auxilliary outputs are calculated.', u"These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They", u'are set to zero values when the temperature difference is less than the', u"threshold and the output 'UF Zone Is Mixed' is set to 1"], u'minimum': '0.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Temperature Difference Threshold for Reporting`
                Units: deltaC
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
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_difference_threshold_for_reporting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_difference_threshold_for_reporting`')
        self._data["Temperature Difference Threshold for Reporting"] = value

    @property
    def floor_diffuser_type(self):
        """Get floor_diffuser_type

        Returns:
            str: the value of `floor_diffuser_type` or None if not set
        """
        return self._data["Floor Diffuser Type"]

    @floor_diffuser_type.setter
    def floor_diffuser_type(self, value="Swirl"):
        """  Corresponds to IDD Field `Floor Diffuser Type`
        
        {u'default': u'Swirl', u'type': u'choice', u'key': [u'Custom', u'Swirl', u'VariableArea', u'HorizontalSwirl', u'LinearBarGrille'], u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Floor Diffuser Type`
                Accepted values are:
                      - Custom
                      - Swirl
                      - VariableArea
                      - HorizontalSwirl
                      - LinearBarGrille
                Default value: Swirl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_diffuser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_diffuser_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `floor_diffuser_type`')
            vals = {}
            vals["custom"] = "Custom"
            vals["swirl"] = "Swirl"
            vals["variablearea"] = "VariableArea"
            vals["horizontalswirl"] = "HorizontalSwirl"
            vals["linearbargrille"] = "LinearBarGrille"
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
                                     'field `floor_diffuser_type`'.format(value))
            value = vals[value_lower]
        self._data["Floor Diffuser Type"] = value

    @property
    def transition_height(self):
        """Get transition_height

        Returns:
            float: the value of `transition_height` or None if not set
        """
        return self._data["Transition Height"]

    @transition_height.setter
    def transition_height(self, value=1.7 ):
        """  Corresponds to IDD Field `Transition Height`
        user-specified height above floor of boundary between occupied and upper subzones
        
        {'pytype': 'float', u'default': '1.7', u'minimum>': '0.0', u'note': [u'user-specified height above floor of boundary between occupied and upper subzones'], u'units': u'm', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Transition Height`
                Units: m
                Default value: 1.7
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Transition Height"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `transition_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `transition_height`')
        self._data["Transition Height"] = value

    @property
    def coefficient_a(self):
        """Get coefficient_a

        Returns:
            float: the value of `coefficient_a` or None if not set
        """
        return self._data["Coefficient A"]

    @coefficient_a.setter
    def coefficient_a(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient A`
        Coefficient A in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Coefficient A in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient A`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient A"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_a`'.format(value))
        self._data["Coefficient A"] = value

    @property
    def coefficient_b(self):
        """Get coefficient_b

        Returns:
            float: the value of `coefficient_b` or None if not set
        """
        return self._data["Coefficient B"]

    @coefficient_b.setter
    def coefficient_b(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient B`
        Coefficient B in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Coefficient B in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient B`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient B"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_b`'.format(value))
        self._data["Coefficient B"] = value

    @property
    def coefficient_c(self):
        """Get coefficient_c

        Returns:
            float: the value of `coefficient_c` or None if not set
        """
        return self._data["Coefficient C"]

    @coefficient_c.setter
    def coefficient_c(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient C`
        Coefficient C in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Coefficient C in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient C`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient C"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_c`'.format(value))
        self._data["Coefficient C"] = value

    @property
    def coefficient_d(self):
        """Get coefficient_d

        Returns:
            float: the value of `coefficient_d` or None if not set
        """
        return self._data["Coefficient D"]

    @coefficient_d.setter
    def coefficient_d(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient D`
        Coefficient D in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Coefficient D in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient D`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient D"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_d`'.format(value))
        self._data["Coefficient D"] = value

    @property
    def coefficient_e(self):
        """Get coefficient_e

        Returns:
            float: the value of `coefficient_e` or None if not set
        """
        return self._data["Coefficient E"]

    @coefficient_e.setter
    def coefficient_e(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient E`
        Coefficient E in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Coefficient E in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2', u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient E`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient E"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_e`'.format(value))
        self._data["Coefficient E"] = value

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

class RoomAirSettingsUnderFloorAirDistributionExterior(object):
    """ Corresponds to IDD object `RoomAirSettings:UnderFloorAirDistributionExterior`
        Applicable to exterior spaces that are served by an underfloor air distribution system.
        The dominant sources of heat gain should be from people, equipment, and other
        localized sources located in the occupied part of the room, as well as convective gain
        coming from a warm window. Used with RoomAirModelType = CrossVentilation.
    
    """
    internal_name = "RoomAirSettings:UnderFloorAirDistributionExterior"
    field_count = 15
    required_fields = ["Zone Name", "Temperature Difference Threshold for Reporting", "Floor Diffuser Type"]

    def __init__(self):
        """ Init data dictionary object for IDD  `RoomAirSettings:UnderFloorAirDistributionExterior`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Number of Diffusers per Zone"] = None
        self._data["Power per Plume"] = None
        self._data["Design Effective Area of Diffuser"] = None
        self._data["Diffuser Slot Angle from Vertical"] = None
        self._data["Thermostat Height"] = None
        self._data["Comfort Height"] = None
        self._data["Temperature Difference Threshold for Reporting"] = None
        self._data["Floor Diffuser Type"] = None
        self._data["Transition Height"] = None
        self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_diffusers_per_zone = None
        else:
            self.number_of_diffusers_per_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.power_per_plume = None
        else:
            self.power_per_plume = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_effective_area_of_diffuser = None
        else:
            self.design_effective_area_of_diffuser = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.diffuser_slot_angle_from_vertical = None
        else:
            self.diffuser_slot_angle_from_vertical = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_height = None
        else:
            self.thermostat_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.comfort_height = None
        else:
            self.comfort_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.temperature_difference_threshold_for_reporting = None
        else:
            self.temperature_difference_threshold_for_reporting = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.floor_diffuser_type = None
        else:
            self.floor_diffuser_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.transition_height = None
        else:
            self.transition_height = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2 = None
        else:
            self.coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `Zone Name`
        Name of Zone being described. Any existing zone name
        
        {u'note': [u'Name of Zone being described. Any existing zone name'], u'type': u'object-list', u'object-list': u'ZoneNames', u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Zone Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
        self._data["Zone Name"] = value

    @property
    def number_of_diffusers_per_zone(self):
        """Get number_of_diffusers_per_zone

        Returns:
            float: the value of `number_of_diffusers_per_zone` or None if not set
        """
        return self._data["Number of Diffusers per Zone"]

    @number_of_diffusers_per_zone.setter
    def number_of_diffusers_per_zone(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Number of Diffusers per Zone`
        
        {u'default': '"Autocalculate"', u'minimum>': '0.0', u'type': u'real', u'autocalculatable': True, 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Number of Diffusers per Zone`
                Default value: "Autocalculate"
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Number of Diffusers per Zone"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_diffusers_per_zone`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_diffusers_per_zone`')
        self._data["Number of Diffusers per Zone"] = value

    @property
    def power_per_plume(self):
        """Get power_per_plume

        Returns:
            float: the value of `power_per_plume` or None if not set
        """
        return self._data["Power per Plume"]

    @power_per_plume.setter
    def power_per_plume(self, value="autocalculate" ):
        """  Corresponds to IDD Field `Power per Plume`
        
        {'pytype': 'float', u'default': '"autocalculate"', u'minimum': '0.0', u'units': u'W', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Power per Plume`
                Units: W
                Default value: "autocalculate"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Power per Plume"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `power_per_plume`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `power_per_plume`')
        self._data["Power per Plume"] = value

    @property
    def design_effective_area_of_diffuser(self):
        """Get design_effective_area_of_diffuser

        Returns:
            float: the value of `design_effective_area_of_diffuser` or None if not set
        """
        return self._data["Design Effective Area of Diffuser"]

    @design_effective_area_of_diffuser.setter
    def design_effective_area_of_diffuser(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Design Effective Area of Diffuser`
        
        {'pytype': 'float', u'default': '"Autocalculate"', u'minimum>': '0.0', u'units': u'm2', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Design Effective Area of Diffuser`
                Units: m2
                Default value: "Autocalculate"
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Design Effective Area of Diffuser"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_effective_area_of_diffuser`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_effective_area_of_diffuser`')
        self._data["Design Effective Area of Diffuser"] = value

    @property
    def diffuser_slot_angle_from_vertical(self):
        """Get diffuser_slot_angle_from_vertical

        Returns:
            float: the value of `diffuser_slot_angle_from_vertical` or None if not set
        """
        return self._data["Diffuser Slot Angle from Vertical"]

    @diffuser_slot_angle_from_vertical.setter
    def diffuser_slot_angle_from_vertical(self, value="autocalculate" ):
        """  Corresponds to IDD Field `Diffuser Slot Angle from Vertical`
        
        {'pytype': 'float', u'default': '"autocalculate"', u'maximum': '90.0', u'minimum': '0.0', u'units': u'deg', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Diffuser Slot Angle from Vertical`
                Units: deg
                Default value: "autocalculate"
                value >= 0.0
                value <= 90.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Diffuser Slot Angle from Vertical"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `diffuser_slot_angle_from_vertical`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')
            if value > 90.0:
                raise ValueError('value need to be smaller 90.0 '
                                 'for field `diffuser_slot_angle_from_vertical`')
        self._data["Diffuser Slot Angle from Vertical"] = value

    @property
    def thermostat_height(self):
        """Get thermostat_height

        Returns:
            float: the value of `thermostat_height` or None if not set
        """
        return self._data["Thermostat Height"]

    @thermostat_height.setter
    def thermostat_height(self, value=1.2 ):
        """  Corresponds to IDD Field `Thermostat Height`
        Height of thermostat/temperature control sensor above floor
        
        {'pytype': 'float', u'default': '1.2', u'minimum>': '0.0', u'note': [u'Height of thermostat/temperature control sensor above floor'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Thermostat Height`
                Units: m
                Default value: 1.2
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
                raise ValueError('value {} need to be of type float '
                                 'for field `thermostat_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `thermostat_height`')
        self._data["Thermostat Height"] = value

    @property
    def comfort_height(self):
        """Get comfort_height

        Returns:
            float: the value of `comfort_height` or None if not set
        """
        return self._data["Comfort Height"]

    @comfort_height.setter
    def comfort_height(self, value=1.1 ):
        """  Corresponds to IDD Field `Comfort Height`
        Height at which Air temperature is calculated for comfort purposes
        
        {'pytype': 'float', u'default': '1.1', u'minimum>': '0.0', u'note': [u'Height at which Air temperature is calculated for comfort purposes'], u'units': u'm', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Comfort Height`
                Units: m
                Default value: 1.1
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
                raise ValueError('value {} need to be of type float '
                                 'for field `comfort_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `comfort_height`')
        self._data["Comfort Height"] = value

    @property
    def temperature_difference_threshold_for_reporting(self):
        """Get temperature_difference_threshold_for_reporting

        Returns:
            float: the value of `temperature_difference_threshold_for_reporting` or None if not set
        """
        return self._data["Temperature Difference Threshold for Reporting"]

    @temperature_difference_threshold_for_reporting.setter
    def temperature_difference_threshold_for_reporting(self, value=0.4 ):
        """  Corresponds to IDD Field `Temperature Difference Threshold for Reporting`
        Minimum temperature difference between upper and lower layer
        temperatures above which UFAD auxilliary outputs are calculated.
        These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They
        are set to zero values when the temperature difference is less than the
        threshold and the output 'UF Zone Is Mixed' is set to 1
        
        {'pytype': 'float', u'default': '0.4', u'required-field': True, u'note': [u'Minimum temperature difference between upper and lower layer', u'temperatures above which UFAD auxilliary outputs are calculated.', u"These outputs are 'UF Transition Height'and 'UF Average Temp Gradient'.  They", u'are set to zero values when the temperature difference is less than the', u"threshold and the output 'UF Zone Is Mixed' is set to 1"], u'minimum': '0.0', u'units': u'deltaC', u'type': u'real'}

        Args:
            value (float): value for IDD Field `Temperature Difference Threshold for Reporting`
                Units: deltaC
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
                raise ValueError('value {} need to be of type float '
                                 'for field `temperature_difference_threshold_for_reporting`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `temperature_difference_threshold_for_reporting`')
        self._data["Temperature Difference Threshold for Reporting"] = value

    @property
    def floor_diffuser_type(self):
        """Get floor_diffuser_type

        Returns:
            str: the value of `floor_diffuser_type` or None if not set
        """
        return self._data["Floor Diffuser Type"]

    @floor_diffuser_type.setter
    def floor_diffuser_type(self, value="Swirl"):
        """  Corresponds to IDD Field `Floor Diffuser Type`
        
        {u'default': u'Swirl', u'type': u'choice', u'key': [u'Custom', u'Swirl', u'VariableArea', u'HorizontalSwirl', u'LinearBarGrille'], u'required-field': True, 'pytype': 'str'}

        Args:
            value (str): value for IDD Field `Floor Diffuser Type`
                Accepted values are:
                      - Custom
                      - Swirl
                      - VariableArea
                      - HorizontalSwirl
                      - LinearBarGrille
                Default value: Swirl
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `floor_diffuser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `floor_diffuser_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `floor_diffuser_type`')
            vals = {}
            vals["custom"] = "Custom"
            vals["swirl"] = "Swirl"
            vals["variablearea"] = "VariableArea"
            vals["horizontalswirl"] = "HorizontalSwirl"
            vals["linearbargrille"] = "LinearBarGrille"
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
                                     'field `floor_diffuser_type`'.format(value))
            value = vals[value_lower]
        self._data["Floor Diffuser Type"] = value

    @property
    def transition_height(self):
        """Get transition_height

        Returns:
            float: the value of `transition_height` or None if not set
        """
        return self._data["Transition Height"]

    @transition_height.setter
    def transition_height(self, value=1.7 ):
        """  Corresponds to IDD Field `Transition Height`
        User-specified height above floor of boundary between occupied and upper subzones
        
        {'pytype': 'float', u'default': '1.7', u'minimum>': '0.0', u'note': [u'User-specified height above floor of boundary between occupied and upper subzones'], u'units': u'm', u'autocalculatable': True, u'type': u'real'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Transition Height`
                Units: m
                Default value: 1.7
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Transition Height"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `transition_height`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `transition_height`')
        self._data["Transition Height"] = value

    @property
    def coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_a_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))
        self._data["Coefficient A in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_b_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))
        self._data["Coefficient B in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_c_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))
        self._data["Coefficient C in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_d_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))
        self._data["Coefficient D in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

    @property
    def coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2(self):
        """Get coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2

        Returns:
            float: the value of `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2` or None if not set
        """
        return self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"]

    @coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2.setter
    def coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2(self, value="Autocalculate" ):
        """  Corresponds to IDD Field `Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
        Kc is the fraction of the total zone load attributable to the lower subzone
        
        {u'note': [u'Kc is the fraction of the total zone load attributable to the lower subzone'], u'default': '"Autocalculate"', u'autocalculatable': True, u'type': u'real', 'pytype': 'float'}

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2`
                Default value: "Autocalculate"
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autocalculate":
                    self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float '
                                 'for field `coefficient_e_in_formula_kc_agammab_c_dgamma_egamma2`'.format(value))
        self._data["Coefficient E in formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2"] = value

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