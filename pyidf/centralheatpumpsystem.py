from collections import OrderedDict

class CentralHeatPumpSystem(object):
    """ Corresponds to IDD object `CentralHeatPumpSystem`
        This chiller bank can contain multiple chiller heaters and heat pump performance objects.
        Its function is to encapsulate the extra controls needed to turn individual modules on/off
        and whether they are to operate in cooling-only, heating-only or simultaneous cooling/heating
        mode and whether to connect the source water to the evaporator or condenser side.
    """
    internal_name = "CentralHeatPumpSystem"
    field_count = 90

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `CentralHeatPumpSystem`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Control Method"] = None
        self._data["Cooling Loop Inlet Node Name"] = None
        self._data["Cooling Loop Outlet Node Name"] = None
        self._data["Source Loop Inlet Node Name"] = None
        self._data["Source Loop Outlet Node Name"] = None
        self._data["Heating Loop Inlet Node Name"] = None
        self._data["Heating Loop Outlet Node Name"] = None
        self._data["Ancillary Power"] = None
        self._data["Ancillary Operation Schedule Name"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 1"] = None
        self._data["Chiller Heater Modules Performance Component Name 1"] = None
        self._data["Chiller Heater Modules Control Schedule Name 1"] = None
        self._data["Number of Chiller Heater Modules 1"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 2"] = None
        self._data["Chiller Heater Modules Performance Component Name 2"] = None
        self._data["Chiller Heater Modules Control Schedule Name 2"] = None
        self._data["Number of Chiller Heater Modules 2"] = None
        self._data["Chiller Heater Performance Component Object Type 3"] = None
        self._data["Chiller Heater Performance Component Name 3"] = None
        self._data["Chiller Heater Modules Control Schedule Name 3"] = None
        self._data["Number of Chiller Heater Modules 3"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 4"] = None
        self._data["Chiller Heater Modules Performance Component Name 4"] = None
        self._data["Chiller Heater Modules Control Schedule Name 4"] = None
        self._data["Number of Chiller Heater Modules 4"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 5"] = None
        self._data["Chiller Heater Models Performance Component Name 5"] = None
        self._data["Chiller Heater Modules Control Schedule Name 5"] = None
        self._data["Number of Chiller Heater Modules 5"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 6"] = None
        self._data["Chiller Heater Modules Performance Component Name 6"] = None
        self._data["Chiller Heater Modules Control Schedule Name 6"] = None
        self._data["Number of Chiller Heater Modules 6"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 7"] = None
        self._data["Chiller Heater Modules Performance Component Name 7"] = None
        self._data["Chiller Heater Modules Control Schedule Name 7"] = None
        self._data["Number of Chiller Heater Modules 7"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 8"] = None
        self._data["Chiller Heater Modules Performance Component Name 8"] = None
        self._data["Chiller Heater Modules Control Schedule Name 8"] = None
        self._data["Number of Chiller Heater Modules 8"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 9"] = None
        self._data["Chiller Heater Modules Performance Component Name 9"] = None
        self._data["Chiller Heater Modules Control Schedule Name 9"] = None
        self._data["Number of Chiller Heater Modules 9"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 10"] = None
        self._data["Chiller Heater Modules Performance Component Name 10"] = None
        self._data["Chiller Heater Modules Control Schedule Name 10"] = None
        self._data["Number of Chiller Heater Modules 10"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 11"] = None
        self._data["Chiller Heater Modules Performance Component Name 11"] = None
        self._data["Chiller Heater Module Control Schedule Name 11"] = None
        self._data["Number of Chiller Heater Modules 11"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 12"] = None
        self._data["Chiller Heater Modules Performance Component Name 12"] = None
        self._data["Chiller Heater Modules Control Schedule Name 12"] = None
        self._data["Number of Chiller Heater Modules 12"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 13"] = None
        self._data["Chiller Heater Modules Performance Component Name 13"] = None
        self._data["Chiller Heater Modules Control Schedule Name 13"] = None
        self._data["Number of Chiller Heater Modules 13"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 14"] = None
        self._data["Chiller Heater Modules Performance Component Name 14"] = None
        self._data["Chiller Heater Modules Control Schedule Name 14"] = None
        self._data["Number of Chiller Heater Modules 14"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 15"] = None
        self._data["Chiller Heater Modules Performance Component Name 15"] = None
        self._data["Chiller Heater Modules Control Schedule Name 15"] = None
        self._data["Number of Chiller Heater Modules 15"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 16"] = None
        self._data["Chiller Heater Modules Performance Component Name 16"] = None
        self._data["Chiller Heater Modules Control Schedule Name 16"] = None
        self._data["Number of Chiller Heater Modules 16"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 17"] = None
        self._data["Chiller Heater Modules Performance Component Name 17"] = None
        self._data["Chiller Heater Modules Control Schedule Name 17"] = None
        self._data["Number of Chiller Heater Modules 17"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 18"] = None
        self._data["Chiller Heater Modules Performance Component Name 18"] = None
        self._data["Chiller Heater Modules Control Control Schedule Name 18"] = None
        self._data["Number of Chiller Heater Modules 18"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 19"] = None
        self._data["Chiller Heater Modules Performance Component Name 19"] = None
        self._data["Chiller Heater Modules Control Schedule Name 19"] = None
        self._data["Number of Chiller Heater Modules 19"] = None
        self._data["Chiller Heater Modules Performance Component Object Type 20"] = None
        self._data["Chiller Heater Modules Performance Component Name 20"] = None
        self._data["Chiller Heater Modules Control Schedule Name 20"] = None
        self._data["Number of Chiller Heater Modules 20"] = None

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
            self.control_method = None
        else:
            self.control_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_loop_inlet_node_name = None
        else:
            self.cooling_loop_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_loop_outlet_node_name = None
        else:
            self.cooling_loop_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_loop_inlet_node_name = None
        else:
            self.source_loop_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.source_loop_outlet_node_name = None
        else:
            self.source_loop_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_loop_inlet_node_name = None
        else:
            self.heating_loop_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_loop_outlet_node_name = None
        else:
            self.heating_loop_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ancillary_power = None
        else:
            self.ancillary_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ancillary_operation_schedule_name = None
        else:
            self.ancillary_operation_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_1 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_1 = None
        else:
            self.chiller_heater_modules_performance_component_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_1 = None
        else:
            self.chiller_heater_modules_control_schedule_name_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_1 = None
        else:
            self.number_of_chiller_heater_modules_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_2 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_2 = None
        else:
            self.chiller_heater_modules_performance_component_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_2 = None
        else:
            self.chiller_heater_modules_control_schedule_name_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_2 = None
        else:
            self.number_of_chiller_heater_modules_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_performance_component_object_type_3 = None
        else:
            self.chiller_heater_performance_component_object_type_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_performance_component_name_3 = None
        else:
            self.chiller_heater_performance_component_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_3 = None
        else:
            self.chiller_heater_modules_control_schedule_name_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_3 = None
        else:
            self.number_of_chiller_heater_modules_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_4 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_4 = None
        else:
            self.chiller_heater_modules_performance_component_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_4 = None
        else:
            self.chiller_heater_modules_control_schedule_name_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_4 = None
        else:
            self.number_of_chiller_heater_modules_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_5 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_models_performance_component_name_5 = None
        else:
            self.chiller_heater_models_performance_component_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_5 = None
        else:
            self.chiller_heater_modules_control_schedule_name_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_5 = None
        else:
            self.number_of_chiller_heater_modules_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_6 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_6 = None
        else:
            self.chiller_heater_modules_performance_component_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_6 = None
        else:
            self.chiller_heater_modules_control_schedule_name_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_6 = None
        else:
            self.number_of_chiller_heater_modules_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_7 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_7 = None
        else:
            self.chiller_heater_modules_performance_component_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_7 = None
        else:
            self.chiller_heater_modules_control_schedule_name_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_7 = None
        else:
            self.number_of_chiller_heater_modules_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_8 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_8 = None
        else:
            self.chiller_heater_modules_performance_component_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_8 = None
        else:
            self.chiller_heater_modules_control_schedule_name_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_8 = None
        else:
            self.number_of_chiller_heater_modules_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_9 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_9 = None
        else:
            self.chiller_heater_modules_performance_component_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_9 = None
        else:
            self.chiller_heater_modules_control_schedule_name_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_9 = None
        else:
            self.number_of_chiller_heater_modules_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_10 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_10 = None
        else:
            self.chiller_heater_modules_performance_component_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_10 = None
        else:
            self.chiller_heater_modules_control_schedule_name_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_10 = None
        else:
            self.number_of_chiller_heater_modules_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_11 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_11 = None
        else:
            self.chiller_heater_modules_performance_component_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_module_control_schedule_name_11 = None
        else:
            self.chiller_heater_module_control_schedule_name_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_11 = None
        else:
            self.number_of_chiller_heater_modules_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_12 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_12 = None
        else:
            self.chiller_heater_modules_performance_component_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_12 = None
        else:
            self.chiller_heater_modules_control_schedule_name_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_12 = None
        else:
            self.number_of_chiller_heater_modules_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_13 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_13 = None
        else:
            self.chiller_heater_modules_performance_component_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_13 = None
        else:
            self.chiller_heater_modules_control_schedule_name_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_13 = None
        else:
            self.number_of_chiller_heater_modules_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_14 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_14 = None
        else:
            self.chiller_heater_modules_performance_component_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_14 = None
        else:
            self.chiller_heater_modules_control_schedule_name_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_14 = None
        else:
            self.number_of_chiller_heater_modules_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_15 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_15 = None
        else:
            self.chiller_heater_modules_performance_component_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_15 = None
        else:
            self.chiller_heater_modules_control_schedule_name_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_15 = None
        else:
            self.number_of_chiller_heater_modules_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_16 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_16 = None
        else:
            self.chiller_heater_modules_performance_component_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_16 = None
        else:
            self.chiller_heater_modules_control_schedule_name_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_16 = None
        else:
            self.number_of_chiller_heater_modules_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_17 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_17 = None
        else:
            self.chiller_heater_modules_performance_component_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_17 = None
        else:
            self.chiller_heater_modules_control_schedule_name_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_17 = None
        else:
            self.number_of_chiller_heater_modules_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_18 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_18 = None
        else:
            self.chiller_heater_modules_performance_component_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_control_schedule_name_18 = None
        else:
            self.chiller_heater_modules_control_control_schedule_name_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_18 = None
        else:
            self.number_of_chiller_heater_modules_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_19 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_19 = None
        else:
            self.chiller_heater_modules_performance_component_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_19 = None
        else:
            self.chiller_heater_modules_control_schedule_name_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_19 = None
        else:
            self.number_of_chiller_heater_modules_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_object_type_20 = None
        else:
            self.chiller_heater_modules_performance_component_object_type_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_performance_component_name_20 = None
        else:
            self.chiller_heater_modules_performance_component_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.chiller_heater_modules_control_schedule_name_20 = None
        else:
            self.chiller_heater_modules_control_schedule_name_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_chiller_heater_modules_20 = None
        else:
            self.number_of_chiller_heater_modules_20 = vals[i]
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
    def control_method(self):
        """Get control_method

        Returns:
            str: the value of `control_method` or None if not set
        """
        return self._data["Control Method"]

    @control_method.setter
    def control_method(self, value="SmartMixing"):
        """  Corresponds to IDD Field `control_method`

        Args:
            value (str): value for IDD Field `control_method`
                Accepted values are:
                      - SmartMixing
                Default value: SmartMixing
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
                                 'for field `control_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_method`')
            vals = set()
            vals.add("SmartMixing")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `control_method`'.format(value))

        self._data["Control Method"] = value

    @property
    def cooling_loop_inlet_node_name(self):
        """Get cooling_loop_inlet_node_name

        Returns:
            str: the value of `cooling_loop_inlet_node_name` or None if not set
        """
        return self._data["Cooling Loop Inlet Node Name"]

    @cooling_loop_inlet_node_name.setter
    def cooling_loop_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `cooling_loop_inlet_node_name`

        Args:
            value (str): value for IDD Field `cooling_loop_inlet_node_name`
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
                                 'for field `cooling_loop_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_loop_inlet_node_name`')

        self._data["Cooling Loop Inlet Node Name"] = value

    @property
    def cooling_loop_outlet_node_name(self):
        """Get cooling_loop_outlet_node_name

        Returns:
            str: the value of `cooling_loop_outlet_node_name` or None if not set
        """
        return self._data["Cooling Loop Outlet Node Name"]

    @cooling_loop_outlet_node_name.setter
    def cooling_loop_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `cooling_loop_outlet_node_name`

        Args:
            value (str): value for IDD Field `cooling_loop_outlet_node_name`
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
                                 'for field `cooling_loop_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_loop_outlet_node_name`')

        self._data["Cooling Loop Outlet Node Name"] = value

    @property
    def source_loop_inlet_node_name(self):
        """Get source_loop_inlet_node_name

        Returns:
            str: the value of `source_loop_inlet_node_name` or None if not set
        """
        return self._data["Source Loop Inlet Node Name"]

    @source_loop_inlet_node_name.setter
    def source_loop_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_loop_inlet_node_name`

        Args:
            value (str): value for IDD Field `source_loop_inlet_node_name`
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
                                 'for field `source_loop_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_loop_inlet_node_name`')

        self._data["Source Loop Inlet Node Name"] = value

    @property
    def source_loop_outlet_node_name(self):
        """Get source_loop_outlet_node_name

        Returns:
            str: the value of `source_loop_outlet_node_name` or None if not set
        """
        return self._data["Source Loop Outlet Node Name"]

    @source_loop_outlet_node_name.setter
    def source_loop_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `source_loop_outlet_node_name`

        Args:
            value (str): value for IDD Field `source_loop_outlet_node_name`
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
                                 'for field `source_loop_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `source_loop_outlet_node_name`')

        self._data["Source Loop Outlet Node Name"] = value

    @property
    def heating_loop_inlet_node_name(self):
        """Get heating_loop_inlet_node_name

        Returns:
            str: the value of `heating_loop_inlet_node_name` or None if not set
        """
        return self._data["Heating Loop Inlet Node Name"]

    @heating_loop_inlet_node_name.setter
    def heating_loop_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heating_loop_inlet_node_name`

        Args:
            value (str): value for IDD Field `heating_loop_inlet_node_name`
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
                                 'for field `heating_loop_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_loop_inlet_node_name`')

        self._data["Heating Loop Inlet Node Name"] = value

    @property
    def heating_loop_outlet_node_name(self):
        """Get heating_loop_outlet_node_name

        Returns:
            str: the value of `heating_loop_outlet_node_name` or None if not set
        """
        return self._data["Heating Loop Outlet Node Name"]

    @heating_loop_outlet_node_name.setter
    def heating_loop_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `heating_loop_outlet_node_name`

        Args:
            value (str): value for IDD Field `heating_loop_outlet_node_name`
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
                                 'for field `heating_loop_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_loop_outlet_node_name`')

        self._data["Heating Loop Outlet Node Name"] = value

    @property
    def ancillary_power(self):
        """Get ancillary_power

        Returns:
            float: the value of `ancillary_power` or None if not set
        """
        return self._data["Ancillary Power"]

    @ancillary_power.setter
    def ancillary_power(self, value=0.0 ):
        """  Corresponds to IDD Field `ancillary_power`
        Power as demanded from any auxiliary controls

        Args:
            value (float): value for IDD Field `ancillary_power`
                Unit: W
                Default value: 0.0
                value >= 0.0
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
                                 'for field `ancillary_power`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `ancillary_power`')

        self._data["Ancillary Power"] = value

    @property
    def ancillary_operation_schedule_name(self):
        """Get ancillary_operation_schedule_name

        Returns:
            str: the value of `ancillary_operation_schedule_name` or None if not set
        """
        return self._data["Ancillary Operation Schedule Name"]

    @ancillary_operation_schedule_name.setter
    def ancillary_operation_schedule_name(self, value=None):
        """  Corresponds to IDD Field `ancillary_operation_schedule_name`
        This value from this schedule is multiplied times the Ancilliary Power

        Args:
            value (str): value for IDD Field `ancillary_operation_schedule_name`
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
                                 'for field `ancillary_operation_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `ancillary_operation_schedule_name`')

        self._data["Ancillary Operation Schedule Name"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_1(self):
        """Get chiller_heater_modules_performance_component_object_type_1

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_1` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 1"]

    @chiller_heater_modules_performance_component_object_type_1.setter
    def chiller_heater_modules_performance_component_object_type_1(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_1`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_1`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_1`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_1`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 1"] = value

    @property
    def chiller_heater_modules_performance_component_name_1(self):
        """Get chiller_heater_modules_performance_component_name_1

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_1` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 1"]

    @chiller_heater_modules_performance_component_name_1.setter
    def chiller_heater_modules_performance_component_name_1(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_1`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_1`
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
                                 'for field `chiller_heater_modules_performance_component_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_1`')

        self._data["Chiller Heater Modules Performance Component Name 1"] = value

    @property
    def chiller_heater_modules_control_schedule_name_1(self):
        """Get chiller_heater_modules_control_schedule_name_1

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_1` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 1"]

    @chiller_heater_modules_control_schedule_name_1.setter
    def chiller_heater_modules_control_schedule_name_1(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_1`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_1`
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
                                 'for field `chiller_heater_modules_control_schedule_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_1`')

        self._data["Chiller Heater Modules Control Schedule Name 1"] = value

    @property
    def number_of_chiller_heater_modules_1(self):
        """Get number_of_chiller_heater_modules_1

        Returns:
            int: the value of `number_of_chiller_heater_modules_1` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 1"]

    @number_of_chiller_heater_modules_1.setter
    def number_of_chiller_heater_modules_1(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_1`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_1`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_1`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_1`')

        self._data["Number of Chiller Heater Modules 1"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_2(self):
        """Get chiller_heater_modules_performance_component_object_type_2

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_2` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 2"]

    @chiller_heater_modules_performance_component_object_type_2.setter
    def chiller_heater_modules_performance_component_object_type_2(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_2`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_2`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_2`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_2`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 2"] = value

    @property
    def chiller_heater_modules_performance_component_name_2(self):
        """Get chiller_heater_modules_performance_component_name_2

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_2` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 2"]

    @chiller_heater_modules_performance_component_name_2.setter
    def chiller_heater_modules_performance_component_name_2(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_2`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_2`
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
                                 'for field `chiller_heater_modules_performance_component_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_2`')

        self._data["Chiller Heater Modules Performance Component Name 2"] = value

    @property
    def chiller_heater_modules_control_schedule_name_2(self):
        """Get chiller_heater_modules_control_schedule_name_2

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_2` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 2"]

    @chiller_heater_modules_control_schedule_name_2.setter
    def chiller_heater_modules_control_schedule_name_2(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_2`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_2`
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
                                 'for field `chiller_heater_modules_control_schedule_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_2`')

        self._data["Chiller Heater Modules Control Schedule Name 2"] = value

    @property
    def number_of_chiller_heater_modules_2(self):
        """Get number_of_chiller_heater_modules_2

        Returns:
            int: the value of `number_of_chiller_heater_modules_2` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 2"]

    @number_of_chiller_heater_modules_2.setter
    def number_of_chiller_heater_modules_2(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_2`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_2`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_2`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_2`')

        self._data["Number of Chiller Heater Modules 2"] = value

    @property
    def chiller_heater_performance_component_object_type_3(self):
        """Get chiller_heater_performance_component_object_type_3

        Returns:
            str: the value of `chiller_heater_performance_component_object_type_3` or None if not set
        """
        return self._data["Chiller Heater Performance Component Object Type 3"]

    @chiller_heater_performance_component_object_type_3.setter
    def chiller_heater_performance_component_object_type_3(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_performance_component_object_type_3`

        Args:
            value (str): value for IDD Field `chiller_heater_performance_component_object_type_3`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_performance_component_object_type_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_performance_component_object_type_3`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_performance_component_object_type_3`'.format(value))

        self._data["Chiller Heater Performance Component Object Type 3"] = value

    @property
    def chiller_heater_performance_component_name_3(self):
        """Get chiller_heater_performance_component_name_3

        Returns:
            str: the value of `chiller_heater_performance_component_name_3` or None if not set
        """
        return self._data["Chiller Heater Performance Component Name 3"]

    @chiller_heater_performance_component_name_3.setter
    def chiller_heater_performance_component_name_3(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_performance_component_name_3`

        Args:
            value (str): value for IDD Field `chiller_heater_performance_component_name_3`
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
                                 'for field `chiller_heater_performance_component_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_performance_component_name_3`')

        self._data["Chiller Heater Performance Component Name 3"] = value

    @property
    def chiller_heater_modules_control_schedule_name_3(self):
        """Get chiller_heater_modules_control_schedule_name_3

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_3` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 3"]

    @chiller_heater_modules_control_schedule_name_3.setter
    def chiller_heater_modules_control_schedule_name_3(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_3`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_3`
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
                                 'for field `chiller_heater_modules_control_schedule_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_3`')

        self._data["Chiller Heater Modules Control Schedule Name 3"] = value

    @property
    def number_of_chiller_heater_modules_3(self):
        """Get number_of_chiller_heater_modules_3

        Returns:
            int: the value of `number_of_chiller_heater_modules_3` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 3"]

    @number_of_chiller_heater_modules_3.setter
    def number_of_chiller_heater_modules_3(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_3`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_3`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_3`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_3`')

        self._data["Number of Chiller Heater Modules 3"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_4(self):
        """Get chiller_heater_modules_performance_component_object_type_4

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_4` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 4"]

    @chiller_heater_modules_performance_component_object_type_4.setter
    def chiller_heater_modules_performance_component_object_type_4(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_4`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_4`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_4`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_4`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 4"] = value

    @property
    def chiller_heater_modules_performance_component_name_4(self):
        """Get chiller_heater_modules_performance_component_name_4

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_4` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 4"]

    @chiller_heater_modules_performance_component_name_4.setter
    def chiller_heater_modules_performance_component_name_4(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_4`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_4`
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
                                 'for field `chiller_heater_modules_performance_component_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_4`')

        self._data["Chiller Heater Modules Performance Component Name 4"] = value

    @property
    def chiller_heater_modules_control_schedule_name_4(self):
        """Get chiller_heater_modules_control_schedule_name_4

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_4` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 4"]

    @chiller_heater_modules_control_schedule_name_4.setter
    def chiller_heater_modules_control_schedule_name_4(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_4`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_4`
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
                                 'for field `chiller_heater_modules_control_schedule_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_4`')

        self._data["Chiller Heater Modules Control Schedule Name 4"] = value

    @property
    def number_of_chiller_heater_modules_4(self):
        """Get number_of_chiller_heater_modules_4

        Returns:
            int: the value of `number_of_chiller_heater_modules_4` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 4"]

    @number_of_chiller_heater_modules_4.setter
    def number_of_chiller_heater_modules_4(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_4`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_4`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_4`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_4`')

        self._data["Number of Chiller Heater Modules 4"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_5(self):
        """Get chiller_heater_modules_performance_component_object_type_5

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_5` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 5"]

    @chiller_heater_modules_performance_component_object_type_5.setter
    def chiller_heater_modules_performance_component_object_type_5(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_5`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_5`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_5`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_5`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 5"] = value

    @property
    def chiller_heater_models_performance_component_name_5(self):
        """Get chiller_heater_models_performance_component_name_5

        Returns:
            str: the value of `chiller_heater_models_performance_component_name_5` or None if not set
        """
        return self._data["Chiller Heater Models Performance Component Name 5"]

    @chiller_heater_models_performance_component_name_5.setter
    def chiller_heater_models_performance_component_name_5(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_models_performance_component_name_5`

        Args:
            value (str): value for IDD Field `chiller_heater_models_performance_component_name_5`
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
                                 'for field `chiller_heater_models_performance_component_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_models_performance_component_name_5`')

        self._data["Chiller Heater Models Performance Component Name 5"] = value

    @property
    def chiller_heater_modules_control_schedule_name_5(self):
        """Get chiller_heater_modules_control_schedule_name_5

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_5` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 5"]

    @chiller_heater_modules_control_schedule_name_5.setter
    def chiller_heater_modules_control_schedule_name_5(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_5`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_5`
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
                                 'for field `chiller_heater_modules_control_schedule_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_5`')

        self._data["Chiller Heater Modules Control Schedule Name 5"] = value

    @property
    def number_of_chiller_heater_modules_5(self):
        """Get number_of_chiller_heater_modules_5

        Returns:
            int: the value of `number_of_chiller_heater_modules_5` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 5"]

    @number_of_chiller_heater_modules_5.setter
    def number_of_chiller_heater_modules_5(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_5`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_5`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_5`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_5`')

        self._data["Number of Chiller Heater Modules 5"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_6(self):
        """Get chiller_heater_modules_performance_component_object_type_6

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_6` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 6"]

    @chiller_heater_modules_performance_component_object_type_6.setter
    def chiller_heater_modules_performance_component_object_type_6(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_6`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_6`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_6`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_6`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 6"] = value

    @property
    def chiller_heater_modules_performance_component_name_6(self):
        """Get chiller_heater_modules_performance_component_name_6

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_6` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 6"]

    @chiller_heater_modules_performance_component_name_6.setter
    def chiller_heater_modules_performance_component_name_6(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_6`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_6`
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
                                 'for field `chiller_heater_modules_performance_component_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_6`')

        self._data["Chiller Heater Modules Performance Component Name 6"] = value

    @property
    def chiller_heater_modules_control_schedule_name_6(self):
        """Get chiller_heater_modules_control_schedule_name_6

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_6` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 6"]

    @chiller_heater_modules_control_schedule_name_6.setter
    def chiller_heater_modules_control_schedule_name_6(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_6`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_6`
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
                                 'for field `chiller_heater_modules_control_schedule_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_6`')

        self._data["Chiller Heater Modules Control Schedule Name 6"] = value

    @property
    def number_of_chiller_heater_modules_6(self):
        """Get number_of_chiller_heater_modules_6

        Returns:
            int: the value of `number_of_chiller_heater_modules_6` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 6"]

    @number_of_chiller_heater_modules_6.setter
    def number_of_chiller_heater_modules_6(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_6`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_6`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_6`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_6`')

        self._data["Number of Chiller Heater Modules 6"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_7(self):
        """Get chiller_heater_modules_performance_component_object_type_7

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_7` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 7"]

    @chiller_heater_modules_performance_component_object_type_7.setter
    def chiller_heater_modules_performance_component_object_type_7(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_7`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_7`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_7`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_7`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 7"] = value

    @property
    def chiller_heater_modules_performance_component_name_7(self):
        """Get chiller_heater_modules_performance_component_name_7

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_7` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 7"]

    @chiller_heater_modules_performance_component_name_7.setter
    def chiller_heater_modules_performance_component_name_7(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_7`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_7`
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
                                 'for field `chiller_heater_modules_performance_component_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_7`')

        self._data["Chiller Heater Modules Performance Component Name 7"] = value

    @property
    def chiller_heater_modules_control_schedule_name_7(self):
        """Get chiller_heater_modules_control_schedule_name_7

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_7` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 7"]

    @chiller_heater_modules_control_schedule_name_7.setter
    def chiller_heater_modules_control_schedule_name_7(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_7`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_7`
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
                                 'for field `chiller_heater_modules_control_schedule_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_7`')

        self._data["Chiller Heater Modules Control Schedule Name 7"] = value

    @property
    def number_of_chiller_heater_modules_7(self):
        """Get number_of_chiller_heater_modules_7

        Returns:
            int: the value of `number_of_chiller_heater_modules_7` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 7"]

    @number_of_chiller_heater_modules_7.setter
    def number_of_chiller_heater_modules_7(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_7`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_7`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_7`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_7`')

        self._data["Number of Chiller Heater Modules 7"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_8(self):
        """Get chiller_heater_modules_performance_component_object_type_8

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_8` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 8"]

    @chiller_heater_modules_performance_component_object_type_8.setter
    def chiller_heater_modules_performance_component_object_type_8(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_8`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_8`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_8`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_8`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 8"] = value

    @property
    def chiller_heater_modules_performance_component_name_8(self):
        """Get chiller_heater_modules_performance_component_name_8

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_8` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 8"]

    @chiller_heater_modules_performance_component_name_8.setter
    def chiller_heater_modules_performance_component_name_8(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_8`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_8`
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
                                 'for field `chiller_heater_modules_performance_component_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_8`')

        self._data["Chiller Heater Modules Performance Component Name 8"] = value

    @property
    def chiller_heater_modules_control_schedule_name_8(self):
        """Get chiller_heater_modules_control_schedule_name_8

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_8` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 8"]

    @chiller_heater_modules_control_schedule_name_8.setter
    def chiller_heater_modules_control_schedule_name_8(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_8`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_8`
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
                                 'for field `chiller_heater_modules_control_schedule_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_8`')

        self._data["Chiller Heater Modules Control Schedule Name 8"] = value

    @property
    def number_of_chiller_heater_modules_8(self):
        """Get number_of_chiller_heater_modules_8

        Returns:
            int: the value of `number_of_chiller_heater_modules_8` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 8"]

    @number_of_chiller_heater_modules_8.setter
    def number_of_chiller_heater_modules_8(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_8`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_8`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_8`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_8`')

        self._data["Number of Chiller Heater Modules 8"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_9(self):
        """Get chiller_heater_modules_performance_component_object_type_9

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_9` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 9"]

    @chiller_heater_modules_performance_component_object_type_9.setter
    def chiller_heater_modules_performance_component_object_type_9(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_9`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_9`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_9`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_9`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 9"] = value

    @property
    def chiller_heater_modules_performance_component_name_9(self):
        """Get chiller_heater_modules_performance_component_name_9

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_9` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 9"]

    @chiller_heater_modules_performance_component_name_9.setter
    def chiller_heater_modules_performance_component_name_9(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_9`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_9`
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
                                 'for field `chiller_heater_modules_performance_component_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_9`')

        self._data["Chiller Heater Modules Performance Component Name 9"] = value

    @property
    def chiller_heater_modules_control_schedule_name_9(self):
        """Get chiller_heater_modules_control_schedule_name_9

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_9` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 9"]

    @chiller_heater_modules_control_schedule_name_9.setter
    def chiller_heater_modules_control_schedule_name_9(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_9`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_9`
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
                                 'for field `chiller_heater_modules_control_schedule_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_9`')

        self._data["Chiller Heater Modules Control Schedule Name 9"] = value

    @property
    def number_of_chiller_heater_modules_9(self):
        """Get number_of_chiller_heater_modules_9

        Returns:
            int: the value of `number_of_chiller_heater_modules_9` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 9"]

    @number_of_chiller_heater_modules_9.setter
    def number_of_chiller_heater_modules_9(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_9`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_9`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_9`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_9`')

        self._data["Number of Chiller Heater Modules 9"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_10(self):
        """Get chiller_heater_modules_performance_component_object_type_10

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_10` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 10"]

    @chiller_heater_modules_performance_component_object_type_10.setter
    def chiller_heater_modules_performance_component_object_type_10(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_10`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_10`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_10`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_10`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 10"] = value

    @property
    def chiller_heater_modules_performance_component_name_10(self):
        """Get chiller_heater_modules_performance_component_name_10

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_10` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 10"]

    @chiller_heater_modules_performance_component_name_10.setter
    def chiller_heater_modules_performance_component_name_10(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_10`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_10`
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
                                 'for field `chiller_heater_modules_performance_component_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_10`')

        self._data["Chiller Heater Modules Performance Component Name 10"] = value

    @property
    def chiller_heater_modules_control_schedule_name_10(self):
        """Get chiller_heater_modules_control_schedule_name_10

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_10` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 10"]

    @chiller_heater_modules_control_schedule_name_10.setter
    def chiller_heater_modules_control_schedule_name_10(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_10`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_10`
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
                                 'for field `chiller_heater_modules_control_schedule_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_10`')

        self._data["Chiller Heater Modules Control Schedule Name 10"] = value

    @property
    def number_of_chiller_heater_modules_10(self):
        """Get number_of_chiller_heater_modules_10

        Returns:
            int: the value of `number_of_chiller_heater_modules_10` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 10"]

    @number_of_chiller_heater_modules_10.setter
    def number_of_chiller_heater_modules_10(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_10`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_10`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_10`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_10`')

        self._data["Number of Chiller Heater Modules 10"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_11(self):
        """Get chiller_heater_modules_performance_component_object_type_11

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_11` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 11"]

    @chiller_heater_modules_performance_component_object_type_11.setter
    def chiller_heater_modules_performance_component_object_type_11(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_11`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_11`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_11`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_11`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 11"] = value

    @property
    def chiller_heater_modules_performance_component_name_11(self):
        """Get chiller_heater_modules_performance_component_name_11

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_11` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 11"]

    @chiller_heater_modules_performance_component_name_11.setter
    def chiller_heater_modules_performance_component_name_11(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_11`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_11`
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
                                 'for field `chiller_heater_modules_performance_component_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_11`')

        self._data["Chiller Heater Modules Performance Component Name 11"] = value

    @property
    def chiller_heater_module_control_schedule_name_11(self):
        """Get chiller_heater_module_control_schedule_name_11

        Returns:
            str: the value of `chiller_heater_module_control_schedule_name_11` or None if not set
        """
        return self._data["Chiller Heater Module Control Schedule Name 11"]

    @chiller_heater_module_control_schedule_name_11.setter
    def chiller_heater_module_control_schedule_name_11(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_module_control_schedule_name_11`

        Args:
            value (str): value for IDD Field `chiller_heater_module_control_schedule_name_11`
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
                                 'for field `chiller_heater_module_control_schedule_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_module_control_schedule_name_11`')

        self._data["Chiller Heater Module Control Schedule Name 11"] = value

    @property
    def number_of_chiller_heater_modules_11(self):
        """Get number_of_chiller_heater_modules_11

        Returns:
            int: the value of `number_of_chiller_heater_modules_11` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 11"]

    @number_of_chiller_heater_modules_11.setter
    def number_of_chiller_heater_modules_11(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_11`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_11`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_11`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_11`')

        self._data["Number of Chiller Heater Modules 11"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_12(self):
        """Get chiller_heater_modules_performance_component_object_type_12

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_12` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 12"]

    @chiller_heater_modules_performance_component_object_type_12.setter
    def chiller_heater_modules_performance_component_object_type_12(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_12`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_12`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_12`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_12`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 12"] = value

    @property
    def chiller_heater_modules_performance_component_name_12(self):
        """Get chiller_heater_modules_performance_component_name_12

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_12` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 12"]

    @chiller_heater_modules_performance_component_name_12.setter
    def chiller_heater_modules_performance_component_name_12(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_12`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_12`
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
                                 'for field `chiller_heater_modules_performance_component_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_12`')

        self._data["Chiller Heater Modules Performance Component Name 12"] = value

    @property
    def chiller_heater_modules_control_schedule_name_12(self):
        """Get chiller_heater_modules_control_schedule_name_12

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_12` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 12"]

    @chiller_heater_modules_control_schedule_name_12.setter
    def chiller_heater_modules_control_schedule_name_12(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_12`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_12`
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
                                 'for field `chiller_heater_modules_control_schedule_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_12`')

        self._data["Chiller Heater Modules Control Schedule Name 12"] = value

    @property
    def number_of_chiller_heater_modules_12(self):
        """Get number_of_chiller_heater_modules_12

        Returns:
            int: the value of `number_of_chiller_heater_modules_12` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 12"]

    @number_of_chiller_heater_modules_12.setter
    def number_of_chiller_heater_modules_12(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_12`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_12`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_12`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_12`')

        self._data["Number of Chiller Heater Modules 12"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_13(self):
        """Get chiller_heater_modules_performance_component_object_type_13

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_13` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 13"]

    @chiller_heater_modules_performance_component_object_type_13.setter
    def chiller_heater_modules_performance_component_object_type_13(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_13`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_13`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_13`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_13`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 13"] = value

    @property
    def chiller_heater_modules_performance_component_name_13(self):
        """Get chiller_heater_modules_performance_component_name_13

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_13` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 13"]

    @chiller_heater_modules_performance_component_name_13.setter
    def chiller_heater_modules_performance_component_name_13(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_13`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_13`
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
                                 'for field `chiller_heater_modules_performance_component_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_13`')

        self._data["Chiller Heater Modules Performance Component Name 13"] = value

    @property
    def chiller_heater_modules_control_schedule_name_13(self):
        """Get chiller_heater_modules_control_schedule_name_13

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_13` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 13"]

    @chiller_heater_modules_control_schedule_name_13.setter
    def chiller_heater_modules_control_schedule_name_13(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_13`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_13`
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
                                 'for field `chiller_heater_modules_control_schedule_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_13`')

        self._data["Chiller Heater Modules Control Schedule Name 13"] = value

    @property
    def number_of_chiller_heater_modules_13(self):
        """Get number_of_chiller_heater_modules_13

        Returns:
            int: the value of `number_of_chiller_heater_modules_13` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 13"]

    @number_of_chiller_heater_modules_13.setter
    def number_of_chiller_heater_modules_13(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_13`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_13`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_13`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_13`')

        self._data["Number of Chiller Heater Modules 13"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_14(self):
        """Get chiller_heater_modules_performance_component_object_type_14

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_14` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 14"]

    @chiller_heater_modules_performance_component_object_type_14.setter
    def chiller_heater_modules_performance_component_object_type_14(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_14`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_14`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_14`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_14`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 14"] = value

    @property
    def chiller_heater_modules_performance_component_name_14(self):
        """Get chiller_heater_modules_performance_component_name_14

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_14` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 14"]

    @chiller_heater_modules_performance_component_name_14.setter
    def chiller_heater_modules_performance_component_name_14(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_14`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_14`
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
                                 'for field `chiller_heater_modules_performance_component_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_14`')

        self._data["Chiller Heater Modules Performance Component Name 14"] = value

    @property
    def chiller_heater_modules_control_schedule_name_14(self):
        """Get chiller_heater_modules_control_schedule_name_14

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_14` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 14"]

    @chiller_heater_modules_control_schedule_name_14.setter
    def chiller_heater_modules_control_schedule_name_14(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_14`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_14`
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
                                 'for field `chiller_heater_modules_control_schedule_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_14`')

        self._data["Chiller Heater Modules Control Schedule Name 14"] = value

    @property
    def number_of_chiller_heater_modules_14(self):
        """Get number_of_chiller_heater_modules_14

        Returns:
            int: the value of `number_of_chiller_heater_modules_14` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 14"]

    @number_of_chiller_heater_modules_14.setter
    def number_of_chiller_heater_modules_14(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_14`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_14`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_14`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_14`')

        self._data["Number of Chiller Heater Modules 14"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_15(self):
        """Get chiller_heater_modules_performance_component_object_type_15

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_15` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 15"]

    @chiller_heater_modules_performance_component_object_type_15.setter
    def chiller_heater_modules_performance_component_object_type_15(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_15`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_15`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_15`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_15`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 15"] = value

    @property
    def chiller_heater_modules_performance_component_name_15(self):
        """Get chiller_heater_modules_performance_component_name_15

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_15` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 15"]

    @chiller_heater_modules_performance_component_name_15.setter
    def chiller_heater_modules_performance_component_name_15(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_15`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_15`
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
                                 'for field `chiller_heater_modules_performance_component_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_15`')

        self._data["Chiller Heater Modules Performance Component Name 15"] = value

    @property
    def chiller_heater_modules_control_schedule_name_15(self):
        """Get chiller_heater_modules_control_schedule_name_15

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_15` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 15"]

    @chiller_heater_modules_control_schedule_name_15.setter
    def chiller_heater_modules_control_schedule_name_15(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_15`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_15`
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
                                 'for field `chiller_heater_modules_control_schedule_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_15`')

        self._data["Chiller Heater Modules Control Schedule Name 15"] = value

    @property
    def number_of_chiller_heater_modules_15(self):
        """Get number_of_chiller_heater_modules_15

        Returns:
            int: the value of `number_of_chiller_heater_modules_15` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 15"]

    @number_of_chiller_heater_modules_15.setter
    def number_of_chiller_heater_modules_15(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_15`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_15`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_15`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_15`')

        self._data["Number of Chiller Heater Modules 15"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_16(self):
        """Get chiller_heater_modules_performance_component_object_type_16

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_16` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 16"]

    @chiller_heater_modules_performance_component_object_type_16.setter
    def chiller_heater_modules_performance_component_object_type_16(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_16`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_16`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_16`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_16`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 16"] = value

    @property
    def chiller_heater_modules_performance_component_name_16(self):
        """Get chiller_heater_modules_performance_component_name_16

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_16` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 16"]

    @chiller_heater_modules_performance_component_name_16.setter
    def chiller_heater_modules_performance_component_name_16(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_16`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_16`
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
                                 'for field `chiller_heater_modules_performance_component_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_16`')

        self._data["Chiller Heater Modules Performance Component Name 16"] = value

    @property
    def chiller_heater_modules_control_schedule_name_16(self):
        """Get chiller_heater_modules_control_schedule_name_16

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_16` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 16"]

    @chiller_heater_modules_control_schedule_name_16.setter
    def chiller_heater_modules_control_schedule_name_16(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_16`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_16`
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
                                 'for field `chiller_heater_modules_control_schedule_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_16`')

        self._data["Chiller Heater Modules Control Schedule Name 16"] = value

    @property
    def number_of_chiller_heater_modules_16(self):
        """Get number_of_chiller_heater_modules_16

        Returns:
            int: the value of `number_of_chiller_heater_modules_16` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 16"]

    @number_of_chiller_heater_modules_16.setter
    def number_of_chiller_heater_modules_16(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_16`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_16`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_16`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_16`')

        self._data["Number of Chiller Heater Modules 16"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_17(self):
        """Get chiller_heater_modules_performance_component_object_type_17

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_17` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 17"]

    @chiller_heater_modules_performance_component_object_type_17.setter
    def chiller_heater_modules_performance_component_object_type_17(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_17`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_17`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_17`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_17`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 17"] = value

    @property
    def chiller_heater_modules_performance_component_name_17(self):
        """Get chiller_heater_modules_performance_component_name_17

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_17` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 17"]

    @chiller_heater_modules_performance_component_name_17.setter
    def chiller_heater_modules_performance_component_name_17(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_17`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_17`
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
                                 'for field `chiller_heater_modules_performance_component_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_17`')

        self._data["Chiller Heater Modules Performance Component Name 17"] = value

    @property
    def chiller_heater_modules_control_schedule_name_17(self):
        """Get chiller_heater_modules_control_schedule_name_17

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_17` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 17"]

    @chiller_heater_modules_control_schedule_name_17.setter
    def chiller_heater_modules_control_schedule_name_17(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_17`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_17`
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
                                 'for field `chiller_heater_modules_control_schedule_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_17`')

        self._data["Chiller Heater Modules Control Schedule Name 17"] = value

    @property
    def number_of_chiller_heater_modules_17(self):
        """Get number_of_chiller_heater_modules_17

        Returns:
            int: the value of `number_of_chiller_heater_modules_17` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 17"]

    @number_of_chiller_heater_modules_17.setter
    def number_of_chiller_heater_modules_17(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_17`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_17`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_17`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_17`')

        self._data["Number of Chiller Heater Modules 17"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_18(self):
        """Get chiller_heater_modules_performance_component_object_type_18

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_18` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 18"]

    @chiller_heater_modules_performance_component_object_type_18.setter
    def chiller_heater_modules_performance_component_object_type_18(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_18`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_18`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_18`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_18`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 18"] = value

    @property
    def chiller_heater_modules_performance_component_name_18(self):
        """Get chiller_heater_modules_performance_component_name_18

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_18` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 18"]

    @chiller_heater_modules_performance_component_name_18.setter
    def chiller_heater_modules_performance_component_name_18(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_18`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_18`
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
                                 'for field `chiller_heater_modules_performance_component_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_18`')

        self._data["Chiller Heater Modules Performance Component Name 18"] = value

    @property
    def chiller_heater_modules_control_control_schedule_name_18(self):
        """Get chiller_heater_modules_control_control_schedule_name_18

        Returns:
            str: the value of `chiller_heater_modules_control_control_schedule_name_18` or None if not set
        """
        return self._data["Chiller Heater Modules Control Control Schedule Name 18"]

    @chiller_heater_modules_control_control_schedule_name_18.setter
    def chiller_heater_modules_control_control_schedule_name_18(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_control_schedule_name_18`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_control_schedule_name_18`
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
                                 'for field `chiller_heater_modules_control_control_schedule_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_control_schedule_name_18`')

        self._data["Chiller Heater Modules Control Control Schedule Name 18"] = value

    @property
    def number_of_chiller_heater_modules_18(self):
        """Get number_of_chiller_heater_modules_18

        Returns:
            int: the value of `number_of_chiller_heater_modules_18` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 18"]

    @number_of_chiller_heater_modules_18.setter
    def number_of_chiller_heater_modules_18(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_18`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_18`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_18`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_18`')

        self._data["Number of Chiller Heater Modules 18"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_19(self):
        """Get chiller_heater_modules_performance_component_object_type_19

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_19` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 19"]

    @chiller_heater_modules_performance_component_object_type_19.setter
    def chiller_heater_modules_performance_component_object_type_19(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_19`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_19`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_19`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_19`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 19"] = value

    @property
    def chiller_heater_modules_performance_component_name_19(self):
        """Get chiller_heater_modules_performance_component_name_19

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_19` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 19"]

    @chiller_heater_modules_performance_component_name_19.setter
    def chiller_heater_modules_performance_component_name_19(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_19`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_19`
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
                                 'for field `chiller_heater_modules_performance_component_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_19`')

        self._data["Chiller Heater Modules Performance Component Name 19"] = value

    @property
    def chiller_heater_modules_control_schedule_name_19(self):
        """Get chiller_heater_modules_control_schedule_name_19

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_19` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 19"]

    @chiller_heater_modules_control_schedule_name_19.setter
    def chiller_heater_modules_control_schedule_name_19(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_19`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_19`
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
                                 'for field `chiller_heater_modules_control_schedule_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_19`')

        self._data["Chiller Heater Modules Control Schedule Name 19"] = value

    @property
    def number_of_chiller_heater_modules_19(self):
        """Get number_of_chiller_heater_modules_19

        Returns:
            int: the value of `number_of_chiller_heater_modules_19` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 19"]

    @number_of_chiller_heater_modules_19.setter
    def number_of_chiller_heater_modules_19(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_19`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_19`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_19`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_19`')

        self._data["Number of Chiller Heater Modules 19"] = value

    @property
    def chiller_heater_modules_performance_component_object_type_20(self):
        """Get chiller_heater_modules_performance_component_object_type_20

        Returns:
            str: the value of `chiller_heater_modules_performance_component_object_type_20` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Object Type 20"]

    @chiller_heater_modules_performance_component_object_type_20.setter
    def chiller_heater_modules_performance_component_object_type_20(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_object_type_20`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_object_type_20`
                Accepted values are:
                      - ChillerHeaterPerformance:Electric:EIR
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
                                 'for field `chiller_heater_modules_performance_component_object_type_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_object_type_20`')
            vals = set()
            vals.add("ChillerHeaterPerformance:Electric:EIR")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `chiller_heater_modules_performance_component_object_type_20`'.format(value))

        self._data["Chiller Heater Modules Performance Component Object Type 20"] = value

    @property
    def chiller_heater_modules_performance_component_name_20(self):
        """Get chiller_heater_modules_performance_component_name_20

        Returns:
            str: the value of `chiller_heater_modules_performance_component_name_20` or None if not set
        """
        return self._data["Chiller Heater Modules Performance Component Name 20"]

    @chiller_heater_modules_performance_component_name_20.setter
    def chiller_heater_modules_performance_component_name_20(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_performance_component_name_20`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_performance_component_name_20`
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
                                 'for field `chiller_heater_modules_performance_component_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_performance_component_name_20`')

        self._data["Chiller Heater Modules Performance Component Name 20"] = value

    @property
    def chiller_heater_modules_control_schedule_name_20(self):
        """Get chiller_heater_modules_control_schedule_name_20

        Returns:
            str: the value of `chiller_heater_modules_control_schedule_name_20` or None if not set
        """
        return self._data["Chiller Heater Modules Control Schedule Name 20"]

    @chiller_heater_modules_control_schedule_name_20.setter
    def chiller_heater_modules_control_schedule_name_20(self, value=None):
        """  Corresponds to IDD Field `chiller_heater_modules_control_schedule_name_20`

        Args:
            value (str): value for IDD Field `chiller_heater_modules_control_schedule_name_20`
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
                                 'for field `chiller_heater_modules_control_schedule_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `chiller_heater_modules_control_schedule_name_20`')

        self._data["Chiller Heater Modules Control Schedule Name 20"] = value

    @property
    def number_of_chiller_heater_modules_20(self):
        """Get number_of_chiller_heater_modules_20

        Returns:
            int: the value of `number_of_chiller_heater_modules_20` or None if not set
        """
        return self._data["Number of Chiller Heater Modules 20"]

    @number_of_chiller_heater_modules_20.setter
    def number_of_chiller_heater_modules_20(self, value=1 ):
        """  Corresponds to IDD Field `number_of_chiller_heater_modules_20`

        Args:
            value (int): value for IDD Field `number_of_chiller_heater_modules_20`
                Default value: 1
                value >= 1
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
                                 'for field `number_of_chiller_heater_modules_20`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_chiller_heater_modules_20`')

        self._data["Number of Chiller Heater Modules 20"] = value

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
        out.append(self._to_str(self.control_method))
        out.append(self._to_str(self.cooling_loop_inlet_node_name))
        out.append(self._to_str(self.cooling_loop_outlet_node_name))
        out.append(self._to_str(self.source_loop_inlet_node_name))
        out.append(self._to_str(self.source_loop_outlet_node_name))
        out.append(self._to_str(self.heating_loop_inlet_node_name))
        out.append(self._to_str(self.heating_loop_outlet_node_name))
        out.append(self._to_str(self.ancillary_power))
        out.append(self._to_str(self.ancillary_operation_schedule_name))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_1))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_1))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_1))
        out.append(self._to_str(self.number_of_chiller_heater_modules_1))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_2))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_2))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_2))
        out.append(self._to_str(self.number_of_chiller_heater_modules_2))
        out.append(self._to_str(self.chiller_heater_performance_component_object_type_3))
        out.append(self._to_str(self.chiller_heater_performance_component_name_3))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_3))
        out.append(self._to_str(self.number_of_chiller_heater_modules_3))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_4))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_4))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_4))
        out.append(self._to_str(self.number_of_chiller_heater_modules_4))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_5))
        out.append(self._to_str(self.chiller_heater_models_performance_component_name_5))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_5))
        out.append(self._to_str(self.number_of_chiller_heater_modules_5))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_6))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_6))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_6))
        out.append(self._to_str(self.number_of_chiller_heater_modules_6))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_7))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_7))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_7))
        out.append(self._to_str(self.number_of_chiller_heater_modules_7))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_8))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_8))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_8))
        out.append(self._to_str(self.number_of_chiller_heater_modules_8))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_9))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_9))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_9))
        out.append(self._to_str(self.number_of_chiller_heater_modules_9))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_10))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_10))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_10))
        out.append(self._to_str(self.number_of_chiller_heater_modules_10))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_11))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_11))
        out.append(self._to_str(self.chiller_heater_module_control_schedule_name_11))
        out.append(self._to_str(self.number_of_chiller_heater_modules_11))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_12))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_12))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_12))
        out.append(self._to_str(self.number_of_chiller_heater_modules_12))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_13))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_13))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_13))
        out.append(self._to_str(self.number_of_chiller_heater_modules_13))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_14))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_14))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_14))
        out.append(self._to_str(self.number_of_chiller_heater_modules_14))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_15))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_15))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_15))
        out.append(self._to_str(self.number_of_chiller_heater_modules_15))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_16))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_16))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_16))
        out.append(self._to_str(self.number_of_chiller_heater_modules_16))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_17))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_17))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_17))
        out.append(self._to_str(self.number_of_chiller_heater_modules_17))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_18))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_18))
        out.append(self._to_str(self.chiller_heater_modules_control_control_schedule_name_18))
        out.append(self._to_str(self.number_of_chiller_heater_modules_18))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_19))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_19))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_19))
        out.append(self._to_str(self.number_of_chiller_heater_modules_19))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_object_type_20))
        out.append(self._to_str(self.chiller_heater_modules_performance_component_name_20))
        out.append(self._to_str(self.chiller_heater_modules_control_schedule_name_20))
        out.append(self._to_str(self.number_of_chiller_heater_modules_20))
        return ",".join(out)