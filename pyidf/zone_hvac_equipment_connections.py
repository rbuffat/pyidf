from collections import OrderedDict
import logging
import re

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
    field_count = 73
    required_fields = ["Name", "Zone Equipment 1 Object Type", "Zone Equipment 1 Name", "Zone Equipment 1 Cooling Sequence", "Zone Equipment 1 Heating or No-Load Sequence"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneHVAC:EquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Equipment 1 Object Type"] = None
        self._data["Zone Equipment 1 Name"] = None
        self._data["Zone Equipment 1 Cooling Sequence"] = None
        self._data["Zone Equipment 1 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 2 Object Type"] = None
        self._data["Zone Equipment 2 Name"] = None
        self._data["Zone Equipment 2 Cooling Sequence"] = None
        self._data["Zone Equipment 2 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 3 Object Type"] = None
        self._data["Zone Equipment 3 Name"] = None
        self._data["Zone Equipment 3 Cooling Sequence"] = None
        self._data["Zone Equipment 3 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 4 Object Type"] = None
        self._data["Zone Equipment 4 Name"] = None
        self._data["Zone Equipment 4 Cooling Sequence"] = None
        self._data["Zone Equipment 4 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 5 Object Type"] = None
        self._data["Zone Equipment 5 Name"] = None
        self._data["Zone Equipment 5 Cooling Sequence"] = None
        self._data["Zone Equipment 5 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 6 Object Type"] = None
        self._data["Zone Equipment 6 Name"] = None
        self._data["Zone Equipment 6 Cooling Sequence"] = None
        self._data["Zone Equipment 6 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 7 Object Type"] = None
        self._data["Zone Equipment 7 Name"] = None
        self._data["Zone Equipment 7 Cooling Sequence"] = None
        self._data["Zone Equipment 7 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 8 Object Type"] = None
        self._data["Zone Equipment 8 Name"] = None
        self._data["Zone Equipment 8 Cooling Sequence"] = None
        self._data["Zone Equipment 8 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 9 Object Type"] = None
        self._data["Zone Equipment 9 Name"] = None
        self._data["Zone Equipment 9 Cooling Sequence"] = None
        self._data["Zone Equipment 9 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 10 Object Type"] = None
        self._data["Zone Equipment 10 Name"] = None
        self._data["Zone Equipment 10 Cooling Sequence"] = None
        self._data["Zone Equipment 10 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 11 Object Type"] = None
        self._data["Zone Equipment 11 Name"] = None
        self._data["Zone Equipment 11 Cooling Sequence"] = None
        self._data["Zone Equipment 11 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 12 Object Type"] = None
        self._data["Zone Equipment 12 Name"] = None
        self._data["Zone Equipment 12 Cooling Sequence"] = None
        self._data["Zone Equipment 12 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 13 Object Type"] = None
        self._data["Zone Equipment 13 Name"] = None
        self._data["Zone Equipment 13 Cooling Sequence"] = None
        self._data["Zone Equipment 13 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 14 Object Type"] = None
        self._data["Zone Equipment 14 Name"] = None
        self._data["Zone Equipment 14 Cooling Sequence"] = None
        self._data["Zone Equipment 14 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 15 Object Type"] = None
        self._data["Zone Equipment 15 Name"] = None
        self._data["Zone Equipment 15 Cooling Sequence"] = None
        self._data["Zone Equipment 15 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 16 Object Type"] = None
        self._data["Zone Equipment 16 Name"] = None
        self._data["Zone Equipment 16 Cooling Sequence"] = None
        self._data["Zone Equipment 16 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 17 Object Type"] = None
        self._data["Zone Equipment 17 Name"] = None
        self._data["Zone Equipment 17 Cooling Sequence"] = None
        self._data["Zone Equipment 17 Heating or No-Load Sequence"] = None
        self._data["Zone Equipment 18 Object Type"] = None
        self._data["Zone Equipment 18 Name"] = None
        self._data["Zone Equipment 18 Cooling Sequence"] = None
        self._data["Zone Equipment 18 Heating or No-Load Sequence"] = None
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
            self.zone_equipment_1_object_type = None
        else:
            self.zone_equipment_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_1_name = None
        else:
            self.zone_equipment_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_1_cooling_sequence = None
        else:
            self.zone_equipment_1_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_1_heating_or_noload_sequence = None
        else:
            self.zone_equipment_1_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_2_object_type = None
        else:
            self.zone_equipment_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_2_name = None
        else:
            self.zone_equipment_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_2_cooling_sequence = None
        else:
            self.zone_equipment_2_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_2_heating_or_noload_sequence = None
        else:
            self.zone_equipment_2_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_3_object_type = None
        else:
            self.zone_equipment_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_3_name = None
        else:
            self.zone_equipment_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_3_cooling_sequence = None
        else:
            self.zone_equipment_3_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_3_heating_or_noload_sequence = None
        else:
            self.zone_equipment_3_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_4_object_type = None
        else:
            self.zone_equipment_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_4_name = None
        else:
            self.zone_equipment_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_4_cooling_sequence = None
        else:
            self.zone_equipment_4_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_4_heating_or_noload_sequence = None
        else:
            self.zone_equipment_4_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_5_object_type = None
        else:
            self.zone_equipment_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_5_name = None
        else:
            self.zone_equipment_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_5_cooling_sequence = None
        else:
            self.zone_equipment_5_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_5_heating_or_noload_sequence = None
        else:
            self.zone_equipment_5_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_6_object_type = None
        else:
            self.zone_equipment_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_6_name = None
        else:
            self.zone_equipment_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_6_cooling_sequence = None
        else:
            self.zone_equipment_6_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_6_heating_or_noload_sequence = None
        else:
            self.zone_equipment_6_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_7_object_type = None
        else:
            self.zone_equipment_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_7_name = None
        else:
            self.zone_equipment_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_7_cooling_sequence = None
        else:
            self.zone_equipment_7_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_7_heating_or_noload_sequence = None
        else:
            self.zone_equipment_7_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_8_object_type = None
        else:
            self.zone_equipment_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_8_name = None
        else:
            self.zone_equipment_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_8_cooling_sequence = None
        else:
            self.zone_equipment_8_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_8_heating_or_noload_sequence = None
        else:
            self.zone_equipment_8_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_9_object_type = None
        else:
            self.zone_equipment_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_9_name = None
        else:
            self.zone_equipment_9_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_9_cooling_sequence = None
        else:
            self.zone_equipment_9_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_9_heating_or_noload_sequence = None
        else:
            self.zone_equipment_9_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_10_object_type = None
        else:
            self.zone_equipment_10_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_10_name = None
        else:
            self.zone_equipment_10_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_10_cooling_sequence = None
        else:
            self.zone_equipment_10_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_10_heating_or_noload_sequence = None
        else:
            self.zone_equipment_10_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_11_object_type = None
        else:
            self.zone_equipment_11_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_11_name = None
        else:
            self.zone_equipment_11_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_11_cooling_sequence = None
        else:
            self.zone_equipment_11_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_11_heating_or_noload_sequence = None
        else:
            self.zone_equipment_11_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_12_object_type = None
        else:
            self.zone_equipment_12_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_12_name = None
        else:
            self.zone_equipment_12_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_12_cooling_sequence = None
        else:
            self.zone_equipment_12_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_12_heating_or_noload_sequence = None
        else:
            self.zone_equipment_12_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_13_object_type = None
        else:
            self.zone_equipment_13_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_13_name = None
        else:
            self.zone_equipment_13_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_13_cooling_sequence = None
        else:
            self.zone_equipment_13_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_13_heating_or_noload_sequence = None
        else:
            self.zone_equipment_13_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_14_object_type = None
        else:
            self.zone_equipment_14_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_14_name = None
        else:
            self.zone_equipment_14_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_14_cooling_sequence = None
        else:
            self.zone_equipment_14_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_14_heating_or_noload_sequence = None
        else:
            self.zone_equipment_14_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_15_object_type = None
        else:
            self.zone_equipment_15_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_15_name = None
        else:
            self.zone_equipment_15_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_15_cooling_sequence = None
        else:
            self.zone_equipment_15_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_15_heating_or_noload_sequence = None
        else:
            self.zone_equipment_15_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_16_object_type = None
        else:
            self.zone_equipment_16_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_16_name = None
        else:
            self.zone_equipment_16_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_16_cooling_sequence = None
        else:
            self.zone_equipment_16_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_16_heating_or_noload_sequence = None
        else:
            self.zone_equipment_16_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_17_object_type = None
        else:
            self.zone_equipment_17_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_17_name = None
        else:
            self.zone_equipment_17_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_17_cooling_sequence = None
        else:
            self.zone_equipment_17_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_17_heating_or_noload_sequence = None
        else:
            self.zone_equipment_17_heating_or_noload_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_18_object_type = None
        else:
            self.zone_equipment_18_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_18_name = None
        else:
            self.zone_equipment_18_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_18_cooling_sequence = None
        else:
            self.zone_equipment_18_cooling_sequence = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_equipment_18_heating_or_noload_sequence = None
        else:
            self.zone_equipment_18_heating_or_noload_sequence = vals[i]
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
    def zone_equipment_1_object_type(self):
        """Get zone_equipment_1_object_type

        Returns:
            str: the value of `zone_equipment_1_object_type` or None if not set
        """
        return self._data["Zone Equipment 1 Object Type"]

    @zone_equipment_1_object_type.setter
    def zone_equipment_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 1 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_1_object_type`')
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
                                     'field `zone_equipment_1_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 1 Object Type"] = value

    @property
    def zone_equipment_1_name(self):
        """Get zone_equipment_1_name

        Returns:
            str: the value of `zone_equipment_1_name` or None if not set
        """
        return self._data["Zone Equipment 1 Name"]

    @zone_equipment_1_name.setter
    def zone_equipment_1_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 1 Name`
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
                                 'for field `zone_equipment_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_1_name`')
        self._data["Zone Equipment 1 Name"] = value

    @property
    def zone_equipment_1_cooling_sequence(self):
        """Get zone_equipment_1_cooling_sequence

        Returns:
            int: the value of `zone_equipment_1_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 1 Cooling Sequence"]

    @zone_equipment_1_cooling_sequence.setter
    def zone_equipment_1_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 1 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 1 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_1_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_1_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_1_cooling_sequence`')
        self._data["Zone Equipment 1 Cooling Sequence"] = value

    @property
    def zone_equipment_1_heating_or_noload_sequence(self):
        """Get zone_equipment_1_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_1_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 1 Heating or No-Load Sequence"]

    @zone_equipment_1_heating_or_noload_sequence.setter
    def zone_equipment_1_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 1 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 1 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_1_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_1_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_1_heating_or_noload_sequence`')
        self._data["Zone Equipment 1 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_2_object_type(self):
        """Get zone_equipment_2_object_type

        Returns:
            str: the value of `zone_equipment_2_object_type` or None if not set
        """
        return self._data["Zone Equipment 2 Object Type"]

    @zone_equipment_2_object_type.setter
    def zone_equipment_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 2 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_2_object_type`')
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
                                     'field `zone_equipment_2_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_2_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 2 Object Type"] = value

    @property
    def zone_equipment_2_name(self):
        """Get zone_equipment_2_name

        Returns:
            str: the value of `zone_equipment_2_name` or None if not set
        """
        return self._data["Zone Equipment 2 Name"]

    @zone_equipment_2_name.setter
    def zone_equipment_2_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 2 Name`
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
                                 'for field `zone_equipment_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_2_name`')
        self._data["Zone Equipment 2 Name"] = value

    @property
    def zone_equipment_2_cooling_sequence(self):
        """Get zone_equipment_2_cooling_sequence

        Returns:
            int: the value of `zone_equipment_2_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 2 Cooling Sequence"]

    @zone_equipment_2_cooling_sequence.setter
    def zone_equipment_2_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 2 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 2 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_2_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_2_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_2_cooling_sequence`')
        self._data["Zone Equipment 2 Cooling Sequence"] = value

    @property
    def zone_equipment_2_heating_or_noload_sequence(self):
        """Get zone_equipment_2_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_2_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 2 Heating or No-Load Sequence"]

    @zone_equipment_2_heating_or_noload_sequence.setter
    def zone_equipment_2_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 2 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 2 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_2_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_2_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_2_heating_or_noload_sequence`')
        self._data["Zone Equipment 2 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_3_object_type(self):
        """Get zone_equipment_3_object_type

        Returns:
            str: the value of `zone_equipment_3_object_type` or None if not set
        """
        return self._data["Zone Equipment 3 Object Type"]

    @zone_equipment_3_object_type.setter
    def zone_equipment_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 3 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_3_object_type`')
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
                                     'field `zone_equipment_3_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_3_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 3 Object Type"] = value

    @property
    def zone_equipment_3_name(self):
        """Get zone_equipment_3_name

        Returns:
            str: the value of `zone_equipment_3_name` or None if not set
        """
        return self._data["Zone Equipment 3 Name"]

    @zone_equipment_3_name.setter
    def zone_equipment_3_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 3 Name`
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
                                 'for field `zone_equipment_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_3_name`')
        self._data["Zone Equipment 3 Name"] = value

    @property
    def zone_equipment_3_cooling_sequence(self):
        """Get zone_equipment_3_cooling_sequence

        Returns:
            int: the value of `zone_equipment_3_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 3 Cooling Sequence"]

    @zone_equipment_3_cooling_sequence.setter
    def zone_equipment_3_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 3 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 3 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_3_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_3_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_3_cooling_sequence`')
        self._data["Zone Equipment 3 Cooling Sequence"] = value

    @property
    def zone_equipment_3_heating_or_noload_sequence(self):
        """Get zone_equipment_3_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_3_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 3 Heating or No-Load Sequence"]

    @zone_equipment_3_heating_or_noload_sequence.setter
    def zone_equipment_3_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 3 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 3 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_3_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_3_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_3_heating_or_noload_sequence`')
        self._data["Zone Equipment 3 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_4_object_type(self):
        """Get zone_equipment_4_object_type

        Returns:
            str: the value of `zone_equipment_4_object_type` or None if not set
        """
        return self._data["Zone Equipment 4 Object Type"]

    @zone_equipment_4_object_type.setter
    def zone_equipment_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 4 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_4_object_type`')
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
                                     'field `zone_equipment_4_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_4_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 4 Object Type"] = value

    @property
    def zone_equipment_4_name(self):
        """Get zone_equipment_4_name

        Returns:
            str: the value of `zone_equipment_4_name` or None if not set
        """
        return self._data["Zone Equipment 4 Name"]

    @zone_equipment_4_name.setter
    def zone_equipment_4_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 4 Name`
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
                                 'for field `zone_equipment_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_4_name`')
        self._data["Zone Equipment 4 Name"] = value

    @property
    def zone_equipment_4_cooling_sequence(self):
        """Get zone_equipment_4_cooling_sequence

        Returns:
            int: the value of `zone_equipment_4_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 4 Cooling Sequence"]

    @zone_equipment_4_cooling_sequence.setter
    def zone_equipment_4_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 4 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 4 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_4_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_4_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_4_cooling_sequence`')
        self._data["Zone Equipment 4 Cooling Sequence"] = value

    @property
    def zone_equipment_4_heating_or_noload_sequence(self):
        """Get zone_equipment_4_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_4_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 4 Heating or No-Load Sequence"]

    @zone_equipment_4_heating_or_noload_sequence.setter
    def zone_equipment_4_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 4 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 4 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_4_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_4_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_4_heating_or_noload_sequence`')
        self._data["Zone Equipment 4 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_5_object_type(self):
        """Get zone_equipment_5_object_type

        Returns:
            str: the value of `zone_equipment_5_object_type` or None if not set
        """
        return self._data["Zone Equipment 5 Object Type"]

    @zone_equipment_5_object_type.setter
    def zone_equipment_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 5 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_5_object_type`')
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
                                     'field `zone_equipment_5_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_5_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 5 Object Type"] = value

    @property
    def zone_equipment_5_name(self):
        """Get zone_equipment_5_name

        Returns:
            str: the value of `zone_equipment_5_name` or None if not set
        """
        return self._data["Zone Equipment 5 Name"]

    @zone_equipment_5_name.setter
    def zone_equipment_5_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 5 Name`
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
                                 'for field `zone_equipment_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_5_name`')
        self._data["Zone Equipment 5 Name"] = value

    @property
    def zone_equipment_5_cooling_sequence(self):
        """Get zone_equipment_5_cooling_sequence

        Returns:
            int: the value of `zone_equipment_5_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 5 Cooling Sequence"]

    @zone_equipment_5_cooling_sequence.setter
    def zone_equipment_5_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 5 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 5 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_5_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_5_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_5_cooling_sequence`')
        self._data["Zone Equipment 5 Cooling Sequence"] = value

    @property
    def zone_equipment_5_heating_or_noload_sequence(self):
        """Get zone_equipment_5_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_5_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 5 Heating or No-Load Sequence"]

    @zone_equipment_5_heating_or_noload_sequence.setter
    def zone_equipment_5_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 5 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 5 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_5_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_5_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_5_heating_or_noload_sequence`')
        self._data["Zone Equipment 5 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_6_object_type(self):
        """Get zone_equipment_6_object_type

        Returns:
            str: the value of `zone_equipment_6_object_type` or None if not set
        """
        return self._data["Zone Equipment 6 Object Type"]

    @zone_equipment_6_object_type.setter
    def zone_equipment_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 6 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_6_object_type`')
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
                                     'field `zone_equipment_6_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_6_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 6 Object Type"] = value

    @property
    def zone_equipment_6_name(self):
        """Get zone_equipment_6_name

        Returns:
            str: the value of `zone_equipment_6_name` or None if not set
        """
        return self._data["Zone Equipment 6 Name"]

    @zone_equipment_6_name.setter
    def zone_equipment_6_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 6 Name`
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
                                 'for field `zone_equipment_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_6_name`')
        self._data["Zone Equipment 6 Name"] = value

    @property
    def zone_equipment_6_cooling_sequence(self):
        """Get zone_equipment_6_cooling_sequence

        Returns:
            int: the value of `zone_equipment_6_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 6 Cooling Sequence"]

    @zone_equipment_6_cooling_sequence.setter
    def zone_equipment_6_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 6 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 6 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_6_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_6_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_6_cooling_sequence`')
        self._data["Zone Equipment 6 Cooling Sequence"] = value

    @property
    def zone_equipment_6_heating_or_noload_sequence(self):
        """Get zone_equipment_6_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_6_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 6 Heating or No-Load Sequence"]

    @zone_equipment_6_heating_or_noload_sequence.setter
    def zone_equipment_6_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 6 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 6 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_6_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_6_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_6_heating_or_noload_sequence`')
        self._data["Zone Equipment 6 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_7_object_type(self):
        """Get zone_equipment_7_object_type

        Returns:
            str: the value of `zone_equipment_7_object_type` or None if not set
        """
        return self._data["Zone Equipment 7 Object Type"]

    @zone_equipment_7_object_type.setter
    def zone_equipment_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 7 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_7_object_type`')
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
                                     'field `zone_equipment_7_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_7_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 7 Object Type"] = value

    @property
    def zone_equipment_7_name(self):
        """Get zone_equipment_7_name

        Returns:
            str: the value of `zone_equipment_7_name` or None if not set
        """
        return self._data["Zone Equipment 7 Name"]

    @zone_equipment_7_name.setter
    def zone_equipment_7_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 7 Name`
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
                                 'for field `zone_equipment_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_7_name`')
        self._data["Zone Equipment 7 Name"] = value

    @property
    def zone_equipment_7_cooling_sequence(self):
        """Get zone_equipment_7_cooling_sequence

        Returns:
            int: the value of `zone_equipment_7_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 7 Cooling Sequence"]

    @zone_equipment_7_cooling_sequence.setter
    def zone_equipment_7_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 7 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 7 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_7_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_7_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_7_cooling_sequence`')
        self._data["Zone Equipment 7 Cooling Sequence"] = value

    @property
    def zone_equipment_7_heating_or_noload_sequence(self):
        """Get zone_equipment_7_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_7_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 7 Heating or No-Load Sequence"]

    @zone_equipment_7_heating_or_noload_sequence.setter
    def zone_equipment_7_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 7 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 7 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_7_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_7_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_7_heating_or_noload_sequence`')
        self._data["Zone Equipment 7 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_8_object_type(self):
        """Get zone_equipment_8_object_type

        Returns:
            str: the value of `zone_equipment_8_object_type` or None if not set
        """
        return self._data["Zone Equipment 8 Object Type"]

    @zone_equipment_8_object_type.setter
    def zone_equipment_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 8 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_8_object_type`')
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
                                     'field `zone_equipment_8_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_8_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 8 Object Type"] = value

    @property
    def zone_equipment_8_name(self):
        """Get zone_equipment_8_name

        Returns:
            str: the value of `zone_equipment_8_name` or None if not set
        """
        return self._data["Zone Equipment 8 Name"]

    @zone_equipment_8_name.setter
    def zone_equipment_8_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 8 Name`
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
                                 'for field `zone_equipment_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_8_name`')
        self._data["Zone Equipment 8 Name"] = value

    @property
    def zone_equipment_8_cooling_sequence(self):
        """Get zone_equipment_8_cooling_sequence

        Returns:
            int: the value of `zone_equipment_8_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 8 Cooling Sequence"]

    @zone_equipment_8_cooling_sequence.setter
    def zone_equipment_8_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 8 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 8 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_8_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_8_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_8_cooling_sequence`')
        self._data["Zone Equipment 8 Cooling Sequence"] = value

    @property
    def zone_equipment_8_heating_or_noload_sequence(self):
        """Get zone_equipment_8_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_8_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 8 Heating or No-Load Sequence"]

    @zone_equipment_8_heating_or_noload_sequence.setter
    def zone_equipment_8_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 8 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 8 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_8_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_8_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_8_heating_or_noload_sequence`')
        self._data["Zone Equipment 8 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_9_object_type(self):
        """Get zone_equipment_9_object_type

        Returns:
            str: the value of `zone_equipment_9_object_type` or None if not set
        """
        return self._data["Zone Equipment 9 Object Type"]

    @zone_equipment_9_object_type.setter
    def zone_equipment_9_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 9 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_9_object_type`')
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
                                     'field `zone_equipment_9_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_9_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 9 Object Type"] = value

    @property
    def zone_equipment_9_name(self):
        """Get zone_equipment_9_name

        Returns:
            str: the value of `zone_equipment_9_name` or None if not set
        """
        return self._data["Zone Equipment 9 Name"]

    @zone_equipment_9_name.setter
    def zone_equipment_9_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 9 Name`
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
                                 'for field `zone_equipment_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_9_name`')
        self._data["Zone Equipment 9 Name"] = value

    @property
    def zone_equipment_9_cooling_sequence(self):
        """Get zone_equipment_9_cooling_sequence

        Returns:
            int: the value of `zone_equipment_9_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 9 Cooling Sequence"]

    @zone_equipment_9_cooling_sequence.setter
    def zone_equipment_9_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 9 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 9 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_9_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_9_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_9_cooling_sequence`')
        self._data["Zone Equipment 9 Cooling Sequence"] = value

    @property
    def zone_equipment_9_heating_or_noload_sequence(self):
        """Get zone_equipment_9_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_9_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 9 Heating or No-Load Sequence"]

    @zone_equipment_9_heating_or_noload_sequence.setter
    def zone_equipment_9_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 9 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 9 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_9_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_9_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_9_heating_or_noload_sequence`')
        self._data["Zone Equipment 9 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_10_object_type(self):
        """Get zone_equipment_10_object_type

        Returns:
            str: the value of `zone_equipment_10_object_type` or None if not set
        """
        return self._data["Zone Equipment 10 Object Type"]

    @zone_equipment_10_object_type.setter
    def zone_equipment_10_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 10 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_10_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_10_object_type`')
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
                                     'field `zone_equipment_10_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_10_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 10 Object Type"] = value

    @property
    def zone_equipment_10_name(self):
        """Get zone_equipment_10_name

        Returns:
            str: the value of `zone_equipment_10_name` or None if not set
        """
        return self._data["Zone Equipment 10 Name"]

    @zone_equipment_10_name.setter
    def zone_equipment_10_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 10 Name`
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
                                 'for field `zone_equipment_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_10_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_10_name`')
        self._data["Zone Equipment 10 Name"] = value

    @property
    def zone_equipment_10_cooling_sequence(self):
        """Get zone_equipment_10_cooling_sequence

        Returns:
            int: the value of `zone_equipment_10_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 10 Cooling Sequence"]

    @zone_equipment_10_cooling_sequence.setter
    def zone_equipment_10_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 10 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 10 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_10_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_10_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_10_cooling_sequence`')
        self._data["Zone Equipment 10 Cooling Sequence"] = value

    @property
    def zone_equipment_10_heating_or_noload_sequence(self):
        """Get zone_equipment_10_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_10_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 10 Heating or No-Load Sequence"]

    @zone_equipment_10_heating_or_noload_sequence.setter
    def zone_equipment_10_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 10 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 10 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_10_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_10_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_10_heating_or_noload_sequence`')
        self._data["Zone Equipment 10 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_11_object_type(self):
        """Get zone_equipment_11_object_type

        Returns:
            str: the value of `zone_equipment_11_object_type` or None if not set
        """
        return self._data["Zone Equipment 11 Object Type"]

    @zone_equipment_11_object_type.setter
    def zone_equipment_11_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 11 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 11 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_11_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_11_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_11_object_type`')
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
                                     'field `zone_equipment_11_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_11_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 11 Object Type"] = value

    @property
    def zone_equipment_11_name(self):
        """Get zone_equipment_11_name

        Returns:
            str: the value of `zone_equipment_11_name` or None if not set
        """
        return self._data["Zone Equipment 11 Name"]

    @zone_equipment_11_name.setter
    def zone_equipment_11_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 11 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 11 Name`
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
                                 'for field `zone_equipment_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_11_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_11_name`')
        self._data["Zone Equipment 11 Name"] = value

    @property
    def zone_equipment_11_cooling_sequence(self):
        """Get zone_equipment_11_cooling_sequence

        Returns:
            int: the value of `zone_equipment_11_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 11 Cooling Sequence"]

    @zone_equipment_11_cooling_sequence.setter
    def zone_equipment_11_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 11 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 11 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_11_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_11_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_11_cooling_sequence`')
        self._data["Zone Equipment 11 Cooling Sequence"] = value

    @property
    def zone_equipment_11_heating_or_noload_sequence(self):
        """Get zone_equipment_11_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_11_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 11 Heating or No-Load Sequence"]

    @zone_equipment_11_heating_or_noload_sequence.setter
    def zone_equipment_11_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 11 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 11 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_11_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_11_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_11_heating_or_noload_sequence`')
        self._data["Zone Equipment 11 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_12_object_type(self):
        """Get zone_equipment_12_object_type

        Returns:
            str: the value of `zone_equipment_12_object_type` or None if not set
        """
        return self._data["Zone Equipment 12 Object Type"]

    @zone_equipment_12_object_type.setter
    def zone_equipment_12_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 12 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 12 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_12_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_12_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_12_object_type`')
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
                                     'field `zone_equipment_12_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_12_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 12 Object Type"] = value

    @property
    def zone_equipment_12_name(self):
        """Get zone_equipment_12_name

        Returns:
            str: the value of `zone_equipment_12_name` or None if not set
        """
        return self._data["Zone Equipment 12 Name"]

    @zone_equipment_12_name.setter
    def zone_equipment_12_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 12 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 12 Name`
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
                                 'for field `zone_equipment_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_12_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_12_name`')
        self._data["Zone Equipment 12 Name"] = value

    @property
    def zone_equipment_12_cooling_sequence(self):
        """Get zone_equipment_12_cooling_sequence

        Returns:
            int: the value of `zone_equipment_12_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 12 Cooling Sequence"]

    @zone_equipment_12_cooling_sequence.setter
    def zone_equipment_12_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 12 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 12 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_12_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_12_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_12_cooling_sequence`')
        self._data["Zone Equipment 12 Cooling Sequence"] = value

    @property
    def zone_equipment_12_heating_or_noload_sequence(self):
        """Get zone_equipment_12_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_12_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 12 Heating or No-Load Sequence"]

    @zone_equipment_12_heating_or_noload_sequence.setter
    def zone_equipment_12_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 12 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 12 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_12_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_12_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_12_heating_or_noload_sequence`')
        self._data["Zone Equipment 12 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_13_object_type(self):
        """Get zone_equipment_13_object_type

        Returns:
            str: the value of `zone_equipment_13_object_type` or None if not set
        """
        return self._data["Zone Equipment 13 Object Type"]

    @zone_equipment_13_object_type.setter
    def zone_equipment_13_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 13 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 13 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_13_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_13_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_13_object_type`')
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
                                     'field `zone_equipment_13_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_13_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 13 Object Type"] = value

    @property
    def zone_equipment_13_name(self):
        """Get zone_equipment_13_name

        Returns:
            str: the value of `zone_equipment_13_name` or None if not set
        """
        return self._data["Zone Equipment 13 Name"]

    @zone_equipment_13_name.setter
    def zone_equipment_13_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 13 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 13 Name`
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
                                 'for field `zone_equipment_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_13_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_13_name`')
        self._data["Zone Equipment 13 Name"] = value

    @property
    def zone_equipment_13_cooling_sequence(self):
        """Get zone_equipment_13_cooling_sequence

        Returns:
            int: the value of `zone_equipment_13_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 13 Cooling Sequence"]

    @zone_equipment_13_cooling_sequence.setter
    def zone_equipment_13_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 13 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 13 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_13_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_13_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_13_cooling_sequence`')
        self._data["Zone Equipment 13 Cooling Sequence"] = value

    @property
    def zone_equipment_13_heating_or_noload_sequence(self):
        """Get zone_equipment_13_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_13_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 13 Heating or No-Load Sequence"]

    @zone_equipment_13_heating_or_noload_sequence.setter
    def zone_equipment_13_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 13 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 13 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_13_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_13_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_13_heating_or_noload_sequence`')
        self._data["Zone Equipment 13 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_14_object_type(self):
        """Get zone_equipment_14_object_type

        Returns:
            str: the value of `zone_equipment_14_object_type` or None if not set
        """
        return self._data["Zone Equipment 14 Object Type"]

    @zone_equipment_14_object_type.setter
    def zone_equipment_14_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 14 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 14 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_14_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_14_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_14_object_type`')
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
                                     'field `zone_equipment_14_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_14_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 14 Object Type"] = value

    @property
    def zone_equipment_14_name(self):
        """Get zone_equipment_14_name

        Returns:
            str: the value of `zone_equipment_14_name` or None if not set
        """
        return self._data["Zone Equipment 14 Name"]

    @zone_equipment_14_name.setter
    def zone_equipment_14_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 14 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 14 Name`
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
                                 'for field `zone_equipment_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_14_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_14_name`')
        self._data["Zone Equipment 14 Name"] = value

    @property
    def zone_equipment_14_cooling_sequence(self):
        """Get zone_equipment_14_cooling_sequence

        Returns:
            int: the value of `zone_equipment_14_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 14 Cooling Sequence"]

    @zone_equipment_14_cooling_sequence.setter
    def zone_equipment_14_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 14 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 14 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_14_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_14_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_14_cooling_sequence`')
        self._data["Zone Equipment 14 Cooling Sequence"] = value

    @property
    def zone_equipment_14_heating_or_noload_sequence(self):
        """Get zone_equipment_14_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_14_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 14 Heating or No-Load Sequence"]

    @zone_equipment_14_heating_or_noload_sequence.setter
    def zone_equipment_14_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 14 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 14 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_14_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_14_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_14_heating_or_noload_sequence`')
        self._data["Zone Equipment 14 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_15_object_type(self):
        """Get zone_equipment_15_object_type

        Returns:
            str: the value of `zone_equipment_15_object_type` or None if not set
        """
        return self._data["Zone Equipment 15 Object Type"]

    @zone_equipment_15_object_type.setter
    def zone_equipment_15_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 15 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 15 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_15_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_15_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_15_object_type`')
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
                                     'field `zone_equipment_15_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_15_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 15 Object Type"] = value

    @property
    def zone_equipment_15_name(self):
        """Get zone_equipment_15_name

        Returns:
            str: the value of `zone_equipment_15_name` or None if not set
        """
        return self._data["Zone Equipment 15 Name"]

    @zone_equipment_15_name.setter
    def zone_equipment_15_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 15 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 15 Name`
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
                                 'for field `zone_equipment_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_15_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_15_name`')
        self._data["Zone Equipment 15 Name"] = value

    @property
    def zone_equipment_15_cooling_sequence(self):
        """Get zone_equipment_15_cooling_sequence

        Returns:
            int: the value of `zone_equipment_15_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 15 Cooling Sequence"]

    @zone_equipment_15_cooling_sequence.setter
    def zone_equipment_15_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 15 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 15 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_15_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_15_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_15_cooling_sequence`')
        self._data["Zone Equipment 15 Cooling Sequence"] = value

    @property
    def zone_equipment_15_heating_or_noload_sequence(self):
        """Get zone_equipment_15_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_15_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 15 Heating or No-Load Sequence"]

    @zone_equipment_15_heating_or_noload_sequence.setter
    def zone_equipment_15_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 15 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 15 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_15_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_15_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_15_heating_or_noload_sequence`')
        self._data["Zone Equipment 15 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_16_object_type(self):
        """Get zone_equipment_16_object_type

        Returns:
            str: the value of `zone_equipment_16_object_type` or None if not set
        """
        return self._data["Zone Equipment 16 Object Type"]

    @zone_equipment_16_object_type.setter
    def zone_equipment_16_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 16 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 16 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_16_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_16_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_16_object_type`')
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
                                     'field `zone_equipment_16_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_16_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 16 Object Type"] = value

    @property
    def zone_equipment_16_name(self):
        """Get zone_equipment_16_name

        Returns:
            str: the value of `zone_equipment_16_name` or None if not set
        """
        return self._data["Zone Equipment 16 Name"]

    @zone_equipment_16_name.setter
    def zone_equipment_16_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 16 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 16 Name`
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
                                 'for field `zone_equipment_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_16_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_16_name`')
        self._data["Zone Equipment 16 Name"] = value

    @property
    def zone_equipment_16_cooling_sequence(self):
        """Get zone_equipment_16_cooling_sequence

        Returns:
            int: the value of `zone_equipment_16_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 16 Cooling Sequence"]

    @zone_equipment_16_cooling_sequence.setter
    def zone_equipment_16_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 16 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 16 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_16_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_16_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_16_cooling_sequence`')
        self._data["Zone Equipment 16 Cooling Sequence"] = value

    @property
    def zone_equipment_16_heating_or_noload_sequence(self):
        """Get zone_equipment_16_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_16_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 16 Heating or No-Load Sequence"]

    @zone_equipment_16_heating_or_noload_sequence.setter
    def zone_equipment_16_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 16 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 16 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_16_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_16_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_16_heating_or_noload_sequence`')
        self._data["Zone Equipment 16 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_17_object_type(self):
        """Get zone_equipment_17_object_type

        Returns:
            str: the value of `zone_equipment_17_object_type` or None if not set
        """
        return self._data["Zone Equipment 17 Object Type"]

    @zone_equipment_17_object_type.setter
    def zone_equipment_17_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 17 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 17 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_17_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_17_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_17_object_type`')
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
                                     'field `zone_equipment_17_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_17_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 17 Object Type"] = value

    @property
    def zone_equipment_17_name(self):
        """Get zone_equipment_17_name

        Returns:
            str: the value of `zone_equipment_17_name` or None if not set
        """
        return self._data["Zone Equipment 17 Name"]

    @zone_equipment_17_name.setter
    def zone_equipment_17_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 17 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 17 Name`
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
                                 'for field `zone_equipment_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_17_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_17_name`')
        self._data["Zone Equipment 17 Name"] = value

    @property
    def zone_equipment_17_cooling_sequence(self):
        """Get zone_equipment_17_cooling_sequence

        Returns:
            int: the value of `zone_equipment_17_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 17 Cooling Sequence"]

    @zone_equipment_17_cooling_sequence.setter
    def zone_equipment_17_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 17 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 17 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_17_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_17_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_17_cooling_sequence`')
        self._data["Zone Equipment 17 Cooling Sequence"] = value

    @property
    def zone_equipment_17_heating_or_noload_sequence(self):
        """Get zone_equipment_17_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_17_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 17 Heating or No-Load Sequence"]

    @zone_equipment_17_heating_or_noload_sequence.setter
    def zone_equipment_17_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 17 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 17 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_17_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_17_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_17_heating_or_noload_sequence`')
        self._data["Zone Equipment 17 Heating or No-Load Sequence"] = value

    @property
    def zone_equipment_18_object_type(self):
        """Get zone_equipment_18_object_type

        Returns:
            str: the value of `zone_equipment_18_object_type` or None if not set
        """
        return self._data["Zone Equipment 18 Object Type"]

    @zone_equipment_18_object_type.setter
    def zone_equipment_18_object_type(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 18 Object Type`

        Args:
            value (str): value for IDD Field `Zone Equipment 18 Object Type`
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

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 'for field `zone_equipment_18_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_18_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_18_object_type`')
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
                                     'field `zone_equipment_18_object_type`'.format(value))
                else:
                    logging.warn('change value {} to accepted value {} for '
                                 'field `zone_equipment_18_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        self._data["Zone Equipment 18 Object Type"] = value

    @property
    def zone_equipment_18_name(self):
        """Get zone_equipment_18_name

        Returns:
            str: the value of `zone_equipment_18_name` or None if not set
        """
        return self._data["Zone Equipment 18 Name"]

    @zone_equipment_18_name.setter
    def zone_equipment_18_name(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 18 Name`

        Args:
            value (str): value for IDD Field `Zone Equipment 18 Name`
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
                                 'for field `zone_equipment_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_equipment_18_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_equipment_18_name`')
        self._data["Zone Equipment 18 Name"] = value

    @property
    def zone_equipment_18_cooling_sequence(self):
        """Get zone_equipment_18_cooling_sequence

        Returns:
            int: the value of `zone_equipment_18_cooling_sequence` or None if not set
        """
        return self._data["Zone Equipment 18 Cooling Sequence"]

    @zone_equipment_18_cooling_sequence.setter
    def zone_equipment_18_cooling_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 18 Cooling Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests cooling

        Args:
            value (int): value for IDD Field `Zone Equipment 18 Cooling Sequence`
                value >= 1
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
                                     'for field `zone_equipment_18_cooling_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_18_cooling_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_18_cooling_sequence`')
        self._data["Zone Equipment 18 Cooling Sequence"] = value

    @property
    def zone_equipment_18_heating_or_noload_sequence(self):
        """Get zone_equipment_18_heating_or_noload_sequence

        Returns:
            int: the value of `zone_equipment_18_heating_or_noload_sequence` or None if not set
        """
        return self._data["Zone Equipment 18 Heating or No-Load Sequence"]

    @zone_equipment_18_heating_or_noload_sequence.setter
    def zone_equipment_18_heating_or_noload_sequence(self, value=None):
        """  Corresponds to IDD Field `Zone Equipment 18 Heating or No-Load Sequence`
        Specifies the zone equipment simulation order
        when the zone thermostat requests heating or no load

        Args:
            value (int): value for IDD Field `Zone Equipment 18 Heating or No-Load Sequence`
                value >= 1
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
                                     'for field `zone_equipment_18_heating_or_noload_sequence`'.format(value, conv_value))
                        value = conv_value
                    except ValueError:
                        raise ValueError('value {} need to be of type int '
                                         'for field `zone_equipment_18_heating_or_noload_sequence`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `zone_equipment_18_heating_or_noload_sequence`')
        self._data["Zone Equipment 18 Heating or No-Load Sequence"] = value

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

class ZoneHvacEquipmentConnections(object):
    """ Corresponds to IDD object `ZoneHVAC:EquipmentConnections`
        Specifies the HVAC equipment connections for a zone. Node names are specified for the
        zone air node, air inlet nodes, air exhaust nodes, and the air return node. A zone
        equipment list is referenced which lists all HVAC equipment connected to the zone.
    """
    internal_name = "ZoneHVAC:EquipmentConnections"
    field_count = 6
    required_fields = ["Zone Name", "Zone Conditioning Equipment List Name", "Zone Air Node Name", "Zone Return Air Node Name"]

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
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')
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
                                 'for field `zone_conditioning_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_conditioning_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_conditioning_equipment_list_name`')
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
                                 'for field `zone_air_inlet_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_air_inlet_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_air_inlet_node_or_nodelist_name`')
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
                                 'for field `zone_air_exhaust_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_air_exhaust_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_air_exhaust_node_or_nodelist_name`')
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
                                 'for field `zone_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_air_node_name`')
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
                                 'for field `zone_return_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_return_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_return_air_node_name`')
        self._data["Zone Return Air Node Name"] = value

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