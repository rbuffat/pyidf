""" Data objects in group "User Defined HVAC and Plant Component Models"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class ZoneHvacForcedAirUserDefined(DataObject):

    """ Corresponds to IDD object `ZoneHVAC:ForcedAir:UserDefined`
        Defines a generic zone air unit for custom modeling
        using Energy Management System or External Interface
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'overall model simulation program calling manager name',
                                       {'name': u'Overall Model Simulation Program Calling Manager Name',
                                        'pyname': u'overall_model_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'model setup and sizing program calling manager name',
                                       {'name': u'Model Setup and Sizing Program Calling Manager Name',
                                        'pyname': u'model_setup_and_sizing_program_calling_manager_name',
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
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'secondary air outlet node name',
                                       {'name': u'Secondary Air Outlet Node Name',
                                        'pyname': u'secondary_air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'number of plant loop connections',
                                       {'name': u'Number of Plant Loop Connections',
                                        'pyname': u'number_of_plant_loop_connections',
                                        'maximum': 3,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'plant connection 1 inlet node name',
                                       {'name': u'Plant Connection 1 Inlet Node Name',
                                        'pyname': u'plant_connection_1_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 1 outlet node name',
                                       {'name': u'Plant Connection 1 Outlet Node Name',
                                        'pyname': u'plant_connection_1_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 2 inlet node name',
                                       {'name': u'Plant Connection 2 Inlet Node Name',
                                        'pyname': u'plant_connection_2_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 2 outlet node name',
                                       {'name': u'Plant Connection 2 Outlet Node Name',
                                        'pyname': u'plant_connection_2_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 3 inlet node name',
                                       {'name': u'Plant Connection 3 Inlet Node Name',
                                        'pyname': u'plant_connection_3_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 3 outlet node name',
                                       {'name': u'Plant Connection 3 Outlet Node Name',
                                        'pyname': u'plant_connection_3_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply inlet water storage tank name',
                                       {'name': u'Supply Inlet Water Storage Tank Name',
                                        'pyname': u'supply_inlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'collection outlet water storage tank name',
                                       {'name': u'Collection Outlet Water Storage Tank Name',
                                        'pyname': u'collection_outlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient zone name',
                                       {'name': u'Ambient Zone Name',
                                        'pyname': u'ambient_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'User Defined HVAC and Plant Component Models',
               'min-fields': 8,
               'name': u'ZoneHVAC:ForcedAir:UserDefined',
               'pyname': u'ZoneHvacForcedAirUserDefined',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This is the name of the zone unit

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
    def overall_model_simulation_program_calling_manager_name(self):
        """field `Overall Model Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Overall Model Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `overall_model_simulation_program_calling_manager_name` or None if not set

        """
        return self["Overall Model Simulation Program Calling Manager Name"]

    @overall_model_simulation_program_calling_manager_name.setter
    def overall_model_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Overall Model Simulation Program Calling
        Manager Name`"""
        self["Overall Model Simulation Program Calling Manager Name"] = value

    @property
    def model_setup_and_sizing_program_calling_manager_name(self):
        """field `Model Setup and Sizing Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Model Setup and Sizing Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `model_setup_and_sizing_program_calling_manager_name` or None if not set

        """
        return self["Model Setup and Sizing Program Calling Manager Name"]

    @model_setup_and_sizing_program_calling_manager_name.setter
    def model_setup_and_sizing_program_calling_manager_name(self, value=None):
        """Corresponds to IDD field `Model Setup and Sizing Program Calling
        Manager Name`"""
        self["Model Setup and Sizing Program Calling Manager Name"] = value

    @property
    def primary_air_inlet_node_name(self):
        """field `Primary Air Inlet Node Name`

        |  Air inlet node for the unit must be a zone air exhaust Node.

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

        |  Air outlet node for the unit must be a zone air inlet node.

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
    def secondary_air_inlet_node_name(self):
        """field `Secondary Air Inlet Node Name`

        |  Inlet air used for heat rejection or air source

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

        |  Outlet air used for heat rejection or air source

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
    def number_of_plant_loop_connections(self):
        """field `Number of Plant Loop Connections`

        |  value <= 3

        Args:
            value (int): value for IDD Field `Number of Plant Loop Connections`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set

        """
        return self["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """Corresponds to IDD field `Number of Plant Loop Connections`"""
        self["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """field `Plant Connection 1 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set

        """
        return self["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Inlet Node Name`"""
        self["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """field `Plant Connection 1 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set

        """
        return self["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Outlet Node Name`"""
        self["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """field `Plant Connection 2 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set

        """
        return self["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Inlet Node Name`"""
        self["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """field `Plant Connection 2 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set

        """
        return self["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Outlet Node Name`"""
        self["Plant Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_3_inlet_node_name(self):
        """field `Plant Connection 3 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_inlet_node_name` or None if not set

        """
        return self["Plant Connection 3 Inlet Node Name"]

    @plant_connection_3_inlet_node_name.setter
    def plant_connection_3_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 3 Inlet Node Name`"""
        self["Plant Connection 3 Inlet Node Name"] = value

    @property
    def plant_connection_3_outlet_node_name(self):
        """field `Plant Connection 3 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_outlet_node_name` or None if not set

        """
        return self["Plant Connection 3 Outlet Node Name"]

    @plant_connection_3_outlet_node_name.setter
    def plant_connection_3_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 3 Outlet Node Name`"""
        self["Plant Connection 3 Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """field `Supply Inlet Water Storage Tank Name`

        |  Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `Supply Inlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set

        """
        return self["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Supply Inlet Water Storage Tank Name`"""
        self["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """field `Collection Outlet Water Storage Tank Name`

        |  Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `Collection Outlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set

        """
        return self["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Collection Outlet Water Storage Tank
        Name`"""
        self["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """field `Ambient Zone Name`

        |  Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `Ambient Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_zone_name` or None if not set

        """
        return self["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Zone Name`"""
        self["Ambient Zone Name"] = value




class AirTerminalSingleDuctUserDefined(DataObject):

    """ Corresponds to IDD object `AirTerminal:SingleDuct:UserDefined`
        Defines a generic single duct air terminal unit for custom modeling
        using Energy Management System or External Interface
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'overall model simulation program calling manager name',
                                       {'name': u'Overall Model Simulation Program Calling Manager Name',
                                        'pyname': u'overall_model_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'model setup and sizing program calling manager name',
                                       {'name': u'Model Setup and Sizing Program Calling Manager Name',
                                        'pyname': u'model_setup_and_sizing_program_calling_manager_name',
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
                                      (u'secondary air inlet node name',
                                       {'name': u'Secondary Air Inlet Node Name',
                                        'pyname': u'secondary_air_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'secondary air outlet node name',
                                       {'name': u'Secondary Air Outlet Node Name',
                                        'pyname': u'secondary_air_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'number of plant loop connections',
                                       {'name': u'Number of Plant Loop Connections',
                                        'pyname': u'number_of_plant_loop_connections',
                                        'maximum': 2,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 0,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'plant connection 1 inlet node name',
                                       {'name': u'Plant Connection 1 Inlet Node Name',
                                        'pyname': u'plant_connection_1_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 1 outlet node name',
                                       {'name': u'Plant Connection 1 Outlet Node Name',
                                        'pyname': u'plant_connection_1_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 2 inlet node name',
                                       {'name': u'Plant Connection 2 Inlet Node Name',
                                        'pyname': u'plant_connection_2_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 2 outlet node name',
                                       {'name': u'Plant Connection 2 Outlet Node Name',
                                        'pyname': u'plant_connection_2_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply inlet water storage tank name',
                                       {'name': u'Supply Inlet Water Storage Tank Name',
                                        'pyname': u'supply_inlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'collection outlet water storage tank name',
                                       {'name': u'Collection Outlet Water Storage Tank Name',
                                        'pyname': u'collection_outlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient zone name',
                                       {'name': u'Ambient Zone Name',
                                        'pyname': u'ambient_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'User Defined HVAC and Plant Component Models',
               'min-fields': 8,
               'name': u'AirTerminal:SingleDuct:UserDefined',
               'pyname': u'AirTerminalSingleDuctUserDefined',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This is the name of the air terminal

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
    def overall_model_simulation_program_calling_manager_name(self):
        """field `Overall Model Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Overall Model Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `overall_model_simulation_program_calling_manager_name` or None if not set

        """
        return self["Overall Model Simulation Program Calling Manager Name"]

    @overall_model_simulation_program_calling_manager_name.setter
    def overall_model_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Overall Model Simulation Program Calling
        Manager Name`"""
        self["Overall Model Simulation Program Calling Manager Name"] = value

    @property
    def model_setup_and_sizing_program_calling_manager_name(self):
        """field `Model Setup and Sizing Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Model Setup and Sizing Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `model_setup_and_sizing_program_calling_manager_name` or None if not set

        """
        return self["Model Setup and Sizing Program Calling Manager Name"]

    @model_setup_and_sizing_program_calling_manager_name.setter
    def model_setup_and_sizing_program_calling_manager_name(self, value=None):
        """Corresponds to IDD field `Model Setup and Sizing Program Calling
        Manager Name`"""
        self["Model Setup and Sizing Program Calling Manager Name"] = value

    @property
    def primary_air_inlet_node_name(self):
        """field `Primary Air Inlet Node Name`

        |  Air inlet node for the unit must be a zone splitter outlet.

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

        |  Air outlet node for the unit must be a zone air inlet node.

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
    def secondary_air_inlet_node_name(self):
        """field `Secondary Air Inlet Node Name`

        |  Inlet air used for heat rejection or air source

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

        |  Outlet air used for heat rejection or air source

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
    def number_of_plant_loop_connections(self):
        """field `Number of Plant Loop Connections`

        |  value <= 2

        Args:
            value (int): value for IDD Field `Number of Plant Loop Connections`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set

        """
        return self["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """Corresponds to IDD field `Number of Plant Loop Connections`"""
        self["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """field `Plant Connection 1 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set

        """
        return self["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Inlet Node Name`"""
        self["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """field `Plant Connection 1 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set

        """
        return self["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Outlet Node Name`"""
        self["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """field `Plant Connection 2 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set

        """
        return self["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Inlet Node Name`"""
        self["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """field `Plant Connection 2 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set

        """
        return self["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Outlet Node Name`"""
        self["Plant Connection 2 Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """field `Supply Inlet Water Storage Tank Name`

        |  Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `Supply Inlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set

        """
        return self["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Supply Inlet Water Storage Tank Name`"""
        self["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """field `Collection Outlet Water Storage Tank Name`

        |  Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `Collection Outlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set

        """
        return self["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Collection Outlet Water Storage Tank
        Name`"""
        self["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """field `Ambient Zone Name`

        |  Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `Ambient Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_zone_name` or None if not set

        """
        return self["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Zone Name`"""
        self["Ambient Zone Name"] = value




class CoilUserDefined(DataObject):

    """ Corresponds to IDD object `Coil:UserDefined`
        Defines a generic air system component for custom modeling
        using Energy Management System or External Interface
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'overall model simulation program calling manager name',
                                       {'name': u'Overall Model Simulation Program Calling Manager Name',
                                        'pyname': u'overall_model_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'model setup and sizing program calling manager name',
                                       {'name': u'Model Setup and Sizing Program Calling Manager Name',
                                        'pyname': u'model_setup_and_sizing_program_calling_manager_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of air connections',
                                       {'name': u'Number of Air Connections',
                                        'pyname': u'number_of_air_connections',
                                        'maximum': 2,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'air connection 1 inlet node name',
                                       {'name': u'Air Connection 1 Inlet Node Name',
                                        'pyname': u'air_connection_1_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air connection 1 outlet node name',
                                       {'name': u'Air Connection 1 Outlet Node Name',
                                        'pyname': u'air_connection_1_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air connection 2 inlet node name',
                                       {'name': u'Air Connection 2 Inlet Node Name',
                                        'pyname': u'air_connection_2_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air connection 2 outlet node name',
                                       {'name': u'Air Connection 2 Outlet Node Name',
                                        'pyname': u'air_connection_2_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection is used',
                                       {'name': u'Plant Connection is Used',
                                        'pyname': u'plant_connection_is_used',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Yes',
                                                            u'No'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection inlet node name',
                                       {'name': u'Plant Connection Inlet Node Name',
                                        'pyname': u'plant_connection_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection outlet node name',
                                       {'name': u'Plant Connection Outlet Node Name',
                                        'pyname': u'plant_connection_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply inlet water storage tank name',
                                       {'name': u'Supply Inlet Water Storage Tank Name',
                                        'pyname': u'supply_inlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'collection outlet water storage tank name',
                                       {'name': u'Collection Outlet Water Storage Tank Name',
                                        'pyname': u'collection_outlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient zone name',
                                       {'name': u'Ambient Zone Name',
                                        'pyname': u'ambient_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'User Defined HVAC and Plant Component Models',
               'min-fields': 9,
               'name': u'Coil:UserDefined',
               'pyname': u'CoilUserDefined',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This is the name of the coil

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
    def overall_model_simulation_program_calling_manager_name(self):
        """field `Overall Model Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Overall Model Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `overall_model_simulation_program_calling_manager_name` or None if not set

        """
        return self["Overall Model Simulation Program Calling Manager Name"]

    @overall_model_simulation_program_calling_manager_name.setter
    def overall_model_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Overall Model Simulation Program Calling
        Manager Name`"""
        self["Overall Model Simulation Program Calling Manager Name"] = value

    @property
    def model_setup_and_sizing_program_calling_manager_name(self):
        """field `Model Setup and Sizing Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Model Setup and Sizing Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `model_setup_and_sizing_program_calling_manager_name` or None if not set

        """
        return self["Model Setup and Sizing Program Calling Manager Name"]

    @model_setup_and_sizing_program_calling_manager_name.setter
    def model_setup_and_sizing_program_calling_manager_name(self, value=None):
        """Corresponds to IDD field `Model Setup and Sizing Program Calling
        Manager Name`"""
        self["Model Setup and Sizing Program Calling Manager Name"] = value

    @property
    def number_of_air_connections(self):
        """field `Number of Air Connections`

        |  value >= 1
        |  value <= 2

        Args:
            value (int): value for IDD Field `Number of Air Connections`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_air_connections` or None if not set

        """
        return self["Number of Air Connections"]

    @number_of_air_connections.setter
    def number_of_air_connections(self, value=None):
        """Corresponds to IDD field `Number of Air Connections`"""
        self["Number of Air Connections"] = value

    @property
    def air_connection_1_inlet_node_name(self):
        """field `Air Connection 1 Inlet Node Name`

        |  Inlet air for primary air stream

        Args:
            value (str): value for IDD Field `Air Connection 1 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_connection_1_inlet_node_name` or None if not set

        """
        return self["Air Connection 1 Inlet Node Name"]

    @air_connection_1_inlet_node_name.setter
    def air_connection_1_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Connection 1 Inlet Node Name`"""
        self["Air Connection 1 Inlet Node Name"] = value

    @property
    def air_connection_1_outlet_node_name(self):
        """field `Air Connection 1 Outlet Node Name`

        |  Outlet air for primary air stream

        Args:
            value (str): value for IDD Field `Air Connection 1 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_connection_1_outlet_node_name` or None if not set

        """
        return self["Air Connection 1 Outlet Node Name"]

    @air_connection_1_outlet_node_name.setter
    def air_connection_1_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Connection 1 Outlet Node Name`"""
        self["Air Connection 1 Outlet Node Name"] = value

    @property
    def air_connection_2_inlet_node_name(self):
        """field `Air Connection 2 Inlet Node Name`

        |  Inlet air for secondary air stream

        Args:
            value (str): value for IDD Field `Air Connection 2 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_connection_2_inlet_node_name` or None if not set

        """
        return self["Air Connection 2 Inlet Node Name"]

    @air_connection_2_inlet_node_name.setter
    def air_connection_2_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Connection 2 Inlet Node Name`"""
        self["Air Connection 2 Inlet Node Name"] = value

    @property
    def air_connection_2_outlet_node_name(self):
        """field `Air Connection 2 Outlet Node Name`

        |  Outlet air for secondary air stream

        Args:
            value (str): value for IDD Field `Air Connection 2 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_connection_2_outlet_node_name` or None if not set

        """
        return self["Air Connection 2 Outlet Node Name"]

    @air_connection_2_outlet_node_name.setter
    def air_connection_2_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Connection 2 Outlet Node Name`"""
        self["Air Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_is_used(self):
        """field `Plant Connection is Used`

        Args:
            value (str): value for IDD Field `Plant Connection is Used`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_is_used` or None if not set

        """
        return self["Plant Connection is Used"]

    @plant_connection_is_used.setter
    def plant_connection_is_used(self, value=None):
        """Corresponds to IDD field `Plant Connection is Used`"""
        self["Plant Connection is Used"] = value

    @property
    def plant_connection_inlet_node_name(self):
        """field `Plant Connection Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_inlet_node_name` or None if not set

        """
        return self["Plant Connection Inlet Node Name"]

    @plant_connection_inlet_node_name.setter
    def plant_connection_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection Inlet Node Name`"""
        self["Plant Connection Inlet Node Name"] = value

    @property
    def plant_connection_outlet_node_name(self):
        """field `Plant Connection Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_outlet_node_name` or None if not set

        """
        return self["Plant Connection Outlet Node Name"]

    @plant_connection_outlet_node_name.setter
    def plant_connection_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection Outlet Node Name`"""
        self["Plant Connection Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """field `Supply Inlet Water Storage Tank Name`

        |  Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `Supply Inlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set

        """
        return self["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Supply Inlet Water Storage Tank Name`"""
        self["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """field `Collection Outlet Water Storage Tank Name`

        |  Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `Collection Outlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set

        """
        return self["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Collection Outlet Water Storage Tank
        Name`"""
        self["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """field `Ambient Zone Name`

        |  Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `Ambient Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_zone_name` or None if not set

        """
        return self["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Zone Name`"""
        self["Ambient Zone Name"] = value




class PlantComponentUserDefined(DataObject):

    """ Corresponds to IDD object `PlantComponent:UserDefined`
        Defines a generic plant component for custom modeling
        using Energy Management System or External Interface
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'main model program calling manager name',
                                       {'name': u'Main Model Program Calling Manager Name',
                                        'pyname': u'main_model_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'number of plant loop connections',
                                       {'name': u'Number of Plant Loop Connections',
                                        'pyname': u'number_of_plant_loop_connections',
                                        'maximum': 4,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 1,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'plant connection 1 inlet node name',
                                       {'name': u'Plant Connection 1 Inlet Node Name',
                                        'pyname': u'plant_connection_1_inlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 1 outlet node name',
                                       {'name': u'Plant Connection 1 Outlet Node Name',
                                        'pyname': u'plant_connection_1_outlet_node_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 1 loading mode',
                                       {'name': u'Plant Connection 1 Loading Mode',
                                        'pyname': u'plant_connection_1_loading_mode',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'DemandsLoad',
                                                            u'MeetsLoadWithPassiveCapacity',
                                                            u'MeetsLoadWithNominalCapacity',
                                                            u'MeetsLoadWithNominalCapacityLowOutLimit',
                                                            u'MeetsLoadWithNominalCapacityHiOutLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 1 loop flow request mode',
                                       {'name': u'Plant Connection 1 Loop Flow Request Mode',
                                        'pyname': u'plant_connection_1_loop_flow_request_mode',
                                        'required-field': True,
                                        'autosizable': False,
                                        'accepted-values': [u'NeedsFlowIfLoopOn',
                                                            u'NeedsFlowAndTurnsLoopOn',
                                                            u'ReceivesWhateverFlowAvailable'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 1 initialization program calling manager name',
                                       {'name': u'Plant Connection 1 Initialization Program Calling Manager Name',
                                        'pyname': u'plant_connection_1_initialization_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 1 simulation program calling manager name',
                                       {'name': u'Plant Connection 1 Simulation Program Calling Manager Name',
                                        'pyname': u'plant_connection_1_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 2 inlet node name',
                                       {'name': u'Plant Connection 2 Inlet Node Name',
                                        'pyname': u'plant_connection_2_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 2 outlet node name',
                                       {'name': u'Plant Connection 2 Outlet Node Name',
                                        'pyname': u'plant_connection_2_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 2 loading mode',
                                       {'name': u'Plant Connection 2 Loading Mode',
                                        'pyname': u'plant_connection_2_loading_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DemandsLoad',
                                                            u'MeetLoadWithPassiveCapacity',
                                                            u'MeetLoadWithNominalCapacity',
                                                            u'MeetLoadWithNominalCapacityLowOutLimit',
                                                            u'MeetLoadWithNominalCapacityHiOutLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 2 loop flow request mode',
                                       {'name': u'Plant Connection 2 Loop Flow Request Mode',
                                        'pyname': u'plant_connection_2_loop_flow_request_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NeedsFlowIfLoopOn',
                                                            u'NeedsFlowAndTurnsLoopOn',
                                                            u'ReceivesWhateverFlowAvailable'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 2 initialization program calling manager name',
                                       {'name': u'Plant Connection 2 Initialization Program Calling Manager Name',
                                        'pyname': u'plant_connection_2_initialization_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 2 simulation program calling manager name',
                                       {'name': u'Plant Connection 2 Simulation Program Calling Manager Name',
                                        'pyname': u'plant_connection_2_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 3 inlet node name',
                                       {'name': u'Plant Connection 3 Inlet Node Name',
                                        'pyname': u'plant_connection_3_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 3 outlet node name',
                                       {'name': u'Plant Connection 3 Outlet Node Name',
                                        'pyname': u'plant_connection_3_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 3 loading mode',
                                       {'name': u'Plant Connection 3 Loading Mode',
                                        'pyname': u'plant_connection_3_loading_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DemandsLoad',
                                                            u'MeetLoadWithPassiveCapacity',
                                                            u'MeetLoadWithNominalCapacity',
                                                            u'MeetLoadWithNominalCapacityLowOutLimit',
                                                            u'MeetLoadWithNominalCapacityHiOutLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 3 loop flow request mode',
                                       {'name': u'Plant Connection 3 Loop Flow Request Mode',
                                        'pyname': u'plant_connection_3_loop_flow_request_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NeedsFlowIfLoopOn',
                                                            u'NeedsFlowAndTurnsLoopOn',
                                                            u'ReceivesWhateverFlowAvailable'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 3 initialization program calling manager name',
                                       {'name': u'Plant Connection 3 Initialization Program Calling Manager Name',
                                        'pyname': u'plant_connection_3_initialization_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 3 simulation program calling manager name',
                                       {'name': u'Plant Connection 3 Simulation Program Calling Manager Name',
                                        'pyname': u'plant_connection_3_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 4 inlet node name',
                                       {'name': u'Plant Connection 4 Inlet Node Name',
                                        'pyname': u'plant_connection_4_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 4 outlet node name',
                                       {'name': u'Plant Connection 4 Outlet Node Name',
                                        'pyname': u'plant_connection_4_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'plant connection 4 loading mode',
                                       {'name': u'Plant Connection 4 Loading Mode',
                                        'pyname': u'plant_connection_4_loading_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DemandsLoad',
                                                            u'MeetLoadWithPassiveCapacity',
                                                            u'MeetLoadWithNominalCapacity',
                                                            u'MeetLoadWithNominalCapacityLowOutLimit',
                                                            u'MeetLoadWithNominalCapacityHiOutLimit'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 4 loop flow request mode',
                                       {'name': u'Plant Connection 4 Loop Flow Request Mode',
                                        'pyname': u'plant_connection_4_loop_flow_request_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'NeedsFlowIfLoopOn',
                                                            u'NeedsFlowAndTurnsLoopOn',
                                                            u'ReceivesWhateverFlowAvailable'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'plant connection 4 initialization program calling manager name',
                                       {'name': u'Plant Connection 4 Initialization Program Calling Manager Name',
                                        'pyname': u'plant_connection_4_initialization_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'plant connection 4 simulation program calling manager name',
                                       {'name': u'Plant Connection 4 Simulation Program Calling Manager Name',
                                        'pyname': u'plant_connection_4_simulation_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'air connection inlet node name',
                                       {'name': u'Air Connection Inlet Node Name',
                                        'pyname': u'air_connection_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'air connection outlet node name',
                                       {'name': u'Air Connection Outlet Node Name',
                                        'pyname': u'air_connection_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'supply inlet water storage tank name',
                                       {'name': u'Supply Inlet Water Storage Tank Name',
                                        'pyname': u'supply_inlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'collection outlet water storage tank name',
                                       {'name': u'Collection Outlet Water Storage Tank Name',
                                        'pyname': u'collection_outlet_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'ambient zone name',
                                       {'name': u'Ambient Zone Name',
                                        'pyname': u'ambient_zone_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'User Defined HVAC and Plant Component Models',
               'min-fields': 9,
               'name': u'PlantComponent:UserDefined',
               'pyname': u'PlantComponentUserDefined',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This is the name of the plant component

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
    def main_model_program_calling_manager_name(self):
        """field `Main Model Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Main Model Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `main_model_program_calling_manager_name` or None if not set

        """
        return self["Main Model Program Calling Manager Name"]

    @main_model_program_calling_manager_name.setter
    def main_model_program_calling_manager_name(self, value=None):
        """Corresponds to IDD field `Main Model Program Calling Manager
        Name`"""
        self["Main Model Program Calling Manager Name"] = value

    @property
    def number_of_plant_loop_connections(self):
        """field `Number of Plant Loop Connections`

        |  value >= 1
        |  value <= 4

        Args:
            value (int): value for IDD Field `Number of Plant Loop Connections`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set

        """
        return self["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """Corresponds to IDD field `Number of Plant Loop Connections`"""
        self["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """field `Plant Connection 1 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set

        """
        return self["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Inlet Node Name`"""
        self["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """field `Plant Connection 1 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set

        """
        return self["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Outlet Node Name`"""
        self["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_1_loading_mode(self):
        """field `Plant Connection 1 Loading Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Loading Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_loading_mode` or None if not set

        """
        return self["Plant Connection 1 Loading Mode"]

    @plant_connection_1_loading_mode.setter
    def plant_connection_1_loading_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Loading Mode`"""
        self["Plant Connection 1 Loading Mode"] = value

    @property
    def plant_connection_1_loop_flow_request_mode(self):
        """field `Plant Connection 1 Loop Flow Request Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Loop Flow Request Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_loop_flow_request_mode` or None if not set

        """
        return self["Plant Connection 1 Loop Flow Request Mode"]

    @plant_connection_1_loop_flow_request_mode.setter
    def plant_connection_1_loop_flow_request_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 1 Loop Flow Request
        Mode`"""
        self["Plant Connection 1 Loop Flow Request Mode"] = value

    @property
    def plant_connection_1_initialization_program_calling_manager_name(self):
        """field `Plant Connection 1 Initialization Program Calling Manager
        Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Initialization Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_initialization_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 1 Initialization Program Calling Manager Name"]

    @plant_connection_1_initialization_program_calling_manager_name.setter
    def plant_connection_1_initialization_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 1 Initialization Program
        Calling Manager Name`"""
        self[
            "Plant Connection 1 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_1_simulation_program_calling_manager_name(self):
        """field `Plant Connection 1 Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Plant Connection 1 Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_1_simulation_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 1 Simulation Program Calling Manager Name"]

    @plant_connection_1_simulation_program_calling_manager_name.setter
    def plant_connection_1_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 1 Simulation Program
        Calling Manager Name`"""
        self[
            "Plant Connection 1 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """field `Plant Connection 2 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set

        """
        return self["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Inlet Node Name`"""
        self["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """field `Plant Connection 2 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set

        """
        return self["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Outlet Node Name`"""
        self["Plant Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_2_loading_mode(self):
        """field `Plant Connection 2 Loading Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Loading Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_loading_mode` or None if not set

        """
        return self["Plant Connection 2 Loading Mode"]

    @plant_connection_2_loading_mode.setter
    def plant_connection_2_loading_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Loading Mode`"""
        self["Plant Connection 2 Loading Mode"] = value

    @property
    def plant_connection_2_loop_flow_request_mode(self):
        """field `Plant Connection 2 Loop Flow Request Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Loop Flow Request Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_loop_flow_request_mode` or None if not set

        """
        return self["Plant Connection 2 Loop Flow Request Mode"]

    @plant_connection_2_loop_flow_request_mode.setter
    def plant_connection_2_loop_flow_request_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 2 Loop Flow Request
        Mode`"""
        self["Plant Connection 2 Loop Flow Request Mode"] = value

    @property
    def plant_connection_2_initialization_program_calling_manager_name(self):
        """field `Plant Connection 2 Initialization Program Calling Manager
        Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Initialization Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_initialization_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 2 Initialization Program Calling Manager Name"]

    @plant_connection_2_initialization_program_calling_manager_name.setter
    def plant_connection_2_initialization_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 2 Initialization Program
        Calling Manager Name`"""
        self[
            "Plant Connection 2 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_2_simulation_program_calling_manager_name(self):
        """field `Plant Connection 2 Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Plant Connection 2 Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_2_simulation_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 2 Simulation Program Calling Manager Name"]

    @plant_connection_2_simulation_program_calling_manager_name.setter
    def plant_connection_2_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 2 Simulation Program
        Calling Manager Name`"""
        self[
            "Plant Connection 2 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_3_inlet_node_name(self):
        """field `Plant Connection 3 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_inlet_node_name` or None if not set

        """
        return self["Plant Connection 3 Inlet Node Name"]

    @plant_connection_3_inlet_node_name.setter
    def plant_connection_3_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 3 Inlet Node Name`"""
        self["Plant Connection 3 Inlet Node Name"] = value

    @property
    def plant_connection_3_outlet_node_name(self):
        """field `Plant Connection 3 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_outlet_node_name` or None if not set

        """
        return self["Plant Connection 3 Outlet Node Name"]

    @plant_connection_3_outlet_node_name.setter
    def plant_connection_3_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 3 Outlet Node Name`"""
        self["Plant Connection 3 Outlet Node Name"] = value

    @property
    def plant_connection_3_loading_mode(self):
        """field `Plant Connection 3 Loading Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Loading Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_loading_mode` or None if not set

        """
        return self["Plant Connection 3 Loading Mode"]

    @plant_connection_3_loading_mode.setter
    def plant_connection_3_loading_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 3 Loading Mode`"""
        self["Plant Connection 3 Loading Mode"] = value

    @property
    def plant_connection_3_loop_flow_request_mode(self):
        """field `Plant Connection 3 Loop Flow Request Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Loop Flow Request Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_loop_flow_request_mode` or None if not set

        """
        return self["Plant Connection 3 Loop Flow Request Mode"]

    @plant_connection_3_loop_flow_request_mode.setter
    def plant_connection_3_loop_flow_request_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 3 Loop Flow Request
        Mode`"""
        self["Plant Connection 3 Loop Flow Request Mode"] = value

    @property
    def plant_connection_3_initialization_program_calling_manager_name(self):
        """field `Plant Connection 3 Initialization Program Calling Manager
        Name`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Initialization Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_initialization_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 3 Initialization Program Calling Manager Name"]

    @plant_connection_3_initialization_program_calling_manager_name.setter
    def plant_connection_3_initialization_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 3 Initialization Program
        Calling Manager Name`"""
        self[
            "Plant Connection 3 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_3_simulation_program_calling_manager_name(self):
        """field `Plant Connection 3 Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Plant Connection 3 Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_3_simulation_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 3 Simulation Program Calling Manager Name"]

    @plant_connection_3_simulation_program_calling_manager_name.setter
    def plant_connection_3_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 3 Simulation Program
        Calling Manager Name`"""
        self[
            "Plant Connection 3 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_4_inlet_node_name(self):
        """field `Plant Connection 4 Inlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 4 Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_4_inlet_node_name` or None if not set

        """
        return self["Plant Connection 4 Inlet Node Name"]

    @plant_connection_4_inlet_node_name.setter
    def plant_connection_4_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 4 Inlet Node Name`"""
        self["Plant Connection 4 Inlet Node Name"] = value

    @property
    def plant_connection_4_outlet_node_name(self):
        """field `Plant Connection 4 Outlet Node Name`

        Args:
            value (str): value for IDD Field `Plant Connection 4 Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_4_outlet_node_name` or None if not set

        """
        return self["Plant Connection 4 Outlet Node Name"]

    @plant_connection_4_outlet_node_name.setter
    def plant_connection_4_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Plant Connection 4 Outlet Node Name`"""
        self["Plant Connection 4 Outlet Node Name"] = value

    @property
    def plant_connection_4_loading_mode(self):
        """field `Plant Connection 4 Loading Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 4 Loading Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_4_loading_mode` or None if not set

        """
        return self["Plant Connection 4 Loading Mode"]

    @plant_connection_4_loading_mode.setter
    def plant_connection_4_loading_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 4 Loading Mode`"""
        self["Plant Connection 4 Loading Mode"] = value

    @property
    def plant_connection_4_loop_flow_request_mode(self):
        """field `Plant Connection 4 Loop Flow Request Mode`

        Args:
            value (str): value for IDD Field `Plant Connection 4 Loop Flow Request Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_4_loop_flow_request_mode` or None if not set

        """
        return self["Plant Connection 4 Loop Flow Request Mode"]

    @plant_connection_4_loop_flow_request_mode.setter
    def plant_connection_4_loop_flow_request_mode(self, value=None):
        """Corresponds to IDD field `Plant Connection 4 Loop Flow Request
        Mode`"""
        self["Plant Connection 4 Loop Flow Request Mode"] = value

    @property
    def plant_connection_4_initialization_program_calling_manager_name(self):
        """field `Plant Connection 4 Initialization Program Calling Manager
        Name`

        Args:
            value (str): value for IDD Field `Plant Connection 4 Initialization Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_4_initialization_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 4 Initialization Program Calling Manager Name"]

    @plant_connection_4_initialization_program_calling_manager_name.setter
    def plant_connection_4_initialization_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 4 Initialization Program
        Calling Manager Name`"""
        self[
            "Plant Connection 4 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_4_simulation_program_calling_manager_name(self):
        """field `Plant Connection 4 Simulation Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Plant Connection 4 Simulation Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `plant_connection_4_simulation_program_calling_manager_name` or None if not set

        """
        return self[
            "Plant Connection 4 Simulation Program Calling Manager Name"]

    @plant_connection_4_simulation_program_calling_manager_name.setter
    def plant_connection_4_simulation_program_calling_manager_name(
            self,
            value=None):
        """Corresponds to IDD field `Plant Connection 4 Simulation Program
        Calling Manager Name`"""
        self[
            "Plant Connection 4 Simulation Program Calling Manager Name"] = value

    @property
    def air_connection_inlet_node_name(self):
        """field `Air Connection Inlet Node Name`

        |  Inlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `Air Connection Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_connection_inlet_node_name` or None if not set

        """
        return self["Air Connection Inlet Node Name"]

    @air_connection_inlet_node_name.setter
    def air_connection_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Connection Inlet Node Name`"""
        self["Air Connection Inlet Node Name"] = value

    @property
    def air_connection_outlet_node_name(self):
        """field `Air Connection Outlet Node Name`

        |  Outlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `Air Connection Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `air_connection_outlet_node_name` or None if not set

        """
        return self["Air Connection Outlet Node Name"]

    @air_connection_outlet_node_name.setter
    def air_connection_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Air Connection Outlet Node Name`"""
        self["Air Connection Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """field `Supply Inlet Water Storage Tank Name`

        |  Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `Supply Inlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set

        """
        return self["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Supply Inlet Water Storage Tank Name`"""
        self["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """field `Collection Outlet Water Storage Tank Name`

        |  Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `Collection Outlet Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set

        """
        return self["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Collection Outlet Water Storage Tank
        Name`"""
        self["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """field `Ambient Zone Name`

        |  Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `Ambient Zone Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `ambient_zone_name` or None if not set

        """
        return self["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """Corresponds to IDD field `Ambient Zone Name`"""
        self["Ambient Zone Name"] = value




class PlantEquipmentOperationUserDefined(DataObject):

    """ Corresponds to IDD object `PlantEquipmentOperation:UserDefined`
        Defines a generic plant operation scheme for custom supervisory control
        using Energy Management System or External Interface to dispatch loads
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'name',
                                       {'name': u'Name',
                                        'pyname': u'name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'main model program calling manager name',
                                       {'name': u'Main Model Program Calling Manager Name',
                                        'pyname': u'main_model_program_calling_manager_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initialization program calling manager name',
                                       {'name': u'Initialization Program Calling Manager Name',
                                        'pyname': u'initialization_program_calling_manager_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'equipment 1 object type',
                                       {'name': u'Equipment 1 Object Type',
                                        'pyname': u'equipment_1_object_type',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
                                      (u'equipment 1 name',
                                       {'name': u'Equipment 1 Name',
                                        'pyname': u'equipment_1_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'}),
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
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'User Defined HVAC and Plant Component Models',
               'min-fields': 5,
               'name': u'PlantEquipmentOperation:UserDefined',
               'pyname': u'PlantEquipmentOperationUserDefined',
               'required-object': False,
               'unique-object': False}

    @property
    def name(self):
        """field `Name`

        |  This is the name of the plant operation scheme

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
    def main_model_program_calling_manager_name(self):
        """field `Main Model Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Main Model Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `main_model_program_calling_manager_name` or None if not set

        """
        return self["Main Model Program Calling Manager Name"]

    @main_model_program_calling_manager_name.setter
    def main_model_program_calling_manager_name(self, value=None):
        """Corresponds to IDD field `Main Model Program Calling Manager
        Name`"""
        self["Main Model Program Calling Manager Name"] = value

    @property
    def initialization_program_calling_manager_name(self):
        """field `Initialization Program Calling Manager Name`

        Args:
            value (str): value for IDD Field `Initialization Program Calling Manager Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `initialization_program_calling_manager_name` or None if not set

        """
        return self["Initialization Program Calling Manager Name"]

    @initialization_program_calling_manager_name.setter
    def initialization_program_calling_manager_name(self, value=None):
        """Corresponds to IDD field `Initialization Program Calling Manager
        Name`"""
        self["Initialization Program Calling Manager Name"] = value

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


