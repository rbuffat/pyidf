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
                                        'default': 'Autosize',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm2'}),
                                      (u'direct pad depth',
                                       {'name': u'Direct Pad Depth',
                                        'pyname': u'direct_pad_depth',
                                        'default': 'Autosize',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
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
               'min-fields': 7,
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
    def direct_pad_area(self):
        """field `Direct Pad Area`

        |  Units: m2
        |  Default value: "Autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Direct Pad Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `direct_pad_area` or None if not set

        """
        return self["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value="Autosize"):
        """Corresponds to IDD field `Direct Pad Area`"""
        self["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """field `Direct Pad Depth`

        |  Units: m
        |  Default value: "Autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Direct Pad Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `direct_pad_depth` or None if not set

        """
        return self["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value="Autosize"):
        """Corresponds to IDD field `Direct Pad Depth`"""
        self["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`

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
        """field `Control Type`

        |  This field is not currently used and can be left blank

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
                                        'default': 'Autosize',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2'}),
                                      (u'direct pad depth',
                                       {'name': u'Direct Pad Depth',
                                        'pyname': u'direct_pad_depth',
                                        'default': 'Autosize',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'recirculating water pump power consumption',
                                       {'name': u'Recirculating Water Pump Power Consumption',
                                        'pyname': u'recirculating_water_pump_power_consumption',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'secondary air fan flow rate',
                                       {'name': u'Secondary Air Fan Flow Rate',
                                        'pyname': u'secondary_air_fan_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'secondary air fan total efficiency',
                                       {'name': u'Secondary Air Fan Total Efficiency',
                                        'pyname': u'secondary_air_fan_total_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'secondary air fan delta pressure',
                                       {'name': u'Secondary Air Fan Delta Pressure',
                                        'pyname': u'secondary_air_fan_delta_pressure',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'indirect heat exchanger effectiveness',
                                       {'name': u'Indirect Heat Exchanger Effectiveness',
                                        'pyname': u'indirect_heat_exchanger_effectiveness',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'primary air inlet node name',
                                       {'name': u'Primary Air Inlet Node Name',
                                        'pyname': u'primary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air outlet node name',
                                       {'name': u'Primary Air Outlet Node Name',
                                        'pyname': u'primary_air_outlet_node_name',
                                        'required-field': True,
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
               'min-fields': 14,
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
    def direct_pad_area(self):
        """field `Direct Pad Area`

        |  Units: m2
        |  Default value: "Autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Direct Pad Area`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `direct_pad_area` or None if not set

        """
        return self["Direct Pad Area"]

    @direct_pad_area.setter
    def direct_pad_area(self, value="Autosize"):
        """Corresponds to IDD field `Direct Pad Area`"""
        self["Direct Pad Area"] = value

    @property
    def direct_pad_depth(self):
        """field `Direct Pad Depth`

        |  Units: m
        |  Default value: "Autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Direct Pad Depth`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `direct_pad_depth` or None if not set

        """
        return self["Direct Pad Depth"]

    @direct_pad_depth.setter
    def direct_pad_depth(self, value="Autosize"):
        """Corresponds to IDD field `Direct Pad Depth`"""
        self["Direct Pad Depth"] = value

    @property
    def recirculating_water_pump_power_consumption(self):
        """field `Recirculating Water Pump Power Consumption`

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`

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
    def secondary_air_fan_flow_rate(self):
        """field `Secondary Air Fan Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Secondary Air Fan Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_flow_rate` or None if not set

        """
        return self["Secondary Air Fan Flow Rate"]

    @secondary_air_fan_flow_rate.setter
    def secondary_air_fan_flow_rate(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Flow Rate`"""
        self["Secondary Air Fan Flow Rate"] = value

    @property
    def secondary_air_fan_total_efficiency(self):
        """field `Secondary Air Fan Total Efficiency`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Secondary Air Fan Total Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_total_efficiency` or None if not set

        """
        return self["Secondary Air Fan Total Efficiency"]

    @secondary_air_fan_total_efficiency.setter
    def secondary_air_fan_total_efficiency(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Total Efficiency`"""
        self["Secondary Air Fan Total Efficiency"] = value

    @property
    def secondary_air_fan_delta_pressure(self):
        """field `Secondary Air Fan Delta Pressure`

        |  Units: Pa
        |  IP-Units: inH2O

        Args:
            value (float): value for IDD Field `Secondary Air Fan Delta Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_delta_pressure` or None if not set

        """
        return self["Secondary Air Fan Delta Pressure"]

    @secondary_air_fan_delta_pressure.setter
    def secondary_air_fan_delta_pressure(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Delta Pressure`"""
        self["Secondary Air Fan Delta Pressure"] = value

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
        """field `Control Type`

        |  This field is not currently used and can be left blank

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
        """field `Secondary Air Inlet Node Name`

        |  Enter the name of an outdoor air node

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
                                      (u'coil maximum efficiency',
                                       {'name': u'Coil Maximum Efficiency',
                                        'pyname': u'coil_maximum_efficiency',
                                        'maximum': 1.0,
                                        'required-field': True,
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
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'secondary air fan flow rate',
                                       {'name': u'Secondary Air Fan Flow Rate',
                                        'pyname': u'secondary_air_fan_flow_rate',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'secondary air fan total efficiency',
                                       {'name': u'Secondary Air Fan Total Efficiency',
                                        'pyname': u'secondary_air_fan_total_efficiency',
                                        'minimum>': 0.0,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'secondary air fan delta pressure',
                                       {'name': u'Secondary Air Fan Delta Pressure',
                                        'pyname': u'secondary_air_fan_delta_pressure',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'Pa'}),
                                      (u'primary air inlet node name',
                                       {'name': u'Primary Air Inlet Node Name',
                                        'pyname': u'primary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air outlet node name',
                                       {'name': u'Primary Air Outlet Node Name',
                                        'pyname': u'primary_air_outlet_node_name',
                                        'required-field': True,
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
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 13,
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
    def coil_maximum_efficiency(self):
        """field `Coil Maximum Efficiency`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Coil Maximum Efficiency`

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

        |  Units: W
        |  IP-Units: W

        Args:
            value (float): value for IDD Field `Recirculating Water Pump Power Consumption`

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
    def secondary_air_fan_flow_rate(self):
        """field `Secondary Air Fan Flow Rate`

        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Secondary Air Fan Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_flow_rate` or None if not set

        """
        return self["Secondary Air Fan Flow Rate"]

    @secondary_air_fan_flow_rate.setter
    def secondary_air_fan_flow_rate(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Flow Rate`"""
        self["Secondary Air Fan Flow Rate"] = value

    @property
    def secondary_air_fan_total_efficiency(self):
        """field `Secondary Air Fan Total Efficiency`

        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Secondary Air Fan Total Efficiency`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_total_efficiency` or None if not set

        """
        return self["Secondary Air Fan Total Efficiency"]

    @secondary_air_fan_total_efficiency.setter
    def secondary_air_fan_total_efficiency(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Total Efficiency`"""
        self["Secondary Air Fan Total Efficiency"] = value

    @property
    def secondary_air_fan_delta_pressure(self):
        """field `Secondary Air Fan Delta Pressure`

        |  Units: Pa
        |  IP-Units: inH2O

        Args:
            value (float): value for IDD Field `Secondary Air Fan Delta Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_delta_pressure` or None if not set

        """
        return self["Secondary Air Fan Delta Pressure"]

    @secondary_air_fan_delta_pressure.setter
    def secondary_air_fan_delta_pressure(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Delta Pressure`"""
        self["Secondary Air Fan Delta Pressure"] = value

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

        |  This field is not currently used and can be left blank

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
        """field `Secondary Air Inlet Node Name`

        |  Enter the name of an outdoor air node

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
                                      (u'cooler wetbulb design effectiveness',
                                       {'name': u'Cooler Wetbulb Design Effectiveness',
                                        'pyname': u'cooler_wetbulb_design_effectiveness',
                                        'maximum': 2.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'wetbulb effectiveness flow ratio modifier curve name',
                                       {'name': u'Wetbulb Effectiveness Flow Ratio Modifier Curve Name',
                                        'pyname': u'wetbulb_effectiveness_flow_ratio_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooler drybulb design effectiveness',
                                       {'name': u'Cooler Drybulb Design Effectiveness',
                                        'pyname': u'cooler_drybulb_design_effectiveness',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'drybulb effectiveness flow ratio modifier curve name',
                                       {'name': u'Drybulb Effectiveness Flow Ratio Modifier Curve Name',
                                        'pyname': u'drybulb_effectiveness_flow_ratio_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'recirculating water pump design power',
                                       {'name': u'Recirculating Water Pump Design Power',
                                        'pyname': u'recirculating_water_pump_design_power',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'water pump power sizing factor',
                                       {'name': u'Water Pump Power Sizing Factor',
                                        'pyname': u'water_pump_power_sizing_factor',
                                        'default': 90.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/(m3/s)'}),
                                      (u'water pump power modifier curve name',
                                       {'name': u'Water Pump Power Modifier Curve Name',
                                        'pyname': u'water_pump_power_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'secondary air design flow rate',
                                       {'name': u'Secondary Air Design Flow Rate',
                                        'pyname': u'secondary_air_design_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'secondary air flow scaling factor',
                                       {'name': u'Secondary Air Flow Scaling Factor',
                                        'pyname': u'secondary_air_flow_scaling_factor',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'secondary air fan design power',
                                       {'name': u'Secondary Air Fan Design Power',
                                        'pyname': u'secondary_air_fan_design_power',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'secondary air fan sizing specific power',
                                       {'name': u'Secondary Air Fan Sizing Specific Power',
                                        'pyname': u'secondary_air_fan_sizing_specific_power',
                                        'default': 250.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/(m3/s)'}),
                                      (u'secondary air fan power modifier curve name',
                                       {'name': u'Secondary Air Fan Power Modifier Curve Name',
                                        'pyname': u'secondary_air_fan_power_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'primary air inlet node name',
                                       {'name': u'Primary Air Inlet Node Name',
                                        'pyname': u'primary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air outlet node name',
                                       {'name': u'Primary Air Outlet Node Name',
                                        'pyname': u'primary_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'primary air design flow rate',
                                       {'name': u'Primary Air Design Flow Rate',
                                        'pyname': u'primary_air_design_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'dewpoint effectiveness factor',
                                       {'name': u'Dewpoint Effectiveness Factor',
                                        'pyname': u'dewpoint_effectiveness_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
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
                                        'type': u'node'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
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
                                        'default': 0.0,
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
                                        'type': u'real'}),
                                      (u'evaporative operation minimum limit secondary air drybulb temperature',
                                       {'name': u'Evaporative Operation Minimum Limit Secondary Air Drybulb Temperature',
                                        'pyname': u'evaporative_operation_minimum_limit_secondary_air_drybulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'evaporative operation maximum limit outdoor wetbulb temperature',
                                       {'name': u'Evaporative Operation Maximum Limit Outdoor Wetbulb Temperature',
                                        'pyname': u'evaporative_operation_maximum_limit_outdoor_wetbulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'dry operation maximum limit outdoor drybulb temperature',
                                       {'name': u'Dry Operation Maximum Limit Outdoor Drybulb Temperature',
                                        'pyname': u'dry_operation_maximum_limit_outdoor_drybulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 21,
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
    def cooler_wetbulb_design_effectiveness(self):
        """field `Cooler Wetbulb Design Effectiveness`

        |  wet operation effectiveness with respect to wetbulb depression
        |  this is the nominal design wetbulb effectiveness at design air flow rates and water rate
        |  value <= 2.0

        Args:
            value (float): value for IDD Field `Cooler Wetbulb Design Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooler_wetbulb_design_effectiveness` or None if not set

        """
        return self["Cooler Wetbulb Design Effectiveness"]

    @cooler_wetbulb_design_effectiveness.setter
    def cooler_wetbulb_design_effectiveness(self, value=None):
        """Corresponds to IDD field `Cooler Wetbulb Design Effectiveness`"""
        self["Cooler Wetbulb Design Effectiveness"] = value

    @property
    def wetbulb_effectiveness_flow_ratio_modifier_curve_name(self):
        """field `Wetbulb Effectiveness Flow Ratio Modifier Curve Name`

        |  this curve modifies the wetbulb effectiveness in the previous field (eff_wb_design)
        |  by multiplying the value by the result of this curve, eff_wb = eff_wb_design * func(HXFlowRatio)
        |  x = HXFlowRatio = sum of the primary and secondary flow rates divided by the sum of the design flow
        |  rates. If this input field is left blank, constant cooler wetbulb effectiveness is assumed.
        |  Any curve or table with one independent variable can be used:
        |  Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        |  Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        |  Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        |  Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Wetbulb Effectiveness Flow Ratio Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `wetbulb_effectiveness_flow_ratio_modifier_curve_name` or None if not set

        """
        return self["Wetbulb Effectiveness Flow Ratio Modifier Curve Name"]

    @wetbulb_effectiveness_flow_ratio_modifier_curve_name.setter
    def wetbulb_effectiveness_flow_ratio_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Wetbulb Effectiveness Flow Ratio Modifier
        Curve Name`"""
        self["Wetbulb Effectiveness Flow Ratio Modifier Curve Name"] = value

    @property
    def cooler_drybulb_design_effectiveness(self):
        """field `Cooler Drybulb Design Effectiveness`

        |  dry operation effectiveness with respect to drybulb temperature difference
        |  this is the nominal design dryblub effectiveness at design air flow rates, no evaporation water active

        Args:
            value (float): value for IDD Field `Cooler Drybulb Design Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooler_drybulb_design_effectiveness` or None if not set

        """
        return self["Cooler Drybulb Design Effectiveness"]

    @cooler_drybulb_design_effectiveness.setter
    def cooler_drybulb_design_effectiveness(self, value=None):
        """Corresponds to IDD field `Cooler Drybulb Design Effectiveness`"""
        self["Cooler Drybulb Design Effectiveness"] = value

    @property
    def drybulb_effectiveness_flow_ratio_modifier_curve_name(self):
        """field `Drybulb Effectiveness Flow Ratio Modifier Curve Name`

        |  this curve modifies the drybulb effectiveness in the previous field (eff_db_design)
        |  by multiplying the value by the result of this curve, eff_db = eff_db_design * f(HXFlowRatio)
        |  x = HXFlowRatio = sum of the primary and secondary flow rates divided by the sum of the design flow
        |  rates. If this input field is left blank, constant cooler drybulb effectiveness is assumed.
        |  Any curve or table with one independent variable can be used:
        |  Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        |  Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        |  Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        |  Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Drybulb Effectiveness Flow Ratio Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `drybulb_effectiveness_flow_ratio_modifier_curve_name` or None if not set

        """
        return self["Drybulb Effectiveness Flow Ratio Modifier Curve Name"]

    @drybulb_effectiveness_flow_ratio_modifier_curve_name.setter
    def drybulb_effectiveness_flow_ratio_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Drybulb Effectiveness Flow Ratio Modifier
        Curve Name`"""
        self["Drybulb Effectiveness Flow Ratio Modifier Curve Name"] = value

    @property
    def recirculating_water_pump_design_power(self):
        """field `Recirculating Water Pump Design Power`

        |  This is the nominal design pump power of water recirculation and spray for evaporation at design air flow
        |  rates and cooler design effectiveness
        |  Units: W
        |  IP-Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Recirculating Water Pump Design Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `recirculating_water_pump_design_power` or None if not set

        """
        return self["Recirculating Water Pump Design Power"]

    @recirculating_water_pump_design_power.setter
    def recirculating_water_pump_design_power(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Design Power`"""
        self["Recirculating Water Pump Design Power"] = value

    @property
    def water_pump_power_sizing_factor(self):
        """field `Water Pump Power Sizing Factor`

        |  This field is used when the previous field is set to autosize. The pump power is scaled with Secondary Air
        |  Design Air Flow Rate. This value was backed out from inputs in energy plus example files. Average Pump Power
        |  sizing factor was estimated from pump power and secondary air design flow rates inputs from energyplus example
        |  files is about 90.0 [W/(m3/s)] (=90.0 ~ Pump Power / Secondary Air Design Flow Rate). The factor ranges from
        |  55.0 to 150.0 [W/(m3/s)] were noted.
        |  Units: W/(m3/s)
        |  Default value: 90.0

        Args:
            value (float): value for IDD Field `Water Pump Power Sizing Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_pump_power_sizing_factor` or None if not set

        """
        return self["Water Pump Power Sizing Factor"]

    @water_pump_power_sizing_factor.setter
    def water_pump_power_sizing_factor(self, value=90.0):
        """Corresponds to IDD field `Water Pump Power Sizing Factor`"""
        self["Water Pump Power Sizing Factor"] = value

    @property
    def water_pump_power_modifier_curve_name(self):
        """field `Water Pump Power Modifier Curve Name`

        |  this curve modifies the pump power in the previous field by multiplying the design power by the result of this curve.
        |  x = ff = flow fraction on the secondary side, secondary air flow rate during operation divided by Secondary Air
        |  Design Air Flow Rate. If this input field is left blank, pump power is assumed to be proportional to part load ratio.
        |  Any curve or table with one independent variable can be used:
        |  Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        |  Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        |  Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        |  Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Water Pump Power Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_pump_power_modifier_curve_name` or None if not set

        """
        return self["Water Pump Power Modifier Curve Name"]

    @water_pump_power_modifier_curve_name.setter
    def water_pump_power_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Water Pump Power Modifier Curve Name`"""
        self["Water Pump Power Modifier Curve Name"] = value

    @property
    def secondary_air_design_flow_rate(self):
        """field `Secondary Air Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Secondary Air Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `secondary_air_design_flow_rate` or None if not set

        """
        return self["Secondary Air Design Flow Rate"]

    @secondary_air_design_flow_rate.setter
    def secondary_air_design_flow_rate(self, value=None):
        """Corresponds to IDD field `Secondary Air Design Flow Rate`"""
        self["Secondary Air Design Flow Rate"] = value

    @property
    def secondary_air_flow_scaling_factor(self):
        """field `Secondary Air Flow Scaling Factor`

        |  This field is used when the previous field is set to autoize.  The Primary Design Air Flow Rate is scaled using this factor
        |  to calculate the secondary design air flow rate.
        |  Units: dimensionless
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Secondary Air Flow Scaling Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_flow_scaling_factor` or None if not set

        """
        return self["Secondary Air Flow Scaling Factor"]

    @secondary_air_flow_scaling_factor.setter
    def secondary_air_flow_scaling_factor(self, value=1.0):
        """Corresponds to IDD field `Secondary Air Flow Scaling Factor`"""
        self["Secondary Air Flow Scaling Factor"] = value

    @property
    def secondary_air_fan_design_power(self):
        """field `Secondary Air Fan Design Power`

        |  This is the fan design power at Secondary Design Air Flow Rate. This is the nominal design power at full speed.
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Secondary Air Fan Design Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `secondary_air_fan_design_power` or None if not set

        """
        return self["Secondary Air Fan Design Power"]

    @secondary_air_fan_design_power.setter
    def secondary_air_fan_design_power(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Design Power`"""
        self["Secondary Air Fan Design Power"] = value

    @property
    def secondary_air_fan_sizing_specific_power(self):
        """field `Secondary Air Fan Sizing Specific Power`

        |  This field is used when the previous field is set to autosize. The fan power is scaled with Secondary Air Design Flow Rate.
        |  The default value is estimated from 125 Pa fan total pressure and fan total efficiency of 50.0% (250.0 = 125/0.5).
        |  Units: W/(m3/s)
        |  Default value: 250.0

        Args:
            value (float): value for IDD Field `Secondary Air Fan Sizing Specific Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `secondary_air_fan_sizing_specific_power` or None if not set

        """
        return self["Secondary Air Fan Sizing Specific Power"]

    @secondary_air_fan_sizing_specific_power.setter
    def secondary_air_fan_sizing_specific_power(self, value=250.0):
        """Corresponds to IDD field `Secondary Air Fan Sizing Specific
        Power`"""
        self["Secondary Air Fan Sizing Specific Power"] = value

    @property
    def secondary_air_fan_power_modifier_curve_name(self):
        """field `Secondary Air Fan Power Modifier Curve Name`

        |  this curve modifies the design fan power in the previous field by multiplying the value by the result
        |  of this curve.  It should have a value of 1.0 at a x = 1.0.
        |  x = ff = flow fraction on the secondary side, secondary air flow rate during operation divided by Secondary Air Design Air
        |  Flow Rate. If this input field is left blank, the secondary fan power is assumed to be proportional to part load ratio.
        |  Any curve or table with one independent variable can be used:
        |  Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        |  Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        |  Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        |  Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Secondary Air Fan Power Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `secondary_air_fan_power_modifier_curve_name` or None if not set

        """
        return self["Secondary Air Fan Power Modifier Curve Name"]

    @secondary_air_fan_power_modifier_curve_name.setter
    def secondary_air_fan_power_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Secondary Air Fan Power Modifier Curve
        Name`"""
        self["Secondary Air Fan Power Modifier Curve Name"] = value

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
    def primary_air_design_flow_rate(self):
        """field `Primary Air Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Primary Air Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `primary_air_design_flow_rate` or None if not set

        """
        return self["Primary Air Design Flow Rate"]

    @primary_air_design_flow_rate.setter
    def primary_air_design_flow_rate(self, value=None):
        """Corresponds to IDD field `Primary Air Design Flow Rate`"""
        self["Primary Air Design Flow Rate"] = value

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
        """field `Drift Loss Fraction`

        |  Rate of drift loss as a fraction of evaporated water flow rate.
        |  If this input field is left blank, then zero drift loss is assumed.

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

        |  Characterizes the rate of blowdown in the evaporative cooler.
        |  Blowdown is water intentionally drained from the cooler in order to offset the build
        |  up of solids in the water that would otherwise occur because of evaporation.
        |  Ratio of solids in the blowdown water to solids in the make up water.
        |  A typical value is 3.  If left blank then there is no blowdown.
        |  value >= 2.0

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`

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

    @property
    def evaporative_operation_minimum_limit_secondary_air_drybulb_temperature(
            self):
        """field `Evaporative Operation Minimum Limit Secondary Air Drybulb
        Temperature`

        |  This input field value defines the secondary air inlet node drybulb temperature
        |  limits in degreeCelsius. When the secondary side entering air dry bulb temperature
        |  drops below this limit, then the evaporative cooler operation mode changes to dry
        |  heat exchanger. Users specify their own limits. If this field is left blank, then
        |  there is no drybulb temperature lower limit for evaporative cooler operation. If
        |  operating range control is desired then this input field and the next two input
        |  fields should be specified or all the three should be left blank or left out. If
        |  no minimum drybulb temperature limit is desired while there are maximum drybulb
        |  and wetbulb temperature limits then specify very low minimum temperature limit
        |  value (e.g. -99.0C).

        Args:
            value (float): value for IDD Field `Evaporative Operation Minimum Limit Secondary Air Drybulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_operation_minimum_limit_secondary_air_drybulb_temperature` or None if not set

        """
        return self[
            "Evaporative Operation Minimum Limit Secondary Air Drybulb Temperature"]

    @evaporative_operation_minimum_limit_secondary_air_drybulb_temperature.setter
    def evaporative_operation_minimum_limit_secondary_air_drybulb_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Evaporative Operation Minimum Limit
        Secondary Air Drybulb Temperature`"""
        self[
            "Evaporative Operation Minimum Limit Secondary Air Drybulb Temperature"] = value

    @property
    def evaporative_operation_maximum_limit_outdoor_wetbulb_temperature(self):
        """field `Evaporative Operation Maximum Limit Outdoor Wetbulb
        Temperature`

        |  This input field value defines the secondary air inlet node wetbulb temperature
        |  limits in degree Celsius. When the secondary side entering air wet bulb temperature
        |  exceeds this limit, then the evaporative cooler urns off and does not attempt to do
        |  any cooling. If this field is left blank, then there is no wetbulb temperature
        |  upper limit for evaporative cooler wet operation mode. If this input field is left
        |  blank then, the previous and the next input fields should also be left blank. If no
        |  maximum wetbulb temperature limits is desired while there are minimum drybulb and
        |  maximum drybulb upper temperature limits then specify very high maximum wetbulb
        |  temperature limit value (e.g. 99.0 C).

        Args:
            value (float): value for IDD Field `Evaporative Operation Maximum Limit Outdoor Wetbulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_operation_maximum_limit_outdoor_wetbulb_temperature` or None if not set

        """
        return self[
            "Evaporative Operation Maximum Limit Outdoor Wetbulb Temperature"]

    @evaporative_operation_maximum_limit_outdoor_wetbulb_temperature.setter
    def evaporative_operation_maximum_limit_outdoor_wetbulb_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Evaporative Operation Maximum Limit
        Outdoor Wetbulb Temperature`"""
        self[
            "Evaporative Operation Maximum Limit Outdoor Wetbulb Temperature"] = value

    @property
    def dry_operation_maximum_limit_outdoor_drybulb_temperature(self):
        """field `Dry Operation Maximum Limit Outdoor Drybulb Temperature`

        |  This input field value defines the secondary air inlet node drybulb temperature
        |  limits in degree Celsius. When the secondary side entering air drybulb temperature
        |  exceeds this limit, then the evaporative cooler will not run in dry operation mode
        |  or may be turned off depending on its wetbulb temperature. If this field is left
        |  blank, then there is no drybulb temperature maximum limit for evaporative cooler
        |  operation. If this input field is left blank then, the previous and the next input
        |  fields should also be left blank. If no maximum drybulb temperature limit is
        |  desired while there are minimum drybulb and maximum wetbulb upper temperature
        |  limits then specify very high maximum drybulb temperature limit value (e.g. 99.0 C).

        Args:
            value (float): value for IDD Field `Dry Operation Maximum Limit Outdoor Drybulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dry_operation_maximum_limit_outdoor_drybulb_temperature` or None if not set

        """
        return self["Dry Operation Maximum Limit Outdoor Drybulb Temperature"]

    @dry_operation_maximum_limit_outdoor_drybulb_temperature.setter
    def dry_operation_maximum_limit_outdoor_drybulb_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Dry Operation Maximum Limit Outdoor
        Drybulb Temperature`"""
        self["Dry Operation Maximum Limit Outdoor Drybulb Temperature"] = value




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
                                      (u'cooler design effectiveness',
                                       {'name': u'Cooler Design Effectiveness',
                                        'pyname': u'cooler_design_effectiveness',
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'effectiveness flow ratio modifier curve name',
                                       {'name': u'Effectiveness Flow Ratio Modifier Curve Name',
                                        'pyname': u'effectiveness_flow_ratio_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'primary air design flow rate',
                                       {'name': u'Primary Air Design Flow Rate',
                                        'pyname': u'primary_air_design_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'recirculating water pump design power',
                                       {'name': u'Recirculating Water Pump Design Power',
                                        'pyname': u'recirculating_water_pump_design_power',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'W'}),
                                      (u'water pump power sizing factor',
                                       {'name': u'Water Pump Power Sizing Factor',
                                        'pyname': u'water_pump_power_sizing_factor',
                                        'default': 90.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/(m3/s)'}),
                                      (u'water pump power modifier curve name',
                                       {'name': u'Water Pump Power Modifier Curve Name',
                                        'pyname': u'water_pump_power_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'sensor node name',
                                       {'name': u'Sensor Node Name',
                                        'pyname': u'sensor_node_name',
                                        'required-field': True,
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
                                        'type': u'real'}),
                                      (u'evaporative operation minimum drybulb temperature',
                                       {'name': u'Evaporative Operation Minimum Drybulb Temperature',
                                        'pyname': u'evaporative_operation_minimum_drybulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -99.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'evaporative operation maximum limit wetbulb temperature',
                                       {'name': u'Evaporative Operation Maximum Limit Wetbulb Temperature',
                                        'pyname': u'evaporative_operation_maximum_limit_wetbulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'evaporative operation maximum limit drybulb temperature',
                                       {'name': u'Evaporative Operation Maximum Limit Drybulb Temperature',
                                        'pyname': u'evaporative_operation_maximum_limit_drybulb_temperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Evaporative Coolers',
               'min-fields': 11,
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
    def cooler_design_effectiveness(self):
        """field `Cooler Design Effectiveness`

        |  effectiveness with respect to wet-bulb depression
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Cooler Design Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooler_design_effectiveness` or None if not set

        """
        return self["Cooler Design Effectiveness"]

    @cooler_design_effectiveness.setter
    def cooler_design_effectiveness(self, value=None):
        """Corresponds to IDD field `Cooler Design Effectiveness`"""
        self["Cooler Design Effectiveness"] = value

    @property
    def effectiveness_flow_ratio_modifier_curve_name(self):
        """field `Effectiveness Flow Ratio Modifier Curve Name`

        |  this curve modifies the design effectiveness in the previous field
        |  by multiplying the value by the result of this curve.  The effectiveness flow modifier curve
        |  is a function of flow fraction. Flow fraction is the ratio of current primary air flow rate to
        |  the primary air design flow rate. If this input field is left blank then, the effectiveness
        |  is assumed to be constant.
        |  Any curve or table with one independent variable can be used:
        |  Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        |  Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        |  Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        |  Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Effectiveness Flow Ratio Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `effectiveness_flow_ratio_modifier_curve_name` or None if not set

        """
        return self["Effectiveness Flow Ratio Modifier Curve Name"]

    @effectiveness_flow_ratio_modifier_curve_name.setter
    def effectiveness_flow_ratio_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Effectiveness Flow Ratio Modifier Curve
        Name`"""
        self["Effectiveness Flow Ratio Modifier Curve Name"] = value

    @property
    def primary_air_design_flow_rate(self):
        """field `Primary Air Design Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Primary Air Design Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `primary_air_design_flow_rate` or None if not set

        """
        return self["Primary Air Design Flow Rate"]

    @primary_air_design_flow_rate.setter
    def primary_air_design_flow_rate(self, value=None):
        """Corresponds to IDD field `Primary Air Design Flow Rate`"""
        self["Primary Air Design Flow Rate"] = value

    @property
    def recirculating_water_pump_design_power(self):
        """field `Recirculating Water Pump Design Power`

        |  This is the design water pump or spray for evaporation at the primary air design air flow rates
        |  and cooler design effectiveness
        |  Units: W
        |  IP-Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Recirculating Water Pump Design Power`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `recirculating_water_pump_design_power` or None if not set

        """
        return self["Recirculating Water Pump Design Power"]

    @recirculating_water_pump_design_power.setter
    def recirculating_water_pump_design_power(self, value=None):
        """Corresponds to IDD field `Recirculating Water Pump Design Power`"""
        self["Recirculating Water Pump Design Power"] = value

    @property
    def water_pump_power_sizing_factor(self):
        """field `Water Pump Power Sizing Factor`

        |  This field is used when the previous field is set to autosize. The pump power is scaled with Secondary Air
        |  Design Air Flow Rate. This value was backed out from inputs in energy plus example files. Average Pump Power
        |  sizing factor was estimated from pump power and primary air design flow rates inputs from energyplus example
        |  files is about 90.0 [W/(m3/s)] (=90.0 ~ Pump Power / Primary Air Design Flow Rate). The factor ranges from
        |  55.0 to 150.0 [W/(m3/s)].
        |  Units: W/(m3/s)
        |  Default value: 90.0

        Args:
            value (float): value for IDD Field `Water Pump Power Sizing Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `water_pump_power_sizing_factor` or None if not set

        """
        return self["Water Pump Power Sizing Factor"]

    @water_pump_power_sizing_factor.setter
    def water_pump_power_sizing_factor(self, value=90.0):
        """Corresponds to IDD field `Water Pump Power Sizing Factor`"""
        self["Water Pump Power Sizing Factor"] = value

    @property
    def water_pump_power_modifier_curve_name(self):
        """field `Water Pump Power Modifier Curve Name`

        |  this curve modifies the pump power in the previous field by multiplying the design power by the result of this curve.
        |  x = ff = flow fraction on the primary air. The flow fraction is the secondary air flow rate during current operation divided
        |  by Primary Air Design Flow Rate
        |  Any curve or table with one independent variable can be used:
        |  Curve:Linear, Curve:Quadratic, Curve:Cubic, Curve:Quartic, Curve:Exponent,
        |  Curve:ExponentialSkewNormal, Curve:Sigmoid, Curve:RectuangularHyperbola1,
        |  Curve:RectangularHyperbola2, Curve:ExponentialDecay, Curve:DoubleExponentialDecay,
        |  Table:OneIndependentVariable

        Args:
            value (str): value for IDD Field `Water Pump Power Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `water_pump_power_modifier_curve_name` or None if not set

        """
        return self["Water Pump Power Modifier Curve Name"]

    @water_pump_power_modifier_curve_name.setter
    def water_pump_power_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Water Pump Power Modifier Curve Name`"""
        self["Water Pump Power Modifier Curve Name"] = value

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
        """field `Drift Loss Fraction`

        |  Rate of drift loss as a fraction of evaporated water flow rate

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

        |  Characterizes the rate of blowdown in the evaporative cooler.
        |  Blowdown is water intentionally drained from the cooler in order to offset the build up
        |  of solids in the water that would otherwise occur because of evaporation.
        |  Ratio of solids in the blowdown water to solids in the make up water.
        |  A typical value is 3. If left blank then there is no blowdown.
        |  value >= 2.0

        Args:
            value (float): value for IDD Field `Blowdown Concentration Ratio`

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

    @property
    def evaporative_operation_minimum_drybulb_temperature(self):
        """field `Evaporative Operation Minimum Drybulb Temperature`

        |  This numeric field defines the evaporative cooler air inlet node drybulb temperature minimum
        |  limit in degrees Celsius. The evaporative cooler will be turned off when the evaporator cooler
        |  air inlet node dry-bulb temperature falls below this limit. The typical minimum value is 16degC. Users
        |  are allowed to specify their own limits. If this field is left blank, then there is no drybulb lower
        |  temperature limit for evaporative cooler operation.
        |  value >= -99.0

        Args:
            value (float): value for IDD Field `Evaporative Operation Minimum Drybulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_operation_minimum_drybulb_temperature` or None if not set

        """
        return self["Evaporative Operation Minimum Drybulb Temperature"]

    @evaporative_operation_minimum_drybulb_temperature.setter
    def evaporative_operation_minimum_drybulb_temperature(self, value=None):
        """Corresponds to IDD field `Evaporative Operation Minimum Drybulb
        Temperature`"""
        self["Evaporative Operation Minimum Drybulb Temperature"] = value

    @property
    def evaporative_operation_maximum_limit_wetbulb_temperature(self):
        """field `Evaporative Operation Maximum Limit Wetbulb Temperature`

        |  when outdoor wetbulb temperature rises above this limit the cooler shuts down.
        |  This numeric field defines the evaporative cooler air inlet node wet-bulb temperature maximum
        |  limit in degrees Celsius. The evaporative cooler will be turned off when the evaporative cooler
        |  air inlet node wet-bulb temperature exceeds this limit. The typical maximum value is 24degC. Users
        |  are allowed to specify their own limits. If this field is left blank, then there is no upper
        |  wetbulb temperature limit for evaporative cooler operation.

        Args:
            value (float): value for IDD Field `Evaporative Operation Maximum Limit Wetbulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_operation_maximum_limit_wetbulb_temperature` or None if not set

        """
        return self["Evaporative Operation Maximum Limit Wetbulb Temperature"]

    @evaporative_operation_maximum_limit_wetbulb_temperature.setter
    def evaporative_operation_maximum_limit_wetbulb_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Evaporative Operation Maximum Limit
        Wetbulb Temperature`"""
        self["Evaporative Operation Maximum Limit Wetbulb Temperature"] = value

    @property
    def evaporative_operation_maximum_limit_drybulb_temperature(self):
        """field `Evaporative Operation Maximum Limit Drybulb Temperature`

        |  This numeric field defines the evaporative cooler air inlet node dry-bulb temperature maximum
        |  limit in degrees Celsius. The evaporative cooler will be turned off when its air inlet node
        |  drybulb temperature exceeds this limit. The typical maximum value is 26degC. Users
        |  are allowed to specify their own limits. If this field is left blank, then there is no upper
        |  temperature limit for evaporative cooler operation.

        Args:
            value (float): value for IDD Field `Evaporative Operation Maximum Limit Drybulb Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_operation_maximum_limit_drybulb_temperature` or None if not set

        """
        return self["Evaporative Operation Maximum Limit Drybulb Temperature"]

    @evaporative_operation_maximum_limit_drybulb_temperature.setter
    def evaporative_operation_maximum_limit_drybulb_temperature(
            self,
            value=None):
        """Corresponds to IDD field `Evaporative Operation Maximum Limit
        Drybulb Temperature`"""
        self["Evaporative Operation Maximum Limit Drybulb Temperature"] = value


