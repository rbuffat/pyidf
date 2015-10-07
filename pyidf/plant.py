""" Data objects in group "Plant"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class TemperingValve(DataObject):

    """ Corresponds to IDD object `TemperingValve`
        Temperature-controlled diversion valve used to divert flow around one or more plant
        components such as a hot water heater. It can only be used on one of two branches
        between a Splitter and a Mixer.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
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
                                      (u'stream 2 source node name',
                                       {'name': u'Stream 2 Source Node Name',
                                        'pyname': u'stream_2_source_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'temperature setpoint node name',
                                       {'name': u'Temperature Setpoint Node Name',
                                        'pyname': u'temperature_setpoint_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'pump outlet node name',
                                       {'name': u'Pump Outlet Node Name',
                                        'pyname': u'pump_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 0,
               'name': u'TemperingValve',
               'pyname': u'TemperingValve',
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
    def inlet_node_name(self):
        """field `Inlet Node Name`

        |  Name of a Node

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

        |  Name of a Node

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
    def stream_2_source_node_name(self):
        """field `Stream 2 Source Node Name`

        |  Name of a Node

        Args:
            value (str): value for IDD Field `Stream 2 Source Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `stream_2_source_node_name` or None if not set

        """
        return self["Stream 2 Source Node Name"]

    @stream_2_source_node_name.setter
    def stream_2_source_node_name(self, value=None):
        """Corresponds to IDD field `Stream 2 Source Node Name`"""
        self["Stream 2 Source Node Name"] = value

    @property
    def temperature_setpoint_node_name(self):
        """field `Temperature Setpoint Node Name`

        |  Name of a Node

        Args:
            value (str): value for IDD Field `Temperature Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `temperature_setpoint_node_name` or None if not set

        """
        return self["Temperature Setpoint Node Name"]

    @temperature_setpoint_node_name.setter
    def temperature_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Temperature Setpoint Node Name`"""
        self["Temperature Setpoint Node Name"] = value

    @property
    def pump_outlet_node_name(self):
        """field `Pump Outlet Node Name`

        Args:
            value (str): value for IDD Field `Pump Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pump_outlet_node_name` or None if not set

        """
        return self["Pump Outlet Node Name"]

    @pump_outlet_node_name.setter
    def pump_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Pump Outlet Node Name`"""
        self["Pump Outlet Node Name"] = value




class PlantLoop(DataObject):

    """Corresponds to IDD object `PlantLoop` Defines a central plant loop."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fluid type',
                                       {'name': u'Fluid Type',
                                        'pyname': u'fluid_type',
                                        'default': u'Water',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Water',
                                                            u'Steam',
                                                            u'UserDefinedFluidType'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'user defined fluid type',
                                       {'name': u'User Defined Fluid Type',
                                        'pyname': u'user_defined_fluid_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant equipment operation scheme name',
                                       {'name': u'Plant Equipment Operation Scheme Name',
                                        'pyname': u'plant_equipment_operation_scheme_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loop temperature setpoint node name',
                                       {'name': u'Loop Temperature Setpoint Node Name',
                                        'pyname': u'loop_temperature_setpoint_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum loop temperature',
                                       {'name': u'Maximum Loop Temperature',
                                        'pyname': u'maximum_loop_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'minimum loop temperature',
                                       {'name': u'Minimum Loop Temperature',
                                        'pyname': u'minimum_loop_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'maximum loop flow rate',
                                       {'name': u'Maximum Loop Flow Rate',
                                        'pyname': u'maximum_loop_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum loop flow rate',
                                       {'name': u'Minimum Loop Flow Rate',
                                        'pyname': u'minimum_loop_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'plant loop volume',
                                       {'name': u'Plant Loop Volume',
                                        'pyname': u'plant_loop_volume',
                                        'default': 'Autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'plant side inlet node name',
                                       {'name': u'Plant Side Inlet Node Name',
                                        'pyname': u'plant_side_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant side outlet node name',
                                       {'name': u'Plant Side Outlet Node Name',
                                        'pyname': u'plant_side_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant side branch list name',
                                       {'name': u'Plant Side Branch List Name',
                                        'pyname': u'plant_side_branch_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant side connector list name',
                                       {'name': u'Plant Side Connector List Name',
                                        'pyname': u'plant_side_connector_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'demand side inlet node name',
                                       {'name': u'Demand Side Inlet Node Name',
                                        'pyname': u'demand_side_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'demand side outlet node name',
                                       {'name': u'Demand Side Outlet Node Name',
                                        'pyname': u'demand_side_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'demand side branch list name',
                                       {'name': u'Demand Side Branch List Name',
                                        'pyname': u'demand_side_branch_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'demand side connector list name',
                                       {'name': u'Demand Side Connector List Name',
                                        'pyname': u'demand_side_connector_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load distribution scheme',
                                       {'name': u'Load Distribution Scheme',
                                        'pyname': u'load_distribution_scheme',
                                        'default': u'SequentialLoad',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Optimal',
                                                            u'SequentialLoad',
                                                            u'UniformLoad',
                                                            u'UniformPLR',
                                                            u'SequentialUniformPLR'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant loop demand calculation scheme',
                                       {'name': u'Plant Loop Demand Calculation Scheme',
                                        'pyname': u'plant_loop_demand_calculation_scheme',
                                        'default': u'SingleSetpoint',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'SingleSetpoint',
                                                            u'DualSetpointDeadband'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'common pipe simulation',
                                       {'name': u'Common Pipe Simulation',
                                        'pyname': u'common_pipe_simulation',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'CommonPipe',
                                                            u'TwoWayCommonPipe',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'pressure simulation type',
                                       {'name': u'Pressure Simulation Type',
                                        'pyname': u'pressure_simulation_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PumpPowerCorrection',
                                                            u'LoopFlowCorrection',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 0,
               'name': u'PlantLoop',
               'pyname': u'PlantLoop',
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
    def fluid_type(self):
        """field `Fluid Type`

        |  Default value: Water

        Args:
            value (str): value for IDD Field `Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fluid_type` or None if not set

        """
        return self["Fluid Type"]

    @fluid_type.setter
    def fluid_type(self, value="Water"):
        """Corresponds to IDD field `Fluid Type`"""
        self["Fluid Type"] = value

    @property
    def user_defined_fluid_type(self):
        """field `User Defined Fluid Type`

        |  This field is only required when Fluid Type is UserDefinedFluidType

        Args:
            value (str): value for IDD Field `User Defined Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `user_defined_fluid_type` or None if not set

        """
        return self["User Defined Fluid Type"]

    @user_defined_fluid_type.setter
    def user_defined_fluid_type(self, value=None):
        """Corresponds to IDD field `User Defined Fluid Type`"""
        self["User Defined Fluid Type"] = value

    @property
    def plant_equipment_operation_scheme_name(self):
        """field `Plant Equipment Operation Scheme Name`

        Args:
            value (str): value for IDD Field `Plant Equipment Operation Scheme Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_equipment_operation_scheme_name` or None if not set

        """
        return self["Plant Equipment Operation Scheme Name"]

    @plant_equipment_operation_scheme_name.setter
    def plant_equipment_operation_scheme_name(self, value=None):
        """Corresponds to IDD field `Plant Equipment Operation Scheme Name`"""
        self["Plant Equipment Operation Scheme Name"] = value

    @property
    def loop_temperature_setpoint_node_name(self):
        """field `Loop Temperature Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Loop Temperature Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loop_temperature_setpoint_node_name` or None if not set

        """
        return self["Loop Temperature Setpoint Node Name"]

    @loop_temperature_setpoint_node_name.setter
    def loop_temperature_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Loop Temperature Setpoint Node Name`"""
        self["Loop Temperature Setpoint Node Name"] = value

    @property
    def maximum_loop_temperature(self):
        """field `Maximum Loop Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Loop Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_loop_temperature` or None if not set

        """
        return self["Maximum Loop Temperature"]

    @maximum_loop_temperature.setter
    def maximum_loop_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Loop Temperature`"""
        self["Maximum Loop Temperature"] = value

    @property
    def minimum_loop_temperature(self):
        """field `Minimum Loop Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Loop Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_loop_temperature` or None if not set

        """
        return self["Minimum Loop Temperature"]

    @minimum_loop_temperature.setter
    def minimum_loop_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Loop Temperature`"""
        self["Minimum Loop Temperature"] = value

    @property
    def maximum_loop_flow_rate(self):
        """field `Maximum Loop Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Loop Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_loop_flow_rate` or None if not set

        """
        return self["Maximum Loop Flow Rate"]

    @maximum_loop_flow_rate.setter
    def maximum_loop_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Loop Flow Rate`"""
        self["Maximum Loop Flow Rate"] = value

    @property
    def minimum_loop_flow_rate(self):
        """field `Minimum Loop Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Loop Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_loop_flow_rate` or None if not set

        """
        return self["Minimum Loop Flow Rate"]

    @minimum_loop_flow_rate.setter
    def minimum_loop_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Loop Flow Rate`"""
        self["Minimum Loop Flow Rate"] = value

    @property
    def plant_loop_volume(self):
        """field `Plant Loop Volume`

        |  Units: m3
        |  IP-Units: gal
        |  Default value: "Autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Plant Loop Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `plant_loop_volume` or None if not set

        """
        return self["Plant Loop Volume"]

    @plant_loop_volume.setter
    def plant_loop_volume(self, value="Autocalculate"):
        """Corresponds to IDD field `Plant Loop Volume`"""
        self["Plant Loop Volume"] = value

    @property
    def plant_side_inlet_node_name(self):
        """field `Plant Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_side_inlet_node_name` or None if not set

        """
        return self["Plant Side Inlet Node Name"]

    @plant_side_inlet_node_name.setter
    def plant_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Side Inlet Node Name`"""
        self["Plant Side Inlet Node Name"] = value

    @property
    def plant_side_outlet_node_name(self):
        """field `Plant Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_side_outlet_node_name` or None if not set

        """
        return self["Plant Side Outlet Node Name"]

    @plant_side_outlet_node_name.setter
    def plant_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Side Outlet Node Name`"""
        self["Plant Side Outlet Node Name"] = value

    @property
    def plant_side_branch_list_name(self):
        """field `Plant Side Branch List Name`

        Args:
            value (str): value for IDD Field `Plant Side Branch List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_side_branch_list_name` or None if not set

        """
        return self["Plant Side Branch List Name"]

    @plant_side_branch_list_name.setter
    def plant_side_branch_list_name(self, value=None):
        """Corresponds to IDD field `Plant Side Branch List Name`"""
        self["Plant Side Branch List Name"] = value

    @property
    def plant_side_connector_list_name(self):
        """field `Plant Side Connector List Name`

        Args:
            value (str): value for IDD Field `Plant Side Connector List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_side_connector_list_name` or None if not set

        """
        return self["Plant Side Connector List Name"]

    @plant_side_connector_list_name.setter
    def plant_side_connector_list_name(self, value=None):
        """Corresponds to IDD field `Plant Side Connector List Name`"""
        self["Plant Side Connector List Name"] = value

    @property
    def demand_side_inlet_node_name(self):
        """field `Demand Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_inlet_node_name` or None if not set

        """
        return self["Demand Side Inlet Node Name"]

    @demand_side_inlet_node_name.setter
    def demand_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Demand Side Inlet Node Name`"""
        self["Demand Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """field `Demand Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_outlet_node_name` or None if not set

        """
        return self["Demand Side Outlet Node Name"]

    @demand_side_outlet_node_name.setter
    def demand_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Demand Side Outlet Node Name`"""
        self["Demand Side Outlet Node Name"] = value

    @property
    def demand_side_branch_list_name(self):
        """field `Demand Side Branch List Name`

        Args:
            value (str): value for IDD Field `Demand Side Branch List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_branch_list_name` or None if not set

        """
        return self["Demand Side Branch List Name"]

    @demand_side_branch_list_name.setter
    def demand_side_branch_list_name(self, value=None):
        """Corresponds to IDD field `Demand Side Branch List Name`"""
        self["Demand Side Branch List Name"] = value

    @property
    def demand_side_connector_list_name(self):
        """field `Demand Side Connector List Name`

        Args:
            value (str): value for IDD Field `Demand Side Connector List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_connector_list_name` or None if not set

        """
        return self["Demand Side Connector List Name"]

    @demand_side_connector_list_name.setter
    def demand_side_connector_list_name(self, value=None):
        """Corresponds to IDD field `Demand Side Connector List Name`"""
        self["Demand Side Connector List Name"] = value

    @property
    def load_distribution_scheme(self):
        """field `Load Distribution Scheme`

        |  Default value: SequentialLoad

        Args:
            value (str): value for IDD Field `Load Distribution Scheme`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `load_distribution_scheme` or None if not set

        """
        return self["Load Distribution Scheme"]

    @load_distribution_scheme.setter
    def load_distribution_scheme(self, value="SequentialLoad"):
        """Corresponds to IDD field `Load Distribution Scheme`"""
        self["Load Distribution Scheme"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        Args:
            value (str): value for IDD Field `Availability Manager List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `availability_manager_list_name` or None if not set

        """
        return self["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """Corresponds to IDD field `Availability Manager List Name`"""
        self["Availability Manager List Name"] = value

    @property
    def plant_loop_demand_calculation_scheme(self):
        """field `Plant Loop Demand Calculation Scheme`

        |  Default value: SingleSetpoint

        Args:
            value (str): value for IDD Field `Plant Loop Demand Calculation Scheme`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_loop_demand_calculation_scheme` or None if not set

        """
        return self["Plant Loop Demand Calculation Scheme"]

    @plant_loop_demand_calculation_scheme.setter
    def plant_loop_demand_calculation_scheme(self, value="SingleSetpoint"):
        """Corresponds to IDD field `Plant Loop Demand Calculation Scheme`"""
        self["Plant Loop Demand Calculation Scheme"] = value

    @property
    def common_pipe_simulation(self):
        """field `Common Pipe Simulation`

        |  Specifies a primary-secondary loop configuration. The plant side is the
        |  primary loop, and the demand side is the secondary loop.
        |  A secondary supply pump is required on the demand side.
        |  None = Primary-only, no secondary simulation
        |  CommonPipe = Primary-secondary with no temperature control at primary-secondary interface
        |  TwoWayCommonPipe = Primary-secondary with control of secondary supply temperature or
        |  primary return temperature (requires a setpoint be placed on the
        |  plant side or demand side inlet node).
        |  Default value: None

        Args:
            value (str): value for IDD Field `Common Pipe Simulation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `common_pipe_simulation` or None if not set

        """
        return self["Common Pipe Simulation"]

    @common_pipe_simulation.setter
    def common_pipe_simulation(self, value="None"):
        """Corresponds to IDD field `Common Pipe Simulation`"""
        self["Common Pipe Simulation"] = value

    @property
    def pressure_simulation_type(self):
        """field `Pressure Simulation Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Pressure Simulation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pressure_simulation_type` or None if not set

        """
        return self["Pressure Simulation Type"]

    @pressure_simulation_type.setter
    def pressure_simulation_type(self, value="None"):
        """Corresponds to IDD field `Pressure Simulation Type`"""
        self["Pressure Simulation Type"] = value




class CondenserLoop(DataObject):

    """Corresponds to IDD object `CondenserLoop` Defines a central plant
    condenser loop.

    CondenserLoop and PlantLoop are nearly identical except some
    components and operation schemes are applicable to only one loop
    type or the other.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'fluid type',
                                       {'name': u'Fluid Type',
                                        'pyname': u'fluid_type',
                                        'default': u'Water',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Water',
                                                            u'UserDefinedFluidType'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'user defined fluid type',
                                       {'name': u'User Defined Fluid Type',
                                        'pyname': u'user_defined_fluid_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condenser equipment operation scheme name',
                                       {'name': u'Condenser Equipment Operation Scheme Name',
                                        'pyname': u'condenser_equipment_operation_scheme_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condenser loop temperature setpoint node name',
                                       {'name': u'Condenser Loop Temperature Setpoint Node Name',
                                        'pyname': u'condenser_loop_temperature_setpoint_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'maximum loop temperature',
                                       {'name': u'Maximum Loop Temperature',
                                        'pyname': u'maximum_loop_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'minimum loop temperature',
                                       {'name': u'Minimum Loop Temperature',
                                        'pyname': u'minimum_loop_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'C'}),
                                      (u'maximum loop flow rate',
                                       {'name': u'Maximum Loop Flow Rate',
                                        'pyname': u'maximum_loop_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'minimum loop flow rate',
                                       {'name': u'Minimum Loop Flow Rate',
                                        'pyname': u'minimum_loop_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'condenser loop volume',
                                       {'name': u'Condenser Loop Volume',
                                        'pyname': u'condenser_loop_volume',
                                        'default': 'Autocalculate',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': True,
                                        'type': u'real',
                                        'unit': u'm3'}),
                                      (u'condenser side inlet node name',
                                       {'name': u'Condenser Side Inlet Node Name',
                                        'pyname': u'condenser_side_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'condenser side outlet node name',
                                       {'name': u'Condenser Side Outlet Node Name',
                                        'pyname': u'condenser_side_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'condenser side branch list name',
                                       {'name': u'Condenser Side Branch List Name',
                                        'pyname': u'condenser_side_branch_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condenser side connector list name',
                                       {'name': u'Condenser Side Connector List Name',
                                        'pyname': u'condenser_side_connector_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'demand side inlet node name',
                                       {'name': u'Demand Side Inlet Node Name',
                                        'pyname': u'demand_side_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'demand side outlet node name',
                                       {'name': u'Demand Side Outlet Node Name',
                                        'pyname': u'demand_side_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'condenser demand side branch list name',
                                       {'name': u'Condenser Demand Side Branch List Name',
                                        'pyname': u'condenser_demand_side_branch_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'condenser demand side connector list name',
                                       {'name': u'Condenser Demand Side Connector List Name',
                                        'pyname': u'condenser_demand_side_connector_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load distribution scheme',
                                       {'name': u'Load Distribution Scheme',
                                        'pyname': u'load_distribution_scheme',
                                        'default': u'SequentialLoad',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Optimal',
                                                            u'SequentialLoad',
                                                            u'UniformLoad',
                                                            u'UniformPLR',
                                                            u'SequentialUniformPLR'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'pressure simulation type',
                                       {'name': u'Pressure Simulation Type',
                                        'pyname': u'pressure_simulation_type',
                                        'default': u'None',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PumpPowerCorrection',
                                                            u'LoopFlowCorrection',
                                                            u'None'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 0,
               'name': u'CondenserLoop',
               'pyname': u'CondenserLoop',
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
    def fluid_type(self):
        """field `Fluid Type`

        |  Default value: Water

        Args:
            value (str): value for IDD Field `Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fluid_type` or None if not set

        """
        return self["Fluid Type"]

    @fluid_type.setter
    def fluid_type(self, value="Water"):
        """Corresponds to IDD field `Fluid Type`"""
        self["Fluid Type"] = value

    @property
    def user_defined_fluid_type(self):
        """field `User Defined Fluid Type`

        |  This field is only required when Fluid Type is UserDefinedFluidType

        Args:
            value (str): value for IDD Field `User Defined Fluid Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `user_defined_fluid_type` or None if not set

        """
        return self["User Defined Fluid Type"]

    @user_defined_fluid_type.setter
    def user_defined_fluid_type(self, value=None):
        """Corresponds to IDD field `User Defined Fluid Type`"""
        self["User Defined Fluid Type"] = value

    @property
    def condenser_equipment_operation_scheme_name(self):
        """field `Condenser Equipment Operation Scheme Name`

        Args:
            value (str): value for IDD Field `Condenser Equipment Operation Scheme Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_equipment_operation_scheme_name` or None if not set

        """
        return self["Condenser Equipment Operation Scheme Name"]

    @condenser_equipment_operation_scheme_name.setter
    def condenser_equipment_operation_scheme_name(self, value=None):
        """Corresponds to IDD field `Condenser Equipment Operation Scheme
        Name`"""
        self["Condenser Equipment Operation Scheme Name"] = value

    @property
    def condenser_loop_temperature_setpoint_node_name(self):
        """field `Condenser Loop Temperature Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Condenser Loop Temperature Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_loop_temperature_setpoint_node_name` or None if not set

        """
        return self["Condenser Loop Temperature Setpoint Node Name"]

    @condenser_loop_temperature_setpoint_node_name.setter
    def condenser_loop_temperature_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Loop Temperature Setpoint Node
        Name`"""
        self["Condenser Loop Temperature Setpoint Node Name"] = value

    @property
    def maximum_loop_temperature(self):
        """field `Maximum Loop Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Loop Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_loop_temperature` or None if not set

        """
        return self["Maximum Loop Temperature"]

    @maximum_loop_temperature.setter
    def maximum_loop_temperature(self, value=None):
        """Corresponds to IDD field `Maximum Loop Temperature`"""
        self["Maximum Loop Temperature"] = value

    @property
    def minimum_loop_temperature(self):
        """field `Minimum Loop Temperature`

        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Loop Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_loop_temperature` or None if not set

        """
        return self["Minimum Loop Temperature"]

    @minimum_loop_temperature.setter
    def minimum_loop_temperature(self, value=None):
        """Corresponds to IDD field `Minimum Loop Temperature`"""
        self["Minimum Loop Temperature"] = value

    @property
    def maximum_loop_flow_rate(self):
        """field `Maximum Loop Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float or "Autosize"): value for IDD Field `Maximum Loop Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `maximum_loop_flow_rate` or None if not set

        """
        return self["Maximum Loop Flow Rate"]

    @maximum_loop_flow_rate.setter
    def maximum_loop_flow_rate(self, value=None):
        """Corresponds to IDD field `Maximum Loop Flow Rate`"""
        self["Maximum Loop Flow Rate"] = value

    @property
    def minimum_loop_flow_rate(self):
        """field `Minimum Loop Flow Rate`

        |  Units: m3/s
        |  IP-Units: gal/min

        Args:
            value (float): value for IDD Field `Minimum Loop Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_loop_flow_rate` or None if not set

        """
        return self["Minimum Loop Flow Rate"]

    @minimum_loop_flow_rate.setter
    def minimum_loop_flow_rate(self, value=None):
        """Corresponds to IDD field `Minimum Loop Flow Rate`"""
        self["Minimum Loop Flow Rate"] = value

    @property
    def condenser_loop_volume(self):
        """field `Condenser Loop Volume`

        |  Units: m3
        |  IP-Units: gal
        |  Default value: "Autocalculate"

        Args:
            value (float or "Autocalculate"): value for IDD Field `Condenser Loop Volume`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autocalculate": the value of `condenser_loop_volume` or None if not set

        """
        return self["Condenser Loop Volume"]

    @condenser_loop_volume.setter
    def condenser_loop_volume(self, value="Autocalculate"):
        """Corresponds to IDD field `Condenser Loop Volume`"""
        self["Condenser Loop Volume"] = value

    @property
    def condenser_side_inlet_node_name(self):
        """field `Condenser Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Condenser Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_side_inlet_node_name` or None if not set

        """
        return self["Condenser Side Inlet Node Name"]

    @condenser_side_inlet_node_name.setter
    def condenser_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Side Inlet Node Name`"""
        self["Condenser Side Inlet Node Name"] = value

    @property
    def condenser_side_outlet_node_name(self):
        """field `Condenser Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Condenser Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_side_outlet_node_name` or None if not set

        """
        return self["Condenser Side Outlet Node Name"]

    @condenser_side_outlet_node_name.setter
    def condenser_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Side Outlet Node Name`"""
        self["Condenser Side Outlet Node Name"] = value

    @property
    def condenser_side_branch_list_name(self):
        """field `Condenser Side Branch List Name`

        Args:
            value (str): value for IDD Field `Condenser Side Branch List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_side_branch_list_name` or None if not set

        """
        return self["Condenser Side Branch List Name"]

    @condenser_side_branch_list_name.setter
    def condenser_side_branch_list_name(self, value=None):
        """Corresponds to IDD field `Condenser Side Branch List Name`"""
        self["Condenser Side Branch List Name"] = value

    @property
    def condenser_side_connector_list_name(self):
        """field `Condenser Side Connector List Name`

        Args:
            value (str): value for IDD Field `Condenser Side Connector List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_side_connector_list_name` or None if not set

        """
        return self["Condenser Side Connector List Name"]

    @condenser_side_connector_list_name.setter
    def condenser_side_connector_list_name(self, value=None):
        """Corresponds to IDD field `Condenser Side Connector List Name`"""
        self["Condenser Side Connector List Name"] = value

    @property
    def demand_side_inlet_node_name(self):
        """field `Demand Side Inlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_inlet_node_name` or None if not set

        """
        return self["Demand Side Inlet Node Name"]

    @demand_side_inlet_node_name.setter
    def demand_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Demand Side Inlet Node Name`"""
        self["Demand Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """field `Demand Side Outlet Node Name`

        Args:
            value (str): value for IDD Field `Demand Side Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_outlet_node_name` or None if not set

        """
        return self["Demand Side Outlet Node Name"]

    @demand_side_outlet_node_name.setter
    def demand_side_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Demand Side Outlet Node Name`"""
        self["Demand Side Outlet Node Name"] = value

    @property
    def condenser_demand_side_branch_list_name(self):
        """field `Condenser Demand Side Branch List Name`

        Args:
            value (str): value for IDD Field `Condenser Demand Side Branch List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_demand_side_branch_list_name` or None if not set

        """
        return self["Condenser Demand Side Branch List Name"]

    @condenser_demand_side_branch_list_name.setter
    def condenser_demand_side_branch_list_name(self, value=None):
        """Corresponds to IDD field `Condenser Demand Side Branch List Name`"""
        self["Condenser Demand Side Branch List Name"] = value

    @property
    def condenser_demand_side_connector_list_name(self):
        """field `Condenser Demand Side Connector List Name`

        Args:
            value (str): value for IDD Field `Condenser Demand Side Connector List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_demand_side_connector_list_name` or None if not set

        """
        return self["Condenser Demand Side Connector List Name"]

    @condenser_demand_side_connector_list_name.setter
    def condenser_demand_side_connector_list_name(self, value=None):
        """Corresponds to IDD field `Condenser Demand Side Connector List
        Name`"""
        self["Condenser Demand Side Connector List Name"] = value

    @property
    def load_distribution_scheme(self):
        """field `Load Distribution Scheme`

        |  Default value: SequentialLoad

        Args:
            value (str): value for IDD Field `Load Distribution Scheme`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `load_distribution_scheme` or None if not set

        """
        return self["Load Distribution Scheme"]

    @load_distribution_scheme.setter
    def load_distribution_scheme(self, value="SequentialLoad"):
        """Corresponds to IDD field `Load Distribution Scheme`"""
        self["Load Distribution Scheme"] = value

    @property
    def pressure_simulation_type(self):
        """field `Pressure Simulation Type`

        |  Default value: None

        Args:
            value (str): value for IDD Field `Pressure Simulation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `pressure_simulation_type` or None if not set

        """
        return self["Pressure Simulation Type"]

    @pressure_simulation_type.setter
    def pressure_simulation_type(self, value="None"):
        """Corresponds to IDD field `Pressure Simulation Type`"""
        self["Pressure Simulation Type"] = value




class PlantEquipmentList(DataObject):

    """Corresponds to IDD object `PlantEquipmentList` List plant equipment in
    order of operating priority, 1st in list will be used 1st, etc Use only
    plant equipment in this list.

    If no equipment object types and equipment names are specified, then the corresponding
    PlantEquipmentOperation:* object will assume all available plant equipment for the loop
    should be OFF (not operate) within the specified lower/upper limit.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 1 object type',
                                       {'name': u'Equipment 1 Object Type',
                                        'pyname': u'equipment_1_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 1 name',
                                       {'name': u'Equipment 1 Name',
                                        'pyname': u'equipment_1_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 2 object type',
                                       {'name': u'Equipment 2 Object Type',
                                        'pyname': u'equipment_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 2 name',
                                       {'name': u'Equipment 2 Name',
                                        'pyname': u'equipment_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 3 object type',
                                       {'name': u'Equipment 3 Object Type',
                                        'pyname': u'equipment_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 3 name',
                                       {'name': u'Equipment 3 Name',
                                        'pyname': u'equipment_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 4 object type',
                                       {'name': u'Equipment 4 Object Type',
                                        'pyname': u'equipment_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 4 name',
                                       {'name': u'Equipment 4 Name',
                                        'pyname': u'equipment_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 5 object type',
                                       {'name': u'Equipment 5 Object Type',
                                        'pyname': u'equipment_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 5 name',
                                       {'name': u'Equipment 5 Name',
                                        'pyname': u'equipment_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 6 object type',
                                       {'name': u'Equipment 6 Object Type',
                                        'pyname': u'equipment_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 6 name',
                                       {'name': u'Equipment 6 Name',
                                        'pyname': u'equipment_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 7 object type',
                                       {'name': u'Equipment 7 Object Type',
                                        'pyname': u'equipment_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 7 name',
                                       {'name': u'Equipment 7 Name',
                                        'pyname': u'equipment_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 8 object type',
                                       {'name': u'Equipment 8 Object Type',
                                        'pyname': u'equipment_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 8 name',
                                       {'name': u'Equipment 8 Name',
                                        'pyname': u'equipment_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 9 object type',
                                       {'name': u'Equipment 9 Object Type',
                                        'pyname': u'equipment_9_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 9 name',
                                       {'name': u'Equipment 9 Name',
                                        'pyname': u'equipment_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 10 object type',
                                       {'name': u'Equipment 10 Object Type',
                                        'pyname': u'equipment_10_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 10 name',
                                       {'name': u'Equipment 10 Name',
                                        'pyname': u'equipment_10_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 1,
               'name': u'PlantEquipmentList',
               'pyname': u'PlantEquipmentList',
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
    def equipment_1_object_type(self):
        """field `Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_1_object_type` or None if not set

        """
        return self["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 1 Object Type`"""
        self["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """field `Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Equipment 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_1_name` or None if not set

        """
        return self["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """Corresponds to IDD field `Equipment 1 Name`"""
        self["Equipment 1 Name"] = value

    @property
    def equipment_2_object_type(self):
        """field `Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_2_object_type` or None if not set

        """
        return self["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 2 Object Type`"""
        self["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """field `Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Equipment 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_2_name` or None if not set

        """
        return self["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """Corresponds to IDD field `Equipment 2 Name`"""
        self["Equipment 2 Name"] = value

    @property
    def equipment_3_object_type(self):
        """field `Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_3_object_type` or None if not set

        """
        return self["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 3 Object Type`"""
        self["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """field `Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Equipment 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_3_name` or None if not set

        """
        return self["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """Corresponds to IDD field `Equipment 3 Name`"""
        self["Equipment 3 Name"] = value

    @property
    def equipment_4_object_type(self):
        """field `Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_4_object_type` or None if not set

        """
        return self["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 4 Object Type`"""
        self["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """field `Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Equipment 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_4_name` or None if not set

        """
        return self["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """Corresponds to IDD field `Equipment 4 Name`"""
        self["Equipment 4 Name"] = value

    @property
    def equipment_5_object_type(self):
        """field `Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_5_object_type` or None if not set

        """
        return self["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 5 Object Type`"""
        self["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """field `Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Equipment 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_5_name` or None if not set

        """
        return self["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """Corresponds to IDD field `Equipment 5 Name`"""
        self["Equipment 5 Name"] = value

    @property
    def equipment_6_object_type(self):
        """field `Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_6_object_type` or None if not set

        """
        return self["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 6 Object Type`"""
        self["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """field `Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Equipment 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_6_name` or None if not set

        """
        return self["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """Corresponds to IDD field `Equipment 6 Name`"""
        self["Equipment 6 Name"] = value

    @property
    def equipment_7_object_type(self):
        """field `Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_7_object_type` or None if not set

        """
        return self["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 7 Object Type`"""
        self["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """field `Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Equipment 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_7_name` or None if not set

        """
        return self["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """Corresponds to IDD field `Equipment 7 Name`"""
        self["Equipment 7 Name"] = value

    @property
    def equipment_8_object_type(self):
        """field `Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_8_object_type` or None if not set

        """
        return self["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 8 Object Type`"""
        self["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """field `Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Equipment 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_8_name` or None if not set

        """
        return self["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """Corresponds to IDD field `Equipment 8 Name`"""
        self["Equipment 8 Name"] = value

    @property
    def equipment_9_object_type(self):
        """field `Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 9 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_9_object_type` or None if not set

        """
        return self["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 9 Object Type`"""
        self["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """field `Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Equipment 9 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_9_name` or None if not set

        """
        return self["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """Corresponds to IDD field `Equipment 9 Name`"""
        self["Equipment 9 Name"] = value

    @property
    def equipment_10_object_type(self):
        """field `Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 10 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_10_object_type` or None if not set

        """
        return self["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 10 Object Type`"""
        self["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """field `Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Equipment 10 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_10_name` or None if not set

        """
        return self["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """Corresponds to IDD field `Equipment 10 Name`"""
        self["Equipment 10 Name"] = value




class CondenserEquipmentList(DataObject):

    """Corresponds to IDD object `CondenserEquipmentList` List condenser
    equipment in order of operating priority, 1st in list will be used 1st, etc
    Use only condenser equipment in this list.

    If no equipment object types and equipment names are specified, then the corresponding
    PlantEquipmentOperation:* object will assume all available condenser equipment for the loop
    should be OFF (not operate) within the specified lower/upper limit.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 1 object type',
                                       {'name': u'Equipment 1 Object Type',
                                        'pyname': u'equipment_1_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 1 name',
                                       {'name': u'Equipment 1 Name',
                                        'pyname': u'equipment_1_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 2 object type',
                                       {'name': u'Equipment 2 Object Type',
                                        'pyname': u'equipment_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 2 name',
                                       {'name': u'Equipment 2 Name',
                                        'pyname': u'equipment_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 3 object type',
                                       {'name': u'Equipment 3 Object Type',
                                        'pyname': u'equipment_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 3 name',
                                       {'name': u'Equipment 3 Name',
                                        'pyname': u'equipment_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 4 object type',
                                       {'name': u'Equipment 4 Object Type',
                                        'pyname': u'equipment_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 4 name',
                                       {'name': u'Equipment 4 Name',
                                        'pyname': u'equipment_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 5 object type',
                                       {'name': u'Equipment 5 Object Type',
                                        'pyname': u'equipment_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 5 name',
                                       {'name': u'Equipment 5 Name',
                                        'pyname': u'equipment_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 6 object type',
                                       {'name': u'Equipment 6 Object Type',
                                        'pyname': u'equipment_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 6 name',
                                       {'name': u'Equipment 6 Name',
                                        'pyname': u'equipment_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 7 object type',
                                       {'name': u'Equipment 7 Object Type',
                                        'pyname': u'equipment_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 7 name',
                                       {'name': u'Equipment 7 Name',
                                        'pyname': u'equipment_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 8 object type',
                                       {'name': u'Equipment 8 Object Type',
                                        'pyname': u'equipment_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 8 name',
                                       {'name': u'Equipment 8 Name',
                                        'pyname': u'equipment_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 9 object type',
                                       {'name': u'Equipment 9 Object Type',
                                        'pyname': u'equipment_9_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 9 name',
                                       {'name': u'Equipment 9 Name',
                                        'pyname': u'equipment_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 10 object type',
                                       {'name': u'Equipment 10 Object Type',
                                        'pyname': u'equipment_10_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 10 name',
                                       {'name': u'Equipment 10 Name',
                                        'pyname': u'equipment_10_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 1,
               'name': u'CondenserEquipmentList',
               'pyname': u'CondenserEquipmentList',
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
    def equipment_1_object_type(self):
        """field `Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_1_object_type` or None if not set

        """
        return self["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 1 Object Type`"""
        self["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """field `Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Equipment 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_1_name` or None if not set

        """
        return self["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """Corresponds to IDD field `Equipment 1 Name`"""
        self["Equipment 1 Name"] = value

    @property
    def equipment_2_object_type(self):
        """field `Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_2_object_type` or None if not set

        """
        return self["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 2 Object Type`"""
        self["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """field `Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Equipment 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_2_name` or None if not set

        """
        return self["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """Corresponds to IDD field `Equipment 2 Name`"""
        self["Equipment 2 Name"] = value

    @property
    def equipment_3_object_type(self):
        """field `Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_3_object_type` or None if not set

        """
        return self["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 3 Object Type`"""
        self["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """field `Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Equipment 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_3_name` or None if not set

        """
        return self["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """Corresponds to IDD field `Equipment 3 Name`"""
        self["Equipment 3 Name"] = value

    @property
    def equipment_4_object_type(self):
        """field `Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_4_object_type` or None if not set

        """
        return self["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 4 Object Type`"""
        self["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """field `Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Equipment 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_4_name` or None if not set

        """
        return self["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """Corresponds to IDD field `Equipment 4 Name`"""
        self["Equipment 4 Name"] = value

    @property
    def equipment_5_object_type(self):
        """field `Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_5_object_type` or None if not set

        """
        return self["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 5 Object Type`"""
        self["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """field `Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Equipment 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_5_name` or None if not set

        """
        return self["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """Corresponds to IDD field `Equipment 5 Name`"""
        self["Equipment 5 Name"] = value

    @property
    def equipment_6_object_type(self):
        """field `Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_6_object_type` or None if not set

        """
        return self["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 6 Object Type`"""
        self["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """field `Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Equipment 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_6_name` or None if not set

        """
        return self["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """Corresponds to IDD field `Equipment 6 Name`"""
        self["Equipment 6 Name"] = value

    @property
    def equipment_7_object_type(self):
        """field `Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_7_object_type` or None if not set

        """
        return self["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 7 Object Type`"""
        self["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """field `Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Equipment 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_7_name` or None if not set

        """
        return self["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """Corresponds to IDD field `Equipment 7 Name`"""
        self["Equipment 7 Name"] = value

    @property
    def equipment_8_object_type(self):
        """field `Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_8_object_type` or None if not set

        """
        return self["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 8 Object Type`"""
        self["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """field `Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Equipment 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_8_name` or None if not set

        """
        return self["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """Corresponds to IDD field `Equipment 8 Name`"""
        self["Equipment 8 Name"] = value

    @property
    def equipment_9_object_type(self):
        """field `Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 9 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_9_object_type` or None if not set

        """
        return self["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 9 Object Type`"""
        self["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """field `Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Equipment 9 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_9_name` or None if not set

        """
        return self["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """Corresponds to IDD field `Equipment 9 Name`"""
        self["Equipment 9 Name"] = value

    @property
    def equipment_10_object_type(self):
        """field `Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 10 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_10_object_type` or None if not set

        """
        return self["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 10 Object Type`"""
        self["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """field `Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Equipment 10 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_10_name` or None if not set

        """
        return self["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """Corresponds to IDD field `Equipment 10 Name`"""
        self["Equipment 10 Name"] = value




class PlantEquipmentOperationUncontrolled(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:Uncontrolled`
        Plant equipment operation scheme for uncontrolled operation. Specifies a group of
        equipment that runs if the loop is active, unless turned off by the loop flow resolver
        to maintain continuity in the fluid loop.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment list name',
                                       {'name': u'Equipment List Name',
                                        'pyname': u'equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 2,
               'name': u'PlantEquipmentOperation:Uncontrolled',
               'pyname': u'PlantEquipmentOperationUncontrolled',
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
    def equipment_list_name(self):
        """field `Equipment List Name`

        Args:
            value (str): value for IDD Field `Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_list_name` or None if not set

        """
        return self["Equipment List Name"]

    @equipment_list_name.setter
    def equipment_list_name(self, value=None):
        """Corresponds to IDD field `Equipment List Name`"""
        self["Equipment List Name"] = value




class PlantEquipmentOperationCoolingLoad(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:CoolingLoad`
        Plant equipment operation scheme for cooling load range operation. Specifies one or
        more groups of equipment which are available to operate for successive cooling load
        ranges.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'load range 1 lower limit',
                                       {'name': u'Load Range 1 Lower Limit',
                                        'pyname': u'load_range_1_lower_limit',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 1 upper limit',
                                       {'name': u'Load Range 1 Upper Limit',
                                        'pyname': u'load_range_1_upper_limit',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 2 lower limit',
                                       {'name': u'Load Range 2 Lower Limit',
                                        'pyname': u'load_range_2_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 2 upper limit',
                                       {'name': u'Load Range 2 Upper Limit',
                                        'pyname': u'load_range_2_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 3 lower limit',
                                       {'name': u'Load Range 3 Lower Limit',
                                        'pyname': u'load_range_3_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 3 upper limit',
                                       {'name': u'Load Range 3 Upper Limit',
                                        'pyname': u'load_range_3_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 4 lower limit',
                                       {'name': u'Load Range 4 Lower Limit',
                                        'pyname': u'load_range_4_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 4 upper limit',
                                       {'name': u'Load Range 4 Upper Limit',
                                        'pyname': u'load_range_4_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 5 lower limit',
                                       {'name': u'Load Range 5 Lower Limit',
                                        'pyname': u'load_range_5_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 5 upper limit',
                                       {'name': u'Load Range 5 Upper Limit',
                                        'pyname': u'load_range_5_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 6 lower limit',
                                       {'name': u'Load Range 6 Lower Limit',
                                        'pyname': u'load_range_6_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 6 upper limit',
                                       {'name': u'Load Range 6 Upper Limit',
                                        'pyname': u'load_range_6_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 7 lower limit',
                                       {'name': u'Load Range 7 Lower Limit',
                                        'pyname': u'load_range_7_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 7 upper limit',
                                       {'name': u'Load Range 7 Upper Limit',
                                        'pyname': u'load_range_7_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 8 lower limit',
                                       {'name': u'Load Range 8 Lower Limit',
                                        'pyname': u'load_range_8_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 8 upper limit',
                                       {'name': u'Load Range 8 Upper Limit',
                                        'pyname': u'load_range_8_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 9 lower limit',
                                       {'name': u'Load Range 9 Lower Limit',
                                        'pyname': u'load_range_9_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 9 upper limit',
                                       {'name': u'Load Range 9 Upper Limit',
                                        'pyname': u'load_range_9_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 10 lower limit',
                                       {'name': u'Load Range 10 Lower Limit',
                                        'pyname': u'load_range_10_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 10 upper limit',
                                       {'name': u'Load Range 10 Upper Limit',
                                        'pyname': u'load_range_10_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperation:CoolingLoad',
               'pyname': u'PlantEquipmentOperationCoolingLoad',
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
    def load_range_1_lower_limit(self):
        """field `Load Range 1 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_1_lower_limit` or None if not set

        """
        return self["Load Range 1 Lower Limit"]

    @load_range_1_lower_limit.setter
    def load_range_1_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 1 Lower Limit`"""
        self["Load Range 1 Lower Limit"] = value

    @property
    def load_range_1_upper_limit(self):
        """field `Load Range 1 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_1_upper_limit` or None if not set

        """
        return self["Load Range 1 Upper Limit"]

    @load_range_1_upper_limit.setter
    def load_range_1_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 1 Upper Limit`"""
        self["Load Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def load_range_2_lower_limit(self):
        """field `Load Range 2 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_2_lower_limit` or None if not set

        """
        return self["Load Range 2 Lower Limit"]

    @load_range_2_lower_limit.setter
    def load_range_2_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 2 Lower Limit`"""
        self["Load Range 2 Lower Limit"] = value

    @property
    def load_range_2_upper_limit(self):
        """field `Load Range 2 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_2_upper_limit` or None if not set

        """
        return self["Load Range 2 Upper Limit"]

    @load_range_2_upper_limit.setter
    def load_range_2_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 2 Upper Limit`"""
        self["Load Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def load_range_3_lower_limit(self):
        """field `Load Range 3 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_3_lower_limit` or None if not set

        """
        return self["Load Range 3 Lower Limit"]

    @load_range_3_lower_limit.setter
    def load_range_3_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 3 Lower Limit`"""
        self["Load Range 3 Lower Limit"] = value

    @property
    def load_range_3_upper_limit(self):
        """field `Load Range 3 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_3_upper_limit` or None if not set

        """
        return self["Load Range 3 Upper Limit"]

    @load_range_3_upper_limit.setter
    def load_range_3_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 3 Upper Limit`"""
        self["Load Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def load_range_4_lower_limit(self):
        """field `Load Range 4 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_4_lower_limit` or None if not set

        """
        return self["Load Range 4 Lower Limit"]

    @load_range_4_lower_limit.setter
    def load_range_4_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 4 Lower Limit`"""
        self["Load Range 4 Lower Limit"] = value

    @property
    def load_range_4_upper_limit(self):
        """field `Load Range 4 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_4_upper_limit` or None if not set

        """
        return self["Load Range 4 Upper Limit"]

    @load_range_4_upper_limit.setter
    def load_range_4_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 4 Upper Limit`"""
        self["Load Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def load_range_5_lower_limit(self):
        """field `Load Range 5 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_5_lower_limit` or None if not set

        """
        return self["Load Range 5 Lower Limit"]

    @load_range_5_lower_limit.setter
    def load_range_5_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 5 Lower Limit`"""
        self["Load Range 5 Lower Limit"] = value

    @property
    def load_range_5_upper_limit(self):
        """field `Load Range 5 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_5_upper_limit` or None if not set

        """
        return self["Load Range 5 Upper Limit"]

    @load_range_5_upper_limit.setter
    def load_range_5_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 5 Upper Limit`"""
        self["Load Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def load_range_6_lower_limit(self):
        """field `Load Range 6 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_6_lower_limit` or None if not set

        """
        return self["Load Range 6 Lower Limit"]

    @load_range_6_lower_limit.setter
    def load_range_6_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 6 Lower Limit`"""
        self["Load Range 6 Lower Limit"] = value

    @property
    def load_range_6_upper_limit(self):
        """field `Load Range 6 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_6_upper_limit` or None if not set

        """
        return self["Load Range 6 Upper Limit"]

    @load_range_6_upper_limit.setter
    def load_range_6_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 6 Upper Limit`"""
        self["Load Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def load_range_7_lower_limit(self):
        """field `Load Range 7 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_7_lower_limit` or None if not set

        """
        return self["Load Range 7 Lower Limit"]

    @load_range_7_lower_limit.setter
    def load_range_7_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 7 Lower Limit`"""
        self["Load Range 7 Lower Limit"] = value

    @property
    def load_range_7_upper_limit(self):
        """field `Load Range 7 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_7_upper_limit` or None if not set

        """
        return self["Load Range 7 Upper Limit"]

    @load_range_7_upper_limit.setter
    def load_range_7_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 7 Upper Limit`"""
        self["Load Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def load_range_8_lower_limit(self):
        """field `Load Range 8 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_8_lower_limit` or None if not set

        """
        return self["Load Range 8 Lower Limit"]

    @load_range_8_lower_limit.setter
    def load_range_8_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 8 Lower Limit`"""
        self["Load Range 8 Lower Limit"] = value

    @property
    def load_range_8_upper_limit(self):
        """field `Load Range 8 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_8_upper_limit` or None if not set

        """
        return self["Load Range 8 Upper Limit"]

    @load_range_8_upper_limit.setter
    def load_range_8_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 8 Upper Limit`"""
        self["Load Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def load_range_9_lower_limit(self):
        """field `Load Range 9 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_9_lower_limit` or None if not set

        """
        return self["Load Range 9 Lower Limit"]

    @load_range_9_lower_limit.setter
    def load_range_9_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 9 Lower Limit`"""
        self["Load Range 9 Lower Limit"] = value

    @property
    def load_range_9_upper_limit(self):
        """field `Load Range 9 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_9_upper_limit` or None if not set

        """
        return self["Load Range 9 Upper Limit"]

    @load_range_9_upper_limit.setter
    def load_range_9_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 9 Upper Limit`"""
        self["Load Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def load_range_10_lower_limit(self):
        """field `Load Range 10 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_10_lower_limit` or None if not set

        """
        return self["Load Range 10 Lower Limit"]

    @load_range_10_lower_limit.setter
    def load_range_10_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 10 Lower Limit`"""
        self["Load Range 10 Lower Limit"] = value

    @property
    def load_range_10_upper_limit(self):
        """field `Load Range 10 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_10_upper_limit` or None if not set

        """
        return self["Load Range 10 Upper Limit"]

    @load_range_10_upper_limit.setter
    def load_range_10_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 10 Upper Limit`"""
        self["Load Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationHeatingLoad(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:HeatingLoad`
        Plant equipment operation scheme for heating load range operation. Specifies one or
        more groups of equipment which are available to operate for successive heating load
        ranges.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'load range 1 lower limit',
                                       {'name': u'Load Range 1 Lower Limit',
                                        'pyname': u'load_range_1_lower_limit',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 1 upper limit',
                                       {'name': u'Load Range 1 Upper Limit',
                                        'pyname': u'load_range_1_upper_limit',
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 2 lower limit',
                                       {'name': u'Load Range 2 Lower Limit',
                                        'pyname': u'load_range_2_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 2 upper limit',
                                       {'name': u'Load Range 2 Upper Limit',
                                        'pyname': u'load_range_2_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 3 lower limit',
                                       {'name': u'Load Range 3 Lower Limit',
                                        'pyname': u'load_range_3_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 3 upper limit',
                                       {'name': u'Load Range 3 Upper Limit',
                                        'pyname': u'load_range_3_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 4 lower limit',
                                       {'name': u'Load Range 4 Lower Limit',
                                        'pyname': u'load_range_4_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 4 upper limit',
                                       {'name': u'Load Range 4 Upper Limit',
                                        'pyname': u'load_range_4_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 5 lower limit',
                                       {'name': u'Load Range 5 Lower Limit',
                                        'pyname': u'load_range_5_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 5 upper limit',
                                       {'name': u'Load Range 5 Upper Limit',
                                        'pyname': u'load_range_5_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 6 lower limit',
                                       {'name': u'Load Range 6 Lower Limit',
                                        'pyname': u'load_range_6_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 6 upper limit',
                                       {'name': u'Load Range 6 Upper Limit',
                                        'pyname': u'load_range_6_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 7 lower limit',
                                       {'name': u'Load Range 7 Lower Limit',
                                        'pyname': u'load_range_7_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 7 upper limit',
                                       {'name': u'Load Range 7 Upper Limit',
                                        'pyname': u'load_range_7_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 8 lower limit',
                                       {'name': u'Load Range 8 Lower Limit',
                                        'pyname': u'load_range_8_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 8 upper limit',
                                       {'name': u'Load Range 8 Upper Limit',
                                        'pyname': u'load_range_8_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 9 lower limit',
                                       {'name': u'Load Range 9 Lower Limit',
                                        'pyname': u'load_range_9_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 9 upper limit',
                                       {'name': u'Load Range 9 Upper Limit',
                                        'pyname': u'load_range_9_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'load range 10 lower limit',
                                       {'name': u'Load Range 10 Lower Limit',
                                        'pyname': u'load_range_10_lower_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'load range 10 upper limit',
                                       {'name': u'Load Range 10 Upper Limit',
                                        'pyname': u'load_range_10_upper_limit',
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperation:HeatingLoad',
               'pyname': u'PlantEquipmentOperationHeatingLoad',
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
    def load_range_1_lower_limit(self):
        """field `Load Range 1 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_1_lower_limit` or None if not set

        """
        return self["Load Range 1 Lower Limit"]

    @load_range_1_lower_limit.setter
    def load_range_1_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 1 Lower Limit`"""
        self["Load Range 1 Lower Limit"] = value

    @property
    def load_range_1_upper_limit(self):
        """field `Load Range 1 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_1_upper_limit` or None if not set

        """
        return self["Load Range 1 Upper Limit"]

    @load_range_1_upper_limit.setter
    def load_range_1_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 1 Upper Limit`"""
        self["Load Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def load_range_2_lower_limit(self):
        """field `Load Range 2 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_2_lower_limit` or None if not set

        """
        return self["Load Range 2 Lower Limit"]

    @load_range_2_lower_limit.setter
    def load_range_2_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 2 Lower Limit`"""
        self["Load Range 2 Lower Limit"] = value

    @property
    def load_range_2_upper_limit(self):
        """field `Load Range 2 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_2_upper_limit` or None if not set

        """
        return self["Load Range 2 Upper Limit"]

    @load_range_2_upper_limit.setter
    def load_range_2_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 2 Upper Limit`"""
        self["Load Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def load_range_3_lower_limit(self):
        """field `Load Range 3 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_3_lower_limit` or None if not set

        """
        return self["Load Range 3 Lower Limit"]

    @load_range_3_lower_limit.setter
    def load_range_3_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 3 Lower Limit`"""
        self["Load Range 3 Lower Limit"] = value

    @property
    def load_range_3_upper_limit(self):
        """field `Load Range 3 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_3_upper_limit` or None if not set

        """
        return self["Load Range 3 Upper Limit"]

    @load_range_3_upper_limit.setter
    def load_range_3_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 3 Upper Limit`"""
        self["Load Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def load_range_4_lower_limit(self):
        """field `Load Range 4 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_4_lower_limit` or None if not set

        """
        return self["Load Range 4 Lower Limit"]

    @load_range_4_lower_limit.setter
    def load_range_4_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 4 Lower Limit`"""
        self["Load Range 4 Lower Limit"] = value

    @property
    def load_range_4_upper_limit(self):
        """field `Load Range 4 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_4_upper_limit` or None if not set

        """
        return self["Load Range 4 Upper Limit"]

    @load_range_4_upper_limit.setter
    def load_range_4_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 4 Upper Limit`"""
        self["Load Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def load_range_5_lower_limit(self):
        """field `Load Range 5 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_5_lower_limit` or None if not set

        """
        return self["Load Range 5 Lower Limit"]

    @load_range_5_lower_limit.setter
    def load_range_5_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 5 Lower Limit`"""
        self["Load Range 5 Lower Limit"] = value

    @property
    def load_range_5_upper_limit(self):
        """field `Load Range 5 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_5_upper_limit` or None if not set

        """
        return self["Load Range 5 Upper Limit"]

    @load_range_5_upper_limit.setter
    def load_range_5_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 5 Upper Limit`"""
        self["Load Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def load_range_6_lower_limit(self):
        """field `Load Range 6 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_6_lower_limit` or None if not set

        """
        return self["Load Range 6 Lower Limit"]

    @load_range_6_lower_limit.setter
    def load_range_6_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 6 Lower Limit`"""
        self["Load Range 6 Lower Limit"] = value

    @property
    def load_range_6_upper_limit(self):
        """field `Load Range 6 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_6_upper_limit` or None if not set

        """
        return self["Load Range 6 Upper Limit"]

    @load_range_6_upper_limit.setter
    def load_range_6_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 6 Upper Limit`"""
        self["Load Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def load_range_7_lower_limit(self):
        """field `Load Range 7 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_7_lower_limit` or None if not set

        """
        return self["Load Range 7 Lower Limit"]

    @load_range_7_lower_limit.setter
    def load_range_7_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 7 Lower Limit`"""
        self["Load Range 7 Lower Limit"] = value

    @property
    def load_range_7_upper_limit(self):
        """field `Load Range 7 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_7_upper_limit` or None if not set

        """
        return self["Load Range 7 Upper Limit"]

    @load_range_7_upper_limit.setter
    def load_range_7_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 7 Upper Limit`"""
        self["Load Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def load_range_8_lower_limit(self):
        """field `Load Range 8 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_8_lower_limit` or None if not set

        """
        return self["Load Range 8 Lower Limit"]

    @load_range_8_lower_limit.setter
    def load_range_8_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 8 Lower Limit`"""
        self["Load Range 8 Lower Limit"] = value

    @property
    def load_range_8_upper_limit(self):
        """field `Load Range 8 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_8_upper_limit` or None if not set

        """
        return self["Load Range 8 Upper Limit"]

    @load_range_8_upper_limit.setter
    def load_range_8_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 8 Upper Limit`"""
        self["Load Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def load_range_9_lower_limit(self):
        """field `Load Range 9 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_9_lower_limit` or None if not set

        """
        return self["Load Range 9 Lower Limit"]

    @load_range_9_lower_limit.setter
    def load_range_9_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 9 Lower Limit`"""
        self["Load Range 9 Lower Limit"] = value

    @property
    def load_range_9_upper_limit(self):
        """field `Load Range 9 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_9_upper_limit` or None if not set

        """
        return self["Load Range 9 Upper Limit"]

    @load_range_9_upper_limit.setter
    def load_range_9_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 9 Upper Limit`"""
        self["Load Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def load_range_10_lower_limit(self):
        """field `Load Range 10 Lower Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_10_lower_limit` or None if not set

        """
        return self["Load Range 10 Lower Limit"]

    @load_range_10_lower_limit.setter
    def load_range_10_lower_limit(self, value=None):
        """Corresponds to IDD field `Load Range 10 Lower Limit`"""
        self["Load Range 10 Lower Limit"] = value

    @property
    def load_range_10_upper_limit(self):
        """field `Load Range 10 Upper Limit`

        |  Units: W

        Args:
            value (float): value for IDD Field `Load Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `load_range_10_upper_limit` or None if not set

        """
        return self["Load Range 10 Upper Limit"]

    @load_range_10_upper_limit.setter
    def load_range_10_upper_limit(self, value=None):
        """Corresponds to IDD field `Load Range 10 Upper Limit`"""
        self["Load Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationOutdoorDryBulb(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDryBulb`
        Plant equipment operation scheme for outdoor dry-bulb temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor dry-bulb temperature ranges.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dry-bulb temperature range 1 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 1 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_1_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 1 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 1 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_1_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 2 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 2 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_2_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 2 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 2 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_2_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 3 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 3 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_3_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 3 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 3 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_3_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 4 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 4 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_4_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 4 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 4 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_4_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 5 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 5 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_5_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 5 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 5 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_5_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 6 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 6 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_6_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 6 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 6 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_6_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 7 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 7 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_7_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 7 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 7 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_7_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 8 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 8 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_8_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 8 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 8 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_8_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 9 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 9 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_9_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 9 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 9 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_9_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature range 10 lower limit',
                                       {'name': u'Dry-Bulb Temperature Range 10 Lower Limit',
                                        'pyname': u'drybulb_temperature_range_10_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dry-bulb temperature range 10 upper limit',
                                       {'name': u'Dry-Bulb Temperature Range 10 Upper Limit',
                                        'pyname': u'drybulb_temperature_range_10_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperation:OutdoorDryBulb',
               'pyname': u'PlantEquipmentOperationOutdoorDryBulb',
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
    def drybulb_temperature_range_1_lower_limit(self):
        """field `Dry-Bulb Temperature Range 1 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_1_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 1 Lower Limit"]

    @drybulb_temperature_range_1_lower_limit.setter
    def drybulb_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 1 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 1 Lower Limit"] = value

    @property
    def drybulb_temperature_range_1_upper_limit(self):
        """field `Dry-Bulb Temperature Range 1 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_1_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 1 Upper Limit"]

    @drybulb_temperature_range_1_upper_limit.setter
    def drybulb_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 1 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_2_lower_limit(self):
        """field `Dry-Bulb Temperature Range 2 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_2_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 2 Lower Limit"]

    @drybulb_temperature_range_2_lower_limit.setter
    def drybulb_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 2 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 2 Lower Limit"] = value

    @property
    def drybulb_temperature_range_2_upper_limit(self):
        """field `Dry-Bulb Temperature Range 2 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_2_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 2 Upper Limit"]

    @drybulb_temperature_range_2_upper_limit.setter
    def drybulb_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 2 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_3_lower_limit(self):
        """field `Dry-Bulb Temperature Range 3 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_3_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 3 Lower Limit"]

    @drybulb_temperature_range_3_lower_limit.setter
    def drybulb_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 3 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 3 Lower Limit"] = value

    @property
    def drybulb_temperature_range_3_upper_limit(self):
        """field `Dry-Bulb Temperature Range 3 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_3_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 3 Upper Limit"]

    @drybulb_temperature_range_3_upper_limit.setter
    def drybulb_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 3 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_4_lower_limit(self):
        """field `Dry-Bulb Temperature Range 4 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_4_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 4 Lower Limit"]

    @drybulb_temperature_range_4_lower_limit.setter
    def drybulb_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 4 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 4 Lower Limit"] = value

    @property
    def drybulb_temperature_range_4_upper_limit(self):
        """field `Dry-Bulb Temperature Range 4 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_4_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 4 Upper Limit"]

    @drybulb_temperature_range_4_upper_limit.setter
    def drybulb_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 4 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_5_lower_limit(self):
        """field `Dry-Bulb Temperature Range 5 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_5_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 5 Lower Limit"]

    @drybulb_temperature_range_5_lower_limit.setter
    def drybulb_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 5 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 5 Lower Limit"] = value

    @property
    def drybulb_temperature_range_5_upper_limit(self):
        """field `Dry-Bulb Temperature Range 5 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_5_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 5 Upper Limit"]

    @drybulb_temperature_range_5_upper_limit.setter
    def drybulb_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 5 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_6_lower_limit(self):
        """field `Dry-Bulb Temperature Range 6 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_6_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 6 Lower Limit"]

    @drybulb_temperature_range_6_lower_limit.setter
    def drybulb_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 6 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 6 Lower Limit"] = value

    @property
    def drybulb_temperature_range_6_upper_limit(self):
        """field `Dry-Bulb Temperature Range 6 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_6_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 6 Upper Limit"]

    @drybulb_temperature_range_6_upper_limit.setter
    def drybulb_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 6 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_7_lower_limit(self):
        """field `Dry-Bulb Temperature Range 7 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_7_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 7 Lower Limit"]

    @drybulb_temperature_range_7_lower_limit.setter
    def drybulb_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 7 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 7 Lower Limit"] = value

    @property
    def drybulb_temperature_range_7_upper_limit(self):
        """field `Dry-Bulb Temperature Range 7 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_7_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 7 Upper Limit"]

    @drybulb_temperature_range_7_upper_limit.setter
    def drybulb_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 7 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_8_lower_limit(self):
        """field `Dry-Bulb Temperature Range 8 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_8_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 8 Lower Limit"]

    @drybulb_temperature_range_8_lower_limit.setter
    def drybulb_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 8 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 8 Lower Limit"] = value

    @property
    def drybulb_temperature_range_8_upper_limit(self):
        """field `Dry-Bulb Temperature Range 8 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_8_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 8 Upper Limit"]

    @drybulb_temperature_range_8_upper_limit.setter
    def drybulb_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 8 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_9_lower_limit(self):
        """field `Dry-Bulb Temperature Range 9 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_9_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 9 Lower Limit"]

    @drybulb_temperature_range_9_lower_limit.setter
    def drybulb_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 9 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 9 Lower Limit"] = value

    @property
    def drybulb_temperature_range_9_upper_limit(self):
        """field `Dry-Bulb Temperature Range 9 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_9_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 9 Upper Limit"]

    @drybulb_temperature_range_9_upper_limit.setter
    def drybulb_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 9 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def drybulb_temperature_range_10_lower_limit(self):
        """field `Dry-Bulb Temperature Range 10 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_10_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 10 Lower Limit"]

    @drybulb_temperature_range_10_lower_limit.setter
    def drybulb_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 10 Lower Limit`

        """
        self["Dry-Bulb Temperature Range 10 Lower Limit"] = value

    @property
    def drybulb_temperature_range_10_upper_limit(self):
        """field `Dry-Bulb Temperature Range 10 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_range_10_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Range 10 Upper Limit"]

    @drybulb_temperature_range_10_upper_limit.setter
    def drybulb_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Range 10 Upper Limit`

        """
        self["Dry-Bulb Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationOutdoorWetBulb(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorWetBulb`
        Plant equipment operation scheme for outdoor wet-bulb temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor wet-bulb temperature ranges.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'wet-bulb temperature range 1 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 1 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_1_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 1 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 1 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_1_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 2 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 2 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_2_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 2 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 2 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_2_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 3 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 3 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_3_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 3 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 3 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_3_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 4 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 4 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_4_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 4 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 4 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_4_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 5 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 5 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_5_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 5 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 5 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_5_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 6 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 6 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_6_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 6 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 6 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_6_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 7 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 7 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_7_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 7 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 7 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_7_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 8 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 8 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_8_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 8 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 8 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_8_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 9 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 9 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_9_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 9 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 9 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_9_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature range 10 lower limit',
                                       {'name': u'Wet-Bulb Temperature Range 10 Lower Limit',
                                        'pyname': u'wetbulb_temperature_range_10_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'wet-bulb temperature range 10 upper limit',
                                       {'name': u'Wet-Bulb Temperature Range 10 Upper Limit',
                                        'pyname': u'wetbulb_temperature_range_10_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperation:OutdoorWetBulb',
               'pyname': u'PlantEquipmentOperationOutdoorWetBulb',
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
    def wetbulb_temperature_range_1_lower_limit(self):
        """field `Wet-Bulb Temperature Range 1 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_1_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 1 Lower Limit"]

    @wetbulb_temperature_range_1_lower_limit.setter
    def wetbulb_temperature_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 1 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 1 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_1_upper_limit(self):
        """field `Wet-Bulb Temperature Range 1 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_1_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 1 Upper Limit"]

    @wetbulb_temperature_range_1_upper_limit.setter
    def wetbulb_temperature_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 1 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_2_lower_limit(self):
        """field `Wet-Bulb Temperature Range 2 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_2_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 2 Lower Limit"]

    @wetbulb_temperature_range_2_lower_limit.setter
    def wetbulb_temperature_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 2 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 2 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_2_upper_limit(self):
        """field `Wet-Bulb Temperature Range 2 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_2_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 2 Upper Limit"]

    @wetbulb_temperature_range_2_upper_limit.setter
    def wetbulb_temperature_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 2 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_3_lower_limit(self):
        """field `Wet-Bulb Temperature Range 3 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_3_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 3 Lower Limit"]

    @wetbulb_temperature_range_3_lower_limit.setter
    def wetbulb_temperature_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 3 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 3 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_3_upper_limit(self):
        """field `Wet-Bulb Temperature Range 3 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_3_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 3 Upper Limit"]

    @wetbulb_temperature_range_3_upper_limit.setter
    def wetbulb_temperature_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 3 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_4_lower_limit(self):
        """field `Wet-Bulb Temperature Range 4 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_4_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 4 Lower Limit"]

    @wetbulb_temperature_range_4_lower_limit.setter
    def wetbulb_temperature_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 4 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 4 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_4_upper_limit(self):
        """field `Wet-Bulb Temperature Range 4 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_4_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 4 Upper Limit"]

    @wetbulb_temperature_range_4_upper_limit.setter
    def wetbulb_temperature_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 4 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_5_lower_limit(self):
        """field `Wet-Bulb Temperature Range 5 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_5_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 5 Lower Limit"]

    @wetbulb_temperature_range_5_lower_limit.setter
    def wetbulb_temperature_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 5 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 5 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_5_upper_limit(self):
        """field `Wet-Bulb Temperature Range 5 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_5_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 5 Upper Limit"]

    @wetbulb_temperature_range_5_upper_limit.setter
    def wetbulb_temperature_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 5 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_6_lower_limit(self):
        """field `Wet-Bulb Temperature Range 6 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_6_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 6 Lower Limit"]

    @wetbulb_temperature_range_6_lower_limit.setter
    def wetbulb_temperature_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 6 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 6 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_6_upper_limit(self):
        """field `Wet-Bulb Temperature Range 6 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_6_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 6 Upper Limit"]

    @wetbulb_temperature_range_6_upper_limit.setter
    def wetbulb_temperature_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 6 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_7_lower_limit(self):
        """field `Wet-Bulb Temperature Range 7 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_7_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 7 Lower Limit"]

    @wetbulb_temperature_range_7_lower_limit.setter
    def wetbulb_temperature_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 7 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 7 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_7_upper_limit(self):
        """field `Wet-Bulb Temperature Range 7 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_7_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 7 Upper Limit"]

    @wetbulb_temperature_range_7_upper_limit.setter
    def wetbulb_temperature_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 7 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_8_lower_limit(self):
        """field `Wet-Bulb Temperature Range 8 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_8_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 8 Lower Limit"]

    @wetbulb_temperature_range_8_lower_limit.setter
    def wetbulb_temperature_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 8 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 8 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_8_upper_limit(self):
        """field `Wet-Bulb Temperature Range 8 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_8_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 8 Upper Limit"]

    @wetbulb_temperature_range_8_upper_limit.setter
    def wetbulb_temperature_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 8 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_9_lower_limit(self):
        """field `Wet-Bulb Temperature Range 9 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_9_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 9 Lower Limit"]

    @wetbulb_temperature_range_9_lower_limit.setter
    def wetbulb_temperature_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 9 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 9 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_9_upper_limit(self):
        """field `Wet-Bulb Temperature Range 9 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_9_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 9 Upper Limit"]

    @wetbulb_temperature_range_9_upper_limit.setter
    def wetbulb_temperature_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 9 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def wetbulb_temperature_range_10_lower_limit(self):
        """field `Wet-Bulb Temperature Range 10 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_10_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 10 Lower Limit"]

    @wetbulb_temperature_range_10_lower_limit.setter
    def wetbulb_temperature_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 10 Lower Limit`

        """
        self["Wet-Bulb Temperature Range 10 Lower Limit"] = value

    @property
    def wetbulb_temperature_range_10_upper_limit(self):
        """field `Wet-Bulb Temperature Range 10 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_range_10_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Range 10 Upper Limit"]

    @wetbulb_temperature_range_10_upper_limit.setter
    def wetbulb_temperature_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Range 10 Upper Limit`

        """
        self["Wet-Bulb Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationOutdoorRelativeHumidity(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorRelativeHumidity`
        Plant equipment operation scheme for outdoor relative humidity range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor relative humidity ranges.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'relative humidity range 1 lower limit',
                                       {'name': u'Relative Humidity Range 1 Lower Limit',
                                        'pyname': u'relative_humidity_range_1_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 1 upper limit',
                                       {'name': u'Relative Humidity Range 1 Upper Limit',
                                        'pyname': u'relative_humidity_range_1_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 2 lower limit',
                                       {'name': u'Relative Humidity Range 2 Lower Limit',
                                        'pyname': u'relative_humidity_range_2_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 2 upper limit',
                                       {'name': u'Relative Humidity Range 2 Upper Limit',
                                        'pyname': u'relative_humidity_range_2_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 3 lower limit',
                                       {'name': u'Relative Humidity Range 3 Lower Limit',
                                        'pyname': u'relative_humidity_range_3_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 3 upper limit',
                                       {'name': u'Relative Humidity Range 3 Upper Limit',
                                        'pyname': u'relative_humidity_range_3_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 4 lower limit',
                                       {'name': u'Relative Humidity Range 4 Lower Limit',
                                        'pyname': u'relative_humidity_range_4_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 4 upper limit',
                                       {'name': u'Relative Humidity Range 4 Upper Limit',
                                        'pyname': u'relative_humidity_range_4_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 5 lower limit',
                                       {'name': u'Relative Humidity Range 5 Lower Limit',
                                        'pyname': u'relative_humidity_range_5_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 5 upper limit',
                                       {'name': u'Relative Humidity Range 5 Upper Limit',
                                        'pyname': u'relative_humidity_range_5_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 6 lower limit',
                                       {'name': u'Relative Humidity Range 6 Lower Limit',
                                        'pyname': u'relative_humidity_range_6_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 6 upper limit',
                                       {'name': u'Relative Humidity Range 6 Upper Limit',
                                        'pyname': u'relative_humidity_range_6_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 7 lower limit',
                                       {'name': u'Relative Humidity Range 7 Lower Limit',
                                        'pyname': u'relative_humidity_range_7_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 7 upper limit',
                                       {'name': u'Relative Humidity Range 7 Upper Limit',
                                        'pyname': u'relative_humidity_range_7_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 8 lower limit',
                                       {'name': u'Relative Humidity Range 8 Lower Limit',
                                        'pyname': u'relative_humidity_range_8_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 8 upper limit',
                                       {'name': u'Relative Humidity Range 8 Upper Limit',
                                        'pyname': u'relative_humidity_range_8_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 9 lower limit',
                                       {'name': u'Relative Humidity Range 9 Lower Limit',
                                        'pyname': u'relative_humidity_range_9_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 9 upper limit',
                                       {'name': u'Relative Humidity Range 9 Upper Limit',
                                        'pyname': u'relative_humidity_range_9_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'relative humidity range 10 lower limit',
                                       {'name': u'Relative Humidity Range 10 Lower Limit',
                                        'pyname': u'relative_humidity_range_10_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'relative humidity range 10 upper limit',
                                       {'name': u'Relative Humidity Range 10 Upper Limit',
                                        'pyname': u'relative_humidity_range_10_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'percent'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperation:OutdoorRelativeHumidity',
               'pyname': u'PlantEquipmentOperationOutdoorRelativeHumidity',
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
    def relative_humidity_range_1_lower_limit(self):
        """field `Relative Humidity Range 1 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_1_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 1 Lower Limit"]

    @relative_humidity_range_1_lower_limit.setter
    def relative_humidity_range_1_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 1 Lower Limit`"""
        self["Relative Humidity Range 1 Lower Limit"] = value

    @property
    def relative_humidity_range_1_upper_limit(self):
        """field `Relative Humidity Range 1 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_1_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 1 Upper Limit"]

    @relative_humidity_range_1_upper_limit.setter
    def relative_humidity_range_1_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 1 Upper Limit`"""
        self["Relative Humidity Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def relative_humidity_range_2_lower_limit(self):
        """field `Relative Humidity Range 2 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_2_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 2 Lower Limit"]

    @relative_humidity_range_2_lower_limit.setter
    def relative_humidity_range_2_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 2 Lower Limit`"""
        self["Relative Humidity Range 2 Lower Limit"] = value

    @property
    def relative_humidity_range_2_upper_limit(self):
        """field `Relative Humidity Range 2 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_2_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 2 Upper Limit"]

    @relative_humidity_range_2_upper_limit.setter
    def relative_humidity_range_2_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 2 Upper Limit`"""
        self["Relative Humidity Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def relative_humidity_range_3_lower_limit(self):
        """field `Relative Humidity Range 3 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_3_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 3 Lower Limit"]

    @relative_humidity_range_3_lower_limit.setter
    def relative_humidity_range_3_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 3 Lower Limit`"""
        self["Relative Humidity Range 3 Lower Limit"] = value

    @property
    def relative_humidity_range_3_upper_limit(self):
        """field `Relative Humidity Range 3 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_3_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 3 Upper Limit"]

    @relative_humidity_range_3_upper_limit.setter
    def relative_humidity_range_3_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 3 Upper Limit`"""
        self["Relative Humidity Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def relative_humidity_range_4_lower_limit(self):
        """field `Relative Humidity Range 4 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_4_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 4 Lower Limit"]

    @relative_humidity_range_4_lower_limit.setter
    def relative_humidity_range_4_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 4 Lower Limit`"""
        self["Relative Humidity Range 4 Lower Limit"] = value

    @property
    def relative_humidity_range_4_upper_limit(self):
        """field `Relative Humidity Range 4 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_4_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 4 Upper Limit"]

    @relative_humidity_range_4_upper_limit.setter
    def relative_humidity_range_4_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 4 Upper Limit`"""
        self["Relative Humidity Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def relative_humidity_range_5_lower_limit(self):
        """field `Relative Humidity Range 5 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_5_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 5 Lower Limit"]

    @relative_humidity_range_5_lower_limit.setter
    def relative_humidity_range_5_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 5 Lower Limit`"""
        self["Relative Humidity Range 5 Lower Limit"] = value

    @property
    def relative_humidity_range_5_upper_limit(self):
        """field `Relative Humidity Range 5 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_5_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 5 Upper Limit"]

    @relative_humidity_range_5_upper_limit.setter
    def relative_humidity_range_5_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 5 Upper Limit`"""
        self["Relative Humidity Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def relative_humidity_range_6_lower_limit(self):
        """field `Relative Humidity Range 6 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_6_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 6 Lower Limit"]

    @relative_humidity_range_6_lower_limit.setter
    def relative_humidity_range_6_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 6 Lower Limit`"""
        self["Relative Humidity Range 6 Lower Limit"] = value

    @property
    def relative_humidity_range_6_upper_limit(self):
        """field `Relative Humidity Range 6 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_6_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 6 Upper Limit"]

    @relative_humidity_range_6_upper_limit.setter
    def relative_humidity_range_6_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 6 Upper Limit`"""
        self["Relative Humidity Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def relative_humidity_range_7_lower_limit(self):
        """field `Relative Humidity Range 7 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_7_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 7 Lower Limit"]

    @relative_humidity_range_7_lower_limit.setter
    def relative_humidity_range_7_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 7 Lower Limit`"""
        self["Relative Humidity Range 7 Lower Limit"] = value

    @property
    def relative_humidity_range_7_upper_limit(self):
        """field `Relative Humidity Range 7 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_7_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 7 Upper Limit"]

    @relative_humidity_range_7_upper_limit.setter
    def relative_humidity_range_7_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 7 Upper Limit`"""
        self["Relative Humidity Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def relative_humidity_range_8_lower_limit(self):
        """field `Relative Humidity Range 8 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_8_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 8 Lower Limit"]

    @relative_humidity_range_8_lower_limit.setter
    def relative_humidity_range_8_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 8 Lower Limit`"""
        self["Relative Humidity Range 8 Lower Limit"] = value

    @property
    def relative_humidity_range_8_upper_limit(self):
        """field `Relative Humidity Range 8 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_8_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 8 Upper Limit"]

    @relative_humidity_range_8_upper_limit.setter
    def relative_humidity_range_8_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 8 Upper Limit`"""
        self["Relative Humidity Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def relative_humidity_range_9_lower_limit(self):
        """field `Relative Humidity Range 9 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_9_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 9 Lower Limit"]

    @relative_humidity_range_9_lower_limit.setter
    def relative_humidity_range_9_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 9 Lower Limit`"""
        self["Relative Humidity Range 9 Lower Limit"] = value

    @property
    def relative_humidity_range_9_upper_limit(self):
        """field `Relative Humidity Range 9 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_9_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 9 Upper Limit"]

    @relative_humidity_range_9_upper_limit.setter
    def relative_humidity_range_9_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 9 Upper Limit`"""
        self["Relative Humidity Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def relative_humidity_range_10_lower_limit(self):
        """field `Relative Humidity Range 10 Lower Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_10_lower_limit` or None if not set

        """
        return self["Relative Humidity Range 10 Lower Limit"]

    @relative_humidity_range_10_lower_limit.setter
    def relative_humidity_range_10_lower_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 10 Lower Limit`"""
        self["Relative Humidity Range 10 Lower Limit"] = value

    @property
    def relative_humidity_range_10_upper_limit(self):
        """field `Relative Humidity Range 10 Upper Limit`

        |  Units: percent
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Relative Humidity Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `relative_humidity_range_10_upper_limit` or None if not set

        """
        return self["Relative Humidity Range 10 Upper Limit"]

    @relative_humidity_range_10_upper_limit.setter
    def relative_humidity_range_10_upper_limit(self, value=None):
        """Corresponds to IDD field `Relative Humidity Range 10 Upper Limit`"""
        self["Relative Humidity Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationOutdoorDewpoint(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDewpoint`
        Plant equipment operation scheme for outdoor dewpoint temperature range operation.
        Specifies one or more groups of equipment which are available to operate for
        successive outdoor dewpoint temperature ranges.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'dewpoint temperature range 1 lower limit',
                                       {'name': u'Dewpoint Temperature Range 1 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_1_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 1 upper limit',
                                       {'name': u'Dewpoint Temperature Range 1 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_1_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 2 lower limit',
                                       {'name': u'Dewpoint Temperature Range 2 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_2_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 2 upper limit',
                                       {'name': u'Dewpoint Temperature Range 2 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_2_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 3 lower limit',
                                       {'name': u'Dewpoint Temperature Range 3 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_3_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 3 upper limit',
                                       {'name': u'Dewpoint Temperature Range 3 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_3_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 4 lower limit',
                                       {'name': u'Dewpoint Temperature Range 4 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_4_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 4 upper limit',
                                       {'name': u'Dewpoint Temperature Range 4 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_4_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 5 lower limit',
                                       {'name': u'Dewpoint Temperature Range 5 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_5_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 5 upper limit',
                                       {'name': u'Dewpoint Temperature Range 5 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_5_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 6 lower limit',
                                       {'name': u'Dewpoint Temperature Range 6 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_6_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 6 upper limit',
                                       {'name': u'Dewpoint Temperature Range 6 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_6_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 7 lower limit',
                                       {'name': u'Dewpoint Temperature Range 7 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_7_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 7 upper limit',
                                       {'name': u'Dewpoint Temperature Range 7 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_7_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 8 lower limit',
                                       {'name': u'Dewpoint Temperature Range 8 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_8_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 8 upper limit',
                                       {'name': u'Dewpoint Temperature Range 8 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_8_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 9 lower limit',
                                       {'name': u'Dewpoint Temperature Range 9 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_9_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 9 upper limit',
                                       {'name': u'Dewpoint Temperature Range 9 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_9_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature range 10 lower limit',
                                       {'name': u'Dewpoint Temperature Range 10 Lower Limit',
                                        'pyname': u'dewpoint_temperature_range_10_lower_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'dewpoint temperature range 10 upper limit',
                                       {'name': u'Dewpoint Temperature Range 10 Upper Limit',
                                        'pyname': u'dewpoint_temperature_range_10_upper_limit',
                                        'maximum': 70.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -70.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperation:OutdoorDewpoint',
               'pyname': u'PlantEquipmentOperationOutdoorDewpoint',
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
    def dewpoint_temperature_range_1_lower_limit(self):
        """field `Dewpoint Temperature Range 1 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_1_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 1 Lower Limit"]

    @dewpoint_temperature_range_1_lower_limit.setter
    def dewpoint_temperature_range_1_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 1 Lower
        Limit`"""
        self["Dewpoint Temperature Range 1 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_1_upper_limit(self):
        """field `Dewpoint Temperature Range 1 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_1_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 1 Upper Limit"]

    @dewpoint_temperature_range_1_upper_limit.setter
    def dewpoint_temperature_range_1_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 1 Upper
        Limit`"""
        self["Dewpoint Temperature Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_2_lower_limit(self):
        """field `Dewpoint Temperature Range 2 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_2_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 2 Lower Limit"]

    @dewpoint_temperature_range_2_lower_limit.setter
    def dewpoint_temperature_range_2_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 2 Lower
        Limit`"""
        self["Dewpoint Temperature Range 2 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_2_upper_limit(self):
        """field `Dewpoint Temperature Range 2 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_2_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 2 Upper Limit"]

    @dewpoint_temperature_range_2_upper_limit.setter
    def dewpoint_temperature_range_2_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 2 Upper
        Limit`"""
        self["Dewpoint Temperature Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_3_lower_limit(self):
        """field `Dewpoint Temperature Range 3 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_3_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 3 Lower Limit"]

    @dewpoint_temperature_range_3_lower_limit.setter
    def dewpoint_temperature_range_3_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 3 Lower
        Limit`"""
        self["Dewpoint Temperature Range 3 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_3_upper_limit(self):
        """field `Dewpoint Temperature Range 3 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_3_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 3 Upper Limit"]

    @dewpoint_temperature_range_3_upper_limit.setter
    def dewpoint_temperature_range_3_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 3 Upper
        Limit`"""
        self["Dewpoint Temperature Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_4_lower_limit(self):
        """field `Dewpoint Temperature Range 4 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_4_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 4 Lower Limit"]

    @dewpoint_temperature_range_4_lower_limit.setter
    def dewpoint_temperature_range_4_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 4 Lower
        Limit`"""
        self["Dewpoint Temperature Range 4 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_4_upper_limit(self):
        """field `Dewpoint Temperature Range 4 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_4_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 4 Upper Limit"]

    @dewpoint_temperature_range_4_upper_limit.setter
    def dewpoint_temperature_range_4_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 4 Upper
        Limit`"""
        self["Dewpoint Temperature Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_5_lower_limit(self):
        """field `Dewpoint Temperature Range 5 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_5_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 5 Lower Limit"]

    @dewpoint_temperature_range_5_lower_limit.setter
    def dewpoint_temperature_range_5_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 5 Lower
        Limit`"""
        self["Dewpoint Temperature Range 5 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_5_upper_limit(self):
        """field `Dewpoint Temperature Range 5 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_5_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 5 Upper Limit"]

    @dewpoint_temperature_range_5_upper_limit.setter
    def dewpoint_temperature_range_5_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 5 Upper
        Limit`"""
        self["Dewpoint Temperature Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_6_lower_limit(self):
        """field `Dewpoint Temperature Range 6 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_6_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 6 Lower Limit"]

    @dewpoint_temperature_range_6_lower_limit.setter
    def dewpoint_temperature_range_6_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 6 Lower
        Limit`"""
        self["Dewpoint Temperature Range 6 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_6_upper_limit(self):
        """field `Dewpoint Temperature Range 6 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_6_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 6 Upper Limit"]

    @dewpoint_temperature_range_6_upper_limit.setter
    def dewpoint_temperature_range_6_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 6 Upper
        Limit`"""
        self["Dewpoint Temperature Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_7_lower_limit(self):
        """field `Dewpoint Temperature Range 7 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_7_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 7 Lower Limit"]

    @dewpoint_temperature_range_7_lower_limit.setter
    def dewpoint_temperature_range_7_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 7 Lower
        Limit`"""
        self["Dewpoint Temperature Range 7 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_7_upper_limit(self):
        """field `Dewpoint Temperature Range 7 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_7_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 7 Upper Limit"]

    @dewpoint_temperature_range_7_upper_limit.setter
    def dewpoint_temperature_range_7_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 7 Upper
        Limit`"""
        self["Dewpoint Temperature Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_8_lower_limit(self):
        """field `Dewpoint Temperature Range 8 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_8_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 8 Lower Limit"]

    @dewpoint_temperature_range_8_lower_limit.setter
    def dewpoint_temperature_range_8_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 8 Lower
        Limit`"""
        self["Dewpoint Temperature Range 8 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_8_upper_limit(self):
        """field `Dewpoint Temperature Range 8 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_8_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 8 Upper Limit"]

    @dewpoint_temperature_range_8_upper_limit.setter
    def dewpoint_temperature_range_8_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 8 Upper
        Limit`"""
        self["Dewpoint Temperature Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_9_lower_limit(self):
        """field `Dewpoint Temperature Range 9 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_9_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 9 Lower Limit"]

    @dewpoint_temperature_range_9_lower_limit.setter
    def dewpoint_temperature_range_9_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 9 Lower
        Limit`"""
        self["Dewpoint Temperature Range 9 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_9_upper_limit(self):
        """field `Dewpoint Temperature Range 9 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_9_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 9 Upper Limit"]

    @dewpoint_temperature_range_9_upper_limit.setter
    def dewpoint_temperature_range_9_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 9 Upper
        Limit`"""
        self["Dewpoint Temperature Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def dewpoint_temperature_range_10_lower_limit(self):
        """field `Dewpoint Temperature Range 10 Lower Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_10_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 10 Lower Limit"]

    @dewpoint_temperature_range_10_lower_limit.setter
    def dewpoint_temperature_range_10_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 10 Lower
        Limit`"""
        self["Dewpoint Temperature Range 10 Lower Limit"] = value

    @property
    def dewpoint_temperature_range_10_upper_limit(self):
        """field `Dewpoint Temperature Range 10 Upper Limit`

        |  Units: C
        |  value >= -70.0
        |  value <= 70.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_range_10_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Range 10 Upper Limit"]

    @dewpoint_temperature_range_10_upper_limit.setter
    def dewpoint_temperature_range_10_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Range 10 Upper
        Limit`"""
        self["Dewpoint Temperature Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationComponentSetpoint(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:ComponentSetpoint`
        Plant equipment operation scheme for component setpoint operation. Specifies one or
        pieces of equipment which are controlled to meet the temperature setpoint at the
        component outlet node.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 1 object type',
                                       {'name': u'Equipment 1 Object Type',
                                        'pyname': u'equipment_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 1 name',
                                       {'name': u'Equipment 1 Name',
                                        'pyname': u'equipment_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 1 node name',
                                       {'name': u'Demand Calculation 1 Node Name',
                                        'pyname': u'demand_calculation_1_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 1 node name',
                                       {'name': u'Setpoint 1 Node Name',
                                        'pyname': u'setpoint_1_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 1 flow rate',
                                       {'name': u'Component 1 Flow Rate',
                                        'pyname': u'component_1_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 1 type',
                                       {'name': u'Operation 1 Type',
                                        'pyname': u'operation_1_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 2 object type',
                                       {'name': u'Equipment 2 Object Type',
                                        'pyname': u'equipment_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 2 name',
                                       {'name': u'Equipment 2 Name',
                                        'pyname': u'equipment_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 2 node name',
                                       {'name': u'Demand Calculation 2 Node Name',
                                        'pyname': u'demand_calculation_2_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 2 node name',
                                       {'name': u'Setpoint 2 Node Name',
                                        'pyname': u'setpoint_2_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 2 flow rate',
                                       {'name': u'Component 2 Flow Rate',
                                        'pyname': u'component_2_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 2 type',
                                       {'name': u'Operation 2 Type',
                                        'pyname': u'operation_2_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 3 object type',
                                       {'name': u'Equipment 3 Object Type',
                                        'pyname': u'equipment_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 3 name',
                                       {'name': u'Equipment 3 Name',
                                        'pyname': u'equipment_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 3 node name',
                                       {'name': u'Demand Calculation 3 Node Name',
                                        'pyname': u'demand_calculation_3_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 3 node name',
                                       {'name': u'Setpoint 3 Node Name',
                                        'pyname': u'setpoint_3_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 3 flow rate',
                                       {'name': u'Component 3 Flow Rate',
                                        'pyname': u'component_3_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 3 type',
                                       {'name': u'Operation 3 Type',
                                        'pyname': u'operation_3_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 4 object type',
                                       {'name': u'Equipment 4 Object Type',
                                        'pyname': u'equipment_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 4 name',
                                       {'name': u'Equipment 4 Name',
                                        'pyname': u'equipment_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 4 node name',
                                       {'name': u'Demand Calculation 4 Node Name',
                                        'pyname': u'demand_calculation_4_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 4 node name',
                                       {'name': u'Setpoint 4 Node Name',
                                        'pyname': u'setpoint_4_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 4 flow rate',
                                       {'name': u'Component 4 Flow Rate',
                                        'pyname': u'component_4_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 4 type',
                                       {'name': u'Operation 4 Type',
                                        'pyname': u'operation_4_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 5 object type',
                                       {'name': u'Equipment 5 Object Type',
                                        'pyname': u'equipment_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 5 name',
                                       {'name': u'Equipment 5 Name',
                                        'pyname': u'equipment_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 5 node name',
                                       {'name': u'Demand Calculation 5 Node Name',
                                        'pyname': u'demand_calculation_5_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 5 node name',
                                       {'name': u'Setpoint 5 Node Name',
                                        'pyname': u'setpoint_5_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 5 flow rate',
                                       {'name': u'Component 5 Flow Rate',
                                        'pyname': u'component_5_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 5 type',
                                       {'name': u'Operation 5 Type',
                                        'pyname': u'operation_5_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 6 object type',
                                       {'name': u'Equipment 6 Object Type',
                                        'pyname': u'equipment_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 6 name',
                                       {'name': u'Equipment 6 Name',
                                        'pyname': u'equipment_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 6 node name',
                                       {'name': u'Demand Calculation 6 Node Name',
                                        'pyname': u'demand_calculation_6_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 6 node name',
                                       {'name': u'Setpoint 6 Node Name',
                                        'pyname': u'setpoint_6_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 6 flow rate',
                                       {'name': u'Component 6 Flow Rate',
                                        'pyname': u'component_6_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 6 type',
                                       {'name': u'Operation 6 Type',
                                        'pyname': u'operation_6_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 7 object type',
                                       {'name': u'Equipment 7 Object Type',
                                        'pyname': u'equipment_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 7 name',
                                       {'name': u'Equipment 7 Name',
                                        'pyname': u'equipment_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 7 node name',
                                       {'name': u'Demand Calculation 7 Node Name',
                                        'pyname': u'demand_calculation_7_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 7 node name',
                                       {'name': u'Setpoint 7 Node Name',
                                        'pyname': u'setpoint_7_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 7 flow rate',
                                       {'name': u'Component 7 Flow Rate',
                                        'pyname': u'component_7_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 7 type',
                                       {'name': u'Operation 7 Type',
                                        'pyname': u'operation_7_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 8 object type',
                                       {'name': u'Equipment 8 Object Type',
                                        'pyname': u'equipment_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 8 name',
                                       {'name': u'Equipment 8 Name',
                                        'pyname': u'equipment_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 8 node name',
                                       {'name': u'Demand Calculation 8 Node Name',
                                        'pyname': u'demand_calculation_8_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 8 node name',
                                       {'name': u'Setpoint 8 Node Name',
                                        'pyname': u'setpoint_8_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 8 flow rate',
                                       {'name': u'Component 8 Flow Rate',
                                        'pyname': u'component_8_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 8 type',
                                       {'name': u'Operation 8 Type',
                                        'pyname': u'operation_8_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 9 object type',
                                       {'name': u'Equipment 9 Object Type',
                                        'pyname': u'equipment_9_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 9 name',
                                       {'name': u'Equipment 9 Name',
                                        'pyname': u'equipment_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 9 node name',
                                       {'name': u'Demand Calculation 9 Node Name',
                                        'pyname': u'demand_calculation_9_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 9 node name',
                                       {'name': u'Setpoint 9 Node Name',
                                        'pyname': u'setpoint_9_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 9 flow rate',
                                       {'name': u'Component 9 Flow Rate',
                                        'pyname': u'component_9_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 9 type',
                                       {'name': u'Operation 9 Type',
                                        'pyname': u'operation_9_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equipment 10 object type',
                                       {'name': u'Equipment 10 Object Type',
                                        'pyname': u'equipment_10_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 10 name',
                                       {'name': u'Equipment 10 Name',
                                        'pyname': u'equipment_10_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'demand calculation 10 node name',
                                       {'name': u'Demand Calculation 10 Node Name',
                                        'pyname': u'demand_calculation_10_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'setpoint 10 node name',
                                       {'name': u'Setpoint 10 Node Name',
                                        'pyname': u'setpoint_10_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 10 flow rate',
                                       {'name': u'Component 10 Flow Rate',
                                        'pyname': u'component_10_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'operation 10 type',
                                       {'name': u'Operation 10 Type',
                                        'pyname': u'operation_10_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 7,
               'name': u'PlantEquipmentOperation:ComponentSetpoint',
               'pyname': u'PlantEquipmentOperationComponentSetpoint',
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
    def equipment_1_object_type(self):
        """field `Equipment 1 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_1_object_type` or None if not set

        """
        return self["Equipment 1 Object Type"]

    @equipment_1_object_type.setter
    def equipment_1_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 1 Object Type`"""
        self["Equipment 1 Object Type"] = value

    @property
    def equipment_1_name(self):
        """field `Equipment 1 Name`

        Args:
            value (str): value for IDD Field `Equipment 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_1_name` or None if not set

        """
        return self["Equipment 1 Name"]

    @equipment_1_name.setter
    def equipment_1_name(self, value=None):
        """Corresponds to IDD field `Equipment 1 Name`"""
        self["Equipment 1 Name"] = value

    @property
    def demand_calculation_1_node_name(self):
        """field `Demand Calculation 1 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 1 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_1_node_name` or None if not set

        """
        return self["Demand Calculation 1 Node Name"]

    @demand_calculation_1_node_name.setter
    def demand_calculation_1_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 1 Node Name`"""
        self["Demand Calculation 1 Node Name"] = value

    @property
    def setpoint_1_node_name(self):
        """field `Setpoint 1 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 1 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_1_node_name` or None if not set

        """
        return self["Setpoint 1 Node Name"]

    @setpoint_1_node_name.setter
    def setpoint_1_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 1 Node Name`"""
        self["Setpoint 1 Node Name"] = value

    @property
    def component_1_flow_rate(self):
        """field `Component 1 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 1 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_1_flow_rate` or None if not set

        """
        return self["Component 1 Flow Rate"]

    @component_1_flow_rate.setter
    def component_1_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 1 Flow Rate`"""
        self["Component 1 Flow Rate"] = value

    @property
    def operation_1_type(self):
        """field `Operation 1 Type`

        Args:
            value (str): value for IDD Field `Operation 1 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_1_type` or None if not set

        """
        return self["Operation 1 Type"]

    @operation_1_type.setter
    def operation_1_type(self, value=None):
        """Corresponds to IDD field `Operation 1 Type`"""
        self["Operation 1 Type"] = value

    @property
    def equipment_2_object_type(self):
        """field `Equipment 2 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_2_object_type` or None if not set

        """
        return self["Equipment 2 Object Type"]

    @equipment_2_object_type.setter
    def equipment_2_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 2 Object Type`"""
        self["Equipment 2 Object Type"] = value

    @property
    def equipment_2_name(self):
        """field `Equipment 2 Name`

        Args:
            value (str): value for IDD Field `Equipment 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_2_name` or None if not set

        """
        return self["Equipment 2 Name"]

    @equipment_2_name.setter
    def equipment_2_name(self, value=None):
        """Corresponds to IDD field `Equipment 2 Name`"""
        self["Equipment 2 Name"] = value

    @property
    def demand_calculation_2_node_name(self):
        """field `Demand Calculation 2 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 2 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_2_node_name` or None if not set

        """
        return self["Demand Calculation 2 Node Name"]

    @demand_calculation_2_node_name.setter
    def demand_calculation_2_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 2 Node Name`"""
        self["Demand Calculation 2 Node Name"] = value

    @property
    def setpoint_2_node_name(self):
        """field `Setpoint 2 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 2 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_2_node_name` or None if not set

        """
        return self["Setpoint 2 Node Name"]

    @setpoint_2_node_name.setter
    def setpoint_2_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 2 Node Name`"""
        self["Setpoint 2 Node Name"] = value

    @property
    def component_2_flow_rate(self):
        """field `Component 2 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 2 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_2_flow_rate` or None if not set

        """
        return self["Component 2 Flow Rate"]

    @component_2_flow_rate.setter
    def component_2_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 2 Flow Rate`"""
        self["Component 2 Flow Rate"] = value

    @property
    def operation_2_type(self):
        """field `Operation 2 Type`

        Args:
            value (str): value for IDD Field `Operation 2 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_2_type` or None if not set

        """
        return self["Operation 2 Type"]

    @operation_2_type.setter
    def operation_2_type(self, value=None):
        """Corresponds to IDD field `Operation 2 Type`"""
        self["Operation 2 Type"] = value

    @property
    def equipment_3_object_type(self):
        """field `Equipment 3 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_3_object_type` or None if not set

        """
        return self["Equipment 3 Object Type"]

    @equipment_3_object_type.setter
    def equipment_3_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 3 Object Type`"""
        self["Equipment 3 Object Type"] = value

    @property
    def equipment_3_name(self):
        """field `Equipment 3 Name`

        Args:
            value (str): value for IDD Field `Equipment 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_3_name` or None if not set

        """
        return self["Equipment 3 Name"]

    @equipment_3_name.setter
    def equipment_3_name(self, value=None):
        """Corresponds to IDD field `Equipment 3 Name`"""
        self["Equipment 3 Name"] = value

    @property
    def demand_calculation_3_node_name(self):
        """field `Demand Calculation 3 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 3 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_3_node_name` or None if not set

        """
        return self["Demand Calculation 3 Node Name"]

    @demand_calculation_3_node_name.setter
    def demand_calculation_3_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 3 Node Name`"""
        self["Demand Calculation 3 Node Name"] = value

    @property
    def setpoint_3_node_name(self):
        """field `Setpoint 3 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 3 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_3_node_name` or None if not set

        """
        return self["Setpoint 3 Node Name"]

    @setpoint_3_node_name.setter
    def setpoint_3_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 3 Node Name`"""
        self["Setpoint 3 Node Name"] = value

    @property
    def component_3_flow_rate(self):
        """field `Component 3 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 3 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_3_flow_rate` or None if not set

        """
        return self["Component 3 Flow Rate"]

    @component_3_flow_rate.setter
    def component_3_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 3 Flow Rate`"""
        self["Component 3 Flow Rate"] = value

    @property
    def operation_3_type(self):
        """field `Operation 3 Type`

        Args:
            value (str): value for IDD Field `Operation 3 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_3_type` or None if not set

        """
        return self["Operation 3 Type"]

    @operation_3_type.setter
    def operation_3_type(self, value=None):
        """Corresponds to IDD field `Operation 3 Type`"""
        self["Operation 3 Type"] = value

    @property
    def equipment_4_object_type(self):
        """field `Equipment 4 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_4_object_type` or None if not set

        """
        return self["Equipment 4 Object Type"]

    @equipment_4_object_type.setter
    def equipment_4_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 4 Object Type`"""
        self["Equipment 4 Object Type"] = value

    @property
    def equipment_4_name(self):
        """field `Equipment 4 Name`

        Args:
            value (str): value for IDD Field `Equipment 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_4_name` or None if not set

        """
        return self["Equipment 4 Name"]

    @equipment_4_name.setter
    def equipment_4_name(self, value=None):
        """Corresponds to IDD field `Equipment 4 Name`"""
        self["Equipment 4 Name"] = value

    @property
    def demand_calculation_4_node_name(self):
        """field `Demand Calculation 4 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 4 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_4_node_name` or None if not set

        """
        return self["Demand Calculation 4 Node Name"]

    @demand_calculation_4_node_name.setter
    def demand_calculation_4_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 4 Node Name`"""
        self["Demand Calculation 4 Node Name"] = value

    @property
    def setpoint_4_node_name(self):
        """field `Setpoint 4 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 4 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_4_node_name` or None if not set

        """
        return self["Setpoint 4 Node Name"]

    @setpoint_4_node_name.setter
    def setpoint_4_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 4 Node Name`"""
        self["Setpoint 4 Node Name"] = value

    @property
    def component_4_flow_rate(self):
        """field `Component 4 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 4 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_4_flow_rate` or None if not set

        """
        return self["Component 4 Flow Rate"]

    @component_4_flow_rate.setter
    def component_4_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 4 Flow Rate`"""
        self["Component 4 Flow Rate"] = value

    @property
    def operation_4_type(self):
        """field `Operation 4 Type`

        Args:
            value (str): value for IDD Field `Operation 4 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_4_type` or None if not set

        """
        return self["Operation 4 Type"]

    @operation_4_type.setter
    def operation_4_type(self, value=None):
        """Corresponds to IDD field `Operation 4 Type`"""
        self["Operation 4 Type"] = value

    @property
    def equipment_5_object_type(self):
        """field `Equipment 5 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_5_object_type` or None if not set

        """
        return self["Equipment 5 Object Type"]

    @equipment_5_object_type.setter
    def equipment_5_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 5 Object Type`"""
        self["Equipment 5 Object Type"] = value

    @property
    def equipment_5_name(self):
        """field `Equipment 5 Name`

        Args:
            value (str): value for IDD Field `Equipment 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_5_name` or None if not set

        """
        return self["Equipment 5 Name"]

    @equipment_5_name.setter
    def equipment_5_name(self, value=None):
        """Corresponds to IDD field `Equipment 5 Name`"""
        self["Equipment 5 Name"] = value

    @property
    def demand_calculation_5_node_name(self):
        """field `Demand Calculation 5 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 5 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_5_node_name` or None if not set

        """
        return self["Demand Calculation 5 Node Name"]

    @demand_calculation_5_node_name.setter
    def demand_calculation_5_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 5 Node Name`"""
        self["Demand Calculation 5 Node Name"] = value

    @property
    def setpoint_5_node_name(self):
        """field `Setpoint 5 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 5 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_5_node_name` or None if not set

        """
        return self["Setpoint 5 Node Name"]

    @setpoint_5_node_name.setter
    def setpoint_5_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 5 Node Name`"""
        self["Setpoint 5 Node Name"] = value

    @property
    def component_5_flow_rate(self):
        """field `Component 5 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 5 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_5_flow_rate` or None if not set

        """
        return self["Component 5 Flow Rate"]

    @component_5_flow_rate.setter
    def component_5_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 5 Flow Rate`"""
        self["Component 5 Flow Rate"] = value

    @property
    def operation_5_type(self):
        """field `Operation 5 Type`

        Args:
            value (str): value for IDD Field `Operation 5 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_5_type` or None if not set

        """
        return self["Operation 5 Type"]

    @operation_5_type.setter
    def operation_5_type(self, value=None):
        """Corresponds to IDD field `Operation 5 Type`"""
        self["Operation 5 Type"] = value

    @property
    def equipment_6_object_type(self):
        """field `Equipment 6 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_6_object_type` or None if not set

        """
        return self["Equipment 6 Object Type"]

    @equipment_6_object_type.setter
    def equipment_6_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 6 Object Type`"""
        self["Equipment 6 Object Type"] = value

    @property
    def equipment_6_name(self):
        """field `Equipment 6 Name`

        Args:
            value (str): value for IDD Field `Equipment 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_6_name` or None if not set

        """
        return self["Equipment 6 Name"]

    @equipment_6_name.setter
    def equipment_6_name(self, value=None):
        """Corresponds to IDD field `Equipment 6 Name`"""
        self["Equipment 6 Name"] = value

    @property
    def demand_calculation_6_node_name(self):
        """field `Demand Calculation 6 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 6 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_6_node_name` or None if not set

        """
        return self["Demand Calculation 6 Node Name"]

    @demand_calculation_6_node_name.setter
    def demand_calculation_6_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 6 Node Name`"""
        self["Demand Calculation 6 Node Name"] = value

    @property
    def setpoint_6_node_name(self):
        """field `Setpoint 6 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 6 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_6_node_name` or None if not set

        """
        return self["Setpoint 6 Node Name"]

    @setpoint_6_node_name.setter
    def setpoint_6_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 6 Node Name`"""
        self["Setpoint 6 Node Name"] = value

    @property
    def component_6_flow_rate(self):
        """field `Component 6 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 6 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_6_flow_rate` or None if not set

        """
        return self["Component 6 Flow Rate"]

    @component_6_flow_rate.setter
    def component_6_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 6 Flow Rate`"""
        self["Component 6 Flow Rate"] = value

    @property
    def operation_6_type(self):
        """field `Operation 6 Type`

        Args:
            value (str): value for IDD Field `Operation 6 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_6_type` or None if not set

        """
        return self["Operation 6 Type"]

    @operation_6_type.setter
    def operation_6_type(self, value=None):
        """Corresponds to IDD field `Operation 6 Type`"""
        self["Operation 6 Type"] = value

    @property
    def equipment_7_object_type(self):
        """field `Equipment 7 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_7_object_type` or None if not set

        """
        return self["Equipment 7 Object Type"]

    @equipment_7_object_type.setter
    def equipment_7_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 7 Object Type`"""
        self["Equipment 7 Object Type"] = value

    @property
    def equipment_7_name(self):
        """field `Equipment 7 Name`

        Args:
            value (str): value for IDD Field `Equipment 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_7_name` or None if not set

        """
        return self["Equipment 7 Name"]

    @equipment_7_name.setter
    def equipment_7_name(self, value=None):
        """Corresponds to IDD field `Equipment 7 Name`"""
        self["Equipment 7 Name"] = value

    @property
    def demand_calculation_7_node_name(self):
        """field `Demand Calculation 7 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 7 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_7_node_name` or None if not set

        """
        return self["Demand Calculation 7 Node Name"]

    @demand_calculation_7_node_name.setter
    def demand_calculation_7_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 7 Node Name`"""
        self["Demand Calculation 7 Node Name"] = value

    @property
    def setpoint_7_node_name(self):
        """field `Setpoint 7 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 7 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_7_node_name` or None if not set

        """
        return self["Setpoint 7 Node Name"]

    @setpoint_7_node_name.setter
    def setpoint_7_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 7 Node Name`"""
        self["Setpoint 7 Node Name"] = value

    @property
    def component_7_flow_rate(self):
        """field `Component 7 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 7 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_7_flow_rate` or None if not set

        """
        return self["Component 7 Flow Rate"]

    @component_7_flow_rate.setter
    def component_7_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 7 Flow Rate`"""
        self["Component 7 Flow Rate"] = value

    @property
    def operation_7_type(self):
        """field `Operation 7 Type`

        Args:
            value (str): value for IDD Field `Operation 7 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_7_type` or None if not set

        """
        return self["Operation 7 Type"]

    @operation_7_type.setter
    def operation_7_type(self, value=None):
        """Corresponds to IDD field `Operation 7 Type`"""
        self["Operation 7 Type"] = value

    @property
    def equipment_8_object_type(self):
        """field `Equipment 8 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_8_object_type` or None if not set

        """
        return self["Equipment 8 Object Type"]

    @equipment_8_object_type.setter
    def equipment_8_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 8 Object Type`"""
        self["Equipment 8 Object Type"] = value

    @property
    def equipment_8_name(self):
        """field `Equipment 8 Name`

        Args:
            value (str): value for IDD Field `Equipment 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_8_name` or None if not set

        """
        return self["Equipment 8 Name"]

    @equipment_8_name.setter
    def equipment_8_name(self, value=None):
        """Corresponds to IDD field `Equipment 8 Name`"""
        self["Equipment 8 Name"] = value

    @property
    def demand_calculation_8_node_name(self):
        """field `Demand Calculation 8 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 8 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_8_node_name` or None if not set

        """
        return self["Demand Calculation 8 Node Name"]

    @demand_calculation_8_node_name.setter
    def demand_calculation_8_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 8 Node Name`"""
        self["Demand Calculation 8 Node Name"] = value

    @property
    def setpoint_8_node_name(self):
        """field `Setpoint 8 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 8 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_8_node_name` or None if not set

        """
        return self["Setpoint 8 Node Name"]

    @setpoint_8_node_name.setter
    def setpoint_8_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 8 Node Name`"""
        self["Setpoint 8 Node Name"] = value

    @property
    def component_8_flow_rate(self):
        """field `Component 8 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 8 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_8_flow_rate` or None if not set

        """
        return self["Component 8 Flow Rate"]

    @component_8_flow_rate.setter
    def component_8_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 8 Flow Rate`"""
        self["Component 8 Flow Rate"] = value

    @property
    def operation_8_type(self):
        """field `Operation 8 Type`

        Args:
            value (str): value for IDD Field `Operation 8 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_8_type` or None if not set

        """
        return self["Operation 8 Type"]

    @operation_8_type.setter
    def operation_8_type(self, value=None):
        """Corresponds to IDD field `Operation 8 Type`"""
        self["Operation 8 Type"] = value

    @property
    def equipment_9_object_type(self):
        """field `Equipment 9 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 9 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_9_object_type` or None if not set

        """
        return self["Equipment 9 Object Type"]

    @equipment_9_object_type.setter
    def equipment_9_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 9 Object Type`"""
        self["Equipment 9 Object Type"] = value

    @property
    def equipment_9_name(self):
        """field `Equipment 9 Name`

        Args:
            value (str): value for IDD Field `Equipment 9 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_9_name` or None if not set

        """
        return self["Equipment 9 Name"]

    @equipment_9_name.setter
    def equipment_9_name(self, value=None):
        """Corresponds to IDD field `Equipment 9 Name`"""
        self["Equipment 9 Name"] = value

    @property
    def demand_calculation_9_node_name(self):
        """field `Demand Calculation 9 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 9 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_9_node_name` or None if not set

        """
        return self["Demand Calculation 9 Node Name"]

    @demand_calculation_9_node_name.setter
    def demand_calculation_9_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 9 Node Name`"""
        self["Demand Calculation 9 Node Name"] = value

    @property
    def setpoint_9_node_name(self):
        """field `Setpoint 9 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 9 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_9_node_name` or None if not set

        """
        return self["Setpoint 9 Node Name"]

    @setpoint_9_node_name.setter
    def setpoint_9_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 9 Node Name`"""
        self["Setpoint 9 Node Name"] = value

    @property
    def component_9_flow_rate(self):
        """field `Component 9 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 9 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_9_flow_rate` or None if not set

        """
        return self["Component 9 Flow Rate"]

    @component_9_flow_rate.setter
    def component_9_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 9 Flow Rate`"""
        self["Component 9 Flow Rate"] = value

    @property
    def operation_9_type(self):
        """field `Operation 9 Type`

        Args:
            value (str): value for IDD Field `Operation 9 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_9_type` or None if not set

        """
        return self["Operation 9 Type"]

    @operation_9_type.setter
    def operation_9_type(self, value=None):
        """Corresponds to IDD field `Operation 9 Type`"""
        self["Operation 9 Type"] = value

    @property
    def equipment_10_object_type(self):
        """field `Equipment 10 Object Type`

        Args:
            value (str): value for IDD Field `Equipment 10 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_10_object_type` or None if not set

        """
        return self["Equipment 10 Object Type"]

    @equipment_10_object_type.setter
    def equipment_10_object_type(self, value=None):
        """Corresponds to IDD field `Equipment 10 Object Type`"""
        self["Equipment 10 Object Type"] = value

    @property
    def equipment_10_name(self):
        """field `Equipment 10 Name`

        Args:
            value (str): value for IDD Field `Equipment 10 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `equipment_10_name` or None if not set

        """
        return self["Equipment 10 Name"]

    @equipment_10_name.setter
    def equipment_10_name(self, value=None):
        """Corresponds to IDD field `Equipment 10 Name`"""
        self["Equipment 10 Name"] = value

    @property
    def demand_calculation_10_node_name(self):
        """field `Demand Calculation 10 Node Name`

        Args:
            value (str): value for IDD Field `Demand Calculation 10 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_calculation_10_node_name` or None if not set

        """
        return self["Demand Calculation 10 Node Name"]

    @demand_calculation_10_node_name.setter
    def demand_calculation_10_node_name(self, value=None):
        """Corresponds to IDD field `Demand Calculation 10 Node Name`"""
        self["Demand Calculation 10 Node Name"] = value

    @property
    def setpoint_10_node_name(self):
        """field `Setpoint 10 Node Name`

        Args:
            value (str): value for IDD Field `Setpoint 10 Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `setpoint_10_node_name` or None if not set

        """
        return self["Setpoint 10 Node Name"]

    @setpoint_10_node_name.setter
    def setpoint_10_node_name(self, value=None):
        """Corresponds to IDD field `Setpoint 10 Node Name`"""
        self["Setpoint 10 Node Name"] = value

    @property
    def component_10_flow_rate(self):
        """field `Component 10 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 10 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_10_flow_rate` or None if not set

        """
        return self["Component 10 Flow Rate"]

    @component_10_flow_rate.setter
    def component_10_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 10 Flow Rate`"""
        self["Component 10 Flow Rate"] = value

    @property
    def operation_10_type(self):
        """field `Operation 10 Type`

        Args:
            value (str): value for IDD Field `Operation 10 Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `operation_10_type` or None if not set

        """
        return self["Operation 10 Type"]

    @operation_10_type.setter
    def operation_10_type(self, value=None):
        """Corresponds to IDD field `Operation 10 Type`"""
        self["Operation 10 Type"] = value




class PlantEquipmentOperationThermalEnergyStorage(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:ThermalEnergyStorage`
        Plant equipment operation scheme for simpler input to control thermal (ice)
        energy storage systems.  It replaces a host of setpoint managers with simple,
        single input values.  For more complex controls, use the ComponentSetpoint
        scheme.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'on-peak schedule',
                                       {'name': u'On-Peak Schedule',
                                        'pyname': u'onpeak_schedule',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'charging availability schedule',
                                       {'name': u'Charging Availability Schedule',
                                        'pyname': u'charging_availability_schedule',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'non-charging chilled water temperature',
                                       {'name': u'Non-Charging Chilled Water Temperature',
                                        'pyname': u'noncharging_chilled_water_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'charging chilled water temperature',
                                       {'name': u'Charging Chilled Water Temperature',
                                        'pyname': u'charging_chilled_water_temperature',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'component 1 object type',
                                       {'name': u'Component 1 Object Type',
                                        'pyname': u'component_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 1 name',
                                       {'name': u'Component 1 Name',
                                        'pyname': u'component_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 1 demand calculation node name',
                                       {'name': u'Component 1 Demand Calculation Node Name',
                                        'pyname': u'component_1_demand_calculation_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 1 setpoint node name',
                                       {'name': u'Component 1 Setpoint Node Name',
                                        'pyname': u'component_1_setpoint_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 1 flow rate',
                                       {'name': u'Component 1 Flow Rate',
                                        'pyname': u'component_1_flow_rate',
                                        'required-field': True,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 1 operation type',
                                       {'name': u'Component 1 Operation Type',
                                        'pyname': u'component_1_operation_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 2 object type',
                                       {'name': u'Component 2 Object Type',
                                        'pyname': u'component_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 2 name',
                                       {'name': u'Component 2 Name',
                                        'pyname': u'component_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 2 demand calculation node name',
                                       {'name': u'Component 2 Demand Calculation Node Name',
                                        'pyname': u'component_2_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 2 setpoint node name',
                                       {'name': u'Component 2 Setpoint Node Name',
                                        'pyname': u'component_2_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 2 flow rate',
                                       {'name': u'Component 2 Flow Rate',
                                        'pyname': u'component_2_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 2 operation type',
                                       {'name': u'Component 2 Operation Type',
                                        'pyname': u'component_2_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 3 object type',
                                       {'name': u'Component 3 Object Type',
                                        'pyname': u'component_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 3 name',
                                       {'name': u'Component 3 Name',
                                        'pyname': u'component_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 3 demand calculation node name',
                                       {'name': u'Component 3 Demand Calculation Node Name',
                                        'pyname': u'component_3_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 3 setpoint node name',
                                       {'name': u'Component 3 Setpoint Node Name',
                                        'pyname': u'component_3_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 3 flow rate',
                                       {'name': u'Component 3 Flow Rate',
                                        'pyname': u'component_3_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 3 operation type',
                                       {'name': u'Component 3 Operation Type',
                                        'pyname': u'component_3_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 4 object type',
                                       {'name': u'Component 4 Object Type',
                                        'pyname': u'component_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 4 name',
                                       {'name': u'Component 4 Name',
                                        'pyname': u'component_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 4 demand calculation node name',
                                       {'name': u'Component 4 Demand Calculation Node Name',
                                        'pyname': u'component_4_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 4 setpoint node name',
                                       {'name': u'Component 4 Setpoint Node Name',
                                        'pyname': u'component_4_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 4 flow rate',
                                       {'name': u'Component 4 Flow Rate',
                                        'pyname': u'component_4_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 4 operation type',
                                       {'name': u'Component 4 Operation Type',
                                        'pyname': u'component_4_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 5 object type',
                                       {'name': u'Component 5 Object Type',
                                        'pyname': u'component_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 5 name',
                                       {'name': u'Component 5 Name',
                                        'pyname': u'component_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 5 demand calculation node name',
                                       {'name': u'Component 5 Demand Calculation Node Name',
                                        'pyname': u'component_5_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 5 setpoint node name',
                                       {'name': u'Component 5 Setpoint Node Name',
                                        'pyname': u'component_5_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 5 flow rate',
                                       {'name': u'Component 5 Flow Rate',
                                        'pyname': u'component_5_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 5 operation type',
                                       {'name': u'Component 5 Operation Type',
                                        'pyname': u'component_5_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 6 object type',
                                       {'name': u'Component 6 Object Type',
                                        'pyname': u'component_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 6 name',
                                       {'name': u'Component 6 Name',
                                        'pyname': u'component_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 6 demand calculation node name',
                                       {'name': u'Component 6 Demand Calculation Node Name',
                                        'pyname': u'component_6_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 6 setpoint node name',
                                       {'name': u'Component 6 Setpoint Node Name',
                                        'pyname': u'component_6_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 6 flow rate',
                                       {'name': u'Component 6 Flow Rate',
                                        'pyname': u'component_6_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 6 operation type',
                                       {'name': u'Component 6 Operation Type',
                                        'pyname': u'component_6_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 7 object type',
                                       {'name': u'Component 7 Object Type',
                                        'pyname': u'component_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 7 name',
                                       {'name': u'Component 7 Name',
                                        'pyname': u'component_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 7 demand calculation node name',
                                       {'name': u'Component 7 Demand Calculation Node Name',
                                        'pyname': u'component_7_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 7 setpoint node name',
                                       {'name': u'Component 7 Setpoint Node Name',
                                        'pyname': u'component_7_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 7 flow rate',
                                       {'name': u'Component 7 Flow Rate',
                                        'pyname': u'component_7_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 7 operation type',
                                       {'name': u'Component 7 Operation Type',
                                        'pyname': u'component_7_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 8 object type',
                                       {'name': u'Component 8 Object Type',
                                        'pyname': u'component_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 8 name',
                                       {'name': u'Component 8 Name',
                                        'pyname': u'component_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 8 demand calculation node name',
                                       {'name': u'Component 8 Demand Calculation Node Name',
                                        'pyname': u'component_8_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 8 setpoint node name',
                                       {'name': u'Component 8 Setpoint Node Name',
                                        'pyname': u'component_8_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 8 flow rate',
                                       {'name': u'Component 8 Flow Rate',
                                        'pyname': u'component_8_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 8 operation type',
                                       {'name': u'Component 8 Operation Type',
                                        'pyname': u'component_8_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 9 object type',
                                       {'name': u'Component 9 Object Type',
                                        'pyname': u'component_9_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 9 name',
                                       {'name': u'Component 9 Name',
                                        'pyname': u'component_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 9 demand calculation node name',
                                       {'name': u'Component 9 Demand Calculation Node Name',
                                        'pyname': u'component_9_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 9 setpoint node name',
                                       {'name': u'Component 9 Setpoint Node Name',
                                        'pyname': u'component_9_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 9 flow rate',
                                       {'name': u'Component 9 Flow Rate',
                                        'pyname': u'component_9_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 9 operation type',
                                       {'name': u'Component 9 Operation Type',
                                        'pyname': u'component_9_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 10 object type',
                                       {'name': u'Component 10 Object Type',
                                        'pyname': u'component_10_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ThermalStorage:Ice:Simple',
                                                            u'ThermalStorage:Ice:Detailed',
                                                            u'Chiller:Electric:EIR',
                                                            u'Chiller:Electric:ReformulatedEIR',
                                                            u'Chiller:Electric',
                                                            u'Chiller:Absorption:Indirect',
                                                            u'Chiller:Absorption',
                                                            u'Chiller:ConstantCOP',
                                                            u'Chiller:EngineDriven',
                                                            u'Chiller:CombustionTurbine'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 10 name',
                                       {'name': u'Component 10 Name',
                                        'pyname': u'component_10_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'component 10 demand calculation node name',
                                       {'name': u'Component 10 Demand Calculation Node Name',
                                        'pyname': u'component_10_demand_calculation_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 10 setpoint node name',
                                       {'name': u'Component 10 Setpoint Node Name',
                                        'pyname': u'component_10_setpoint_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'component 10 flow rate',
                                       {'name': u'Component 10 Flow Rate',
                                        'pyname': u'component_10_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'component 10 operation type',
                                       {'name': u'Component 10 Operation Type',
                                        'pyname': u'component_10_operation_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Heating',
                                                            u'Cooling',
                                                            u'Dual'],
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 7,
               'name': u'PlantEquipmentOperation:ThermalEnergyStorage',
               'pyname': u'PlantEquipmentOperationThermalEnergyStorage',
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
    def onpeak_schedule(self):
        """field `On-Peak Schedule`


        Args:
            value (str): value for IDD Field `On-Peak Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `onpeak_schedule` or None if not set
        """
        return self["On-Peak Schedule"]

    @onpeak_schedule.setter
    def onpeak_schedule(self, value=None):
        """  Corresponds to IDD field `On-Peak Schedule`

        """
        self["On-Peak Schedule"] = value

    @property
    def charging_availability_schedule(self):
        """field `Charging Availability Schedule`

        Args:
            value (str): value for IDD Field `Charging Availability Schedule`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `charging_availability_schedule` or None if not set

        """
        return self["Charging Availability Schedule"]

    @charging_availability_schedule.setter
    def charging_availability_schedule(self, value=None):
        """Corresponds to IDD field `Charging Availability Schedule`"""
        self["Charging Availability Schedule"] = value

    @property
    def noncharging_chilled_water_temperature(self):
        """field `Non-Charging Chilled Water Temperature`

        |  Single temperature for chiller outlet when not in cooling season
        |  or during on-peak cooling (discharge)
        |  Units: C

        Args:
            value (float): value for IDD Field `Non-Charging Chilled Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `noncharging_chilled_water_temperature` or None if not set
        """
        return self["Non-Charging Chilled Water Temperature"]

    @noncharging_chilled_water_temperature.setter
    def noncharging_chilled_water_temperature(self, value=None):
        """  Corresponds to IDD field `Non-Charging Chilled Water Temperature`

        """
        self["Non-Charging Chilled Water Temperature"] = value

    @property
    def charging_chilled_water_temperature(self):
        """field `Charging Chilled Water Temperature`

        |  Single temperature for chiller outlet when off-peak during cooling
        |  season (charging)
        |  Units: C

        Args:
            value (float): value for IDD Field `Charging Chilled Water Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `charging_chilled_water_temperature` or None if not set

        """
        return self["Charging Chilled Water Temperature"]

    @charging_chilled_water_temperature.setter
    def charging_chilled_water_temperature(self, value=None):
        """Corresponds to IDD field `Charging Chilled Water Temperature`"""
        self["Charging Chilled Water Temperature"] = value

    @property
    def component_1_object_type(self):
        """field `Component 1 Object Type`

        |  This field is the type of object and should either be a chiller or some
        |  ice storage equipment.

        Args:
            value (str): value for IDD Field `Component 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_object_type` or None if not set

        """
        return self["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """Corresponds to IDD field `Component 1 Object Type`"""
        self["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """field `Component 1 Name`

        |  This field is the name of either the chiller or ice storage equipment
        |  on the loop.

        Args:
            value (str): value for IDD Field `Component 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_name` or None if not set

        """
        return self["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """Corresponds to IDD field `Component 1 Name`"""
        self["Component 1 Name"] = value

    @property
    def component_1_demand_calculation_node_name(self):
        """field `Component 1 Demand Calculation Node Name`

        |  This field is the name of the inlet node for the component defined in
        |  the two previous input fields.

        Args:
            value (str): value for IDD Field `Component 1 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_demand_calculation_node_name` or None if not set

        """
        return self["Component 1 Demand Calculation Node Name"]

    @component_1_demand_calculation_node_name.setter
    def component_1_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 1 Demand Calculation Node
        Name`"""
        self["Component 1 Demand Calculation Node Name"] = value

    @property
    def component_1_setpoint_node_name(self):
        """field `Component 1 Setpoint Node Name`

        |  This field is the name of the outlet node for the component listed above.

        Args:
            value (str): value for IDD Field `Component 1 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_setpoint_node_name` or None if not set

        """
        return self["Component 1 Setpoint Node Name"]

    @component_1_setpoint_node_name.setter
    def component_1_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 1 Setpoint Node Name`"""
        self["Component 1 Setpoint Node Name"] = value

    @property
    def component_1_flow_rate(self):
        """field `Component 1 Flow Rate`

        |  This field is the flow rate for the component listed above.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 1 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_1_flow_rate` or None if not set

        """
        return self["Component 1 Flow Rate"]

    @component_1_flow_rate.setter
    def component_1_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 1 Flow Rate`"""
        self["Component 1 Flow Rate"] = value

    @property
    def component_1_operation_type(self):
        """field `Component 1 Operation Type`

        |  This field is the operation type for the component listed above.  For this
        |  plant equipment operation scheme, "Cooling" should be selected for chiller
        |  equipment while ice storage equipment should be defined as "Dual".

        Args:
            value (str): value for IDD Field `Component 1 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_1_operation_type` or None if not set

        """
        return self["Component 1 Operation Type"]

    @component_1_operation_type.setter
    def component_1_operation_type(self, value=None):
        """Corresponds to IDD field `Component 1 Operation Type`"""
        self["Component 1 Operation Type"] = value

    @property
    def component_2_object_type(self):
        """field `Component 2 Object Type`

        Args:
            value (str): value for IDD Field `Component 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_object_type` or None if not set

        """
        return self["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """Corresponds to IDD field `Component 2 Object Type`"""
        self["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """field `Component 2 Name`

        Args:
            value (str): value for IDD Field `Component 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_name` or None if not set

        """
        return self["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """Corresponds to IDD field `Component 2 Name`"""
        self["Component 2 Name"] = value

    @property
    def component_2_demand_calculation_node_name(self):
        """field `Component 2 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 2 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_demand_calculation_node_name` or None if not set

        """
        return self["Component 2 Demand Calculation Node Name"]

    @component_2_demand_calculation_node_name.setter
    def component_2_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 2 Demand Calculation Node
        Name`"""
        self["Component 2 Demand Calculation Node Name"] = value

    @property
    def component_2_setpoint_node_name(self):
        """field `Component 2 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 2 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_setpoint_node_name` or None if not set

        """
        return self["Component 2 Setpoint Node Name"]

    @component_2_setpoint_node_name.setter
    def component_2_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 2 Setpoint Node Name`"""
        self["Component 2 Setpoint Node Name"] = value

    @property
    def component_2_flow_rate(self):
        """field `Component 2 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 2 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_2_flow_rate` or None if not set

        """
        return self["Component 2 Flow Rate"]

    @component_2_flow_rate.setter
    def component_2_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 2 Flow Rate`"""
        self["Component 2 Flow Rate"] = value

    @property
    def component_2_operation_type(self):
        """field `Component 2 Operation Type`

        Args:
            value (str): value for IDD Field `Component 2 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_2_operation_type` or None if not set

        """
        return self["Component 2 Operation Type"]

    @component_2_operation_type.setter
    def component_2_operation_type(self, value=None):
        """Corresponds to IDD field `Component 2 Operation Type`"""
        self["Component 2 Operation Type"] = value

    @property
    def component_3_object_type(self):
        """field `Component 3 Object Type`

        Args:
            value (str): value for IDD Field `Component 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_object_type` or None if not set

        """
        return self["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """Corresponds to IDD field `Component 3 Object Type`"""
        self["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """field `Component 3 Name`

        Args:
            value (str): value for IDD Field `Component 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_name` or None if not set

        """
        return self["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """Corresponds to IDD field `Component 3 Name`"""
        self["Component 3 Name"] = value

    @property
    def component_3_demand_calculation_node_name(self):
        """field `Component 3 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 3 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_demand_calculation_node_name` or None if not set

        """
        return self["Component 3 Demand Calculation Node Name"]

    @component_3_demand_calculation_node_name.setter
    def component_3_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 3 Demand Calculation Node
        Name`"""
        self["Component 3 Demand Calculation Node Name"] = value

    @property
    def component_3_setpoint_node_name(self):
        """field `Component 3 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 3 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_setpoint_node_name` or None if not set

        """
        return self["Component 3 Setpoint Node Name"]

    @component_3_setpoint_node_name.setter
    def component_3_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 3 Setpoint Node Name`"""
        self["Component 3 Setpoint Node Name"] = value

    @property
    def component_3_flow_rate(self):
        """field `Component 3 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 3 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_3_flow_rate` or None if not set

        """
        return self["Component 3 Flow Rate"]

    @component_3_flow_rate.setter
    def component_3_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 3 Flow Rate`"""
        self["Component 3 Flow Rate"] = value

    @property
    def component_3_operation_type(self):
        """field `Component 3 Operation Type`

        Args:
            value (str): value for IDD Field `Component 3 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_3_operation_type` or None if not set

        """
        return self["Component 3 Operation Type"]

    @component_3_operation_type.setter
    def component_3_operation_type(self, value=None):
        """Corresponds to IDD field `Component 3 Operation Type`"""
        self["Component 3 Operation Type"] = value

    @property
    def component_4_object_type(self):
        """field `Component 4 Object Type`

        Args:
            value (str): value for IDD Field `Component 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_object_type` or None if not set

        """
        return self["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """Corresponds to IDD field `Component 4 Object Type`"""
        self["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """field `Component 4 Name`

        Args:
            value (str): value for IDD Field `Component 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_name` or None if not set

        """
        return self["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """Corresponds to IDD field `Component 4 Name`"""
        self["Component 4 Name"] = value

    @property
    def component_4_demand_calculation_node_name(self):
        """field `Component 4 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 4 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_demand_calculation_node_name` or None if not set

        """
        return self["Component 4 Demand Calculation Node Name"]

    @component_4_demand_calculation_node_name.setter
    def component_4_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 4 Demand Calculation Node
        Name`"""
        self["Component 4 Demand Calculation Node Name"] = value

    @property
    def component_4_setpoint_node_name(self):
        """field `Component 4 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 4 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_setpoint_node_name` or None if not set

        """
        return self["Component 4 Setpoint Node Name"]

    @component_4_setpoint_node_name.setter
    def component_4_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 4 Setpoint Node Name`"""
        self["Component 4 Setpoint Node Name"] = value

    @property
    def component_4_flow_rate(self):
        """field `Component 4 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 4 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_4_flow_rate` or None if not set

        """
        return self["Component 4 Flow Rate"]

    @component_4_flow_rate.setter
    def component_4_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 4 Flow Rate`"""
        self["Component 4 Flow Rate"] = value

    @property
    def component_4_operation_type(self):
        """field `Component 4 Operation Type`

        Args:
            value (str): value for IDD Field `Component 4 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_4_operation_type` or None if not set

        """
        return self["Component 4 Operation Type"]

    @component_4_operation_type.setter
    def component_4_operation_type(self, value=None):
        """Corresponds to IDD field `Component 4 Operation Type`"""
        self["Component 4 Operation Type"] = value

    @property
    def component_5_object_type(self):
        """field `Component 5 Object Type`

        Args:
            value (str): value for IDD Field `Component 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_object_type` or None if not set

        """
        return self["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """Corresponds to IDD field `Component 5 Object Type`"""
        self["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """field `Component 5 Name`

        Args:
            value (str): value for IDD Field `Component 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_name` or None if not set

        """
        return self["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """Corresponds to IDD field `Component 5 Name`"""
        self["Component 5 Name"] = value

    @property
    def component_5_demand_calculation_node_name(self):
        """field `Component 5 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 5 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_demand_calculation_node_name` or None if not set

        """
        return self["Component 5 Demand Calculation Node Name"]

    @component_5_demand_calculation_node_name.setter
    def component_5_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 5 Demand Calculation Node
        Name`"""
        self["Component 5 Demand Calculation Node Name"] = value

    @property
    def component_5_setpoint_node_name(self):
        """field `Component 5 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 5 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_setpoint_node_name` or None if not set

        """
        return self["Component 5 Setpoint Node Name"]

    @component_5_setpoint_node_name.setter
    def component_5_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 5 Setpoint Node Name`"""
        self["Component 5 Setpoint Node Name"] = value

    @property
    def component_5_flow_rate(self):
        """field `Component 5 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 5 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_5_flow_rate` or None if not set

        """
        return self["Component 5 Flow Rate"]

    @component_5_flow_rate.setter
    def component_5_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 5 Flow Rate`"""
        self["Component 5 Flow Rate"] = value

    @property
    def component_5_operation_type(self):
        """field `Component 5 Operation Type`

        Args:
            value (str): value for IDD Field `Component 5 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_5_operation_type` or None if not set

        """
        return self["Component 5 Operation Type"]

    @component_5_operation_type.setter
    def component_5_operation_type(self, value=None):
        """Corresponds to IDD field `Component 5 Operation Type`"""
        self["Component 5 Operation Type"] = value

    @property
    def component_6_object_type(self):
        """field `Component 6 Object Type`

        Args:
            value (str): value for IDD Field `Component 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_object_type` or None if not set

        """
        return self["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """Corresponds to IDD field `Component 6 Object Type`"""
        self["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """field `Component 6 Name`

        Args:
            value (str): value for IDD Field `Component 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_name` or None if not set

        """
        return self["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """Corresponds to IDD field `Component 6 Name`"""
        self["Component 6 Name"] = value

    @property
    def component_6_demand_calculation_node_name(self):
        """field `Component 6 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 6 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_demand_calculation_node_name` or None if not set

        """
        return self["Component 6 Demand Calculation Node Name"]

    @component_6_demand_calculation_node_name.setter
    def component_6_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 6 Demand Calculation Node
        Name`"""
        self["Component 6 Demand Calculation Node Name"] = value

    @property
    def component_6_setpoint_node_name(self):
        """field `Component 6 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 6 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_setpoint_node_name` or None if not set

        """
        return self["Component 6 Setpoint Node Name"]

    @component_6_setpoint_node_name.setter
    def component_6_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 6 Setpoint Node Name`"""
        self["Component 6 Setpoint Node Name"] = value

    @property
    def component_6_flow_rate(self):
        """field `Component 6 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 6 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_6_flow_rate` or None if not set

        """
        return self["Component 6 Flow Rate"]

    @component_6_flow_rate.setter
    def component_6_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 6 Flow Rate`"""
        self["Component 6 Flow Rate"] = value

    @property
    def component_6_operation_type(self):
        """field `Component 6 Operation Type`

        Args:
            value (str): value for IDD Field `Component 6 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_6_operation_type` or None if not set

        """
        return self["Component 6 Operation Type"]

    @component_6_operation_type.setter
    def component_6_operation_type(self, value=None):
        """Corresponds to IDD field `Component 6 Operation Type`"""
        self["Component 6 Operation Type"] = value

    @property
    def component_7_object_type(self):
        """field `Component 7 Object Type`

        Args:
            value (str): value for IDD Field `Component 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_object_type` or None if not set

        """
        return self["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """Corresponds to IDD field `Component 7 Object Type`"""
        self["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """field `Component 7 Name`

        Args:
            value (str): value for IDD Field `Component 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_name` or None if not set

        """
        return self["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """Corresponds to IDD field `Component 7 Name`"""
        self["Component 7 Name"] = value

    @property
    def component_7_demand_calculation_node_name(self):
        """field `Component 7 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 7 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_demand_calculation_node_name` or None if not set

        """
        return self["Component 7 Demand Calculation Node Name"]

    @component_7_demand_calculation_node_name.setter
    def component_7_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 7 Demand Calculation Node
        Name`"""
        self["Component 7 Demand Calculation Node Name"] = value

    @property
    def component_7_setpoint_node_name(self):
        """field `Component 7 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 7 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_setpoint_node_name` or None if not set

        """
        return self["Component 7 Setpoint Node Name"]

    @component_7_setpoint_node_name.setter
    def component_7_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 7 Setpoint Node Name`"""
        self["Component 7 Setpoint Node Name"] = value

    @property
    def component_7_flow_rate(self):
        """field `Component 7 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 7 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_7_flow_rate` or None if not set

        """
        return self["Component 7 Flow Rate"]

    @component_7_flow_rate.setter
    def component_7_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 7 Flow Rate`"""
        self["Component 7 Flow Rate"] = value

    @property
    def component_7_operation_type(self):
        """field `Component 7 Operation Type`

        Args:
            value (str): value for IDD Field `Component 7 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_7_operation_type` or None if not set

        """
        return self["Component 7 Operation Type"]

    @component_7_operation_type.setter
    def component_7_operation_type(self, value=None):
        """Corresponds to IDD field `Component 7 Operation Type`"""
        self["Component 7 Operation Type"] = value

    @property
    def component_8_object_type(self):
        """field `Component 8 Object Type`

        Args:
            value (str): value for IDD Field `Component 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_object_type` or None if not set

        """
        return self["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """Corresponds to IDD field `Component 8 Object Type`"""
        self["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """field `Component 8 Name`

        Args:
            value (str): value for IDD Field `Component 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_name` or None if not set

        """
        return self["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """Corresponds to IDD field `Component 8 Name`"""
        self["Component 8 Name"] = value

    @property
    def component_8_demand_calculation_node_name(self):
        """field `Component 8 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 8 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_demand_calculation_node_name` or None if not set

        """
        return self["Component 8 Demand Calculation Node Name"]

    @component_8_demand_calculation_node_name.setter
    def component_8_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 8 Demand Calculation Node
        Name`"""
        self["Component 8 Demand Calculation Node Name"] = value

    @property
    def component_8_setpoint_node_name(self):
        """field `Component 8 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 8 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_setpoint_node_name` or None if not set

        """
        return self["Component 8 Setpoint Node Name"]

    @component_8_setpoint_node_name.setter
    def component_8_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 8 Setpoint Node Name`"""
        self["Component 8 Setpoint Node Name"] = value

    @property
    def component_8_flow_rate(self):
        """field `Component 8 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 8 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_8_flow_rate` or None if not set

        """
        return self["Component 8 Flow Rate"]

    @component_8_flow_rate.setter
    def component_8_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 8 Flow Rate`"""
        self["Component 8 Flow Rate"] = value

    @property
    def component_8_operation_type(self):
        """field `Component 8 Operation Type`

        Args:
            value (str): value for IDD Field `Component 8 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_8_operation_type` or None if not set

        """
        return self["Component 8 Operation Type"]

    @component_8_operation_type.setter
    def component_8_operation_type(self, value=None):
        """Corresponds to IDD field `Component 8 Operation Type`"""
        self["Component 8 Operation Type"] = value

    @property
    def component_9_object_type(self):
        """field `Component 9 Object Type`

        Args:
            value (str): value for IDD Field `Component 9 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_9_object_type` or None if not set

        """
        return self["Component 9 Object Type"]

    @component_9_object_type.setter
    def component_9_object_type(self, value=None):
        """Corresponds to IDD field `Component 9 Object Type`"""
        self["Component 9 Object Type"] = value

    @property
    def component_9_name(self):
        """field `Component 9 Name`

        Args:
            value (str): value for IDD Field `Component 9 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_9_name` or None if not set

        """
        return self["Component 9 Name"]

    @component_9_name.setter
    def component_9_name(self, value=None):
        """Corresponds to IDD field `Component 9 Name`"""
        self["Component 9 Name"] = value

    @property
    def component_9_demand_calculation_node_name(self):
        """field `Component 9 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 9 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_9_demand_calculation_node_name` or None if not set

        """
        return self["Component 9 Demand Calculation Node Name"]

    @component_9_demand_calculation_node_name.setter
    def component_9_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 9 Demand Calculation Node
        Name`"""
        self["Component 9 Demand Calculation Node Name"] = value

    @property
    def component_9_setpoint_node_name(self):
        """field `Component 9 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 9 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_9_setpoint_node_name` or None if not set

        """
        return self["Component 9 Setpoint Node Name"]

    @component_9_setpoint_node_name.setter
    def component_9_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 9 Setpoint Node Name`"""
        self["Component 9 Setpoint Node Name"] = value

    @property
    def component_9_flow_rate(self):
        """field `Component 9 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 9 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_9_flow_rate` or None if not set

        """
        return self["Component 9 Flow Rate"]

    @component_9_flow_rate.setter
    def component_9_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 9 Flow Rate`"""
        self["Component 9 Flow Rate"] = value

    @property
    def component_9_operation_type(self):
        """field `Component 9 Operation Type`

        Args:
            value (str): value for IDD Field `Component 9 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_9_operation_type` or None if not set

        """
        return self["Component 9 Operation Type"]

    @component_9_operation_type.setter
    def component_9_operation_type(self, value=None):
        """Corresponds to IDD field `Component 9 Operation Type`"""
        self["Component 9 Operation Type"] = value

    @property
    def component_10_object_type(self):
        """field `Component 10 Object Type`

        Args:
            value (str): value for IDD Field `Component 10 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_10_object_type` or None if not set

        """
        return self["Component 10 Object Type"]

    @component_10_object_type.setter
    def component_10_object_type(self, value=None):
        """Corresponds to IDD field `Component 10 Object Type`"""
        self["Component 10 Object Type"] = value

    @property
    def component_10_name(self):
        """field `Component 10 Name`

        Args:
            value (str): value for IDD Field `Component 10 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_10_name` or None if not set

        """
        return self["Component 10 Name"]

    @component_10_name.setter
    def component_10_name(self, value=None):
        """Corresponds to IDD field `Component 10 Name`"""
        self["Component 10 Name"] = value

    @property
    def component_10_demand_calculation_node_name(self):
        """field `Component 10 Demand Calculation Node Name`

        Args:
            value (str): value for IDD Field `Component 10 Demand Calculation Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_10_demand_calculation_node_name` or None if not set

        """
        return self["Component 10 Demand Calculation Node Name"]

    @component_10_demand_calculation_node_name.setter
    def component_10_demand_calculation_node_name(self, value=None):
        """Corresponds to IDD field `Component 10 Demand Calculation Node
        Name`"""
        self["Component 10 Demand Calculation Node Name"] = value

    @property
    def component_10_setpoint_node_name(self):
        """field `Component 10 Setpoint Node Name`

        Args:
            value (str): value for IDD Field `Component 10 Setpoint Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_10_setpoint_node_name` or None if not set

        """
        return self["Component 10 Setpoint Node Name"]

    @component_10_setpoint_node_name.setter
    def component_10_setpoint_node_name(self, value=None):
        """Corresponds to IDD field `Component 10 Setpoint Node Name`"""
        self["Component 10 Setpoint Node Name"] = value

    @property
    def component_10_flow_rate(self):
        """field `Component 10 Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Component 10 Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `component_10_flow_rate` or None if not set

        """
        return self["Component 10 Flow Rate"]

    @component_10_flow_rate.setter
    def component_10_flow_rate(self, value=None):
        """Corresponds to IDD field `Component 10 Flow Rate`"""
        self["Component 10 Flow Rate"] = value

    @property
    def component_10_operation_type(self):
        """field `Component 10 Operation Type`

        Args:
            value (str): value for IDD Field `Component 10 Operation Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `component_10_operation_type` or None if not set

        """
        return self["Component 10 Operation Type"]

    @component_10_operation_type.setter
    def component_10_operation_type(self, value=None):
        """Corresponds to IDD field `Component 10 Operation Type`"""
        self["Component 10 Operation Type"] = value




class PlantEquipmentOperationOutdoorDryBulbDifference(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDryBulbDifference`
        Plant equipment operation scheme for outdoor dry-bulb temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor dry-bulb temperature.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference temperature node name',
                                       {'name': u'Reference Temperature Node Name',
                                        'pyname': u'reference_temperature_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'dry-bulb temperature difference range 1 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 1 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_1_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 1 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 1 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_1_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 2 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 2 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_2_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 2 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 2 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_2_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 3 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 3 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_3_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 3 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 3 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_3_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 4 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 4 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_4_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 4 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 4 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_4_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 5 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 5 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_5_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 5 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 5 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_5_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 6 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 6 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_6_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 6 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 6 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_6_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 7 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 7 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_7_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 7 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 7 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_7_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 8 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 8 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_8_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 8 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 8 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_8_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 9 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 9 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_9_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 9 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 9 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_9_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dry-bulb temperature difference range 10 lower limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 10 Lower Limit',
                                        'pyname': u'drybulb_temperature_difference_range_10_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dry-bulb temperature difference range 10 upper limit',
                                       {'name': u'Dry-Bulb Temperature Difference Range 10 Upper Limit',
                                        'pyname': u'drybulb_temperature_difference_range_10_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 5,
               'name': u'PlantEquipmentOperation:OutdoorDryBulbDifference',
               'pyname': u'PlantEquipmentOperationOutdoorDryBulbDifference',
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
    def reference_temperature_node_name(self):
        """field `Reference Temperature Node Name`

        Args:
            value (str): value for IDD Field `Reference Temperature Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set

        """
        return self["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """Corresponds to IDD field `Reference Temperature Node Name`"""
        self["Reference Temperature Node Name"] = value

    @property
    def drybulb_temperature_difference_range_1_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 1 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 1 Lower Limit"]

    @drybulb_temperature_difference_range_1_lower_limit.setter
    def drybulb_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 1 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 1 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_1_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 1 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 1 Upper Limit"]

    @drybulb_temperature_difference_range_1_upper_limit.setter
    def drybulb_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 1 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_2_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 2 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 2 Lower Limit"]

    @drybulb_temperature_difference_range_2_lower_limit.setter
    def drybulb_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 2 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 2 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_2_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 2 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 2 Upper Limit"]

    @drybulb_temperature_difference_range_2_upper_limit.setter
    def drybulb_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 2 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_3_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 3 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 3 Lower Limit"]

    @drybulb_temperature_difference_range_3_lower_limit.setter
    def drybulb_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 3 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 3 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_3_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 3 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 3 Upper Limit"]

    @drybulb_temperature_difference_range_3_upper_limit.setter
    def drybulb_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 3 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_4_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 4 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 4 Lower Limit"]

    @drybulb_temperature_difference_range_4_lower_limit.setter
    def drybulb_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 4 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 4 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_4_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 4 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 4 Upper Limit"]

    @drybulb_temperature_difference_range_4_upper_limit.setter
    def drybulb_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 4 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_5_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 5 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 5 Lower Limit"]

    @drybulb_temperature_difference_range_5_lower_limit.setter
    def drybulb_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 5 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 5 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_5_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 5 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 5 Upper Limit"]

    @drybulb_temperature_difference_range_5_upper_limit.setter
    def drybulb_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 5 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_6_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 6 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 6 Lower Limit"]

    @drybulb_temperature_difference_range_6_lower_limit.setter
    def drybulb_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 6 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 6 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_6_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 6 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 6 Upper Limit"]

    @drybulb_temperature_difference_range_6_upper_limit.setter
    def drybulb_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 6 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_7_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 7 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 7 Lower Limit"]

    @drybulb_temperature_difference_range_7_lower_limit.setter
    def drybulb_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 7 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 7 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_7_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 7 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 7 Upper Limit"]

    @drybulb_temperature_difference_range_7_upper_limit.setter
    def drybulb_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 7 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_8_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 8 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 8 Lower Limit"]

    @drybulb_temperature_difference_range_8_lower_limit.setter
    def drybulb_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 8 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 8 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_8_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 8 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 8 Upper Limit"]

    @drybulb_temperature_difference_range_8_upper_limit.setter
    def drybulb_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 8 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_9_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 9 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 9 Lower Limit"]

    @drybulb_temperature_difference_range_9_lower_limit.setter
    def drybulb_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 9 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 9 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_9_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 9 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 9 Upper Limit"]

    @drybulb_temperature_difference_range_9_upper_limit.setter
    def drybulb_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 9 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def drybulb_temperature_difference_range_10_lower_limit(self):
        """field `Dry-Bulb Temperature Difference Range 10 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 10 Lower Limit"]

    @drybulb_temperature_difference_range_10_lower_limit.setter
    def drybulb_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 10 Lower Limit`

        """
        self["Dry-Bulb Temperature Difference Range 10 Lower Limit"] = value

    @property
    def drybulb_temperature_difference_range_10_upper_limit(self):
        """field `Dry-Bulb Temperature Difference Range 10 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dry-Bulb Temperature Difference Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `drybulb_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self["Dry-Bulb Temperature Difference Range 10 Upper Limit"]

    @drybulb_temperature_difference_range_10_upper_limit.setter
    def drybulb_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD field `Dry-Bulb Temperature Difference Range 10 Upper Limit`

        """
        self["Dry-Bulb Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationOutdoorWetBulbDifference(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorWetBulbDifference`
        Plant equipment operation scheme for outdoor wet-bulb temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor wet-bulb temperature.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference temperature node name',
                                       {'name': u'Reference Temperature Node Name',
                                        'pyname': u'reference_temperature_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'wet-bulb temperature difference range 1 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 1 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_1_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 1 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 1 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_1_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 2 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 2 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_2_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 2 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 2 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_2_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 3 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 3 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_3_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 3 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 3 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_3_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 4 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 4 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_4_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 4 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 4 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_4_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 5 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 5 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_5_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 5 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 5 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_5_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 6 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 6 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_6_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 6 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 6 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_6_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 7 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 7 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_7_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 7 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 7 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_7_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 8 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 8 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_8_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 8 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 8 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_8_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 9 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 9 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_9_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 9 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 9 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_9_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'wet-bulb temperature difference range 10 lower limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 10 Lower Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_10_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'wet-bulb temperature difference range 10 upper limit',
                                       {'name': u'Wet-Bulb Temperature Difference Range 10 Upper Limit',
                                        'pyname': u'wetbulb_temperature_difference_range_10_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 5,
               'name': u'PlantEquipmentOperation:OutdoorWetBulbDifference',
               'pyname': u'PlantEquipmentOperationOutdoorWetBulbDifference',
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
    def reference_temperature_node_name(self):
        """field `Reference Temperature Node Name`

        Args:
            value (str): value for IDD Field `Reference Temperature Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set

        """
        return self["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """Corresponds to IDD field `Reference Temperature Node Name`"""
        self["Reference Temperature Node Name"] = value

    @property
    def wetbulb_temperature_difference_range_1_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 1 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_1_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 1 Lower Limit"]

    @wetbulb_temperature_difference_range_1_lower_limit.setter
    def wetbulb_temperature_difference_range_1_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 1 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 1 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_1_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 1 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_1_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 1 Upper Limit"]

    @wetbulb_temperature_difference_range_1_upper_limit.setter
    def wetbulb_temperature_difference_range_1_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 1 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_2_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 2 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_2_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 2 Lower Limit"]

    @wetbulb_temperature_difference_range_2_lower_limit.setter
    def wetbulb_temperature_difference_range_2_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 2 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 2 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_2_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 2 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_2_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 2 Upper Limit"]

    @wetbulb_temperature_difference_range_2_upper_limit.setter
    def wetbulb_temperature_difference_range_2_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 2 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_3_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 3 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_3_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 3 Lower Limit"]

    @wetbulb_temperature_difference_range_3_lower_limit.setter
    def wetbulb_temperature_difference_range_3_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 3 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 3 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_3_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 3 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_3_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 3 Upper Limit"]

    @wetbulb_temperature_difference_range_3_upper_limit.setter
    def wetbulb_temperature_difference_range_3_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 3 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_4_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 4 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_4_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 4 Lower Limit"]

    @wetbulb_temperature_difference_range_4_lower_limit.setter
    def wetbulb_temperature_difference_range_4_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 4 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 4 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_4_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 4 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_4_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 4 Upper Limit"]

    @wetbulb_temperature_difference_range_4_upper_limit.setter
    def wetbulb_temperature_difference_range_4_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 4 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_5_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 5 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_5_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 5 Lower Limit"]

    @wetbulb_temperature_difference_range_5_lower_limit.setter
    def wetbulb_temperature_difference_range_5_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 5 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 5 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_5_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 5 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_5_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 5 Upper Limit"]

    @wetbulb_temperature_difference_range_5_upper_limit.setter
    def wetbulb_temperature_difference_range_5_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 5 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_6_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 6 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_6_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 6 Lower Limit"]

    @wetbulb_temperature_difference_range_6_lower_limit.setter
    def wetbulb_temperature_difference_range_6_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 6 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 6 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_6_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 6 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_6_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 6 Upper Limit"]

    @wetbulb_temperature_difference_range_6_upper_limit.setter
    def wetbulb_temperature_difference_range_6_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 6 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_7_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 7 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_7_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 7 Lower Limit"]

    @wetbulb_temperature_difference_range_7_lower_limit.setter
    def wetbulb_temperature_difference_range_7_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 7 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 7 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_7_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 7 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_7_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 7 Upper Limit"]

    @wetbulb_temperature_difference_range_7_upper_limit.setter
    def wetbulb_temperature_difference_range_7_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 7 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_8_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 8 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_8_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 8 Lower Limit"]

    @wetbulb_temperature_difference_range_8_lower_limit.setter
    def wetbulb_temperature_difference_range_8_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 8 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 8 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_8_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 8 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_8_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 8 Upper Limit"]

    @wetbulb_temperature_difference_range_8_upper_limit.setter
    def wetbulb_temperature_difference_range_8_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 8 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_9_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 9 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_9_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 9 Lower Limit"]

    @wetbulb_temperature_difference_range_9_lower_limit.setter
    def wetbulb_temperature_difference_range_9_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 9 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 9 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_9_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 9 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_9_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 9 Upper Limit"]

    @wetbulb_temperature_difference_range_9_upper_limit.setter
    def wetbulb_temperature_difference_range_9_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 9 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def wetbulb_temperature_difference_range_10_lower_limit(self):
        """field `Wet-Bulb Temperature Difference Range 10 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_10_lower_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 10 Lower Limit"]

    @wetbulb_temperature_difference_range_10_lower_limit.setter
    def wetbulb_temperature_difference_range_10_lower_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 10 Lower Limit`

        """
        self["Wet-Bulb Temperature Difference Range 10 Lower Limit"] = value

    @property
    def wetbulb_temperature_difference_range_10_upper_limit(self):
        """field `Wet-Bulb Temperature Difference Range 10 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Wet-Bulb Temperature Difference Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `wetbulb_temperature_difference_range_10_upper_limit` or None if not set
        """
        return self["Wet-Bulb Temperature Difference Range 10 Upper Limit"]

    @wetbulb_temperature_difference_range_10_upper_limit.setter
    def wetbulb_temperature_difference_range_10_upper_limit(self, value=None):
        """  Corresponds to IDD field `Wet-Bulb Temperature Difference Range 10 Upper Limit`

        """
        self["Wet-Bulb Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationOutdoorDewpointDifference(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:OutdoorDewpointDifference`
        Plant equipment operation scheme for outdoor dewpoint temperature difference
        operation. Specifies one or more groups of equipment which are available to operate
        for successive ranges based the difference between a reference node temperature and
        the outdoor dewpoint temperature.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference temperature node name',
                                       {'name': u'Reference Temperature Node Name',
                                        'pyname': u'reference_temperature_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'dewpoint temperature difference range 1 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 1 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_1_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 1 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 1 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_1_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 1 equipment list name',
                                       {'name': u'Range 1 Equipment List Name',
                                        'pyname': u'range_1_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 2 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 2 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_2_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 2 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 2 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_2_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 2 equipment list name',
                                       {'name': u'Range 2 Equipment List Name',
                                        'pyname': u'range_2_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 3 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 3 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_3_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 3 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 3 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_3_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 3 equipment list name',
                                       {'name': u'Range 3 Equipment List Name',
                                        'pyname': u'range_3_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 4 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 4 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_4_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 4 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 4 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_4_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 4 equipment list name',
                                       {'name': u'Range 4 Equipment List Name',
                                        'pyname': u'range_4_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 5 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 5 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_5_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 5 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 5 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_5_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 5 equipment list name',
                                       {'name': u'Range 5 Equipment List Name',
                                        'pyname': u'range_5_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 6 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 6 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_6_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 6 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 6 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_6_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 6 equipment list name',
                                       {'name': u'Range 6 Equipment List Name',
                                        'pyname': u'range_6_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 7 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 7 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_7_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 7 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 7 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_7_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 7 equipment list name',
                                       {'name': u'Range 7 Equipment List Name',
                                        'pyname': u'range_7_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 8 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 8 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_8_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 8 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 8 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_8_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 8 equipment list name',
                                       {'name': u'Range 8 Equipment List Name',
                                        'pyname': u'range_8_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 9 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 9 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_9_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 9 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 9 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_9_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 9 equipment list name',
                                       {'name': u'Range 9 Equipment List Name',
                                        'pyname': u'range_9_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'dewpoint temperature difference range 10 lower limit',
                                       {'name': u'Dewpoint Temperature Difference Range 10 Lower Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_10_lower_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'dewpoint temperature difference range 10 upper limit',
                                       {'name': u'Dewpoint Temperature Difference Range 10 Upper Limit',
                                        'pyname': u'dewpoint_temperature_difference_range_10_upper_limit',
                                        'maximum': 100.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': -50.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'range 10 equipment list name',
                                       {'name': u'Range 10 Equipment List Name',
                                        'pyname': u'range_10_equipment_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 5,
               'name': u'PlantEquipmentOperation:OutdoorDewpointDifference',
               'pyname': u'PlantEquipmentOperationOutdoorDewpointDifference',
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
    def reference_temperature_node_name(self):
        """field `Reference Temperature Node Name`

        Args:
            value (str): value for IDD Field `Reference Temperature Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `reference_temperature_node_name` or None if not set

        """
        return self["Reference Temperature Node Name"]

    @reference_temperature_node_name.setter
    def reference_temperature_node_name(self, value=None):
        """Corresponds to IDD field `Reference Temperature Node Name`"""
        self["Reference Temperature Node Name"] = value

    @property
    def dewpoint_temperature_difference_range_1_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 1 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 1 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_1_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 1 Lower Limit"]

    @dewpoint_temperature_difference_range_1_lower_limit.setter
    def dewpoint_temperature_difference_range_1_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 1
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 1 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_1_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 1 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 1 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_1_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 1 Upper Limit"]

    @dewpoint_temperature_difference_range_1_upper_limit.setter
    def dewpoint_temperature_difference_range_1_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 1
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 1 Upper Limit"] = value

    @property
    def range_1_equipment_list_name(self):
        """field `Range 1 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 1 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_1_equipment_list_name` or None if not set

        """
        return self["Range 1 Equipment List Name"]

    @range_1_equipment_list_name.setter
    def range_1_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 1 Equipment List Name`"""
        self["Range 1 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_2_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 2 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 2 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_2_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 2 Lower Limit"]

    @dewpoint_temperature_difference_range_2_lower_limit.setter
    def dewpoint_temperature_difference_range_2_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 2
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 2 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_2_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 2 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 2 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_2_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 2 Upper Limit"]

    @dewpoint_temperature_difference_range_2_upper_limit.setter
    def dewpoint_temperature_difference_range_2_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 2
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 2 Upper Limit"] = value

    @property
    def range_2_equipment_list_name(self):
        """field `Range 2 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 2 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_2_equipment_list_name` or None if not set

        """
        return self["Range 2 Equipment List Name"]

    @range_2_equipment_list_name.setter
    def range_2_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 2 Equipment List Name`"""
        self["Range 2 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_3_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 3 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 3 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_3_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 3 Lower Limit"]

    @dewpoint_temperature_difference_range_3_lower_limit.setter
    def dewpoint_temperature_difference_range_3_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 3
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 3 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_3_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 3 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 3 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_3_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 3 Upper Limit"]

    @dewpoint_temperature_difference_range_3_upper_limit.setter
    def dewpoint_temperature_difference_range_3_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 3
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 3 Upper Limit"] = value

    @property
    def range_3_equipment_list_name(self):
        """field `Range 3 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 3 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_3_equipment_list_name` or None if not set

        """
        return self["Range 3 Equipment List Name"]

    @range_3_equipment_list_name.setter
    def range_3_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 3 Equipment List Name`"""
        self["Range 3 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_4_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 4 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 4 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_4_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 4 Lower Limit"]

    @dewpoint_temperature_difference_range_4_lower_limit.setter
    def dewpoint_temperature_difference_range_4_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 4
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 4 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_4_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 4 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 4 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_4_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 4 Upper Limit"]

    @dewpoint_temperature_difference_range_4_upper_limit.setter
    def dewpoint_temperature_difference_range_4_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 4
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 4 Upper Limit"] = value

    @property
    def range_4_equipment_list_name(self):
        """field `Range 4 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 4 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_4_equipment_list_name` or None if not set

        """
        return self["Range 4 Equipment List Name"]

    @range_4_equipment_list_name.setter
    def range_4_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 4 Equipment List Name`"""
        self["Range 4 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_5_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 5 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 5 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_5_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 5 Lower Limit"]

    @dewpoint_temperature_difference_range_5_lower_limit.setter
    def dewpoint_temperature_difference_range_5_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 5
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 5 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_5_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 5 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 5 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_5_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 5 Upper Limit"]

    @dewpoint_temperature_difference_range_5_upper_limit.setter
    def dewpoint_temperature_difference_range_5_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 5
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 5 Upper Limit"] = value

    @property
    def range_5_equipment_list_name(self):
        """field `Range 5 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 5 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_5_equipment_list_name` or None if not set

        """
        return self["Range 5 Equipment List Name"]

    @range_5_equipment_list_name.setter
    def range_5_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 5 Equipment List Name`"""
        self["Range 5 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_6_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 6 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 6 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_6_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 6 Lower Limit"]

    @dewpoint_temperature_difference_range_6_lower_limit.setter
    def dewpoint_temperature_difference_range_6_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 6
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 6 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_6_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 6 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 6 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_6_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 6 Upper Limit"]

    @dewpoint_temperature_difference_range_6_upper_limit.setter
    def dewpoint_temperature_difference_range_6_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 6
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 6 Upper Limit"] = value

    @property
    def range_6_equipment_list_name(self):
        """field `Range 6 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 6 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_6_equipment_list_name` or None if not set

        """
        return self["Range 6 Equipment List Name"]

    @range_6_equipment_list_name.setter
    def range_6_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 6 Equipment List Name`"""
        self["Range 6 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_7_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 7 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 7 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_7_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 7 Lower Limit"]

    @dewpoint_temperature_difference_range_7_lower_limit.setter
    def dewpoint_temperature_difference_range_7_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 7
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 7 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_7_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 7 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 7 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_7_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 7 Upper Limit"]

    @dewpoint_temperature_difference_range_7_upper_limit.setter
    def dewpoint_temperature_difference_range_7_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 7
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 7 Upper Limit"] = value

    @property
    def range_7_equipment_list_name(self):
        """field `Range 7 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 7 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_7_equipment_list_name` or None if not set

        """
        return self["Range 7 Equipment List Name"]

    @range_7_equipment_list_name.setter
    def range_7_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 7 Equipment List Name`"""
        self["Range 7 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_8_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 8 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 8 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_8_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 8 Lower Limit"]

    @dewpoint_temperature_difference_range_8_lower_limit.setter
    def dewpoint_temperature_difference_range_8_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 8
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 8 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_8_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 8 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 8 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_8_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 8 Upper Limit"]

    @dewpoint_temperature_difference_range_8_upper_limit.setter
    def dewpoint_temperature_difference_range_8_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 8
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 8 Upper Limit"] = value

    @property
    def range_8_equipment_list_name(self):
        """field `Range 8 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 8 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_8_equipment_list_name` or None if not set

        """
        return self["Range 8 Equipment List Name"]

    @range_8_equipment_list_name.setter
    def range_8_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 8 Equipment List Name`"""
        self["Range 8 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_9_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 9 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 9 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_9_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 9 Lower Limit"]

    @dewpoint_temperature_difference_range_9_lower_limit.setter
    def dewpoint_temperature_difference_range_9_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 9
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 9 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_9_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 9 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 9 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_9_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 9 Upper Limit"]

    @dewpoint_temperature_difference_range_9_upper_limit.setter
    def dewpoint_temperature_difference_range_9_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 9
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 9 Upper Limit"] = value

    @property
    def range_9_equipment_list_name(self):
        """field `Range 9 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 9 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_9_equipment_list_name` or None if not set

        """
        return self["Range 9 Equipment List Name"]

    @range_9_equipment_list_name.setter
    def range_9_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 9 Equipment List Name`"""
        self["Range 9 Equipment List Name"] = value

    @property
    def dewpoint_temperature_difference_range_10_lower_limit(self):
        """field `Dewpoint Temperature Difference Range 10 Lower Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 10 Lower Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_10_lower_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 10 Lower Limit"]

    @dewpoint_temperature_difference_range_10_lower_limit.setter
    def dewpoint_temperature_difference_range_10_lower_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 10
        Lower Limit`"""
        self["Dewpoint Temperature Difference Range 10 Lower Limit"] = value

    @property
    def dewpoint_temperature_difference_range_10_upper_limit(self):
        """field `Dewpoint Temperature Difference Range 10 Upper Limit`

        |  Units: deltaC
        |  value >= -50.0
        |  value <= 100.0

        Args:
            value (float): value for IDD Field `Dewpoint Temperature Difference Range 10 Upper Limit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `dewpoint_temperature_difference_range_10_upper_limit` or None if not set

        """
        return self["Dewpoint Temperature Difference Range 10 Upper Limit"]

    @dewpoint_temperature_difference_range_10_upper_limit.setter
    def dewpoint_temperature_difference_range_10_upper_limit(self, value=None):
        """Corresponds to IDD field `Dewpoint Temperature Difference Range 10
        Upper Limit`"""
        self["Dewpoint Temperature Difference Range 10 Upper Limit"] = value

    @property
    def range_10_equipment_list_name(self):
        """field `Range 10 Equipment List Name`

        Args:
            value (str): value for IDD Field `Range 10 Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `range_10_equipment_list_name` or None if not set

        """
        return self["Range 10 Equipment List Name"]

    @range_10_equipment_list_name.setter
    def range_10_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Range 10 Equipment List Name`"""
        self["Range 10 Equipment List Name"] = value




class PlantEquipmentOperationSchemes(DataObject):

    """Corresponds to IDD object `PlantEquipmentOperationSchemes` Operation
    schemes are listed in "priority" order.

    Note that each scheme
    must address the entire load and/or condition ranges for the simulation.
    The actual one selected for use will be the first that is "Scheduled"
    on.  That is, if control scheme 1 is not "on" and control scheme 2
    is -- then control scheme 2 is selected.
    Only plant equipment should be listed on a Control Scheme for this item.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 1 object type',
                                       {'name': u'Control Scheme 1 Object Type',
                                        'pyname': u'control_scheme_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 1 name',
                                       {'name': u'Control Scheme 1 Name',
                                        'pyname': u'control_scheme_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 1 schedule name',
                                       {'name': u'Control Scheme 1 Schedule Name',
                                        'pyname': u'control_scheme_1_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 2 object type',
                                       {'name': u'Control Scheme 2 Object Type',
                                        'pyname': u'control_scheme_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 2 name',
                                       {'name': u'Control Scheme 2 Name',
                                        'pyname': u'control_scheme_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 2 schedule name',
                                       {'name': u'Control Scheme 2 Schedule Name',
                                        'pyname': u'control_scheme_2_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 3 object type',
                                       {'name': u'Control Scheme 3 Object Type',
                                        'pyname': u'control_scheme_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 3 name',
                                       {'name': u'Control Scheme 3 Name',
                                        'pyname': u'control_scheme_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 3 schedule name',
                                       {'name': u'Control Scheme 3 Schedule Name',
                                        'pyname': u'control_scheme_3_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 4 object type',
                                       {'name': u'Control Scheme 4 Object Type',
                                        'pyname': u'control_scheme_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 4 name',
                                       {'name': u'Control Scheme 4 Name',
                                        'pyname': u'control_scheme_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 4 schedule name',
                                       {'name': u'Control Scheme 4 Schedule Name',
                                        'pyname': u'control_scheme_4_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 5 object type',
                                       {'name': u'Control Scheme 5 Object Type',
                                        'pyname': u'control_scheme_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 5 name',
                                       {'name': u'Control Scheme 5 Name',
                                        'pyname': u'control_scheme_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 5 schedule name',
                                       {'name': u'Control Scheme 5 Schedule Name',
                                        'pyname': u'control_scheme_5_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 6 object type',
                                       {'name': u'Control Scheme 6 Object Type',
                                        'pyname': u'control_scheme_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 6 name',
                                       {'name': u'Control Scheme 6 Name',
                                        'pyname': u'control_scheme_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 6 schedule name',
                                       {'name': u'Control Scheme 6 Schedule Name',
                                        'pyname': u'control_scheme_6_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 7 object type',
                                       {'name': u'Control Scheme 7 Object Type',
                                        'pyname': u'control_scheme_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 7 name',
                                       {'name': u'Control Scheme 7 Name',
                                        'pyname': u'control_scheme_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 7 schedule name',
                                       {'name': u'Control Scheme 7 Schedule Name',
                                        'pyname': u'control_scheme_7_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 8 object type',
                                       {'name': u'Control Scheme 8 Object Type',
                                        'pyname': u'control_scheme_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:ComponentSetpoint',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 8 name',
                                       {'name': u'Control Scheme 8 Name',
                                        'pyname': u'control_scheme_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 8 schedule name',
                                       {'name': u'Control Scheme 8 Schedule Name',
                                        'pyname': u'control_scheme_8_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'PlantEquipmentOperationSchemes',
               'pyname': u'PlantEquipmentOperationSchemes',
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
    def control_scheme_1_object_type(self):
        """field `Control Scheme 1 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_1_object_type` or None if not set

        """
        return self["Control Scheme 1 Object Type"]

    @control_scheme_1_object_type.setter
    def control_scheme_1_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 1 Object Type`"""
        self["Control Scheme 1 Object Type"] = value

    @property
    def control_scheme_1_name(self):
        """field `Control Scheme 1 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_1_name` or None if not set

        """
        return self["Control Scheme 1 Name"]

    @control_scheme_1_name.setter
    def control_scheme_1_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 1 Name`"""
        self["Control Scheme 1 Name"] = value

    @property
    def control_scheme_1_schedule_name(self):
        """field `Control Scheme 1 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_1_schedule_name` or None if not set

        """
        return self["Control Scheme 1 Schedule Name"]

    @control_scheme_1_schedule_name.setter
    def control_scheme_1_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 1 Schedule Name`"""
        self["Control Scheme 1 Schedule Name"] = value

    @property
    def control_scheme_2_object_type(self):
        """field `Control Scheme 2 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_2_object_type` or None if not set

        """
        return self["Control Scheme 2 Object Type"]

    @control_scheme_2_object_type.setter
    def control_scheme_2_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 2 Object Type`"""
        self["Control Scheme 2 Object Type"] = value

    @property
    def control_scheme_2_name(self):
        """field `Control Scheme 2 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_2_name` or None if not set

        """
        return self["Control Scheme 2 Name"]

    @control_scheme_2_name.setter
    def control_scheme_2_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 2 Name`"""
        self["Control Scheme 2 Name"] = value

    @property
    def control_scheme_2_schedule_name(self):
        """field `Control Scheme 2 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_2_schedule_name` or None if not set

        """
        return self["Control Scheme 2 Schedule Name"]

    @control_scheme_2_schedule_name.setter
    def control_scheme_2_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 2 Schedule Name`"""
        self["Control Scheme 2 Schedule Name"] = value

    @property
    def control_scheme_3_object_type(self):
        """field `Control Scheme 3 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_3_object_type` or None if not set

        """
        return self["Control Scheme 3 Object Type"]

    @control_scheme_3_object_type.setter
    def control_scheme_3_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 3 Object Type`"""
        self["Control Scheme 3 Object Type"] = value

    @property
    def control_scheme_3_name(self):
        """field `Control Scheme 3 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_3_name` or None if not set

        """
        return self["Control Scheme 3 Name"]

    @control_scheme_3_name.setter
    def control_scheme_3_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 3 Name`"""
        self["Control Scheme 3 Name"] = value

    @property
    def control_scheme_3_schedule_name(self):
        """field `Control Scheme 3 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_3_schedule_name` or None if not set

        """
        return self["Control Scheme 3 Schedule Name"]

    @control_scheme_3_schedule_name.setter
    def control_scheme_3_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 3 Schedule Name`"""
        self["Control Scheme 3 Schedule Name"] = value

    @property
    def control_scheme_4_object_type(self):
        """field `Control Scheme 4 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_4_object_type` or None if not set

        """
        return self["Control Scheme 4 Object Type"]

    @control_scheme_4_object_type.setter
    def control_scheme_4_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 4 Object Type`"""
        self["Control Scheme 4 Object Type"] = value

    @property
    def control_scheme_4_name(self):
        """field `Control Scheme 4 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_4_name` or None if not set

        """
        return self["Control Scheme 4 Name"]

    @control_scheme_4_name.setter
    def control_scheme_4_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 4 Name`"""
        self["Control Scheme 4 Name"] = value

    @property
    def control_scheme_4_schedule_name(self):
        """field `Control Scheme 4 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_4_schedule_name` or None if not set

        """
        return self["Control Scheme 4 Schedule Name"]

    @control_scheme_4_schedule_name.setter
    def control_scheme_4_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 4 Schedule Name`"""
        self["Control Scheme 4 Schedule Name"] = value

    @property
    def control_scheme_5_object_type(self):
        """field `Control Scheme 5 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_5_object_type` or None if not set

        """
        return self["Control Scheme 5 Object Type"]

    @control_scheme_5_object_type.setter
    def control_scheme_5_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 5 Object Type`"""
        self["Control Scheme 5 Object Type"] = value

    @property
    def control_scheme_5_name(self):
        """field `Control Scheme 5 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_5_name` or None if not set

        """
        return self["Control Scheme 5 Name"]

    @control_scheme_5_name.setter
    def control_scheme_5_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 5 Name`"""
        self["Control Scheme 5 Name"] = value

    @property
    def control_scheme_5_schedule_name(self):
        """field `Control Scheme 5 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_5_schedule_name` or None if not set

        """
        return self["Control Scheme 5 Schedule Name"]

    @control_scheme_5_schedule_name.setter
    def control_scheme_5_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 5 Schedule Name`"""
        self["Control Scheme 5 Schedule Name"] = value

    @property
    def control_scheme_6_object_type(self):
        """field `Control Scheme 6 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_6_object_type` or None if not set

        """
        return self["Control Scheme 6 Object Type"]

    @control_scheme_6_object_type.setter
    def control_scheme_6_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 6 Object Type`"""
        self["Control Scheme 6 Object Type"] = value

    @property
    def control_scheme_6_name(self):
        """field `Control Scheme 6 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_6_name` or None if not set

        """
        return self["Control Scheme 6 Name"]

    @control_scheme_6_name.setter
    def control_scheme_6_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 6 Name`"""
        self["Control Scheme 6 Name"] = value

    @property
    def control_scheme_6_schedule_name(self):
        """field `Control Scheme 6 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_6_schedule_name` or None if not set

        """
        return self["Control Scheme 6 Schedule Name"]

    @control_scheme_6_schedule_name.setter
    def control_scheme_6_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 6 Schedule Name`"""
        self["Control Scheme 6 Schedule Name"] = value

    @property
    def control_scheme_7_object_type(self):
        """field `Control Scheme 7 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_7_object_type` or None if not set

        """
        return self["Control Scheme 7 Object Type"]

    @control_scheme_7_object_type.setter
    def control_scheme_7_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 7 Object Type`"""
        self["Control Scheme 7 Object Type"] = value

    @property
    def control_scheme_7_name(self):
        """field `Control Scheme 7 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_7_name` or None if not set

        """
        return self["Control Scheme 7 Name"]

    @control_scheme_7_name.setter
    def control_scheme_7_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 7 Name`"""
        self["Control Scheme 7 Name"] = value

    @property
    def control_scheme_7_schedule_name(self):
        """field `Control Scheme 7 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_7_schedule_name` or None if not set

        """
        return self["Control Scheme 7 Schedule Name"]

    @control_scheme_7_schedule_name.setter
    def control_scheme_7_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 7 Schedule Name`"""
        self["Control Scheme 7 Schedule Name"] = value

    @property
    def control_scheme_8_object_type(self):
        """field `Control Scheme 8 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_8_object_type` or None if not set

        """
        return self["Control Scheme 8 Object Type"]

    @control_scheme_8_object_type.setter
    def control_scheme_8_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 8 Object Type`"""
        self["Control Scheme 8 Object Type"] = value

    @property
    def control_scheme_8_name(self):
        """field `Control Scheme 8 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_8_name` or None if not set

        """
        return self["Control Scheme 8 Name"]

    @control_scheme_8_name.setter
    def control_scheme_8_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 8 Name`"""
        self["Control Scheme 8 Name"] = value

    @property
    def control_scheme_8_schedule_name(self):
        """field `Control Scheme 8 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_8_schedule_name` or None if not set

        """
        return self["Control Scheme 8 Schedule Name"]

    @control_scheme_8_schedule_name.setter
    def control_scheme_8_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 8 Schedule Name`"""
        self["Control Scheme 8 Schedule Name"] = value




class CondenserEquipmentOperationSchemes(DataObject):

    """Corresponds to IDD object `CondenserEquipmentOperationSchemes` Operation
    schemes are listed in "priority" order.

    Note that each scheme
    must address the entire load and/or condition ranges for the simulation.
    The actual one selected for use will be the first that is "Scheduled"
    on.  That is, if control scheme 1 is not "on" and control scheme 2
    is -- then control scheme 2 is selected.
    Only condenser equipment should be listed on a Control Scheme for this item.

    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 1 object type',
                                       {'name': u'Control Scheme 1 Object Type',
                                        'pyname': u'control_scheme_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 1 name',
                                       {'name': u'Control Scheme 1 Name',
                                        'pyname': u'control_scheme_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 1 schedule name',
                                       {'name': u'Control Scheme 1 Schedule Name',
                                        'pyname': u'control_scheme_1_schedule_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 2 object type',
                                       {'name': u'Control Scheme 2 Object Type',
                                        'pyname': u'control_scheme_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 2 name',
                                       {'name': u'Control Scheme 2 Name',
                                        'pyname': u'control_scheme_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 2 schedule name',
                                       {'name': u'Control Scheme 2 Schedule Name',
                                        'pyname': u'control_scheme_2_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 3 object type',
                                       {'name': u'Control Scheme 3 Object Type',
                                        'pyname': u'control_scheme_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 3 name',
                                       {'name': u'Control Scheme 3 Name',
                                        'pyname': u'control_scheme_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 3 schedule name',
                                       {'name': u'Control Scheme 3 Schedule Name',
                                        'pyname': u'control_scheme_3_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 4 object type',
                                       {'name': u'Control Scheme 4 Object Type',
                                        'pyname': u'control_scheme_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 4 name',
                                       {'name': u'Control Scheme 4 Name',
                                        'pyname': u'control_scheme_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 4 schedule name',
                                       {'name': u'Control Scheme 4 Schedule Name',
                                        'pyname': u'control_scheme_4_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 5 object type',
                                       {'name': u'Control Scheme 5 Object Type',
                                        'pyname': u'control_scheme_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 5 name',
                                       {'name': u'Control Scheme 5 Name',
                                        'pyname': u'control_scheme_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 5 schedule name',
                                       {'name': u'Control Scheme 5 Schedule Name',
                                        'pyname': u'control_scheme_5_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 6 object type',
                                       {'name': u'Control Scheme 6 Object Type',
                                        'pyname': u'control_scheme_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 6 name',
                                       {'name': u'Control Scheme 6 Name',
                                        'pyname': u'control_scheme_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 6 schedule name',
                                       {'name': u'Control Scheme 6 Schedule Name',
                                        'pyname': u'control_scheme_6_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 7 object type',
                                       {'name': u'Control Scheme 7 Object Type',
                                        'pyname': u'control_scheme_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 7 name',
                                       {'name': u'Control Scheme 7 Name',
                                        'pyname': u'control_scheme_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 7 schedule name',
                                       {'name': u'Control Scheme 7 Schedule Name',
                                        'pyname': u'control_scheme_7_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 8 object type',
                                       {'name': u'Control Scheme 8 Object Type',
                                        'pyname': u'control_scheme_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'PlantEquipmentOperation:Uncontrolled',
                                                            u'PlantEquipmentOperation:CoolingLoad',
                                                            u'PlantEquipmentOperation:HeatingLoad',
                                                            u'PlantEquipmentOperation:OutdoorDryBulb',
                                                            u'PlantEquipmentOperation:OutdoorWetBulb',
                                                            u'PlantEquipmentOperation:OutdoorRelativeHumidity',
                                                            u'PlantEquipmentOperation:OutdoorDewpoint',
                                                            u'PlantEquipmentOperation:OutdoorDryBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorWetBulbDifference',
                                                            u'PlantEquipmentOperation:OutdoorDewpointDifference',
                                                            u'PlantEquipmentOperation:UserDefined'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'control scheme 8 name',
                                       {'name': u'Control Scheme 8 Name',
                                        'pyname': u'control_scheme_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'control scheme 8 schedule name',
                                       {'name': u'Control Scheme 8 Schedule Name',
                                        'pyname': u'control_scheme_8_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Plant',
               'min-fields': 4,
               'name': u'CondenserEquipmentOperationSchemes',
               'pyname': u'CondenserEquipmentOperationSchemes',
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
    def control_scheme_1_object_type(self):
        """field `Control Scheme 1 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_1_object_type` or None if not set

        """
        return self["Control Scheme 1 Object Type"]

    @control_scheme_1_object_type.setter
    def control_scheme_1_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 1 Object Type`"""
        self["Control Scheme 1 Object Type"] = value

    @property
    def control_scheme_1_name(self):
        """field `Control Scheme 1 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_1_name` or None if not set

        """
        return self["Control Scheme 1 Name"]

    @control_scheme_1_name.setter
    def control_scheme_1_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 1 Name`"""
        self["Control Scheme 1 Name"] = value

    @property
    def control_scheme_1_schedule_name(self):
        """field `Control Scheme 1 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 1 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_1_schedule_name` or None if not set

        """
        return self["Control Scheme 1 Schedule Name"]

    @control_scheme_1_schedule_name.setter
    def control_scheme_1_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 1 Schedule Name`"""
        self["Control Scheme 1 Schedule Name"] = value

    @property
    def control_scheme_2_object_type(self):
        """field `Control Scheme 2 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_2_object_type` or None if not set

        """
        return self["Control Scheme 2 Object Type"]

    @control_scheme_2_object_type.setter
    def control_scheme_2_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 2 Object Type`"""
        self["Control Scheme 2 Object Type"] = value

    @property
    def control_scheme_2_name(self):
        """field `Control Scheme 2 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_2_name` or None if not set

        """
        return self["Control Scheme 2 Name"]

    @control_scheme_2_name.setter
    def control_scheme_2_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 2 Name`"""
        self["Control Scheme 2 Name"] = value

    @property
    def control_scheme_2_schedule_name(self):
        """field `Control Scheme 2 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 2 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_2_schedule_name` or None if not set

        """
        return self["Control Scheme 2 Schedule Name"]

    @control_scheme_2_schedule_name.setter
    def control_scheme_2_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 2 Schedule Name`"""
        self["Control Scheme 2 Schedule Name"] = value

    @property
    def control_scheme_3_object_type(self):
        """field `Control Scheme 3 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_3_object_type` or None if not set

        """
        return self["Control Scheme 3 Object Type"]

    @control_scheme_3_object_type.setter
    def control_scheme_3_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 3 Object Type`"""
        self["Control Scheme 3 Object Type"] = value

    @property
    def control_scheme_3_name(self):
        """field `Control Scheme 3 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_3_name` or None if not set

        """
        return self["Control Scheme 3 Name"]

    @control_scheme_3_name.setter
    def control_scheme_3_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 3 Name`"""
        self["Control Scheme 3 Name"] = value

    @property
    def control_scheme_3_schedule_name(self):
        """field `Control Scheme 3 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 3 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_3_schedule_name` or None if not set

        """
        return self["Control Scheme 3 Schedule Name"]

    @control_scheme_3_schedule_name.setter
    def control_scheme_3_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 3 Schedule Name`"""
        self["Control Scheme 3 Schedule Name"] = value

    @property
    def control_scheme_4_object_type(self):
        """field `Control Scheme 4 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_4_object_type` or None if not set

        """
        return self["Control Scheme 4 Object Type"]

    @control_scheme_4_object_type.setter
    def control_scheme_4_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 4 Object Type`"""
        self["Control Scheme 4 Object Type"] = value

    @property
    def control_scheme_4_name(self):
        """field `Control Scheme 4 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_4_name` or None if not set

        """
        return self["Control Scheme 4 Name"]

    @control_scheme_4_name.setter
    def control_scheme_4_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 4 Name`"""
        self["Control Scheme 4 Name"] = value

    @property
    def control_scheme_4_schedule_name(self):
        """field `Control Scheme 4 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 4 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_4_schedule_name` or None if not set

        """
        return self["Control Scheme 4 Schedule Name"]

    @control_scheme_4_schedule_name.setter
    def control_scheme_4_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 4 Schedule Name`"""
        self["Control Scheme 4 Schedule Name"] = value

    @property
    def control_scheme_5_object_type(self):
        """field `Control Scheme 5 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_5_object_type` or None if not set

        """
        return self["Control Scheme 5 Object Type"]

    @control_scheme_5_object_type.setter
    def control_scheme_5_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 5 Object Type`"""
        self["Control Scheme 5 Object Type"] = value

    @property
    def control_scheme_5_name(self):
        """field `Control Scheme 5 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_5_name` or None if not set

        """
        return self["Control Scheme 5 Name"]

    @control_scheme_5_name.setter
    def control_scheme_5_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 5 Name`"""
        self["Control Scheme 5 Name"] = value

    @property
    def control_scheme_5_schedule_name(self):
        """field `Control Scheme 5 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 5 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_5_schedule_name` or None if not set

        """
        return self["Control Scheme 5 Schedule Name"]

    @control_scheme_5_schedule_name.setter
    def control_scheme_5_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 5 Schedule Name`"""
        self["Control Scheme 5 Schedule Name"] = value

    @property
    def control_scheme_6_object_type(self):
        """field `Control Scheme 6 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_6_object_type` or None if not set

        """
        return self["Control Scheme 6 Object Type"]

    @control_scheme_6_object_type.setter
    def control_scheme_6_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 6 Object Type`"""
        self["Control Scheme 6 Object Type"] = value

    @property
    def control_scheme_6_name(self):
        """field `Control Scheme 6 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_6_name` or None if not set

        """
        return self["Control Scheme 6 Name"]

    @control_scheme_6_name.setter
    def control_scheme_6_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 6 Name`"""
        self["Control Scheme 6 Name"] = value

    @property
    def control_scheme_6_schedule_name(self):
        """field `Control Scheme 6 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 6 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_6_schedule_name` or None if not set

        """
        return self["Control Scheme 6 Schedule Name"]

    @control_scheme_6_schedule_name.setter
    def control_scheme_6_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 6 Schedule Name`"""
        self["Control Scheme 6 Schedule Name"] = value

    @property
    def control_scheme_7_object_type(self):
        """field `Control Scheme 7 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_7_object_type` or None if not set

        """
        return self["Control Scheme 7 Object Type"]

    @control_scheme_7_object_type.setter
    def control_scheme_7_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 7 Object Type`"""
        self["Control Scheme 7 Object Type"] = value

    @property
    def control_scheme_7_name(self):
        """field `Control Scheme 7 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_7_name` or None if not set

        """
        return self["Control Scheme 7 Name"]

    @control_scheme_7_name.setter
    def control_scheme_7_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 7 Name`"""
        self["Control Scheme 7 Name"] = value

    @property
    def control_scheme_7_schedule_name(self):
        """field `Control Scheme 7 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 7 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_7_schedule_name` or None if not set

        """
        return self["Control Scheme 7 Schedule Name"]

    @control_scheme_7_schedule_name.setter
    def control_scheme_7_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 7 Schedule Name`"""
        self["Control Scheme 7 Schedule Name"] = value

    @property
    def control_scheme_8_object_type(self):
        """field `Control Scheme 8 Object Type`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Object Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_8_object_type` or None if not set

        """
        return self["Control Scheme 8 Object Type"]

    @control_scheme_8_object_type.setter
    def control_scheme_8_object_type(self, value=None):
        """Corresponds to IDD field `Control Scheme 8 Object Type`"""
        self["Control Scheme 8 Object Type"] = value

    @property
    def control_scheme_8_name(self):
        """field `Control Scheme 8 Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_8_name` or None if not set

        """
        return self["Control Scheme 8 Name"]

    @control_scheme_8_name.setter
    def control_scheme_8_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 8 Name`"""
        self["Control Scheme 8 Name"] = value

    @property
    def control_scheme_8_schedule_name(self):
        """field `Control Scheme 8 Schedule Name`

        Args:
            value (str): value for IDD Field `Control Scheme 8 Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `control_scheme_8_schedule_name` or None if not set

        """
        return self["Control Scheme 8 Schedule Name"]

    @control_scheme_8_schedule_name.setter
    def control_scheme_8_schedule_name(self, value=None):
        """Corresponds to IDD field `Control Scheme 8 Schedule Name`"""
        self["Control Scheme 8 Schedule Name"] = value


