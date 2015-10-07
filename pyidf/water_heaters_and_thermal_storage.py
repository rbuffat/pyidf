""" Data objects in group "Water Heaters and Thermal Storage"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class WaterHeaterMixed(DataObject):

    """ Corresponds to IDD object `WaterHeater:Mixed`
        Water heater with well-mixed, single-node water tank. May be used to model a tankless
        water heater (small tank volume), a hot water storage tank (zero heater capacity), or
        a heat pump water heater (see WaterHeater:HeatPump:PumpedCondenser.)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'tank volume',
                                       {'name': u'Tank Volume',
                                        'pyname': u'tank_volume',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'setpoint temperature schedule name',
                                       {'name': u'Setpoint Temperature Schedule Name',
                                        'pyname': u'setpoint_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'deadband temperature difference',
                                       {'name': u'Deadband Temperature Difference',
                                        'pyname': u'deadband_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'maximum temperature limit',
                                       {'name': u'Maximum Temperature Limit',
                                        'pyname': u'maximum_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'heater control type',
                                       {'name': u'Heater Control Type',
                                        'pyname': u'heater_control_type',
                                        'default': u'Cycle',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Cycle',
                                                            u'Modulate'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heater maximum capacity',
                                       {'name': u'Heater Maximum Capacity',
                                        'pyname': u'heater_maximum_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heater minimum capacity',
                                       {'name': u'Heater Minimum Capacity',
                                        'pyname': u'heater_minimum_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heater ignition minimum flow rate',
                                       {'name': u'Heater Ignition Minimum Flow Rate',
                                        'pyname': u'heater_ignition_minimum_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heater ignition delay',
                                       {'name': u'Heater Ignition Delay',
                                        'pyname': u'heater_ignition_delay',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u's'}),
                                      (u'heater fuel type',
                                       {'name': u'Heater Fuel Type',
                                        'pyname': u'heater_fuel_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'Steam',
                                                            u'DistrictHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heater thermal efficiency',
                                       {'name': u'Heater Thermal Efficiency',
                                        'pyname': u'heater_thermal_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'part load factor curve name',
                                       {'name': u'Part Load Factor Curve Name',
                                        'pyname': u'part_load_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'off cycle parasitic fuel consumption rate',
                                       {'name': u'Off Cycle Parasitic Fuel Consumption Rate',
                                        'pyname': u'off_cycle_parasitic_fuel_consumption_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'off cycle parasitic fuel type',
                                       {'name': u'Off Cycle Parasitic Fuel Type',
                                        'pyname': u'off_cycle_parasitic_fuel_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'Steam',
                                                            u'DistrictHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'off cycle parasitic heat fraction to tank',
                                       {'name': u'Off Cycle Parasitic Heat Fraction to Tank',
                                        'pyname': u'off_cycle_parasitic_heat_fraction_to_tank',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'on cycle parasitic fuel consumption rate',
                                       {'name': u'On Cycle Parasitic Fuel Consumption Rate',
                                        'pyname': u'on_cycle_parasitic_fuel_consumption_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'on cycle parasitic fuel type',
                                       {'name': u'On Cycle Parasitic Fuel Type',
                                        'pyname': u'on_cycle_parasitic_fuel_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'Steam',
                                                            u'DistrictHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'on cycle parasitic heat fraction to tank',
                                       {'name': u'On Cycle Parasitic Heat Fraction to Tank',
                                        'pyname': u'on_cycle_parasitic_heat_fraction_to_tank',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'ambient temperature indicator',
                                       {'name': u'Ambient Temperature Indicator',
                                        'pyname': u'ambient_temperature_indicator',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ambient temperature schedule name',
                                       {'name': u'Ambient Temperature Schedule Name',
                                        'pyname': u'ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature zone name',
                                       {'name': u'Ambient Temperature Zone Name',
                                        'pyname': u'ambient_temperature_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature outdoor air node name',
                                       {'name': u'Ambient Temperature Outdoor Air Node Name',
                                        'pyname': u'ambient_temperature_outdoor_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'off cycle loss coefficient to ambient temperature',
                                       {'name': u'Off Cycle Loss Coefficient to Ambient Temperature',
                                        'pyname': u'off_cycle_loss_coefficient_to_ambient_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'off cycle loss fraction to zone',
                                       {'name': u'Off Cycle Loss Fraction to Zone',
                                        'pyname': u'off_cycle_loss_fraction_to_zone',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'on cycle loss coefficient to ambient temperature',
                                       {'name': u'On Cycle Loss Coefficient to Ambient Temperature',
                                        'pyname': u'on_cycle_loss_coefficient_to_ambient_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'on cycle loss fraction to zone',
                                       {'name': u'On Cycle Loss Fraction to Zone',
                                        'pyname': u'on_cycle_loss_fraction_to_zone',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'peak use flow rate',
                                       {'name': u'Peak Use Flow Rate',
                                        'pyname': u'peak_use_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'use flow rate fraction schedule name',
                                       {'name': u'Use Flow Rate Fraction Schedule Name',
                                        'pyname': u'use_flow_rate_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cold water supply temperature schedule name',
                                       {'name': u'Cold Water Supply Temperature Schedule Name',
                                        'pyname': u'cold_water_supply_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'use side inlet node name',
                                       {'name': u'Use Side Inlet Node Name',
                                        'pyname': u'use_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side outlet node name',
                                       {'name': u'Use Side Outlet Node Name',
                                        'pyname': u'use_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side effectiveness',
                                       {'name': u'Use Side Effectiveness',
                                        'pyname': u'use_side_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'source side inlet node name',
                                       {'name': u'Source Side Inlet Node Name',
                                        'pyname': u'source_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side outlet node name',
                                       {'name': u'Source Side Outlet Node Name',
                                        'pyname': u'source_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side effectiveness',
                                       {'name': u'Source Side Effectiveness',
                                        'pyname': u'source_side_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'use side design flow rate',
                                       {'name': u'Use Side Design Flow Rate',
                                        'pyname': u'use_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'source side design flow rate',
                                       {'name': u'Source Side Design Flow Rate',
                                        'pyname': u'source_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'indirect water heating recovery time',
                                       {'name': u'Indirect Water Heating Recovery Time',
                                        'pyname': u'indirect_water_heating_recovery_time',
                                        'default': 1.5,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'source side flow control mode',
                                       {'name': u'Source Side Flow Control Mode',
                                        'pyname': u'source_side_flow_control_mode',
                                        'default': u'IndirectHeatPrimarySetpoint',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'StorageTank',
                                                            u'IndirectHeatPrimarySetpoint',
                                                            u'IndirectHeatAlternateSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'indirect alternate setpoint temperature schedule name',
                                       {'name': u'Indirect Alternate Setpoint Temperature Schedule Name',
                                        'pyname': u'indirect_alternate_setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 0,
               'name': u'WaterHeater:Mixed',
               'pyname': u'WaterHeaterMixed',
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
    def tank_volume(self):
        """field `Tank Volume`

        |  Units: m3
        |  IP-Units: gal

        Args:
            value (float or "Autosize"): value for IDD Field `Tank Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `tank_volume` or None if not set

        """
        return self["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=None):
        """Corresponds to IDD field `Tank Volume`"""
        self["Tank Volume"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set

        """
        return self["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule Name`"""
        self["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """field `Deadband Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Deadband Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set

        """
        return self["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=None):
        """Corresponds to IDD field `Deadband Temperature Difference`"""
        self["Deadband Temperature Difference"] = value

    @property
    def maximum_temperature_limit(self):
        """field `Maximum Temperature Limit`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_temperature_limit` or None if not set

        """
        return self["Maximum Temperature Limit"]

    @maximum_temperature_limit.setter
    def maximum_temperature_limit(self, value=None):
        """Corresponds to IDD field `Maximum Temperature Limit`"""
        self["Maximum Temperature Limit"] = value

    @property
    def heater_control_type(self):
        """field `Heater Control Type`

        |  Default value: Cycle

        Args:
            value (str): value for IDD Field `Heater Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heater_control_type` or None if not set

        """
        return self["Heater Control Type"]

    @heater_control_type.setter
    def heater_control_type(self, value="Cycle"):
        """Corresponds to IDD field `Heater Control Type`"""
        self["Heater Control Type"] = value

    @property
    def heater_maximum_capacity(self):
        """field `Heater Maximum Capacity`

        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Heater Maximum Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heater_maximum_capacity` or None if not set

        """
        return self["Heater Maximum Capacity"]

    @heater_maximum_capacity.setter
    def heater_maximum_capacity(self, value=None):
        """Corresponds to IDD field `Heater Maximum Capacity`"""
        self["Heater Maximum Capacity"] = value

    @property
    def heater_minimum_capacity(self):
        """field `Heater Minimum Capacity`

        |  Only used when Heater Control Type is set to Modulate
        |  Units: W

        Args:
            value (float): value for IDD Field `Heater Minimum Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_minimum_capacity` or None if not set

        """
        return self["Heater Minimum Capacity"]

    @heater_minimum_capacity.setter
    def heater_minimum_capacity(self, value=None):
        """Corresponds to IDD field `Heater Minimum Capacity`"""
        self["Heater Minimum Capacity"] = value

    @property
    def heater_ignition_minimum_flow_rate(self):
        """field `Heater Ignition Minimum Flow Rate`

        |  Not yet implemented
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Heater Ignition Minimum Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_ignition_minimum_flow_rate` or None if not set

        """
        return self["Heater Ignition Minimum Flow Rate"]

    @heater_ignition_minimum_flow_rate.setter
    def heater_ignition_minimum_flow_rate(self, value=None):
        """Corresponds to IDD field `Heater Ignition Minimum Flow Rate`"""
        self["Heater Ignition Minimum Flow Rate"] = value

    @property
    def heater_ignition_delay(self):
        """field `Heater Ignition Delay`

        |  Not yet implemented
        |  Units: s

        Args:
            value (float): value for IDD Field `Heater Ignition Delay`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_ignition_delay` or None if not set

        """
        return self["Heater Ignition Delay"]

    @heater_ignition_delay.setter
    def heater_ignition_delay(self, value=None):
        """Corresponds to IDD field `Heater Ignition Delay`"""
        self["Heater Ignition Delay"] = value

    @property
    def heater_fuel_type(self):
        """field `Heater Fuel Type`

        Args:
            value (str): value for IDD Field `Heater Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heater_fuel_type` or None if not set

        """
        return self["Heater Fuel Type"]

    @heater_fuel_type.setter
    def heater_fuel_type(self, value=None):
        """Corresponds to IDD field `Heater Fuel Type`"""
        self["Heater Fuel Type"] = value

    @property
    def heater_thermal_efficiency(self):
        """field `Heater Thermal Efficiency`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Heater Thermal Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_thermal_efficiency` or None if not set

        """
        return self["Heater Thermal Efficiency"]

    @heater_thermal_efficiency.setter
    def heater_thermal_efficiency(self, value=None):
        """Corresponds to IDD field `Heater Thermal Efficiency`"""
        self["Heater Thermal Efficiency"] = value

    @property
    def part_load_factor_curve_name(self):
        """field `Part Load Factor Curve Name`

        Args:
            value (str): value for IDD Field `Part Load Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `part_load_factor_curve_name` or None if not set

        """
        return self["Part Load Factor Curve Name"]

    @part_load_factor_curve_name.setter
    def part_load_factor_curve_name(self, value=None):
        """Corresponds to IDD field `Part Load Factor Curve Name`"""
        self["Part Load Factor Curve Name"] = value

    @property
    def off_cycle_parasitic_fuel_consumption_rate(self):
        """field `Off Cycle Parasitic Fuel Consumption Rate`

        |  Units: W

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Fuel Consumption Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_fuel_consumption_rate` or None if not set

        """
        return self["Off Cycle Parasitic Fuel Consumption Rate"]

    @off_cycle_parasitic_fuel_consumption_rate.setter
    def off_cycle_parasitic_fuel_consumption_rate(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Fuel Consumption
        Rate`"""
        self["Off Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def off_cycle_parasitic_fuel_type(self):
        """field `Off Cycle Parasitic Fuel Type`

        Args:
            value (str): value for IDD Field `Off Cycle Parasitic Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `off_cycle_parasitic_fuel_type` or None if not set

        """
        return self["Off Cycle Parasitic Fuel Type"]

    @off_cycle_parasitic_fuel_type.setter
    def off_cycle_parasitic_fuel_type(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Fuel Type`"""
        self["Off Cycle Parasitic Fuel Type"] = value

    @property
    def off_cycle_parasitic_heat_fraction_to_tank(self):
        """field `Off Cycle Parasitic Heat Fraction to Tank`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Heat Fraction to Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_heat_fraction_to_tank` or None if not set

        """
        return self["Off Cycle Parasitic Heat Fraction to Tank"]

    @off_cycle_parasitic_heat_fraction_to_tank.setter
    def off_cycle_parasitic_heat_fraction_to_tank(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Heat Fraction to
        Tank`"""
        self["Off Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def on_cycle_parasitic_fuel_consumption_rate(self):
        """field `On Cycle Parasitic Fuel Consumption Rate`

        |  Units: W

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Fuel Consumption Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_fuel_consumption_rate` or None if not set

        """
        return self["On Cycle Parasitic Fuel Consumption Rate"]

    @on_cycle_parasitic_fuel_consumption_rate.setter
    def on_cycle_parasitic_fuel_consumption_rate(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Fuel Consumption
        Rate`"""
        self["On Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def on_cycle_parasitic_fuel_type(self):
        """field `On Cycle Parasitic Fuel Type`

        Args:
            value (str): value for IDD Field `On Cycle Parasitic Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `on_cycle_parasitic_fuel_type` or None if not set

        """
        return self["On Cycle Parasitic Fuel Type"]

    @on_cycle_parasitic_fuel_type.setter
    def on_cycle_parasitic_fuel_type(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Fuel Type`"""
        self["On Cycle Parasitic Fuel Type"] = value

    @property
    def on_cycle_parasitic_heat_fraction_to_tank(self):
        """field `On Cycle Parasitic Heat Fraction to Tank`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Heat Fraction to Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_heat_fraction_to_tank` or None if not set

        """
        return self["On Cycle Parasitic Heat Fraction to Tank"]

    @on_cycle_parasitic_heat_fraction_to_tank.setter
    def on_cycle_parasitic_heat_fraction_to_tank(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Heat Fraction to
        Tank`"""
        self["On Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def ambient_temperature_indicator(self):
        """field `Ambient Temperature Indicator`

        Args:
            value (str): value for IDD Field `Ambient Temperature Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set

        """
        return self["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Indicator`"""
        self["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set

        """
        return self["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Schedule Name`"""
        self["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """field `Ambient Temperature Zone Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set

        """
        return self["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Zone Name`"""
        self["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """field `Ambient Temperature Outdoor Air Node Name`

        |  required for Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `Ambient Temperature Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set

        """
        return self["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Outdoor Air Node
        Name`"""
        self["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def off_cycle_loss_coefficient_to_ambient_temperature(self):
        """field `Off Cycle Loss Coefficient to Ambient Temperature`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Off Cycle Loss Coefficient to Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_loss_coefficient_to_ambient_temperature` or None if not set

        """
        return self["Off Cycle Loss Coefficient to Ambient Temperature"]

    @off_cycle_loss_coefficient_to_ambient_temperature.setter
    def off_cycle_loss_coefficient_to_ambient_temperature(self, value=None):
        """Corresponds to IDD field `Off Cycle Loss Coefficient to Ambient
        Temperature`"""
        self["Off Cycle Loss Coefficient to Ambient Temperature"] = value

    @property
    def off_cycle_loss_fraction_to_zone(self):
        """field `Off Cycle Loss Fraction to Zone`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Off Cycle Loss Fraction to Zone`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_loss_fraction_to_zone` or None if not set

        """
        return self["Off Cycle Loss Fraction to Zone"]

    @off_cycle_loss_fraction_to_zone.setter
    def off_cycle_loss_fraction_to_zone(self, value=1.0):
        """Corresponds to IDD field `Off Cycle Loss Fraction to Zone`"""
        self["Off Cycle Loss Fraction to Zone"] = value

    @property
    def on_cycle_loss_coefficient_to_ambient_temperature(self):
        """field `On Cycle Loss Coefficient to Ambient Temperature`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `On Cycle Loss Coefficient to Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_loss_coefficient_to_ambient_temperature` or None if not set

        """
        return self["On Cycle Loss Coefficient to Ambient Temperature"]

    @on_cycle_loss_coefficient_to_ambient_temperature.setter
    def on_cycle_loss_coefficient_to_ambient_temperature(self, value=None):
        """Corresponds to IDD field `On Cycle Loss Coefficient to Ambient
        Temperature`"""
        self["On Cycle Loss Coefficient to Ambient Temperature"] = value

    @property
    def on_cycle_loss_fraction_to_zone(self):
        """field `On Cycle Loss Fraction to Zone`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `On Cycle Loss Fraction to Zone`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_loss_fraction_to_zone` or None if not set

        """
        return self["On Cycle Loss Fraction to Zone"]

    @on_cycle_loss_fraction_to_zone.setter
    def on_cycle_loss_fraction_to_zone(self, value=1.0):
        """Corresponds to IDD field `On Cycle Loss Fraction to Zone`"""
        self["On Cycle Loss Fraction to Zone"] = value

    @property
    def peak_use_flow_rate(self):
        """field `Peak Use Flow Rate`

        |  Only used if Use Side Node connections are blank
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Peak Use Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `peak_use_flow_rate` or None if not set

        """
        return self["Peak Use Flow Rate"]

    @peak_use_flow_rate.setter
    def peak_use_flow_rate(self, value=None):
        """Corresponds to IDD field `Peak Use Flow Rate`"""
        self["Peak Use Flow Rate"] = value

    @property
    def use_flow_rate_fraction_schedule_name(self):
        """field `Use Flow Rate Fraction Schedule Name`

        |  Only used if Use Side Node connections are blank

        Args:
            value (str): value for IDD Field `Use Flow Rate Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_flow_rate_fraction_schedule_name` or None if not set

        """
        return self["Use Flow Rate Fraction Schedule Name"]

    @use_flow_rate_fraction_schedule_name.setter
    def use_flow_rate_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Use Flow Rate Fraction Schedule Name`"""
        self["Use Flow Rate Fraction Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """field `Cold Water Supply Temperature Schedule Name`

        |  Only used if Use Side Node connections are blank
        |  Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `Cold Water Supply Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set

        """
        return self["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cold Water Supply Temperature Schedule
        Name`"""
        self["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def use_side_inlet_node_name(self):
        """field `Use Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set

        """
        return self["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Inlet Node Name`"""
        self["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """field `Use Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set

        """
        return self["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Outlet Node Name`"""
        self["Use Side Outlet Node Name"] = value

    @property
    def use_side_effectiveness(self):
        """field `Use Side Effectiveness`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Use Side Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `use_side_effectiveness` or None if not set

        """
        return self["Use Side Effectiveness"]

    @use_side_effectiveness.setter
    def use_side_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Use Side Effectiveness`"""
        self["Use Side Effectiveness"] = value

    @property
    def source_side_inlet_node_name(self):
        """field `Source Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set

        """
        return self["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Inlet Node Name`"""
        self["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """field `Source Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set

        """
        return self["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Outlet Node Name`"""
        self["Source Side Outlet Node Name"] = value

    @property
    def source_side_effectiveness(self):
        """field `Source Side Effectiveness`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Source Side Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_side_effectiveness` or None if not set

        """
        return self["Source Side Effectiveness"]

    @source_side_effectiveness.setter
    def source_side_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Source Side Effectiveness`"""
        self["Source Side Effectiveness"] = value

    @property
    def use_side_design_flow_rate(self):
        """field `Use Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Use Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `use_side_design_flow_rate` or None if not set

        """
        return self["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Use Side Design Flow Rate`"""
        self["Use Side Design Flow Rate"] = value

    @property
    def source_side_design_flow_rate(self):
        """field `Source Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Source Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `source_side_design_flow_rate` or None if not set

        """
        return self["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Source Side Design Flow Rate`"""
        self["Source Side Design Flow Rate"] = value

    @property
    def indirect_water_heating_recovery_time(self):
        """field `Indirect Water Heating Recovery Time`

        |  Parameter for autosizing design flow rates for indirectly heated water tanks
        |  Time required to raise temperature of entire tank from 14.4C to 57.2C
        |  Units: hr
        |  Default value: 1.5

        Args:
            value (float): value for IDD Field `Indirect Water Heating Recovery Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `indirect_water_heating_recovery_time` or None if not set

        """
        return self["Indirect Water Heating Recovery Time"]

    @indirect_water_heating_recovery_time.setter
    def indirect_water_heating_recovery_time(self, value=1.5):
        """Corresponds to IDD field `Indirect Water Heating Recovery Time`"""
        self["Indirect Water Heating Recovery Time"] = value

    @property
    def source_side_flow_control_mode(self):
        """field `Source Side Flow Control Mode`

        |  StorageTank mode always requests flow unless tank is at its Maximum Temperature Limit
        |  IndirectHeatPrimarySetpoint mode requests flow whenever primary setpoint calls for heat
        |  IndirectHeatAlternateSetpoint mode requests flow whenever alternate indirect setpoint calls for heat
        |  Default value: IndirectHeatPrimarySetpoint

        Args:
            value (str): value for IDD Field `Source Side Flow Control Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_flow_control_mode` or None if not set

        """
        return self["Source Side Flow Control Mode"]

    @source_side_flow_control_mode.setter
    def source_side_flow_control_mode(
            self,
            value="IndirectHeatPrimarySetpoint"):
        """Corresponds to IDD field `Source Side Flow Control Mode`"""
        self["Source Side Flow Control Mode"] = value

    @property
    def indirect_alternate_setpoint_temperature_schedule_name(self):
        """field `Indirect Alternate Setpoint Temperature Schedule Name`

        |  This field is only used if the previous is set to IndirectHeatAlternateSetpoint

        Args:
            value (str): value for IDD Field `Indirect Alternate Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `indirect_alternate_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Indirect Alternate Setpoint Temperature Schedule Name"]

    @indirect_alternate_setpoint_temperature_schedule_name.setter
    def indirect_alternate_setpoint_temperature_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Indirect Alternate Setpoint Temperature
        Schedule Name`"""
        self["Indirect Alternate Setpoint Temperature Schedule Name"] = value




class WaterHeaterStratified(DataObject):

    """ Corresponds to IDD object `WaterHeater:Stratified`
        Water heater with stratified, multi-node water tank. May be used to model a tankless
        water heater (small tank volume), a hot water storage tank (zero heater capacity), or
        a heat pump water heater (see WaterHeater:HeatPump:*.)
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'end-use subcategory',
                                       {'name': u'End-Use Subcategory',
                                        'pyname': u'enduse_subcategory',
                                        'default': u'General',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'tank volume',
                                       {'name': u'Tank Volume',
                                        'pyname': u'tank_volume',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'tank height',
                                       {'name': u'Tank Height',
                                        'pyname': u'tank_height',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'tank shape',
                                       {'name': u'Tank Shape',
                                        'pyname': u'tank_shape',
                                        'default': u'VerticalCylinder',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'VerticalCylinder',
                                                            u'HorizontalCylinder',
                                                            u'Other'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'tank perimeter',
                                       {'name': u'Tank Perimeter',
                                        'pyname': u'tank_perimeter',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'maximum temperature limit',
                                       {'name': u'Maximum Temperature Limit',
                                        'pyname': u'maximum_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'heater priority control',
                                       {'name': u'Heater Priority Control',
                                        'pyname': u'heater_priority_control',
                                        'default': u'MasterSlave',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MasterSlave',
                                                            u'Simultaneous'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heater 1 setpoint temperature schedule name',
                                       {'name': u'Heater 1 Setpoint Temperature Schedule Name',
                                        'pyname': u'heater_1_setpoint_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heater 1 deadband temperature difference',
                                       {'name': u'Heater 1 Deadband Temperature Difference',
                                        'pyname': u'heater_1_deadband_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'heater 1 capacity',
                                       {'name': u'Heater 1 Capacity',
                                        'pyname': u'heater_1_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heater 1 height',
                                       {'name': u'Heater 1 Height',
                                        'pyname': u'heater_1_height',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'heater 2 setpoint temperature schedule name',
                                       {'name': u'Heater 2 Setpoint Temperature Schedule Name',
                                        'pyname': u'heater_2_setpoint_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heater 2 deadband temperature difference',
                                       {'name': u'Heater 2 Deadband Temperature Difference',
                                        'pyname': u'heater_2_deadband_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'heater 2 capacity',
                                       {'name': u'Heater 2 Capacity',
                                        'pyname': u'heater_2_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'heater 2 height',
                                       {'name': u'Heater 2 Height',
                                        'pyname': u'heater_2_height',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'heater fuel type',
                                       {'name': u'Heater Fuel Type',
                                        'pyname': u'heater_fuel_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'Steam',
                                                            u'DistrictHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heater thermal efficiency',
                                       {'name': u'Heater Thermal Efficiency',
                                        'pyname': u'heater_thermal_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'off cycle parasitic fuel consumption rate',
                                       {'name': u'Off Cycle Parasitic Fuel Consumption Rate',
                                        'pyname': u'off_cycle_parasitic_fuel_consumption_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'off cycle parasitic fuel type',
                                       {'name': u'Off Cycle Parasitic Fuel Type',
                                        'pyname': u'off_cycle_parasitic_fuel_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'Steam',
                                                            u'DistrictHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'off cycle parasitic heat fraction to tank',
                                       {'name': u'Off Cycle Parasitic Heat Fraction to Tank',
                                        'pyname': u'off_cycle_parasitic_heat_fraction_to_tank',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'off cycle parasitic height',
                                       {'name': u'Off Cycle Parasitic Height',
                                        'pyname': u'off_cycle_parasitic_height',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'on cycle parasitic fuel consumption rate',
                                       {'name': u'On Cycle Parasitic Fuel Consumption Rate',
                                        'pyname': u'on_cycle_parasitic_fuel_consumption_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'on cycle parasitic fuel type',
                                       {'name': u'On Cycle Parasitic Fuel Type',
                                        'pyname': u'on_cycle_parasitic_fuel_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'Coal',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2',
                                                            u'Steam',
                                                            u'DistrictHeating'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'on cycle parasitic heat fraction to tank',
                                       {'name': u'On Cycle Parasitic Heat Fraction to Tank',
                                        'pyname': u'on_cycle_parasitic_heat_fraction_to_tank',
                                        'default': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'on cycle parasitic height',
                                       {'name': u'On Cycle Parasitic Height',
                                        'pyname': u'on_cycle_parasitic_height',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'ambient temperature indicator',
                                       {'name': u'Ambient Temperature Indicator',
                                        'pyname': u'ambient_temperature_indicator',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ambient temperature schedule name',
                                       {'name': u'Ambient Temperature Schedule Name',
                                        'pyname': u'ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature zone name',
                                       {'name': u'Ambient Temperature Zone Name',
                                        'pyname': u'ambient_temperature_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature outdoor air node name',
                                       {'name': u'Ambient Temperature Outdoor Air Node Name',
                                        'pyname': u'ambient_temperature_outdoor_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'uniform skin loss coefficient per unit area to ambient temperature',
                                       {'name': u'Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature',
                                        'pyname': u'uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'skin loss fraction to zone',
                                       {'name': u'Skin Loss Fraction to Zone',
                                        'pyname': u'skin_loss_fraction_to_zone',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'off cycle flue loss coefficient to ambient temperature',
                                       {'name': u'Off Cycle Flue Loss Coefficient to Ambient Temperature',
                                        'pyname': u'off_cycle_flue_loss_coefficient_to_ambient_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'off cycle flue loss fraction to zone',
                                       {'name': u'Off Cycle Flue Loss Fraction to Zone',
                                        'pyname': u'off_cycle_flue_loss_fraction_to_zone',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'peak use flow rate',
                                       {'name': u'Peak Use Flow Rate',
                                        'pyname': u'peak_use_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'use flow rate fraction schedule name',
                                       {'name': u'Use Flow Rate Fraction Schedule Name',
                                        'pyname': u'use_flow_rate_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cold water supply temperature schedule name',
                                       {'name': u'Cold Water Supply Temperature Schedule Name',
                                        'pyname': u'cold_water_supply_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'use side inlet node name',
                                       {'name': u'Use Side Inlet Node Name',
                                        'pyname': u'use_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side outlet node name',
                                       {'name': u'Use Side Outlet Node Name',
                                        'pyname': u'use_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side effectiveness',
                                       {'name': u'Use Side Effectiveness',
                                        'pyname': u'use_side_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'use side inlet height',
                                       {'name': u'Use Side Inlet Height',
                                        'pyname': u'use_side_inlet_height',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'use side outlet height',
                                       {'name': u'Use Side Outlet Height',
                                        'pyname': u'use_side_outlet_height',
                                        'default': 'Autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'source side inlet node name',
                                       {'name': u'Source Side Inlet Node Name',
                                        'pyname': u'source_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side outlet node name',
                                       {'name': u'Source Side Outlet Node Name',
                                        'pyname': u'source_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side effectiveness',
                                       {'name': u'Source Side Effectiveness',
                                        'pyname': u'source_side_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'source side inlet height',
                                       {'name': u'Source Side Inlet Height',
                                        'pyname': u'source_side_inlet_height',
                                        'default': 'Autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'source side outlet height',
                                       {'name': u'Source Side Outlet Height',
                                        'pyname': u'source_side_outlet_height',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'inlet mode',
                                       {'name': u'Inlet Mode',
                                        'pyname': u'inlet_mode',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'Seeking'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'use side design flow rate',
                                       {'name': u'Use Side Design Flow Rate',
                                        'pyname': u'use_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'source side design flow rate',
                                       {'name': u'Source Side Design Flow Rate',
                                        'pyname': u'source_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'indirect water heating recovery time',
                                       {'name': u'Indirect Water Heating Recovery Time',
                                        'pyname': u'indirect_water_heating_recovery_time',
                                        'default': 1.5,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'number of nodes',
                                       {'name': u'Number of Nodes',
                                        'pyname': u'number_of_nodes',
                                        'default': 1,
                                        'maximum': 12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'additional destratification conductivity',
                                       {'name': u'Additional Destratification Conductivity',
                                        'pyname': u'additional_destratification_conductivity',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'node 1 additional loss coefficient',
                                       {'name': u'Node 1 Additional Loss Coefficient',
                                        'pyname': u'node_1_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 2 additional loss coefficient',
                                       {'name': u'Node 2 Additional Loss Coefficient',
                                        'pyname': u'node_2_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 3 additional loss coefficient',
                                       {'name': u'Node 3 Additional Loss Coefficient',
                                        'pyname': u'node_3_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 4 additional loss coefficient',
                                       {'name': u'Node 4 Additional Loss Coefficient',
                                        'pyname': u'node_4_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 5 additional loss coefficient',
                                       {'name': u'Node 5 Additional Loss Coefficient',
                                        'pyname': u'node_5_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 6 additional loss coefficient',
                                       {'name': u'Node 6 Additional Loss Coefficient',
                                        'pyname': u'node_6_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 7 additional loss coefficient',
                                       {'name': u'Node 7 Additional Loss Coefficient',
                                        'pyname': u'node_7_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 8 additional loss coefficient',
                                       {'name': u'Node 8 Additional Loss Coefficient',
                                        'pyname': u'node_8_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 9 additional loss coefficient',
                                       {'name': u'Node 9 Additional Loss Coefficient',
                                        'pyname': u'node_9_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 10 additional loss coefficient',
                                       {'name': u'Node 10 Additional Loss Coefficient',
                                        'pyname': u'node_10_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 11 additional loss coefficient',
                                       {'name': u'Node 11 Additional Loss Coefficient',
                                        'pyname': u'node_11_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 12 additional loss coefficient',
                                       {'name': u'Node 12 Additional Loss Coefficient',
                                        'pyname': u'node_12_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'source side flow control mode',
                                       {'name': u'Source Side Flow Control Mode',
                                        'pyname': u'source_side_flow_control_mode',
                                        'default': u'IndirectHeatPrimarySetpoint',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'StorageTank',
                                                            u'IndirectHeatPrimarySetpoint',
                                                            u'IndirectHeatAlternateSetpoint'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'indirect alternate setpoint temperature schedule name',
                                       {'name': u'Indirect Alternate Setpoint Temperature Schedule Name',
                                        'pyname': u'indirect_alternate_setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 0,
               'name': u'WaterHeater:Stratified',
               'pyname': u'WaterHeaterStratified',
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
    def enduse_subcategory(self):
        """field `End-Use Subcategory`

        |  Default value: General

        Args:
            value (str): value for IDD Field `End-Use Subcategory`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `enduse_subcategory` or None if not set
        """
        return self["End-Use Subcategory"]

    @enduse_subcategory.setter
    def enduse_subcategory(self, value="General"):
        """  Corresponds to IDD field `End-Use Subcategory`

        """
        self["End-Use Subcategory"] = value

    @property
    def tank_volume(self):
        """field `Tank Volume`

        |  Units: m3
        |  IP-Units: gal

        Args:
            value (float or "Autosize"): value for IDD Field `Tank Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `tank_volume` or None if not set

        """
        return self["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=None):
        """Corresponds to IDD field `Tank Volume`"""
        self["Tank Volume"] = value

    @property
    def tank_height(self):
        """field `Tank Height`

        |  Height is measured in the axial direction for horizontal cylinders
        |  Units: m

        Args:
            value (float or "Autosize"): value for IDD Field `Tank Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `tank_height` or None if not set

        """
        return self["Tank Height"]

    @tank_height.setter
    def tank_height(self, value=None):
        """Corresponds to IDD field `Tank Height`"""
        self["Tank Height"] = value

    @property
    def tank_shape(self):
        """field `Tank Shape`

        |  Default value: VerticalCylinder

        Args:
            value (str): value for IDD Field `Tank Shape`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_shape` or None if not set

        """
        return self["Tank Shape"]

    @tank_shape.setter
    def tank_shape(self, value="VerticalCylinder"):
        """Corresponds to IDD field `Tank Shape`"""
        self["Tank Shape"] = value

    @property
    def tank_perimeter(self):
        """field `Tank Perimeter`

        |  Only used if Tank Shape is Other
        |  Units: m

        Args:
            value (float): value for IDD Field `Tank Perimeter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_perimeter` or None if not set

        """
        return self["Tank Perimeter"]

    @tank_perimeter.setter
    def tank_perimeter(self, value=None):
        """Corresponds to IDD field `Tank Perimeter`"""
        self["Tank Perimeter"] = value

    @property
    def maximum_temperature_limit(self):
        """field `Maximum Temperature Limit`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_temperature_limit` or None if not set

        """
        return self["Maximum Temperature Limit"]

    @maximum_temperature_limit.setter
    def maximum_temperature_limit(self, value=None):
        """Corresponds to IDD field `Maximum Temperature Limit`"""
        self["Maximum Temperature Limit"] = value

    @property
    def heater_priority_control(self):
        """field `Heater Priority Control`

        |  Default value: MasterSlave

        Args:
            value (str): value for IDD Field `Heater Priority Control`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heater_priority_control` or None if not set

        """
        return self["Heater Priority Control"]

    @heater_priority_control.setter
    def heater_priority_control(self, value="MasterSlave"):
        """Corresponds to IDD field `Heater Priority Control`"""
        self["Heater Priority Control"] = value

    @property
    def heater_1_setpoint_temperature_schedule_name(self):
        """field `Heater 1 Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heater 1 Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heater_1_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Heater 1 Setpoint Temperature Schedule Name"]

    @heater_1_setpoint_temperature_schedule_name.setter
    def heater_1_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heater 1 Setpoint Temperature Schedule
        Name`"""
        self["Heater 1 Setpoint Temperature Schedule Name"] = value

    @property
    def heater_1_deadband_temperature_difference(self):
        """field `Heater 1 Deadband Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Heater 1 Deadband Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_1_deadband_temperature_difference` or None if not set

        """
        return self["Heater 1 Deadband Temperature Difference"]

    @heater_1_deadband_temperature_difference.setter
    def heater_1_deadband_temperature_difference(self, value=None):
        """Corresponds to IDD field `Heater 1 Deadband Temperature
        Difference`"""
        self["Heater 1 Deadband Temperature Difference"] = value

    @property
    def heater_1_capacity(self):
        """field `Heater 1 Capacity`

        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Heater 1 Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `heater_1_capacity` or None if not set

        """
        return self["Heater 1 Capacity"]

    @heater_1_capacity.setter
    def heater_1_capacity(self, value=None):
        """Corresponds to IDD field `Heater 1 Capacity`"""
        self["Heater 1 Capacity"] = value

    @property
    def heater_1_height(self):
        """field `Heater 1 Height`

        |  Units: m

        Args:
            value (float): value for IDD Field `Heater 1 Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_1_height` or None if not set

        """
        return self["Heater 1 Height"]

    @heater_1_height.setter
    def heater_1_height(self, value=None):
        """Corresponds to IDD field `Heater 1 Height`"""
        self["Heater 1 Height"] = value

    @property
    def heater_2_setpoint_temperature_schedule_name(self):
        """field `Heater 2 Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Heater 2 Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heater_2_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Heater 2 Setpoint Temperature Schedule Name"]

    @heater_2_setpoint_temperature_schedule_name.setter
    def heater_2_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Heater 2 Setpoint Temperature Schedule
        Name`"""
        self["Heater 2 Setpoint Temperature Schedule Name"] = value

    @property
    def heater_2_deadband_temperature_difference(self):
        """field `Heater 2 Deadband Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Heater 2 Deadband Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_2_deadband_temperature_difference` or None if not set

        """
        return self["Heater 2 Deadband Temperature Difference"]

    @heater_2_deadband_temperature_difference.setter
    def heater_2_deadband_temperature_difference(self, value=None):
        """Corresponds to IDD field `Heater 2 Deadband Temperature
        Difference`"""
        self["Heater 2 Deadband Temperature Difference"] = value

    @property
    def heater_2_capacity(self):
        """field `Heater 2 Capacity`

        |  Units: W

        Args:
            value (float): value for IDD Field `Heater 2 Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_2_capacity` or None if not set

        """
        return self["Heater 2 Capacity"]

    @heater_2_capacity.setter
    def heater_2_capacity(self, value=None):
        """Corresponds to IDD field `Heater 2 Capacity`"""
        self["Heater 2 Capacity"] = value

    @property
    def heater_2_height(self):
        """field `Heater 2 Height`

        |  Units: m

        Args:
            value (float): value for IDD Field `Heater 2 Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_2_height` or None if not set

        """
        return self["Heater 2 Height"]

    @heater_2_height.setter
    def heater_2_height(self, value=None):
        """Corresponds to IDD field `Heater 2 Height`"""
        self["Heater 2 Height"] = value

    @property
    def heater_fuel_type(self):
        """field `Heater Fuel Type`

        Args:
            value (str): value for IDD Field `Heater Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heater_fuel_type` or None if not set

        """
        return self["Heater Fuel Type"]

    @heater_fuel_type.setter
    def heater_fuel_type(self, value=None):
        """Corresponds to IDD field `Heater Fuel Type`"""
        self["Heater Fuel Type"] = value

    @property
    def heater_thermal_efficiency(self):
        """field `Heater Thermal Efficiency`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Heater Thermal Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heater_thermal_efficiency` or None if not set

        """
        return self["Heater Thermal Efficiency"]

    @heater_thermal_efficiency.setter
    def heater_thermal_efficiency(self, value=None):
        """Corresponds to IDD field `Heater Thermal Efficiency`"""
        self["Heater Thermal Efficiency"] = value

    @property
    def off_cycle_parasitic_fuel_consumption_rate(self):
        """field `Off Cycle Parasitic Fuel Consumption Rate`

        |  Units: W

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Fuel Consumption Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_fuel_consumption_rate` or None if not set

        """
        return self["Off Cycle Parasitic Fuel Consumption Rate"]

    @off_cycle_parasitic_fuel_consumption_rate.setter
    def off_cycle_parasitic_fuel_consumption_rate(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Fuel Consumption
        Rate`"""
        self["Off Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def off_cycle_parasitic_fuel_type(self):
        """field `Off Cycle Parasitic Fuel Type`

        Args:
            value (str): value for IDD Field `Off Cycle Parasitic Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `off_cycle_parasitic_fuel_type` or None if not set

        """
        return self["Off Cycle Parasitic Fuel Type"]

    @off_cycle_parasitic_fuel_type.setter
    def off_cycle_parasitic_fuel_type(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Fuel Type`"""
        self["Off Cycle Parasitic Fuel Type"] = value

    @property
    def off_cycle_parasitic_heat_fraction_to_tank(self):
        """field `Off Cycle Parasitic Heat Fraction to Tank`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Heat Fraction to Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_heat_fraction_to_tank` or None if not set

        """
        return self["Off Cycle Parasitic Heat Fraction to Tank"]

    @off_cycle_parasitic_heat_fraction_to_tank.setter
    def off_cycle_parasitic_heat_fraction_to_tank(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Heat Fraction to
        Tank`"""
        self["Off Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def off_cycle_parasitic_height(self):
        """field `Off Cycle Parasitic Height`

        |  Units: m

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_height` or None if not set

        """
        return self["Off Cycle Parasitic Height"]

    @off_cycle_parasitic_height.setter
    def off_cycle_parasitic_height(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Height`"""
        self["Off Cycle Parasitic Height"] = value

    @property
    def on_cycle_parasitic_fuel_consumption_rate(self):
        """field `On Cycle Parasitic Fuel Consumption Rate`

        |  Units: W

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Fuel Consumption Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_fuel_consumption_rate` or None if not set

        """
        return self["On Cycle Parasitic Fuel Consumption Rate"]

    @on_cycle_parasitic_fuel_consumption_rate.setter
    def on_cycle_parasitic_fuel_consumption_rate(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Fuel Consumption
        Rate`"""
        self["On Cycle Parasitic Fuel Consumption Rate"] = value

    @property
    def on_cycle_parasitic_fuel_type(self):
        """field `On Cycle Parasitic Fuel Type`

        Args:
            value (str): value for IDD Field `On Cycle Parasitic Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `on_cycle_parasitic_fuel_type` or None if not set

        """
        return self["On Cycle Parasitic Fuel Type"]

    @on_cycle_parasitic_fuel_type.setter
    def on_cycle_parasitic_fuel_type(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Fuel Type`"""
        self["On Cycle Parasitic Fuel Type"] = value

    @property
    def on_cycle_parasitic_heat_fraction_to_tank(self):
        """field `On Cycle Parasitic Heat Fraction to Tank`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Heat Fraction to Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_heat_fraction_to_tank` or None if not set

        """
        return self["On Cycle Parasitic Heat Fraction to Tank"]

    @on_cycle_parasitic_heat_fraction_to_tank.setter
    def on_cycle_parasitic_heat_fraction_to_tank(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Heat Fraction to
        Tank`"""
        self["On Cycle Parasitic Heat Fraction to Tank"] = value

    @property
    def on_cycle_parasitic_height(self):
        """field `On Cycle Parasitic Height`

        |  Units: m

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_height` or None if not set

        """
        return self["On Cycle Parasitic Height"]

    @on_cycle_parasitic_height.setter
    def on_cycle_parasitic_height(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Height`"""
        self["On Cycle Parasitic Height"] = value

    @property
    def ambient_temperature_indicator(self):
        """field `Ambient Temperature Indicator`

        Args:
            value (str): value for IDD Field `Ambient Temperature Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set

        """
        return self["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Indicator`"""
        self["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set

        """
        return self["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Schedule Name`"""
        self["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """field `Ambient Temperature Zone Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set

        """
        return self["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Zone Name`"""
        self["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """field `Ambient Temperature Outdoor Air Node Name`

        |  required for Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `Ambient Temperature Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set

        """
        return self["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Outdoor Air Node
        Name`"""
        self["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(
            self):
        """field `Uniform Skin Loss Coefficient per Unit Area to Ambient
        Temperature`

        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature` or None if not set

        """
        return self[
            "Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"]

    @uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature.setter
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Uniform Skin Loss Coefficient per Unit
        Area to Ambient Temperature`"""
        self[
            "Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = value

    @property
    def skin_loss_fraction_to_zone(self):
        """field `Skin Loss Fraction to Zone`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Skin Loss Fraction to Zone`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `skin_loss_fraction_to_zone` or None if not set

        """
        return self["Skin Loss Fraction to Zone"]

    @skin_loss_fraction_to_zone.setter
    def skin_loss_fraction_to_zone(self, value=1.0):
        """Corresponds to IDD field `Skin Loss Fraction to Zone`"""
        self["Skin Loss Fraction to Zone"] = value

    @property
    def off_cycle_flue_loss_coefficient_to_ambient_temperature(self):
        """field `Off Cycle Flue Loss Coefficient to Ambient Temperature`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Off Cycle Flue Loss Coefficient to Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_flue_loss_coefficient_to_ambient_temperature` or None if not set

        """
        return self["Off Cycle Flue Loss Coefficient to Ambient Temperature"]

    @off_cycle_flue_loss_coefficient_to_ambient_temperature.setter
    def off_cycle_flue_loss_coefficient_to_ambient_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Off Cycle Flue Loss Coefficient to Ambient
        Temperature`"""
        self["Off Cycle Flue Loss Coefficient to Ambient Temperature"] = value

    @property
    def off_cycle_flue_loss_fraction_to_zone(self):
        """field `Off Cycle Flue Loss Fraction to Zone`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Off Cycle Flue Loss Fraction to Zone`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_flue_loss_fraction_to_zone` or None if not set

        """
        return self["Off Cycle Flue Loss Fraction to Zone"]

    @off_cycle_flue_loss_fraction_to_zone.setter
    def off_cycle_flue_loss_fraction_to_zone(self, value=1.0):
        """Corresponds to IDD field `Off Cycle Flue Loss Fraction to Zone`"""
        self["Off Cycle Flue Loss Fraction to Zone"] = value

    @property
    def peak_use_flow_rate(self):
        """field `Peak Use Flow Rate`

        |  Only used if Use Side Node connections are blank
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Peak Use Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `peak_use_flow_rate` or None if not set

        """
        return self["Peak Use Flow Rate"]

    @peak_use_flow_rate.setter
    def peak_use_flow_rate(self, value=None):
        """Corresponds to IDD field `Peak Use Flow Rate`"""
        self["Peak Use Flow Rate"] = value

    @property
    def use_flow_rate_fraction_schedule_name(self):
        """field `Use Flow Rate Fraction Schedule Name`

        |  If blank, defaults to 1.0 at all times
        |  Only used if use side node connections are blank

        Args:
            value (str): value for IDD Field `Use Flow Rate Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_flow_rate_fraction_schedule_name` or None if not set

        """
        return self["Use Flow Rate Fraction Schedule Name"]

    @use_flow_rate_fraction_schedule_name.setter
    def use_flow_rate_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Use Flow Rate Fraction Schedule Name`"""
        self["Use Flow Rate Fraction Schedule Name"] = value

    @property
    def cold_water_supply_temperature_schedule_name(self):
        """field `Cold Water Supply Temperature Schedule Name`

        |  Only used if use side node connections are blank
        |  Defaults to water temperatures calculated by Site:WaterMainsTemperature object

        Args:
            value (str): value for IDD Field `Cold Water Supply Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_water_supply_temperature_schedule_name` or None if not set

        """
        return self["Cold Water Supply Temperature Schedule Name"]

    @cold_water_supply_temperature_schedule_name.setter
    def cold_water_supply_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Cold Water Supply Temperature Schedule
        Name`"""
        self["Cold Water Supply Temperature Schedule Name"] = value

    @property
    def use_side_inlet_node_name(self):
        """field `Use Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set

        """
        return self["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Inlet Node Name`"""
        self["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """field `Use Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set

        """
        return self["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Outlet Node Name`"""
        self["Use Side Outlet Node Name"] = value

    @property
    def use_side_effectiveness(self):
        """field `Use Side Effectiveness`

        |  The use side effectiveness in the stratified tank model is a simplified analogy of
        |  a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        |  use mass flow rate that directly mixes with the tank fluid. And one minus the
        |  effectiveness is the fraction that bypasses the tank. The use side mass flow rate
        |  that bypasses the tank is mixed with the fluid or water leaving the stratified tank.
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Use Side Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `use_side_effectiveness` or None if not set

        """
        return self["Use Side Effectiveness"]

    @use_side_effectiveness.setter
    def use_side_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Use Side Effectiveness`"""
        self["Use Side Effectiveness"] = value

    @property
    def use_side_inlet_height(self):
        """field `Use Side Inlet Height`

        |  Defaults to bottom of tank
        |  Units: m

        Args:
            value (float): value for IDD Field `Use Side Inlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `use_side_inlet_height` or None if not set

        """
        return self["Use Side Inlet Height"]

    @use_side_inlet_height.setter
    def use_side_inlet_height(self, value=None):
        """Corresponds to IDD field `Use Side Inlet Height`"""
        self["Use Side Inlet Height"] = value

    @property
    def use_side_outlet_height(self):
        """field `Use Side Outlet Height`

        |  Defaults to top of tank
        |  Units: m
        |  Default value: "Autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Use Side Outlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `use_side_outlet_height` or None if not set

        """
        return self["Use Side Outlet Height"]

    @use_side_outlet_height.setter
    def use_side_outlet_height(self, value="Autocalculate"):
        """Corresponds to IDD field `Use Side Outlet Height`"""
        self["Use Side Outlet Height"] = value

    @property
    def source_side_inlet_node_name(self):
        """field `Source Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set

        """
        return self["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Inlet Node Name`"""
        self["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """field `Source Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set

        """
        return self["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Outlet Node Name`"""
        self["Source Side Outlet Node Name"] = value

    @property
    def source_side_effectiveness(self):
        """field `Source Side Effectiveness`

        |  The source side effectiveness in the stratified tank model is a simplified analogy of
        |  a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        |  source mass flow rate that directly mixes with the tank fluid. And one minus the
        |  effectiveness is the fraction that bypasses the tank. The source side mass flow rate
        |  that bypasses the tank is mixed with the fluid or water leaving the stratified tank.
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Source Side Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_side_effectiveness` or None if not set

        """
        return self["Source Side Effectiveness"]

    @source_side_effectiveness.setter
    def source_side_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Source Side Effectiveness`"""
        self["Source Side Effectiveness"] = value

    @property
    def source_side_inlet_height(self):
        """field `Source Side Inlet Height`

        |  Defaults to top of tank
        |  Units: m
        |  Default value: "Autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Source Side Inlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `source_side_inlet_height` or None if not set

        """
        return self["Source Side Inlet Height"]

    @source_side_inlet_height.setter
    def source_side_inlet_height(self, value="Autocalculate"):
        """Corresponds to IDD field `Source Side Inlet Height`"""
        self["Source Side Inlet Height"] = value

    @property
    def source_side_outlet_height(self):
        """field `Source Side Outlet Height`

        |  Defaults to bottom of tank
        |  Units: m

        Args:
            value (float): value for IDD Field `Source Side Outlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_side_outlet_height` or None if not set

        """
        return self["Source Side Outlet Height"]

    @source_side_outlet_height.setter
    def source_side_outlet_height(self, value=None):
        """Corresponds to IDD field `Source Side Outlet Height`"""
        self["Source Side Outlet Height"] = value

    @property
    def inlet_mode(self):
        """field `Inlet Mode`

        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Inlet Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_mode` or None if not set

        """
        return self["Inlet Mode"]

    @inlet_mode.setter
    def inlet_mode(self, value="Fixed"):
        """Corresponds to IDD field `Inlet Mode`"""
        self["Inlet Mode"] = value

    @property
    def use_side_design_flow_rate(self):
        """field `Use Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Use Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `use_side_design_flow_rate` or None if not set

        """
        return self["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Use Side Design Flow Rate`"""
        self["Use Side Design Flow Rate"] = value

    @property
    def source_side_design_flow_rate(self):
        """field `Source Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Source Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `source_side_design_flow_rate` or None if not set

        """
        return self["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Source Side Design Flow Rate`"""
        self["Source Side Design Flow Rate"] = value

    @property
    def indirect_water_heating_recovery_time(self):
        """field `Indirect Water Heating Recovery Time`

        |  Parameter for autosizing design flow rates for indirectly heated water tanks
        |  time required to raise temperature of entire tank from 14.4C to 57.2C
        |  Units: hr
        |  Default value: 1.5

        Args:
            value (float): value for IDD Field `Indirect Water Heating Recovery Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `indirect_water_heating_recovery_time` or None if not set

        """
        return self["Indirect Water Heating Recovery Time"]

    @indirect_water_heating_recovery_time.setter
    def indirect_water_heating_recovery_time(self, value=1.5):
        """Corresponds to IDD field `Indirect Water Heating Recovery Time`"""
        self["Indirect Water Heating Recovery Time"] = value

    @property
    def number_of_nodes(self):
        """field `Number of Nodes`

        |  Default value: 1
        |  value >= 1
        |  value <= 12

        Args:
            value (int): value for IDD Field `Number of Nodes`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_nodes` or None if not set

        """
        return self["Number of Nodes"]

    @number_of_nodes.setter
    def number_of_nodes(self, value=1):
        """Corresponds to IDD field `Number of Nodes`"""
        self["Number of Nodes"] = value

    @property
    def additional_destratification_conductivity(self):
        """field `Additional Destratification Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Additional Destratification Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `additional_destratification_conductivity` or None if not set

        """
        return self["Additional Destratification Conductivity"]

    @additional_destratification_conductivity.setter
    def additional_destratification_conductivity(self, value=None):
        """Corresponds to IDD field `Additional Destratification
        Conductivity`"""
        self["Additional Destratification Conductivity"] = value

    @property
    def node_1_additional_loss_coefficient(self):
        """field `Node 1 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 1 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_1_additional_loss_coefficient` or None if not set

        """
        return self["Node 1 Additional Loss Coefficient"]

    @node_1_additional_loss_coefficient.setter
    def node_1_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 1 Additional Loss Coefficient`"""
        self["Node 1 Additional Loss Coefficient"] = value

    @property
    def node_2_additional_loss_coefficient(self):
        """field `Node 2 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 2 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_2_additional_loss_coefficient` or None if not set

        """
        return self["Node 2 Additional Loss Coefficient"]

    @node_2_additional_loss_coefficient.setter
    def node_2_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 2 Additional Loss Coefficient`"""
        self["Node 2 Additional Loss Coefficient"] = value

    @property
    def node_3_additional_loss_coefficient(self):
        """field `Node 3 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 3 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_3_additional_loss_coefficient` or None if not set

        """
        return self["Node 3 Additional Loss Coefficient"]

    @node_3_additional_loss_coefficient.setter
    def node_3_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 3 Additional Loss Coefficient`"""
        self["Node 3 Additional Loss Coefficient"] = value

    @property
    def node_4_additional_loss_coefficient(self):
        """field `Node 4 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 4 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_4_additional_loss_coefficient` or None if not set

        """
        return self["Node 4 Additional Loss Coefficient"]

    @node_4_additional_loss_coefficient.setter
    def node_4_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 4 Additional Loss Coefficient`"""
        self["Node 4 Additional Loss Coefficient"] = value

    @property
    def node_5_additional_loss_coefficient(self):
        """field `Node 5 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 5 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_5_additional_loss_coefficient` or None if not set

        """
        return self["Node 5 Additional Loss Coefficient"]

    @node_5_additional_loss_coefficient.setter
    def node_5_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 5 Additional Loss Coefficient`"""
        self["Node 5 Additional Loss Coefficient"] = value

    @property
    def node_6_additional_loss_coefficient(self):
        """field `Node 6 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 6 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_6_additional_loss_coefficient` or None if not set

        """
        return self["Node 6 Additional Loss Coefficient"]

    @node_6_additional_loss_coefficient.setter
    def node_6_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 6 Additional Loss Coefficient`"""
        self["Node 6 Additional Loss Coefficient"] = value

    @property
    def node_7_additional_loss_coefficient(self):
        """field `Node 7 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 7 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_7_additional_loss_coefficient` or None if not set

        """
        return self["Node 7 Additional Loss Coefficient"]

    @node_7_additional_loss_coefficient.setter
    def node_7_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 7 Additional Loss Coefficient`"""
        self["Node 7 Additional Loss Coefficient"] = value

    @property
    def node_8_additional_loss_coefficient(self):
        """field `Node 8 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 8 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_8_additional_loss_coefficient` or None if not set

        """
        return self["Node 8 Additional Loss Coefficient"]

    @node_8_additional_loss_coefficient.setter
    def node_8_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 8 Additional Loss Coefficient`"""
        self["Node 8 Additional Loss Coefficient"] = value

    @property
    def node_9_additional_loss_coefficient(self):
        """field `Node 9 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 9 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_9_additional_loss_coefficient` or None if not set

        """
        return self["Node 9 Additional Loss Coefficient"]

    @node_9_additional_loss_coefficient.setter
    def node_9_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 9 Additional Loss Coefficient`"""
        self["Node 9 Additional Loss Coefficient"] = value

    @property
    def node_10_additional_loss_coefficient(self):
        """field `Node 10 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 10 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_10_additional_loss_coefficient` or None if not set

        """
        return self["Node 10 Additional Loss Coefficient"]

    @node_10_additional_loss_coefficient.setter
    def node_10_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 10 Additional Loss Coefficient`"""
        self["Node 10 Additional Loss Coefficient"] = value

    @property
    def node_11_additional_loss_coefficient(self):
        """field `Node 11 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 11 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_11_additional_loss_coefficient` or None if not set

        """
        return self["Node 11 Additional Loss Coefficient"]

    @node_11_additional_loss_coefficient.setter
    def node_11_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 11 Additional Loss Coefficient`"""
        self["Node 11 Additional Loss Coefficient"] = value

    @property
    def node_12_additional_loss_coefficient(self):
        """field `Node 12 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 12 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_12_additional_loss_coefficient` or None if not set

        """
        return self["Node 12 Additional Loss Coefficient"]

    @node_12_additional_loss_coefficient.setter
    def node_12_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 12 Additional Loss Coefficient`"""
        self["Node 12 Additional Loss Coefficient"] = value

    @property
    def source_side_flow_control_mode(self):
        """field `Source Side Flow Control Mode`

        |  StorageTank mode always requests flow unless tank is at its Maximum Temperature Limit
        |  IndirectHeatPrimarySetpoint mode requests flow whenever primary setpoint for heater 1 calls for heat
        |  IndirectHeatAlternateSetpoint mode requests flow whenever alternate indirect setpoint calls for heat
        |  Default value: IndirectHeatPrimarySetpoint

        Args:
            value (str): value for IDD Field `Source Side Flow Control Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_flow_control_mode` or None if not set

        """
        return self["Source Side Flow Control Mode"]

    @source_side_flow_control_mode.setter
    def source_side_flow_control_mode(
            self,
            value="IndirectHeatPrimarySetpoint"):
        """Corresponds to IDD field `Source Side Flow Control Mode`"""
        self["Source Side Flow Control Mode"] = value

    @property
    def indirect_alternate_setpoint_temperature_schedule_name(self):
        """field `Indirect Alternate Setpoint Temperature Schedule Name`

        |  This field is only used if the previous is set to IndirectHeatAlternateSetpoint

        Args:
            value (str): value for IDD Field `Indirect Alternate Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `indirect_alternate_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Indirect Alternate Setpoint Temperature Schedule Name"]

    @indirect_alternate_setpoint_temperature_schedule_name.setter
    def indirect_alternate_setpoint_temperature_schedule_name(
            self,
            value=None):
        """Corresponds to IDD field `Indirect Alternate Setpoint Temperature
        Schedule Name`"""
        self["Indirect Alternate Setpoint Temperature Schedule Name"] = value




class WaterHeaterSizing(DataObject):

    """ Corresponds to IDD object `WaterHeater:Sizing`
        This input object is used with WaterHeater:Mixed or
        with WaterHeater:Stratified to autosize tank volume and heater capacity
        This object is not needed if water heaters are not autosized.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'waterheater name',
                                       {'name': u'WaterHeater Name',
                                        'pyname': u'waterheater_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design mode',
                                       {'name': u'Design Mode',
                                        'pyname': u'design_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PeakDraw',
                                                            u'ResidentialHUD-FHAMinimum',
                                                            u'PerPerson',
                                                            u'PerFloorArea',
                                                            u'PerUnit',
                                                            u'PerSolarCollectorArea'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'time storage can meet peak draw',
                                       {'name': u'Time Storage Can Meet Peak Draw',
                                        'pyname': u'time_storage_can_meet_peak_draw',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'time for tank recovery',
                                       {'name': u'Time for Tank Recovery',
                                        'pyname': u'time_for_tank_recovery',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'nominal tank volume for autosizing plant connections',
                                       {'name': u'Nominal Tank Volume for Autosizing Plant Connections',
                                        'pyname': u'nominal_tank_volume_for_autosizing_plant_connections',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'number of bedrooms',
                                       {'name': u'Number of Bedrooms',
                                        'pyname': u'number_of_bedrooms',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'number of bathrooms',
                                       {'name': u'Number of Bathrooms',
                                        'pyname': u'number_of_bathrooms',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'storage capacity per person',
                                       {'name': u'Storage Capacity per Person',
                                        'pyname': u'storage_capacity_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/Person'}),
                                      (u'recovery capacity per person',
                                       {'name': u'Recovery Capacity per Person',
                                        'pyname': u'recovery_capacity_per_person',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/hr-person'}),
                                      (u'storage capacity per floor area',
                                       {'name': u'Storage Capacity per Floor Area',
                                        'pyname': u'storage_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/m2'}),
                                      (u'recovery capacity per floor area',
                                       {'name': u'Recovery Capacity per Floor Area',
                                        'pyname': u'recovery_capacity_per_floor_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/hr-m2'}),
                                      (u'number of units',
                                       {'name': u'Number of Units',
                                        'pyname': u'number_of_units',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'storage capacity per unit',
                                       {'name': u'Storage Capacity per Unit',
                                        'pyname': u'storage_capacity_per_unit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'recovery capacity perunit',
                                       {'name': u'Recovery Capacity PerUnit',
                                        'pyname': u'recovery_capacity_perunit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/hr'}),
                                      (u'storage capacity per collector area',
                                       {'name': u'Storage Capacity per Collector Area',
                                        'pyname': u'storage_capacity_per_collector_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/m2'}),
                                      (u'height aspect ratio',
                                       {'name': u'Height Aspect Ratio',
                                        'pyname': u'height_aspect_ratio',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 4,
               'name': u'WaterHeater:Sizing',
               'pyname': u'WaterHeaterSizing',
               'required-object': False,
               'unique-object': False}

    @property
    def waterheater_name(self):
        """field `WaterHeater Name`

        Args:
            value (str): value for IDD Field `WaterHeater Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `waterheater_name` or None if not set

        """
        return self["WaterHeater Name"]

    @waterheater_name.setter
    def waterheater_name(self, value=None):
        """Corresponds to IDD field `WaterHeater Name`"""
        self["WaterHeater Name"] = value

    @property
    def design_mode(self):
        """field `Design Mode`

        Args:
            value (str): value for IDD Field `Design Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_mode` or None if not set

        """
        return self["Design Mode"]

    @design_mode.setter
    def design_mode(self, value=None):
        """Corresponds to IDD field `Design Mode`"""
        self["Design Mode"] = value

    @property
    def time_storage_can_meet_peak_draw(self):
        """field `Time Storage Can Meet Peak Draw`

        |  Only used for Design Mode = PeakDraw
        |  Units: hr

        Args:
            value (float): value for IDD Field `Time Storage Can Meet Peak Draw`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `time_storage_can_meet_peak_draw` or None if not set

        """
        return self["Time Storage Can Meet Peak Draw"]

    @time_storage_can_meet_peak_draw.setter
    def time_storage_can_meet_peak_draw(self, value=None):
        """Corresponds to IDD field `Time Storage Can Meet Peak Draw`"""
        self["Time Storage Can Meet Peak Draw"] = value

    @property
    def time_for_tank_recovery(self):
        """field `Time for Tank Recovery`

        |  Only used for Design Mode = PeakDraw
        |  Units: hr

        Args:
            value (float): value for IDD Field `Time for Tank Recovery`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `time_for_tank_recovery` or None if not set

        """
        return self["Time for Tank Recovery"]

    @time_for_tank_recovery.setter
    def time_for_tank_recovery(self, value=None):
        """Corresponds to IDD field `Time for Tank Recovery`"""
        self["Time for Tank Recovery"] = value

    @property
    def nominal_tank_volume_for_autosizing_plant_connections(self):
        """field `Nominal Tank Volume for Autosizing Plant Connections`

        |  Only used if Design Mode = PeakDraw and the water heater also
        |  has autosized flow rates for connections on the demand side of a plant loop
        |  Units: m3

        Args:
            value (float): value for IDD Field `Nominal Tank Volume for Autosizing Plant Connections`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_tank_volume_for_autosizing_plant_connections` or None if not set

        """
        return self["Nominal Tank Volume for Autosizing Plant Connections"]

    @nominal_tank_volume_for_autosizing_plant_connections.setter
    def nominal_tank_volume_for_autosizing_plant_connections(self, value=None):
        """Corresponds to IDD field `Nominal Tank Volume for Autosizing Plant
        Connections`"""
        self["Nominal Tank Volume for Autosizing Plant Connections"] = value

    @property
    def number_of_bedrooms(self):
        """field `Number of Bedrooms`

        |  Only used for Design Mode = ResidentialHUD-FHAMinimum
        |  value >= 1

        Args:
            value (int): value for IDD Field `Number of Bedrooms`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_bedrooms` or None if not set

        """
        return self["Number of Bedrooms"]

    @number_of_bedrooms.setter
    def number_of_bedrooms(self, value=None):
        """Corresponds to IDD field `Number of Bedrooms`"""
        self["Number of Bedrooms"] = value

    @property
    def number_of_bathrooms(self):
        """field `Number of Bathrooms`

        |  Only used for Design Mode = ResidentialHUD-FHAMinimum
        |  value >= 1

        Args:
            value (int): value for IDD Field `Number of Bathrooms`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_bathrooms` or None if not set

        """
        return self["Number of Bathrooms"]

    @number_of_bathrooms.setter
    def number_of_bathrooms(self, value=None):
        """Corresponds to IDD field `Number of Bathrooms`"""
        self["Number of Bathrooms"] = value

    @property
    def storage_capacity_per_person(self):
        """field `Storage Capacity per Person`

        |  Only used for Design Mode = PerPerson
        |  Units: m3/Person

        Args:
            value (float): value for IDD Field `Storage Capacity per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `storage_capacity_per_person` or None if not set

        """
        return self["Storage Capacity per Person"]

    @storage_capacity_per_person.setter
    def storage_capacity_per_person(self, value=None):
        """Corresponds to IDD field `Storage Capacity per Person`"""
        self["Storage Capacity per Person"] = value

    @property
    def recovery_capacity_per_person(self):
        """field `Recovery Capacity per Person`

        |  Only used for Design Mode = PerPerson
        |  Units: m3/hr-person

        Args:
            value (float): value for IDD Field `Recovery Capacity per Person`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recovery_capacity_per_person` or None if not set

        """
        return self["Recovery Capacity per Person"]

    @recovery_capacity_per_person.setter
    def recovery_capacity_per_person(self, value=None):
        """Corresponds to IDD field `Recovery Capacity per Person`"""
        self["Recovery Capacity per Person"] = value

    @property
    def storage_capacity_per_floor_area(self):
        """field `Storage Capacity per Floor Area`

        |  Only used for Design Mode = PerFloorArea
        |  Units: m3/m2

        Args:
            value (float): value for IDD Field `Storage Capacity per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `storage_capacity_per_floor_area` or None if not set

        """
        return self["Storage Capacity per Floor Area"]

    @storage_capacity_per_floor_area.setter
    def storage_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Storage Capacity per Floor Area`"""
        self["Storage Capacity per Floor Area"] = value

    @property
    def recovery_capacity_per_floor_area(self):
        """field `Recovery Capacity per Floor Area`

        |  Only used for Design Mode = PerFloorArea
        |  Units: m3/hr-m2

        Args:
            value (float): value for IDD Field `Recovery Capacity per Floor Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recovery_capacity_per_floor_area` or None if not set

        """
        return self["Recovery Capacity per Floor Area"]

    @recovery_capacity_per_floor_area.setter
    def recovery_capacity_per_floor_area(self, value=None):
        """Corresponds to IDD field `Recovery Capacity per Floor Area`"""
        self["Recovery Capacity per Floor Area"] = value

    @property
    def number_of_units(self):
        """field `Number of Units`

        |  Only used for Design Mode = PerUnit

        Args:
            value (float): value for IDD Field `Number of Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `number_of_units` or None if not set

        """
        return self["Number of Units"]

    @number_of_units.setter
    def number_of_units(self, value=None):
        """Corresponds to IDD field `Number of Units`"""
        self["Number of Units"] = value

    @property
    def storage_capacity_per_unit(self):
        """field `Storage Capacity per Unit`

        |  Only used for Design Mode = PerUnit
        |  Units: m3

        Args:
            value (float): value for IDD Field `Storage Capacity per Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `storage_capacity_per_unit` or None if not set

        """
        return self["Storage Capacity per Unit"]

    @storage_capacity_per_unit.setter
    def storage_capacity_per_unit(self, value=None):
        """Corresponds to IDD field `Storage Capacity per Unit`"""
        self["Storage Capacity per Unit"] = value

    @property
    def recovery_capacity_perunit(self):
        """field `Recovery Capacity PerUnit`

        |  Only used for Design Mode = PerUnit
        |  Units: m3/hr

        Args:
            value (float): value for IDD Field `Recovery Capacity PerUnit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recovery_capacity_perunit` or None if not set

        """
        return self["Recovery Capacity PerUnit"]

    @recovery_capacity_perunit.setter
    def recovery_capacity_perunit(self, value=None):
        """Corresponds to IDD field `Recovery Capacity PerUnit`"""
        self["Recovery Capacity PerUnit"] = value

    @property
    def storage_capacity_per_collector_area(self):
        """field `Storage Capacity per Collector Area`

        |  Only used for Design Mode = PerSolarCollectorArea
        |  Units: m3/m2

        Args:
            value (float): value for IDD Field `Storage Capacity per Collector Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `storage_capacity_per_collector_area` or None if not set

        """
        return self["Storage Capacity per Collector Area"]

    @storage_capacity_per_collector_area.setter
    def storage_capacity_per_collector_area(self, value=None):
        """Corresponds to IDD field `Storage Capacity per Collector Area`"""
        self["Storage Capacity per Collector Area"] = value

    @property
    def height_aspect_ratio(self):
        """field `Height Aspect Ratio`

        |  only used if for WaterHeater:Stratified

        Args:
            value (float): value for IDD Field `Height Aspect Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `height_aspect_ratio` or None if not set

        """
        return self["Height Aspect Ratio"]

    @height_aspect_ratio.setter
    def height_aspect_ratio(self, value=None):
        """Corresponds to IDD field `Height Aspect Ratio`"""
        self["Height Aspect Ratio"] = value




class WaterHeaterHeatPumpPumpedCondenser(DataObject):

    """ Corresponds to IDD object `WaterHeater:HeatPump:PumpedCondenser`
        This object models an air-source heat pump for water heating where the water is pumped out of the tank,
        through a heating coil and returned to the tank.
        For wrapped condenser HPWHs, see WaterHeater:HeatPump:WrappedCondenser.
        WaterHeater:HeatPump:PumpedCondenser is a compound object that references other component objects -
        Coil:WaterHeating:AirToWaterHeatPump:*, Fan:OnOff, WaterHeater:Mixed or WaterHeater:Stratified
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
                                      (u'compressor setpoint temperature schedule name',
                                       {'name': u'Compressor Setpoint Temperature Schedule Name',
                                        'pyname': u'compressor_setpoint_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dead band temperature difference',
                                       {'name': u'Dead Band Temperature Difference',
                                        'pyname': u'dead_band_temperature_difference',
                                        'default': 5.0,
                                        'minimum>': 0.0,
                                        'maximum': 20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'condenser water inlet node name',
                                       {'name': u'Condenser Water Inlet Node Name',
                                        'pyname': u'condenser_water_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'condenser water outlet node name',
                                       {'name': u'Condenser Water Outlet Node Name',
                                        'pyname': u'condenser_water_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'condenser water flow rate',
                                       {'name': u'Condenser Water Flow Rate',
                                        'pyname': u'condenser_water_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'evaporator air flow rate',
                                       {'name': u'Evaporator Air Flow Rate',
                                        'pyname': u'evaporator_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'inlet air configuration',
                                       {'name': u'Inlet Air Configuration',
                                        'pyname': u'inlet_air_configuration',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'ZoneAirOnly',
                                                            u'OutdoorAirOnly',
                                                            u'ZoneAndOutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air node name',
                                       {'name': u'Outdoor Air Node Name',
                                        'pyname': u'outdoor_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'exhaust air node name',
                                       {'name': u'Exhaust Air Node Name',
                                        'pyname': u'exhaust_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'inlet air temperature schedule name',
                                       {'name': u'Inlet Air Temperature Schedule Name',
                                        'pyname': u'inlet_air_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet air humidity schedule name',
                                       {'name': u'Inlet Air Humidity Schedule Name',
                                        'pyname': u'inlet_air_humidity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet air zone name',
                                       {'name': u'Inlet Air Zone Name',
                                        'pyname': u'inlet_air_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank object type',
                                       {'name': u'Tank Object Type',
                                        'pyname': u'tank_object_type',
                                        'default': u'WaterHeater:Mixed',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'WaterHeater:Mixed',
                                                            u'WaterHeater:Stratified'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'tank name',
                                       {'name': u'Tank Name',
                                        'pyname': u'tank_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank use side inlet node name',
                                       {'name': u'Tank Use Side Inlet Node Name',
                                        'pyname': u'tank_use_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'tank use side outlet node name',
                                       {'name': u'Tank Use Side Outlet Node Name',
                                        'pyname': u'tank_use_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'dx coil object type',
                                       {'name': u'DX Coil Object Type',
                                        'pyname': u'dx_coil_object_type',
                                        'default': u'Coil:WaterHeating:AirToWaterHeatPump:Pumped',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:WaterHeating:AirToWaterHeatPump:Pumped',
                                                            u'Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dx coil name',
                                       {'name': u'DX Coil Name',
                                        'pyname': u'dx_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum inlet air temperature for compressor operation',
                                       {'name': u'Minimum Inlet Air Temperature for Compressor Operation',
                                        'pyname': u'minimum_inlet_air_temperature_for_compressor_operation',
                                        'default': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -5.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum inlet air temperature for compressor operation',
                                       {'name': u'Maximum Inlet Air Temperature for Compressor Operation',
                                        'pyname': u'maximum_inlet_air_temperature_for_compressor_operation',
                                        'default': 48.88888888889,
                                        'maximum': 94.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 26.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'compressor location',
                                       {'name': u'Compressor Location',
                                        'pyname': u'compressor_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'compressor ambient temperature schedule name',
                                       {'name': u'Compressor Ambient Temperature Schedule Name',
                                        'pyname': u'compressor_ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan object type',
                                       {'name': u'Fan Object Type',
                                        'pyname': u'fan_object_type',
                                        'default': u'Fan:OnOff',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fan name',
                                       {'name': u'Fan Name',
                                        'pyname': u'fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'default': u'DrawThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'on cycle parasitic electric load',
                                       {'name': u'On Cycle Parasitic Electric Load',
                                        'pyname': u'on_cycle_parasitic_electric_load',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'off cycle parasitic electric load',
                                       {'name': u'Off Cycle Parasitic Electric Load',
                                        'pyname': u'off_cycle_parasitic_electric_load',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'parasitic heat rejection location',
                                       {'name': u'Parasitic Heat Rejection Location',
                                        'pyname': u'parasitic_heat_rejection_location',
                                        'default': u'Outdoors',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'inlet air mixer node name',
                                       {'name': u'Inlet Air Mixer Node Name',
                                        'pyname': u'inlet_air_mixer_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet air splitter node name',
                                       {'name': u'Outlet Air Splitter Node Name',
                                        'pyname': u'outlet_air_splitter_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'inlet air mixer schedule name',
                                       {'name': u'Inlet Air Mixer Schedule Name',
                                        'pyname': u'inlet_air_mixer_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank element control logic',
                                       {'name': u'Tank Element Control Logic',
                                        'pyname': u'tank_element_control_logic',
                                        'default': u'Simultaneous',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MutuallyExlcusive',
                                                            u'Simultaneous'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control sensor 1 height in stratified tank',
                                       {'name': u'Control Sensor 1 Height In Stratified Tank',
                                        'pyname': u'control_sensor_1_height_in_stratified_tank',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'control sensor 1 weight',
                                       {'name': u'Control Sensor 1 Weight',
                                        'pyname': u'control_sensor_1_weight',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'control sensor 2 height in stratified tank',
                                       {'name': u'Control Sensor 2 Height In Stratified Tank',
                                        'pyname': u'control_sensor_2_height_in_stratified_tank',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 32,
               'name': u'WaterHeater:HeatPump:PumpedCondenser',
               'pyname': u'WaterHeaterHeatPumpPumpedCondenser',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Unique name for this instance of a heat pump water heater.

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
        |  Schedule values of 0 denote the heat pump compressor is off and the parasitic electric
        |  energy is also off.

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
    def compressor_setpoint_temperature_schedule_name(self):
        """field `Compressor Setpoint Temperature Schedule Name`

        |  Defines the cut-out temperature where the heat pump compressor turns off.
        |  The heat pump compressor setpoint temperature should always be greater
        |  than the water tank's heater (element or burner) setpoint temperature.

        Args:
            value (str): value for IDD Field `Compressor Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Compressor Setpoint Temperature Schedule Name"]

    @compressor_setpoint_temperature_schedule_name.setter
    def compressor_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Compressor Setpoint Temperature Schedule
        Name`"""
        self["Compressor Setpoint Temperature Schedule Name"] = value

    @property
    def dead_band_temperature_difference(self):
        """field `Dead Band Temperature Difference`

        |  Setpoint temperature minus the dead band temperature difference defines
        |  the cut-in temperature where the heat pump compressor turns on.
        |  The water tank's heater (element or burner) setpoint temperature
        |  should always be less than the heat pump compressor cut-in temperature.
        |  Units: deltaC
        |  Default value: 5.0
        |  value <= 20.0

        Args:
            value (float): value for IDD Field `Dead Band Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dead_band_temperature_difference` or None if not set

        """
        return self["Dead Band Temperature Difference"]

    @dead_band_temperature_difference.setter
    def dead_band_temperature_difference(self, value=5.0):
        """Corresponds to IDD field `Dead Band Temperature Difference`"""
        self["Dead Band Temperature Difference"] = value

    @property
    def condenser_water_inlet_node_name(self):
        """field `Condenser Water Inlet Node Name`

        |  Should match the field Source Outlet Node Name in the water heater tank object.
        |  Should also match the Condenser Water Inlet Node Name in the associated
        |  DX coil object.

        Args:
            value (str): value for IDD Field `Condenser Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_water_inlet_node_name` or None if not set

        """
        return self["Condenser Water Inlet Node Name"]

    @condenser_water_inlet_node_name.setter
    def condenser_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Water Inlet Node Name`"""
        self["Condenser Water Inlet Node Name"] = value

    @property
    def condenser_water_outlet_node_name(self):
        """field `Condenser Water Outlet Node Name`

        |  Should match the field Source Inlet Node Name in water heater tank object.
        |  Should also match the Condenser Water Outlet Node Name in the associated
        |  DX Coil object.

        Args:
            value (str): value for IDD Field `Condenser Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_water_outlet_node_name` or None if not set

        """
        return self["Condenser Water Outlet Node Name"]

    @condenser_water_outlet_node_name.setter
    def condenser_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Water Outlet Node Name`"""
        self["Condenser Water Outlet Node Name"] = value

    @property
    def condenser_water_flow_rate(self):
        """field `Condenser Water Flow Rate`

        |  Actual water flow rate through the heat pump's water coil (condenser).
        |  If autocalculated, the water flow rate is set equal to 4.487E-8 m3/s/W times
        |  the rated heating capacity of the heat pump's DX coil.
        |  Units: m3/s

        Args:
            value (float or "Autocalculate"): value for IDD Field `Condenser Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `condenser_water_flow_rate` or None if not set

        """
        return self["Condenser Water Flow Rate"]

    @condenser_water_flow_rate.setter
    def condenser_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Condenser Water Flow Rate`"""
        self["Condenser Water Flow Rate"] = value

    @property
    def evaporator_air_flow_rate(self):
        """field `Evaporator Air Flow Rate`

        |  Actual air flow rate across the heat pump's air coil (evaporator).
        |  If autocalculated, the air flow rate is set equal to 5.035E-5 m3/s/W times
        |  the rated heating capacity of the heat pump's DX coil.
        |  Units: m3/s

        Args:
            value (float or "Autocalculate"): value for IDD Field `Evaporator Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `evaporator_air_flow_rate` or None if not set

        """
        return self["Evaporator Air Flow Rate"]

    @evaporator_air_flow_rate.setter
    def evaporator_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Evaporator Air Flow Rate`"""
        self["Evaporator Air Flow Rate"] = value

    @property
    def inlet_air_configuration(self):
        """field `Inlet Air Configuration`

        |  Defines the configuration of the airflow path through the air coil and fan section.

        Args:
            value (str): value for IDD Field `Inlet Air Configuration`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_configuration` or None if not set

        """
        return self["Inlet Air Configuration"]

    @inlet_air_configuration.setter
    def inlet_air_configuration(self, value=None):
        """Corresponds to IDD field `Inlet Air Configuration`"""
        self["Inlet Air Configuration"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  Zone air exhaust node name if Inlet Air Configuration is ZoneAirOnly or
        |  ZoneAndOutdoorAir.
        |  Simply a unique Node Name if Inlet Air Configuration is Schedule.
        |  Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`"""
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  Zone Air Inlet Node Name if Inlet Air Configuration is ZoneAirOnly or
        |  ZoneAndOutdoorAir.
        |  Simply a unique Node Name if Inlet Air Configuration is Schedule.
        |  Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`"""
        self["Air Outlet Node Name"] = value

    @property
    def outdoor_air_node_name(self):
        """field `Outdoor Air Node Name`

        |  Outdoor air node name if inlet air configuration is ZoneAndOutdoorAir
        |  or OutdoorAirOnly, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set

        """
        return self["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Node Name`"""
        self["Outdoor Air Node Name"] = value

    @property
    def exhaust_air_node_name(self):
        """field `Exhaust Air Node Name`

        |  Simply a unique Node Name if Inlet Air Configuration is ZoneAndOutdoorAir
        |  or OutdoorAirOnly, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `Exhaust Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_node_name` or None if not set

        """
        return self["Exhaust Air Node Name"]

    @exhaust_air_node_name.setter
    def exhaust_air_node_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Node Name`"""
        self["Exhaust Air Node Name"] = value

    @property
    def inlet_air_temperature_schedule_name(self):
        """field `Inlet Air Temperature Schedule Name`

        |  Used only if Inlet Air Configuration is Schedule, otherwise leave blank.
        |  Schedule values should be degrees C.

        Args:
            value (str): value for IDD Field `Inlet Air Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_temperature_schedule_name` or None if not set

        """
        return self["Inlet Air Temperature Schedule Name"]

    @inlet_air_temperature_schedule_name.setter
    def inlet_air_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Temperature Schedule Name`"""
        self["Inlet Air Temperature Schedule Name"] = value

    @property
    def inlet_air_humidity_schedule_name(self):
        """field `Inlet Air Humidity Schedule Name`

        |  Used only if Inlet Air Configuration is Schedule, otherwise leave blank.
        |  Schedule values are entered as a fraction (e.g. 0.5 is equal to 50%RH)

        Args:
            value (str): value for IDD Field `Inlet Air Humidity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_humidity_schedule_name` or None if not set

        """
        return self["Inlet Air Humidity Schedule Name"]

    @inlet_air_humidity_schedule_name.setter
    def inlet_air_humidity_schedule_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Humidity Schedule Name`"""
        self["Inlet Air Humidity Schedule Name"] = value

    @property
    def inlet_air_zone_name(self):
        """field `Inlet Air Zone Name`

        |  Used only if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir.
        |  Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `Inlet Air Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_zone_name` or None if not set

        """
        return self["Inlet Air Zone Name"]

    @inlet_air_zone_name.setter
    def inlet_air_zone_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Zone Name`"""
        self["Inlet Air Zone Name"] = value

    @property
    def tank_object_type(self):
        """field `Tank Object Type`

        |  Specify the type of water heater tank used by this heat pump water heater.
        |  Default value: WaterHeater:Mixed

        Args:
            value (str): value for IDD Field `Tank Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_object_type` or None if not set

        """
        return self["Tank Object Type"]

    @tank_object_type.setter
    def tank_object_type(self, value="WaterHeater:Mixed"):
        """Corresponds to IDD field `Tank Object Type`"""
        self["Tank Object Type"] = value

    @property
    def tank_name(self):
        """field `Tank Name`

        |  Needs to match the name used in the corresponding Water Heater object.

        Args:
            value (str): value for IDD Field `Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_name` or None if not set

        """
        return self["Tank Name"]

    @tank_name.setter
    def tank_name(self, value=None):
        """Corresponds to IDD field `Tank Name`"""
        self["Tank Name"] = value

    @property
    def tank_use_side_inlet_node_name(self):
        """field `Tank Use Side Inlet Node Name`

        |  Used only when the heat pump water heater is connected to a plant loop,
        |  otherwise leave blank. Needs to match the name used in the corresponding
        |  Water Heater object when connected to a plant loop.

        Args:
            value (str): value for IDD Field `Tank Use Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_use_side_inlet_node_name` or None if not set

        """
        return self["Tank Use Side Inlet Node Name"]

    @tank_use_side_inlet_node_name.setter
    def tank_use_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Tank Use Side Inlet Node Name`"""
        self["Tank Use Side Inlet Node Name"] = value

    @property
    def tank_use_side_outlet_node_name(self):
        """field `Tank Use Side Outlet Node Name`

        |  Used only when the heat pump water heater is connected to a plant loop,
        |  otherwise leave blank. Needs to match the name used in the corresponding
        |  Water Heater object when connected to a plant loop.

        Args:
            value (str): value for IDD Field `Tank Use Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_use_side_outlet_node_name` or None if not set

        """
        return self["Tank Use Side Outlet Node Name"]

    @tank_use_side_outlet_node_name.setter
    def tank_use_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Tank Use Side Outlet Node Name`"""
        self["Tank Use Side Outlet Node Name"] = value

    @property
    def dx_coil_object_type(self):
        """field `DX Coil Object Type`

        |  Specify the type of DX coil used by this heat pump water heater. The only
        |  valid choice is Coil:WaterHeating:AirToWaterHeatPump:Pumped and Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed.
        |  Default value: Coil:WaterHeating:AirToWaterHeatPump:Pumped

        Args:
            value (str): value for IDD Field `DX Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dx_coil_object_type` or None if not set

        """
        return self["DX Coil Object Type"]

    @dx_coil_object_type.setter
    def dx_coil_object_type(
            self,
            value="Coil:WaterHeating:AirToWaterHeatPump:Pumped"):
        """Corresponds to IDD field `DX Coil Object Type`"""
        self["DX Coil Object Type"] = value

    @property
    def dx_coil_name(self):
        """field `DX Coil Name`

        |  Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:* object.

        Args:
            value (str): value for IDD Field `DX Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dx_coil_name` or None if not set

        """
        return self["DX Coil Name"]

    @dx_coil_name.setter
    def dx_coil_name(self, value=None):
        """Corresponds to IDD field `DX Coil Name`"""
        self["DX Coil Name"] = value

    @property
    def minimum_inlet_air_temperature_for_compressor_operation(self):
        """field `Minimum Inlet Air Temperature for Compressor Operation`

        |  Heat pump compressor will not operate when the inlet air dry-bulb temperature
        |  is below this value.
        |  Units: C
        |  Default value: 10.0
        |  value >= -5.0

        Args:
            value (float): value for IDD Field `Minimum Inlet Air Temperature for Compressor Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_inlet_air_temperature_for_compressor_operation` or None if not set

        """
        return self["Minimum Inlet Air Temperature for Compressor Operation"]

    @minimum_inlet_air_temperature_for_compressor_operation.setter
    def minimum_inlet_air_temperature_for_compressor_operation(
            self,
            value=10.0):
        """Corresponds to IDD field `Minimum Inlet Air Temperature for
        Compressor Operation`"""
        self["Minimum Inlet Air Temperature for Compressor Operation"] = value

    @property
    def maximum_inlet_air_temperature_for_compressor_operation(self):
        """field `Maximum Inlet Air Temperature for Compressor Operation`

        |  Heat pump compressor will not operate when the inlet air dry-bulb temperature
        |  is above this value.
        |  Units: C
        |  Default value: 48.8888888889
        |  value >= 26.0
        |  value <= 94.0

        Args:
            value (float): value for IDD Field `Maximum Inlet Air Temperature for Compressor Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_inlet_air_temperature_for_compressor_operation` or None if not set

        """
        return self["Maximum Inlet Air Temperature for Compressor Operation"]

    @maximum_inlet_air_temperature_for_compressor_operation.setter
    def maximum_inlet_air_temperature_for_compressor_operation(
            self,
            value=48.8888888889):
        """Corresponds to IDD field `Maximum Inlet Air Temperature for
        Compressor Operation`"""
        self["Maximum Inlet Air Temperature for Compressor Operation"] = value

    @property
    def compressor_location(self):
        """field `Compressor Location`

        |  If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or
        |  ZoneAndOutdoorAir. If Schedule is selected, then you must provide a
        |  Compressor Ambient Temperature Schedule Name below.

        Args:
            value (str): value for IDD Field `Compressor Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_location` or None if not set

        """
        return self["Compressor Location"]

    @compressor_location.setter
    def compressor_location(self, value=None):
        """Corresponds to IDD field `Compressor Location`"""
        self["Compressor Location"] = value

    @property
    def compressor_ambient_temperature_schedule_name(self):
        """field `Compressor Ambient Temperature Schedule Name`

        |  Used only if Compressor Location is Schedule, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `Compressor Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_ambient_temperature_schedule_name` or None if not set

        """
        return self["Compressor Ambient Temperature Schedule Name"]

    @compressor_ambient_temperature_schedule_name.setter
    def compressor_ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Compressor Ambient Temperature Schedule
        Name`"""
        self["Compressor Ambient Temperature Schedule Name"] = value

    @property
    def fan_object_type(self):
        """field `Fan Object Type`

        |  Specify the type of fan used by this heat pump water heater. The only
        |  valid choice is Fan:OnOff.
        |  Default value: Fan:OnOff

        Args:
            value (str): value for IDD Field `Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_object_type` or None if not set

        """
        return self["Fan Object Type"]

    @fan_object_type.setter
    def fan_object_type(self, value="Fan:OnOff"):
        """Corresponds to IDD field `Fan Object Type`"""
        self["Fan Object Type"] = value

    @property
    def fan_name(self):
        """field `Fan Name`

        |  Needs to match the name used in the corresponding Fan:OnOff object.

        Args:
            value (str): value for IDD Field `Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_name` or None if not set

        """
        return self["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """Corresponds to IDD field `Fan Name`"""
        self["Fan Name"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        |  BlowThrough means the fan is located before the air coil (upstream).
        |  DrawThrough means the fan is located after the air coil (downstream).
        |  Default value: DrawThrough

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def on_cycle_parasitic_electric_load(self):
        """field `On Cycle Parasitic Electric Load`

        |  Parasitic electric power consumed when the heat pump compressor operates.
        |  Does not contribute to water heating but can impact the zone air heat balance.
        |  Units: W

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Electric Load`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_electric_load` or None if not set

        """
        return self["On Cycle Parasitic Electric Load"]

    @on_cycle_parasitic_electric_load.setter
    def on_cycle_parasitic_electric_load(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Electric Load`"""
        self["On Cycle Parasitic Electric Load"] = value

    @property
    def off_cycle_parasitic_electric_load(self):
        """field `Off Cycle Parasitic Electric Load`

        |  Parasitic electric power consumed when the heat pump compressor is off.
        |  Does not contribute to water heating but can impact the zone air heat balance.
        |  Off-cycle parasitic power is 0 when the availability schedule is 0.
        |  Units: W

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Electric Load`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_electric_load` or None if not set

        """
        return self["Off Cycle Parasitic Electric Load"]

    @off_cycle_parasitic_electric_load.setter
    def off_cycle_parasitic_electric_load(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Electric Load`"""
        self["Off Cycle Parasitic Electric Load"] = value

    @property
    def parasitic_heat_rejection_location(self):
        """field `Parasitic Heat Rejection Location`

        |  This field determines if the parasitic electric load impacts the zone air
        |  heat balance. If Zone is selected, Inlet Air Configuration must be
        |  ZoneAirOnly or ZoneAndOutdoorAir.
        |  Default value: Outdoors

        Args:
            value (str): value for IDD Field `Parasitic Heat Rejection Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `parasitic_heat_rejection_location` or None if not set

        """
        return self["Parasitic Heat Rejection Location"]

    @parasitic_heat_rejection_location.setter
    def parasitic_heat_rejection_location(self, value="Outdoors"):
        """Corresponds to IDD field `Parasitic Heat Rejection Location`"""
        self["Parasitic Heat Rejection Location"] = value

    @property
    def inlet_air_mixer_node_name(self):
        """field `Inlet Air Mixer Node Name`

        |  Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        |  leave field blank.

        Args:
            value (str): value for IDD Field `Inlet Air Mixer Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_mixer_node_name` or None if not set

        """
        return self["Inlet Air Mixer Node Name"]

    @inlet_air_mixer_node_name.setter
    def inlet_air_mixer_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Mixer Node Name`"""
        self["Inlet Air Mixer Node Name"] = value

    @property
    def outlet_air_splitter_node_name(self):
        """field `Outlet Air Splitter Node Name`

        |  Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        |  leave field blank.

        Args:
            value (str): value for IDD Field `Outlet Air Splitter Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_air_splitter_node_name` or None if not set

        """
        return self["Outlet Air Splitter Node Name"]

    @outlet_air_splitter_node_name.setter
    def outlet_air_splitter_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Air Splitter Node Name`"""
        self["Outlet Air Splitter Node Name"] = value

    @property
    def inlet_air_mixer_schedule_name(self):
        """field `Inlet Air Mixer Schedule Name`

        |  Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        |  leave field blank. Schedule values define whether the heat pump draws its
        |  inlet air from the zone, outdoors or a combination of zone and outdoor air.
        |  A schedule value of 0 denotes inlet air is drawn only from the zone.
        |  A schedule value of 1 denotes inlet air is drawn only from outdoors.
        |  Schedule values between 0 and 1 denote a mixture of zone and outdoor air
        |  proportional to the schedule value (i.e. 0.4 = 40% outdoor air, 60% zone air).

        Args:
            value (str): value for IDD Field `Inlet Air Mixer Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_mixer_schedule_name` or None if not set

        """
        return self["Inlet Air Mixer Schedule Name"]

    @inlet_air_mixer_schedule_name.setter
    def inlet_air_mixer_schedule_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Mixer Schedule Name`"""
        self["Inlet Air Mixer Schedule Name"] = value

    @property
    def tank_element_control_logic(self):
        """field `Tank Element Control Logic`

        |  MutuallyExclusive means that once the tank heating element is active the
        |  heat pump is shut down until setpoint is reached.
        |  Simultaneous (default) means that both the tank heating element and
        |  heat pump are used at the same time recover the tank temperature.
        |  Default value: Simultaneous

        Args:
            value (str): value for IDD Field `Tank Element Control Logic`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_element_control_logic` or None if not set

        """
        return self["Tank Element Control Logic"]

    @tank_element_control_logic.setter
    def tank_element_control_logic(self, value="Simultaneous"):
        """Corresponds to IDD field `Tank Element Control Logic`"""
        self["Tank Element Control Logic"] = value

    @property
    def control_sensor_1_height_in_stratified_tank(self):
        """field `Control Sensor 1 Height In Stratified Tank`

        |  Used to indicate height of control sensor for Tank Object Type = WaterHeater:Stratified
        |  If left blank, it will default to the height of Heater1
        |  Units: m

        Args:
            value (float): value for IDD Field `Control Sensor 1 Height In Stratified Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `control_sensor_1_height_in_stratified_tank` or None if not set

        """
        return self["Control Sensor 1 Height In Stratified Tank"]

    @control_sensor_1_height_in_stratified_tank.setter
    def control_sensor_1_height_in_stratified_tank(self, value=None):
        """Corresponds to IDD field `Control Sensor 1 Height In Stratified
        Tank`"""
        self["Control Sensor 1 Height In Stratified Tank"] = value

    @property
    def control_sensor_1_weight(self):
        """field `Control Sensor 1 Weight`

        |  Weight to give Control Sensor 1 temperature
        |  The weight of Control Sensor 2 will be 1 - (wt. of control sensor 1)
        |  Units: dimensionless
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Control Sensor 1 Weight`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `control_sensor_1_weight` or None if not set

        """
        return self["Control Sensor 1 Weight"]

    @control_sensor_1_weight.setter
    def control_sensor_1_weight(self, value=1.0):
        """Corresponds to IDD field `Control Sensor 1 Weight`"""
        self["Control Sensor 1 Weight"] = value

    @property
    def control_sensor_2_height_in_stratified_tank(self):
        """field `Control Sensor 2 Height In Stratified Tank`

        |  Used to indicate height of control sensor for Tank Object Type = WaterHeater:Stratified
        |  If left blank, it will default to the height of Heater2
        |  Units: m

        Args:
            value (float): value for IDD Field `Control Sensor 2 Height In Stratified Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `control_sensor_2_height_in_stratified_tank` or None if not set

        """
        return self["Control Sensor 2 Height In Stratified Tank"]

    @control_sensor_2_height_in_stratified_tank.setter
    def control_sensor_2_height_in_stratified_tank(self, value=None):
        """Corresponds to IDD field `Control Sensor 2 Height In Stratified
        Tank`"""
        self["Control Sensor 2 Height In Stratified Tank"] = value




class WaterHeaterHeatPumpWrappedCondenser(DataObject):

    """ Corresponds to IDD object `WaterHeater:HeatPump:WrappedCondenser`
        This object models an air-source heat pump for water heating where the heating coil is wrapped around
        the tank, which is typical of residential HPWHs.
        For pumped condenser HPWHs, see WaterHeater:HeatPump:PumpedCondenser.
        WaterHeater:HeatPump:WrappedCondenser is a compound object that references other component objects -
        Coil:WaterHeating:AirToWaterHeatPump:Pumped, Fan:OnOff, WaterHeater:Mixed
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
                                      (u'compressor setpoint temperature schedule name',
                                       {'name': u'Compressor Setpoint Temperature Schedule Name',
                                        'pyname': u'compressor_setpoint_temperature_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dead band temperature difference',
                                       {'name': u'Dead Band Temperature Difference',
                                        'pyname': u'dead_band_temperature_difference',
                                        'default': 5.0,
                                        'minimum>': 0.0,
                                        'maximum': 20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'condenser bottom location',
                                       {'name': u'Condenser Bottom Location',
                                        'pyname': u'condenser_bottom_location',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'condenser top location',
                                       {'name': u'Condenser Top Location',
                                        'pyname': u'condenser_top_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'evaporator air flow rate',
                                       {'name': u'Evaporator Air Flow Rate',
                                        'pyname': u'evaporator_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'inlet air configuration',
                                       {'name': u'Inlet Air Configuration',
                                        'pyname': u'inlet_air_configuration',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'ZoneAirOnly',
                                                            u'OutdoorAirOnly',
                                                            u'ZoneAndOutdoorAir'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air node name',
                                       {'name': u'Outdoor Air Node Name',
                                        'pyname': u'outdoor_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'exhaust air node name',
                                       {'name': u'Exhaust Air Node Name',
                                        'pyname': u'exhaust_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'inlet air temperature schedule name',
                                       {'name': u'Inlet Air Temperature Schedule Name',
                                        'pyname': u'inlet_air_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet air humidity schedule name',
                                       {'name': u'Inlet Air Humidity Schedule Name',
                                        'pyname': u'inlet_air_humidity_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'inlet air zone name',
                                       {'name': u'Inlet Air Zone Name',
                                        'pyname': u'inlet_air_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank object type',
                                       {'name': u'Tank Object Type',
                                        'pyname': u'tank_object_type',
                                        'default': u'WaterHeater:Stratified',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'WaterHeater:Stratified'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'tank name',
                                       {'name': u'Tank Name',
                                        'pyname': u'tank_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank use side inlet node name',
                                       {'name': u'Tank Use Side Inlet Node Name',
                                        'pyname': u'tank_use_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'tank use side outlet node name',
                                       {'name': u'Tank Use Side Outlet Node Name',
                                        'pyname': u'tank_use_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'dx coil object type',
                                       {'name': u'DX Coil Object Type',
                                        'pyname': u'dx_coil_object_type',
                                        'default': u'Coil:WaterHeating:AirToWaterHeatPump:Wrapped',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:WaterHeating:AirToWaterHeatPump:Wrapped'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dx coil name',
                                       {'name': u'DX Coil Name',
                                        'pyname': u'dx_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum inlet air temperature for compressor operation',
                                       {'name': u'Minimum Inlet Air Temperature for Compressor Operation',
                                        'pyname': u'minimum_inlet_air_temperature_for_compressor_operation',
                                        'default': 10.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -5.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum inlet air temperature for compressor operation',
                                       {'name': u'Maximum Inlet Air Temperature for Compressor Operation',
                                        'pyname': u'maximum_inlet_air_temperature_for_compressor_operation',
                                        'default': 48.88888888889,
                                        'maximum': 94.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 26.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'compressor location',
                                       {'name': u'Compressor Location',
                                        'pyname': u'compressor_location',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'compressor ambient temperature schedule name',
                                       {'name': u'Compressor Ambient Temperature Schedule Name',
                                        'pyname': u'compressor_ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan object type',
                                       {'name': u'Fan Object Type',
                                        'pyname': u'fan_object_type',
                                        'default': u'Fan:OnOff',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:OnOff'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fan name',
                                       {'name': u'Fan Name',
                                        'pyname': u'fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan placement',
                                       {'name': u'Fan Placement',
                                        'pyname': u'fan_placement',
                                        'default': u'DrawThrough',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'BlowThrough',
                                                            u'DrawThrough'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'on cycle parasitic electric load',
                                       {'name': u'On Cycle Parasitic Electric Load',
                                        'pyname': u'on_cycle_parasitic_electric_load',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'off cycle parasitic electric load',
                                       {'name': u'Off Cycle Parasitic Electric Load',
                                        'pyname': u'off_cycle_parasitic_electric_load',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'parasitic heat rejection location',
                                       {'name': u'Parasitic Heat Rejection Location',
                                        'pyname': u'parasitic_heat_rejection_location',
                                        'default': u'Outdoors',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'inlet air mixer node name',
                                       {'name': u'Inlet Air Mixer Node Name',
                                        'pyname': u'inlet_air_mixer_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet air splitter node name',
                                       {'name': u'Outlet Air Splitter Node Name',
                                        'pyname': u'outlet_air_splitter_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'inlet air mixer schedule name',
                                       {'name': u'Inlet Air Mixer Schedule Name',
                                        'pyname': u'inlet_air_mixer_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'tank element control logic',
                                       {'name': u'Tank Element Control Logic',
                                        'pyname': u'tank_element_control_logic',
                                        'default': u'Simultaneous',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'MutuallyExlcusive',
                                                            u'Simultaneous'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control sensor 1 height in stratified tank',
                                       {'name': u'Control Sensor 1 Height In Stratified Tank',
                                        'pyname': u'control_sensor_1_height_in_stratified_tank',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'control sensor 1 weight',
                                       {'name': u'Control Sensor 1 Weight',
                                        'pyname': u'control_sensor_1_weight',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'control sensor 2 height in stratified tank',
                                       {'name': u'Control Sensor 2 Height In Stratified Tank',
                                        'pyname': u'control_sensor_2_height_in_stratified_tank',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 31,
               'name': u'WaterHeater:HeatPump:WrappedCondenser',
               'pyname': u'WaterHeaterHeatPumpWrappedCondenser',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  Unique name for this instance of a heat pump water heater.

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
        |  Schedule values of 0 denote the heat pump compressor is off and the parasitic electric
        |  energy is also off.

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
    def compressor_setpoint_temperature_schedule_name(self):
        """field `Compressor Setpoint Temperature Schedule Name`

        |  Defines the cut-out temperature where the heat pump compressor turns off.
        |  The heat pump compressor setpoint temperature should always be greater
        |  than the water tank's heater (element or burner) setpoint temperature.

        Args:
            value (str): value for IDD Field `Compressor Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_setpoint_temperature_schedule_name` or None if not set

        """
        return self["Compressor Setpoint Temperature Schedule Name"]

    @compressor_setpoint_temperature_schedule_name.setter
    def compressor_setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Compressor Setpoint Temperature Schedule
        Name`"""
        self["Compressor Setpoint Temperature Schedule Name"] = value

    @property
    def dead_band_temperature_difference(self):
        """field `Dead Band Temperature Difference`

        |  Setpoint temperature minus the dead band temperature difference defines
        |  the cut-in temperature where the heat pump compressor turns on.
        |  The water tank's heater (element or burner) setpoint temperature
        |  should always be less than the heat pump compressor cut-in temperature.
        |  Units: deltaC
        |  Default value: 5.0
        |  value <= 20.0

        Args:
            value (float): value for IDD Field `Dead Band Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dead_band_temperature_difference` or None if not set

        """
        return self["Dead Band Temperature Difference"]

    @dead_band_temperature_difference.setter
    def dead_band_temperature_difference(self, value=5.0):
        """Corresponds to IDD field `Dead Band Temperature Difference`"""
        self["Dead Band Temperature Difference"] = value

    @property
    def condenser_bottom_location(self):
        """field `Condenser Bottom Location`

        |  Distance from the bottom of the tank to the bottom of the wrapped condenser.
        |  Units: m

        Args:
            value (float): value for IDD Field `Condenser Bottom Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condenser_bottom_location` or None if not set

        """
        return self["Condenser Bottom Location"]

    @condenser_bottom_location.setter
    def condenser_bottom_location(self, value=None):
        """Corresponds to IDD field `Condenser Bottom Location`"""
        self["Condenser Bottom Location"] = value

    @property
    def condenser_top_location(self):
        """field `Condenser Top Location`

        |  Distance from the bottom of the tank to the top of the wrapped condenser.
        |  Units: m

        Args:
            value (float): value for IDD Field `Condenser Top Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `condenser_top_location` or None if not set

        """
        return self["Condenser Top Location"]

    @condenser_top_location.setter
    def condenser_top_location(self, value=None):
        """Corresponds to IDD field `Condenser Top Location`"""
        self["Condenser Top Location"] = value

    @property
    def evaporator_air_flow_rate(self):
        """field `Evaporator Air Flow Rate`

        |  Actual air flow rate across the heat pump's air coil (evaporator).
        |  If autocalculated, the air flow rate is set equal to 5.035E-5 m3/s/W times
        |  the rated heating capacity of the heat pump's DX coil.
        |  Units: m3/s

        Args:
            value (float or "Autocalculate"): value for IDD Field `Evaporator Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `evaporator_air_flow_rate` or None if not set

        """
        return self["Evaporator Air Flow Rate"]

    @evaporator_air_flow_rate.setter
    def evaporator_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Evaporator Air Flow Rate`"""
        self["Evaporator Air Flow Rate"] = value

    @property
    def inlet_air_configuration(self):
        """field `Inlet Air Configuration`

        |  Defines the configuration of the airflow path through the air coil and fan section.

        Args:
            value (str): value for IDD Field `Inlet Air Configuration`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_configuration` or None if not set

        """
        return self["Inlet Air Configuration"]

    @inlet_air_configuration.setter
    def inlet_air_configuration(self, value=None):
        """Corresponds to IDD field `Inlet Air Configuration`"""
        self["Inlet Air Configuration"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  Zone air exhaust node name if Inlet Air Configuration is ZoneAirOnly or
        |  ZoneAndOutdoorAir.
        |  Simply a unique Node Name if Inlet Air Configuration is Schedule.
        |  Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_inlet_node_name` or None if not set

        """
        return self["Air Inlet Node Name"]

    @air_inlet_node_name.setter
    def air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Inlet Node Name`"""
        self["Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  Zone Air Inlet Node Name if Inlet Air Configuration is ZoneAirOnly or
        |  ZoneAndOutdoorAir.
        |  Simply a unique Node Name if Inlet Air Configuration is Schedule.
        |  Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_outlet_node_name` or None if not set

        """
        return self["Air Outlet Node Name"]

    @air_outlet_node_name.setter
    def air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Outlet Node Name`"""
        self["Air Outlet Node Name"] = value

    @property
    def outdoor_air_node_name(self):
        """field `Outdoor Air Node Name`

        |  Outdoor air node name if inlet air configuration is ZoneAndOutdoorAir
        |  or OutdoorAirOnly, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_node_name` or None if not set

        """
        return self["Outdoor Air Node Name"]

    @outdoor_air_node_name.setter
    def outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Node Name`"""
        self["Outdoor Air Node Name"] = value

    @property
    def exhaust_air_node_name(self):
        """field `Exhaust Air Node Name`

        |  Simply a unique Node Name if Inlet Air Configuration is ZoneAndOutdoorAir
        |  or OutdoorAirOnly, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `Exhaust Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `exhaust_air_node_name` or None if not set

        """
        return self["Exhaust Air Node Name"]

    @exhaust_air_node_name.setter
    def exhaust_air_node_name(self, value=None):
        """Corresponds to IDD field `Exhaust Air Node Name`"""
        self["Exhaust Air Node Name"] = value

    @property
    def inlet_air_temperature_schedule_name(self):
        """field `Inlet Air Temperature Schedule Name`

        |  Used only if Inlet Air Configuration is Schedule, otherwise leave blank.
        |  Schedule values should be degrees C.

        Args:
            value (str): value for IDD Field `Inlet Air Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_temperature_schedule_name` or None if not set

        """
        return self["Inlet Air Temperature Schedule Name"]

    @inlet_air_temperature_schedule_name.setter
    def inlet_air_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Temperature Schedule Name`"""
        self["Inlet Air Temperature Schedule Name"] = value

    @property
    def inlet_air_humidity_schedule_name(self):
        """field `Inlet Air Humidity Schedule Name`

        |  Used only if Inlet Air Configuration is Schedule, otherwise leave blank.
        |  Schedule values are entered as a fraction (e.g. 0.5 is equal to 50%RH)

        Args:
            value (str): value for IDD Field `Inlet Air Humidity Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_humidity_schedule_name` or None if not set

        """
        return self["Inlet Air Humidity Schedule Name"]

    @inlet_air_humidity_schedule_name.setter
    def inlet_air_humidity_schedule_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Humidity Schedule Name`"""
        self["Inlet Air Humidity Schedule Name"] = value

    @property
    def inlet_air_zone_name(self):
        """field `Inlet Air Zone Name`

        |  Used only if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir.
        |  Otherwise, leave field blank.

        Args:
            value (str): value for IDD Field `Inlet Air Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_zone_name` or None if not set

        """
        return self["Inlet Air Zone Name"]

    @inlet_air_zone_name.setter
    def inlet_air_zone_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Zone Name`"""
        self["Inlet Air Zone Name"] = value

    @property
    def tank_object_type(self):
        """field `Tank Object Type`

        |  Specify the type of water heater tank used by this heat pump water heater.
        |  Default value: WaterHeater:Stratified

        Args:
            value (str): value for IDD Field `Tank Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_object_type` or None if not set

        """
        return self["Tank Object Type"]

    @tank_object_type.setter
    def tank_object_type(self, value="WaterHeater:Stratified"):
        """Corresponds to IDD field `Tank Object Type`"""
        self["Tank Object Type"] = value

    @property
    def tank_name(self):
        """field `Tank Name`

        |  Needs to match the name used in the corresponding Water Heater object.
        |  Must be a WaterHeater:Stratified tank.

        Args:
            value (str): value for IDD Field `Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_name` or None if not set

        """
        return self["Tank Name"]

    @tank_name.setter
    def tank_name(self, value=None):
        """Corresponds to IDD field `Tank Name`"""
        self["Tank Name"] = value

    @property
    def tank_use_side_inlet_node_name(self):
        """field `Tank Use Side Inlet Node Name`

        |  Used only when the heat pump water heater is connected to a plant loop,
        |  otherwise leave blank. Needs to match the name used in the corresponding
        |  Water Heater object when connected to a plant loop.

        Args:
            value (str): value for IDD Field `Tank Use Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_use_side_inlet_node_name` or None if not set

        """
        return self["Tank Use Side Inlet Node Name"]

    @tank_use_side_inlet_node_name.setter
    def tank_use_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Tank Use Side Inlet Node Name`"""
        self["Tank Use Side Inlet Node Name"] = value

    @property
    def tank_use_side_outlet_node_name(self):
        """field `Tank Use Side Outlet Node Name`

        |  Used only when the heat pump water heater is connected to a plant loop,
        |  otherwise leave blank. Needs to match the name used in the corresponding
        |  Water Heater object when connected to a plant loop.

        Args:
            value (str): value for IDD Field `Tank Use Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_use_side_outlet_node_name` or None if not set

        """
        return self["Tank Use Side Outlet Node Name"]

    @tank_use_side_outlet_node_name.setter
    def tank_use_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Tank Use Side Outlet Node Name`"""
        self["Tank Use Side Outlet Node Name"] = value

    @property
    def dx_coil_object_type(self):
        """field `DX Coil Object Type`

        |  Specify the type of DX coil used by this heat pump water heater. The only
        |  valid choice is Coil:WaterHeating:AirToWaterHeatPump:Wrapped
        |  Default value: Coil:WaterHeating:AirToWaterHeatPump:Wrapped

        Args:
            value (str): value for IDD Field `DX Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dx_coil_object_type` or None if not set

        """
        return self["DX Coil Object Type"]

    @dx_coil_object_type.setter
    def dx_coil_object_type(
            self,
            value="Coil:WaterHeating:AirToWaterHeatPump:Wrapped"):
        """Corresponds to IDD field `DX Coil Object Type`"""
        self["DX Coil Object Type"] = value

    @property
    def dx_coil_name(self):
        """field `DX Coil Name`

        |  Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:Wrapped object.

        Args:
            value (str): value for IDD Field `DX Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `dx_coil_name` or None if not set

        """
        return self["DX Coil Name"]

    @dx_coil_name.setter
    def dx_coil_name(self, value=None):
        """Corresponds to IDD field `DX Coil Name`"""
        self["DX Coil Name"] = value

    @property
    def minimum_inlet_air_temperature_for_compressor_operation(self):
        """field `Minimum Inlet Air Temperature for Compressor Operation`

        |  Heat pump compressor will not operate when the inlet air dry-bulb temperature
        |  is below this value.
        |  Units: C
        |  Default value: 10.0
        |  value >= -5.0

        Args:
            value (float): value for IDD Field `Minimum Inlet Air Temperature for Compressor Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_inlet_air_temperature_for_compressor_operation` or None if not set

        """
        return self["Minimum Inlet Air Temperature for Compressor Operation"]

    @minimum_inlet_air_temperature_for_compressor_operation.setter
    def minimum_inlet_air_temperature_for_compressor_operation(
            self,
            value=10.0):
        """Corresponds to IDD field `Minimum Inlet Air Temperature for
        Compressor Operation`"""
        self["Minimum Inlet Air Temperature for Compressor Operation"] = value

    @property
    def maximum_inlet_air_temperature_for_compressor_operation(self):
        """field `Maximum Inlet Air Temperature for Compressor Operation`

        |  Heat pump compressor will not operate when the inlet air dry-bulb temperature
        |  is above this value.
        |  Units: C
        |  Default value: 48.8888888889
        |  value >= 26.0
        |  value <= 94.0

        Args:
            value (float): value for IDD Field `Maximum Inlet Air Temperature for Compressor Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_inlet_air_temperature_for_compressor_operation` or None if not set

        """
        return self["Maximum Inlet Air Temperature for Compressor Operation"]

    @maximum_inlet_air_temperature_for_compressor_operation.setter
    def maximum_inlet_air_temperature_for_compressor_operation(
            self,
            value=48.8888888889):
        """Corresponds to IDD field `Maximum Inlet Air Temperature for
        Compressor Operation`"""
        self["Maximum Inlet Air Temperature for Compressor Operation"] = value

    @property
    def compressor_location(self):
        """field `Compressor Location`

        |  If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or
        |  ZoneAndOutdoorAir. If Schedule is selected, then you must provide a
        |  Compressor Ambient Temperature Schedule Name below.

        Args:
            value (str): value for IDD Field `Compressor Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_location` or None if not set

        """
        return self["Compressor Location"]

    @compressor_location.setter
    def compressor_location(self, value=None):
        """Corresponds to IDD field `Compressor Location`"""
        self["Compressor Location"] = value

    @property
    def compressor_ambient_temperature_schedule_name(self):
        """field `Compressor Ambient Temperature Schedule Name`

        |  Used only if Compressor Location is Schedule, otherwise leave field blank.

        Args:
            value (str): value for IDD Field `Compressor Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `compressor_ambient_temperature_schedule_name` or None if not set

        """
        return self["Compressor Ambient Temperature Schedule Name"]

    @compressor_ambient_temperature_schedule_name.setter
    def compressor_ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Compressor Ambient Temperature Schedule
        Name`"""
        self["Compressor Ambient Temperature Schedule Name"] = value

    @property
    def fan_object_type(self):
        """field `Fan Object Type`

        |  Specify the type of fan used by this heat pump water heater. The only
        |  valid choice is Fan:OnOff.
        |  Default value: Fan:OnOff

        Args:
            value (str): value for IDD Field `Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_object_type` or None if not set

        """
        return self["Fan Object Type"]

    @fan_object_type.setter
    def fan_object_type(self, value="Fan:OnOff"):
        """Corresponds to IDD field `Fan Object Type`"""
        self["Fan Object Type"] = value

    @property
    def fan_name(self):
        """field `Fan Name`

        |  Needs to match the name used in the corresponding Fan:OnOff object.

        Args:
            value (str): value for IDD Field `Fan Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_name` or None if not set

        """
        return self["Fan Name"]

    @fan_name.setter
    def fan_name(self, value=None):
        """Corresponds to IDD field `Fan Name`"""
        self["Fan Name"] = value

    @property
    def fan_placement(self):
        """field `Fan Placement`

        |  BlowThrough means the fan is located before the air coil (upstream).
        |  DrawThrough means the fan is located after the air coil (downstream).
        |  Default value: DrawThrough

        Args:
            value (str): value for IDD Field `Fan Placement`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_placement` or None if not set

        """
        return self["Fan Placement"]

    @fan_placement.setter
    def fan_placement(self, value="DrawThrough"):
        """Corresponds to IDD field `Fan Placement`"""
        self["Fan Placement"] = value

    @property
    def on_cycle_parasitic_electric_load(self):
        """field `On Cycle Parasitic Electric Load`

        |  Parasitic electric power consumed when the heat pump compressor operates.
        |  Does not contribute to water heating but can impact the zone air heat balance.
        |  Units: W

        Args:
            value (float): value for IDD Field `On Cycle Parasitic Electric Load`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `on_cycle_parasitic_electric_load` or None if not set

        """
        return self["On Cycle Parasitic Electric Load"]

    @on_cycle_parasitic_electric_load.setter
    def on_cycle_parasitic_electric_load(self, value=None):
        """Corresponds to IDD field `On Cycle Parasitic Electric Load`"""
        self["On Cycle Parasitic Electric Load"] = value

    @property
    def off_cycle_parasitic_electric_load(self):
        """field `Off Cycle Parasitic Electric Load`

        |  Parasitic electric power consumed when the heat pump compressor is off.
        |  Does not contribute to water heating but can impact the zone air heat balance.
        |  Off-cycle parasitic power is 0 when the availability schedule is 0.
        |  Units: W

        Args:
            value (float): value for IDD Field `Off Cycle Parasitic Electric Load`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `off_cycle_parasitic_electric_load` or None if not set

        """
        return self["Off Cycle Parasitic Electric Load"]

    @off_cycle_parasitic_electric_load.setter
    def off_cycle_parasitic_electric_load(self, value=None):
        """Corresponds to IDD field `Off Cycle Parasitic Electric Load`"""
        self["Off Cycle Parasitic Electric Load"] = value

    @property
    def parasitic_heat_rejection_location(self):
        """field `Parasitic Heat Rejection Location`

        |  This field determines if the parasitic electric load impacts the zone air
        |  heat balance. If Zone is selected, Inlet Air Configuration must be
        |  ZoneAirOnly or ZoneAndOutdoorAir.
        |  Default value: Outdoors

        Args:
            value (str): value for IDD Field `Parasitic Heat Rejection Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `parasitic_heat_rejection_location` or None if not set

        """
        return self["Parasitic Heat Rejection Location"]

    @parasitic_heat_rejection_location.setter
    def parasitic_heat_rejection_location(self, value="Outdoors"):
        """Corresponds to IDD field `Parasitic Heat Rejection Location`"""
        self["Parasitic Heat Rejection Location"] = value

    @property
    def inlet_air_mixer_node_name(self):
        """field `Inlet Air Mixer Node Name`

        |  Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        |  leave field blank.

        Args:
            value (str): value for IDD Field `Inlet Air Mixer Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_mixer_node_name` or None if not set

        """
        return self["Inlet Air Mixer Node Name"]

    @inlet_air_mixer_node_name.setter
    def inlet_air_mixer_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Mixer Node Name`"""
        self["Inlet Air Mixer Node Name"] = value

    @property
    def outlet_air_splitter_node_name(self):
        """field `Outlet Air Splitter Node Name`

        |  Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        |  leave field blank.

        Args:
            value (str): value for IDD Field `Outlet Air Splitter Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_air_splitter_node_name` or None if not set

        """
        return self["Outlet Air Splitter Node Name"]

    @outlet_air_splitter_node_name.setter
    def outlet_air_splitter_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Air Splitter Node Name`"""
        self["Outlet Air Splitter Node Name"] = value

    @property
    def inlet_air_mixer_schedule_name(self):
        """field `Inlet Air Mixer Schedule Name`

        |  Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise
        |  leave field blank. Schedule values define whether the heat pump draws its
        |  inlet air from the zone, outdoors or a combination of zone and outdoor air.
        |  A schedule value of 0 denotes inlet air is drawn only from the zone.
        |  A schedule value of 1 denotes inlet air is drawn only from outdoors.
        |  Schedule values between 0 and 1 denote a mixture of zone and outdoor air
        |  proportional to the schedule value.

        Args:
            value (str): value for IDD Field `Inlet Air Mixer Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_air_mixer_schedule_name` or None if not set

        """
        return self["Inlet Air Mixer Schedule Name"]

    @inlet_air_mixer_schedule_name.setter
    def inlet_air_mixer_schedule_name(self, value=None):
        """Corresponds to IDD field `Inlet Air Mixer Schedule Name`"""
        self["Inlet Air Mixer Schedule Name"] = value

    @property
    def tank_element_control_logic(self):
        """field `Tank Element Control Logic`

        |  MutuallyExclusive means that once the tank heating element is active the
        |  heat pump is shut down until setpoint is reached.
        |  Simultaneous (default) means that both the tank heating element and
        |  heat pump are used at the same time recover the tank temperature.
        |  Default value: Simultaneous

        Args:
            value (str): value for IDD Field `Tank Element Control Logic`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_element_control_logic` or None if not set

        """
        return self["Tank Element Control Logic"]

    @tank_element_control_logic.setter
    def tank_element_control_logic(self, value="Simultaneous"):
        """Corresponds to IDD field `Tank Element Control Logic`"""
        self["Tank Element Control Logic"] = value

    @property
    def control_sensor_1_height_in_stratified_tank(self):
        """field `Control Sensor 1 Height In Stratified Tank`

        |  Used to indicate height of control sensor if Tank Object Type is WaterHeater:Stratified
        |  If left blank, it will default to the height of Heater1
        |  Units: m

        Args:
            value (float): value for IDD Field `Control Sensor 1 Height In Stratified Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `control_sensor_1_height_in_stratified_tank` or None if not set

        """
        return self["Control Sensor 1 Height In Stratified Tank"]

    @control_sensor_1_height_in_stratified_tank.setter
    def control_sensor_1_height_in_stratified_tank(self, value=None):
        """Corresponds to IDD field `Control Sensor 1 Height In Stratified
        Tank`"""
        self["Control Sensor 1 Height In Stratified Tank"] = value

    @property
    def control_sensor_1_weight(self):
        """field `Control Sensor 1 Weight`

        |  Weight to give Control Sensor 1 temperature
        |  Units: dimensionless
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Control Sensor 1 Weight`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `control_sensor_1_weight` or None if not set

        """
        return self["Control Sensor 1 Weight"]

    @control_sensor_1_weight.setter
    def control_sensor_1_weight(self, value=1.0):
        """Corresponds to IDD field `Control Sensor 1 Weight`"""
        self["Control Sensor 1 Weight"] = value

    @property
    def control_sensor_2_height_in_stratified_tank(self):
        """field `Control Sensor 2 Height In Stratified Tank`

        |  Used to indicate height of control sensor if Tank Object Type is WaterHeater:Stratified
        |  If left blank, it will default to the height of Heater2
        |  The weight of this control sensor will be 1 - (wt. of control sensor 1)
        |  Units: m

        Args:
            value (float): value for IDD Field `Control Sensor 2 Height In Stratified Tank`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `control_sensor_2_height_in_stratified_tank` or None if not set

        """
        return self["Control Sensor 2 Height In Stratified Tank"]

    @control_sensor_2_height_in_stratified_tank.setter
    def control_sensor_2_height_in_stratified_tank(self, value=None):
        """Corresponds to IDD field `Control Sensor 2 Height In Stratified
        Tank`"""
        self["Control Sensor 2 Height In Stratified Tank"] = value




class ThermalStorageIceSimple(DataObject):

    """ Corresponds to IDD object `ThermalStorage:Ice:Simple`
        This ice storage model is a simplified model
        It requires a setpoint placed on the Chilled Water Side Outlet Node
        It should be placed in the chilled water supply side outlet branch
        followed by a pipe.
        Use the PlantEquipmentOperation:ComponentSetpoint plant operation scheme.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'ice storage type',
                                       {'name': u'Ice Storage Type',
                                        'pyname': u'ice_storage_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'IceOnCoilInternal',
                                                            u'IceOnCoilExternal'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'capacity',
                                       {'name': u'Capacity',
                                        'pyname': u'capacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'GJ'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 5,
               'name': u'ThermalStorage:Ice:Simple',
               'pyname': u'ThermalStorageIceSimple',
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
    def ice_storage_type(self):
        """field `Ice Storage Type`

        |  IceOnCoilInternal = Ice-on-Coil, internal melt
        |  IceOnCoilExternal = Ice-on-Coil, external melt

        Args:
            value (str): value for IDD Field `Ice Storage Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ice_storage_type` or None if not set

        """
        return self["Ice Storage Type"]

    @ice_storage_type.setter
    def ice_storage_type(self, value=None):
        """Corresponds to IDD field `Ice Storage Type`"""
        self["Ice Storage Type"] = value

    @property
    def capacity(self):
        """field `Capacity`

        |  Units: GJ
        |  IP-Units: ton-hrs

        Args:
            value (float): value for IDD Field `Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `capacity` or None if not set

        """
        return self["Capacity"]

    @capacity.setter
    def capacity(self, value=None):
        """Corresponds to IDD field `Capacity`"""
        self["Capacity"] = value

    @property
    def inlet_node_name(self):
        """field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value




class ThermalStorageIceDetailed(DataObject):

    """ Corresponds to IDD object `ThermalStorage:Ice:Detailed`
        This input syntax is intended to describe a thermal storage system that
        includes smaller containers filled with water that are placed in a larger
        tank or series of tanks.
        The model uses polynomial equations to describe the system performance.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'availability schedule name',
                                       {'name': u'Availability Schedule Name',
                                        'pyname': u'availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'capacity',
                                       {'name': u'Capacity',
                                        'pyname': u'capacity',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'GJ'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'discharging curve object type',
                                       {'name': u'Discharging Curve Object Type',
                                        'pyname': u'discharging_curve_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Curve:QuadraticLinear',
                                                            u'Curve:CubicLinear'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'discharging curve name',
                                       {'name': u'Discharging Curve Name',
                                        'pyname': u'discharging_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'charging curve object type',
                                       {'name': u'Charging Curve Object Type',
                                        'pyname': u'charging_curve_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Curve:QuadraticLinear',
                                                            u'Curve:CubicLinear'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'charging curve name',
                                       {'name': u'Charging Curve Name',
                                        'pyname': u'charging_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'timestep of the curve data',
                                       {'name': u'Timestep of the Curve Data',
                                        'pyname': u'timestep_of_the_curve_data',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'hr'}),
                                      (u'parasitic electric load during discharging',
                                       {'name': u'Parasitic Electric Load During Discharging',
                                        'pyname': u'parasitic_electric_load_during_discharging',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'parasitic electric load during charging',
                                       {'name': u'Parasitic Electric Load During Charging',
                                        'pyname': u'parasitic_electric_load_during_charging',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'tank loss coefficient',
                                       {'name': u'Tank Loss Coefficient',
                                        'pyname': u'tank_loss_coefficient',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'dimensionless'}),
                                      (u'freezing temperature of storage medium',
                                       {'name': u'Freezing Temperature of Storage Medium',
                                        'pyname': u'freezing_temperature_of_storage_medium',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'thaw process indicator',
                                       {'name': u'Thaw Process Indicator',
                                        'pyname': u'thaw_process_indicator',
                                        'default': u'OutsideMelt',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'InsideMelt',
                                                            u'OutsideMelt'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 14,
               'name': u'ThermalStorage:Ice:Detailed',
               'pyname': u'ThermalStorageIceDetailed',
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
    def capacity(self):
        """field `Capacity`

        |  This includes only the latent storage capacity
        |  Units: GJ

        Args:
            value (float): value for IDD Field `Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `capacity` or None if not set

        """
        return self["Capacity"]

    @capacity.setter
    def capacity(self, value=None):
        """Corresponds to IDD field `Capacity`"""
        self["Capacity"] = value

    @property
    def inlet_node_name(self):
        """field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_node_name` or None if not set

        """
        return self["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """Corresponds to IDD field `Inlet Node Name`"""
        self["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outlet_node_name` or None if not set

        """
        return self["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """Corresponds to IDD field `Outlet Node Name`"""
        self["Outlet Node Name"] = value

    @property
    def discharging_curve_object_type(self):
        """field `Discharging Curve Object Type`

        Args:
            value (str): value for IDD Field `Discharging Curve Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `discharging_curve_object_type` or None if not set

        """
        return self["Discharging Curve Object Type"]

    @discharging_curve_object_type.setter
    def discharging_curve_object_type(self, value=None):
        """Corresponds to IDD field `Discharging Curve Object Type`"""
        self["Discharging Curve Object Type"] = value

    @property
    def discharging_curve_name(self):
        """field `Discharging Curve Name`

        Args:
            value (str): value for IDD Field `Discharging Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `discharging_curve_name` or None if not set

        """
        return self["Discharging Curve Name"]

    @discharging_curve_name.setter
    def discharging_curve_name(self, value=None):
        """Corresponds to IDD field `Discharging Curve Name`"""
        self["Discharging Curve Name"] = value

    @property
    def charging_curve_object_type(self):
        """field `Charging Curve Object Type`

        Args:
            value (str): value for IDD Field `Charging Curve Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `charging_curve_object_type` or None if not set

        """
        return self["Charging Curve Object Type"]

    @charging_curve_object_type.setter
    def charging_curve_object_type(self, value=None):
        """Corresponds to IDD field `Charging Curve Object Type`"""
        self["Charging Curve Object Type"] = value

    @property
    def charging_curve_name(self):
        """field `Charging Curve Name`

        Args:
            value (str): value for IDD Field `Charging Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `charging_curve_name` or None if not set

        """
        return self["Charging Curve Name"]

    @charging_curve_name.setter
    def charging_curve_name(self, value=None):
        """Corresponds to IDD field `Charging Curve Name`"""
        self["Charging Curve Name"] = value

    @property
    def timestep_of_the_curve_data(self):
        """field `Timestep of the Curve Data`

        |  Units: hr

        Args:
            value (float): value for IDD Field `Timestep of the Curve Data`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `timestep_of_the_curve_data` or None if not set

        """
        return self["Timestep of the Curve Data"]

    @timestep_of_the_curve_data.setter
    def timestep_of_the_curve_data(self, value=None):
        """Corresponds to IDD field `Timestep of the Curve Data`"""
        self["Timestep of the Curve Data"] = value

    @property
    def parasitic_electric_load_during_discharging(self):
        """field `Parasitic Electric Load During Discharging`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Parasitic Electric Load During Discharging`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `parasitic_electric_load_during_discharging` or None if not set

        """
        return self["Parasitic Electric Load During Discharging"]

    @parasitic_electric_load_during_discharging.setter
    def parasitic_electric_load_during_discharging(self, value=None):
        """Corresponds to IDD field `Parasitic Electric Load During
        Discharging`"""
        self["Parasitic Electric Load During Discharging"] = value

    @property
    def parasitic_electric_load_during_charging(self):
        """field `Parasitic Electric Load During Charging`

        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Parasitic Electric Load During Charging`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `parasitic_electric_load_during_charging` or None if not set

        """
        return self["Parasitic Electric Load During Charging"]

    @parasitic_electric_load_during_charging.setter
    def parasitic_electric_load_during_charging(self, value=None):
        """Corresponds to IDD field `Parasitic Electric Load During
        Charging`"""
        self["Parasitic Electric Load During Charging"] = value

    @property
    def tank_loss_coefficient(self):
        """field `Tank Loss Coefficient`

        |  This is the fraction the total storage capacity that is lost or melts
        |  each hour
        |  Units: dimensionless

        Args:
            value (float): value for IDD Field `Tank Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_loss_coefficient` or None if not set

        """
        return self["Tank Loss Coefficient"]

    @tank_loss_coefficient.setter
    def tank_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Tank Loss Coefficient`"""
        self["Tank Loss Coefficient"] = value

    @property
    def freezing_temperature_of_storage_medium(self):
        """field `Freezing Temperature of Storage Medium`

        |  This temperature is typically 0C for water.
        |  Simply changing this temperature without adjusting the performance
        |  parameters input above is inappropriate and not advised.
        |  Units: C

        Args:
            value (float): value for IDD Field `Freezing Temperature of Storage Medium`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `freezing_temperature_of_storage_medium` or None if not set

        """
        return self["Freezing Temperature of Storage Medium"]

    @freezing_temperature_of_storage_medium.setter
    def freezing_temperature_of_storage_medium(self, value=None):
        """Corresponds to IDD field `Freezing Temperature of Storage Medium`"""
        self["Freezing Temperature of Storage Medium"] = value

    @property
    def thaw_process_indicator(self):
        """field `Thaw Process Indicator`

        |  This field determines whether the system uses internal or external melt
        |  during discharging.  This will then have an impact on charging performance.
        |  Default value: OutsideMelt

        Args:
            value (str): value for IDD Field `Thaw Process Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thaw_process_indicator` or None if not set

        """
        return self["Thaw Process Indicator"]

    @thaw_process_indicator.setter
    def thaw_process_indicator(self, value="OutsideMelt"):
        """Corresponds to IDD field `Thaw Process Indicator`"""
        self["Thaw Process Indicator"] = value




class ThermalStorageChilledWaterMixed(DataObject):

    """ Corresponds to IDD object `ThermalStorage:ChilledWater:Mixed`
        Chilled water storage with a well-mixed, single-node tank. The chilled water is
        "used" by drawing from the "Use Side" of the water tank.  The tank is indirectly
        charged by circulating cold water through the "Source Side" of the water tank.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'tank volume',
                                       {'name': u'Tank Volume',
                                        'pyname': u'tank_volume',
                                        'default': 0.1,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'setpoint temperature schedule name',
                                       {'name': u'Setpoint Temperature Schedule Name',
                                        'pyname': u'setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'deadband temperature difference',
                                       {'name': u'Deadband Temperature Difference',
                                        'pyname': u'deadband_temperature_difference',
                                        'default': 0.5,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'minimum temperature limit',
                                       {'name': u'Minimum Temperature Limit',
                                        'pyname': u'minimum_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'nominal cooling capacity',
                                       {'name': u'Nominal Cooling Capacity',
                                        'pyname': u'nominal_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'ambient temperature indicator',
                                       {'name': u'Ambient Temperature Indicator',
                                        'pyname': u'ambient_temperature_indicator',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ambient temperature schedule name',
                                       {'name': u'Ambient Temperature Schedule Name',
                                        'pyname': u'ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature zone name',
                                       {'name': u'Ambient Temperature Zone Name',
                                        'pyname': u'ambient_temperature_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature outdoor air node name',
                                       {'name': u'Ambient Temperature Outdoor Air Node Name',
                                        'pyname': u'ambient_temperature_outdoor_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heat gain coefficient from ambient temperature',
                                       {'name': u'Heat Gain Coefficient from Ambient Temperature',
                                        'pyname': u'heat_gain_coefficient_from_ambient_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'use side inlet node name',
                                       {'name': u'Use Side Inlet Node Name',
                                        'pyname': u'use_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side outlet node name',
                                       {'name': u'Use Side Outlet Node Name',
                                        'pyname': u'use_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side heat transfer effectiveness',
                                       {'name': u'Use Side Heat Transfer Effectiveness',
                                        'pyname': u'use_side_heat_transfer_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'use side availability schedule name',
                                       {'name': u'Use Side Availability Schedule Name',
                                        'pyname': u'use_side_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'use side design flow rate',
                                       {'name': u'Use Side Design Flow Rate',
                                        'pyname': u'use_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'source side inlet node name',
                                       {'name': u'Source Side Inlet Node Name',
                                        'pyname': u'source_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side outlet node name',
                                       {'name': u'Source Side Outlet Node Name',
                                        'pyname': u'source_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side heat transfer effectiveness',
                                       {'name': u'Source Side Heat Transfer Effectiveness',
                                        'pyname': u'source_side_heat_transfer_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'source side availability schedule name',
                                       {'name': u'Source Side Availability Schedule Name',
                                        'pyname': u'source_side_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'source side design flow rate',
                                       {'name': u'Source Side Design Flow Rate',
                                        'pyname': u'source_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'tank recovery time',
                                       {'name': u'Tank Recovery Time',
                                        'pyname': u'tank_recovery_time',
                                        'default': 4.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 0,
               'name': u'ThermalStorage:ChilledWater:Mixed',
               'pyname': u'ThermalStorageChilledWaterMixed',
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
    def tank_volume(self):
        """field `Tank Volume`

        |  Units: m3
        |  IP-Units: gal
        |  Default value: 0.1

        Args:
            value (float): value for IDD Field `Tank Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_volume` or None if not set

        """
        return self["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=0.1):
        """Corresponds to IDD field `Tank Volume`"""
        self["Tank Volume"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set

        """
        return self["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule Name`"""
        self["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """field `Deadband Temperature Difference`

        |  Units: deltaC
        |  Default value: 0.5

        Args:
            value (float): value for IDD Field `Deadband Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set

        """
        return self["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=0.5):
        """Corresponds to IDD field `Deadband Temperature Difference`"""
        self["Deadband Temperature Difference"] = value

    @property
    def minimum_temperature_limit(self):
        """field `Minimum Temperature Limit`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_temperature_limit` or None if not set

        """
        return self["Minimum Temperature Limit"]

    @minimum_temperature_limit.setter
    def minimum_temperature_limit(self, value=None):
        """Corresponds to IDD field `Minimum Temperature Limit`"""
        self["Minimum Temperature Limit"] = value

    @property
    def nominal_cooling_capacity(self):
        """field `Nominal Cooling Capacity`

        |  Units: W

        Args:
            value (float): value for IDD Field `Nominal Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set

        """
        return self["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """Corresponds to IDD field `Nominal Cooling Capacity`"""
        self["Nominal Cooling Capacity"] = value

    @property
    def ambient_temperature_indicator(self):
        """field `Ambient Temperature Indicator`

        Args:
            value (str): value for IDD Field `Ambient Temperature Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set

        """
        return self["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Indicator`"""
        self["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set

        """
        return self["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Schedule Name`"""
        self["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """field `Ambient Temperature Zone Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set

        """
        return self["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Zone Name`"""
        self["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """field `Ambient Temperature Outdoor Air Node Name`

        |  required when field Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `Ambient Temperature Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set

        """
        return self["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Outdoor Air Node
        Name`"""
        self["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def heat_gain_coefficient_from_ambient_temperature(self):
        """field `Heat Gain Coefficient from Ambient Temperature`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Heat Gain Coefficient from Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_gain_coefficient_from_ambient_temperature` or None if not set

        """
        return self["Heat Gain Coefficient from Ambient Temperature"]

    @heat_gain_coefficient_from_ambient_temperature.setter
    def heat_gain_coefficient_from_ambient_temperature(self, value=None):
        """Corresponds to IDD field `Heat Gain Coefficient from Ambient
        Temperature`"""
        self["Heat Gain Coefficient from Ambient Temperature"] = value

    @property
    def use_side_inlet_node_name(self):
        """field `Use Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set

        """
        return self["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Inlet Node Name`"""
        self["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """field `Use Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set

        """
        return self["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Outlet Node Name`"""
        self["Use Side Outlet Node Name"] = value

    @property
    def use_side_heat_transfer_effectiveness(self):
        """field `Use Side Heat Transfer Effectiveness`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Use Side Heat Transfer Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `use_side_heat_transfer_effectiveness` or None if not set

        """
        return self["Use Side Heat Transfer Effectiveness"]

    @use_side_heat_transfer_effectiveness.setter
    def use_side_heat_transfer_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Use Side Heat Transfer Effectiveness`"""
        self["Use Side Heat Transfer Effectiveness"] = value

    @property
    def use_side_availability_schedule_name(self):
        """field `Use Side Availability Schedule Name`

        |  Availability schedule name for use side. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Use Side Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_availability_schedule_name` or None if not set

        """
        return self["Use Side Availability Schedule Name"]

    @use_side_availability_schedule_name.setter
    def use_side_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Use Side Availability Schedule Name`"""
        self["Use Side Availability Schedule Name"] = value

    @property
    def use_side_design_flow_rate(self):
        """field `Use Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Use Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `use_side_design_flow_rate` or None if not set

        """
        return self["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Use Side Design Flow Rate`"""
        self["Use Side Design Flow Rate"] = value

    @property
    def source_side_inlet_node_name(self):
        """field `Source Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set

        """
        return self["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Inlet Node Name`"""
        self["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """field `Source Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set

        """
        return self["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Outlet Node Name`"""
        self["Source Side Outlet Node Name"] = value

    @property
    def source_side_heat_transfer_effectiveness(self):
        """field `Source Side Heat Transfer Effectiveness`

        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Source Side Heat Transfer Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_side_heat_transfer_effectiveness` or None if not set

        """
        return self["Source Side Heat Transfer Effectiveness"]

    @source_side_heat_transfer_effectiveness.setter
    def source_side_heat_transfer_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Source Side Heat Transfer
        Effectiveness`"""
        self["Source Side Heat Transfer Effectiveness"] = value

    @property
    def source_side_availability_schedule_name(self):
        """field `Source Side Availability Schedule Name`

        |  Availability schedule name for source side. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Source Side Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_availability_schedule_name` or None if not set

        """
        return self["Source Side Availability Schedule Name"]

    @source_side_availability_schedule_name.setter
    def source_side_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Source Side Availability Schedule Name`"""
        self["Source Side Availability Schedule Name"] = value

    @property
    def source_side_design_flow_rate(self):
        """field `Source Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Source Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `source_side_design_flow_rate` or None if not set

        """
        return self["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Source Side Design Flow Rate`"""
        self["Source Side Design Flow Rate"] = value

    @property
    def tank_recovery_time(self):
        """field `Tank Recovery Time`

        |  Parameter for autosizing design flow rates for indirectly cooled water tanks
        |  time required to lower temperature of entire tank from 14.4C to 9.0C
        |  Units: hr
        |  Default value: 4.0

        Args:
            value (float): value for IDD Field `Tank Recovery Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_recovery_time` or None if not set

        """
        return self["Tank Recovery Time"]

    @tank_recovery_time.setter
    def tank_recovery_time(self, value=4.0):
        """Corresponds to IDD field `Tank Recovery Time`"""
        self["Tank Recovery Time"] = value




class ThermalStorageChilledWaterStratified(DataObject):

    """ Corresponds to IDD object `ThermalStorage:ChilledWater:Stratified`
        Chilled water storage with a stratified, multi-node tank. The chilled water is
        "used" by drawing from the "Use Side" of the water tank.  The tank is indirectly
        charged by circulating cold water through the "Source Side" of the water tank.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'tank volume',
                                       {'name': u'Tank Volume',
                                        'pyname': u'tank_volume',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'tank height',
                                       {'name': u'Tank Height',
                                        'pyname': u'tank_height',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'tank shape',
                                       {'name': u'Tank Shape',
                                        'pyname': u'tank_shape',
                                        'default': u'VerticalCylinder',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'VerticalCylinder',
                                                            u'HorizontalCylinder',
                                                            u'Other'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'tank perimeter',
                                       {'name': u'Tank Perimeter',
                                        'pyname': u'tank_perimeter',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'setpoint temperature schedule name',
                                       {'name': u'Setpoint Temperature Schedule Name',
                                        'pyname': u'setpoint_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'deadband temperature difference',
                                       {'name': u'Deadband Temperature Difference',
                                        'pyname': u'deadband_temperature_difference',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'temperature sensor height',
                                       {'name': u'Temperature Sensor Height',
                                        'pyname': u'temperature_sensor_height',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'minimum temperature limit',
                                       {'name': u'Minimum Temperature Limit',
                                        'pyname': u'minimum_temperature_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'nominal cooling capacity',
                                       {'name': u'Nominal Cooling Capacity',
                                        'pyname': u'nominal_cooling_capacity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'ambient temperature indicator',
                                       {'name': u'Ambient Temperature Indicator',
                                        'pyname': u'ambient_temperature_indicator',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Schedule',
                                                            u'Zone',
                                                            u'Outdoors'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'ambient temperature schedule name',
                                       {'name': u'Ambient Temperature Schedule Name',
                                        'pyname': u'ambient_temperature_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature zone name',
                                       {'name': u'Ambient Temperature Zone Name',
                                        'pyname': u'ambient_temperature_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient temperature outdoor air node name',
                                       {'name': u'Ambient Temperature Outdoor Air Node Name',
                                        'pyname': u'ambient_temperature_outdoor_air_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'uniform skin loss coefficient per unit area to ambient temperature',
                                       {'name': u'Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature',
                                        'pyname': u'uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m2-K'}),
                                      (u'use side inlet node name',
                                       {'name': u'Use Side Inlet Node Name',
                                        'pyname': u'use_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side outlet node name',
                                       {'name': u'Use Side Outlet Node Name',
                                        'pyname': u'use_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'use side heat transfer effectiveness',
                                       {'name': u'Use Side Heat Transfer Effectiveness',
                                        'pyname': u'use_side_heat_transfer_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'use side availability schedule name',
                                       {'name': u'Use Side Availability Schedule Name',
                                        'pyname': u'use_side_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'use side inlet height',
                                       {'name': u'Use Side Inlet Height',
                                        'pyname': u'use_side_inlet_height',
                                        'default': 'autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'use side outlet height',
                                       {'name': u'Use Side Outlet Height',
                                        'pyname': u'use_side_outlet_height',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'use side design flow rate',
                                       {'name': u'Use Side Design Flow Rate',
                                        'pyname': u'use_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'source side inlet node name',
                                       {'name': u'Source Side Inlet Node Name',
                                        'pyname': u'source_side_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side outlet node name',
                                       {'name': u'Source Side Outlet Node Name',
                                        'pyname': u'source_side_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'source side heat transfer effectiveness',
                                       {'name': u'Source Side Heat Transfer Effectiveness',
                                        'pyname': u'source_side_heat_transfer_effectiveness',
                                        'default': 1.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'source side availability schedule name',
                                       {'name': u'Source Side Availability Schedule Name',
                                        'pyname': u'source_side_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'source side inlet height',
                                       {'name': u'Source Side Inlet Height',
                                        'pyname': u'source_side_inlet_height',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'source side outlet height',
                                       {'name': u'Source Side Outlet Height',
                                        'pyname': u'source_side_outlet_height',
                                        'default': 'autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'source side design flow rate',
                                       {'name': u'Source Side Design Flow Rate',
                                        'pyname': u'source_side_design_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'tank recovery time',
                                       {'name': u'Tank Recovery Time',
                                        'pyname': u'tank_recovery_time',
                                        'default': 4.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'inlet mode',
                                       {'name': u'Inlet Mode',
                                        'pyname': u'inlet_mode',
                                        'default': u'Fixed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Fixed',
                                                            u'Seeking'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'number of nodes',
                                       {'name': u'Number of Nodes',
                                        'pyname': u'number_of_nodes',
                                        'default': 1,
                                        'maximum': 10,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'additional destratification conductivity',
                                       {'name': u'Additional Destratification Conductivity',
                                        'pyname': u'additional_destratification_conductivity',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'node 1 additional loss coefficient',
                                       {'name': u'Node 1 Additional Loss Coefficient',
                                        'pyname': u'node_1_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 2 additional loss coefficient',
                                       {'name': u'Node 2 Additional Loss Coefficient',
                                        'pyname': u'node_2_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 3 additional loss coefficient',
                                       {'name': u'Node 3 Additional Loss Coefficient',
                                        'pyname': u'node_3_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 4 additional loss coefficient',
                                       {'name': u'Node 4 Additional Loss Coefficient',
                                        'pyname': u'node_4_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 5 additional loss coefficient',
                                       {'name': u'Node 5 Additional Loss Coefficient',
                                        'pyname': u'node_5_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 6 additional loss coefficient',
                                       {'name': u'Node 6 Additional Loss Coefficient',
                                        'pyname': u'node_6_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 7 additional loss coefficient',
                                       {'name': u'Node 7 Additional Loss Coefficient',
                                        'pyname': u'node_7_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 8 additional loss coefficient',
                                       {'name': u'Node 8 Additional Loss Coefficient',
                                        'pyname': u'node_8_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 9 additional loss coefficient',
                                       {'name': u'Node 9 Additional Loss Coefficient',
                                        'pyname': u'node_9_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'node 10 additional loss coefficient',
                                       {'name': u'Node 10 Additional Loss Coefficient',
                                        'pyname': u'node_10_additional_loss_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'})]),
               'format': None,
               'group': u'Water Heaters and Thermal Storage',
               'min-fields': 0,
               'name': u'ThermalStorage:ChilledWater:Stratified',
               'pyname': u'ThermalStorageChilledWaterStratified',
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
    def tank_volume(self):
        """field `Tank Volume`

        |  Units: m3
        |  IP-Units: gal

        Args:
            value (float): value for IDD Field `Tank Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_volume` or None if not set

        """
        return self["Tank Volume"]

    @tank_volume.setter
    def tank_volume(self, value=None):
        """Corresponds to IDD field `Tank Volume`"""
        self["Tank Volume"] = value

    @property
    def tank_height(self):
        """field `Tank Height`

        |  Height is measured in the axial direction for horizontal cylinders
        |  Units: m

        Args:
            value (float): value for IDD Field `Tank Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_height` or None if not set

        """
        return self["Tank Height"]

    @tank_height.setter
    def tank_height(self, value=None):
        """Corresponds to IDD field `Tank Height`"""
        self["Tank Height"] = value

    @property
    def tank_shape(self):
        """field `Tank Shape`

        |  Default value: VerticalCylinder

        Args:
            value (str): value for IDD Field `Tank Shape`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `tank_shape` or None if not set

        """
        return self["Tank Shape"]

    @tank_shape.setter
    def tank_shape(self, value="VerticalCylinder"):
        """Corresponds to IDD field `Tank Shape`"""
        self["Tank Shape"] = value

    @property
    def tank_perimeter(self):
        """field `Tank Perimeter`

        |  Only used if Tank Shape is Other
        |  Units: m

        Args:
            value (float): value for IDD Field `Tank Perimeter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_perimeter` or None if not set

        """
        return self["Tank Perimeter"]

    @tank_perimeter.setter
    def tank_perimeter(self, value=None):
        """Corresponds to IDD field `Tank Perimeter`"""
        self["Tank Perimeter"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """field `Setpoint Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Setpoint Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set

        """
        return self["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Setpoint Temperature Schedule Name`"""
        self["Setpoint Temperature Schedule Name"] = value

    @property
    def deadband_temperature_difference(self):
        """field `Deadband Temperature Difference`

        |  Units: deltaC

        Args:
            value (float): value for IDD Field `Deadband Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `deadband_temperature_difference` or None if not set

        """
        return self["Deadband Temperature Difference"]

    @deadband_temperature_difference.setter
    def deadband_temperature_difference(self, value=None):
        """Corresponds to IDD field `Deadband Temperature Difference`"""
        self["Deadband Temperature Difference"] = value

    @property
    def temperature_sensor_height(self):
        """field `Temperature Sensor Height`

        |  Units: m

        Args:
            value (float): value for IDD Field `Temperature Sensor Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `temperature_sensor_height` or None if not set

        """
        return self["Temperature Sensor Height"]

    @temperature_sensor_height.setter
    def temperature_sensor_height(self, value=None):
        """Corresponds to IDD field `Temperature Sensor Height`"""
        self["Temperature Sensor Height"] = value

    @property
    def minimum_temperature_limit(self):
        """field `Minimum Temperature Limit`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Temperature Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_temperature_limit` or None if not set

        """
        return self["Minimum Temperature Limit"]

    @minimum_temperature_limit.setter
    def minimum_temperature_limit(self, value=None):
        """Corresponds to IDD field `Minimum Temperature Limit`"""
        self["Minimum Temperature Limit"] = value

    @property
    def nominal_cooling_capacity(self):
        """field `Nominal Cooling Capacity`

        |  Units: W

        Args:
            value (float): value for IDD Field `Nominal Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_cooling_capacity` or None if not set

        """
        return self["Nominal Cooling Capacity"]

    @nominal_cooling_capacity.setter
    def nominal_cooling_capacity(self, value=None):
        """Corresponds to IDD field `Nominal Cooling Capacity`"""
        self["Nominal Cooling Capacity"] = value

    @property
    def ambient_temperature_indicator(self):
        """field `Ambient Temperature Indicator`

        Args:
            value (str): value for IDD Field `Ambient Temperature Indicator`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_indicator` or None if not set

        """
        return self["Ambient Temperature Indicator"]

    @ambient_temperature_indicator.setter
    def ambient_temperature_indicator(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Indicator`"""
        self["Ambient Temperature Indicator"] = value

    @property
    def ambient_temperature_schedule_name(self):
        """field `Ambient Temperature Schedule Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_schedule_name` or None if not set

        """
        return self["Ambient Temperature Schedule Name"]

    @ambient_temperature_schedule_name.setter
    def ambient_temperature_schedule_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Schedule Name`"""
        self["Ambient Temperature Schedule Name"] = value

    @property
    def ambient_temperature_zone_name(self):
        """field `Ambient Temperature Zone Name`

        Args:
            value (str): value for IDD Field `Ambient Temperature Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_zone_name` or None if not set

        """
        return self["Ambient Temperature Zone Name"]

    @ambient_temperature_zone_name.setter
    def ambient_temperature_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Zone Name`"""
        self["Ambient Temperature Zone Name"] = value

    @property
    def ambient_temperature_outdoor_air_node_name(self):
        """field `Ambient Temperature Outdoor Air Node Name`

        |  required for Ambient Temperature Indicator=Outdoors

        Args:
            value (str): value for IDD Field `Ambient Temperature Outdoor Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_temperature_outdoor_air_node_name` or None if not set

        """
        return self["Ambient Temperature Outdoor Air Node Name"]

    @ambient_temperature_outdoor_air_node_name.setter
    def ambient_temperature_outdoor_air_node_name(self, value=None):
        """Corresponds to IDD field `Ambient Temperature Outdoor Air Node
        Name`"""
        self["Ambient Temperature Outdoor Air Node Name"] = value

    @property
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(
            self):
        """field `Uniform Skin Loss Coefficient per Unit Area to Ambient
        Temperature`

        |  Units: W/m2-K

        Args:
            value (float): value for IDD Field `Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature` or None if not set

        """
        return self[
            "Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"]

    @uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature.setter
    def uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Uniform Skin Loss Coefficient per Unit
        Area to Ambient Temperature`"""
        self[
            "Uniform Skin Loss Coefficient per Unit Area to Ambient Temperature"] = value

    @property
    def use_side_inlet_node_name(self):
        """field `Use Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_inlet_node_name` or None if not set

        """
        return self["Use Side Inlet Node Name"]

    @use_side_inlet_node_name.setter
    def use_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Inlet Node Name`"""
        self["Use Side Inlet Node Name"] = value

    @property
    def use_side_outlet_node_name(self):
        """field `Use Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Use Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_outlet_node_name` or None if not set

        """
        return self["Use Side Outlet Node Name"]

    @use_side_outlet_node_name.setter
    def use_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Use Side Outlet Node Name`"""
        self["Use Side Outlet Node Name"] = value

    @property
    def use_side_heat_transfer_effectiveness(self):
        """field `Use Side Heat Transfer Effectiveness`

        |  The use side effectiveness in the stratified tank model is a simplified analogy of
        |  a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        |  use mass flow rate that directly mixes with the tank fluid. And one minus the
        |  effectiveness is the fraction that bypasses the tank. The use side mass flow rate
        |  that bypasses the tank is mixed with the fluid or water leaving the stratified tank.
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Use Side Heat Transfer Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `use_side_heat_transfer_effectiveness` or None if not set

        """
        return self["Use Side Heat Transfer Effectiveness"]

    @use_side_heat_transfer_effectiveness.setter
    def use_side_heat_transfer_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Use Side Heat Transfer Effectiveness`"""
        self["Use Side Heat Transfer Effectiveness"] = value

    @property
    def use_side_availability_schedule_name(self):
        """field `Use Side Availability Schedule Name`

        |  Availability schedule name for use side. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Use Side Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `use_side_availability_schedule_name` or None if not set

        """
        return self["Use Side Availability Schedule Name"]

    @use_side_availability_schedule_name.setter
    def use_side_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Use Side Availability Schedule Name`"""
        self["Use Side Availability Schedule Name"] = value

    @property
    def use_side_inlet_height(self):
        """field `Use Side Inlet Height`

        |  Defaults to top of tank
        |  Units: m
        |  Default value: "autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Use Side Inlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `use_side_inlet_height` or None if not set

        """
        return self["Use Side Inlet Height"]

    @use_side_inlet_height.setter
    def use_side_inlet_height(self, value="autocalculate"):
        """Corresponds to IDD field `Use Side Inlet Height`"""
        self["Use Side Inlet Height"] = value

    @property
    def use_side_outlet_height(self):
        """field `Use Side Outlet Height`

        |  Defaults to bottom of tank
        |  Units: m

        Args:
            value (float): value for IDD Field `Use Side Outlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `use_side_outlet_height` or None if not set

        """
        return self["Use Side Outlet Height"]

    @use_side_outlet_height.setter
    def use_side_outlet_height(self, value=None):
        """Corresponds to IDD field `Use Side Outlet Height`"""
        self["Use Side Outlet Height"] = value

    @property
    def use_side_design_flow_rate(self):
        """field `Use Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Use Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `use_side_design_flow_rate` or None if not set

        """
        return self["Use Side Design Flow Rate"]

    @use_side_design_flow_rate.setter
    def use_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Use Side Design Flow Rate`"""
        self["Use Side Design Flow Rate"] = value

    @property
    def source_side_inlet_node_name(self):
        """field `Source Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_inlet_node_name` or None if not set

        """
        return self["Source Side Inlet Node Name"]

    @source_side_inlet_node_name.setter
    def source_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Inlet Node Name`"""
        self["Source Side Inlet Node Name"] = value

    @property
    def source_side_outlet_node_name(self):
        """field `Source Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Source Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_outlet_node_name` or None if not set

        """
        return self["Source Side Outlet Node Name"]

    @source_side_outlet_node_name.setter
    def source_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Source Side Outlet Node Name`"""
        self["Source Side Outlet Node Name"] = value

    @property
    def source_side_heat_transfer_effectiveness(self):
        """field `Source Side Heat Transfer Effectiveness`

        |  The source side effectiveness in the stratified tank model is a simplified analogy of
        |  a heat exchanger's effectiveness. This effectiveness is equal to the fraction of
        |  source mass flow rate that directly mixes with the tank fluid. And one minus the
        |  effectiveness is the fraction that bypasses the tank. The source side mass flow rate
        |  that bypasses the tank is mixed with the fluid or water leaving the stratified tank.
        |  Default value: 1.0
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Source Side Heat Transfer Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_side_heat_transfer_effectiveness` or None if not set

        """
        return self["Source Side Heat Transfer Effectiveness"]

    @source_side_heat_transfer_effectiveness.setter
    def source_side_heat_transfer_effectiveness(self, value=1.0):
        """Corresponds to IDD field `Source Side Heat Transfer
        Effectiveness`"""
        self["Source Side Heat Transfer Effectiveness"] = value

    @property
    def source_side_availability_schedule_name(self):
        """field `Source Side Availability Schedule Name`

        |  Availability schedule name for use side. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `Source Side Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `source_side_availability_schedule_name` or None if not set

        """
        return self["Source Side Availability Schedule Name"]

    @source_side_availability_schedule_name.setter
    def source_side_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Source Side Availability Schedule Name`"""
        self["Source Side Availability Schedule Name"] = value

    @property
    def source_side_inlet_height(self):
        """field `Source Side Inlet Height`

        |  Defaults to bottom of tank
        |  Units: m

        Args:
            value (float): value for IDD Field `Source Side Inlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `source_side_inlet_height` or None if not set

        """
        return self["Source Side Inlet Height"]

    @source_side_inlet_height.setter
    def source_side_inlet_height(self, value=None):
        """Corresponds to IDD field `Source Side Inlet Height`"""
        self["Source Side Inlet Height"] = value

    @property
    def source_side_outlet_height(self):
        """field `Source Side Outlet Height`

        |  Defaults to top of tank
        |  Units: m
        |  Default value: "autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Source Side Outlet Height`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `source_side_outlet_height` or None if not set

        """
        return self["Source Side Outlet Height"]

    @source_side_outlet_height.setter
    def source_side_outlet_height(self, value="autocalculate"):
        """Corresponds to IDD field `Source Side Outlet Height`"""
        self["Source Side Outlet Height"] = value

    @property
    def source_side_design_flow_rate(self):
        """field `Source Side Design Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Source Side Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `source_side_design_flow_rate` or None if not set

        """
        return self["Source Side Design Flow Rate"]

    @source_side_design_flow_rate.setter
    def source_side_design_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Source Side Design Flow Rate`"""
        self["Source Side Design Flow Rate"] = value

    @property
    def tank_recovery_time(self):
        """field `Tank Recovery Time`

        |  Parameter for autosizing design flow rates for indirectly cooled water tanks
        |  time required to lower temperature of entire tank from 14.4C to 9.0C
        |  Units: hr
        |  Default value: 4.0

        Args:
            value (float): value for IDD Field `Tank Recovery Time`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `tank_recovery_time` or None if not set

        """
        return self["Tank Recovery Time"]

    @tank_recovery_time.setter
    def tank_recovery_time(self, value=4.0):
        """Corresponds to IDD field `Tank Recovery Time`"""
        self["Tank Recovery Time"] = value

    @property
    def inlet_mode(self):
        """field `Inlet Mode`

        |  Default value: Fixed

        Args:
            value (str): value for IDD Field `Inlet Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `inlet_mode` or None if not set

        """
        return self["Inlet Mode"]

    @inlet_mode.setter
    def inlet_mode(self, value="Fixed"):
        """Corresponds to IDD field `Inlet Mode`"""
        self["Inlet Mode"] = value

    @property
    def number_of_nodes(self):
        """field `Number of Nodes`

        |  Default value: 1
        |  value >= 1
        |  value <= 10

        Args:
            value (int): value for IDD Field `Number of Nodes`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_nodes` or None if not set

        """
        return self["Number of Nodes"]

    @number_of_nodes.setter
    def number_of_nodes(self, value=1):
        """Corresponds to IDD field `Number of Nodes`"""
        self["Number of Nodes"] = value

    @property
    def additional_destratification_conductivity(self):
        """field `Additional Destratification Conductivity`

        |  Units: W/m-K

        Args:
            value (float): value for IDD Field `Additional Destratification Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `additional_destratification_conductivity` or None if not set

        """
        return self["Additional Destratification Conductivity"]

    @additional_destratification_conductivity.setter
    def additional_destratification_conductivity(self, value=None):
        """Corresponds to IDD field `Additional Destratification
        Conductivity`"""
        self["Additional Destratification Conductivity"] = value

    @property
    def node_1_additional_loss_coefficient(self):
        """field `Node 1 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 1 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_1_additional_loss_coefficient` or None if not set

        """
        return self["Node 1 Additional Loss Coefficient"]

    @node_1_additional_loss_coefficient.setter
    def node_1_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 1 Additional Loss Coefficient`"""
        self["Node 1 Additional Loss Coefficient"] = value

    @property
    def node_2_additional_loss_coefficient(self):
        """field `Node 2 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 2 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_2_additional_loss_coefficient` or None if not set

        """
        return self["Node 2 Additional Loss Coefficient"]

    @node_2_additional_loss_coefficient.setter
    def node_2_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 2 Additional Loss Coefficient`"""
        self["Node 2 Additional Loss Coefficient"] = value

    @property
    def node_3_additional_loss_coefficient(self):
        """field `Node 3 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 3 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_3_additional_loss_coefficient` or None if not set

        """
        return self["Node 3 Additional Loss Coefficient"]

    @node_3_additional_loss_coefficient.setter
    def node_3_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 3 Additional Loss Coefficient`"""
        self["Node 3 Additional Loss Coefficient"] = value

    @property
    def node_4_additional_loss_coefficient(self):
        """field `Node 4 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 4 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_4_additional_loss_coefficient` or None if not set

        """
        return self["Node 4 Additional Loss Coefficient"]

    @node_4_additional_loss_coefficient.setter
    def node_4_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 4 Additional Loss Coefficient`"""
        self["Node 4 Additional Loss Coefficient"] = value

    @property
    def node_5_additional_loss_coefficient(self):
        """field `Node 5 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 5 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_5_additional_loss_coefficient` or None if not set

        """
        return self["Node 5 Additional Loss Coefficient"]

    @node_5_additional_loss_coefficient.setter
    def node_5_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 5 Additional Loss Coefficient`"""
        self["Node 5 Additional Loss Coefficient"] = value

    @property
    def node_6_additional_loss_coefficient(self):
        """field `Node 6 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 6 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_6_additional_loss_coefficient` or None if not set

        """
        return self["Node 6 Additional Loss Coefficient"]

    @node_6_additional_loss_coefficient.setter
    def node_6_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 6 Additional Loss Coefficient`"""
        self["Node 6 Additional Loss Coefficient"] = value

    @property
    def node_7_additional_loss_coefficient(self):
        """field `Node 7 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 7 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_7_additional_loss_coefficient` or None if not set

        """
        return self["Node 7 Additional Loss Coefficient"]

    @node_7_additional_loss_coefficient.setter
    def node_7_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 7 Additional Loss Coefficient`"""
        self["Node 7 Additional Loss Coefficient"] = value

    @property
    def node_8_additional_loss_coefficient(self):
        """field `Node 8 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 8 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_8_additional_loss_coefficient` or None if not set

        """
        return self["Node 8 Additional Loss Coefficient"]

    @node_8_additional_loss_coefficient.setter
    def node_8_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 8 Additional Loss Coefficient`"""
        self["Node 8 Additional Loss Coefficient"] = value

    @property
    def node_9_additional_loss_coefficient(self):
        """field `Node 9 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 9 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_9_additional_loss_coefficient` or None if not set

        """
        return self["Node 9 Additional Loss Coefficient"]

    @node_9_additional_loss_coefficient.setter
    def node_9_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 9 Additional Loss Coefficient`"""
        self["Node 9 Additional Loss Coefficient"] = value

    @property
    def node_10_additional_loss_coefficient(self):
        """field `Node 10 Additional Loss Coefficient`

        |  Units: W/K

        Args:
            value (float): value for IDD Field `Node 10 Additional Loss Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `node_10_additional_loss_coefficient` or None if not set

        """
        return self["Node 10 Additional Loss Coefficient"]

    @node_10_additional_loss_coefficient.setter
    def node_10_additional_loss_coefficient(self, value=None):
        """Corresponds to IDD field `Node 10 Additional Loss Coefficient`"""
        self["Node 10 Additional Loss Coefficient"] = value


