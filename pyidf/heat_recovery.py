""" Data objects in group "Heat Recovery"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class HeatExchangerAirToAirFlatPlate(DataObject):

    """ Corresponds to IDD object `HeatExchanger:AirToAir:FlatPlate`
        Flat plate air-to-air heat exchanger, typically used for exhaust or relief air heat
        recovery.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'flow arrangement type',
                                       {'name': u'Flow Arrangement Type',
                                        'pyname': u'flow_arrangement_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'CounterFlow',
                                                            u'ParallelFlow',
                                                            u'CrossFlowBothUnmixed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'economizer lockout',
                                       {'name': u'Economizer Lockout',
                                        'pyname': u'economizer_lockout',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ratio of supply to secondary ha values',
                                       {'name': u'Ratio of Supply to Secondary hA Values',
                                        'pyname': u'ratio_of_supply_to_secondary_ha_values',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'nominal supply air flow rate',
                                       {'name': u'Nominal Supply Air Flow Rate',
                                        'pyname': u'nominal_supply_air_flow_rate',
                                        'default': 'Autosize',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'nominal supply air inlet temperature',
                                       {'name': u'Nominal Supply Air Inlet Temperature',
                                        'pyname': u'nominal_supply_air_inlet_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'nominal supply air outlet temperature',
                                       {'name': u'Nominal Supply Air Outlet Temperature',
                                        'pyname': u'nominal_supply_air_outlet_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'nominal secondary air flow rate',
                                       {'name': u'Nominal Secondary Air Flow Rate',
                                        'pyname': u'nominal_secondary_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'nominal secondary air inlet temperature',
                                       {'name': u'Nominal Secondary Air Inlet Temperature',
                                        'pyname': u'nominal_secondary_air_inlet_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'nominal electric power',
                                       {'name': u'Nominal Electric Power',
                                        'pyname': u'nominal_electric_power',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'supply air inlet node name',
                                       {'name': u'Supply Air Inlet Node Name',
                                        'pyname': u'supply_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air outlet node name',
                                       {'name': u'Supply Air Outlet Node Name',
                                        'pyname': u'supply_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'secondary air outlet node name',
                                       {'name': u'Secondary Air Outlet Node Name',
                                        'pyname': u'secondary_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Heat Recovery',
               'min-fields': 15,
               'name': u'HeatExchanger:AirToAir:FlatPlate',
               'pyname': u'HeatExchangerAirToAirFlatPlate',
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

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def flow_arrangement_type(self):
        """field `Flow Arrangement Type`

        Args:
            value (str): value for IDD Field `Flow Arrangement Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `flow_arrangement_type` or None if not set

        """
        return self["Flow Arrangement Type"]

    @flow_arrangement_type.setter
    def flow_arrangement_type(self, value=None):
        """Corresponds to IDD field `Flow Arrangement Type`"""
        self["Flow Arrangement Type"] = value

    @property
    def economizer_lockout(self):
        """field `Economizer Lockout`

        |  Yes means that the heat exchanger will be locked out (off)
        |  when the economizer is operating or high humidity control is active
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Economizer Lockout`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `economizer_lockout` or None if not set

        """
        return self["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """Corresponds to IDD field `Economizer Lockout`"""
        self["Economizer Lockout"] = value

    @property
    def ratio_of_supply_to_secondary_ha_values(self):
        """field `Ratio of Supply to Secondary hA Values`

        |  Ratio of h*A for supply side to h*A for exhaust side

        Args:
            value (float): value for IDD Field `Ratio of Supply to Secondary hA Values`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ratio_of_supply_to_secondary_ha_values` or None if not set

        """
        return self["Ratio of Supply to Secondary hA Values"]

    @ratio_of_supply_to_secondary_ha_values.setter
    def ratio_of_supply_to_secondary_ha_values(self, value=None):
        """Corresponds to IDD field `Ratio of Supply to Secondary hA Values`"""
        self["Ratio of Supply to Secondary hA Values"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """field `Nominal Supply Air Flow Rate`

        |  Units: m3/s
        |  Default value: "Autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `nominal_supply_air_flow_rate` or None if not set

        """
        return self["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value="Autosize"):
        """Corresponds to IDD field `Nominal Supply Air Flow Rate`"""
        self["Nominal Supply Air Flow Rate"] = value

    @property
    def nominal_supply_air_inlet_temperature(self):
        """field `Nominal Supply Air Inlet Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Nominal Supply Air Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_supply_air_inlet_temperature` or None if not set

        """
        return self["Nominal Supply Air Inlet Temperature"]

    @nominal_supply_air_inlet_temperature.setter
    def nominal_supply_air_inlet_temperature(self, value=None):
        """Corresponds to IDD field `Nominal Supply Air Inlet Temperature`"""
        self["Nominal Supply Air Inlet Temperature"] = value

    @property
    def nominal_supply_air_outlet_temperature(self):
        """field `Nominal Supply Air Outlet Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Nominal Supply Air Outlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_supply_air_outlet_temperature` or None if not set

        """
        return self["Nominal Supply Air Outlet Temperature"]

    @nominal_supply_air_outlet_temperature.setter
    def nominal_supply_air_outlet_temperature(self, value=None):
        """Corresponds to IDD field `Nominal Supply Air Outlet Temperature`"""
        self["Nominal Supply Air Outlet Temperature"] = value

    @property
    def nominal_secondary_air_flow_rate(self):
        """field `Nominal Secondary Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Secondary Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `nominal_secondary_air_flow_rate` or None if not set

        """
        return self["Nominal Secondary Air Flow Rate"]

    @nominal_secondary_air_flow_rate.setter
    def nominal_secondary_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Nominal Secondary Air Flow Rate`"""
        self["Nominal Secondary Air Flow Rate"] = value

    @property
    def nominal_secondary_air_inlet_temperature(self):
        """field `Nominal Secondary Air Inlet Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Nominal Secondary Air Inlet Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_secondary_air_inlet_temperature` or None if not set

        """
        return self["Nominal Secondary Air Inlet Temperature"]

    @nominal_secondary_air_inlet_temperature.setter
    def nominal_secondary_air_inlet_temperature(self, value=None):
        """Corresponds to IDD field `Nominal Secondary Air Inlet
        Temperature`"""
        self["Nominal Secondary Air Inlet Temperature"] = value

    @property
    def nominal_electric_power(self):
        """field `Nominal Electric Power`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Nominal Electric Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_electric_power` or None if not set

        """
        return self["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """Corresponds to IDD field `Nominal Electric Power`"""
        self["Nominal Electric Power"] = value

    @property
    def supply_air_inlet_node_name(self):
        """field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set

        """
        return self["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply Air Inlet Node Name`"""
        self["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set

        """
        return self["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply Air Outlet Node Name`"""
        self["Supply Air Outlet Node Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """field `Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `secondary_air_inlet_node_name` or None if not set

        """
        return self["Secondary Air Inlet Node Name"]

    @secondary_air_inlet_node_name.setter
    def secondary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Secondary Air Inlet Node Name`"""
        self["Secondary Air Inlet Node Name"] = value

    @property
    def secondary_air_outlet_node_name(self):
        """field `Secondary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Secondary Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `secondary_air_outlet_node_name` or None if not set

        """
        return self["Secondary Air Outlet Node Name"]

    @secondary_air_outlet_node_name.setter
    def secondary_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Secondary Air Outlet Node Name`"""
        self["Secondary Air Outlet Node Name"] = value




class HeatExchangerAirToAirSensibleAndLatent(DataObject):

    """ Corresponds to IDD object `HeatExchanger:AirToAir:SensibleAndLatent`
        This object models an air-to-air heat exchanger using effectiveness relationships.
        The heat exchanger can transfer sensible energy, latent energy, or both between the
        supply (primary) and exhaust (secondary) air streams.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'nominal supply air flow rate',
                                       {'name': u'Nominal Supply Air Flow Rate',
                                        'pyname': u'nominal_supply_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'sensible effectiveness at 100% heating air flow',
                                       {'name': u'Sensible Effectiveness at 100% Heating Air Flow',
                                        'pyname': u'sensible_effectiveness_at_100_heating_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'latent effectiveness at 100% heating air flow',
                                       {'name': u'Latent Effectiveness at 100% Heating Air Flow',
                                        'pyname': u'latent_effectiveness_at_100_heating_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'sensible effectiveness at 75% heating air flow',
                                       {'name': u'Sensible Effectiveness at 75% Heating Air Flow',
                                        'pyname': u'sensible_effectiveness_at_75_heating_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'latent effectiveness at 75% heating air flow',
                                       {'name': u'Latent Effectiveness at 75% Heating Air Flow',
                                        'pyname': u'latent_effectiveness_at_75_heating_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'sensible effectiveness at 100% cooling air flow',
                                       {'name': u'Sensible Effectiveness at 100% Cooling Air Flow',
                                        'pyname': u'sensible_effectiveness_at_100_cooling_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'latent effectiveness at 100% cooling air flow',
                                       {'name': u'Latent Effectiveness at 100% Cooling Air Flow',
                                        'pyname': u'latent_effectiveness_at_100_cooling_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'sensible effectiveness at 75% cooling air flow',
                                       {'name': u'Sensible Effectiveness at 75% Cooling Air Flow',
                                        'pyname': u'sensible_effectiveness_at_75_cooling_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'latent effectiveness at 75% cooling air flow',
                                       {'name': u'Latent Effectiveness at 75% Cooling Air Flow',
                                        'pyname': u'latent_effectiveness_at_75_cooling_air_flow',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'supply air inlet node name',
                                       {'name': u'Supply Air Inlet Node Name',
                                        'pyname': u'supply_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air outlet node name',
                                       {'name': u'Supply Air Outlet Node Name',
                                        'pyname': u'supply_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'exhaust air inlet node name',
                                       {'name': u'Exhaust Air Inlet Node Name',
                                        'pyname': u'exhaust_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'exhaust air outlet node name',
                                       {'name': u'Exhaust Air Outlet Node Name',
                                        'pyname': u'exhaust_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'nominal electric power',
                                       {'name': u'Nominal Electric Power',
                                        'pyname': u'nominal_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'supply air outlet temperature control',
                                       {'name': u'Supply Air Outlet Temperature Control',
                                        'pyname': u'supply_air_outlet_temperature_control',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'No',
                                                            u'Yes'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heat exchanger type',
                                       {'name': u'Heat Exchanger Type',
                                        'pyname': u'heat_exchanger_type',
                                        'default': u'Plate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Plate',
                                                            u'Rotary'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'frost control type',
                                       {'name': u'Frost Control Type',
                                        'pyname': u'frost_control_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'None',
                                                            u'ExhaustAirRecirculation',
                                                            u'ExhaustOnly',
                                                            u'MinimumExhaustTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'threshold temperature',
                                       {'name': u'Threshold Temperature',
                                        'pyname': u'threshold_temperature',
                                        'default': 1.7,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'initial defrost time fraction',
                                       {'name': u'Initial Defrost Time Fraction',
                                        'pyname': u'initial_defrost_time_fraction',
                                        'default': 0.083,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'rate of defrost time fraction increase',
                                       {'name': u'Rate of Defrost Time Fraction Increase',
                                        'pyname': u'rate_of_defrost_time_fraction_increase',
                                        'default': 0.012,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/K'}),
                                      (u'economizer lockout',
                                       {'name': u'Economizer Lockout',
                                        'pyname': u'economizer_lockout',
                                        'default': u'Yes',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Heat Recovery',
               'min-fields': 19,
               'name': u'HeatExchanger:AirToAir:SensibleAndLatent',
               'pyname': u'HeatExchangerAirToAirSensibleAndLatent',
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

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def nominal_supply_air_flow_rate(self):
        """field `Nominal Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `nominal_supply_air_flow_rate` or None if not set

        """
        return self["Nominal Supply Air Flow Rate"]

    @nominal_supply_air_flow_rate.setter
    def nominal_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Nominal Supply Air Flow Rate`"""
        self["Nominal Supply Air Flow Rate"] = value

    @property
    def sensible_effectiveness_at_100_heating_air_flow(self):
        """field `Sensible Effectiveness at 100% Heating Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 100% Heating Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sensible_effectiveness_at_100_heating_air_flow` or None if not set

        """
        return self["Sensible Effectiveness at 100% Heating Air Flow"]

    @sensible_effectiveness_at_100_heating_air_flow.setter
    def sensible_effectiveness_at_100_heating_air_flow(self, value=None):
        """Corresponds to IDD field `Sensible Effectiveness at 100% Heating Air
        Flow`"""
        self["Sensible Effectiveness at 100% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_100_heating_air_flow(self):
        """field `Latent Effectiveness at 100% Heating Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 100% Heating Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `latent_effectiveness_at_100_heating_air_flow` or None if not set

        """
        return self["Latent Effectiveness at 100% Heating Air Flow"]

    @latent_effectiveness_at_100_heating_air_flow.setter
    def latent_effectiveness_at_100_heating_air_flow(self, value=None):
        """Corresponds to IDD field `Latent Effectiveness at 100% Heating Air
        Flow`"""
        self["Latent Effectiveness at 100% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_heating_air_flow(self):
        """field `Sensible Effectiveness at 75% Heating Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 75% Heating Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sensible_effectiveness_at_75_heating_air_flow` or None if not set

        """
        return self["Sensible Effectiveness at 75% Heating Air Flow"]

    @sensible_effectiveness_at_75_heating_air_flow.setter
    def sensible_effectiveness_at_75_heating_air_flow(self, value=None):
        """Corresponds to IDD field `Sensible Effectiveness at 75% Heating Air
        Flow`"""
        self["Sensible Effectiveness at 75% Heating Air Flow"] = value

    @property
    def latent_effectiveness_at_75_heating_air_flow(self):
        """field `Latent Effectiveness at 75% Heating Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 75% Heating Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `latent_effectiveness_at_75_heating_air_flow` or None if not set

        """
        return self["Latent Effectiveness at 75% Heating Air Flow"]

    @latent_effectiveness_at_75_heating_air_flow.setter
    def latent_effectiveness_at_75_heating_air_flow(self, value=None):
        """Corresponds to IDD field `Latent Effectiveness at 75% Heating Air
        Flow`"""
        self["Latent Effectiveness at 75% Heating Air Flow"] = value

    @property
    def sensible_effectiveness_at_100_cooling_air_flow(self):
        """field `Sensible Effectiveness at 100% Cooling Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 100% Cooling Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sensible_effectiveness_at_100_cooling_air_flow` or None if not set

        """
        return self["Sensible Effectiveness at 100% Cooling Air Flow"]

    @sensible_effectiveness_at_100_cooling_air_flow.setter
    def sensible_effectiveness_at_100_cooling_air_flow(self, value=None):
        """Corresponds to IDD field `Sensible Effectiveness at 100% Cooling Air
        Flow`"""
        self["Sensible Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_100_cooling_air_flow(self):
        """field `Latent Effectiveness at 100% Cooling Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 100% Cooling Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `latent_effectiveness_at_100_cooling_air_flow` or None if not set

        """
        return self["Latent Effectiveness at 100% Cooling Air Flow"]

    @latent_effectiveness_at_100_cooling_air_flow.setter
    def latent_effectiveness_at_100_cooling_air_flow(self, value=None):
        """Corresponds to IDD field `Latent Effectiveness at 100% Cooling Air
        Flow`"""
        self["Latent Effectiveness at 100% Cooling Air Flow"] = value

    @property
    def sensible_effectiveness_at_75_cooling_air_flow(self):
        """field `Sensible Effectiveness at 75% Cooling Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Sensible Effectiveness at 75% Cooling Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `sensible_effectiveness_at_75_cooling_air_flow` or None if not set

        """
        return self["Sensible Effectiveness at 75% Cooling Air Flow"]

    @sensible_effectiveness_at_75_cooling_air_flow.setter
    def sensible_effectiveness_at_75_cooling_air_flow(self, value=None):
        """Corresponds to IDD field `Sensible Effectiveness at 75% Cooling Air
        Flow`"""
        self["Sensible Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def latent_effectiveness_at_75_cooling_air_flow(self):
        """field `Latent Effectiveness at 75% Cooling Air Flow`

        |  Units: dimensionless
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Latent Effectiveness at 75% Cooling Air Flow`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `latent_effectiveness_at_75_cooling_air_flow` or None if not set

        """
        return self["Latent Effectiveness at 75% Cooling Air Flow"]

    @latent_effectiveness_at_75_cooling_air_flow.setter
    def latent_effectiveness_at_75_cooling_air_flow(self, value=None):
        """Corresponds to IDD field `Latent Effectiveness at 75% Cooling Air
        Flow`"""
        self["Latent Effectiveness at 75% Cooling Air Flow"] = value

    @property
    def supply_air_inlet_node_name(self):
        """field `Supply Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_inlet_node_name` or None if not set

        """
        return self["Supply Air Inlet Node Name"]

    @supply_air_inlet_node_name.setter
    def supply_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply Air Inlet Node Name`"""
        self["Supply Air Inlet Node Name"] = value

    @property
    def supply_air_outlet_node_name(self):
        """field `Supply Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_outlet_node_name` or None if not set

        """
        return self["Supply Air Outlet Node Name"]

    @supply_air_outlet_node_name.setter
    def supply_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply Air Outlet Node Name`"""
        self["Supply Air Outlet Node Name"] = value

    @property
    def exhaust_air_inlet_node_name(self):
        """field `Exhaust Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_inlet_node_name` or None if not set

        """
        return self["Exhaust Air Inlet Node Name"]

    @exhaust_air_inlet_node_name.setter
    def exhaust_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Inlet Node Name`"""
        self["Exhaust Air Inlet Node Name"] = value

    @property
    def exhaust_air_outlet_node_name(self):
        """field `Exhaust Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Exhaust Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_outlet_node_name` or None if not set

        """
        return self["Exhaust Air Outlet Node Name"]

    @exhaust_air_outlet_node_name.setter
    def exhaust_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Outlet Node Name`"""
        self["Exhaust Air Outlet Node Name"] = value

    @property
    def nominal_electric_power(self):
        """field `Nominal Electric Power`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Nominal Electric Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_electric_power` or None if not set

        """
        return self["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """Corresponds to IDD field `Nominal Electric Power`"""
        self["Nominal Electric Power"] = value

    @property
    def supply_air_outlet_temperature_control(self):
        """field `Supply Air Outlet Temperature Control`

        |  Default value: No

        Args:
            value (str): value for IDD Field `Supply Air Outlet Temperature Control`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_outlet_temperature_control` or None if not set

        """
        return self["Supply Air Outlet Temperature Control"]

    @supply_air_outlet_temperature_control.setter
    def supply_air_outlet_temperature_control(self, value="No"):
        """Corresponds to IDD field `Supply Air Outlet Temperature Control`"""
        self["Supply Air Outlet Temperature Control"] = value

    @property
    def heat_exchanger_type(self):
        """field `Heat Exchanger Type`

        |  Default value: Plate

        Args:
            value (str): value for IDD Field `Heat Exchanger Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_exchanger_type` or None if not set

        """
        return self["Heat Exchanger Type"]

    @heat_exchanger_type.setter
    def heat_exchanger_type(self, value="Plate"):
        """Corresponds to IDD field `Heat Exchanger Type`"""
        self["Heat Exchanger Type"] = value

    @property
    def frost_control_type(self):
        """field `Frost Control Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Frost Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `frost_control_type` or None if not set

        """
        return self["Frost Control Type"]

    @frost_control_type.setter
    def frost_control_type(self, value="None"):
        """Corresponds to IDD field `Frost Control Type`"""
        self["Frost Control Type"] = value

    @property
    def threshold_temperature(self):
        """field `Threshold Temperature`

        |  Supply (outdoor) air inlet temp threshold for exhaust air recirculation and
        |  exhaust only frost control types. Exhaust air outlet threshold Temperature for
        |  minimum exhaust temperature frost control type.
        |  Units: C
        |  Default value: 1.7

        Args:
            value (float): value for IDD Field `Threshold Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `threshold_temperature` or None if not set

        """
        return self["Threshold Temperature"]

    @threshold_temperature.setter
    def threshold_temperature(self, value=1.7):
        """Corresponds to IDD field `Threshold Temperature`"""
        self["Threshold Temperature"] = value

    @property
    def initial_defrost_time_fraction(self):
        """field `Initial Defrost Time Fraction`

        |  Fraction of the time when frost control will be invoked at the threshold temperature.
        |  This field only used for exhaust air recirc and exhaust-only frost control types.
        |  Units: dimensionless
        |  Default value: 0.083
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Initial Defrost Time Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_defrost_time_fraction` or None if not set

        """
        return self["Initial Defrost Time Fraction"]

    @initial_defrost_time_fraction.setter
    def initial_defrost_time_fraction(self, value=0.083):
        """Corresponds to IDD field `Initial Defrost Time Fraction`"""
        self["Initial Defrost Time Fraction"] = value

    @property
    def rate_of_defrost_time_fraction_increase(self):
        """field `Rate of Defrost Time Fraction Increase`

        |  Rate of increase in defrost time fraction as actual temp falls below threshold temperature.
        |  This field only used for exhaust air recirc and exhaust-only frost control types.
        |  Units: 1/K
        |  Default value: 0.012

        Args:
            value (float): value for IDD Field `Rate of Defrost Time Fraction Increase`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rate_of_defrost_time_fraction_increase` or None if not set

        """
        return self["Rate of Defrost Time Fraction Increase"]

    @rate_of_defrost_time_fraction_increase.setter
    def rate_of_defrost_time_fraction_increase(self, value=0.012):
        """Corresponds to IDD field `Rate of Defrost Time Fraction Increase`"""
        self["Rate of Defrost Time Fraction Increase"] = value

    @property
    def economizer_lockout(self):
        """field `Economizer Lockout`

        |  Yes means that the heat exchanger will be locked out (off)
        |  when the economizer is operating or high humidity control is active
        |  Default value: Yes

        Args:
            value (str): value for IDD Field `Economizer Lockout`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `economizer_lockout` or None if not set

        """
        return self["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="Yes"):
        """Corresponds to IDD field `Economizer Lockout`"""
        self["Economizer Lockout"] = value




class HeatExchangerDesiccantBalancedFlow(DataObject):

    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow`
        This object models a balanced desiccant heat exchanger.
        The heat exchanger transfers both sensible and latent energy between the
        process and regeneration air streams. The air flow rate and face velocity
        are assumed to be the same on both the process and regeneration sides of the
        heat exchanger.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'regeneration air inlet node name',
                                       {'name': u'Regeneration Air Inlet Node Name',
                                        'pyname': u'regeneration_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'regeneration air outlet node name',
                                       {'name': u'Regeneration Air Outlet Node Name',
                                        'pyname': u'regeneration_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'process air inlet node name',
                                       {'name': u'Process Air Inlet Node Name',
                                        'pyname': u'process_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'process air outlet node name',
                                       {'name': u'Process Air Outlet Node Name',
                                        'pyname': u'process_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heat exchanger performance object type',
                                       {'name': u'Heat Exchanger Performance Object Type',
                                        'pyname': u'heat_exchanger_performance_object_type',
                                        'default': u'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heat exchanger performance name',
                                       {'name': u'Heat Exchanger Performance Name',
                                        'pyname': u'heat_exchanger_performance_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'economizer lockout',
                                       {'name': u'Economizer Lockout',
                                        'pyname': u'economizer_lockout',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Heat Recovery',
               'min-fields': 8,
               'name': u'HeatExchanger:Desiccant:BalancedFlow',
               'pyname': u'HeatExchangerDesiccantBalancedFlow',
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

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_schedule_name` or None if not set

        """
        return self["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Availability Schedule Name`"""
        self["Availability Schedule Name"] = value

    @property
    def regeneration_air_inlet_node_name(self):
        """field `Regeneration Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_inlet_node_name` or None if not set

        """
        return self["Regeneration Air Inlet Node Name"]

    @regeneration_air_inlet_node_name.setter
    def regeneration_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Regeneration Air Inlet Node Name`"""
        self["Regeneration Air Inlet Node Name"] = value

    @property
    def regeneration_air_outlet_node_name(self):
        """field `Regeneration Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Regeneration Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `regeneration_air_outlet_node_name` or None if not set

        """
        return self["Regeneration Air Outlet Node Name"]

    @regeneration_air_outlet_node_name.setter
    def regeneration_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Regeneration Air Outlet Node Name`"""
        self["Regeneration Air Outlet Node Name"] = value

    @property
    def process_air_inlet_node_name(self):
        """field `Process Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Process Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `process_air_inlet_node_name` or None if not set

        """
        return self["Process Air Inlet Node Name"]

    @process_air_inlet_node_name.setter
    def process_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Process Air Inlet Node Name`"""
        self["Process Air Inlet Node Name"] = value

    @property
    def process_air_outlet_node_name(self):
        """field `Process Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Process Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `process_air_outlet_node_name` or None if not set

        """
        return self["Process Air Outlet Node Name"]

    @process_air_outlet_node_name.setter
    def process_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Process Air Outlet Node Name`"""
        self["Process Air Outlet Node Name"] = value

    @property
    def heat_exchanger_performance_object_type(self):
        """field `Heat Exchanger Performance Object Type`

        |  Default value: HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1

        Args:
            value (str): value for IDD Field `Heat Exchanger Performance Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_exchanger_performance_object_type` or None if not set

        """
        return self["Heat Exchanger Performance Object Type"]

    @heat_exchanger_performance_object_type.setter
    def heat_exchanger_performance_object_type(
            self,
            value="HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1"):
        """Corresponds to IDD field `Heat Exchanger Performance Object Type`"""
        self["Heat Exchanger Performance Object Type"] = value

    @property
    def heat_exchanger_performance_name(self):
        """field `Heat Exchanger Performance Name`

        Args:
            value (str): value for IDD Field `Heat Exchanger Performance Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_exchanger_performance_name` or None if not set

        """
        return self["Heat Exchanger Performance Name"]

    @heat_exchanger_performance_name.setter
    def heat_exchanger_performance_name(self, value=None):
        """Corresponds to IDD field `Heat Exchanger Performance Name`"""
        self["Heat Exchanger Performance Name"] = value

    @property
    def economizer_lockout(self):
        """field `Economizer Lockout`

        |  Yes means that the heat exchanger will be locked out (off)
        |  when the economizer is operating or high humidity control is active
        |  Default value: No

        Args:
            value (str): value for IDD Field `Economizer Lockout`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `economizer_lockout` or None if not set

        """
        return self["Economizer Lockout"]

    @economizer_lockout.setter
    def economizer_lockout(self, value="No"):
        """Corresponds to IDD field `Economizer Lockout`"""
        self["Economizer Lockout"] = value




class HeatExchangerDesiccantBalancedFlowPerformanceDataType1(DataObject):

    """ Corresponds to IDD object `HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1`
        RTO = B1 + B2*RWI + B3*RTI + B4*(RWI/RTI) + B5*PWI + B6*PTI + B7*(PWI/PTI)
        + B8*RFV
        RWO = C1 + C2*RWI + C3*RTI + C4*(RWI/RTI) + C5*PWI + C6*PTI + C7*(PWI/PTI)
        + C8*RFV
        where,
        RTO = Dry-bulb temperature of the regeneration outlet air (C)
        RWO = Humidity ratio of the regeneration outlet air (kgWater/kgDryAir)
        RWI = Humidity ratio of the regeneration inlet air (kgWater/kgDryAir)
        RTI = Dry-bulb temperature of the regeneration inlet air (C)
        PWI = Humidity ratio of the process inlet air (kgWater/kgDryAir)
        PTI = Dry-bulb temperature of the process inlet air (C)
        RFV = Regeneration Face Velocity (m/s)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'nominal air flow rate',
                                       {'name': u'Nominal Air Flow Rate',
                                        'pyname': u'nominal_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'nominal air face velocity',
                                       {'name': u'Nominal Air Face Velocity',
                                        'pyname': u'nominal_air_face_velocity',
                                        'minimum>': 0.0,
                                        'maximum': 6.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'nominal electric power',
                                       {'name': u'Nominal Electric Power',
                                        'pyname': u'nominal_electric_power',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'temperature equation coefficient 1',
                                       {'name': u'Temperature Equation Coefficient 1',
                                        'pyname': u'temperature_equation_coefficient_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 2',
                                       {'name': u'Temperature Equation Coefficient 2',
                                        'pyname': u'temperature_equation_coefficient_2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 3',
                                       {'name': u'Temperature Equation Coefficient 3',
                                        'pyname': u'temperature_equation_coefficient_3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 4',
                                       {'name': u'Temperature Equation Coefficient 4',
                                        'pyname': u'temperature_equation_coefficient_4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 5',
                                       {'name': u'Temperature Equation Coefficient 5',
                                        'pyname': u'temperature_equation_coefficient_5',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 6',
                                       {'name': u'Temperature Equation Coefficient 6',
                                        'pyname': u'temperature_equation_coefficient_6',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 7',
                                       {'name': u'Temperature Equation Coefficient 7',
                                        'pyname': u'temperature_equation_coefficient_7',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'temperature equation coefficient 8',
                                       {'name': u'Temperature Equation Coefficient 8',
                                        'pyname': u'temperature_equation_coefficient_8',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum regeneration inlet air humidity ratio for temperature equation',
                                       {'name': u'Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation',
                                        'pyname': u'minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum regeneration inlet air humidity ratio for temperature equation',
                                       {'name': u'Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation',
                                        'pyname': u'maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'minimum regeneration inlet air temperature for temperature equation',
                                       {'name': u'Minimum Regeneration Inlet Air Temperature for Temperature Equation',
                                        'pyname': u'minimum_regeneration_inlet_air_temperature_for_temperature_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum regeneration inlet air temperature for temperature equation',
                                       {'name': u'Maximum Regeneration Inlet Air Temperature for Temperature Equation',
                                        'pyname': u'maximum_regeneration_inlet_air_temperature_for_temperature_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum process inlet air humidity ratio for temperature equation',
                                       {'name': u'Minimum Process Inlet Air Humidity Ratio for Temperature Equation',
                                        'pyname': u'minimum_process_inlet_air_humidity_ratio_for_temperature_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum process inlet air humidity ratio for temperature equation',
                                       {'name': u'Maximum Process Inlet Air Humidity Ratio for Temperature Equation',
                                        'pyname': u'maximum_process_inlet_air_humidity_ratio_for_temperature_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'minimum process inlet air temperature for temperature equation',
                                       {'name': u'Minimum Process Inlet Air Temperature for Temperature Equation',
                                        'pyname': u'minimum_process_inlet_air_temperature_for_temperature_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum process inlet air temperature for temperature equation',
                                       {'name': u'Maximum Process Inlet Air Temperature for Temperature Equation',
                                        'pyname': u'maximum_process_inlet_air_temperature_for_temperature_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum regeneration air velocity for temperature equation',
                                       {'name': u'Minimum Regeneration Air Velocity for Temperature Equation',
                                        'pyname': u'minimum_regeneration_air_velocity_for_temperature_equation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'maximum regeneration air velocity for temperature equation',
                                       {'name': u'Maximum Regeneration Air Velocity for Temperature Equation',
                                        'pyname': u'maximum_regeneration_air_velocity_for_temperature_equation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'minimum regeneration outlet air temperature for temperature equation',
                                       {'name': u'Minimum Regeneration Outlet Air Temperature for Temperature Equation',
                                        'pyname': u'minimum_regeneration_outlet_air_temperature_for_temperature_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum regeneration outlet air temperature for temperature equation',
                                       {'name': u'Maximum Regeneration Outlet Air Temperature for Temperature Equation',
                                        'pyname': u'maximum_regeneration_outlet_air_temperature_for_temperature_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum regeneration inlet air relative humidity for temperature equation',
                                       {'name': u'Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation',
                                        'pyname': u'minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'maximum regeneration inlet air relative humidity for temperature equation',
                                       {'name': u'Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation',
                                        'pyname': u'maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'minimum process inlet air relative humidity for temperature equation',
                                       {'name': u'Minimum Process Inlet Air Relative Humidity for Temperature Equation',
                                        'pyname': u'minimum_process_inlet_air_relative_humidity_for_temperature_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'maximum process inlet air relative humidity for temperature equation',
                                       {'name': u'Maximum Process Inlet Air Relative Humidity for Temperature Equation',
                                        'pyname': u'maximum_process_inlet_air_relative_humidity_for_temperature_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'humidity ratio equation coefficient 1',
                                       {'name': u'Humidity Ratio Equation Coefficient 1',
                                        'pyname': u'humidity_ratio_equation_coefficient_1',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 2',
                                       {'name': u'Humidity Ratio Equation Coefficient 2',
                                        'pyname': u'humidity_ratio_equation_coefficient_2',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 3',
                                       {'name': u'Humidity Ratio Equation Coefficient 3',
                                        'pyname': u'humidity_ratio_equation_coefficient_3',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 4',
                                       {'name': u'Humidity Ratio Equation Coefficient 4',
                                        'pyname': u'humidity_ratio_equation_coefficient_4',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 5',
                                       {'name': u'Humidity Ratio Equation Coefficient 5',
                                        'pyname': u'humidity_ratio_equation_coefficient_5',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 6',
                                       {'name': u'Humidity Ratio Equation Coefficient 6',
                                        'pyname': u'humidity_ratio_equation_coefficient_6',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 7',
                                       {'name': u'Humidity Ratio Equation Coefficient 7',
                                        'pyname': u'humidity_ratio_equation_coefficient_7',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'humidity ratio equation coefficient 8',
                                       {'name': u'Humidity Ratio Equation Coefficient 8',
                                        'pyname': u'humidity_ratio_equation_coefficient_8',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'minimum regeneration inlet air humidity ratio for humidity ratio equation',
                                       {'name': u'Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation',
                                        'pyname': u'minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum regeneration inlet air humidity ratio for humidity ratio equation',
                                       {'name': u'Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation',
                                        'pyname': u'maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'minimum regeneration inlet air temperature for humidity ratio equation',
                                       {'name': u'Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation',
                                        'pyname': u'minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum regeneration inlet air temperature for humidity ratio equation',
                                       {'name': u'Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation',
                                        'pyname': u'maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum process inlet air humidity ratio for humidity ratio equation',
                                       {'name': u'Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation',
                                        'pyname': u'minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum process inlet air humidity ratio for humidity ratio equation',
                                       {'name': u'Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation',
                                        'pyname': u'maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'minimum process inlet air temperature for humidity ratio equation',
                                       {'name': u'Minimum Process Inlet Air Temperature for Humidity Ratio Equation',
                                        'pyname': u'minimum_process_inlet_air_temperature_for_humidity_ratio_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum process inlet air temperature for humidity ratio equation',
                                       {'name': u'Maximum Process Inlet Air Temperature for Humidity Ratio Equation',
                                        'pyname': u'maximum_process_inlet_air_temperature_for_humidity_ratio_equation',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum regeneration air velocity for humidity ratio equation',
                                       {'name': u'Minimum Regeneration Air Velocity for Humidity Ratio Equation',
                                        'pyname': u'minimum_regeneration_air_velocity_for_humidity_ratio_equation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'maximum regeneration air velocity for humidity ratio equation',
                                       {'name': u'Maximum Regeneration Air Velocity for Humidity Ratio Equation',
                                        'pyname': u'maximum_regeneration_air_velocity_for_humidity_ratio_equation',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm/s'}),
                                      (u'minimum regeneration outlet air humidity ratio for humidity ratio equation',
                                       {'name': u'Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation',
                                        'pyname': u'minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'maximum regeneration outlet air humidity ratio for humidity ratio equation',
                                       {'name': u'Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation',
                                        'pyname': u'maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'kgWater/kgDryAir'}),
                                      (u'minimum regeneration inlet air relative humidity for humidity ratio equation',
                                       {'name': u'Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation',
                                        'pyname': u'minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'maximum regeneration inlet air relative humidity for humidity ratio equation',
                                       {'name': u'Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation',
                                        'pyname': u'maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'minimum process inlet air relative humidity for humidity ratio equation',
                                       {'name': u'Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation',
                                        'pyname': u'minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'maximum process inlet air relative humidity for humidity ratio equation',
                                       {'name': u'Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation',
                                        'pyname': u'maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'})]),
               'format': None,
               'group': u'Heat Recovery',
               'min-fields': 52,
               'name': u'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1',
               'pyname': u'HeatExchangerDesiccantBalancedFlowPerformanceDataType1',
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

    @property
    def nominal_air_flow_rate(self):
        """field `Nominal Air Flow Rate`

        |  Air flow rate at nominal conditions (assumed to be the same for both sides
        |  of the heat exchanger).
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `nominal_air_flow_rate` or None if not set

        """
        return self["Nominal Air Flow Rate"]

    @nominal_air_flow_rate.setter
    def nominal_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Nominal Air Flow Rate`"""
        self["Nominal Air Flow Rate"] = value

    @property
    def nominal_air_face_velocity(self):
        """field `Nominal Air Face Velocity`

        |  Units: m/s
        |  value <= 6.0

        Args:
            value (float or "Autosize"): value for IDD Field `Nominal Air Face Velocity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `nominal_air_face_velocity` or None if not set

        """
        return self["Nominal Air Face Velocity"]

    @nominal_air_face_velocity.setter
    def nominal_air_face_velocity(self, value=None):
        """Corresponds to IDD field `Nominal Air Face Velocity`"""
        self["Nominal Air Face Velocity"] = value

    @property
    def nominal_electric_power(self):
        """field `Nominal Electric Power`

        |  Parasitic electric power (e.g., desiccant wheel motor)
        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Nominal Electric Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_electric_power` or None if not set

        """
        return self["Nominal Electric Power"]

    @nominal_electric_power.setter
    def nominal_electric_power(self, value=None):
        """Corresponds to IDD field `Nominal Electric Power`"""
        self["Nominal Electric Power"] = value

    @property
    def temperature_equation_coefficient_1(self):
        """field `Temperature Equation Coefficient 1`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_1` or None if not set

        """
        return self["Temperature Equation Coefficient 1"]

    @temperature_equation_coefficient_1.setter
    def temperature_equation_coefficient_1(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 1`"""
        self["Temperature Equation Coefficient 1"] = value

    @property
    def temperature_equation_coefficient_2(self):
        """field `Temperature Equation Coefficient 2`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_2` or None if not set

        """
        return self["Temperature Equation Coefficient 2"]

    @temperature_equation_coefficient_2.setter
    def temperature_equation_coefficient_2(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 2`"""
        self["Temperature Equation Coefficient 2"] = value

    @property
    def temperature_equation_coefficient_3(self):
        """field `Temperature Equation Coefficient 3`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_3` or None if not set

        """
        return self["Temperature Equation Coefficient 3"]

    @temperature_equation_coefficient_3.setter
    def temperature_equation_coefficient_3(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 3`"""
        self["Temperature Equation Coefficient 3"] = value

    @property
    def temperature_equation_coefficient_4(self):
        """field `Temperature Equation Coefficient 4`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_4` or None if not set

        """
        return self["Temperature Equation Coefficient 4"]

    @temperature_equation_coefficient_4.setter
    def temperature_equation_coefficient_4(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 4`"""
        self["Temperature Equation Coefficient 4"] = value

    @property
    def temperature_equation_coefficient_5(self):
        """field `Temperature Equation Coefficient 5`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_5` or None if not set

        """
        return self["Temperature Equation Coefficient 5"]

    @temperature_equation_coefficient_5.setter
    def temperature_equation_coefficient_5(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 5`"""
        self["Temperature Equation Coefficient 5"] = value

    @property
    def temperature_equation_coefficient_6(self):
        """field `Temperature Equation Coefficient 6`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_6` or None if not set

        """
        return self["Temperature Equation Coefficient 6"]

    @temperature_equation_coefficient_6.setter
    def temperature_equation_coefficient_6(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 6`"""
        self["Temperature Equation Coefficient 6"] = value

    @property
    def temperature_equation_coefficient_7(self):
        """field `Temperature Equation Coefficient 7`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_7` or None if not set

        """
        return self["Temperature Equation Coefficient 7"]

    @temperature_equation_coefficient_7.setter
    def temperature_equation_coefficient_7(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 7`"""
        self["Temperature Equation Coefficient 7"] = value

    @property
    def temperature_equation_coefficient_8(self):
        """field `Temperature Equation Coefficient 8`

        Args:
            value (float): value for IDD Field `Temperature Equation Coefficient 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_equation_coefficient_8` or None if not set

        """
        return self["Temperature Equation Coefficient 8"]

    @temperature_equation_coefficient_8.setter
    def temperature_equation_coefficient_8(self, value=None):
        """Corresponds to IDD field `Temperature Equation Coefficient 8`"""
        self["Temperature Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(
            self):
        """field `Minimum Regeneration Inlet Air Humidity Ratio for Temperature
        Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Inlet Air Humidity
        Ratio for Temperature Equation`"""
        self[
            "Minimum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(
            self):
        """field `Maximum Regeneration Inlet Air Humidity Ratio for Temperature
        Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Inlet Air Humidity
        Ratio for Temperature Equation`"""
        self[
            "Maximum Regeneration Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(
            self):
        """field `Minimum Regeneration Inlet Air Temperature for Temperature
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Temperature for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Inlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Inlet Air Temperature
        for Temperature Equation`"""
        self[
            "Minimum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(
            self):
        """field `Maximum Regeneration Inlet Air Temperature for Temperature
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Temperature for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Inlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_inlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Inlet Air Temperature
        for Temperature Equation`"""
        self[
            "Maximum Regeneration Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(
            self):
        """field `Minimum Process Inlet Air Humidity Ratio for Temperature
        Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Humidity Ratio for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Process Inlet Air Humidity Ratio
        for Temperature Equation`"""
        self[
            "Minimum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(
            self):
        """field `Maximum Process Inlet Air Humidity Ratio for Temperature
        Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Humidity Ratio for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Process Inlet Air Humidity Ratio for Temperature Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_temperature_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Process Inlet Air Humidity Ratio
        for Temperature Equation`"""
        self[
            "Maximum Process Inlet Air Humidity Ratio for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_temperature_equation(self):
        """field `Minimum Process Inlet Air Temperature for Temperature
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Temperature for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Process Inlet Air Temperature for Temperature Equation"]

    @minimum_process_inlet_air_temperature_for_temperature_equation.setter
    def minimum_process_inlet_air_temperature_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Process Inlet Air Temperature for
        Temperature Equation`"""
        self[
            "Minimum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_temperature_equation(self):
        """field `Maximum Process Inlet Air Temperature for Temperature
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Temperature for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Process Inlet Air Temperature for Temperature Equation"]

    @maximum_process_inlet_air_temperature_for_temperature_equation.setter
    def maximum_process_inlet_air_temperature_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Process Inlet Air Temperature for
        Temperature Equation`"""
        self[
            "Maximum Process Inlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_temperature_equation(self):
        """field `Minimum Regeneration Air Velocity for Temperature Equation`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Minimum Regeneration Air Velocity for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Air Velocity for Temperature Equation"]

    @minimum_regeneration_air_velocity_for_temperature_equation.setter
    def minimum_regeneration_air_velocity_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Air Velocity for
        Temperature Equation`"""
        self[
            "Minimum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_temperature_equation(self):
        """field `Maximum Regeneration Air Velocity for Temperature Equation`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Maximum Regeneration Air Velocity for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Air Velocity for Temperature Equation"]

    @maximum_regeneration_air_velocity_for_temperature_equation.setter
    def maximum_regeneration_air_velocity_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Air Velocity for
        Temperature Equation`"""
        self[
            "Maximum Regeneration Air Velocity for Temperature Equation"] = value

    @property
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(
            self):
        """field `Minimum Regeneration Outlet Air Temperature for Temperature
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Regeneration Outlet Air Temperature for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Outlet Air Temperature for Temperature Equation"]

    @minimum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def minimum_regeneration_outlet_air_temperature_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Outlet Air
        Temperature for Temperature Equation`"""
        self[
            "Minimum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(
            self):
        """field `Maximum Regeneration Outlet Air Temperature for Temperature
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Regeneration Outlet Air Temperature for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_outlet_air_temperature_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Outlet Air Temperature for Temperature Equation"]

    @maximum_regeneration_outlet_air_temperature_for_temperature_equation.setter
    def maximum_regeneration_outlet_air_temperature_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Outlet Air
        Temperature for Temperature Equation`"""
        self[
            "Maximum Regeneration Outlet Air Temperature for Temperature Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(
            self):
        """field `Minimum Regeneration Inlet Air Relative Humidity for
        Temperature Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Inlet Air Relative
        Humidity for Temperature Equation`"""
        self[
            "Minimum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(
            self):
        """field `Maximum Regeneration Inlet Air Relative Humidity for
        Temperature Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Inlet Air Relative
        Humidity for Temperature Equation`"""
        self[
            "Maximum Regeneration Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(
            self):
        """field `Minimum Process Inlet Air Relative Humidity for Temperature
        Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Relative Humidity for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set

        """
        return self[
            "Minimum Process Inlet Air Relative Humidity for Temperature Equation"]

    @minimum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Process Inlet Air Relative
        Humidity for Temperature Equation`"""
        self[
            "Minimum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(
            self):
        """field `Maximum Process Inlet Air Relative Humidity for Temperature
        Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Relative Humidity for Temperature Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_temperature_equation` or None if not set

        """
        return self[
            "Maximum Process Inlet Air Relative Humidity for Temperature Equation"]

    @maximum_process_inlet_air_relative_humidity_for_temperature_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_temperature_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Process Inlet Air Relative
        Humidity for Temperature Equation`"""
        self[
            "Maximum Process Inlet Air Relative Humidity for Temperature Equation"] = value

    @property
    def humidity_ratio_equation_coefficient_1(self):
        """field `Humidity Ratio Equation Coefficient 1`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_1` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 1"]

    @humidity_ratio_equation_coefficient_1.setter
    def humidity_ratio_equation_coefficient_1(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 1`"""
        self["Humidity Ratio Equation Coefficient 1"] = value

    @property
    def humidity_ratio_equation_coefficient_2(self):
        """field `Humidity Ratio Equation Coefficient 2`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_2` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 2"]

    @humidity_ratio_equation_coefficient_2.setter
    def humidity_ratio_equation_coefficient_2(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 2`"""
        self["Humidity Ratio Equation Coefficient 2"] = value

    @property
    def humidity_ratio_equation_coefficient_3(self):
        """field `Humidity Ratio Equation Coefficient 3`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_3` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 3"]

    @humidity_ratio_equation_coefficient_3.setter
    def humidity_ratio_equation_coefficient_3(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 3`"""
        self["Humidity Ratio Equation Coefficient 3"] = value

    @property
    def humidity_ratio_equation_coefficient_4(self):
        """field `Humidity Ratio Equation Coefficient 4`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_4` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 4"]

    @humidity_ratio_equation_coefficient_4.setter
    def humidity_ratio_equation_coefficient_4(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 4`"""
        self["Humidity Ratio Equation Coefficient 4"] = value

    @property
    def humidity_ratio_equation_coefficient_5(self):
        """field `Humidity Ratio Equation Coefficient 5`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_5` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 5"]

    @humidity_ratio_equation_coefficient_5.setter
    def humidity_ratio_equation_coefficient_5(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 5`"""
        self["Humidity Ratio Equation Coefficient 5"] = value

    @property
    def humidity_ratio_equation_coefficient_6(self):
        """field `Humidity Ratio Equation Coefficient 6`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_6` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 6"]

    @humidity_ratio_equation_coefficient_6.setter
    def humidity_ratio_equation_coefficient_6(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 6`"""
        self["Humidity Ratio Equation Coefficient 6"] = value

    @property
    def humidity_ratio_equation_coefficient_7(self):
        """field `Humidity Ratio Equation Coefficient 7`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_7` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 7"]

    @humidity_ratio_equation_coefficient_7.setter
    def humidity_ratio_equation_coefficient_7(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 7`"""
        self["Humidity Ratio Equation Coefficient 7"] = value

    @property
    def humidity_ratio_equation_coefficient_8(self):
        """field `Humidity Ratio Equation Coefficient 8`

        Args:
            value (float): value for IDD Field `Humidity Ratio Equation Coefficient 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `humidity_ratio_equation_coefficient_8` or None if not set

        """
        return self["Humidity Ratio Equation Coefficient 8"]

    @humidity_ratio_equation_coefficient_8.setter
    def humidity_ratio_equation_coefficient_8(self, value=None):
        """Corresponds to IDD field `Humidity Ratio Equation Coefficient 8`"""
        self["Humidity Ratio Equation Coefficient 8"] = value

    @property
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self):
        """field `Minimum Regeneration Inlet Air Humidity Ratio for Humidity
        Ratio Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Inlet Air Humidity
        Ratio for Humidity Ratio Equation`"""
        self[
            "Minimum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self):
        """field `Maximum Regeneration Inlet Air Humidity Ratio for Humidity
        Ratio Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Inlet Air Humidity
        Ratio for Humidity Ratio Equation`"""
        self[
            "Maximum Regeneration Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(
            self):
        """field `Minimum Regeneration Inlet Air Temperature for Humidity Ratio
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Inlet Air Temperature
        for Humidity Ratio Equation`"""
        self[
            "Minimum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(
            self):
        """field `Maximum Regeneration Inlet Air Temperature for Humidity Ratio
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Inlet Air Temperature
        for Humidity Ratio Equation`"""
        self[
            "Maximum Regeneration Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self):
        """field `Minimum Process Inlet Air Humidity Ratio for Humidity Ratio
        Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Process Inlet Air Humidity Ratio
        for Humidity Ratio Equation`"""
        self[
            "Minimum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self):
        """field `Maximum Process Inlet Air Humidity Ratio for Humidity Ratio
        Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Process Inlet Air Humidity Ratio
        for Humidity Ratio Equation`"""
        self[
            "Maximum Process Inlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(
            self):
        """field `Minimum Process Inlet Air Temperature for Humidity Ratio
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Temperature for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @minimum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_temperature_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Process Inlet Air Temperature for
        Humidity Ratio Equation`"""
        self[
            "Minimum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(
            self):
        """field `Maximum Process Inlet Air Temperature for Humidity Ratio
        Equation`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Temperature for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_process_inlet_air_temperature_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Process Inlet Air Temperature for Humidity Ratio Equation"]

    @maximum_process_inlet_air_temperature_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_temperature_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Process Inlet Air Temperature for
        Humidity Ratio Equation`"""
        self[
            "Maximum Process Inlet Air Temperature for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """field `Minimum Regeneration Air Velocity for Humidity Ratio
        Equation`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Minimum Regeneration Air Velocity for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Air Velocity for Humidity Ratio Equation"]

    @minimum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def minimum_regeneration_air_velocity_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Air Velocity for
        Humidity Ratio Equation`"""
        self[
            "Minimum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(self):
        """field `Maximum Regeneration Air Velocity for Humidity Ratio
        Equation`

        |  Units: m/s

        Args:
            value (float): value for IDD Field `Maximum Regeneration Air Velocity for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_air_velocity_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Air Velocity for Humidity Ratio Equation"]

    @maximum_regeneration_air_velocity_for_humidity_ratio_equation.setter
    def maximum_regeneration_air_velocity_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Air Velocity for
        Humidity Ratio Equation`"""
        self[
            "Maximum Regeneration Air Velocity for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(
            self):
        """field `Minimum Regeneration Outlet Air Humidity Ratio for Humidity
        Ratio Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Outlet Air Humidity
        Ratio for Humidity Ratio Equation`"""
        self[
            "Minimum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(
            self):
        """field `Maximum Regeneration Outlet Air Humidity Ratio for Humidity
        Ratio Equation`

        |  Units: kgWater/kgDryAir
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"]

    @maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation.setter
    def maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Outlet Air Humidity
        Ratio for Humidity Ratio Equation`"""
        self[
            "Maximum Regeneration Outlet Air Humidity Ratio for Humidity Ratio Equation"] = value

    @property
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self):
        """field `Minimum Regeneration Inlet Air Relative Humidity for Humidity
        Ratio Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Regeneration Inlet Air Relative
        Humidity for Humidity Ratio Equation`"""
        self[
            "Minimum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self):
        """field `Maximum Regeneration Inlet Air Relative Humidity for Humidity
        Ratio Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Regeneration Inlet Air Relative
        Humidity for Humidity Ratio Equation`"""
        self[
            "Maximum Regeneration Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self):
        """field `Minimum Process Inlet Air Relative Humidity for Humidity
        Ratio Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Minimum Process Inlet Air Relative
        Humidity for Humidity Ratio Equation`"""
        self[
            "Minimum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value

    @property
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self):
        """field `Maximum Process Inlet Air Relative Humidity for Humidity
        Ratio Equation`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation` or None if not set

        """
        return self[
            "Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"]

    @maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation.setter
    def maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation(
            self,
            value=None):
        """Corresponds to IDD field `Maximum Process Inlet Air Relative
        Humidity for Humidity Ratio Equation`"""
        self[
            "Maximum Process Inlet Air Relative Humidity for Humidity Ratio Equation"] = value


