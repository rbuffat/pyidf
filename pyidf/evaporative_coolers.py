""" Data objects in group "Evaporative Coolers"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class EvaporativeCoolerDirectCelDekPad(DataObject):

    """ Corresponds to IDD object `EvaporativeCooler:Direct:CelDekPad`
        Direct evaporative cooler with rigid media evaporative pad and recirculating water
        pump. This model has no controls other than its availability schedule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
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
                                      (u'direct pad area',
                                       {'name': u'Direct Pad Area',
                                        'pyname': u'direct_pad_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2'}),
                                      (u'direct pad depth',
                                       {'name': u'Direct Pad Depth',
                                        'pyname': u'direct_pad_depth',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
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
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water supply storage tank name',
                                       {'name': u'Water Supply Storage Tank Name',
                                        'pyname': u'water_supply_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 0,
               'name': u'EvaporativeCooler:Direct:CelDekPad',
               'pyname': u'EvaporativeCoolerDirectCelDekPad',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def direct_pad_area(self):
        """field `Direct Pad Area`

        Args:
            value (float): value for IDD Field `Direct Pad Area`
                Units: m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `direct_pad_area` or None if not set

        """
        return self["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value=None):
        """Corresponds to IDD field `Direct Pad Area`"""
        self["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """field `Direct Pad Depth`

        Args:
            value (float): value for IDD Field `Direct Pad Depth`
                Units: m

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `direct_pad_depth` or None if not set

        """
        return self["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value=None):
        """Corresponds to IDD field `Direct Pad Depth`"""
        self["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set

        """
        return self["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Power
        Consumption`"""
        self["Recirculating Water Pump Power Consumption"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

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
    def control_type(self):
        """field `Control Type` This field is not currently used and can be
        left blank.

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def water_supply_storage_tank_name(self):
        """field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set

        """
        return self["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Supply Storage Tank Name`"""
        self["Water Supply Storage Tank Name"] = value




class EvaporativeCoolerIndirectCelDekPad(DataObject):

    """ Corresponds to IDD object `EvaporativeCooler:Indirect:CelDekPad`
        Indirect evaporative cooler with rigid media evaporative pad, recirculating water
        pump, and secondary air fan. This model has no controls other than its availability
        schedule.
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
                                      (u'direct pad area',
                                       {'name': u'Direct Pad Area',
                                        'pyname': u'direct_pad_area',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2'}),
                                      (u'direct pad depth',
                                       {'name': u'Direct Pad Depth',
                                        'pyname': u'direct_pad_depth',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'secondary fan flow rate',
                                       {'name': u'Secondary Fan Flow Rate',
                                        'pyname': u'secondary_fan_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'secondary fan total efficiency',
                                       {'name': u'Secondary Fan Total Efficiency',
                                        'pyname': u'secondary_fan_total_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'secondary fan delta pressure',
                                       {'name': u'Secondary Fan Delta Pressure',
                                        'pyname': u'secondary_fan_delta_pressure',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'Pa'}),
                                      (u'indirect heat exchanger effectiveness',
                                       {'name': u'Indirect Heat Exchanger Effectiveness',
                                        'pyname': u'indirect_heat_exchanger_effectiveness',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'primary air inlet node name',
                                       {'name': u'Primary Air Inlet Node Name',
                                        'pyname': u'primary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air outlet node name',
                                       {'name': u'Primary Air Outlet Node Name',
                                        'pyname': u'primary_air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water supply storage tank name',
                                       {'name': u'Water Supply Storage Tank Name',
                                        'pyname': u'water_supply_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 0,
               'name': u'EvaporativeCooler:Indirect:CelDekPad',
               'pyname': u'EvaporativeCoolerIndirectCelDekPad',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def direct_pad_area(self):
        """field `Direct Pad Area`

        Args:
            value (float): value for IDD Field `Direct Pad Area`
                Units: m2

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `direct_pad_area` or None if not set

        """
        return self["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value=None):
        """Corresponds to IDD field `Direct Pad Area`"""
        self["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """field `Direct Pad Depth`

        Args:
            value (float): value for IDD Field `Direct Pad Depth`
                Units: m

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `direct_pad_depth` or None if not set

        """
        return self["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value=None):
        """Corresponds to IDD field `Direct Pad Depth`"""
        self["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set

        """
        return self["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Power
        Consumption`"""
        self["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """field `Secondary Fan Flow Rate`

        Args:
            value (float): value for IDD Field `Secondary Fan Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set

        """
        return self["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """Corresponds to IDD field `Secondary Fan Flow Rate`"""
        self["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """field `Secondary Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Secondary Fan Total Efficiency`
                value <= 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set

        """
        return self["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """Corresponds to IDD field `Secondary Fan Total Efficiency`"""
        self["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """field `Secondary Fan Delta Pressure`

        Args:
            value (float): value for IDD Field `Secondary Fan Delta Pressure`
                Units: Pa
                IP-Units: inH2O

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set

        """
        return self["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """Corresponds to IDD field `Secondary Fan Delta Pressure`"""
        self["Secondary Fan Delta Pressure"] = value

    @property
    def indirect_heat_exchanger_effectiveness(self):
        """field `Indirect Heat Exchanger Effectiveness`

        Args:
            value (float): value for IDD Field `Indirect Heat Exchanger Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `indirect_heat_exchanger_effectiveness` or None if not set

        """
        return self["Indirect Heat Exchanger Effectiveness"]

    @indirect_heat_exchanger_effectiveness.setter
    def indirect_heat_exchanger_effectiveness(self, value=None):
        """Corresponds to IDD field `Indirect Heat Exchanger Effectiveness`"""
        self["Indirect Heat Exchanger Effectiveness"] = value

    @property
    def primary_air_inlet_node_name(self):
        """field `Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set

        """
        return self["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Primary Air Inlet Node Name`"""
        self["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """field `Primary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set

        """
        return self["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Primary Air Outlet Node Name`"""
        self["Primary Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """field `Control Type` This field is not currently used and can be
        left blank.

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def water_supply_storage_tank_name(self):
        """field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set

        """
        return self["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Supply Storage Tank Name`"""
        self["Water Supply Storage Tank Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """field `Secondary Air Inlet Node Name` Enter the name of an outdoor
        air node.

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




class EvaporativeCoolerIndirectWetCoil(DataObject):

    """ Corresponds to IDD object `EvaporativeCooler:Indirect:WetCoil`
        Indirect evaporative cooler with wetted coil, recirculating water pump, and secondary
        air fan. This model has no controls other than its availability schedule.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
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
                                      (u'coil maximum efficiency',
                                       {'name': u'Coil Maximum Efficiency',
                                        'pyname': u'coil_maximum_efficiency',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coil flow ratio',
                                       {'name': u'Coil Flow Ratio',
                                        'pyname': u'coil_flow_ratio',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'secondary fan flow rate',
                                       {'name': u'Secondary Fan Flow Rate',
                                        'pyname': u'secondary_fan_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'secondary fan total efficiency',
                                       {'name': u'Secondary Fan Total Efficiency',
                                        'pyname': u'secondary_fan_total_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'secondary fan delta pressure',
                                       {'name': u'Secondary Fan Delta Pressure',
                                        'pyname': u'secondary_fan_delta_pressure',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'Pa'}),
                                      (u'primary air inlet node name',
                                       {'name': u'Primary Air Inlet Node Name',
                                        'pyname': u'primary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air outlet node name',
                                       {'name': u'Primary Air Outlet Node Name',
                                        'pyname': u'primary_air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'water supply storage tank name',
                                       {'name': u'Water Supply Storage Tank Name',
                                        'pyname': u'water_supply_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 0,
               'name': u'EvaporativeCooler:Indirect:WetCoil',
               'pyname': u'EvaporativeCoolerIndirectWetCoil',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def coil_maximum_efficiency(self):
        """field `Coil Maximum Efficiency`

        Args:
            value (float): value for IDD Field `Coil Maximum Efficiency`
                value <= 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coil_maximum_efficiency` or None if not set

        """
        return self["Coil Maximum Efficiency"]

    @coil_maximum_efficiency.setter
    def coil_maximum_efficiency(self, value=None):
        """Corresponds to IDD field `Coil Maximum Efficiency`"""
        self["Coil Maximum Efficiency"] = value

    @property
    def coil_flow_ratio(self):
        """field `Coil Flow Ratio`

        Args:
            value (float): value for IDD Field `Coil Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coil_flow_ratio` or None if not set

        """
        return self["Coil Flow Ratio"]

    @coil_flow_ratio.setter
    def coil_flow_ratio(self, value=None):
        """Corresponds to IDD field `Coil Flow Ratio`"""
        self["Coil Flow Ratio"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set

        """
        return self["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Power
        Consumption`"""
        self["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """field `Secondary Fan Flow Rate`

        Args:
            value (float): value for IDD Field `Secondary Fan Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set

        """
        return self["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """Corresponds to IDD field `Secondary Fan Flow Rate`"""
        self["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """field `Secondary Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Secondary Fan Total Efficiency`
                value <= 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set

        """
        return self["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """Corresponds to IDD field `Secondary Fan Total Efficiency`"""
        self["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """field `Secondary Fan Delta Pressure`

        Args:
            value (float): value for IDD Field `Secondary Fan Delta Pressure`
                Units: Pa
                IP-Units: inH2O

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set

        """
        return self["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """Corresponds to IDD field `Secondary Fan Delta Pressure`"""
        self["Secondary Fan Delta Pressure"] = value

    @property
    def primary_air_inlet_node_name(self):
        """field `Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set

        """
        return self["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Primary Air Inlet Node Name`"""
        self["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """field `Primary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set

        """
        return self["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Primary Air Outlet Node Name`"""
        self["Primary Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """field `Control Type` This field is not currently used and can be
        left blank.

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def water_supply_storage_tank_name(self):
        """field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set

        """
        return self["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Supply Storage Tank Name`"""
        self["Water Supply Storage Tank Name"] = value

    @property
    def secondary_air_inlet_node_name(self):
        """field `Secondary Air Inlet Node Name` Enter the name of an outdoor
        air node.

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




class EvaporativeCoolerIndirectResearchSpecial(DataObject):

    """ Corresponds to IDD object `EvaporativeCooler:Indirect:ResearchSpecial`
        Indirect evaporative cooler with user-specified effectiveness (can represent rigid pad
        or wetted coil), recirculating water pump, and secondary air fan. This model is
        controlled to meet the primary air outlet temperature setpoint.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
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
                                      (u'cooler maximum effectiveness',
                                       {'name': u'Cooler Maximum Effectiveness',
                                        'pyname': u'cooler_maximum_effectiveness',
                                        'maximum': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooler flow ratio',
                                       {'name': u'Cooler Flow Ratio',
                                        'pyname': u'cooler_flow_ratio',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'secondary fan flow rate',
                                       {'name': u'Secondary Fan Flow Rate',
                                        'pyname': u'secondary_fan_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'secondary fan total efficiency',
                                       {'name': u'Secondary Fan Total Efficiency',
                                        'pyname': u'secondary_fan_total_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'secondary fan delta pressure',
                                       {'name': u'Secondary Fan Delta Pressure',
                                        'pyname': u'secondary_fan_delta_pressure',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'Pa'}),
                                      (u'primary air inlet node name',
                                       {'name': u'Primary Air Inlet Node Name',
                                        'pyname': u'primary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air outlet node name',
                                       {'name': u'Primary Air Outlet Node Name',
                                        'pyname': u'primary_air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'control type',
                                       {'name': u'Control Type',
                                        'pyname': u'control_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dewpoint effectiveness factor',
                                       {'name': u'Dewpoint Effectiveness Factor',
                                        'pyname': u'dewpoint_effectiveness_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'relief air inlet node name',
                                       {'name': u'Relief Air Inlet Node Name',
                                        'pyname': u'relief_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water supply storage tank name',
                                       {'name': u'Water Supply Storage Tank Name',
                                        'pyname': u'water_supply_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'drift loss fraction',
                                       {'name': u'Drift Loss Fraction',
                                        'pyname': u'drift_loss_fraction',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'blowdown concentration ratio',
                                       {'name': u'Blowdown Concentration Ratio',
                                        'pyname': u'blowdown_concentration_ratio',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 0,
               'name': u'EvaporativeCooler:Indirect:ResearchSpecial',
               'pyname': u'EvaporativeCoolerIndirectResearchSpecial',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def cooler_maximum_effectiveness(self):
        """field `Cooler Maximum Effectiveness`

        Args:
            value (float): value for IDD Field `Cooler Maximum Effectiveness`
                value <= 2.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooler_maximum_effectiveness` or None if not set

        """
        return self["Cooler Maximum Effectiveness"]

    @cooler_maximum_effectiveness.setter
    def cooler_maximum_effectiveness(self, value=None):
        """Corresponds to IDD field `Cooler Maximum Effectiveness`"""
        self["Cooler Maximum Effectiveness"] = value

    @property
    def cooler_flow_ratio(self):
        """field `Cooler Flow Ratio`

        Args:
            value (float): value for IDD Field `Cooler Flow Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooler_flow_ratio` or None if not set

        """
        return self["Cooler Flow Ratio"]

    @cooler_flow_ratio.setter
    def cooler_flow_ratio(self, value=None):
        """Corresponds to IDD field `Cooler Flow Ratio`"""
        self["Cooler Flow Ratio"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set

        """
        return self["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Power
        Consumption`"""
        self["Recirculating Water Pump Power Consumption"] = value

    @property
    def secondary_fan_flow_rate(self):
        """field `Secondary Fan Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Secondary Fan Flow Rate`
                Units: m3/s

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_flow_rate` or None if not set

        """
        return self["Secondary Fan Flow Rate"]

    @secondary_fan_flow_rate.setter
    def secondary_fan_flow_rate(self, value=None):
        """Corresponds to IDD field `Secondary Fan Flow Rate`"""
        self["Secondary Fan Flow Rate"] = value

    @property
    def secondary_fan_total_efficiency(self):
        """field `Secondary Fan Total Efficiency`

        Args:
            value (float): value for IDD Field `Secondary Fan Total Efficiency`
                value <= 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_total_efficiency` or None if not set

        """
        return self["Secondary Fan Total Efficiency"]

    @secondary_fan_total_efficiency.setter
    def secondary_fan_total_efficiency(self, value=None):
        """Corresponds to IDD field `Secondary Fan Total Efficiency`"""
        self["Secondary Fan Total Efficiency"] = value

    @property
    def secondary_fan_delta_pressure(self):
        """field `Secondary Fan Delta Pressure`

        Args:
            value (float): value for IDD Field `Secondary Fan Delta Pressure`
                Units: Pa
                IP-Units: inH2O

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_fan_delta_pressure` or None if not set

        """
        return self["Secondary Fan Delta Pressure"]

    @secondary_fan_delta_pressure.setter
    def secondary_fan_delta_pressure(self, value=None):
        """Corresponds to IDD field `Secondary Fan Delta Pressure`"""
        self["Secondary Fan Delta Pressure"] = value

    @property
    def primary_air_inlet_node_name(self):
        """field `Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_inlet_node_name` or None if not set

        """
        return self["Primary Air Inlet Node Name"]

    @primary_air_inlet_node_name.setter
    def primary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Primary Air Inlet Node Name`"""
        self["Primary Air Inlet Node Name"] = value

    @property
    def primary_air_outlet_node_name(self):
        """field `Primary Air Outlet Node Name`

        Args:
            value (str): value for IDD Field `Primary Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_outlet_node_name` or None if not set

        """
        return self["Primary Air Outlet Node Name"]

    @primary_air_outlet_node_name.setter
    def primary_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Primary Air Outlet Node Name`"""
        self["Primary Air Outlet Node Name"] = value

    @property
    def control_type(self):
        """field `Control Type`

        Args:
            value (str): value for IDD Field `Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_type` or None if not set

        """
        return self["Control Type"]

    @control_type.setter
    def control_type(self, value=None):
        """Corresponds to IDD field `Control Type`"""
        self["Control Type"] = value

    @property
    def dewpoint_effectiveness_factor(self):
        """field `Dewpoint Effectiveness Factor`

        Args:
            value (float): value for IDD Field `Dewpoint Effectiveness Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_effectiveness_factor` or None if not set

        """
        return self["Dewpoint Effectiveness Factor"]

    @dewpoint_effectiveness_factor.setter
    def dewpoint_effectiveness_factor(self, value=None):
        """Corresponds to IDD field `Dewpoint Effectiveness Factor`"""
        self["Dewpoint Effectiveness Factor"] = value

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
    def sensor_node_name(self):
        """field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sensor_node_name` or None if not set

        """
        return self["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """Corresponds to IDD field `Sensor Node Name`"""
        self["Sensor Node Name"] = value

    @property
    def relief_air_inlet_node_name(self):
        """field `Relief Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Relief Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `relief_air_inlet_node_name` or None if not set

        """
        return self["Relief Air Inlet Node Name"]

    @relief_air_inlet_node_name.setter
    def relief_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Relief Air Inlet Node Name`"""
        self["Relief Air Inlet Node Name"] = value

    @property
    def water_supply_storage_tank_name(self):
        """field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set

        """
        return self["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Supply Storage Tank Name`"""
        self["Water Supply Storage Tank Name"] = value

    @property
    def drift_loss_fraction(self):
        """field `Drift Loss Fraction` Rate of drift loss as a fraction of
        evaporated water flow rate.

        Args:
            value (float): value for IDD Field `Drift Loss Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drift_loss_fraction` or None if not set

        """
        return self["Drift Loss Fraction"]

    @drift_loss_fraction.setter
    def drift_loss_fraction(self, value=None):
        """Corresponds to IDD field `Drift Loss Fraction`"""
        self["Drift Loss Fraction"] = value

    @property
    def blowdown_concentration_ratio(self):
        """field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the evaporative cooler.
        Blowdown is water intentionally drained from the cooler in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        A typical value is 3.  If left blank then there is no blowdown.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                value >= 2.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=None):
        """Corresponds to IDD field `Blowdown Concentration Ratio`"""
        self["Blowdown Concentration Ratio"] = value




class EvaporativeCoolerDirectResearchSpecial(DataObject):

    """ Corresponds to IDD object `EvaporativeCooler:Direct:ResearchSpecial`
        Direct evaporative cooler with user-specified effectiveness (can represent rigid pad
        or similar media), and recirculating water pump, and secondary air fan. This model is
        controlled to meet the primary air outlet temperature setpoint.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': False,
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
                                      (u'cooler effectiveness',
                                       {'name': u'Cooler Effectiveness',
                                        'pyname': u'cooler_effectiveness',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
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
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water supply storage tank name',
                                       {'name': u'Water Supply Storage Tank Name',
                                        'pyname': u'water_supply_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'drift loss fraction',
                                       {'name': u'Drift Loss Fraction',
                                        'pyname': u'drift_loss_fraction',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'blowdown concentration ratio',
                                       {'name': u'Blowdown Concentration Ratio',
                                        'pyname': u'blowdown_concentration_ratio',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 0,
               'name': u'EvaporativeCooler:Direct:ResearchSpecial',
               'pyname': u'EvaporativeCoolerDirectResearchSpecial',
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
        """field `Availability Schedule Name` Availability schedule name for
        this system. Schedule value > 0 means the system is available. If this
        field is blank, the system is always available.

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
    def cooler_effectiveness(self):
        """field `Cooler Effectiveness` effectiveness with respect to wetbulb
        depression.

        Args:
            value (float): value for IDD Field `Cooler Effectiveness`
                value <= 1.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooler_effectiveness` or None if not set

        """
        return self["Cooler Effectiveness"]

    @cooler_effectiveness.setter
    def cooler_effectiveness(self, value=None):
        """Corresponds to IDD field `Cooler Effectiveness`"""
        self["Cooler Effectiveness"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`
                Units: W
                IP-Units: W

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `recirculating_water_pump_power_consumption` or None if not set

        """
        return self["Recirculating Water Pump Power Consumption"]

    @recirculating_water_pump_power_consumption.setter
    def recirculating_water_pump_power_consumption(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Power
        Consumption`"""
        self["Recirculating Water Pump Power Consumption"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

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
    def sensor_node_name(self):
        """field `Sensor Node Name`

        Args:
            value (str): value for IDD Field `Sensor Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `sensor_node_name` or None if not set

        """
        return self["Sensor Node Name"]

    @sensor_node_name.setter
    def sensor_node_name(self, value=None):
        """Corresponds to IDD field `Sensor Node Name`"""
        self["Sensor Node Name"] = value

    @property
    def water_supply_storage_tank_name(self):
        """field `Water Supply Storage Tank Name`

        Args:
            value (str): value for IDD Field `Water Supply Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_supply_storage_tank_name` or None if not set

        """
        return self["Water Supply Storage Tank Name"]

    @water_supply_storage_tank_name.setter
    def water_supply_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Water Supply Storage Tank Name`"""
        self["Water Supply Storage Tank Name"] = value

    @property
    def drift_loss_fraction(self):
        """field `Drift Loss Fraction` Rate of drift loss as a fraction of
        evaporated water flow rate.

        Args:
            value (float): value for IDD Field `Drift Loss Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drift_loss_fraction` or None if not set

        """
        return self["Drift Loss Fraction"]

    @drift_loss_fraction.setter
    def drift_loss_fraction(self, value=None):
        """Corresponds to IDD field `Drift Loss Fraction`"""
        self["Drift Loss Fraction"] = value

    @property
    def blowdown_concentration_ratio(self):
        """field `Blowdown Concentration Ratio`
        Characterizes the rate of blowdown in the evaporative cooler.
        Blowdown is water intentionally drained from the cooler in order to offset the build up
        of solids in the water that would otherwise occur because of evaporation.
        Ratio of solids in the blowdown water to solids in the make up water.
        A typical value is 3. If left blank then there is no blowdown.

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`
                value >= 2.0

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `blowdown_concentration_ratio` or None if not set
        """
        return self["Blowdown Concentration Ratio"]

    @blowdown_concentration_ratio.setter
    def blowdown_concentration_ratio(self, value=None):
        """Corresponds to IDD field `Blowdown Concentration Ratio`"""
        self["Blowdown Concentration Ratio"] = value


