""" Data objects in group "Air Distribution"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class AirLoopHvac(DataObject):

    """Corresponds to IDD object `AirLoopHVAC` Defines a central forced air
    system."""
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'controller list name',
                                       {'name': u'Controller List Name',
                                        'pyname': u'controller_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'design supply air flow rate',
                                       {'name': u'Design Supply Air Flow Rate',
                                        'pyname': u'design_supply_air_flow_rate',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': 'real',
                                        'unit': u'm3/s'}),
                                      (u'branch list name',
                                       {'name': u'Branch List Name',
                                        'pyname': u'branch_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'connector list name',
                                       {'name': u'Connector List Name',
                                        'pyname': u'connector_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'supply side inlet node name',
                                       {'name': u'Supply Side Inlet Node Name',
                                        'pyname': u'supply_side_inlet_node_name',
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
                                      (u'demand side inlet node names',
                                       {'name': u'Demand Side Inlet Node Names',
                                        'pyname': u'demand_side_inlet_node_names',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply side outlet node names',
                                       {'name': u'Supply Side Outlet Node Names',
                                        'pyname': u'supply_side_outlet_node_names',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 10,
               'name': u'AirLoopHVAC',
               'pyname': u'AirLoopHvac',
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
    def controller_list_name(self):
        """field `Controller List Name`

        |  Enter the name of an AirLoopHVAC:ControllerList object.

        Args:
            value (str): value for IDD Field `Controller List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_list_name` or None if not set

        """
        return self["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """Corresponds to IDD field `Controller List Name`"""
        self["Controller List Name"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

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
    def design_supply_air_flow_rate(self):
        """field `Design Supply Air Flow Rate`

        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Design Supply Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `design_supply_air_flow_rate` or None if not set

        """
        return self["Design Supply Air Flow Rate"]

    @design_supply_air_flow_rate.setter
    def design_supply_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Design Supply Air Flow Rate`"""
        self["Design Supply Air Flow Rate"] = value

    @property
    def branch_list_name(self):
        """field `Branch List Name`

        |  Name of a BranchList containing all the branches in this air loop

        Args:
            value (str): value for IDD Field `Branch List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `branch_list_name` or None if not set

        """
        return self["Branch List Name"]

    @branch_list_name.setter
    def branch_list_name(self, value=None):
        """Corresponds to IDD field `Branch List Name`"""
        self["Branch List Name"] = value

    @property
    def connector_list_name(self):
        """field `Connector List Name`

        |  Name of a ConnectorList containing all the splitters and mixers in the loop

        Args:
            value (str): value for IDD Field `Connector List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `connector_list_name` or None if not set

        """
        return self["Connector List Name"]

    @connector_list_name.setter
    def connector_list_name(self, value=None):
        """Corresponds to IDD field `Connector List Name`"""
        self["Connector List Name"] = value

    @property
    def supply_side_inlet_node_name(self):
        """field `Supply Side Inlet Node Name`

        |  Name of inlet node where return air enters the supply side of the air loop

        Args:
            value (str): value for IDD Field `Supply Side Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_side_inlet_node_name` or None if not set

        """
        return self["Supply Side Inlet Node Name"]

    @supply_side_inlet_node_name.setter
    def supply_side_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply Side Inlet Node Name`"""
        self["Supply Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """field `Demand Side Outlet Node Name`

        |  Name of outlet node where return air leaves the demand side and enters the supply side.

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
    def demand_side_inlet_node_names(self):
        """field `Demand Side Inlet Node Names`

        |  Name of a Node or NodeList containing the inlet node(s) supplying air to zone equipment.

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Names`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `demand_side_inlet_node_names` or None if not set

        """
        return self["Demand Side Inlet Node Names"]

    @demand_side_inlet_node_names.setter
    def demand_side_inlet_node_names(self, value=None):
        """Corresponds to IDD field `Demand Side Inlet Node Names`"""
        self["Demand Side Inlet Node Names"] = value

    @property
    def supply_side_outlet_node_names(self):
        """field `Supply Side Outlet Node Names`

        |  Name of a Node or NodeList containing the outlet node(s) supplying air to the demand side.

        Args:
            value (str): value for IDD Field `Supply Side Outlet Node Names`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_side_outlet_node_names` or None if not set

        """
        return self["Supply Side Outlet Node Names"]

    @supply_side_outlet_node_names.setter
    def supply_side_outlet_node_names(self, value=None):
        """Corresponds to IDD field `Supply Side Outlet Node Names`"""
        self["Supply Side Outlet Node Names"] = value




class AirLoopHvacOutdoorAirSystemEquipmentList(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem:EquipmentList`
        List equipment in simulation order
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'component 1 object type',
                                       {'name': u'Component 1 Object Type',
                                        'pyname': u'component_1_object_type',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 1 name',
                                       {'name': u'Component 1 Name',
                                        'pyname': u'component_1_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 2 object type',
                                       {'name': u'Component 2 Object Type',
                                        'pyname': u'component_2_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 2 name',
                                       {'name': u'Component 2 Name',
                                        'pyname': u'component_2_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 3 object type',
                                       {'name': u'Component 3 Object Type',
                                        'pyname': u'component_3_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 3 name',
                                       {'name': u'Component 3 Name',
                                        'pyname': u'component_3_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 4 object type',
                                       {'name': u'Component 4 Object Type',
                                        'pyname': u'component_4_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 4 name',
                                       {'name': u'Component 4 Name',
                                        'pyname': u'component_4_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 5 object type',
                                       {'name': u'Component 5 Object Type',
                                        'pyname': u'component_5_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 5 name',
                                       {'name': u'Component 5 Name',
                                        'pyname': u'component_5_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 6 object type',
                                       {'name': u'Component 6 Object Type',
                                        'pyname': u'component_6_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 6 name',
                                       {'name': u'Component 6 Name',
                                        'pyname': u'component_6_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 7 object type',
                                       {'name': u'Component 7 Object Type',
                                        'pyname': u'component_7_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 7 name',
                                       {'name': u'Component 7 Name',
                                        'pyname': u'component_7_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 8 object type',
                                       {'name': u'Component 8 Object Type',
                                        'pyname': u'component_8_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 8 name',
                                       {'name': u'Component 8 Name',
                                        'pyname': u'component_8_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 9 object type',
                                       {'name': u'Component 9 Object Type',
                                        'pyname': u'component_9_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'component 9 name',
                                       {'name': u'Component 9 Name',
                                        'pyname': u'component_9_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 0,
               'name': u'AirLoopHVAC:OutdoorAirSystem:EquipmentList',
               'pyname': u'AirLoopHvacOutdoorAirSystemEquipmentList',
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
    def component_1_object_type(self):
        """field `Component 1 Object Type`

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




class AirLoopHvacOutdoorAirSystem(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem`
        Outdoor air subsystem for an AirLoopHVAC. Includes an outdoor air mixing box and
        optional outdoor air conditioning equipment such as heat recovery, preheat, and precool
        coils. From the perspective of the primary air loop the outdoor air system is treated
        as a single component.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'controller list name',
                                       {'name': u'Controller List Name',
                                        'pyname': u'controller_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outdoor air equipment list name',
                                       {'name': u'Outdoor Air Equipment List Name',
                                        'pyname': u'outdoor_air_equipment_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'availability manager list name',
                                       {'name': u'Availability Manager List Name',
                                        'pyname': u'availability_manager_list_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 3,
               'name': u'AirLoopHVAC:OutdoorAirSystem',
               'pyname': u'AirLoopHvacOutdoorAirSystem',
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
    def controller_list_name(self):
        """field `Controller List Name`

        |  Enter the name of an AirLoopHVAC:ControllerList object.

        Args:
            value (str): value for IDD Field `Controller List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `controller_list_name` or None if not set

        """
        return self["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """Corresponds to IDD field `Controller List Name`"""
        self["Controller List Name"] = value

    @property
    def outdoor_air_equipment_list_name(self):
        """field `Outdoor Air Equipment List Name`

        |  Enter the name of an AirLoopHVAC:OutdoorAirSystem:EquipmentList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Equipment List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_equipment_list_name` or None if not set

        """
        return self["Outdoor Air Equipment List Name"]

    @outdoor_air_equipment_list_name.setter
    def outdoor_air_equipment_list_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Equipment List Name`"""
        self["Outdoor Air Equipment List Name"] = value

    @property
    def availability_manager_list_name(self):
        """field `Availability Manager List Name`

        |  Enter the name of an AvailabilityManagerAssignmentList object.

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




class OutdoorAirMixer(DataObject):

    """ Corresponds to IDD object `OutdoorAir:Mixer`
        Outdoor air mixer. Node names cannot be duplicated within a single OutdoorAir:Mixer
        object or across all outdoor air mixers.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'mixed air node name',
                                       {'name': u'Mixed Air Node Name',
                                        'pyname': u'mixed_air_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'outdoor air stream node name',
                                       {'name': u'Outdoor Air Stream Node Name',
                                        'pyname': u'outdoor_air_stream_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'relief air stream node name',
                                       {'name': u'Relief Air Stream Node Name',
                                        'pyname': u'relief_air_stream_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'return air stream node name',
                                       {'name': u'Return Air Stream Node Name',
                                        'pyname': u'return_air_stream_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 0,
               'name': u'OutdoorAir:Mixer',
               'pyname': u'OutdoorAirMixer',
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
    def mixed_air_node_name(self):
        """field `Mixed Air Node Name`

        |  Name of Mixed Air Node

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `mixed_air_node_name` or None if not set

        """
        return self["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """Corresponds to IDD field `Mixed Air Node Name`"""
        self["Mixed Air Node Name"] = value

    @property
    def outdoor_air_stream_node_name(self):
        """field `Outdoor Air Stream Node Name`

        |  Name of Outdoor Air Stream Node

        Args:
            value (str): value for IDD Field `Outdoor Air Stream Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set

        """
        return self["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """Corresponds to IDD field `Outdoor Air Stream Node Name`"""
        self["Outdoor Air Stream Node Name"] = value

    @property
    def relief_air_stream_node_name(self):
        """field `Relief Air Stream Node Name`

        |  Name of Relief Air Stream Node

        Args:
            value (str): value for IDD Field `Relief Air Stream Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `relief_air_stream_node_name` or None if not set

        """
        return self["Relief Air Stream Node Name"]

    @relief_air_stream_node_name.setter
    def relief_air_stream_node_name(self, value=None):
        """Corresponds to IDD field `Relief Air Stream Node Name`"""
        self["Relief Air Stream Node Name"] = value

    @property
    def return_air_stream_node_name(self):
        """field `Return Air Stream Node Name`

        |  Name of Return Air Stream Node

        Args:
            value (str): value for IDD Field `Return Air Stream Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_air_stream_node_name` or None if not set

        """
        return self["Return Air Stream Node Name"]

    @return_air_stream_node_name.setter
    def return_air_stream_node_name(self, value=None):
        """Corresponds to IDD field `Return Air Stream Node Name`"""
        self["Return Air Stream Node Name"] = value




class AirLoopHvacSupplyPath(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:SupplyPath`
        A supply path can only contain AirLoopHVAC:ZoneSplitter and AirLoopHVAC:SupplyPlenum objects
        which may be in series or parallel.
    """
    _schema = {'extensible-fields': OrderedDict([(u'component 1 object type',
                                                  {'name': u'Component 1 Object Type',
                                                   'pyname': u'component_1_object_type',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'accepted-values': [u'AirLoopHVAC:ZoneSplitter',
                                                                       u'AirLoopHVAC:SupplyPlenum'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'}),
                                                 (u'component 1 name',
                                                  {'name': u'Component 1 Name',
                                                   'pyname': u'component_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'supply air path inlet node name',
                                       {'name': u'Supply Air Path Inlet Node Name',
                                        'pyname': u'supply_air_path_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 0,
               'name': u'AirLoopHVAC:SupplyPath',
               'pyname': u'AirLoopHvacSupplyPath',
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
    def supply_air_path_inlet_node_name(self):
        """field `Supply Air Path Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Path Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_air_path_inlet_node_name` or None if not set

        """
        return self["Supply Air Path Inlet Node Name"]

    @supply_air_path_inlet_node_name.setter
    def supply_air_path_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Supply Air Path Inlet Node Name`"""
        self["Supply Air Path Inlet Node Name"] = value

    def add_extensible(self,
                       component_1_object_type=None,
                       component_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            component_1_object_type (str): value for IDD Field `Component 1 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_name (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        component_1_object_type = self.check_value(
            "Component 1 Object Type",
            component_1_object_type)
        vals.append(component_1_object_type)
        component_1_name = self.check_value(
            "Component 1 Name",
            component_1_name)
        vals.append(component_1_name)
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




class AirLoopHvacReturnPath(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:ReturnPath`
        A return air path can only contain one AirLoopHVAC:ZoneMixer
        and one or more AirLoopHVAC:ReturnPlenum objects.
    """
    _schema = {'extensible-fields': OrderedDict([(u'component 1 object type',
                                                  {'name': u'Component 1 Object Type',
                                                   'pyname': u'component_1_object_type',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'accepted-values': [u'AirLoopHVAC:ZoneMixer',
                                                                       u'AirLoopHVAC:ReturnPlenum'],
                                                      'autocalculatable': False,
                                                      'type': 'alpha'}),
                                                 (u'component 1 name',
                                                  {'name': u'Component 1 Name',
                                                   'pyname': u'component_1_name',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'return air path outlet node name',
                                       {'name': u'Return Air Path Outlet Node Name',
                                        'pyname': u'return_air_path_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 0,
               'name': u'AirLoopHVAC:ReturnPath',
               'pyname': u'AirLoopHvacReturnPath',
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
    def return_air_path_outlet_node_name(self):
        """field `Return Air Path Outlet Node Name`

        Args:
            value (str): value for IDD Field `Return Air Path Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `return_air_path_outlet_node_name` or None if not set

        """
        return self["Return Air Path Outlet Node Name"]

    @return_air_path_outlet_node_name.setter
    def return_air_path_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Return Air Path Outlet Node Name`"""
        self["Return Air Path Outlet Node Name"] = value

    def add_extensible(self,
                       component_1_object_type=None,
                       component_1_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            component_1_object_type (str): value for IDD Field `Component 1 Object Type`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_name (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        component_1_object_type = self.check_value(
            "Component 1 Object Type",
            component_1_object_type)
        vals.append(component_1_object_type)
        component_1_name = self.check_value(
            "Component 1 Name",
            component_1_name)
        vals.append(component_1_name)
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




class AirLoopHvacZoneSplitter(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:ZoneSplitter`
        Split one air stream into N outlet streams (currently 500 per air loop, but extensible).  Node names
        cannot be duplicated within a single zone splitter (AirLoopHVAC:ZoneSplitter) list.
    """
    _schema = {'extensible-fields': OrderedDict([(u'outlet  node name',
                                                  {'name': u'Outlet  Node Name',
                                                   'pyname': u'outlet_node_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 0,
               'name': u'AirLoopHVAC:ZoneSplitter',
               'pyname': u'AirLoopHvacZoneSplitter',
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

    def add_extensible(self,
                       outlet_node_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            outlet_node_name (str): value for IDD Field `Outlet  Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        outlet_node_name = self.check_value(
            "Outlet  Node Name",
            outlet_node_name)
        vals.append(outlet_node_name)
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




class AirLoopHvacSupplyPlenum(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:SupplyPlenum`
        Connects 1 zone inlet air stream, through zone supply plenum, to one or more outlets.
        Node names cannot be duplicated within a single supply plenum list.
    """
    _schema = {'extensible-fields': OrderedDict([(u'outlet node name',
                                                  {'name': u'Outlet Node Name',
                                                   'pyname': u'outlet_node_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone node name',
                                       {'name': u'Zone Node Name',
                                        'pyname': u'zone_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'inlet node name',
                                       {'name': u'Inlet Node Name',
                                        'pyname': u'inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 5,
               'name': u'AirLoopHVAC:SupplyPlenum',
               'pyname': u'AirLoopHvacSupplyPlenum',
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
    def zone_node_name(self):
        """field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_node_name` or None if not set

        """
        return self["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """Corresponds to IDD field `Zone Node Name`"""
        self["Zone Node Name"] = value

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

    def add_extensible(self,
                       outlet_node_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            outlet_node_name (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        outlet_node_name = self.check_value(
            "Outlet Node Name",
            outlet_node_name)
        vals.append(outlet_node_name)
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




class AirLoopHvacZoneMixer(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:ZoneMixer`
        Mix N inlet air streams into one (currently 500 per air loop, but extensible).  Node names cannot
        be duplicated within a single zone mixer (AirLoopHVAC:ZoneMixer) list.
    """
    _schema = {'extensible-fields': OrderedDict([(u'inlet 1 node name',
                                                  {'name': u'Inlet 1 Node Name',
                                                   'pyname': u'inlet_1_node_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'outlet node name',
                                       {'name': u'Outlet Node Name',
                                        'pyname': u'outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 3,
               'name': u'AirLoopHVAC:ZoneMixer',
               'pyname': u'AirLoopHvacZoneMixer',
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

    def add_extensible(self,
                       inlet_1_node_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            inlet_1_node_name (str): value for IDD Field `Inlet 1 Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        inlet_1_node_name = self.check_value(
            "Inlet 1 Node Name",
            inlet_1_node_name)
        vals.append(inlet_1_node_name)
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




class AirLoopHvacReturnPlenum(DataObject):

    """ Corresponds to IDD object `AirLoopHVAC:ReturnPlenum`
        Connects N zone inlet air streams, through zone return plenum, to outlet
        (currently 500 per air loop)
        Node names cannot be duplicated within a single plenum list.
    """
    _schema = {'extensible-fields': OrderedDict([(u'inlet node name',
                                                  {'name': u'Inlet Node Name',
                                                   'pyname': u'inlet_node_name',
                                                   'required-field': False,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'node'})]),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'zone name',
                                       {'name': u'Zone Name',
                                        'pyname': u'zone_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone node name',
                                       {'name': u'Zone Node Name',
                                        'pyname': u'zone_node_name',
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
                                      (u'induced air outlet node or nodelist name',
                                       {'name': u'Induced Air Outlet Node or NodeList Name',
                                        'pyname': u'induced_air_outlet_node_or_nodelist_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'})]),
               'format': None,
               'group': u'Air Distribution',
               'min-fields': 6,
               'name': u'AirLoopHVAC:ReturnPlenum',
               'pyname': u'AirLoopHvacReturnPlenum',
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
    def zone_node_name(self):
        """field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_node_name` or None if not set

        """
        return self["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """Corresponds to IDD field `Zone Node Name`"""
        self["Zone Node Name"] = value

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
    def induced_air_outlet_node_or_nodelist_name(self):
        """field `Induced Air Outlet Node or NodeList Name`

        Args:
            value (str): value for IDD Field `Induced Air Outlet Node or NodeList Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `induced_air_outlet_node_or_nodelist_name` or None if not set

        """
        return self["Induced Air Outlet Node or NodeList Name"]

    @induced_air_outlet_node_or_nodelist_name.setter
    def induced_air_outlet_node_or_nodelist_name(self, value=None):
        """Corresponds to IDD field `Induced Air Outlet Node or NodeList
        Name`"""
        self["Induced Air Outlet Node or NodeList Name"] = value

    def add_extensible(self,
                       inlet_node_name=None,
                       ):
        """Add values for extensible fields.

        Args:

            inlet_node_name (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        inlet_node_name = self.check_value("Inlet Node Name", inlet_node_name)
        vals.append(inlet_node_name)
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


