from collections import OrderedDict
import logging
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

class AirLoopHvac(object):
    """ Corresponds to IDD object `AirLoopHVAC`
        Defines a central forced air system.
    """
    internal_name = "AirLoopHVAC"
    field_count = 10
    required_fields = ["Name", "Branch List Name", "Supply Side Inlet Node Name", "Demand Side Outlet Node Name", "Demand Side Inlet Node Names", "Supply Side Outlet Node Names"]
    extensible_fields = 0
    format = None
    min_fields = 10
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controller List Name"] = None
        self._data["Availability Manager List Name"] = None
        self._data["Design Supply Air Flow Rate"] = None
        self._data["Branch List Name"] = None
        self._data["Connector List Name"] = None
        self._data["Supply Side Inlet Node Name"] = None
        self._data["Demand Side Outlet Node Name"] = None
        self._data["Demand Side Inlet Node Names"] = None
        self._data["Supply Side Outlet Node Names"] = None
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
        if len(vals[i]) == 0:
            self.controller_list_name = None
        else:
            self.controller_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate = None
        else:
            self.design_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.branch_list_name = None
        else:
            self.branch_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.connector_list_name = None
        else:
            self.connector_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_side_inlet_node_name = None
        else:
            self.supply_side_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_outlet_node_name = None
        else:
            self.demand_side_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.demand_side_inlet_node_names = None
        else:
            self.demand_side_inlet_node_names = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_side_outlet_node_names = None
        else:
            self.supply_side_outlet_node_names = vals[i]
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
                                 ' for field `AirLoopHvac.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.name`')
        self._data["Name"] = value

    @property
    def controller_list_name(self):
        """Get controller_list_name

        Returns:
            str: the value of `controller_list_name` or None if not set
        """
        return self._data["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """  Corresponds to IDD Field `Controller List Name`
        Enter the name of an AirLoopHVAC:ControllerList object.

        Args:
            value (str): value for IDD Field `Controller List Name`
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
                                 ' for field `AirLoopHvac.controller_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.controller_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.controller_list_name`')
        self._data["Controller List Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
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
                                 ' for field `AirLoopHvac.availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

    @property
    def design_supply_air_flow_rate(self):
        """Get design_supply_air_flow_rate

        Returns:
            float: the value of `design_supply_air_flow_rate` or None if not set
        """
        return self._data["Design Supply Air Flow Rate"]

    @design_supply_air_flow_rate.setter
    def design_supply_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Design Supply Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Supply Air Flow Rate`
                Units: m3/s
                Default value: 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Supply Air Flow Rate"] = "Autosize"
                    return
                if not self.strict and "auto" in value_lower:
                    logger.warn('Accept value {} as "Autosize" '
                                 'for field `AirLoopHvac.design_supply_air_flow_rate`'.format(value))
                    self._data["Design Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
                raise ValueError('value {} need to be of type float or "Autosize"'
                                 ' for field `AirLoopHvac.design_supply_air_flow_rate`'.format(value))
        self._data["Design Supply Air Flow Rate"] = value

    @property
    def branch_list_name(self):
        """Get branch_list_name

        Returns:
            str: the value of `branch_list_name` or None if not set
        """
        return self._data["Branch List Name"]

    @branch_list_name.setter
    def branch_list_name(self, value=None):
        """  Corresponds to IDD Field `Branch List Name`
        Name of a BranchList containing all the branches in this air loop

        Args:
            value (str): value for IDD Field `Branch List Name`
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
                                 ' for field `AirLoopHvac.branch_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.branch_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.branch_list_name`')
        self._data["Branch List Name"] = value

    @property
    def connector_list_name(self):
        """Get connector_list_name

        Returns:
            str: the value of `connector_list_name` or None if not set
        """
        return self._data["Connector List Name"]

    @connector_list_name.setter
    def connector_list_name(self, value=None):
        """  Corresponds to IDD Field `Connector List Name`
        Name of a ConnectorList containing all the splitters and mixers in the loop

        Args:
            value (str): value for IDD Field `Connector List Name`
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
                                 ' for field `AirLoopHvac.connector_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.connector_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.connector_list_name`')
        self._data["Connector List Name"] = value

    @property
    def supply_side_inlet_node_name(self):
        """Get supply_side_inlet_node_name

        Returns:
            str: the value of `supply_side_inlet_node_name` or None if not set
        """
        return self._data["Supply Side Inlet Node Name"]

    @supply_side_inlet_node_name.setter
    def supply_side_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Side Inlet Node Name`
        Name of inlet node where return air enters the supply side of the air loop

        Args:
            value (str): value for IDD Field `Supply Side Inlet Node Name`
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
                                 ' for field `AirLoopHvac.supply_side_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.supply_side_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.supply_side_inlet_node_name`')
        self._data["Supply Side Inlet Node Name"] = value

    @property
    def demand_side_outlet_node_name(self):
        """Get demand_side_outlet_node_name

        Returns:
            str: the value of `demand_side_outlet_node_name` or None if not set
        """
        return self._data["Demand Side Outlet Node Name"]

    @demand_side_outlet_node_name.setter
    def demand_side_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Demand Side Outlet Node Name`
        Name of outlet node where return air leaves the demand side and enters the supply side.

        Args:
            value (str): value for IDD Field `Demand Side Outlet Node Name`
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
                                 ' for field `AirLoopHvac.demand_side_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.demand_side_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.demand_side_outlet_node_name`')
        self._data["Demand Side Outlet Node Name"] = value

    @property
    def demand_side_inlet_node_names(self):
        """Get demand_side_inlet_node_names

        Returns:
            str: the value of `demand_side_inlet_node_names` or None if not set
        """
        return self._data["Demand Side Inlet Node Names"]

    @demand_side_inlet_node_names.setter
    def demand_side_inlet_node_names(self, value=None):
        """  Corresponds to IDD Field `Demand Side Inlet Node Names`
        Name of a Node or NodeList containing the inlet node(s) supplying air to zone equipment.

        Args:
            value (str): value for IDD Field `Demand Side Inlet Node Names`
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
                                 ' for field `AirLoopHvac.demand_side_inlet_node_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.demand_side_inlet_node_names`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.demand_side_inlet_node_names`')
        self._data["Demand Side Inlet Node Names"] = value

    @property
    def supply_side_outlet_node_names(self):
        """Get supply_side_outlet_node_names

        Returns:
            str: the value of `supply_side_outlet_node_names` or None if not set
        """
        return self._data["Supply Side Outlet Node Names"]

    @supply_side_outlet_node_names.setter
    def supply_side_outlet_node_names(self, value=None):
        """  Corresponds to IDD Field `Supply Side Outlet Node Names`
        Name of a Node or NodeList containing the outlet node(s) supplying air to the demand side.

        Args:
            value (str): value for IDD Field `Supply Side Outlet Node Names`
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
                                 ' for field `AirLoopHvac.supply_side_outlet_node_names`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvac.supply_side_outlet_node_names`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvac.supply_side_outlet_node_names`')
        self._data["Supply Side Outlet Node Names"] = value

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
                    raise ValueError("Required field AirLoopHvac:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvac:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvac: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvac: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacOutdoorAirSystemEquipmentList(object):
    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem:EquipmentList`
        List equipment in simulation order
    """
    internal_name = "AirLoopHVAC:OutdoorAirSystem:EquipmentList"
    field_count = 19
    required_fields = ["Name", "Component 1 Object Type", "Component 1 Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:OutdoorAirSystem:EquipmentList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Component 1 Object Type"] = None
        self._data["Component 1 Name"] = None
        self._data["Component 2 Object Type"] = None
        self._data["Component 2 Name"] = None
        self._data["Component 3 Object Type"] = None
        self._data["Component 3 Name"] = None
        self._data["Component 4 Object Type"] = None
        self._data["Component 4 Name"] = None
        self._data["Component 5 Object Type"] = None
        self._data["Component 5 Name"] = None
        self._data["Component 6 Object Type"] = None
        self._data["Component 6 Name"] = None
        self._data["Component 7 Object Type"] = None
        self._data["Component 7 Name"] = None
        self._data["Component 8 Object Type"] = None
        self._data["Component 8 Name"] = None
        self._data["Component 9 Object Type"] = None
        self._data["Component 9 Name"] = None
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
        if len(vals[i]) == 0:
            self.component_1_object_type = None
        else:
            self.component_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_1_name = None
        else:
            self.component_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_object_type = None
        else:
            self.component_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_2_name = None
        else:
            self.component_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_object_type = None
        else:
            self.component_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_3_name = None
        else:
            self.component_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_object_type = None
        else:
            self.component_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_4_name = None
        else:
            self.component_4_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_object_type = None
        else:
            self.component_5_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_5_name = None
        else:
            self.component_5_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_object_type = None
        else:
            self.component_6_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_6_name = None
        else:
            self.component_6_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_object_type = None
        else:
            self.component_7_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_7_name = None
        else:
            self.component_7_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_object_type = None
        else:
            self.component_8_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_8_name = None
        else:
            self.component_8_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_object_type = None
        else:
            self.component_9_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.component_9_name = None
        else:
            self.component_9_name = vals[i]
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.name`')
        self._data["Name"] = value

    @property
    def component_1_object_type(self):
        """Get component_1_object_type

        Returns:
            str: the value of `component_1_object_type` or None if not set
        """
        return self._data["Component 1 Object Type"]

    @component_1_object_type.setter
    def component_1_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 1 Object Type`

        Args:
            value (str): value for IDD Field `Component 1 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_1_object_type`')
        self._data["Component 1 Object Type"] = value

    @property
    def component_1_name(self):
        """Get component_1_name

        Returns:
            str: the value of `component_1_name` or None if not set
        """
        return self._data["Component 1 Name"]

    @component_1_name.setter
    def component_1_name(self, value=None):
        """  Corresponds to IDD Field `Component 1 Name`

        Args:
            value (str): value for IDD Field `Component 1 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_1_name`')
        self._data["Component 1 Name"] = value

    @property
    def component_2_object_type(self):
        """Get component_2_object_type

        Returns:
            str: the value of `component_2_object_type` or None if not set
        """
        return self._data["Component 2 Object Type"]

    @component_2_object_type.setter
    def component_2_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 2 Object Type`

        Args:
            value (str): value for IDD Field `Component 2 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_2_object_type`')
        self._data["Component 2 Object Type"] = value

    @property
    def component_2_name(self):
        """Get component_2_name

        Returns:
            str: the value of `component_2_name` or None if not set
        """
        return self._data["Component 2 Name"]

    @component_2_name.setter
    def component_2_name(self, value=None):
        """  Corresponds to IDD Field `Component 2 Name`

        Args:
            value (str): value for IDD Field `Component 2 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_2_name`')
        self._data["Component 2 Name"] = value

    @property
    def component_3_object_type(self):
        """Get component_3_object_type

        Returns:
            str: the value of `component_3_object_type` or None if not set
        """
        return self._data["Component 3 Object Type"]

    @component_3_object_type.setter
    def component_3_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 3 Object Type`

        Args:
            value (str): value for IDD Field `Component 3 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_3_object_type`')
        self._data["Component 3 Object Type"] = value

    @property
    def component_3_name(self):
        """Get component_3_name

        Returns:
            str: the value of `component_3_name` or None if not set
        """
        return self._data["Component 3 Name"]

    @component_3_name.setter
    def component_3_name(self, value=None):
        """  Corresponds to IDD Field `Component 3 Name`

        Args:
            value (str): value for IDD Field `Component 3 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_3_name`')
        self._data["Component 3 Name"] = value

    @property
    def component_4_object_type(self):
        """Get component_4_object_type

        Returns:
            str: the value of `component_4_object_type` or None if not set
        """
        return self._data["Component 4 Object Type"]

    @component_4_object_type.setter
    def component_4_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 4 Object Type`

        Args:
            value (str): value for IDD Field `Component 4 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_4_object_type`')
        self._data["Component 4 Object Type"] = value

    @property
    def component_4_name(self):
        """Get component_4_name

        Returns:
            str: the value of `component_4_name` or None if not set
        """
        return self._data["Component 4 Name"]

    @component_4_name.setter
    def component_4_name(self, value=None):
        """  Corresponds to IDD Field `Component 4 Name`

        Args:
            value (str): value for IDD Field `Component 4 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_4_name`')
        self._data["Component 4 Name"] = value

    @property
    def component_5_object_type(self):
        """Get component_5_object_type

        Returns:
            str: the value of `component_5_object_type` or None if not set
        """
        return self._data["Component 5 Object Type"]

    @component_5_object_type.setter
    def component_5_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 5 Object Type`

        Args:
            value (str): value for IDD Field `Component 5 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_5_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_5_object_type`')
        self._data["Component 5 Object Type"] = value

    @property
    def component_5_name(self):
        """Get component_5_name

        Returns:
            str: the value of `component_5_name` or None if not set
        """
        return self._data["Component 5 Name"]

    @component_5_name.setter
    def component_5_name(self, value=None):
        """  Corresponds to IDD Field `Component 5 Name`

        Args:
            value (str): value for IDD Field `Component 5 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_5_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_5_name`')
        self._data["Component 5 Name"] = value

    @property
    def component_6_object_type(self):
        """Get component_6_object_type

        Returns:
            str: the value of `component_6_object_type` or None if not set
        """
        return self._data["Component 6 Object Type"]

    @component_6_object_type.setter
    def component_6_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 6 Object Type`

        Args:
            value (str): value for IDD Field `Component 6 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_6_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_6_object_type`')
        self._data["Component 6 Object Type"] = value

    @property
    def component_6_name(self):
        """Get component_6_name

        Returns:
            str: the value of `component_6_name` or None if not set
        """
        return self._data["Component 6 Name"]

    @component_6_name.setter
    def component_6_name(self, value=None):
        """  Corresponds to IDD Field `Component 6 Name`

        Args:
            value (str): value for IDD Field `Component 6 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_6_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_6_name`')
        self._data["Component 6 Name"] = value

    @property
    def component_7_object_type(self):
        """Get component_7_object_type

        Returns:
            str: the value of `component_7_object_type` or None if not set
        """
        return self._data["Component 7 Object Type"]

    @component_7_object_type.setter
    def component_7_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 7 Object Type`

        Args:
            value (str): value for IDD Field `Component 7 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_7_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_7_object_type`')
        self._data["Component 7 Object Type"] = value

    @property
    def component_7_name(self):
        """Get component_7_name

        Returns:
            str: the value of `component_7_name` or None if not set
        """
        return self._data["Component 7 Name"]

    @component_7_name.setter
    def component_7_name(self, value=None):
        """  Corresponds to IDD Field `Component 7 Name`

        Args:
            value (str): value for IDD Field `Component 7 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_7_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_7_name`')
        self._data["Component 7 Name"] = value

    @property
    def component_8_object_type(self):
        """Get component_8_object_type

        Returns:
            str: the value of `component_8_object_type` or None if not set
        """
        return self._data["Component 8 Object Type"]

    @component_8_object_type.setter
    def component_8_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 8 Object Type`

        Args:
            value (str): value for IDD Field `Component 8 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_8_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_8_object_type`')
        self._data["Component 8 Object Type"] = value

    @property
    def component_8_name(self):
        """Get component_8_name

        Returns:
            str: the value of `component_8_name` or None if not set
        """
        return self._data["Component 8 Name"]

    @component_8_name.setter
    def component_8_name(self, value=None):
        """  Corresponds to IDD Field `Component 8 Name`

        Args:
            value (str): value for IDD Field `Component 8 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_8_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_8_name`')
        self._data["Component 8 Name"] = value

    @property
    def component_9_object_type(self):
        """Get component_9_object_type

        Returns:
            str: the value of `component_9_object_type` or None if not set
        """
        return self._data["Component 9 Object Type"]

    @component_9_object_type.setter
    def component_9_object_type(self, value=None):
        """  Corresponds to IDD Field `Component 9 Object Type`

        Args:
            value (str): value for IDD Field `Component 9 Object Type`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_9_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_9_object_type`')
        self._data["Component 9 Object Type"] = value

    @property
    def component_9_name(self):
        """Get component_9_name

        Returns:
            str: the value of `component_9_name` or None if not set
        """
        return self._data["Component 9 Name"]

    @component_9_name.setter
    def component_9_name(self, value=None):
        """  Corresponds to IDD Field `Component 9 Name`

        Args:
            value (str): value for IDD Field `Component 9 Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_9_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystemEquipmentList.component_9_name`')
        self._data["Component 9 Name"] = value

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
                    raise ValueError("Required field AirLoopHvacOutdoorAirSystemEquipmentList:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacOutdoorAirSystemEquipmentList:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacOutdoorAirSystemEquipmentList: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacOutdoorAirSystemEquipmentList: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacOutdoorAirSystem(object):
    """ Corresponds to IDD object `AirLoopHVAC:OutdoorAirSystem`
        Outdoor air subsystem for an AirLoopHVAC. Includes an outdoor air mixing box and
        optional outdoor air conditioning equipment such as heat recovery, preheat, and precool
        coils. From the perspective of the primary air loop the outdoor air system is treated
        as a single component.
    """
    internal_name = "AirLoopHVAC:OutdoorAirSystem"
    field_count = 4
    required_fields = ["Name", "Controller List Name", "Outdoor Air Equipment List Name"]
    extensible_fields = 0
    format = None
    min_fields = 3
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:OutdoorAirSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controller List Name"] = None
        self._data["Outdoor Air Equipment List Name"] = None
        self._data["Availability Manager List Name"] = None
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
        if len(vals[i]) == 0:
            self.controller_list_name = None
        else:
            self.controller_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_equipment_list_name = None
        else:
            self.outdoor_air_equipment_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_manager_list_name = None
        else:
            self.availability_manager_list_name = vals[i]
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
                                 ' for field `AirLoopHvacOutdoorAirSystem.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystem.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystem.name`')
        self._data["Name"] = value

    @property
    def controller_list_name(self):
        """Get controller_list_name

        Returns:
            str: the value of `controller_list_name` or None if not set
        """
        return self._data["Controller List Name"]

    @controller_list_name.setter
    def controller_list_name(self, value=None):
        """  Corresponds to IDD Field `Controller List Name`
        Enter the name of an AirLoopHVAC:ControllerList object.

        Args:
            value (str): value for IDD Field `Controller List Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystem.controller_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystem.controller_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystem.controller_list_name`')
        self._data["Controller List Name"] = value

    @property
    def outdoor_air_equipment_list_name(self):
        """Get outdoor_air_equipment_list_name

        Returns:
            str: the value of `outdoor_air_equipment_list_name` or None if not set
        """
        return self._data["Outdoor Air Equipment List Name"]

    @outdoor_air_equipment_list_name.setter
    def outdoor_air_equipment_list_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Equipment List Name`
        Enter the name of an AirLoopHVAC:OutdoorAirSystem:EquipmentList object.

        Args:
            value (str): value for IDD Field `Outdoor Air Equipment List Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystem.outdoor_air_equipment_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystem.outdoor_air_equipment_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystem.outdoor_air_equipment_list_name`')
        self._data["Outdoor Air Equipment List Name"] = value

    @property
    def availability_manager_list_name(self):
        """Get availability_manager_list_name

        Returns:
            str: the value of `availability_manager_list_name` or None if not set
        """
        return self._data["Availability Manager List Name"]

    @availability_manager_list_name.setter
    def availability_manager_list_name(self, value=None):
        """  Corresponds to IDD Field `Availability Manager List Name`
        Enter the name of an AvailabilityManagerAssignmentList object.

        Args:
            value (str): value for IDD Field `Availability Manager List Name`
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
                                 ' for field `AirLoopHvacOutdoorAirSystem.availability_manager_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacOutdoorAirSystem.availability_manager_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacOutdoorAirSystem.availability_manager_list_name`')
        self._data["Availability Manager List Name"] = value

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
                    raise ValueError("Required field AirLoopHvacOutdoorAirSystem:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacOutdoorAirSystem:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacOutdoorAirSystem: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacOutdoorAirSystem: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class OutdoorAirMixer(object):
    """ Corresponds to IDD object `OutdoorAir:Mixer`
        Outdoor air mixer. Node names cannot be duplicated within a single OutdoorAir:Mixer
        object or across all outdoor air mixers.
    """
    internal_name = "OutdoorAir:Mixer"
    field_count = 5
    required_fields = ["Name", "Mixed Air Node Name", "Outdoor Air Stream Node Name", "Relief Air Stream Node Name", "Return Air Stream Node Name"]
    extensible_fields = 0
    format = None
    min_fields = 0
    extensible_keys = []

    def __init__(self):
        """ Init data dictionary object for IDD  `OutdoorAir:Mixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Mixed Air Node Name"] = None
        self._data["Outdoor Air Stream Node Name"] = None
        self._data["Relief Air Stream Node Name"] = None
        self._data["Return Air Stream Node Name"] = None
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
        if len(vals[i]) == 0:
            self.mixed_air_node_name = None
        else:
            self.mixed_air_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_stream_node_name = None
        else:
            self.outdoor_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.relief_air_stream_node_name = None
        else:
            self.relief_air_stream_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.return_air_stream_node_name = None
        else:
            self.return_air_stream_node_name = vals[i]
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
                                 ' for field `OutdoorAirMixer.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirMixer.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirMixer.name`')
        self._data["Name"] = value

    @property
    def mixed_air_node_name(self):
        """Get mixed_air_node_name

        Returns:
            str: the value of `mixed_air_node_name` or None if not set
        """
        return self._data["Mixed Air Node Name"]

    @mixed_air_node_name.setter
    def mixed_air_node_name(self, value=None):
        """  Corresponds to IDD Field `Mixed Air Node Name`
        Name of Mixed Air Node

        Args:
            value (str): value for IDD Field `Mixed Air Node Name`
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
                                 ' for field `OutdoorAirMixer.mixed_air_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirMixer.mixed_air_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirMixer.mixed_air_node_name`')
        self._data["Mixed Air Node Name"] = value

    @property
    def outdoor_air_stream_node_name(self):
        """Get outdoor_air_stream_node_name

        Returns:
            str: the value of `outdoor_air_stream_node_name` or None if not set
        """
        return self._data["Outdoor Air Stream Node Name"]

    @outdoor_air_stream_node_name.setter
    def outdoor_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Outdoor Air Stream Node Name`
        Name of Outdoor Air Stream Node

        Args:
            value (str): value for IDD Field `Outdoor Air Stream Node Name`
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
                                 ' for field `OutdoorAirMixer.outdoor_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirMixer.outdoor_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirMixer.outdoor_air_stream_node_name`')
        self._data["Outdoor Air Stream Node Name"] = value

    @property
    def relief_air_stream_node_name(self):
        """Get relief_air_stream_node_name

        Returns:
            str: the value of `relief_air_stream_node_name` or None if not set
        """
        return self._data["Relief Air Stream Node Name"]

    @relief_air_stream_node_name.setter
    def relief_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Relief Air Stream Node Name`
        Name of Relief Air Stream Node

        Args:
            value (str): value for IDD Field `Relief Air Stream Node Name`
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
                                 ' for field `OutdoorAirMixer.relief_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirMixer.relief_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirMixer.relief_air_stream_node_name`')
        self._data["Relief Air Stream Node Name"] = value

    @property
    def return_air_stream_node_name(self):
        """Get return_air_stream_node_name

        Returns:
            str: the value of `return_air_stream_node_name` or None if not set
        """
        return self._data["Return Air Stream Node Name"]

    @return_air_stream_node_name.setter
    def return_air_stream_node_name(self, value=None):
        """  Corresponds to IDD Field `Return Air Stream Node Name`
        Name of Return Air Stream Node

        Args:
            value (str): value for IDD Field `Return Air Stream Node Name`
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
                                 ' for field `OutdoorAirMixer.return_air_stream_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `OutdoorAirMixer.return_air_stream_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `OutdoorAirMixer.return_air_stream_node_name`')
        self._data["Return Air Stream Node Name"] = value

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
                    raise ValueError("Required field OutdoorAirMixer:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field OutdoorAirMixer:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for OutdoorAirMixer: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for OutdoorAirMixer: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacZoneSplitter(object):
    """ Corresponds to IDD object `AirLoopHVAC:ZoneSplitter`
        Split one air stream into N outlet streams (currently 500 per air loop, but extensible).  Node names
        cannot be duplicated within a single zone splitter (AirLoopHVAC:ZoneSplitter) list.
    """
    internal_name = "AirLoopHVAC:ZoneSplitter"
    field_count = 2
    required_fields = ["Name", "Inlet Node Name"]
    extensible_fields = 1
    format = None
    min_fields = 0
    extensible_keys = ["Outlet  Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:ZoneSplitter`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
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
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
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
                                 ' for field `AirLoopHvacZoneSplitter.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacZoneSplitter.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacZoneSplitter.name`')
        self._data["Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
                                 ' for field `AirLoopHvacZoneSplitter.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacZoneSplitter.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacZoneSplitter.inlet_node_name`')
        self._data["Inlet Node Name"] = value

    def add_extensible(self,
                       outlet_node_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            outlet_node_name (str): value for IDD Field `Outlet  Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_outlet_node_name(outlet_node_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_outlet_node_name(self, value):
        """ Validates falue of field `Outlet  Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacZoneSplitter.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacZoneSplitter.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacZoneSplitter.outlet_node_name`')
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
                    raise ValueError("Required field AirLoopHvacZoneSplitter:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacZoneSplitter:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacZoneSplitter: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacZoneSplitter: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacSupplyPlenum(object):
    """ Corresponds to IDD object `AirLoopHVAC:SupplyPlenum`
        Connects 1 zone inlet air stream, through zone supply plenum, to one or more outlets.
        Node names cannot be duplicated within a single supply plenum list.
    """
    internal_name = "AirLoopHVAC:SupplyPlenum"
    field_count = 4
    required_fields = ["Name", "Zone Name", "Zone Node Name", "Inlet Node Name"]
    extensible_fields = 1
    format = None
    min_fields = 5
    extensible_keys = ["Outlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:SupplyPlenum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Zone Node Name"] = None
        self._data["Inlet Node Name"] = None
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
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
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
                                 ' for field `AirLoopHvacSupplyPlenum.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPlenum.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPlenum.name`')
        self._data["Name"] = value

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
                                 ' for field `AirLoopHvacSupplyPlenum.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPlenum.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPlenum.zone_name`')
        self._data["Zone Name"] = value

    @property
    def zone_node_name(self):
        """Get zone_node_name

        Returns:
            str: the value of `zone_node_name` or None if not set
        """
        return self._data["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`
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
                                 ' for field `AirLoopHvacSupplyPlenum.zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPlenum.zone_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPlenum.zone_node_name`')
        self._data["Zone Node Name"] = value

    @property
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Inlet Node Name`

        Args:
            value (str): value for IDD Field `Inlet Node Name`
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
                                 ' for field `AirLoopHvacSupplyPlenum.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPlenum.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPlenum.inlet_node_name`')
        self._data["Inlet Node Name"] = value

    def add_extensible(self,
                       outlet_node_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            outlet_node_name (str): value for IDD Field `Outlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_outlet_node_name(outlet_node_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_outlet_node_name(self, value):
        """ Validates falue of field `Outlet Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacSupplyPlenum.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPlenum.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPlenum.outlet_node_name`')
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
                    raise ValueError("Required field AirLoopHvacSupplyPlenum:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacSupplyPlenum:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacSupplyPlenum: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacSupplyPlenum: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacSupplyPath(object):
    """ Corresponds to IDD object `AirLoopHVAC:SupplyPath`
        A supply path can only contain AirLoopHVAC:ZoneSplitter and AirLoopHVAC:SupplyPlenum objects
        which may be in series or parallel.
    """
    internal_name = "AirLoopHVAC:SupplyPath"
    field_count = 2
    required_fields = ["Name", "Supply Air Path Inlet Node Name"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Component 1 Object Type", "Component 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:SupplyPath`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Supply Air Path Inlet Node Name"] = None
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
        if len(vals[i]) == 0:
            self.supply_air_path_inlet_node_name = None
        else:
            self.supply_air_path_inlet_node_name = vals[i]
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
                                 ' for field `AirLoopHvacSupplyPath.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPath.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPath.name`')
        self._data["Name"] = value

    @property
    def supply_air_path_inlet_node_name(self):
        """Get supply_air_path_inlet_node_name

        Returns:
            str: the value of `supply_air_path_inlet_node_name` or None if not set
        """
        return self._data["Supply Air Path Inlet Node Name"]

    @supply_air_path_inlet_node_name.setter
    def supply_air_path_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Supply Air Path Inlet Node Name`

        Args:
            value (str): value for IDD Field `Supply Air Path Inlet Node Name`
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
                                 ' for field `AirLoopHvacSupplyPath.supply_air_path_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPath.supply_air_path_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPath.supply_air_path_inlet_node_name`')
        self._data["Supply Air Path Inlet Node Name"] = value

    def add_extensible(self,
                       component_1_object_type=None,
                       component_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            component_1_object_type (str): value for IDD Field `Component 1 Object Type`
                Accepted values are:
                      - AirLoopHVAC:ZoneSplitter
                      - AirLoopHVAC:SupplyPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_name (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_component_1_object_type(component_1_object_type))
        vals.append(self._check_component_1_name(component_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_component_1_object_type(self, value):
        """ Validates falue of field `Component 1 Object Type`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacSupplyPath.component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPath.component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPath.component_1_object_type`')
            vals = {}
            vals["airloophvac:zonesplitter"] = "AirLoopHVAC:ZoneSplitter"
            vals["airloophvac:supplyplenum"] = "AirLoopHVAC:SupplyPlenum"
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
                                     'field `AirLoopHvacSupplyPath.component_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacSupplyPath.component_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        return value

    def _check_component_1_name(self, value):
        """ Validates falue of field `Component 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacSupplyPath.component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacSupplyPath.component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacSupplyPath.component_1_name`')
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
                    raise ValueError("Required field AirLoopHvacSupplyPath:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacSupplyPath:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacSupplyPath: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacSupplyPath: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacZoneMixer(object):
    """ Corresponds to IDD object `AirLoopHVAC:ZoneMixer`
        Mix N inlet air streams into one (currently 500 per air loop, but extensible).  Node names cannot
        be duplicated within a single zone mixer (AirLoopHVAC:ZoneMixer) list.
    """
    internal_name = "AirLoopHVAC:ZoneMixer"
    field_count = 2
    required_fields = ["Name", "Outlet Node Name"]
    extensible_fields = 1
    format = None
    min_fields = 3
    extensible_keys = ["Inlet 1 Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:ZoneMixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outlet Node Name"] = None
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
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
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
                                 ' for field `AirLoopHvacZoneMixer.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacZoneMixer.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacZoneMixer.name`')
        self._data["Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `AirLoopHvacZoneMixer.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacZoneMixer.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacZoneMixer.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    def add_extensible(self,
                       inlet_1_node_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            inlet_1_node_name (str): value for IDD Field `Inlet 1 Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_inlet_1_node_name(inlet_1_node_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_inlet_1_node_name(self, value):
        """ Validates falue of field `Inlet 1 Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacZoneMixer.inlet_1_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacZoneMixer.inlet_1_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacZoneMixer.inlet_1_node_name`')
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
                    raise ValueError("Required field AirLoopHvacZoneMixer:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacZoneMixer:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacZoneMixer: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacZoneMixer: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacReturnPlenum(object):
    """ Corresponds to IDD object `AirLoopHVAC:ReturnPlenum`
        Connects N zone inlet air streams, through zone return plenum, to outlet
        (currently 500 per air loop)
        Node names cannot be duplicated within a single plenum list.
    """
    internal_name = "AirLoopHVAC:ReturnPlenum"
    field_count = 5
    required_fields = ["Name", "Zone Name", "Zone Node Name", "Outlet Node Name"]
    extensible_fields = 1
    format = None
    min_fields = 6
    extensible_keys = ["Inlet Node Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:ReturnPlenum`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Zone Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Induced Air Outlet Node or NodeList Name"] = None
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
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_node_name = None
        else:
            self.zone_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.induced_air_outlet_node_or_nodelist_name = None
        else:
            self.induced_air_outlet_node_or_nodelist_name = vals[i]
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
                                 ' for field `AirLoopHvacReturnPlenum.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPlenum.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPlenum.name`')
        self._data["Name"] = value

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
                                 ' for field `AirLoopHvacReturnPlenum.zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPlenum.zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPlenum.zone_name`')
        self._data["Zone Name"] = value

    @property
    def zone_node_name(self):
        """Get zone_node_name

        Returns:
            str: the value of `zone_node_name` or None if not set
        """
        return self._data["Zone Node Name"]

    @zone_node_name.setter
    def zone_node_name(self, value=None):
        """  Corresponds to IDD Field `Zone Node Name`

        Args:
            value (str): value for IDD Field `Zone Node Name`
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
                                 ' for field `AirLoopHvacReturnPlenum.zone_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPlenum.zone_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPlenum.zone_node_name`')
        self._data["Zone Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Outlet Node Name`

        Args:
            value (str): value for IDD Field `Outlet Node Name`
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
                                 ' for field `AirLoopHvacReturnPlenum.outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPlenum.outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPlenum.outlet_node_name`')
        self._data["Outlet Node Name"] = value

    @property
    def induced_air_outlet_node_or_nodelist_name(self):
        """Get induced_air_outlet_node_or_nodelist_name

        Returns:
            str: the value of `induced_air_outlet_node_or_nodelist_name` or None if not set
        """
        return self._data["Induced Air Outlet Node or NodeList Name"]

    @induced_air_outlet_node_or_nodelist_name.setter
    def induced_air_outlet_node_or_nodelist_name(self, value=None):
        """  Corresponds to IDD Field `Induced Air Outlet Node or NodeList Name`

        Args:
            value (str): value for IDD Field `Induced Air Outlet Node or NodeList Name`
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
                                 ' for field `AirLoopHvacReturnPlenum.induced_air_outlet_node_or_nodelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPlenum.induced_air_outlet_node_or_nodelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPlenum.induced_air_outlet_node_or_nodelist_name`')
        self._data["Induced Air Outlet Node or NodeList Name"] = value

    def add_extensible(self,
                       inlet_node_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            inlet_node_name (str): value for IDD Field `Inlet Node Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_inlet_node_name(inlet_node_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_inlet_node_name(self, value):
        """ Validates falue of field `Inlet Node Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacReturnPlenum.inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPlenum.inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPlenum.inlet_node_name`')
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
                    raise ValueError("Required field AirLoopHvacReturnPlenum:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacReturnPlenum:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacReturnPlenum: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacReturnPlenum: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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

class AirLoopHvacReturnPath(object):
    """ Corresponds to IDD object `AirLoopHVAC:ReturnPath`
        A return air path can only contain one AirLoopHVAC:ZoneMixer
        and one or more AirLoopHVAC:ReturnPlenum objects.
    """
    internal_name = "AirLoopHVAC:ReturnPath"
    field_count = 2
    required_fields = ["Name", "Return Air Path Outlet Node Name"]
    extensible_fields = 2
    format = None
    min_fields = 0
    extensible_keys = ["Component 1 Object Type", "Component 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirLoopHVAC:ReturnPath`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Return Air Path Outlet Node Name"] = None
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
        if len(vals[i]) == 0:
            self.return_air_path_outlet_node_name = None
        else:
            self.return_air_path_outlet_node_name = vals[i]
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
                                 ' for field `AirLoopHvacReturnPath.name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPath.name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPath.name`')
        self._data["Name"] = value

    @property
    def return_air_path_outlet_node_name(self):
        """Get return_air_path_outlet_node_name

        Returns:
            str: the value of `return_air_path_outlet_node_name` or None if not set
        """
        return self._data["Return Air Path Outlet Node Name"]

    @return_air_path_outlet_node_name.setter
    def return_air_path_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `Return Air Path Outlet Node Name`

        Args:
            value (str): value for IDD Field `Return Air Path Outlet Node Name`
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
                                 ' for field `AirLoopHvacReturnPath.return_air_path_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPath.return_air_path_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPath.return_air_path_outlet_node_name`')
        self._data["Return Air Path Outlet Node Name"] = value

    def add_extensible(self,
                       component_1_object_type=None,
                       component_1_name=None,
                       ):
        """ Add values for extensible fields

        Args:

            component_1_object_type (str): value for IDD Field `Component 1 Object Type`
                Accepted values are:
                      - AirLoopHVAC:ZoneMixer
                      - AirLoopHVAC:ReturnPlenum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

            component_1_name (str): value for IDD Field `Component 1 Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value
        """
        vals = []
        vals.append(self._check_component_1_object_type(component_1_object_type))
        vals.append(self._check_component_1_name(component_1_name))
        self._data["extensibles"].append(vals)

    @property
    def extensibles(self):
        """ Get list of all extensibles
        """
        return self._data["extensibles"]

    def _check_component_1_object_type(self, value):
        """ Validates falue of field `Component 1 Object Type`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacReturnPath.component_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPath.component_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPath.component_1_object_type`')
            vals = {}
            vals["airloophvac:zonemixer"] = "AirLoopHVAC:ZoneMixer"
            vals["airloophvac:returnplenum"] = "AirLoopHVAC:ReturnPlenum"
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
                                     'field `AirLoopHvacReturnPath.component_1_object_type`'.format(value))
                else:
                    logger.warn('change value {} to accepted value {} for '
                                 'field `AirLoopHvacReturnPath.component_1_object_type`'.format(value, vals[value_lower]))
            value = vals[value_lower]
        return value

    def _check_component_1_name(self, value):
        """ Validates falue of field `Component 1 Name`
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str'
                                 ' for field `AirLoopHvacReturnPath.component_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `AirLoopHvacReturnPath.component_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `AirLoopHvacReturnPath.component_1_name`')
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
                    raise ValueError("Required field AirLoopHvacReturnPath:{} is None".format(key))
                    break
                else:
                    logger.warn("Required field AirLoopHvacReturnPath:{} is None".format(key))

        out_fields = len(self.export())
        has_minfields = out_fields >= self.min_fields
        if not has_minfields and strict:
            raise ValueError("Not enough fields set for AirLoopHvacReturnPath: {} / {}".format(out_fields,
                                                                                            self.min_fields))
        elif not has_minfields and not strict:
            logger.warn("Not enough fields set for AirLoopHvacReturnPath: {} / {}".format(out_fields,
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

        has_extensibles = False
        for vals in self._data["extensibles"]:
            for i, value in enumerate(vals):
                if value is not None:
                    has_extensibles = True

        if has_extensibles:
            maxel = len(self._data) - 1

        for i, key in reversed(list(enumerate(self._data))):
            maxel = i
            if self._data[key] is not None:
                break

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