from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class ZoneHvacEquipmentList(object):
    """ Corresponds to IDD object `ZoneHVAC:EquipmentList`
        List equipment in simulation order.  Note that an ZoneHVAC:AirDistributionUnit or
        AirTerminal:SingleDuct:Uncontrolled object must be listed in this statement if there is a forced
        air system serving the zone from the air loop.
        Equipment is simulated in the order specified by Zone Equipment Cooling Sequence and
        Zone Equipment Heating or No-Load Sequence, depending on the thermostat request.
        For equipment of similar type, assign sequence 1 to the first system intended to
        serve that type of load.  For situations where one or more equipment types has limited capacity or
        limited control, order the sequence so that the most controllable piece of equipment runs last.
        For example, with a dedicated outdoor air system (DOAS), the air terminal for the DOAS
        should be assigned Heating Sequence = 1 and Cooling Sequence = 1.  Any other equipment should
        be assigned sequence 2 or higher so that it will see the net load after the DOAS air is added
        to the zone.
    """
    internal_name = "ZoneHVAC:EquipmentList"
    field_count = 1
    required_fields = ["Name"]
    extensible_fields = 4
    format = None
    min_fields = 0
    extensible_keys = ["Zone Equipment 1 Object Type", "Zone Equipment 1 Name", "Zone Equipment 1 Cooling Sequence", "Zone Equipment 1 Heating or No-Load Sequence"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:EquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
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
                                 ' for field `ZoneHvacEquipmentList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentList.name`')
        self._data["Name"] = value

    def add_extensible(self,
                       zone_equipment_1_object_type=None,
                       zone_equipment_1_name=None,
                       zone_equipment_1_cooling_sequence=None,
                       zone_equipment_1_heating_or_noload_sequence=None,
                       ):
        """ Add values for extensible fields

        Args:

            zone_equipment_1_object_type (str): value for IDD Field `Zone Equipment 1 Object Type`
                Accepted values are:
                      - ZoneHVAC:TerminalUnit:VariableRefrigerantFlow
                      - ZoneHVAC:AirDistributionUnit
                      - AirTerminal:SingleDuct:Uncontrolled
                      - ZoneHVAC:EnergyRecoveryVentilator
                      - ZoneHVAC:FourPipeFanCoil
                      - ZoneHVAC:OutdoorAirUnit
                      - ZoneHVAC:PackagedTerminalAirConditioner
                      - ZoneHVAC:PackagedTerminalHeatPump
                      - ZoneHVAC:UnitHeater
                      - ZoneHVAC:UnitVentilator
                      - ZoneHVAC:VentilatedSlab
                      - ZoneHVAC:WaterToAirHeatPump
                      - ZoneHVAC:WindowAirConditioner
                      - ZoneHVAC:Baseboard:RadiantConvective:Electric
                      - ZoneHVAC:Baseboard:RadiantConvective:Water
                      - ZoneHVAC:Baseboard:RadiantConvective:Steam
                      - ZoneHVAC:Baseboard:Convective:Electric
                      - ZoneHVAC:Baseboard:Convective:Water
                      - ZoneHVAC:HighTemperatureRadiant
                      - ZoneHVAC:LowTemperatureRadiant:VariableFlow
                      - ZoneHVAC:LowTemperatureRadiant:ConstantFlow
                      - ZoneHVAC:LowTemperatureRadiant:Electric
                      - ZoneHVAC:Dehumidifier:DX
                      - ZoneHVAC:IdealLoadsAirSystem
                      - ZoneHVAC:RefrigerationChillerSet
                      - Fan:ZoneExhaust
                      - WaterHeater:HeatPump
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            zone_equipment_1_name (str): value for IDD Field `Zone Equipment 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            zone_equipment_1_cooling_sequence (int): value for IDD Field `Zone Equipment 1 Cooling Sequence`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            zone_equipment_1_heating_or_noload_sequence (int): value for IDD Field `Zone Equipment 1 Heating or No-Load Sequence`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_zone_equipment_1_object_type(zone_equipment_1_object_type))
        vals.append(self._check_zone_equipment_1_name(zone_equipment_1_name))
        vals.append(self._check_zone_equipment_1_cooling_sequence(zone_equipment_1_cooling_sequence))
        vals.append(self._check_zone_equipment_1_heating_or_noload_sequence(zone_equipment_1_heating_or_noload_sequence))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_zone_equipment_1_object_type(self, value):
        """ Validates falue of field `Zone Equipment 1 Object Type`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacEquipmentList.zone_equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentList.zone_equipment_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentList.zone_equipment_1_object_type`')
            vals = {}
            vals["zonehvac:terminalunit:variablerefrigerantflow"] = "ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"
            vals["zonehvac:airdistributionunit"] = "ZoneHVAC:AirDistributionUnit"
            vals["airterminal:singleduct:uncontrolled"] = "AirTerminal:SingleDuct:Uncontrolled"
            vals["zonehvac:energyrecoveryventilator"] = "ZoneHVAC:EnergyRecoveryVentilator"
            vals["zonehvac:fourpipefancoil"] = "ZoneHVAC:FourPipeFanCoil"
            vals["zonehvac:outdoorairunit"] = "ZoneHVAC:OutdoorAirUnit"
            vals["zonehvac:packagedterminalairconditioner"] = "ZoneHVAC:PackagedTerminalAirConditioner"
            vals["zonehvac:packagedterminalheatpump"] = "ZoneHVAC:PackagedTerminalHeatPump"
            vals["zonehvac:unitheater"] = "ZoneHVAC:UnitHeater"
            vals["zonehvac:unitventilator"] = "ZoneHVAC:UnitVentilator"
            vals["zonehvac:ventilatedslab"] = "ZoneHVAC:VentilatedSlab"
            vals["zonehvac:watertoairheatpump"] = "ZoneHVAC:WaterToAirHeatPump"
            vals["zonehvac:windowairconditioner"] = "ZoneHVAC:WindowAirConditioner"
            vals["zonehvac:baseboard:radiantconvective:electric"] = "ZoneHVAC:Baseboard:RadiantConvective:Electric"
            vals["zonehvac:baseboard:radiantconvective:water"] = "ZoneHVAC:Baseboard:RadiantConvective:Water"
            vals["zonehvac:baseboard:radiantconvective:steam"] = "ZoneHVAC:Baseboard:RadiantConvective:Steam"
            vals["zonehvac:baseboard:convective:electric"] = "ZoneHVAC:Baseboard:Convective:Electric"
            vals["zonehvac:baseboard:convective:water"] = "ZoneHVAC:Baseboard:Convective:Water"
            vals["zonehvac:hightemperatureradiant"] = "ZoneHVAC:HighTemperatureRadiant"
            vals["zonehvac:lowtemperatureradiant:variableflow"] = "ZoneHVAC:LowTemperatureRadiant:VariableFlow"
            vals["zonehvac:lowtemperatureradiant:constantflow"] = "ZoneHVAC:LowTemperatureRadiant:ConstantFlow"
            vals["zonehvac:lowtemperatureradiant:electric"] = "ZoneHVAC:LowTemperatureRadiant:Electric"
            vals["zonehvac:dehumidifier:dx"] = "ZoneHVAC:Dehumidifier:DX"
            vals["zonehvac:idealloadsairsystem"] = "ZoneHVAC:IdealLoadsAirSystem"
            vals["zonehvac:refrigerationchillerset"] = "ZoneHVAC:RefrigerationChillerSet"
            vals["fan:zoneexhaust"] = "Fan:ZoneExhaust"
            vals["waterheater:heatpump"] = "WaterHeater:HeatPump"
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
                                     'field `ZoneHvacEquipmentList.zone_equipment_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `ZoneHvacEquipmentList.zone_equipment_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        return value

    def _check_zone_equipment_1_name(self, value):
        """ Validates falue of field `Zone Equipment 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacEquipmentList.zone_equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentList.zone_equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentList.zone_equipment_1_name`')
        return value

    def _check_zone_equipment_1_cooling_sequence(self, value):
        """ Validates falue of field `Zone Equipment 1 Cooling Sequence`
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ZoneHvacEquipmentList.zone_equipment_1_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ZoneHvacEquipmentList.zone_equipment_1_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ZoneHvacEquipmentList.zone_equipment_1_cooling_sequence`')
        return value

    def _check_zone_equipment_1_heating_or_noload_sequence(self, value):
        """ Validates falue of field `Zone Equipment 1 Heating or No-Load Sequence`
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                if not self.strict:
                    try:
                        conv_value = int(float(value))
                        logger.warn('Cast float {} to int {}, precision may be lost '
                                     'for field `ZoneHvacEquipmentList.zone_equipment_1_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `ZoneHvacEquipmentList.zone_equipment_1_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `ZoneHvacEquipmentList.zone_equipment_1_heating_or_noload_sequence`')
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
                    raise ValueError("Required field ZoneHvacEquipmentList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacEquipmentList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacEquipmentList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacEquipmentList: {} / {}".format(out_fields,
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

class ZoneHvacEquipmentConnections(object):
    """ Corresponds to IDD object `ZoneHVAC:EquipmentConnections`
        Specifies the HVAC equipment connections for a zone. Node names are specified for the
        zone air node, air inlet nodes, air exhaust nodes, and the air return node. A zone
        equipment list is referenced which lists all HVAC equipment connected to the zone.
    """
    internal_name = "ZoneHVAC:EquipmentConnections"
    field_count = 6
    required_fields = ["Zone Name", "Zone Conditioning Equipment List Name", "Zone Air Node Name", "Zone Return Air Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:EquipmentConnections`
        """
        self._data = OrderedDict()
        self._data["Zone Name"] = None
        self._data["Zone Conditioning Equipment List Name"] = None
        self._data["Zone Air Inlet Node or NodeList Name"] = None
        self._data["Zone Air Exhaust Node or NodeList Name"] = None
        self._data["Zone Air Node Name"] = None
        self._data["Zone Return Air Node Name"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_conditioning_equipment_list_name = None
        else:
            self.zone_conditioning_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_air_inlet_node_or_nodelist_name = None
        else:
            self.zone_air_inlet_node_or_nodelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_air_exhaust_node_or_nodelist_name = None
        else:
            self.zone_air_exhaust_node_or_nodelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_air_node_name = None
        else:
            self.zone_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_return_air_node_name = None
        else:
            self.zone_return_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        self.strict = old_strict

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
                raise ValueError('value {} need to be of type str'
                                 ' for field `ZoneHvacEquipmentConnections.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentConnections.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentConnections.zone_name`')
        self._data["Zone Name"] = value

    @property
    def zone_conditioning_equipment_list_name(self):
        """Get zone_conditioning_equipment_list_name

        Returns:
            str: the value of `zone_conditioning_equipment_list_name` or None if not set
        """
        return self._data["Zone Conditioning Equipment List Name"]

    @zone_conditioning_equipment_list_name.setter
    def zone_conditioning_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Zone Conditioning Equipment List Name`
        Enter the name of a ZoneHVAC:EquipmentList object.

        Args:
            value (str): value for IDD Field `Zone Conditioning Equipment List Name`
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
                                 ' for field `ZoneHvacEquipmentConnections.zone_conditioning_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentConnections.zone_conditioning_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentConnections.zone_conditioning_equipment_list_name`')
        self._data["Zone Conditioning Equipment List Name"] = value

    @property
    def zone_air_inlet_node_or_nodelist_name(self):
        """Get zone_air_inlet_node_or_nodelist_name

        Returns:
            str: the value of `zone_air_inlet_node_or_nodelist_name` or None if not set
        """
        return self._data["Zone Air Inlet Node or NodeList Name"]

    @zone_air_inlet_node_or_nodelist_name.setter
    def zone_air_inlet_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Zone Air Inlet Node or NodeList Name`

        Args:
            value (str): value for IDD Field `Zone Air Inlet Node or NodeList Name`
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
                                 ' for field `ZoneHvacEquipmentConnections.zone_air_inlet_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentConnections.zone_air_inlet_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentConnections.zone_air_inlet_node_or_nodelist_name`')
        self._data["Zone Air Inlet Node or NodeList Name"] = value

    @property
    def zone_air_exhaust_node_or_nodelist_name(self):
        """Get zone_air_exhaust_node_or_nodelist_name

        Returns:
            str: the value of `zone_air_exhaust_node_or_nodelist_name` or None if not set
        """
        return self._data["Zone Air Exhaust Node or NodeList Name"]

    @zone_air_exhaust_node_or_nodelist_name.setter
    def zone_air_exhaust_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Zone Air Exhaust Node or NodeList Name`

        Args:
            value (str): value for IDD Field `Zone Air Exhaust Node or NodeList Name`
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
                                 ' for field `ZoneHvacEquipmentConnections.zone_air_exhaust_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentConnections.zone_air_exhaust_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentConnections.zone_air_exhaust_node_or_nodelist_name`')
        self._data["Zone Air Exhaust Node or NodeList Name"] = value

    @property
    def zone_air_node_name(self):
        """Get zone_air_node_name

        Returns:
            str: the value of `zone_air_node_name` or None if not set
        """
        return self._data["Zone Air Node Name"]

    @zone_air_node_name.setter
    def zone_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Air Node Name`

        Args:
            value (str): value for IDD Field `Zone Air Node Name`
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
                                 ' for field `ZoneHvacEquipmentConnections.zone_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentConnections.zone_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentConnections.zone_air_node_name`')
        self._data["Zone Air Node Name"] = value

    @property
    def zone_return_air_node_name(self):
        """Get zone_return_air_node_name

        Returns:
            str: the value of `zone_return_air_node_name` or None if not set
        """
        return self._data["Zone Return Air Node Name"]

    @zone_return_air_node_name.setter
    def zone_return_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Return Air Node Name`

        Args:
            value (str): value for IDD Field `Zone Return Air Node Name`
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
                                 ' for field `ZoneHvacEquipmentConnections.zone_return_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ZoneHvacEquipmentConnections.zone_return_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `ZoneHvacEquipmentConnections.zone_return_air_node_name`')
        self._data["Zone Return Air Node Name"] = value

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
                    raise ValueError("Required field ZoneHvacEquipmentConnections:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field ZoneHvacEquipmentConnections:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for ZoneHvacEquipmentConnections: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for ZoneHvacEquipmentConnections: {} / {}".format(out_fields,
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