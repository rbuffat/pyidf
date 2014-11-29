from collections import OrderedDict

class PlantComponentTemperatureSource(object):
    """ Corresponds to IDD object `PlantComponent:TemperatureSource`
        Simulates an object of pre-determined (constant or scheduled) source temperature
        The object introduces fluid into the plant loop at the specified temperature and
        at the same flow rate as the fluid enters the component
        Fluid entering the component vanishes equivalent to the relief air in an air system
    """
    internal_name = "PlantComponent:TemperatureSource"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantComponent:TemperatureSource`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node"] = None
        self._data["Outlet Node"] = None
        self._data["Design Volume Flow Rate"] = None
        self._data["Temperature Specification Type"] = None
        self._data["Source Temperature"] = None
        self._data["Source Temperature Schedule Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_node = None
        else:
            self.inlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node = None
        else:
            self.outlet_node = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_volume_flow_rate = None
        else:
            self.design_volume_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.temperature_specification_type = None
        else:
            self.temperature_specification_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_temperature = None
        else:
            self.source_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_temperature_schedule_name = None
        else:
            self.source_temperature_schedule_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        Component Name

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def inlet_node(self):
        """Get inlet_node

        Returns:
            str: the value of `inlet_node` or None if not set
        """
        return self._data["Inlet Node"]

    @inlet_node.setter
    def inlet_node(self, value=None):
        """  Corresponds to IDD Field `inlet_node`
        Name of the source inlet node

        Args:
            value (str): value for IDD Field `inlet_node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node`')

        self._data["Inlet Node"] = value

    @property
    def outlet_node(self):
        """Get outlet_node

        Returns:
            str: the value of `outlet_node` or None if not set
        """
        return self._data["Outlet Node"]

    @outlet_node.setter
    def outlet_node(self, value=None):
        """  Corresponds to IDD Field `outlet_node`
        Name of the source outlet node

        Args:
            value (str): value for IDD Field `outlet_node`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node`')

        self._data["Outlet Node"] = value

    @property
    def design_volume_flow_rate(self):
        """Get design_volume_flow_rate

        Returns:
            float: the value of `design_volume_flow_rate` or None if not set
        """
        return self._data["Design Volume Flow Rate"]

    @design_volume_flow_rate.setter
    def design_volume_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_volume_flow_rate`
        The design volumetric flow rate for this source

        Args:
            value (float): value for IDD Field `design_volume_flow_rate`
                Unit: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_volume_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_volume_flow_rate`')

        self._data["Design Volume Flow Rate"] = value

    @property
    def temperature_specification_type(self):
        """Get temperature_specification_type

        Returns:
            str: the value of `temperature_specification_type` or None if not set
        """
        return self._data["Temperature Specification Type"]

    @temperature_specification_type.setter
    def temperature_specification_type(self, value=None):
        """  Corresponds to IDD Field `temperature_specification_type`

        Args:
            value (str): value for IDD Field `temperature_specification_type`
                Accepted values are:
                      - Constant
                      - Scheduled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `temperature_specification_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `temperature_specification_type`')
            vals = set()
            vals.add("Constant")
            vals.add("Scheduled")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `temperature_specification_type`'.format(value))

        self._data["Temperature Specification Type"] = value

    @property
    def source_temperature(self):
        """Get source_temperature

        Returns:
            float: the value of `source_temperature` or None if not set
        """
        return self._data["Source Temperature"]

    @source_temperature.setter
    def source_temperature(self, value=None):
        """  Corresponds to IDD Field `source_temperature`
        Used if Temperature Specification Type = Constant

        Args:
            value (float): value for IDD Field `source_temperature`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `source_temperature`'.format(value))

        self._data["Source Temperature"] = value

    @property
    def source_temperature_schedule_name(self):
        """Get source_temperature_schedule_name

        Returns:
            str: the value of `source_temperature_schedule_name` or None if not set
        """
        return self._data["Source Temperature Schedule Name"]

    @source_temperature_schedule_name.setter
    def source_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `source_temperature_schedule_name`
        Used if Temperature Specification Type = Scheduled

        Args:
            value (str): value for IDD Field `source_temperature_schedule_name`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `source_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_temperature_schedule_name`')

        self._data["Source Temperature Schedule Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.inlet_node))
        out.append(self._to_str(self.outlet_node))
        out.append(self._to_str(self.design_volume_flow_rate))
        out.append(self._to_str(self.temperature_specification_type))
        out.append(self._to_str(self.source_temperature))
        out.append(self._to_str(self.source_temperature_schedule_name))
        return ",".join(out)

class PlantComponentUserDefined(object):
    """ Corresponds to IDD object `PlantComponent:UserDefined`
        Defines a generic plant component for custom modeling
        using Energy Management System or External Interface
    """
    internal_name = "PlantComponent:UserDefined"
    field_count = 32

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `PlantComponent:UserDefined`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Main Model Program Calling Manager Name"] = None
        self._data["Number of Plant Loop Connections"] = None
        self._data["Plant Connection 1 Inlet Node Name"] = None
        self._data["Plant Connection 1 Outlet Node Name"] = None
        self._data["Plant Connection 1 Loading Mode"] = None
        self._data["Plant Connection 1 Loop Flow Request Mode"] = None
        self._data["Plant Connection 1 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 1 Simulation Program Calling Manager Name"] = None
        self._data["Plant Connection 2 Inlet Node Name"] = None
        self._data["Plant Connection 2 Outlet Node Name"] = None
        self._data["Plant Connection 2 Loading Mode"] = None
        self._data["Plant Connection 2 Loop Flow Request Mode"] = None
        self._data["Plant Connection 2 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 2 Simulation Program Calling Manager Name"] = None
        self._data["Plant Connection 3 Inlet Node Name"] = None
        self._data["Plant Connection 3 Outlet Node Name"] = None
        self._data["Plant Connection 3 Loading Mode"] = None
        self._data["Plant Connection 3 Loop Flow Request Mode"] = None
        self._data["Plant Connection 3 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 3 Simulation Program Calling Manager Name"] = None
        self._data["Plant Connection 4 Inlet Node Name"] = None
        self._data["Plant Connection 4 Outlet Node Name"] = None
        self._data["Plant Connection 4 Loading Mode"] = None
        self._data["Plant Connection 4 Loop Flow Request Mode"] = None
        self._data["Plant Connection 4 Initialization Program Calling Manager Name"] = None
        self._data["Plant Connection 4 Simulation Program Calling Manager Name"] = None
        self._data["Air Connection Inlet Node Name"] = None
        self._data["Air Connection Outlet Node Name"] = None
        self._data["Supply Inlet Water Storage Tank Name"] = None
        self._data["Collection Outlet Water Storage Tank Name"] = None
        self._data["Ambient Zone Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.main_model_program_calling_manager_name = None
        else:
            self.main_model_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_plant_loop_connections = None
        else:
            self.number_of_plant_loop_connections = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_inlet_node_name = None
        else:
            self.plant_connection_1_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_outlet_node_name = None
        else:
            self.plant_connection_1_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_loading_mode = None
        else:
            self.plant_connection_1_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_loop_flow_request_mode = None
        else:
            self.plant_connection_1_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_1_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_1_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_1_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_inlet_node_name = None
        else:
            self.plant_connection_2_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_outlet_node_name = None
        else:
            self.plant_connection_2_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_loading_mode = None
        else:
            self.plant_connection_2_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_loop_flow_request_mode = None
        else:
            self.plant_connection_2_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_2_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_2_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_2_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_inlet_node_name = None
        else:
            self.plant_connection_3_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_outlet_node_name = None
        else:
            self.plant_connection_3_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_loading_mode = None
        else:
            self.plant_connection_3_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_loop_flow_request_mode = None
        else:
            self.plant_connection_3_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_3_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_3_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_3_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_inlet_node_name = None
        else:
            self.plant_connection_4_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_outlet_node_name = None
        else:
            self.plant_connection_4_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_loading_mode = None
        else:
            self.plant_connection_4_loading_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_loop_flow_request_mode = None
        else:
            self.plant_connection_4_loop_flow_request_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_initialization_program_calling_manager_name = None
        else:
            self.plant_connection_4_initialization_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.plant_connection_4_simulation_program_calling_manager_name = None
        else:
            self.plant_connection_4_simulation_program_calling_manager_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_inlet_node_name = None
        else:
            self.air_connection_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.air_connection_outlet_node_name = None
        else:
            self.air_connection_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_inlet_water_storage_tank_name = None
        else:
            self.supply_inlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.collection_outlet_water_storage_tank_name = None
        else:
            self.collection_outlet_water_storage_tank_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ambient_zone_name = None
        else:
            self.ambient_zone_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        This is the name of the plant component

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def main_model_program_calling_manager_name(self):
        """Get main_model_program_calling_manager_name

        Returns:
            str: the value of `main_model_program_calling_manager_name` or None if not set
        """
        return self._data["Main Model Program Calling Manager Name"]

    @main_model_program_calling_manager_name.setter
    def main_model_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `main_model_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `main_model_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `main_model_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `main_model_program_calling_manager_name`')

        self._data["Main Model Program Calling Manager Name"] = value

    @property
    def number_of_plant_loop_connections(self):
        """Get number_of_plant_loop_connections

        Returns:
            int: the value of `number_of_plant_loop_connections` or None if not set
        """
        return self._data["Number of Plant Loop Connections"]

    @number_of_plant_loop_connections.setter
    def number_of_plant_loop_connections(self, value=None):
        """  Corresponds to IDD Field `number_of_plant_loop_connections`

        Args:
            value (int): value for IDD Field `number_of_plant_loop_connections`
                value >= 1
                value <= 4
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_plant_loop_connections`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_plant_loop_connections`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_plant_loop_connections`')

        self._data["Number of Plant Loop Connections"] = value

    @property
    def plant_connection_1_inlet_node_name(self):
        """Get plant_connection_1_inlet_node_name

        Returns:
            str: the value of `plant_connection_1_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Inlet Node Name"]

    @plant_connection_1_inlet_node_name.setter
    def plant_connection_1_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_inlet_node_name`')

        self._data["Plant Connection 1 Inlet Node Name"] = value

    @property
    def plant_connection_1_outlet_node_name(self):
        """Get plant_connection_1_outlet_node_name

        Returns:
            str: the value of `plant_connection_1_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 1 Outlet Node Name"]

    @plant_connection_1_outlet_node_name.setter
    def plant_connection_1_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_outlet_node_name`')

        self._data["Plant Connection 1 Outlet Node Name"] = value

    @property
    def plant_connection_1_loading_mode(self):
        """Get plant_connection_1_loading_mode

        Returns:
            str: the value of `plant_connection_1_loading_mode` or None if not set
        """
        return self._data["Plant Connection 1 Loading Mode"]

    @plant_connection_1_loading_mode.setter
    def plant_connection_1_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_1_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetsLoadWithPassiveCapacity
                      - MeetsLoadWithNominalCapacity
                      - MeetsLoadWithNominalCapacityLowOutLimit
                      - MeetsLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetsLoadWithPassiveCapacity")
            vals.add("MeetsLoadWithNominalCapacity")
            vals.add("MeetsLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetsLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_1_loading_mode`'.format(value))

        self._data["Plant Connection 1 Loading Mode"] = value

    @property
    def plant_connection_1_loop_flow_request_mode(self):
        """Get plant_connection_1_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_1_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 1 Loop Flow Request Mode"]

    @plant_connection_1_loop_flow_request_mode.setter
    def plant_connection_1_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_1_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_loop_flow_request_mode`')

        self._data["Plant Connection 1 Loop Flow Request Mode"] = value

    @property
    def plant_connection_1_initialization_program_calling_manager_name(self):
        """Get plant_connection_1_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_1_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 1 Initialization Program Calling Manager Name"]

    @plant_connection_1_initialization_program_calling_manager_name.setter
    def plant_connection_1_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_initialization_program_calling_manager_name`')

        self._data["Plant Connection 1 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_1_simulation_program_calling_manager_name(self):
        """Get plant_connection_1_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_1_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 1 Simulation Program Calling Manager Name"]

    @plant_connection_1_simulation_program_calling_manager_name.setter
    def plant_connection_1_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_1_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_1_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_1_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_1_simulation_program_calling_manager_name`')

        self._data["Plant Connection 1 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_2_inlet_node_name(self):
        """Get plant_connection_2_inlet_node_name

        Returns:
            str: the value of `plant_connection_2_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Inlet Node Name"]

    @plant_connection_2_inlet_node_name.setter
    def plant_connection_2_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_inlet_node_name`')

        self._data["Plant Connection 2 Inlet Node Name"] = value

    @property
    def plant_connection_2_outlet_node_name(self):
        """Get plant_connection_2_outlet_node_name

        Returns:
            str: the value of `plant_connection_2_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 2 Outlet Node Name"]

    @plant_connection_2_outlet_node_name.setter
    def plant_connection_2_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_outlet_node_name`')

        self._data["Plant Connection 2 Outlet Node Name"] = value

    @property
    def plant_connection_2_loading_mode(self):
        """Get plant_connection_2_loading_mode

        Returns:
            str: the value of `plant_connection_2_loading_mode` or None if not set
        """
        return self._data["Plant Connection 2 Loading Mode"]

    @plant_connection_2_loading_mode.setter
    def plant_connection_2_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_2_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetLoadWithPassiveCapacity
                      - MeetLoadWithNominalCapacity
                      - MeetLoadWithNominalCapacityLowOutLimit
                      - MeetLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetLoadWithPassiveCapacity")
            vals.add("MeetLoadWithNominalCapacity")
            vals.add("MeetLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_2_loading_mode`'.format(value))

        self._data["Plant Connection 2 Loading Mode"] = value

    @property
    def plant_connection_2_loop_flow_request_mode(self):
        """Get plant_connection_2_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_2_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 2 Loop Flow Request Mode"]

    @plant_connection_2_loop_flow_request_mode.setter
    def plant_connection_2_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_2_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_loop_flow_request_mode`')

        self._data["Plant Connection 2 Loop Flow Request Mode"] = value

    @property
    def plant_connection_2_initialization_program_calling_manager_name(self):
        """Get plant_connection_2_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_2_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 2 Initialization Program Calling Manager Name"]

    @plant_connection_2_initialization_program_calling_manager_name.setter
    def plant_connection_2_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_initialization_program_calling_manager_name`')

        self._data["Plant Connection 2 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_2_simulation_program_calling_manager_name(self):
        """Get plant_connection_2_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_2_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 2 Simulation Program Calling Manager Name"]

    @plant_connection_2_simulation_program_calling_manager_name.setter
    def plant_connection_2_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_2_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_2_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_2_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_2_simulation_program_calling_manager_name`')

        self._data["Plant Connection 2 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_3_inlet_node_name(self):
        """Get plant_connection_3_inlet_node_name

        Returns:
            str: the value of `plant_connection_3_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 3 Inlet Node Name"]

    @plant_connection_3_inlet_node_name.setter
    def plant_connection_3_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_inlet_node_name`')

        self._data["Plant Connection 3 Inlet Node Name"] = value

    @property
    def plant_connection_3_outlet_node_name(self):
        """Get plant_connection_3_outlet_node_name

        Returns:
            str: the value of `plant_connection_3_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 3 Outlet Node Name"]

    @plant_connection_3_outlet_node_name.setter
    def plant_connection_3_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_outlet_node_name`')

        self._data["Plant Connection 3 Outlet Node Name"] = value

    @property
    def plant_connection_3_loading_mode(self):
        """Get plant_connection_3_loading_mode

        Returns:
            str: the value of `plant_connection_3_loading_mode` or None if not set
        """
        return self._data["Plant Connection 3 Loading Mode"]

    @plant_connection_3_loading_mode.setter
    def plant_connection_3_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_3_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetLoadWithPassiveCapacity
                      - MeetLoadWithNominalCapacity
                      - MeetLoadWithNominalCapacityLowOutLimit
                      - MeetLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetLoadWithPassiveCapacity")
            vals.add("MeetLoadWithNominalCapacity")
            vals.add("MeetLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_3_loading_mode`'.format(value))

        self._data["Plant Connection 3 Loading Mode"] = value

    @property
    def plant_connection_3_loop_flow_request_mode(self):
        """Get plant_connection_3_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_3_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 3 Loop Flow Request Mode"]

    @plant_connection_3_loop_flow_request_mode.setter
    def plant_connection_3_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_3_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_loop_flow_request_mode`')

        self._data["Plant Connection 3 Loop Flow Request Mode"] = value

    @property
    def plant_connection_3_initialization_program_calling_manager_name(self):
        """Get plant_connection_3_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_3_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 3 Initialization Program Calling Manager Name"]

    @plant_connection_3_initialization_program_calling_manager_name.setter
    def plant_connection_3_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_initialization_program_calling_manager_name`')

        self._data["Plant Connection 3 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_3_simulation_program_calling_manager_name(self):
        """Get plant_connection_3_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_3_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 3 Simulation Program Calling Manager Name"]

    @plant_connection_3_simulation_program_calling_manager_name.setter
    def plant_connection_3_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_3_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_3_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_3_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_3_simulation_program_calling_manager_name`')

        self._data["Plant Connection 3 Simulation Program Calling Manager Name"] = value

    @property
    def plant_connection_4_inlet_node_name(self):
        """Get plant_connection_4_inlet_node_name

        Returns:
            str: the value of `plant_connection_4_inlet_node_name` or None if not set
        """
        return self._data["Plant Connection 4 Inlet Node Name"]

    @plant_connection_4_inlet_node_name.setter
    def plant_connection_4_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_inlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_inlet_node_name`')

        self._data["Plant Connection 4 Inlet Node Name"] = value

    @property
    def plant_connection_4_outlet_node_name(self):
        """Get plant_connection_4_outlet_node_name

        Returns:
            str: the value of `plant_connection_4_outlet_node_name` or None if not set
        """
        return self._data["Plant Connection 4 Outlet Node Name"]

    @plant_connection_4_outlet_node_name.setter
    def plant_connection_4_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_outlet_node_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_outlet_node_name`')

        self._data["Plant Connection 4 Outlet Node Name"] = value

    @property
    def plant_connection_4_loading_mode(self):
        """Get plant_connection_4_loading_mode

        Returns:
            str: the value of `plant_connection_4_loading_mode` or None if not set
        """
        return self._data["Plant Connection 4 Loading Mode"]

    @plant_connection_4_loading_mode.setter
    def plant_connection_4_loading_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_loading_mode`

        Args:
            value (str): value for IDD Field `plant_connection_4_loading_mode`
                Accepted values are:
                      - DemandsLoad
                      - MeetLoadWithPassiveCapacity
                      - MeetLoadWithNominalCapacity
                      - MeetLoadWithNominalCapacityLowOutLimit
                      - MeetLoadWithNominalCapacityHiOutLimit
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_loading_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_loading_mode`')
            vals = set()
            vals.add("DemandsLoad")
            vals.add("MeetLoadWithPassiveCapacity")
            vals.add("MeetLoadWithNominalCapacity")
            vals.add("MeetLoadWithNominalCapacityLowOutLimit")
            vals.add("MeetLoadWithNominalCapacityHiOutLimit")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `plant_connection_4_loading_mode`'.format(value))

        self._data["Plant Connection 4 Loading Mode"] = value

    @property
    def plant_connection_4_loop_flow_request_mode(self):
        """Get plant_connection_4_loop_flow_request_mode

        Returns:
            str: the value of `plant_connection_4_loop_flow_request_mode` or None if not set
        """
        return self._data["Plant Connection 4 Loop Flow Request Mode"]

    @plant_connection_4_loop_flow_request_mode.setter
    def plant_connection_4_loop_flow_request_mode(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_loop_flow_request_mode`

        Args:
            value (str): value for IDD Field `plant_connection_4_loop_flow_request_mode`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_loop_flow_request_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_loop_flow_request_mode`')

        self._data["Plant Connection 4 Loop Flow Request Mode"] = value

    @property
    def plant_connection_4_initialization_program_calling_manager_name(self):
        """Get plant_connection_4_initialization_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_4_initialization_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 4 Initialization Program Calling Manager Name"]

    @plant_connection_4_initialization_program_calling_manager_name.setter
    def plant_connection_4_initialization_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_initialization_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_initialization_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_initialization_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_initialization_program_calling_manager_name`')

        self._data["Plant Connection 4 Initialization Program Calling Manager Name"] = value

    @property
    def plant_connection_4_simulation_program_calling_manager_name(self):
        """Get plant_connection_4_simulation_program_calling_manager_name

        Returns:
            str: the value of `plant_connection_4_simulation_program_calling_manager_name` or None if not set
        """
        return self._data["Plant Connection 4 Simulation Program Calling Manager Name"]

    @plant_connection_4_simulation_program_calling_manager_name.setter
    def plant_connection_4_simulation_program_calling_manager_name(self, value=None):
        """  Corresponds to IDD Field `plant_connection_4_simulation_program_calling_manager_name`

        Args:
            value (str): value for IDD Field `plant_connection_4_simulation_program_calling_manager_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_connection_4_simulation_program_calling_manager_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_connection_4_simulation_program_calling_manager_name`')

        self._data["Plant Connection 4 Simulation Program Calling Manager Name"] = value

    @property
    def air_connection_inlet_node_name(self):
        """Get air_connection_inlet_node_name

        Returns:
            str: the value of `air_connection_inlet_node_name` or None if not set
        """
        return self._data["Air Connection Inlet Node Name"]

    @air_connection_inlet_node_name.setter
    def air_connection_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_inlet_node_name`
        Inlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `air_connection_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_inlet_node_name`')

        self._data["Air Connection Inlet Node Name"] = value

    @property
    def air_connection_outlet_node_name(self):
        """Get air_connection_outlet_node_name

        Returns:
            str: the value of `air_connection_outlet_node_name` or None if not set
        """
        return self._data["Air Connection Outlet Node Name"]

    @air_connection_outlet_node_name.setter
    def air_connection_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `air_connection_outlet_node_name`
        Outlet air used for heat rejection or air source

        Args:
            value (str): value for IDD Field `air_connection_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `air_connection_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `air_connection_outlet_node_name`')

        self._data["Air Connection Outlet Node Name"] = value

    @property
    def supply_inlet_water_storage_tank_name(self):
        """Get supply_inlet_water_storage_tank_name

        Returns:
            str: the value of `supply_inlet_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Inlet Water Storage Tank Name"]

    @supply_inlet_water_storage_tank_name.setter
    def supply_inlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_inlet_water_storage_tank_name`
        Water use storage tank for alternate source of water consumed by device

        Args:
            value (str): value for IDD Field `supply_inlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_inlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_inlet_water_storage_tank_name`')

        self._data["Supply Inlet Water Storage Tank Name"] = value

    @property
    def collection_outlet_water_storage_tank_name(self):
        """Get collection_outlet_water_storage_tank_name

        Returns:
            str: the value of `collection_outlet_water_storage_tank_name` or None if not set
        """
        return self._data["Collection Outlet Water Storage Tank Name"]

    @collection_outlet_water_storage_tank_name.setter
    def collection_outlet_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `collection_outlet_water_storage_tank_name`
        Water use storage tank for collection of condensate by device

        Args:
            value (str): value for IDD Field `collection_outlet_water_storage_tank_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `collection_outlet_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `collection_outlet_water_storage_tank_name`')

        self._data["Collection Outlet Water Storage Tank Name"] = value

    @property
    def ambient_zone_name(self):
        """Get ambient_zone_name

        Returns:
            str: the value of `ambient_zone_name` or None if not set
        """
        return self._data["Ambient Zone Name"]

    @ambient_zone_name.setter
    def ambient_zone_name(self, value=None):
        """  Corresponds to IDD Field `ambient_zone_name`
        Used for modeling device losses to surrounding zone

        Args:
            value (str): value for IDD Field `ambient_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `ambient_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ambient_zone_name`')

        self._data["Ambient Zone Name"] = value

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

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.main_model_program_calling_manager_name))
        out.append(self._to_str(self.number_of_plant_loop_connections))
        out.append(self._to_str(self.plant_connection_1_inlet_node_name))
        out.append(self._to_str(self.plant_connection_1_outlet_node_name))
        out.append(self._to_str(self.plant_connection_1_loading_mode))
        out.append(self._to_str(self.plant_connection_1_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_1_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_1_simulation_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_2_inlet_node_name))
        out.append(self._to_str(self.plant_connection_2_outlet_node_name))
        out.append(self._to_str(self.plant_connection_2_loading_mode))
        out.append(self._to_str(self.plant_connection_2_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_2_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_2_simulation_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_3_inlet_node_name))
        out.append(self._to_str(self.plant_connection_3_outlet_node_name))
        out.append(self._to_str(self.plant_connection_3_loading_mode))
        out.append(self._to_str(self.plant_connection_3_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_3_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_3_simulation_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_4_inlet_node_name))
        out.append(self._to_str(self.plant_connection_4_outlet_node_name))
        out.append(self._to_str(self.plant_connection_4_loading_mode))
        out.append(self._to_str(self.plant_connection_4_loop_flow_request_mode))
        out.append(self._to_str(self.plant_connection_4_initialization_program_calling_manager_name))
        out.append(self._to_str(self.plant_connection_4_simulation_program_calling_manager_name))
        out.append(self._to_str(self.air_connection_inlet_node_name))
        out.append(self._to_str(self.air_connection_outlet_node_name))
        out.append(self._to_str(self.supply_inlet_water_storage_tank_name))
        out.append(self._to_str(self.collection_outlet_water_storage_tank_name))
        out.append(self._to_str(self.ambient_zone_name))
        return ",".join(out)