""" Data objects in group "Zone HVAC Air Loop Terminal Units"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class AirTerminalSingleDuctUncontrolled(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:Uncontrolled`
        Central air system terminal unit, single duct, constant volume, no controls other than
        on/off schedule.
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
                                      (u'zone supply air node name',
                                       {'name': u'Zone Supply Air Node Name',
                                        'pyname': u'zone_supply_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 4,
               'name': u'AirTerminal:SingleDuct:Uncontrolled',
               'pyname': u'AirTerminalSingleDuctUncontrolled',
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
    def zone_supply_air_node_name(self):
        """field `Zone Supply Air Node Name`

        Args:
            value (str): value for IDD Field `Zone Supply Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_supply_air_node_name` or None if not set

        """
        return self["Zone Supply Air Node Name"]

    @zone_supply_air_node_name.setter
    def zone_supply_air_node_name(self, value=None):
        """Corresponds to IDD field `Zone Supply Air Node Name`"""
        self["Zone Supply Air Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value




class AirTerminalSingleDuctConstantVolumeReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:Reheat`
        Central air system terminal unit, single duct, constant volume, with reheat coil (hot
        water, electric, gas, or steam).
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
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'hot water or steam inlet node name',
                                       {'name': u'Hot Water or Steam Inlet Node Name',
                                        'pyname': u'hot_water_or_steam_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum reheat air temperature',
                                       {'name': u'Maximum Reheat Air Temperature',
                                        'pyname': u'maximum_reheat_air_temperature',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:ConstantVolume:Reheat',
               'pyname': u'AirTerminalSingleDuctConstantVolumeReheat',
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
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """field `Hot Water or Steam Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set

        """
        return self["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water or Steam Inlet Node Name`"""
        self["Hot Water or Steam Inlet Node Name"] = value

    @property
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value

    @property
    def maximum_reheat_air_temperature(self):
        """field `Maximum Reheat Air Temperature`

        |  Specifies the maximum allowable supply air temperature leaving the reheat coil.
        |  If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.
        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Reheat Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_reheat_air_temperature` or None if not set

        """
        return self["Maximum Reheat Air Temperature"]

    @maximum_reheat_air_temperature.setter
    def maximum_reheat_air_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Reheat Air Temperature`"""
        self["Maximum Reheat Air Temperature"] = value




class AirTerminalSingleDuctVavNoReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:NoReheat`
        Central air system terminal unit, single duct, variable volume, with no reheat coil.
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
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'zone minimum air flow input method',
                                       {'name': u'Zone Minimum Air Flow Input Method',
                                        'pyname': u'zone_minimum_air_flow_input_method',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'FixedFlowRate',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'constant minimum air flow fraction',
                                       {'name': u'Constant Minimum Air Flow Fraction',
                                        'pyname': u'constant_minimum_air_flow_fraction',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fixed minimum air flow rate',
                                       {'name': u'Fixed Minimum Air Flow Rate',
                                        'pyname': u'fixed_minimum_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum air flow fraction schedule name',
                                       {'name': u'Minimum Air Flow Fraction Schedule Name',
                                        'pyname': u'minimum_air_flow_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design specification outdoor air object name',
                                       {'name': u'Design Specification Outdoor Air Object Name',
                                        'pyname': u'design_specification_outdoor_air_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:VAV:NoReheat',
               'pyname': u'AirTerminalSingleDuctVavNoReheat',
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
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_input_method(self):
        """field `Zone Minimum Air Flow Input Method`

        |  Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate)
        |  FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate)
        |  Scheduled = Scheduled Minimum Air Flow Fraction (a fraction of Maximum Air Flow

        Args:
            value (str): value for IDD Field `Zone Minimum Air Flow Input Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_minimum_air_flow_input_method` or None if not set

        """
        return self["Zone Minimum Air Flow Input Method"]

    @zone_minimum_air_flow_input_method.setter
    def zone_minimum_air_flow_input_method(self, value=None):
        """Corresponds to IDD field `Zone Minimum Air Flow Input Method`"""
        self["Zone Minimum Air Flow Input Method"] = value

    @property
    def constant_minimum_air_flow_fraction(self):
        """field `Constant Minimum Air Flow Fraction`

        |  This field is used if the field Zone Minimum Air Flow Input Method is Constant
        |  If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        |  is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        |  If both this field and the following field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `Constant Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_minimum_air_flow_fraction` or None if not set

        """
        return self["Constant Minimum Air Flow Fraction"]

    @constant_minimum_air_flow_fraction.setter
    def constant_minimum_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Constant Minimum Air Flow Fraction`"""
        self["Constant Minimum Air Flow Fraction"] = value

    @property
    def fixed_minimum_air_flow_rate(self):
        """field `Fixed Minimum Air Flow Rate`

        |  This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate.
        |  If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        |  is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        |  If both this field and the previous field are entered, the larger result is used.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Fixed Minimum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fixed_minimum_air_flow_rate` or None if not set

        """
        return self["Fixed Minimum Air Flow Rate"]

    @fixed_minimum_air_flow_rate.setter
    def fixed_minimum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Fixed Minimum Air Flow Rate`"""
        self["Fixed Minimum Air Flow Rate"] = value

    @property
    def minimum_air_flow_fraction_schedule_name(self):
        """field `Minimum Air Flow Fraction Schedule Name`

        |  This field is used if the field Zone Minimum Air Flow Input Method is Scheduled
        |  Schedule values are fractions, 0.0 to 1.0.
        |  If the field Constant Minimum Air Flow Fraction is blank, then the average of the
        |  minimum and maximum schedule values is used for sizing normal-action reheat coils.

        Args:
            value (str): value for IDD Field `Minimum Air Flow Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_air_flow_fraction_schedule_name` or None if not set

        """
        return self["Minimum Air Flow Fraction Schedule Name"]

    @minimum_air_flow_fraction_schedule_name.setter
    def minimum_air_flow_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Air Flow Fraction Schedule
        Name`"""
        self["Minimum Air Flow Fraction Schedule Name"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """field `Design Specification Outdoor Air Object Name`

        |  When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        |  unit will increase flow as needed to meet this outdoor air requirement.
        |  If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        |  be computed based on the current number of occupants in the zone.
        |  At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        |  If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set

        """
        return self["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification Outdoor Air Object
        Name`"""
        self["Design Specification Outdoor Air Object Name"] = value




class AirTerminalSingleDuctVavReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:Reheat`
        Central air system terminal unit, single duct, variable volume, with reheat coil (hot
        water, electric, gas, or steam).
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
                                      (u'damper air outlet node name',
                                       {'name': u'Damper Air Outlet Node Name',
                                        'pyname': u'damper_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'zone minimum air flow input method',
                                       {'name': u'Zone Minimum Air Flow Input Method',
                                        'pyname': u'zone_minimum_air_flow_input_method',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Constant',
                                                            u'FixedFlowRate',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'constant minimum air flow fraction',
                                       {'name': u'Constant Minimum Air Flow Fraction',
                                        'pyname': u'constant_minimum_air_flow_fraction',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'fixed minimum air flow rate',
                                       {'name': u'Fixed Minimum Air Flow Rate',
                                        'pyname': u'fixed_minimum_air_flow_rate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum air flow fraction schedule name',
                                       {'name': u'Minimum Air Flow Fraction Schedule Name',
                                        'pyname': u'minimum_air_flow_fraction_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'damper heating action',
                                       {'name': u'Damper Heating Action',
                                        'pyname': u'damper_heating_action',
                                        'default': u'Normal',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Normal',
                                                            u'Reverse'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'maximum flow per zone floor area during reheat',
                                       {'name': u'Maximum Flow per Zone Floor Area During Reheat',
                                        'pyname': u'maximum_flow_per_zone_floor_area_during_reheat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3/s-m2'}),
                                      (u'maximum flow fraction during reheat',
                                       {'name': u'Maximum Flow Fraction During Reheat',
                                        'pyname': u'maximum_flow_fraction_during_reheat',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': True,
                                        'type': u'real'}),
                                      (u'maximum reheat air temperature',
                                       {'name': u'Maximum Reheat Air Temperature',
                                        'pyname': u'maximum_reheat_air_temperature',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'design specification outdoor air object name',
                                       {'name': u'Design Specification Outdoor Air Object Name',
                                        'pyname': u'design_specification_outdoor_air_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:VAV:Reheat',
               'pyname': u'AirTerminalSingleDuctVavReheat',
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
    def damper_air_outlet_node_name(self):
        """field `Damper Air Outlet Node Name`

        |  the outlet node of the damper and the inlet node of the reheat coil
        |  this is an internal node to the terminal unit and connects the damper and reheat coil

        Args:
            value (str): value for IDD Field `Damper Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `damper_air_outlet_node_name` or None if not set

        """
        return self["Damper Air Outlet Node Name"]

    @damper_air_outlet_node_name.setter
    def damper_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Damper Air Outlet Node Name`"""
        self["Damper Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  the inlet node to the terminal unit and the damper

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
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_input_method(self):
        """field `Zone Minimum Air Flow Input Method`

        |  Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate)
        |  FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate)
        |  Scheduled = Scheduled Minimum Air Flow Fraction (a fraction of Maximum Air Flow

        Args:
            value (str): value for IDD Field `Zone Minimum Air Flow Input Method`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_minimum_air_flow_input_method` or None if not set

        """
        return self["Zone Minimum Air Flow Input Method"]

    @zone_minimum_air_flow_input_method.setter
    def zone_minimum_air_flow_input_method(self, value=None):
        """Corresponds to IDD field `Zone Minimum Air Flow Input Method`"""
        self["Zone Minimum Air Flow Input Method"] = value

    @property
    def constant_minimum_air_flow_fraction(self):
        """field `Constant Minimum Air Flow Fraction`

        |  This field is used if the field Zone Minimum Air Flow Input Method is Constant
        |  If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        |  is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        |  If both this field and the following field are entered, the larger result is used.

        Args:
            value (float): value for IDD Field `Constant Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_minimum_air_flow_fraction` or None if not set

        """
        return self["Constant Minimum Air Flow Fraction"]

    @constant_minimum_air_flow_fraction.setter
    def constant_minimum_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Constant Minimum Air Flow Fraction`"""
        self["Constant Minimum Air Flow Fraction"] = value

    @property
    def fixed_minimum_air_flow_rate(self):
        """field `Fixed Minimum Air Flow Rate`

        |  This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate.
        |  If the field Zone Minimum Air Flow Input Method is Scheduled, then this field
        |  is optional; if a value is entered, then it is used for sizing normal-action reheat coils.
        |  If both this field and the previous field are entered, the larger result is used.
        |  Units: m3/s

        Args:
            value (float): value for IDD Field `Fixed Minimum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `fixed_minimum_air_flow_rate` or None if not set

        """
        return self["Fixed Minimum Air Flow Rate"]

    @fixed_minimum_air_flow_rate.setter
    def fixed_minimum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Fixed Minimum Air Flow Rate`"""
        self["Fixed Minimum Air Flow Rate"] = value

    @property
    def minimum_air_flow_fraction_schedule_name(self):
        """field `Minimum Air Flow Fraction Schedule Name`

        |  This field is used if the field Zone Minimum Air Flow Input Method is Scheduled
        |  Schedule values are fractions, 0.0 to 1.0.
        |  If the field Constant Minimum Air Flow Fraction is blank, then the average of the
        |  minimum and maximum schedule values is used for sizing normal-action reheat coils.

        Args:
            value (str): value for IDD Field `Minimum Air Flow Fraction Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `minimum_air_flow_fraction_schedule_name` or None if not set

        """
        return self["Minimum Air Flow Fraction Schedule Name"]

    @minimum_air_flow_fraction_schedule_name.setter
    def minimum_air_flow_fraction_schedule_name(self, value=None):
        """Corresponds to IDD field `Minimum Air Flow Fraction Schedule
        Name`"""
        self["Minimum Air Flow Fraction Schedule Name"] = value

    @property
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  The outlet node of the terminal unit and the reheat coil.
        |  This is also the zone inlet node.

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
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value

    @property
    def damper_heating_action(self):
        """field `Damper Heating Action`

        |  Default value: Normal

        Args:
            value (str): value for IDD Field `Damper Heating Action`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `damper_heating_action` or None if not set

        """
        return self["Damper Heating Action"]

    @damper_heating_action.setter
    def damper_heating_action(self, value="Normal"):
        """Corresponds to IDD field `Damper Heating Action`"""
        self["Damper Heating Action"] = value

    @property
    def maximum_flow_per_zone_floor_area_during_reheat(self):
        """field `Maximum Flow per Zone Floor Area During Reheat`

        |  Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse
        |  When autocalculating, the maximum flow per zone is set to 0.002032 m3/s-m2 (0.4 cfm/sqft)
        |  This optional field limits the maximum flow allowed in reheat mode.
        |  If this field and the following field are left blank, the maximum flow will not be limited.
        |  At no time will the maximum flow rate calculated here exceed the value of
        |  Maximum Air Flow Rate.
        |  Units: m3/s-m2

        Args:
            value (float or "Autocalculate"): value for IDD Field `Maximum Flow per Zone Floor Area During Reheat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `maximum_flow_per_zone_floor_area_during_reheat` or None if not set

        """
        return self["Maximum Flow per Zone Floor Area During Reheat"]

    @maximum_flow_per_zone_floor_area_during_reheat.setter
    def maximum_flow_per_zone_floor_area_during_reheat(self, value=None):
        """Corresponds to IDD field `Maximum Flow per Zone Floor Area During
        Reheat`"""
        self["Maximum Flow per Zone Floor Area During Reheat"] = value

    @property
    def maximum_flow_fraction_during_reheat(self):
        """field `Maximum Flow Fraction During Reheat`

        |  Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse
        |  When autocalculating, the maximum flow fraction is set to the ratio of
        |  0.002032 m3/s-m2 (0.4 cfm/sqft) multiplied by the zone floor area and the
        |  Maximum Air Flow Rate.
        |  This optional field limits the maximum flow allowed in reheat mode.
        |  If this field and the previous field are left blank, the maximum flow will not be limited.
        |  At no time will the maximum flow rate calculated here exceed the value of
        |  Maximum Air Flow Rate.

        Args:
            value (float or "Autocalculate"): value for IDD Field `Maximum Flow Fraction During Reheat`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `maximum_flow_fraction_during_reheat` or None if not set

        """
        return self["Maximum Flow Fraction During Reheat"]

    @maximum_flow_fraction_during_reheat.setter
    def maximum_flow_fraction_during_reheat(self, value=None):
        """Corresponds to IDD field `Maximum Flow Fraction During Reheat`"""
        self["Maximum Flow Fraction During Reheat"] = value

    @property
    def maximum_reheat_air_temperature(self):
        """field `Maximum Reheat Air Temperature`

        |  Specifies the maximum allowable supply air temperature leaving the reheat coil.
        |  If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.
        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Reheat Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_reheat_air_temperature` or None if not set

        """
        return self["Maximum Reheat Air Temperature"]

    @maximum_reheat_air_temperature.setter
    def maximum_reheat_air_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Reheat Air Temperature`"""
        self["Maximum Reheat Air Temperature"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """field `Design Specification Outdoor Air Object Name`

        |  When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        |  unit will increase flow as needed to meet this outdoor air requirement.
        |  If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        |  be computed based on the current number of occupants in the zone.
        |  At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        |  If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set

        """
        return self["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification Outdoor Air Object
        Name`"""
        self["Design Specification Outdoor Air Object Name"] = value




class AirTerminalSingleDuctVavReheatVariableSpeedFan(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan`
        Central air system terminal unit, single duct, variable volume, with reheat coil (hot
        water, electric, gas, or steam) and variable-speed fan. These units are usually
        employed in underfloor air distribution (UFAD) systems where the air is supplied at
        low static pressure through an underfloor plenum. The fan is used to control the flow
        of conditioned air that enters the space.
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
                                      (u'maximum cooling air flow rate',
                                       {'name': u'Maximum Cooling Air Flow Rate',
                                        'pyname': u'maximum_cooling_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum heating air flow rate',
                                       {'name': u'Maximum Heating Air Flow Rate',
                                        'pyname': u'maximum_heating_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'zone minimum air flow fraction',
                                       {'name': u'Zone Minimum Air Flow Fraction',
                                        'pyname': u'zone_minimum_air_flow_fraction',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
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
                                      (u'heating coil air inlet node name',
                                       {'name': u'Heating Coil Air Inlet Node Name',
                                        'pyname': u'heating_coil_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'hot water or steam inlet node name',
                                       {'name': u'Hot Water or Steam Inlet Node Name',
                                        'pyname': u'hot_water_or_steam_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'fan object type',
                                       {'name': u'Fan Object Type',
                                        'pyname': u'fan_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Fan:VariableVolume'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fan name',
                                       {'name': u'Fan Name',
                                        'pyname': u'fan_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating convergence tolerance',
                                       {'name': u'Heating Convergence Tolerance',
                                        'pyname': u'heating_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan',
               'pyname': u'AirTerminalSingleDuctVavReheatVariableSpeedFan',
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
    def maximum_cooling_air_flow_rate(self):
        """field `Maximum Cooling Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cooling Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_cooling_air_flow_rate` or None if not set

        """
        return self["Maximum Cooling Air Flow Rate"]

    @maximum_cooling_air_flow_rate.setter
    def maximum_cooling_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Cooling Air Flow Rate`"""
        self["Maximum Cooling Air Flow Rate"] = value

    @property
    def maximum_heating_air_flow_rate(self):
        """field `Maximum Heating Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Heating Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_heating_air_flow_rate` or None if not set

        """
        return self["Maximum Heating Air Flow Rate"]

    @maximum_heating_air_flow_rate.setter
    def maximum_heating_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Heating Air Flow Rate`"""
        self["Maximum Heating Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """field `Zone Minimum Air Flow Fraction`

        |  fraction of cooling air flow rate
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set

        """
        return self["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Zone Minimum Air Flow Fraction`"""
        self["Zone Minimum Air Flow Fraction"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

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

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

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
    def heating_coil_air_inlet_node_name(self):
        """field `Heating Coil Air Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Heating Coil Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_air_inlet_node_name` or None if not set

        """
        return self["Heating Coil Air Inlet Node Name"]

    @heating_coil_air_inlet_node_name.setter
    def heating_coil_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Air Inlet Node Name`"""
        self["Heating Coil Air Inlet Node Name"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """field `Hot Water or Steam Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set

        """
        return self["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water or Steam Inlet Node Name`"""
        self["Hot Water or Steam Inlet Node Name"] = value

    @property
    def fan_object_type(self):
        """field `Fan Object Type`

        Args:
            value (str): value for IDD Field `Fan Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fan_object_type` or None if not set

        """
        return self["Fan Object Type"]

    @fan_object_type.setter
    def fan_object_type(self, value=None):
        """Corresponds to IDD field `Fan Object Type`"""
        self["Fan Object Type"] = value

    @property
    def fan_name(self):
        """field `Fan Name`

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
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when heating coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when heating coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """field `Heating Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set

        """
        return self["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence Tolerance`"""
        self["Heating Convergence Tolerance"] = value




class AirTerminalSingleDuctVavHeatAndCoolNoReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat`
        Central air system terminal unit, single duct, variable volume for both cooling and
        heating, with no reheat coil.
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
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'zone minimum air flow fraction',
                                       {'name': u'Zone Minimum Air Flow Fraction',
                                        'pyname': u'zone_minimum_air_flow_fraction',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 6,
               'name': u'AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat',
               'pyname': u'AirTerminalSingleDuctVavHeatAndCoolNoReheat',
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
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  The outlet node of the terminal unit.
        |  This is also the zone inlet node.

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
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """field `Zone Minimum Air Flow Fraction`

        |  fraction of maximum air flow
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set

        """
        return self["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Zone Minimum Air Flow Fraction`"""
        self["Zone Minimum Air Flow Fraction"] = value




class AirTerminalSingleDuctVavHeatAndCoolReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat`
        Central air system terminal unit, single duct, variable volume for both cooling and
        heating, with reheat coil (hot water, electric, gas, or steam).
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
                                      (u'damper air outlet node name',
                                       {'name': u'Damper Air Outlet Node Name',
                                        'pyname': u'damper_air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air inlet node name',
                                       {'name': u'Air Inlet Node Name',
                                        'pyname': u'air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'zone minimum air flow fraction',
                                       {'name': u'Zone Minimum Air Flow Fraction',
                                        'pyname': u'zone_minimum_air_flow_fraction',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'hot water or steam inlet node name',
                                       {'name': u'Hot Water or Steam Inlet Node Name',
                                        'pyname': u'hot_water_or_steam_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'maximum reheat air temperature',
                                       {'name': u'Maximum Reheat Air Temperature',
                                        'pyname': u'maximum_reheat_air_temperature',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 12,
               'name': u'AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat',
               'pyname': u'AirTerminalSingleDuctVavHeatAndCoolReheat',
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
    def damper_air_outlet_node_name(self):
        """field `Damper Air Outlet Node Name`

        |  the outlet node of the damper and the inlet node of the reheat coil
        |  this is an internal node to the terminal unit and connects the damper and reheat coil

        Args:
            value (str): value for IDD Field `Damper Air Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `damper_air_outlet_node_name` or None if not set

        """
        return self["Damper Air Outlet Node Name"]

    @damper_air_outlet_node_name.setter
    def damper_air_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Damper Air Outlet Node Name`"""
        self["Damper Air Outlet Node Name"] = value

    @property
    def air_inlet_node_name(self):
        """field `Air Inlet Node Name`

        |  the inlet node to the terminal unit and the damper

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
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """field `Zone Minimum Air Flow Fraction`

        |  fraction of maximum air flow
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set

        """
        return self["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Zone Minimum Air Flow Fraction`"""
        self["Zone Minimum Air Flow Fraction"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """field `Hot Water or Steam Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set

        """
        return self["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water or Steam Inlet Node Name`"""
        self["Hot Water or Steam Inlet Node Name"] = value

    @property
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  The outlet node of the terminal unit and the reheat coil.
        |  This is also the zone inlet node.

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
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value

    @property
    def maximum_reheat_air_temperature(self):
        """field `Maximum Reheat Air Temperature`

        |  Specifies the maximum allowable supply air temperature leaving the reheat coil.
        |  If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.
        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Reheat Air Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_reheat_air_temperature` or None if not set

        """
        return self["Maximum Reheat Air Temperature"]

    @maximum_reheat_air_temperature.setter
    def maximum_reheat_air_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Reheat Air Temperature`"""
        self["Maximum Reheat Air Temperature"] = value




class AirTerminalSingleDuctSeriesPiuReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:SeriesPIU:Reheat`
        Central air system terminal unit, single duct, variable volume, series powered
        induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).
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
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum primary air flow rate',
                                       {'name': u'Maximum Primary Air Flow Rate',
                                        'pyname': u'maximum_primary_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum primary air flow fraction',
                                       {'name': u'Minimum Primary Air Flow Fraction',
                                        'pyname': u'minimum_primary_air_flow_fraction',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'supply air inlet node name',
                                       {'name': u'Supply Air Inlet Node Name',
                                        'pyname': u'supply_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'reheat coil air inlet node name',
                                       {'name': u'Reheat Coil Air Inlet Node Name',
                                        'pyname': u'reheat_coil_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone mixer name',
                                       {'name': u'Zone Mixer Name',
                                        'pyname': u'zone_mixer_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan name',
                                       {'name': u'Fan Name',
                                        'pyname': u'fan_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'hot water or steam inlet node name',
                                       {'name': u'Hot Water or Steam Inlet Node Name',
                                        'pyname': u'hot_water_or_steam_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:SeriesPIU:Reheat',
               'pyname': u'AirTerminalSingleDuctSeriesPiuReheat',
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
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value

    @property
    def maximum_primary_air_flow_rate(self):
        """field `Maximum Primary Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Primary Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_primary_air_flow_rate` or None if not set

        """
        return self["Maximum Primary Air Flow Rate"]

    @maximum_primary_air_flow_rate.setter
    def maximum_primary_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Primary Air Flow Rate`"""
        self["Maximum Primary Air Flow Rate"] = value

    @property
    def minimum_primary_air_flow_fraction(self):
        """field `Minimum Primary Air Flow Fraction`

        |  value <= 1.0

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Primary Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `minimum_primary_air_flow_fraction` or None if not set

        """
        return self["Minimum Primary Air Flow Fraction"]

    @minimum_primary_air_flow_fraction.setter
    def minimum_primary_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Minimum Primary Air Flow Fraction`"""
        self["Minimum Primary Air Flow Fraction"] = value

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
    def reheat_coil_air_inlet_node_name(self):
        """field `Reheat Coil Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_air_inlet_node_name` or None if not set

        """
        return self["Reheat Coil Air Inlet Node Name"]

    @reheat_coil_air_inlet_node_name.setter
    def reheat_coil_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Air Inlet Node Name`"""
        self["Reheat Coil Air Inlet Node Name"] = value

    @property
    def zone_mixer_name(self):
        """field `Zone Mixer Name`

        Args:
            value (str): value for IDD Field `Zone Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_mixer_name` or None if not set

        """
        return self["Zone Mixer Name"]

    @zone_mixer_name.setter
    def zone_mixer_name(self, value=None):
        """Corresponds to IDD field `Zone Mixer Name`"""
        self["Zone Mixer Name"] = value

    @property
    def fan_name(self):
        """field `Fan Name`

        |  Fan type must be Fan:ConstantVolume

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
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """field `Hot Water or Steam Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set

        """
        return self["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water or Steam Inlet Node Name`"""
        self["Hot Water or Steam Inlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value




class AirTerminalSingleDuctParallelPiuReheat(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:ParallelPIU:Reheat`
        Central air system terminal unit, single duct, variable volume, parallel powered
        induction unit (PIU), with reheat coil (hot water, electric, gas, or steam).
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
                                      (u'maximum primary air flow rate',
                                       {'name': u'Maximum Primary Air Flow Rate',
                                        'pyname': u'maximum_primary_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum secondary air flow rate',
                                       {'name': u'Maximum Secondary Air Flow Rate',
                                        'pyname': u'maximum_secondary_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum primary air flow fraction',
                                       {'name': u'Minimum Primary Air Flow Fraction',
                                        'pyname': u'minimum_primary_air_flow_fraction',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'fan on flow fraction',
                                       {'name': u'Fan On Flow Fraction',
                                        'pyname': u'fan_on_flow_fraction',
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'supply air inlet node name',
                                       {'name': u'Supply Air Inlet Node Name',
                                        'pyname': u'supply_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'reheat coil air inlet node name',
                                       {'name': u'Reheat Coil Air Inlet Node Name',
                                        'pyname': u'reheat_coil_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'zone mixer name',
                                       {'name': u'Zone Mixer Name',
                                        'pyname': u'zone_mixer_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fan name',
                                       {'name': u'Fan Name',
                                        'pyname': u'fan_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'reheat coil object type',
                                       {'name': u'Reheat Coil Object Type',
                                        'pyname': u'reheat_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water',
                                                            u'Coil:Heating:Electric',
                                                            u'Coil:Heating:Gas',
                                                            u'Coil:Heating:Steam'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reheat coil name',
                                       {'name': u'Reheat Coil Name',
                                        'pyname': u'reheat_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water or steam flow rate',
                                       {'name': u'Maximum Hot Water or Steam Flow Rate',
                                        'pyname': u'maximum_hot_water_or_steam_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water or steam flow rate',
                                       {'name': u'Minimum Hot Water or Steam Flow Rate',
                                        'pyname': u'minimum_hot_water_or_steam_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'hot water or steam inlet node name',
                                       {'name': u'Hot Water or Steam Inlet Node Name',
                                        'pyname': u'hot_water_or_steam_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'convergence tolerance',
                                       {'name': u'Convergence Tolerance',
                                        'pyname': u'convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:ParallelPIU:Reheat',
               'pyname': u'AirTerminalSingleDuctParallelPiuReheat',
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
    def maximum_primary_air_flow_rate(self):
        """field `Maximum Primary Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Primary Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_primary_air_flow_rate` or None if not set

        """
        return self["Maximum Primary Air Flow Rate"]

    @maximum_primary_air_flow_rate.setter
    def maximum_primary_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Primary Air Flow Rate`"""
        self["Maximum Primary Air Flow Rate"] = value

    @property
    def maximum_secondary_air_flow_rate(self):
        """field `Maximum Secondary Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Secondary Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_secondary_air_flow_rate` or None if not set

        """
        return self["Maximum Secondary Air Flow Rate"]

    @maximum_secondary_air_flow_rate.setter
    def maximum_secondary_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Secondary Air Flow Rate`"""
        self["Maximum Secondary Air Flow Rate"] = value

    @property
    def minimum_primary_air_flow_fraction(self):
        """field `Minimum Primary Air Flow Fraction`

        |  value <= 1.0

        Args:
            value (float or "Autosize"): value for IDD Field `Minimum Primary Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `minimum_primary_air_flow_fraction` or None if not set

        """
        return self["Minimum Primary Air Flow Fraction"]

    @minimum_primary_air_flow_fraction.setter
    def minimum_primary_air_flow_fraction(self, value=None):
        """Corresponds to IDD field `Minimum Primary Air Flow Fraction`"""
        self["Minimum Primary Air Flow Fraction"] = value

    @property
    def fan_on_flow_fraction(self):
        """field `Fan On Flow Fraction`

        |  the fraction of the primary air flow at which fan turns on
        |  value <= 1.0

        Args:
            value (float or "Autosize"): value for IDD Field `Fan On Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `fan_on_flow_fraction` or None if not set

        """
        return self["Fan On Flow Fraction"]

    @fan_on_flow_fraction.setter
    def fan_on_flow_fraction(self, value=None):
        """Corresponds to IDD field `Fan On Flow Fraction`"""
        self["Fan On Flow Fraction"] = value

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
    def reheat_coil_air_inlet_node_name(self):
        """field `Reheat Coil Air Inlet Node Name`

        |  mixer outlet node

        Args:
            value (str): value for IDD Field `Reheat Coil Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_air_inlet_node_name` or None if not set

        """
        return self["Reheat Coil Air Inlet Node Name"]

    @reheat_coil_air_inlet_node_name.setter
    def reheat_coil_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Air Inlet Node Name`"""
        self["Reheat Coil Air Inlet Node Name"] = value

    @property
    def zone_mixer_name(self):
        """field `Zone Mixer Name`

        Args:
            value (str): value for IDD Field `Zone Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_mixer_name` or None if not set

        """
        return self["Zone Mixer Name"]

    @zone_mixer_name.setter
    def zone_mixer_name(self, value=None):
        """Corresponds to IDD field `Zone Mixer Name`"""
        self["Zone Mixer Name"] = value

    @property
    def fan_name(self):
        """field `Fan Name`

        |  Fan type must be Fan:ConstantVolume

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
    def reheat_coil_object_type(self):
        """field `Reheat Coil Object Type`

        Args:
            value (str): value for IDD Field `Reheat Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_object_type` or None if not set

        """
        return self["Reheat Coil Object Type"]

    @reheat_coil_object_type.setter
    def reheat_coil_object_type(self, value=None):
        """Corresponds to IDD field `Reheat Coil Object Type`"""
        self["Reheat Coil Object Type"] = value

    @property
    def reheat_coil_name(self):
        """field `Reheat Coil Name`

        Args:
            value (str): value for IDD Field `Reheat Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reheat_coil_name` or None if not set

        """
        return self["Reheat Coil Name"]

    @reheat_coil_name.setter
    def reheat_coil_name(self, value=None):
        """Corresponds to IDD field `Reheat Coil Name`"""
        self["Reheat Coil Name"] = value

    @property
    def maximum_hot_water_or_steam_flow_rate(self):
        """field `Maximum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Maximum Hot Water or Steam Flow Rate"]

    @maximum_hot_water_or_steam_flow_rate.setter
    def maximum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water or Steam Flow Rate`"""
        self["Maximum Hot Water or Steam Flow Rate"] = value

    @property
    def minimum_hot_water_or_steam_flow_rate(self):
        """field `Minimum Hot Water or Steam Flow Rate`

        |  Not used when reheat coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water or Steam Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_or_steam_flow_rate` or None if not set

        """
        return self["Minimum Hot Water or Steam Flow Rate"]

    @minimum_hot_water_or_steam_flow_rate.setter
    def minimum_hot_water_or_steam_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water or Steam Flow Rate`"""
        self["Minimum Hot Water or Steam Flow Rate"] = value

    @property
    def hot_water_or_steam_inlet_node_name(self):
        """field `Hot Water or Steam Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water or Steam Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_or_steam_inlet_node_name` or None if not set

        """
        return self["Hot Water or Steam Inlet Node Name"]

    @hot_water_or_steam_inlet_node_name.setter
    def hot_water_or_steam_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water or Steam Inlet Node Name`"""
        self["Hot Water or Steam Inlet Node Name"] = value

    @property
    def convergence_tolerance(self):
        """field `Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `convergence_tolerance` or None if not set

        """
        return self["Convergence Tolerance"]

    @convergence_tolerance.setter
    def convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Convergence Tolerance`"""
        self["Convergence Tolerance"] = value




class AirTerminalSingleDuctConstantVolumeFourPipeInduction(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction`
        Central air system terminal unit, single duct, variable volume, induction unit with
        hot water reheat coil and chilled water recool coil.
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
                                      (u'maximum total air flow rate',
                                       {'name': u'Maximum Total Air Flow Rate',
                                        'pyname': u'maximum_total_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'induction ratio',
                                       {'name': u'Induction Ratio',
                                        'pyname': u'induction_ratio',
                                        'default': 2.5,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'supply air inlet node name',
                                       {'name': u'Supply Air Inlet Node Name',
                                        'pyname': u'supply_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'induced air inlet node name',
                                       {'name': u'Induced Air Inlet Node Name',
                                        'pyname': u'induced_air_inlet_node_name',
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
                                      (u'hot water inlet node name',
                                       {'name': u'Hot Water Inlet Node Name',
                                        'pyname': u'hot_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cold water inlet node name',
                                       {'name': u'Cold Water Inlet Node Name',
                                        'pyname': u'cold_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'heating coil object type',
                                       {'name': u'Heating Coil Object Type',
                                        'pyname': u'heating_coil_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Heating:Water'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating coil name',
                                       {'name': u'Heating Coil Name',
                                        'pyname': u'heating_coil_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum hot water flow rate',
                                       {'name': u'Maximum Hot Water Flow Rate',
                                        'pyname': u'maximum_hot_water_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum hot water flow rate',
                                       {'name': u'Minimum Hot Water Flow Rate',
                                        'pyname': u'minimum_hot_water_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'heating convergence tolerance',
                                       {'name': u'Heating Convergence Tolerance',
                                        'pyname': u'heating_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'cooling coil object type',
                                       {'name': u'Cooling Coil Object Type',
                                        'pyname': u'cooling_coil_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Coil:Cooling:Water',
                                                            u'Coil:Cooling:Water:DetailedGeometry'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'cooling coil name',
                                       {'name': u'Cooling Coil Name',
                                        'pyname': u'cooling_coil_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'maximum cold water flow rate',
                                       {'name': u'Maximum Cold Water Flow Rate',
                                        'pyname': u'maximum_cold_water_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum cold water flow rate',
                                       {'name': u'Minimum Cold Water Flow Rate',
                                        'pyname': u'minimum_cold_water_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'cooling convergence tolerance',
                                       {'name': u'Cooling Convergence Tolerance',
                                        'pyname': u'cooling_convergence_tolerance',
                                        'default': 0.001,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'zone mixer name',
                                       {'name': u'Zone Mixer Name',
                                        'pyname': u'zone_mixer_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction',
               'pyname': u'AirTerminalSingleDuctConstantVolumeFourPipeInduction',
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
    def maximum_total_air_flow_rate(self):
        """field `Maximum Total Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Total Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_total_air_flow_rate` or None if not set

        """
        return self["Maximum Total Air Flow Rate"]

    @maximum_total_air_flow_rate.setter
    def maximum_total_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Total Air Flow Rate`"""
        self["Maximum Total Air Flow Rate"] = value

    @property
    def induction_ratio(self):
        """field `Induction Ratio`

        |  ratio of induced air flow rate to primary air flow rate
        |  Default value: 2.5

        Args:
            value (float): value for IDD Field `Induction Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `induction_ratio` or None if not set

        """
        return self["Induction Ratio"]

    @induction_ratio.setter
    def induction_ratio(self, value=2.5):
        """Corresponds to IDD field `Induction Ratio`"""
        self["Induction Ratio"] = value

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
    def induced_air_inlet_node_name(self):
        """field `Induced Air Inlet Node Name`

        |  should be a zone exhaust node, also the heating coil inlet node

        Args:
            value (str): value for IDD Field `Induced Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `induced_air_inlet_node_name` or None if not set

        """
        return self["Induced Air Inlet Node Name"]

    @induced_air_inlet_node_name.setter
    def induced_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Induced Air Inlet Node Name`"""
        self["Induced Air Inlet Node Name"] = value

    @property
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  should be a zone inlet node

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
    def hot_water_inlet_node_name(self):
        """field `Hot Water Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Hot Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_inlet_node_name` or None if not set

        """
        return self["Hot Water Inlet Node Name"]

    @hot_water_inlet_node_name.setter
    def hot_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water Inlet Node Name`"""
        self["Hot Water Inlet Node Name"] = value

    @property
    def cold_water_inlet_node_name(self):
        """field `Cold Water Inlet Node Name`

        |  This field is not really used and will be deleted from the object.
        |  The required information is gotten internally or
        |  not needed by the program.

        Args:
            value (str): value for IDD Field `Cold Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_water_inlet_node_name` or None if not set

        """
        return self["Cold Water Inlet Node Name"]

    @cold_water_inlet_node_name.setter
    def cold_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Cold Water Inlet Node Name`"""
        self["Cold Water Inlet Node Name"] = value

    @property
    def heating_coil_object_type(self):
        """field `Heating Coil Object Type`

        Args:
            value (str): value for IDD Field `Heating Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_object_type` or None if not set

        """
        return self["Heating Coil Object Type"]

    @heating_coil_object_type.setter
    def heating_coil_object_type(self, value=None):
        """Corresponds to IDD field `Heating Coil Object Type`"""
        self["Heating Coil Object Type"] = value

    @property
    def heating_coil_name(self):
        """field `Heating Coil Name`

        Args:
            value (str): value for IDD Field `Heating Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_coil_name` or None if not set

        """
        return self["Heating Coil Name"]

    @heating_coil_name.setter
    def heating_coil_name(self, value=None):
        """Corresponds to IDD field `Heating Coil Name`"""
        self["Heating Coil Name"] = value

    @property
    def maximum_hot_water_flow_rate(self):
        """field `Maximum Hot Water Flow Rate`

        |  Not used when heating coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Hot Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_hot_water_flow_rate` or None if not set

        """
        return self["Maximum Hot Water Flow Rate"]

    @maximum_hot_water_flow_rate.setter
    def maximum_hot_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Hot Water Flow Rate`"""
        self["Maximum Hot Water Flow Rate"] = value

    @property
    def minimum_hot_water_flow_rate(self):
        """field `Minimum Hot Water Flow Rate`

        |  Not used when heating coil type is gas or electric
        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Hot Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_hot_water_flow_rate` or None if not set

        """
        return self["Minimum Hot Water Flow Rate"]

    @minimum_hot_water_flow_rate.setter
    def minimum_hot_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Hot Water Flow Rate`"""
        self["Minimum Hot Water Flow Rate"] = value

    @property
    def heating_convergence_tolerance(self):
        """field `Heating Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Heating Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heating_convergence_tolerance` or None if not set

        """
        return self["Heating Convergence Tolerance"]

    @heating_convergence_tolerance.setter
    def heating_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Heating Convergence Tolerance`"""
        self["Heating Convergence Tolerance"] = value

    @property
    def cooling_coil_object_type(self):
        """field `Cooling Coil Object Type`

        Args:
            value (str): value for IDD Field `Cooling Coil Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_object_type` or None if not set

        """
        return self["Cooling Coil Object Type"]

    @cooling_coil_object_type.setter
    def cooling_coil_object_type(self, value=None):
        """Corresponds to IDD field `Cooling Coil Object Type`"""
        self["Cooling Coil Object Type"] = value

    @property
    def cooling_coil_name(self):
        """field `Cooling Coil Name`

        Args:
            value (str): value for IDD Field `Cooling Coil Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_coil_name` or None if not set

        """
        return self["Cooling Coil Name"]

    @cooling_coil_name.setter
    def cooling_coil_name(self, value=None):
        """Corresponds to IDD field `Cooling Coil Name`"""
        self["Cooling Coil Name"] = value

    @property
    def maximum_cold_water_flow_rate(self):
        """field `Maximum Cold Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Cold Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_cold_water_flow_rate` or None if not set

        """
        return self["Maximum Cold Water Flow Rate"]

    @maximum_cold_water_flow_rate.setter
    def maximum_cold_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Cold Water Flow Rate`"""
        self["Maximum Cold Water Flow Rate"] = value

    @property
    def minimum_cold_water_flow_rate(self):
        """field `Minimum Cold Water Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Cold Water Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_cold_water_flow_rate` or None if not set

        """
        return self["Minimum Cold Water Flow Rate"]

    @minimum_cold_water_flow_rate.setter
    def minimum_cold_water_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Cold Water Flow Rate`"""
        self["Minimum Cold Water Flow Rate"] = value

    @property
    def cooling_convergence_tolerance(self):
        """field `Cooling Convergence Tolerance`

        |  Default value: 0.001

        Args:
            value (float): value for IDD Field `Cooling Convergence Tolerance`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `cooling_convergence_tolerance` or None if not set

        """
        return self["Cooling Convergence Tolerance"]

    @cooling_convergence_tolerance.setter
    def cooling_convergence_tolerance(self, value=0.001):
        """Corresponds to IDD field `Cooling Convergence Tolerance`"""
        self["Cooling Convergence Tolerance"] = value

    @property
    def zone_mixer_name(self):
        """field `Zone Mixer Name`

        Args:
            value (str): value for IDD Field `Zone Mixer Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_mixer_name` or None if not set

        """
        return self["Zone Mixer Name"]

    @zone_mixer_name.setter
    def zone_mixer_name(self, value=None):
        """Corresponds to IDD field `Zone Mixer Name`"""
        self["Zone Mixer Name"] = value




class AirTerminalSingleDuctConstantVolumeFourPipeBeam(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam`
        Central air system terminal unit, single duct, constant volume,
        with heating and/or cooling.
        Operates as two-pipe unit if heating or cooling water is omitted.
        Heating and/or cooling can be scheduled off for dedicated ventilation.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'primary air availability schedule name',
                                       {'name': u'Primary Air Availability Schedule Name',
                                        'pyname': u'primary_air_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling availability schedule name',
                                       {'name': u'Cooling Availability Schedule Name',
                                        'pyname': u'cooling_availability_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating availability schedule name',
                                       {'name': u'Heating Availability Schedule Name',
                                        'pyname': u'heating_availability_schedule_name',
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
                                      (u'chilled water inlet node name',
                                       {'name': u'Chilled Water Inlet Node Name',
                                        'pyname': u'chilled_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'chilled water outlet node name',
                                       {'name': u'Chilled Water Outlet Node Name',
                                        'pyname': u'chilled_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'hot water inlet node name',
                                       {'name': u'Hot Water Inlet Node Name',
                                        'pyname': u'hot_water_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'hot water outlet node name',
                                       {'name': u'Hot Water Outlet Node Name',
                                        'pyname': u'hot_water_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'design primary air volume flow rate',
                                       {'name': u'Design Primary Air Volume Flow Rate',
                                        'pyname': u'design_primary_air_volume_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'design chilled water volume flow rate',
                                       {'name': u'Design Chilled Water Volume Flow Rate',
                                        'pyname': u'design_chilled_water_volume_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'design hot water volume flow rate',
                                       {'name': u'Design Hot Water Volume Flow Rate',
                                        'pyname': u'design_hot_water_volume_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'zone total beam length',
                                       {'name': u'Zone Total Beam Length',
                                        'pyname': u'zone_total_beam_length',
                                        'default': 'autosize',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'rated primary air flow rate per beam length',
                                       {'name': u'Rated Primary Air Flow Rate per Beam Length',
                                        'pyname': u'rated_primary_air_flow_rate_per_beam_length',
                                        'default': 0.035,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m'}),
                                      (u'beam rated cooling capacity per beam length',
                                       {'name': u'Beam Rated Cooling Capacity per Beam Length',
                                        'pyname': u'beam_rated_cooling_capacity_per_beam_length',
                                        'default': 600.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'beam rated cooling room air chilled water temperature difference',
                                       {'name': u'Beam Rated Cooling Room Air Chilled Water Temperature Difference',
                                        'pyname': u'beam_rated_cooling_room_air_chilled_water_temperature_difference',
                                        'default': 10.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'beam rated chilled water volume flow rate per beam length',
                                       {'name': u'Beam Rated Chilled Water Volume Flow Rate per Beam Length',
                                        'pyname': u'beam_rated_chilled_water_volume_flow_rate_per_beam_length',
                                        'default': 5e-05,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m'}),
                                      (u'beam cooling capacity temperature difference modification factor curve name',
                                       {'name': u'Beam Cooling Capacity Temperature Difference Modification Factor Curve Name',
                                        'pyname': u'beam_cooling_capacity_temperature_difference_modification_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'beam cooling capacity air flow modification factor curve name',
                                       {'name': u'Beam Cooling Capacity Air Flow Modification Factor Curve Name',
                                        'pyname': u'beam_cooling_capacity_air_flow_modification_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'beam cooling capacity chilled water flow modification factor curve name',
                                       {'name': u'Beam Cooling Capacity Chilled Water Flow Modification Factor Curve Name',
                                        'pyname': u'beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'beam rated heating capacity per beam length',
                                       {'name': u'Beam Rated Heating Capacity per Beam Length',
                                        'pyname': u'beam_rated_heating_capacity_per_beam_length',
                                        'default': 1500.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m'}),
                                      (u'beam rated heating room air hot water temperature difference',
                                       {'name': u'Beam Rated Heating Room Air Hot Water Temperature Difference',
                                        'pyname': u'beam_rated_heating_room_air_hot_water_temperature_difference',
                                        'default': 27.8,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'beam rated hot water volume flow rate per beam length',
                                       {'name': u'Beam Rated Hot Water Volume Flow Rate per Beam Length',
                                        'pyname': u'beam_rated_hot_water_volume_flow_rate_per_beam_length',
                                        'default': 5e-05,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-m'}),
                                      (u'beam heating capacity temperature difference modification factor curve name',
                                       {'name': u'Beam Heating Capacity Temperature Difference Modification Factor Curve Name',
                                        'pyname': u'beam_heating_capacity_temperature_difference_modification_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'beam heating capacity air flow modification factor curve name',
                                       {'name': u'Beam Heating Capacity Air Flow Modification Factor Curve Name',
                                        'pyname': u'beam_heating_capacity_air_flow_modification_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'beam heating capacity hot water flow modification factor curve name',
                                       {'name': u'Beam Heating Capacity Hot Water Flow Modification Factor Curve Name',
                                        'pyname': u'beam_heating_capacity_hot_water_flow_modification_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam',
               'pyname': u'AirTerminalSingleDuctConstantVolumeFourPipeBeam',
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
    def primary_air_availability_schedule_name(self):
        """field `Primary Air Availability Schedule Name`

        |  Primary air is supplied by central air handling unit and must be on for heating or cooling.
        |  Schedule value > 0 means the primary air supply is available.
        |  If this field is blank, the primary air supply is always available.

        Args:
            value (str): value for IDD Field `Primary Air Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `primary_air_availability_schedule_name` or None if not set

        """
        return self["Primary Air Availability Schedule Name"]

    @primary_air_availability_schedule_name.setter
    def primary_air_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Primary Air Availability Schedule Name`"""
        self["Primary Air Availability Schedule Name"] = value

    @property
    def cooling_availability_schedule_name(self):
        """field `Cooling Availability Schedule Name`

        |  Cooling operation can be controlled separately using this availability schedule.
        |  Schedule value > 0 means beam cooling is available.
        |  If this field is blank, the beam cooling is always available (as long as primary air is also available).

        Args:
            value (str): value for IDD Field `Cooling Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_availability_schedule_name` or None if not set

        """
        return self["Cooling Availability Schedule Name"]

    @cooling_availability_schedule_name.setter
    def cooling_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Cooling Availability Schedule Name`"""
        self["Cooling Availability Schedule Name"] = value

    @property
    def heating_availability_schedule_name(self):
        """field `Heating Availability Schedule Name`

        |  Heating operation can be controlled separately using this availability schedule.
        |  Schedule value > 0 means beam heating is available.
        |  If this field is blank, the beam heating is always available (as long as primary air is also available).

        Args:
            value (str): value for IDD Field `Heating Availability Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_availability_schedule_name` or None if not set

        """
        return self["Heating Availability Schedule Name"]

    @heating_availability_schedule_name.setter
    def heating_availability_schedule_name(self, value=None):
        """Corresponds to IDD field `Heating Availability Schedule Name`"""
        self["Heating Availability Schedule Name"] = value

    @property
    def primary_air_inlet_node_name(self):
        """field `Primary Air Inlet Node Name`

        |  Name of the air system node for primary supply air entering the air distribution unit.

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

        |  Name of the air system node for primary supply air leaving the air distribution unit and entering the zone.

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
    def chilled_water_inlet_node_name(self):
        """field `Chilled Water Inlet Node Name`

        |  Name of the plant system node for chilled water entering the beam.
        |  The two chilled water nodes can (only) be omitted to model a two-pipe heating only beam.

        Args:
            value (str): value for IDD Field `Chilled Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set

        """
        return self["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Chilled Water Inlet Node Name`"""
        self["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """field `Chilled Water Outlet Node Name`

        |  Name of the plant system node for chilled water leaving the beam.

        Args:
            value (str): value for IDD Field `Chilled Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set

        """
        return self["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Chilled Water Outlet Node Name`"""
        self["Chilled Water Outlet Node Name"] = value

    @property
    def hot_water_inlet_node_name(self):
        """field `Hot Water Inlet Node Name`

        |  Name of the plant system node for hot water entering the beam.
        |  The two hot water nodes can (only) be omitted to model a two-pipe cooling-only beam.

        Args:
            value (str): value for IDD Field `Hot Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_inlet_node_name` or None if not set

        """
        return self["Hot Water Inlet Node Name"]

    @hot_water_inlet_node_name.setter
    def hot_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water Inlet Node Name`"""
        self["Hot Water Inlet Node Name"] = value

    @property
    def hot_water_outlet_node_name(self):
        """field `Hot Water Outlet Node Name`

        |  Name of the plant system node for hot water leaving the beam.

        Args:
            value (str): value for IDD Field `Hot Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_water_outlet_node_name` or None if not set

        """
        return self["Hot Water Outlet Node Name"]

    @hot_water_outlet_node_name.setter
    def hot_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Water Outlet Node Name`"""
        self["Hot Water Outlet Node Name"] = value

    @property
    def design_primary_air_volume_flow_rate(self):
        """field `Design Primary Air Volume Flow Rate`

        |  Units: m3/s
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Design Primary Air Volume Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_primary_air_volume_flow_rate` or None if not set

        """
        return self["Design Primary Air Volume Flow Rate"]

    @design_primary_air_volume_flow_rate.setter
    def design_primary_air_volume_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Design Primary Air Volume Flow Rate`"""
        self["Design Primary Air Volume Flow Rate"] = value

    @property
    def design_chilled_water_volume_flow_rate(self):
        """field `Design Chilled Water Volume Flow Rate`

        |  Units: m3/s
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Design Chilled Water Volume Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_chilled_water_volume_flow_rate` or None if not set

        """
        return self["Design Chilled Water Volume Flow Rate"]

    @design_chilled_water_volume_flow_rate.setter
    def design_chilled_water_volume_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Design Chilled Water Volume Flow Rate`"""
        self["Design Chilled Water Volume Flow Rate"] = value

    @property
    def design_hot_water_volume_flow_rate(self):
        """field `Design Hot Water Volume Flow Rate`

        |  Units: m3/s
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Design Hot Water Volume Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_hot_water_volume_flow_rate` or None if not set

        """
        return self["Design Hot Water Volume Flow Rate"]

    @design_hot_water_volume_flow_rate.setter
    def design_hot_water_volume_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Design Hot Water Volume Flow Rate`"""
        self["Design Hot Water Volume Flow Rate"] = value

    @property
    def zone_total_beam_length(self):
        """field `Zone Total Beam Length`

        |  Sum of the length of all the beam units in the zone represented by this terminal unit.
        |  Units: m
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Zone Total Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `zone_total_beam_length` or None if not set

        """
        return self["Zone Total Beam Length"]

    @zone_total_beam_length.setter
    def zone_total_beam_length(self, value="autosize"):
        """Corresponds to IDD field `Zone Total Beam Length`"""
        self["Zone Total Beam Length"] = value

    @property
    def rated_primary_air_flow_rate_per_beam_length(self):
        """field `Rated Primary Air Flow Rate per Beam Length`

        |  Primary air supply flow rate normalized by beam length.
        |  Units: m3/s-m
        |  Default value: 0.035

        Args:
            value (float): value for IDD Field `Rated Primary Air Flow Rate per Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_primary_air_flow_rate_per_beam_length` or None if not set

        """
        return self["Rated Primary Air Flow Rate per Beam Length"]

    @rated_primary_air_flow_rate_per_beam_length.setter
    def rated_primary_air_flow_rate_per_beam_length(self, value=0.035):
        """Corresponds to IDD field `Rated Primary Air Flow Rate per Beam
        Length`"""
        self["Rated Primary Air Flow Rate per Beam Length"] = value

    @property
    def beam_rated_cooling_capacity_per_beam_length(self):
        """field `Beam Rated Cooling Capacity per Beam Length`

        |  Sensible cooling capacity per meter of beam length at the rating point.
        |  Units: W/m
        |  Default value: 600.0

        Args:
            value (float): value for IDD Field `Beam Rated Cooling Capacity per Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `beam_rated_cooling_capacity_per_beam_length` or None if not set

        """
        return self["Beam Rated Cooling Capacity per Beam Length"]

    @beam_rated_cooling_capacity_per_beam_length.setter
    def beam_rated_cooling_capacity_per_beam_length(self, value=600.0):
        """Corresponds to IDD field `Beam Rated Cooling Capacity per Beam
        Length`"""
        self["Beam Rated Cooling Capacity per Beam Length"] = value

    @property
    def beam_rated_cooling_room_air_chilled_water_temperature_difference(self):
        """field `Beam Rated Cooling Room Air Chilled Water Temperature
        Difference`

        |  Difference in temperature between the zone air and the entering chilled water at the rating point.
        |  Units: deltaC
        |  Default value: 10.0

        Args:
            value (float): value for IDD Field `Beam Rated Cooling Room Air Chilled Water Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `beam_rated_cooling_room_air_chilled_water_temperature_difference` or None if not set

        """
        return self[
            "Beam Rated Cooling Room Air Chilled Water Temperature Difference"]

    @beam_rated_cooling_room_air_chilled_water_temperature_difference.setter
    def beam_rated_cooling_room_air_chilled_water_temperature_difference(
            self,
            value=10.0):
        """Corresponds to IDD field `Beam Rated Cooling Room Air Chilled Water
        Temperature Difference`"""
        self[
            "Beam Rated Cooling Room Air Chilled Water Temperature Difference"] = value

    @property
    def beam_rated_chilled_water_volume_flow_rate_per_beam_length(self):
        """field `Beam Rated Chilled Water Volume Flow Rate per Beam Length`

        |  The volume flow rate of chilled water per meter of beam length at the rating point.
        |  Units: m3/s-m
        |  Default value: 5e-05

        Args:
            value (float): value for IDD Field `Beam Rated Chilled Water Volume Flow Rate per Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `beam_rated_chilled_water_volume_flow_rate_per_beam_length` or None if not set

        """
        return self[
            "Beam Rated Chilled Water Volume Flow Rate per Beam Length"]

    @beam_rated_chilled_water_volume_flow_rate_per_beam_length.setter
    def beam_rated_chilled_water_volume_flow_rate_per_beam_length(
            self,
            value=5e-05):
        """Corresponds to IDD field `Beam Rated Chilled Water Volume Flow Rate
        per Beam Length`"""
        self[
            "Beam Rated Chilled Water Volume Flow Rate per Beam Length"] = value

    @property
    def beam_cooling_capacity_temperature_difference_modification_factor_curve_name(
            self):
        """field `Beam Cooling Capacity Temperature Difference Modification
        Factor Curve Name`

        |  Adjusts beam cooling capacity when the temperature difference between entering water and zone air
        |  is different than at the rating point.  Single independent variable is the ratio of the current
        |  temperature difference divided by the rating point temperature difference.
        |  This field is required when beam is connected to a chilled water plant.

        Args:
            value (str): value for IDD Field `Beam Cooling Capacity Temperature Difference Modification Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_cooling_capacity_temperature_difference_modification_factor_curve_name` or None if not set

        """
        return self[
            "Beam Cooling Capacity Temperature Difference Modification Factor Curve Name"]

    @beam_cooling_capacity_temperature_difference_modification_factor_curve_name.setter
    def beam_cooling_capacity_temperature_difference_modification_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Beam Cooling Capacity Temperature
        Difference Modification Factor Curve Name`"""
        self[
            "Beam Cooling Capacity Temperature Difference Modification Factor Curve Name"] = value

    @property
    def beam_cooling_capacity_air_flow_modification_factor_curve_name(self):
        """field `Beam Cooling Capacity Air Flow Modification Factor Curve
        Name`

        |  Adjusts beam cooling capacity when the primary air supply flow rate is different
        |  than at the rating point. The single independent variable is the current normalized
        |  air flow rate divided by the normalized air flow rate at the rating point.
        |  This field is required when beam is connected to a chilled water plant.

        Args:
            value (str): value for IDD Field `Beam Cooling Capacity Air Flow Modification Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_cooling_capacity_air_flow_modification_factor_curve_name` or None if not set

        """
        return self[
            "Beam Cooling Capacity Air Flow Modification Factor Curve Name"]

    @beam_cooling_capacity_air_flow_modification_factor_curve_name.setter
    def beam_cooling_capacity_air_flow_modification_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Beam Cooling Capacity Air Flow
        Modification Factor Curve Name`"""
        self[
            "Beam Cooling Capacity Air Flow Modification Factor Curve Name"] = value

    @property
    def beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name(
            self):
        """field `Beam Cooling Capacity Chilled Water Flow Modification Factor
        Curve Name`

        |  Adjusts beam cooling capacity when the normalized chilled water flow rate is different
        |  than at the rating point. The single independent variable is the current normalized
        |  chilled water flow rate divided by the normalized chilled water flow rate at the rating point.
        |  This field is required when beam is connected to a chilled water plant.

        Args:
            value (str): value for IDD Field `Beam Cooling Capacity Chilled Water Flow Modification Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name` or None if not set

        """
        return self[
            "Beam Cooling Capacity Chilled Water Flow Modification Factor Curve Name"]

    @beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name.setter
    def beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Beam Cooling Capacity Chilled Water Flow
        Modification Factor Curve Name`"""
        self[
            "Beam Cooling Capacity Chilled Water Flow Modification Factor Curve Name"] = value

    @property
    def beam_rated_heating_capacity_per_beam_length(self):
        """field `Beam Rated Heating Capacity per Beam Length`

        |  Sensible heating capacity per meter of beam length at the rating point.
        |  Units: W/m
        |  Default value: 1500.0

        Args:
            value (float): value for IDD Field `Beam Rated Heating Capacity per Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `beam_rated_heating_capacity_per_beam_length` or None if not set

        """
        return self["Beam Rated Heating Capacity per Beam Length"]

    @beam_rated_heating_capacity_per_beam_length.setter
    def beam_rated_heating_capacity_per_beam_length(self, value=1500.0):
        """Corresponds to IDD field `Beam Rated Heating Capacity per Beam
        Length`"""
        self["Beam Rated Heating Capacity per Beam Length"] = value

    @property
    def beam_rated_heating_room_air_hot_water_temperature_difference(self):
        """field `Beam Rated Heating Room Air Hot Water Temperature Difference`

        |  Difference in temperature between the zone air and the entering hot water at the rating point.
        |  Units: deltaC
        |  Default value: 27.8

        Args:
            value (float): value for IDD Field `Beam Rated Heating Room Air Hot Water Temperature Difference`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `beam_rated_heating_room_air_hot_water_temperature_difference` or None if not set

        """
        return self[
            "Beam Rated Heating Room Air Hot Water Temperature Difference"]

    @beam_rated_heating_room_air_hot_water_temperature_difference.setter
    def beam_rated_heating_room_air_hot_water_temperature_difference(
            self,
            value=27.8):
        """Corresponds to IDD field `Beam Rated Heating Room Air Hot Water
        Temperature Difference`"""
        self[
            "Beam Rated Heating Room Air Hot Water Temperature Difference"] = value

    @property
    def beam_rated_hot_water_volume_flow_rate_per_beam_length(self):
        """field `Beam Rated Hot Water Volume Flow Rate per Beam Length`

        |  The volume flow rate of hoy water per meter of beam length at the rating point.
        |  Units: m3/s-m
        |  Default value: 5e-05

        Args:
            value (float): value for IDD Field `Beam Rated Hot Water Volume Flow Rate per Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `beam_rated_hot_water_volume_flow_rate_per_beam_length` or None if not set

        """
        return self["Beam Rated Hot Water Volume Flow Rate per Beam Length"]

    @beam_rated_hot_water_volume_flow_rate_per_beam_length.setter
    def beam_rated_hot_water_volume_flow_rate_per_beam_length(
            self,
            value=5e-05):
        """Corresponds to IDD field `Beam Rated Hot Water Volume Flow Rate per
        Beam Length`"""
        self["Beam Rated Hot Water Volume Flow Rate per Beam Length"] = value

    @property
    def beam_heating_capacity_temperature_difference_modification_factor_curve_name(
            self):
        """field `Beam Heating Capacity Temperature Difference Modification
        Factor Curve Name`

        |  Adjusts beam heating capacity when the temperature difference between entering water and zone air
        |  is different than at the rating point.  Single independent variable is the ratio of the current
        |  temperature difference divided by the rating point temperature difference.
        |  This field is required when beam is connected to a hot water plant.

        Args:
            value (str): value for IDD Field `Beam Heating Capacity Temperature Difference Modification Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_heating_capacity_temperature_difference_modification_factor_curve_name` or None if not set

        """
        return self[
            "Beam Heating Capacity Temperature Difference Modification Factor Curve Name"]

    @beam_heating_capacity_temperature_difference_modification_factor_curve_name.setter
    def beam_heating_capacity_temperature_difference_modification_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Beam Heating Capacity Temperature
        Difference Modification Factor Curve Name`"""
        self[
            "Beam Heating Capacity Temperature Difference Modification Factor Curve Name"] = value

    @property
    def beam_heating_capacity_air_flow_modification_factor_curve_name(self):
        """field `Beam Heating Capacity Air Flow Modification Factor Curve
        Name`

        |  Adjusts beam heating capacity when the primary air supply flow rate is different
        |  than at the rating point. The single independent variable is the current normalized
        |  air flow rate divided by the normalized air flow rate at the rating point.
        |  This field is required when beam is connected to a hot water plant.

        Args:
            value (str): value for IDD Field `Beam Heating Capacity Air Flow Modification Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_heating_capacity_air_flow_modification_factor_curve_name` or None if not set

        """
        return self[
            "Beam Heating Capacity Air Flow Modification Factor Curve Name"]

    @beam_heating_capacity_air_flow_modification_factor_curve_name.setter
    def beam_heating_capacity_air_flow_modification_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Beam Heating Capacity Air Flow
        Modification Factor Curve Name`"""
        self[
            "Beam Heating Capacity Air Flow Modification Factor Curve Name"] = value

    @property
    def beam_heating_capacity_hot_water_flow_modification_factor_curve_name(
            self):
        """field `Beam Heating Capacity Hot Water Flow Modification Factor
        Curve Name`

        |  Adjusts beam heating capacity when the normalized hot water flow rate is different
        |  than at the rating point. The single independent variable is the current normalized
        |  hot water flow rate divided by the normalized hot water flow rate at the rating point.
        |  This field is required when beam is connected to a hot water plant.

        Args:
            value (str): value for IDD Field `Beam Heating Capacity Hot Water Flow Modification Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `beam_heating_capacity_hot_water_flow_modification_factor_curve_name` or None if not set

        """
        return self[
            "Beam Heating Capacity Hot Water Flow Modification Factor Curve Name"]

    @beam_heating_capacity_hot_water_flow_modification_factor_curve_name.setter
    def beam_heating_capacity_hot_water_flow_modification_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Beam Heating Capacity Hot Water Flow
        Modification Factor Curve Name`"""
        self[
            "Beam Heating Capacity Hot Water Flow Modification Factor Curve Name"] = value




class AirTerminalSingleDuctConstantVolumeCooledBeam(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:ConstantVolume:CooledBeam`
        Central air system terminal unit, single duct, constant volume, with cooled beam
        (active or passive).
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
                                      (u'cooled beam type',
                                       {'name': u'Cooled Beam Type',
                                        'pyname': u'cooled_beam_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Active',
                                                            u'Passive'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
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
                                      (u'chilled water inlet node name',
                                       {'name': u'Chilled Water Inlet Node Name',
                                        'pyname': u'chilled_water_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'chilled water outlet node name',
                                       {'name': u'Chilled Water Outlet Node Name',
                                        'pyname': u'chilled_water_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply air volumetric flow rate',
                                       {'name': u'Supply Air Volumetric Flow Rate',
                                        'pyname': u'supply_air_volumetric_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'maximum total chilled water volumetric flow rate',
                                       {'name': u'Maximum Total Chilled Water Volumetric Flow Rate',
                                        'pyname': u'maximum_total_chilled_water_volumetric_flow_rate',
                                        'default': 'autosize',
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'number of beams',
                                       {'name': u'Number of Beams',
                                        'pyname': u'number_of_beams',
                                        'default': 'autosize',
                                        'minimum>': 0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'beam length',
                                       {'name': u'Beam Length',
                                        'pyname': u'beam_length',
                                        'default': 'autosize',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'design inlet water temperature',
                                       {'name': u'Design Inlet Water Temperature',
                                        'pyname': u'design_inlet_water_temperature',
                                        'default': 15.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'design outlet water temperature',
                                       {'name': u'Design Outlet Water Temperature',
                                        'pyname': u'design_outlet_water_temperature',
                                        'default': 17.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'coil surface area per coil length',
                                       {'name': u'Coil Surface Area per Coil Length',
                                        'pyname': u'coil_surface_area_per_coil_length',
                                        'default': 5.422,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2/m'}),
                                      (u'model parameter a',
                                       {'name': u'Model Parameter a',
                                        'pyname': u'model_parameter_a',
                                        'default': 15.3,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'model parameter n1',
                                       {'name': u'Model Parameter n1',
                                        'pyname': u'model_parameter_n1',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'model parameter n2',
                                       {'name': u'Model Parameter n2',
                                        'pyname': u'model_parameter_n2',
                                        'default': 0.84,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'model parameter n3',
                                       {'name': u'Model Parameter n3',
                                        'pyname': u'model_parameter_n3',
                                        'default': 0.12,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'model parameter a0',
                                       {'name': u'Model Parameter a0',
                                        'pyname': u'model_parameter_a0',
                                        'default': 0.171,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm2/m'}),
                                      (u'model parameter k1',
                                       {'name': u'Model Parameter K1',
                                        'pyname': u'model_parameter_k1',
                                        'default': 0.0057,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'model parameter n',
                                       {'name': u'Model Parameter n',
                                        'pyname': u'model_parameter_n',
                                        'default': 0.4,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'coefficient of induction kin',
                                       {'name': u'Coefficient of Induction Kin',
                                        'pyname': u'coefficient_of_induction_kin',
                                        'default': 'Autocalculate',
                                        'maximum': 4.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real'}),
                                      (u'leaving pipe inside diameter',
                                       {'name': u'Leaving Pipe Inside Diameter',
                                        'pyname': u'leaving_pipe_inside_diameter',
                                        'default': 0.0145,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 23,
               'name': u'AirTerminal:SingleDuct:ConstantVolume:CooledBeam',
               'pyname': u'AirTerminalSingleDuctConstantVolumeCooledBeam',
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
    def cooled_beam_type(self):
        """field `Cooled Beam Type`

        Args:
            value (str): value for IDD Field `Cooled Beam Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooled_beam_type` or None if not set

        """
        return self["Cooled Beam Type"]

    @cooled_beam_type.setter
    def cooled_beam_type(self, value=None):
        """Corresponds to IDD field `Cooled Beam Type`"""
        self["Cooled Beam Type"] = value

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
    def chilled_water_inlet_node_name(self):
        """field `Chilled Water Inlet Node Name`

        Args:
            value (str): value for IDD Field `Chilled Water Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `chilled_water_inlet_node_name` or None if not set

        """
        return self["Chilled Water Inlet Node Name"]

    @chilled_water_inlet_node_name.setter
    def chilled_water_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Chilled Water Inlet Node Name`"""
        self["Chilled Water Inlet Node Name"] = value

    @property
    def chilled_water_outlet_node_name(self):
        """field `Chilled Water Outlet Node Name`

        Args:
            value (str): value for IDD Field `Chilled Water Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `chilled_water_outlet_node_name` or None if not set

        """
        return self["Chilled Water Outlet Node Name"]

    @chilled_water_outlet_node_name.setter
    def chilled_water_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Chilled Water Outlet Node Name`"""
        self["Chilled Water Outlet Node Name"] = value

    @property
    def supply_air_volumetric_flow_rate(self):
        """field `Supply Air Volumetric Flow Rate`

        |  Units: m3/s
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Volumetric Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `supply_air_volumetric_flow_rate` or None if not set

        """
        return self["Supply Air Volumetric Flow Rate"]

    @supply_air_volumetric_flow_rate.setter
    def supply_air_volumetric_flow_rate(self, value="autosize"):
        """Corresponds to IDD field `Supply Air Volumetric Flow Rate`"""
        self["Supply Air Volumetric Flow Rate"] = value

    @property
    def maximum_total_chilled_water_volumetric_flow_rate(self):
        """field `Maximum Total Chilled Water Volumetric Flow Rate`

        |  Units: m3/s
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Total Chilled Water Volumetric Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_total_chilled_water_volumetric_flow_rate` or None if not set

        """
        return self["Maximum Total Chilled Water Volumetric Flow Rate"]

    @maximum_total_chilled_water_volumetric_flow_rate.setter
    def maximum_total_chilled_water_volumetric_flow_rate(
            self,
            value="autosize"):
        """Corresponds to IDD field `Maximum Total Chilled Water Volumetric
        Flow Rate`"""
        self["Maximum Total Chilled Water Volumetric Flow Rate"] = value

    @property
    def number_of_beams(self):
        """field `Number of Beams`

        |  Number of individual beam units in the zone
        |  Default value: "autosize"

        Args:
            value (int or "Autosize"): value for IDD Field `Number of Beams`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int or "Autosize": the value of `number_of_beams` or None if not set

        """
        return self["Number of Beams"]

    @number_of_beams.setter
    def number_of_beams(self, value="autosize"):
        """Corresponds to IDD field `Number of Beams`"""
        self["Number of Beams"] = value

    @property
    def beam_length(self):
        """field `Beam Length`

        |  Length of an individual beam unit
        |  Units: m
        |  Default value: "autosize"

        Args:
            value (float or "Autosize"): value for IDD Field `Beam Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `beam_length` or None if not set

        """
        return self["Beam Length"]

    @beam_length.setter
    def beam_length(self, value="autosize"):
        """Corresponds to IDD field `Beam Length`"""
        self["Beam Length"] = value

    @property
    def design_inlet_water_temperature(self):
        """field `Design Inlet Water Temperature`

        |  Units: C
        |  Default value: 15.0

        Args:
            value (float): value for IDD Field `Design Inlet Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_inlet_water_temperature` or None if not set

        """
        return self["Design Inlet Water Temperature"]

    @design_inlet_water_temperature.setter
    def design_inlet_water_temperature(self, value=15.0):
        """Corresponds to IDD field `Design Inlet Water Temperature`"""
        self["Design Inlet Water Temperature"] = value

    @property
    def design_outlet_water_temperature(self):
        """field `Design Outlet Water Temperature`

        |  Units: C
        |  Default value: 17.0

        Args:
            value (float): value for IDD Field `Design Outlet Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `design_outlet_water_temperature` or None if not set

        """
        return self["Design Outlet Water Temperature"]

    @design_outlet_water_temperature.setter
    def design_outlet_water_temperature(self, value=17.0):
        """Corresponds to IDD field `Design Outlet Water Temperature`"""
        self["Design Outlet Water Temperature"] = value

    @property
    def coil_surface_area_per_coil_length(self):
        """field `Coil Surface Area per Coil Length`

        |  Units: m2/m
        |  Default value: 5.422

        Args:
            value (float): value for IDD Field `Coil Surface Area per Coil Length`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `coil_surface_area_per_coil_length` or None if not set

        """
        return self["Coil Surface Area per Coil Length"]

    @coil_surface_area_per_coil_length.setter
    def coil_surface_area_per_coil_length(self, value=5.422):
        """Corresponds to IDD field `Coil Surface Area per Coil Length`"""
        self["Coil Surface Area per Coil Length"] = value

    @property
    def model_parameter_a(self):
        """field `Model Parameter a`

        |  Default value: 15.3

        Args:
            value (float): value for IDD Field `Model Parameter a`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_a` or None if not set

        """
        return self["Model Parameter a"]

    @model_parameter_a.setter
    def model_parameter_a(self, value=15.3):
        """Corresponds to IDD field `Model Parameter a`"""
        self["Model Parameter a"] = value

    @property
    def model_parameter_n1(self):
        """field `Model Parameter n1`

        Args:
            value (float): value for IDD Field `Model Parameter n1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_n1` or None if not set

        """
        return self["Model Parameter n1"]

    @model_parameter_n1.setter
    def model_parameter_n1(self, value=None):
        """Corresponds to IDD field `Model Parameter n1`"""
        self["Model Parameter n1"] = value

    @property
    def model_parameter_n2(self):
        """field `Model Parameter n2`

        |  Default value: 0.84

        Args:
            value (float): value for IDD Field `Model Parameter n2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_n2` or None if not set

        """
        return self["Model Parameter n2"]

    @model_parameter_n2.setter
    def model_parameter_n2(self, value=0.84):
        """Corresponds to IDD field `Model Parameter n2`"""
        self["Model Parameter n2"] = value

    @property
    def model_parameter_n3(self):
        """field `Model Parameter n3`

        |  Default value: 0.12

        Args:
            value (float): value for IDD Field `Model Parameter n3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_n3` or None if not set

        """
        return self["Model Parameter n3"]

    @model_parameter_n3.setter
    def model_parameter_n3(self, value=0.12):
        """Corresponds to IDD field `Model Parameter n3`"""
        self["Model Parameter n3"] = value

    @property
    def model_parameter_a0(self):
        """field `Model Parameter a0`

        |  Free area of the coil in plan view per unit beam length
        |  Units: m2/m
        |  Default value: 0.171

        Args:
            value (float): value for IDD Field `Model Parameter a0`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_a0` or None if not set

        """
        return self["Model Parameter a0"]

    @model_parameter_a0.setter
    def model_parameter_a0(self, value=0.171):
        """Corresponds to IDD field `Model Parameter a0`"""
        self["Model Parameter a0"] = value

    @property
    def model_parameter_k1(self):
        """field `Model Parameter K1`

        |  Default value: 0.0057

        Args:
            value (float): value for IDD Field `Model Parameter K1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_k1` or None if not set

        """
        return self["Model Parameter K1"]

    @model_parameter_k1.setter
    def model_parameter_k1(self, value=0.0057):
        """Corresponds to IDD field `Model Parameter K1`"""
        self["Model Parameter K1"] = value

    @property
    def model_parameter_n(self):
        """field `Model Parameter n`

        |  Default value: 0.4

        Args:
            value (float): value for IDD Field `Model Parameter n`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `model_parameter_n` or None if not set

        """
        return self["Model Parameter n"]

    @model_parameter_n.setter
    def model_parameter_n(self, value=0.4):
        """Corresponds to IDD field `Model Parameter n`"""
        self["Model Parameter n"] = value

    @property
    def coefficient_of_induction_kin(self):
        """field `Coefficient of Induction Kin`

        |  Default value: "Autocalculate"
        |  value <= 4.0

        Args:
            value (float or "Autocalculate"): value for IDD Field `Coefficient of Induction Kin`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `coefficient_of_induction_kin` or None if not set

        """
        return self["Coefficient of Induction Kin"]

    @coefficient_of_induction_kin.setter
    def coefficient_of_induction_kin(self, value="Autocalculate"):
        """Corresponds to IDD field `Coefficient of Induction Kin`"""
        self["Coefficient of Induction Kin"] = value

    @property
    def leaving_pipe_inside_diameter(self):
        """field `Leaving Pipe Inside Diameter`

        |  Units: m
        |  Default value: 0.0145

        Args:
            value (float): value for IDD Field `Leaving Pipe Inside Diameter`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `leaving_pipe_inside_diameter` or None if not set

        """
        return self["Leaving Pipe Inside Diameter"]

    @leaving_pipe_inside_diameter.setter
    def leaving_pipe_inside_diameter(self, value=0.0145):
        """Corresponds to IDD field `Leaving Pipe Inside Diameter`"""
        self["Leaving Pipe Inside Diameter"] = value




class AirTerminalSingleDuctInletSideMixer(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:InletSideMixer`
        The inlet side mixer air terminal unit provides a means of supplying central system air
        to the air inlet of a zone AC unit such as a four pipe fan coil. Normally the central air
        would be ventilation air from a dedicated outdoor air system (DOAS).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zonehvac terminal unit object type',
                                       {'name': u'ZoneHVAC Terminal Unit Object Type',
                                        'pyname': u'zonehvac_terminal_unit_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneHVAC:FourPipeFanCoil',
                                                            u'ZoneHVAC:WaterToAirHeatPump'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zonehvac terminal unit name',
                                       {'name': u'ZoneHVAC Terminal Unit Name',
                                        'pyname': u'zonehvac_terminal_unit_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'terminal unit outlet node name',
                                       {'name': u'Terminal Unit Outlet Node Name',
                                        'pyname': u'terminal_unit_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'terminal unit primary air inlet node name',
                                       {'name': u'Terminal Unit Primary Air Inlet Node Name',
                                        'pyname': u'terminal_unit_primary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'terminal unit secondary air inlet node name',
                                       {'name': u'Terminal Unit Secondary Air Inlet Node Name',
                                        'pyname': u'terminal_unit_secondary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:InletSideMixer',
               'pyname': u'AirTerminalSingleDuctInletSideMixer',
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
    def zonehvac_terminal_unit_object_type(self):
        """field `ZoneHVAC Terminal Unit Object Type`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zonehvac_terminal_unit_object_type` or None if not set

        """
        return self["ZoneHVAC Terminal Unit Object Type"]

    @zonehvac_terminal_unit_object_type.setter
    def zonehvac_terminal_unit_object_type(self, value=None):
        """Corresponds to IDD field `ZoneHVAC Terminal Unit Object Type`"""
        self["ZoneHVAC Terminal Unit Object Type"] = value

    @property
    def zonehvac_terminal_unit_name(self):
        """field `ZoneHVAC Terminal Unit Name`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zonehvac_terminal_unit_name` or None if not set

        """
        return self["ZoneHVAC Terminal Unit Name"]

    @zonehvac_terminal_unit_name.setter
    def zonehvac_terminal_unit_name(self, value=None):
        """Corresponds to IDD field `ZoneHVAC Terminal Unit Name`"""
        self["ZoneHVAC Terminal Unit Name"] = value

    @property
    def terminal_unit_outlet_node_name(self):
        """field `Terminal Unit Outlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_outlet_node_name` or None if not set

        """
        return self["Terminal Unit Outlet Node Name"]

    @terminal_unit_outlet_node_name.setter
    def terminal_unit_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Outlet Node Name`"""
        self["Terminal Unit Outlet Node Name"] = value

    @property
    def terminal_unit_primary_air_inlet_node_name(self):
        """field `Terminal Unit Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Primary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_primary_air_inlet_node_name` or None if not set

        """
        return self["Terminal Unit Primary Air Inlet Node Name"]

    @terminal_unit_primary_air_inlet_node_name.setter
    def terminal_unit_primary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Primary Air Inlet Node
        Name`"""
        self["Terminal Unit Primary Air Inlet Node Name"] = value

    @property
    def terminal_unit_secondary_air_inlet_node_name(self):
        """field `Terminal Unit Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Secondary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_secondary_air_inlet_node_name` or None if not set

        """
        return self["Terminal Unit Secondary Air Inlet Node Name"]

    @terminal_unit_secondary_air_inlet_node_name.setter
    def terminal_unit_secondary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Secondary Air Inlet Node
        Name`"""
        self["Terminal Unit Secondary Air Inlet Node Name"] = value




class AirTerminalSingleDuctSupplySideMixer(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:SupplySideMixer`
        The supply side mixer air terminal unit provides a means of supplying central system air
        to the air outlet of a zone AC unit such as a four pipe fan coil. Normally the central air
        would be ventilation air from a dedicated outdoor air system (DOAS).
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zonehvac terminal unit object type',
                                       {'name': u'ZoneHVAC Terminal Unit Object Type',
                                        'pyname': u'zonehvac_terminal_unit_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ZoneHVAC:FourPipeFanCoil',
                                                            u'ZoneHVAC:WaterToAirHeatPump'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zonehvac terminal unit name',
                                       {'name': u'ZoneHVAC Terminal Unit Name',
                                        'pyname': u'zonehvac_terminal_unit_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'terminal unit outlet node name',
                                       {'name': u'Terminal Unit Outlet Node Name',
                                        'pyname': u'terminal_unit_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'terminal unit primary air inlet node name',
                                       {'name': u'Terminal Unit Primary Air Inlet Node Name',
                                        'pyname': u'terminal_unit_primary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'terminal unit secondary air inlet node name',
                                       {'name': u'Terminal Unit Secondary Air Inlet Node Name',
                                        'pyname': u'terminal_unit_secondary_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 0,
               'name': u'AirTerminal:SingleDuct:SupplySideMixer',
               'pyname': u'AirTerminalSingleDuctSupplySideMixer',
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
    def zonehvac_terminal_unit_object_type(self):
        """field `ZoneHVAC Terminal Unit Object Type`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zonehvac_terminal_unit_object_type` or None if not set

        """
        return self["ZoneHVAC Terminal Unit Object Type"]

    @zonehvac_terminal_unit_object_type.setter
    def zonehvac_terminal_unit_object_type(self, value=None):
        """Corresponds to IDD field `ZoneHVAC Terminal Unit Object Type`"""
        self["ZoneHVAC Terminal Unit Object Type"] = value

    @property
    def zonehvac_terminal_unit_name(self):
        """field `ZoneHVAC Terminal Unit Name`

        Args:
            value (str): value for IDD Field `ZoneHVAC Terminal Unit Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zonehvac_terminal_unit_name` or None if not set

        """
        return self["ZoneHVAC Terminal Unit Name"]

    @zonehvac_terminal_unit_name.setter
    def zonehvac_terminal_unit_name(self, value=None):
        """Corresponds to IDD field `ZoneHVAC Terminal Unit Name`"""
        self["ZoneHVAC Terminal Unit Name"] = value

    @property
    def terminal_unit_outlet_node_name(self):
        """field `Terminal Unit Outlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_outlet_node_name` or None if not set

        """
        return self["Terminal Unit Outlet Node Name"]

    @terminal_unit_outlet_node_name.setter
    def terminal_unit_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Outlet Node Name`"""
        self["Terminal Unit Outlet Node Name"] = value

    @property
    def terminal_unit_primary_air_inlet_node_name(self):
        """field `Terminal Unit Primary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Primary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_primary_air_inlet_node_name` or None if not set

        """
        return self["Terminal Unit Primary Air Inlet Node Name"]

    @terminal_unit_primary_air_inlet_node_name.setter
    def terminal_unit_primary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Primary Air Inlet Node
        Name`"""
        self["Terminal Unit Primary Air Inlet Node Name"] = value

    @property
    def terminal_unit_secondary_air_inlet_node_name(self):
        """field `Terminal Unit Secondary Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Terminal Unit Secondary Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `terminal_unit_secondary_air_inlet_node_name` or None if not set

        """
        return self["Terminal Unit Secondary Air Inlet Node Name"]

    @terminal_unit_secondary_air_inlet_node_name.setter
    def terminal_unit_secondary_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Terminal Unit Secondary Air Inlet Node
        Name`"""
        self["Terminal Unit Secondary Air Inlet Node Name"] = value




class AirTerminalDualDuctConstantVolume(DataObject):

    """ Corresponds to IDD object `AirTerminal:DualDuct:ConstantVolume`
        Central air system terminal unit, dual duct, constant volume.
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
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'hot air inlet node name',
                                       {'name': u'Hot Air Inlet Node Name',
                                        'pyname': u'hot_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cold air inlet node name',
                                       {'name': u'Cold Air Inlet Node Name',
                                        'pyname': u'cold_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum air flow rate',
                                       {'name': u'Maximum Air Flow Rate',
                                        'pyname': u'maximum_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 6,
               'name': u'AirTerminal:DualDuct:ConstantVolume',
               'pyname': u'AirTerminalDualDuctConstantVolume',
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
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  The outlet node of the terminal unit.
        |  This is also the zone inlet node.

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
    def hot_air_inlet_node_name(self):
        """field `Hot Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Hot Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_air_inlet_node_name` or None if not set

        """
        return self["Hot Air Inlet Node Name"]

    @hot_air_inlet_node_name.setter
    def hot_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Air Inlet Node Name`"""
        self["Hot Air Inlet Node Name"] = value

    @property
    def cold_air_inlet_node_name(self):
        """field `Cold Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cold Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_air_inlet_node_name` or None if not set

        """
        return self["Cold Air Inlet Node Name"]

    @cold_air_inlet_node_name.setter
    def cold_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Cold Air Inlet Node Name`"""
        self["Cold Air Inlet Node Name"] = value

    @property
    def maximum_air_flow_rate(self):
        """field `Maximum Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_air_flow_rate` or None if not set

        """
        return self["Maximum Air Flow Rate"]

    @maximum_air_flow_rate.setter
    def maximum_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Air Flow Rate`"""
        self["Maximum Air Flow Rate"] = value




class AirTerminalDualDuctVav(DataObject):

    """ Corresponds to IDD object `AirTerminal:DualDuct:VAV`
        Central air system terminal unit, dual duct, variable volume.
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
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'hot air inlet node name',
                                       {'name': u'Hot Air Inlet Node Name',
                                        'pyname': u'hot_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'cold air inlet node name',
                                       {'name': u'Cold Air Inlet Node Name',
                                        'pyname': u'cold_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum damper air flow rate',
                                       {'name': u'Maximum Damper Air Flow Rate',
                                        'pyname': u'maximum_damper_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'zone minimum air flow fraction',
                                       {'name': u'Zone Minimum Air Flow Fraction',
                                        'pyname': u'zone_minimum_air_flow_fraction',
                                        'default': 0.2,
                                        'maximum': 1.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real'}),
                                      (u'design specification outdoor air object name',
                                       {'name': u'Design Specification Outdoor Air Object Name',
                                        'pyname': u'design_specification_outdoor_air_object_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 7,
               'name': u'AirTerminal:DualDuct:VAV',
               'pyname': u'AirTerminalDualDuctVav',
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
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  The outlet node of the terminal unit.
        |  This is also the zone inlet node.

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
    def hot_air_inlet_node_name(self):
        """field `Hot Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Hot Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `hot_air_inlet_node_name` or None if not set

        """
        return self["Hot Air Inlet Node Name"]

    @hot_air_inlet_node_name.setter
    def hot_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Hot Air Inlet Node Name`"""
        self["Hot Air Inlet Node Name"] = value

    @property
    def cold_air_inlet_node_name(self):
        """field `Cold Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Cold Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cold_air_inlet_node_name` or None if not set

        """
        return self["Cold Air Inlet Node Name"]

    @cold_air_inlet_node_name.setter
    def cold_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Cold Air Inlet Node Name`"""
        self["Cold Air Inlet Node Name"] = value

    @property
    def maximum_damper_air_flow_rate(self):
        """field `Maximum Damper Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Damper Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_damper_air_flow_rate` or None if not set

        """
        return self["Maximum Damper Air Flow Rate"]

    @maximum_damper_air_flow_rate.setter
    def maximum_damper_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Damper Air Flow Rate`"""
        self["Maximum Damper Air Flow Rate"] = value

    @property
    def zone_minimum_air_flow_fraction(self):
        """field `Zone Minimum Air Flow Fraction`

        |  fraction of maximum air flow
        |  Default value: 0.2
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Zone Minimum Air Flow Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `zone_minimum_air_flow_fraction` or None if not set

        """
        return self["Zone Minimum Air Flow Fraction"]

    @zone_minimum_air_flow_fraction.setter
    def zone_minimum_air_flow_fraction(self, value=0.2):
        """Corresponds to IDD field `Zone Minimum Air Flow Fraction`"""
        self["Zone Minimum Air Flow Fraction"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """field `Design Specification Outdoor Air Object Name`

        |  When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        |  unit will increase flow as needed to meet this outdoor air requirement.
        |  If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        |  be computed based on the current number of occupants in the zone.
        |  At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.
        |  If this field is blank, then the terminal unit will not be controlled for outdoor air flow.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set

        """
        return self["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification Outdoor Air Object
        Name`"""
        self["Design Specification Outdoor Air Object Name"] = value




class AirTerminalDualDuctVavOutdoorAir(DataObject):

    """ Corresponds to IDD object `AirTerminal:DualDuct:VAV:OutdoorAir`
        Central air system terminal unit, dual duct, variable volume with special controls.
        One VAV duct is controlled to supply ventilation air and the other VAV duct is
        controlled to meet the zone cooling load.
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
                                      (u'air outlet node name',
                                       {'name': u'Air Outlet Node Name',
                                        'pyname': u'air_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outdoor air inlet node name',
                                       {'name': u'Outdoor Air Inlet Node Name',
                                        'pyname': u'outdoor_air_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'recirculated air inlet node name',
                                       {'name': u'Recirculated Air Inlet Node Name',
                                        'pyname': u'recirculated_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum terminal air flow rate',
                                       {'name': u'Maximum Terminal Air Flow Rate',
                                        'pyname': u'maximum_terminal_air_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'design specification outdoor air object name',
                                       {'name': u'Design Specification Outdoor Air Object Name',
                                        'pyname': u'design_specification_outdoor_air_object_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'per person ventilation rate mode',
                                       {'name': u'Per Person Ventilation Rate Mode',
                                        'pyname': u'per_person_ventilation_rate_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'CurrentOccupancy',
                                                            u'DesignOccupancy'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 7,
               'name': u'AirTerminal:DualDuct:VAV:OutdoorAir',
               'pyname': u'AirTerminalDualDuctVavOutdoorAir',
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
    def air_outlet_node_name(self):
        """field `Air Outlet Node Name`

        |  The outlet node of the terminal unit.
        |  This is also the zone inlet node.

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
    def outdoor_air_inlet_node_name(self):
        """field `Outdoor Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Outdoor Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_inlet_node_name` or None if not set

        """
        return self["Outdoor Air Inlet Node Name"]

    @outdoor_air_inlet_node_name.setter
    def outdoor_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Inlet Node Name`"""
        self["Outdoor Air Inlet Node Name"] = value

    @property
    def recirculated_air_inlet_node_name(self):
        """field `Recirculated Air Inlet Node Name`

        Args:
            value (str): value for IDD Field `Recirculated Air Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `recirculated_air_inlet_node_name` or None if not set

        """
        return self["Recirculated Air Inlet Node Name"]

    @recirculated_air_inlet_node_name.setter
    def recirculated_air_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Recirculated Air Inlet Node Name`"""
        self["Recirculated Air Inlet Node Name"] = value

    @property
    def maximum_terminal_air_flow_rate(self):
        """field `Maximum Terminal Air Flow Rate`

        |  If autosized this is the sum of flow needed for cooling and maximum required outdoor air
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Terminal Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_terminal_air_flow_rate` or None if not set

        """
        return self["Maximum Terminal Air Flow Rate"]

    @maximum_terminal_air_flow_rate.setter
    def maximum_terminal_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Terminal Air Flow Rate`"""
        self["Maximum Terminal Air Flow Rate"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """field `Design Specification Outdoor Air Object Name`

        |  When the name of a DesignSpecification:OutdoorAir object is entered, the terminal
        |  unit will increase flow as needed to meet this outdoor air requirement.
        |  If Outdoor Air Flow per Person is non-zero, then the outdoor air requirement will
        |  be computed based mode selected in the next field.
        |  At no time will the supply air flow rate exceed the value for Maximum Air Flow Rate.

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set

        """
        return self["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """Corresponds to IDD field `Design Specification Outdoor Air Object
        Name`"""
        self["Design Specification Outdoor Air Object Name"] = value

    @property
    def per_person_ventilation_rate_mode(self):
        """field `Per Person Ventilation Rate Mode`

        |  CurrentOccupancy models demand controlled ventilation using the current number of people
        |  DesignOccupancy uses the total Number of People in the zone and is constant

        Args:
            value (str): value for IDD Field `Per Person Ventilation Rate Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `per_person_ventilation_rate_mode` or None if not set

        """
        return self["Per Person Ventilation Rate Mode"]

    @per_person_ventilation_rate_mode.setter
    def per_person_ventilation_rate_mode(self, value=None):
        """Corresponds to IDD field `Per Person Ventilation Rate Mode`"""
        self["Per Person Ventilation Rate Mode"] = value




class ZoneHvacAirDistributionUnit(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:AirDistributionUnit`
        Central air system air distribution unit, serves as a wrapper for a specific type of
        air terminal unit. This object is referenced in a ZoneHVAC:EquipmentList.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'air distribution unit outlet node name',
                                       {'name': u'Air Distribution Unit Outlet Node Name',
                                        'pyname': u'air_distribution_unit_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air terminal object type',
                                       {'name': u'Air Terminal Object Type',
                                        'pyname': u'air_terminal_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'AirTerminal:DualDuct:ConstantVolume',
                                                            u'AirTerminal:DualDuct:VAV',
                                                            u'AirTerminal:SingleDuct:ConstantVolume:Reheat',
                                                            u'AirTerminal:SingleDuct:VAV:Reheat',
                                                            u'AirTerminal:SingleDuct:VAV:NoReheat',
                                                            u'AirTerminal:SingleDuct:SeriesPIU:Reheat',
                                                            u'AirTerminal:SingleDuct:ParallelPIU:Reheat',
                                                            u'AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction',
                                                            u'AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan',
                                                            u'AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat',
                                                            u'AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat',
                                                            u'AirTerminal:SingleDuct:ConstantVolume:CooledBeam',
                                                            u'AirTerminal:DualDuct:VAV:OutdoorAir',
                                                            u'AirTerminal:SingleDuct:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'air terminal name',
                                       {'name': u'Air Terminal Name',
                                        'pyname': u'air_terminal_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'nominal upstream leakage fraction',
                                       {'name': u'Nominal Upstream Leakage Fraction',
                                        'pyname': u'nominal_upstream_leakage_fraction',
                                        'default': 0.0,
                                        'maximum': 0.3,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'constant downstream leakage fraction',
                                       {'name': u'Constant Downstream Leakage Fraction',
                                        'pyname': u'constant_downstream_leakage_fraction',
                                        'default': 0.0,
                                        'maximum': 0.3,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'})]),
               'format': None,
               'group': u'Zone HVAC Air Loop Terminal Units',
               'min-fields': 4,
               'name': u'ZoneHVAC:AirDistributionUnit',
               'pyname': u'ZoneHvacAirDistributionUnit',
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
    def air_distribution_unit_outlet_node_name(self):
        """field `Air Distribution Unit Outlet Node Name`

        Args:
            value (str): value for IDD Field `Air Distribution Unit Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_distribution_unit_outlet_node_name` or None if not set

        """
        return self["Air Distribution Unit Outlet Node Name"]

    @air_distribution_unit_outlet_node_name.setter
    def air_distribution_unit_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Distribution Unit Outlet Node Name`"""
        self["Air Distribution Unit Outlet Node Name"] = value

    @property
    def air_terminal_object_type(self):
        """field `Air Terminal Object Type`

        Args:
            value (str): value for IDD Field `Air Terminal Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_terminal_object_type` or None if not set

        """
        return self["Air Terminal Object Type"]

    @air_terminal_object_type.setter
    def air_terminal_object_type(self, value=None):
        """Corresponds to IDD field `Air Terminal Object Type`"""
        self["Air Terminal Object Type"] = value

    @property
    def air_terminal_name(self):
        """field `Air Terminal Name`

        Args:
            value (str): value for IDD Field `Air Terminal Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_terminal_name` or None if not set

        """
        return self["Air Terminal Name"]

    @air_terminal_name.setter
    def air_terminal_name(self, value=None):
        """Corresponds to IDD field `Air Terminal Name`"""
        self["Air Terminal Name"] = value

    @property
    def nominal_upstream_leakage_fraction(self):
        """field `Nominal Upstream Leakage Fraction`

        |  fraction at system design Flow; leakage Flow constant, leakage fraction
        |  varies with variable system Flow Rate.
        |  value <= 0.3

        Args:
            value (float): value for IDD Field `Nominal Upstream Leakage Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `nominal_upstream_leakage_fraction` or None if not set

        """
        return self["Nominal Upstream Leakage Fraction"]

    @nominal_upstream_leakage_fraction.setter
    def nominal_upstream_leakage_fraction(self, value=None):
        """Corresponds to IDD field `Nominal Upstream Leakage Fraction`"""
        self["Nominal Upstream Leakage Fraction"] = value

    @property
    def constant_downstream_leakage_fraction(self):
        """field `Constant Downstream Leakage Fraction`

        |  value <= 0.3

        Args:
            value (float): value for IDD Field `Constant Downstream Leakage Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `constant_downstream_leakage_fraction` or None if not set

        """
        return self["Constant Downstream Leakage Fraction"]

    @constant_downstream_leakage_fraction.setter
    def constant_downstream_leakage_fraction(self, value=None):
        """Corresponds to IDD field `Constant Downstream Leakage Fraction`"""
        self["Constant Downstream Leakage Fraction"] = value


