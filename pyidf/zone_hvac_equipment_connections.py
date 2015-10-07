""" Data objects in group "Zone HVAC Equipment Connections"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ZoneHvacEquipmentList(DataObject):

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
    _schema = {'extensible-fields': OrderedDict([(u'zone equipment 1 object type',
                                                  {'name': u'Zone Equipment 1 Object Type',
                                                   'pyname': u'zone_equipment_1_object_type',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'accepted-values': [u'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
                                                                       u'ZoneHVAC:AirDistributionUnit',
                                                                       u'AirTerminal:SingleDuct:Uncontrolled',
                                                                       u'ZoneHVAC:EnergyRecoveryVentilator',
                                                                       u'ZoneHVAC:EvaporativeCoolerUnit',
                                                                       u'ZoneHVAC:FourPipeFanCoil',
                                                                       u'ZoneHVAC:OutdoorAirUnit',
                                                                       u'ZoneHVAC:PackagedTerminalAirConditioner',
                                                                       u'ZoneHVAC:PackagedTerminalHeatPump',
                                                                       u'ZoneHVAC:UnitHeater',
                                                                       u'ZoneHVAC:UnitVentilator',
                                                                       u'ZoneHVAC:VentilatedSlab',
                                                                       u'ZoneHVAC:WaterToAirHeatPump',
                                                                       u'ZoneHVAC:WindowAirConditioner',
                                                                       u'ZoneHVAC:Baseboard:RadiantConvective:Electric',
                                                                       u'ZoneHVAC:Baseboard:RadiantConvective:Water',
                                                                       u'ZoneHVAC:Baseboard:RadiantConvective:Steam',
                                                                       u'ZoneHVAC:Baseboard:Convective:Electric',
                                                                       u'ZoneHVAC:Baseboard:Convective:Water',
                                                                       u'ZoneHVAC:HighTemperatureRadiant',
                                                                       u'ZoneHVAC:LowTemperatureRadiant:VariableFlow',
                                                                       u'ZoneHVAC:LowTemperatureRadiant:ConstantFlow',
                                                                       u'ZoneHVAC:LowTemperatureRadiant:Electric',
                                                                       u'ZoneHVAC:Dehumidifier:DX',
                                                                       u'ZoneHVAC:IdealLoadsAirSystem',
                                                                       u'ZoneHVAC:RefrigerationChillerSet',
                                                                       u'Fan:ZoneExhaust',
                                                                       u'WaterHeater:HeatPump:PumpedCondenser',
                                                                       u'WaterHeater:HeatPump:WrappedCondenser'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'}),
                                                 (u'zone equipment 1 name',
                                                  {'name': u'Zone Equipment 1 Name',
                                                   'pyname': u'zone_equipment_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': 'alpha'}),
                                                 (u'zone equipment 1 cooling sequence',
                                                  {'name': u'Zone Equipment 1 Cooling Sequence',
                                                   'pyname': u'zone_equipment_1_cooling_sequence',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'minimum': 1,
                                                   'autocalculatable': False,
                                                   'type': u'integer'}),
                                                 (u'zone equipment 1 heating or no-load sequence',
                                                  {'name': u'Zone Equipment 1 Heating or No-Load Sequence',
                                                   'pyname': u'zone_equipment_1_heating_or_noload_sequence',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'minimum': 1,
                                                   'autocalculatable': False,
                                                   'type': u'integer'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Zone HVAC Equipment Connections',
               'min-fields': 0,
               'name': u'ZoneHVAC:EquipmentList',
               'pyname': u'ZoneHvacEquipmentList',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        Args:
            value (str): value for IDD Field `Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `name` or None if not set

        """
        return self["Name"]

    @name.setter
    def name(self, value=None):
        """Corresponds to IDD field `Name`"""
        self["Name"] = value

    def add_extensible(self,
                       zone_equipment_1_object_type=None,
                       zone_equipment_1_name=None,
                       zone_equipment_1_cooling_sequence=None,
                       zone_equipment_1_heating_or_noload_sequence=None,
                       ):
        """Add values for extensible fields.

        Args:

            zone_equipment_1_object_type (str): value for IDD Field `Zone Equipment 1 Object Type`
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
        zone_equipment_1_object_type = self.check_value(
            "Zone Equipment 1 Object Type",
            zone_equipment_1_object_type)
        vals.append(zone_equipment_1_object_type)
        zone_equipment_1_name = self.check_value(
            "Zone Equipment 1 Name",
            zone_equipment_1_name)
        vals.append(zone_equipment_1_name)
        zone_equipment_1_cooling_sequence = self.check_value(
            "Zone Equipment 1 Cooling Sequence",
            zone_equipment_1_cooling_sequence)
        vals.append(zone_equipment_1_cooling_sequence)
        zone_equipment_1_heating_or_noload_sequence = self.check_value(
            "Zone Equipment 1 Heating or No-Load Sequence",
            zone_equipment_1_heating_or_noload_sequence)
        vals.append(zone_equipment_1_heating_or_noload_sequence)
        self._extdata.append(vals)

    @property
    def extensibles(self):
        """Get list of all extensibles."""
        return self._extdata

    @extensibles.setter
    def extensibles(self, extensibles):
        """Replaces extensible fields with `extensibles`

        Args:
            extensibles (list): nested list of extensible values

        """
        self._extdata = []
        for ext in extensibles:
            self.add_extensible(*ext)




class ZoneHvacEquipmentConnections(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:EquipmentConnections`
        Specifies the HVAC equipment connections for a zone. Node names are specified for the
        zone air node, air inlet nodes, air exhaust nodes, and the air return node. A zone
        equipment list is referenced which lists all HVAC equipment connected to the zone.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone conditioning equipment list name',
                                       {'name': u'Zone Conditioning Equipment List Name',
                                        'pyname': u'zone_conditioning_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone air inlet node or nodelist name',
                                       {'name': u'Zone Air Inlet Node or NodeList Name',
                                        'pyname': u'zone_air_inlet_node_or_nodelist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone air exhaust node or nodelist name',
                                       {'name': u'Zone Air Exhaust Node or NodeList Name',
                                        'pyname': u'zone_air_exhaust_node_or_nodelist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone air node name',
                                       {'name': u'Zone Air Node Name',
                                        'pyname': u'zone_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone return air node name',
                                       {'name': u'Zone Return Air Node Name',
                                        'pyname': u'zone_return_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone return air flow rate fraction schedule name',
                                       {'name': u'Zone Return Air Flow Rate Fraction Schedule Name',
                                        'pyname': u'zone_return_air_flow_rate_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone return air flow rate basis node or nodelist name',
                                       {'name': u'Zone Return Air Flow Rate Basis Node or NodeList Name',
                                        'pyname': u'zone_return_air_flow_rate_basis_node_or_nodelist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Zone HVAC Equipment Connections',
               'min-fields': 0,
               'name': u'ZoneHVAC:EquipmentConnections',
               'pyname': u'ZoneHvacEquipmentConnections',
               'required-object': False,
               'unique-object': False}

    @property
    def zone_name(self):
        """field `Zone Name`

        Args:
            value (str): value for IDD Field `Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name` or None if not set

        """
        return self["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """Corresponds to IDD field `Zone Name`"""
        self["Zone Name"] = value

    @property
    def zone_conditioning_equipment_list_name(self):
        """field `Zone Conditioning Equipment List Name`

        |  Enter the name of a ZoneHVAC:EquipmentList object.

        Args:
            value (str): value for IDD Field `Zone Conditioning Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_conditioning_equipment_list_name` or None if not set

        """
        return self["Zone Conditioning Equipment List Name"]

    @zone_conditioning_equipment_list_name.setter
    def zone_conditioning_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Zone Conditioning Equipment List Name`"""
        self["Zone Conditioning Equipment List Name"] = value

    @property
    def zone_air_inlet_node_or_nodelist_name(self):
        """field `Zone Air Inlet Node or NodeList Name`

        Args:
            value (str): value for IDD Field `Zone Air Inlet Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_air_inlet_node_or_nodelist_name` or None if not set

        """
        return self["Zone Air Inlet Node or NodeList Name"]

    @zone_air_inlet_node_or_nodelist_name.setter
    def zone_air_inlet_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Zone Air Inlet Node or NodeList Name`"""
        self["Zone Air Inlet Node or NodeList Name"] = value

    @property
    def zone_air_exhaust_node_or_nodelist_name(self):
        """field `Zone Air Exhaust Node or NodeList Name`

        Args:
            value (str): value for IDD Field `Zone Air Exhaust Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_air_exhaust_node_or_nodelist_name` or None if not set

        """
        return self["Zone Air Exhaust Node or NodeList Name"]

    @zone_air_exhaust_node_or_nodelist_name.setter
    def zone_air_exhaust_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Zone Air Exhaust Node or NodeList Name`"""
        self["Zone Air Exhaust Node or NodeList Name"] = value

    @property
    def zone_air_node_name(self):
        """field `Zone Air Node Name`

        Args:
            value (str): value for IDD Field `Zone Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_air_node_name` or None if not set

        """
        return self["Zone Air Node Name"]

    @zone_air_node_name.setter
    def zone_air_node_name(self, value=None):
        """Corresponds to IDD field `Zone Air Node Name`"""
        self["Zone Air Node Name"] = value

    @property
    def zone_return_air_node_name(self):
        """field `Zone Return Air Node Name`

        Args:
            value (str): value for IDD Field `Zone Return Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_return_air_node_name` or None if not set

        """
        return self["Zone Return Air Node Name"]

    @zone_return_air_node_name.setter
    def zone_return_air_node_name(self, value=None):
        """Corresponds to IDD field `Zone Return Air Node Name`"""
        self["Zone Return Air Node Name"] = value

    @property
    def zone_return_air_flow_rate_fraction_schedule_name(self):
        """field `Zone Return Air Flow Rate Fraction Schedule Name`

        |  This schedule is multiplied times the base return air flow rate.
        |  If this field is left blank, the schedule defaults to 1.0 at all times.

        Args:
            value (str): value for IDD Field `Zone Return Air Flow Rate Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_return_air_flow_rate_fraction_schedule_name` or None if not set

        """
        return self["Zone Return Air Flow Rate Fraction Schedule Name"]

    @zone_return_air_flow_rate_fraction_schedule_name.setter
    def zone_return_air_flow_rate_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Zone Return Air Flow Rate Fraction
        Schedule Name`"""
        self["Zone Return Air Flow Rate Fraction Schedule Name"] = value

    @property
    def zone_return_air_flow_rate_basis_node_or_nodelist_name(self):
        """field `Zone Return Air Flow Rate Basis Node or NodeList Name`

        |  The optional basis node(s) used to calculate the base return air flow
        |  rate for this zone. The return air flow rate is the sum of the flow rates
        |  at the basis node(s) multiplied by the Zone Return Air Flow Rate Fraction Schedule.
        |  If this  field is blank, then the base return air flow rate is the total supply
        |  inlet flow rate to the zone less the total exhaust node flow rate from the zone.

        Args:
            value (str): value for IDD Field `Zone Return Air Flow Rate Basis Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_return_air_flow_rate_basis_node_or_nodelist_name` or None if not set

        """
        return self["Zone Return Air Flow Rate Basis Node or NodeList Name"]

    @zone_return_air_flow_rate_basis_node_or_nodelist_name.setter
    def zone_return_air_flow_rate_basis_node_or_nodelist_name(
            self,
            value=None):
        """Corresponds to IDD field `Zone Return Air Flow Rate Basis Node or
        NodeList Name`"""
        self["Zone Return Air Flow Rate Basis Node or NodeList Name"] = value


