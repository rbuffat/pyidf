from collections import OrderedDict

class RoomAirModelType(object):
    """ Corresponds to IDD object `RoomAirModelType`
        Selects the type of room air model to be used in a given zone. If no RoomAirModelType
        object is specified then the default Mixing model (all zone air at the same
        temperature) will be used.
    """
    internal_name = "RoomAirModelType"
    field_count = 4

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `RoomAirModelType`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Room-Air Modeling Type"] = None
        self._data["Air Temperature Coupling Strategy"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.roomair_modeling_type = None
        else:
            self.roomair_modeling_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_temperature_coupling_strategy = None
        else:
            self.air_temperature_coupling_strategy = vals[i]
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
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
        """  Corresponds to IDD Field `roomair_modeling_type`
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

        Args:
            value (str): value for IDD Field `roomair_modeling_type`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `roomair_modeling_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `roomair_modeling_type`')
            vals = set()
            vals.add("Mixing")
            vals.add("UserDefined")
            vals.add("OneNodeDisplacementVentilation")
            vals.add("ThreeNodeDisplacementVentilation")
            vals.add("CrossVentilation")
            vals.add("UnderFloorAirDistributionInterior")
            vals.add("UnderFloorAirDistributionExterior")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `roomair_modeling_type`'.format(value))

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
        """  Corresponds to IDD Field `air_temperature_coupling_strategy`

        Args:
            value (str): value for IDD Field `air_temperature_coupling_strategy`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_temperature_coupling_strategy`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_temperature_coupling_strategy`')
            vals = set()
            vals.add("Direct")
            vals.add("Indirect")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `air_temperature_coupling_strategy`'.format(value))

        self._data["Air Temperature Coupling Strategy"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.roomair_modeling_type))
        out.append(self._to_str(self.air_temperature_coupling_strategy))
        return ",".join(out)