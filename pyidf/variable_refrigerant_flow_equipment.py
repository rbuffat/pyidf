from collections import OrderedDict

class AirConditionerVariableRefrigerantFlow(object):
    """ Corresponds to IDD object `AirConditioner:VariableRefrigerantFlow`
        Variable refrigerant flow (VRF) air-to-air heat pump condensing unit (includes one
        or more electric compressors and outdoor fan). Serves one or more VRF zone terminal
        units. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and ZoneTerminalUnitList.
    
    """
    internal_name = "AirConditioner:VariableRefrigerantFlow"
    field_count = 81
    required_fields = ["Heat Pump Name", "Zone Terminal Unit List Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `AirConditioner:VariableRefrigerantFlow`
        """
        self._data = OrderedDict()
        self._data["Heat Pump Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Gross Rated Total Cooling Capacity"] = None
        self._data["Gross Rated Cooling COP"] = None
        self._data["Minimum Outdoor Temperature in Cooling Mode"] = None
        self._data["Maximum Outdoor Temperature in Cooling Mode"] = None
        self._data["Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name"] = None
        self._data["Cooling Capacity Ratio Boundary Curve Name"] = None
        self._data["Cooling Capacity Ratio Modifier Function of High Temperature Curve Name"] = None
        self._data["Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name"] = None
        self._data["Cooling Energy Input Ratio Boundary Curve Name"] = None
        self._data["Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name"] = None
        self._data["Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"] = None
        self._data["Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"] = None
        self._data["Cooling Combination Ratio Correction Factor Curve Name"] = None
        self._data["Cooling Part-Load Fraction Correlation Curve Name"] = None
        self._data["Gross Rated Heating Capacity"] = None
        self._data["Rated Heating Capacity Sizing Ratio"] = None
        self._data["Gross Rated Heating COP"] = None
        self._data["Minimum Outdoor Temperature in Heating Mode"] = None
        self._data["Maximum Outdoor Temperature in Heating Mode"] = None
        self._data["Heating Capacity Ratio Modifier Function of Low Temperature Curve Name"] = None
        self._data["Heating Capacity Ratio Boundary Curve Name"] = None
        self._data["Heating Capacity Ratio Modifier Function of High Temperature Curve Name"] = None
        self._data["Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name"] = None
        self._data["Heating Energy Input Ratio Boundary Curve Name"] = None
        self._data["Heating Energy Input Ratio Modifier Function of High Temperature Curve Name"] = None
        self._data["Heating Performance Curve Outdoor Temperature Type"] = None
        self._data["Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"] = None
        self._data["Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"] = None
        self._data["Heating Combination Ratio Correction Factor Curve Name"] = None
        self._data["Heating Part-Load Fraction Correlation Curve Name"] = None
        self._data["Minimum Heat Pump Part-Load Ratio"] = None
        self._data["Zone Name for Master Thermostat Location"] = None
        self._data["Master Thermostat Priority Control Type"] = None
        self._data["Thermostat Priority Schedule Name"] = None
        self._data["Zone Terminal Unit List Name"] = None
        self._data["Heat Pump Waste Heat Recovery"] = None
        self._data["Equivalent Piping Length used for Piping Correction Factor in Cooling Mode"] = None
        self._data["Vertical Height used for Piping Correction Factor"] = None
        self._data["Piping Correction Factor for Length in Cooling Mode Curve Name"] = None
        self._data["Piping Correction Factor for Height in Cooling Mode Coefficient"] = None
        self._data["Equivalent Piping Length used for Piping Correction Factor in Heating Mode"] = None
        self._data["Piping Correction Factor for Length in Heating Mode Curve Name"] = None
        self._data["Piping Correction Factor for Height in Heating Mode Coefficient"] = None
        self._data["Crankcase Heater Power per Compressor"] = None
        self._data["Number of Compressors"] = None
        self._data["Ratio of Compressor Size to Total Compressor Capacity"] = None
        self._data["Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"] = None
        self._data["Defrost Strategy"] = None
        self._data["Defrost Control"] = None
        self._data["Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"] = None
        self._data["Defrost Time Period Fraction"] = None
        self._data["Resistive Defrost Heater Capacity"] = None
        self._data["Maximum Outdoor Dry-bulb Temperature for Defrost Operation"] = None
        self._data["Condenser Type"] = None
        self._data["Condenser Inlet Node Name"] = None
        self._data["Condenser Outlet Node Name"] = None
        self._data["Water Condenser Volume Flow Rate"] = None
        self._data["Evaporative Condenser Effectiveness"] = None
        self._data["Evaporative Condenser Air Flow Rate"] = None
        self._data["Evaporative Condenser Pump Rated Power Consumption"] = None
        self._data["Supply Water Storage Tank Name"] = None
        self._data["Basin Heater Capacity"] = None
        self._data["Basin Heater Setpoint Temperature"] = None
        self._data["Basin Heater Operating Schedule Name"] = None
        self._data["Fuel Type"] = None
        self._data["Minimum Outdoor Temperature in Heat Recovery Mode"] = None
        self._data["Maximum Outdoor Temperature in Heat Recovery Mode"] = None
        self._data["Heat Recovery Cooling Capacity Modifier Curve Name"] = None
        self._data["Initial Heat Recovery Cooling Capacity Fraction"] = None
        self._data["Heat Recovery Cooling Capacity Time Constant"] = None
        self._data["Heat Recovery Cooling Energy Modifier Curve Name"] = None
        self._data["Initial Heat Recovery Cooling Energy Fraction"] = None
        self._data["Heat Recovery Cooling Energy Time Constant"] = None
        self._data["Heat Recovery Heating Capacity Modifier Curve Name"] = None
        self._data["Initial Heat Recovery Heating Capacity Fraction"] = None
        self._data["Heat Recovery Heating Capacity Time Constant"] = None
        self._data["Heat Recovery Heating Energy Modifier Curve Name"] = None
        self._data["Initial Heat Recovery Heating Energy Fraction"] = None
        self._data["Heat Recovery Heating Energy Time Constant"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.heat_pump_name = None
        else:
            self.heat_pump_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gross_rated_total_cooling_capacity = None
        else:
            self.gross_rated_total_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gross_rated_cooling_cop = None
        else:
            self.gross_rated_cooling_cop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_in_cooling_mode = None
        else:
            self.minimum_outdoor_temperature_in_cooling_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_in_cooling_mode = None
        else:
            self.maximum_outdoor_temperature_in_cooling_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name = None
        else:
            self.cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_capacity_ratio_boundary_curve_name = None
        else:
            self.cooling_capacity_ratio_boundary_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name = None
        else:
            self.cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name = None
        else:
            self.cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_energy_input_ratio_boundary_curve_name = None
        else:
            self.cooling_energy_input_ratio_boundary_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name = None
        else:
            self.cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = None
        else:
            self.cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = None
        else:
            self.cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_combination_ratio_correction_factor_curve_name = None
        else:
            self.cooling_combination_ratio_correction_factor_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_partload_fraction_correlation_curve_name = None
        else:
            self.cooling_partload_fraction_correlation_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gross_rated_heating_capacity = None
        else:
            self.gross_rated_heating_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.rated_heating_capacity_sizing_ratio = None
        else:
            self.rated_heating_capacity_sizing_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.gross_rated_heating_cop = None
        else:
            self.gross_rated_heating_cop = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_in_heating_mode = None
        else:
            self.minimum_outdoor_temperature_in_heating_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_in_heating_mode = None
        else:
            self.maximum_outdoor_temperature_in_heating_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_capacity_ratio_modifier_function_of_low_temperature_curve_name = None
        else:
            self.heating_capacity_ratio_modifier_function_of_low_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_capacity_ratio_boundary_curve_name = None
        else:
            self.heating_capacity_ratio_boundary_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_capacity_ratio_modifier_function_of_high_temperature_curve_name = None
        else:
            self.heating_capacity_ratio_modifier_function_of_high_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name = None
        else:
            self.heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_energy_input_ratio_boundary_curve_name = None
        else:
            self.heating_energy_input_ratio_boundary_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name = None
        else:
            self.heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_performance_curve_outdoor_temperature_type = None
        else:
            self.heating_performance_curve_outdoor_temperature_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = None
        else:
            self.heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = None
        else:
            self.heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_combination_ratio_correction_factor_curve_name = None
        else:
            self.heating_combination_ratio_correction_factor_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_partload_fraction_correlation_curve_name = None
        else:
            self.heating_partload_fraction_correlation_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_heat_pump_partload_ratio = None
        else:
            self.minimum_heat_pump_partload_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_name_for_master_thermostat_location = None
        else:
            self.zone_name_for_master_thermostat_location = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.master_thermostat_priority_control_type = None
        else:
            self.master_thermostat_priority_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermostat_priority_schedule_name = None
        else:
            self.thermostat_priority_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_list_name = None
        else:
            self.zone_terminal_unit_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_pump_waste_heat_recovery = None
        else:
            self.heat_pump_waste_heat_recovery = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode = None
        else:
            self.equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.vertical_height_used_for_piping_correction_factor = None
        else:
            self.vertical_height_used_for_piping_correction_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.piping_correction_factor_for_length_in_cooling_mode_curve_name = None
        else:
            self.piping_correction_factor_for_length_in_cooling_mode_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.piping_correction_factor_for_height_in_cooling_mode_coefficient = None
        else:
            self.piping_correction_factor_for_height_in_cooling_mode_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode = None
        else:
            self.equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.piping_correction_factor_for_length_in_heating_mode_curve_name = None
        else:
            self.piping_correction_factor_for_length_in_heating_mode_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.piping_correction_factor_for_height_in_heating_mode_coefficient = None
        else:
            self.piping_correction_factor_for_height_in_heating_mode_coefficient = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.crankcase_heater_power_per_compressor = None
        else:
            self.crankcase_heater_power_per_compressor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_compressors = None
        else:
            self.number_of_compressors = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.ratio_of_compressor_size_to_total_compressor_capacity = None
        else:
            self.ratio_of_compressor_size_to_total_compressor_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_crankcase_heater = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_crankcase_heater = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_strategy = None
        else:
            self.defrost_strategy = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_control = None
        else:
            self.defrost_control = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_energy_input_ratio_modifier_function_of_temperature_curve_name = None
        else:
            self.defrost_energy_input_ratio_modifier_function_of_temperature_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.defrost_time_period_fraction = None
        else:
            self.defrost_time_period_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.resistive_defrost_heater_capacity = None
        else:
            self.resistive_defrost_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_drybulb_temperature_for_defrost_operation = None
        else:
            self.maximum_outdoor_drybulb_temperature_for_defrost_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_type = None
        else:
            self.condenser_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_inlet_node_name = None
        else:
            self.condenser_inlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.condenser_outlet_node_name = None
        else:
            self.condenser_outlet_node_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.water_condenser_volume_flow_rate = None
        else:
            self.water_condenser_volume_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_effectiveness = None
        else:
            self.evaporative_condenser_effectiveness = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_air_flow_rate = None
        else:
            self.evaporative_condenser_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.evaporative_condenser_pump_rated_power_consumption = None
        else:
            self.evaporative_condenser_pump_rated_power_consumption = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_water_storage_tank_name = None
        else:
            self.supply_water_storage_tank_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_capacity = None
        else:
            self.basin_heater_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_setpoint_temperature = None
        else:
            self.basin_heater_setpoint_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.basin_heater_operating_schedule_name = None
        else:
            self.basin_heater_operating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fuel_type = None
        else:
            self.fuel_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_outdoor_temperature_in_heat_recovery_mode = None
        else:
            self.minimum_outdoor_temperature_in_heat_recovery_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_outdoor_temperature_in_heat_recovery_mode = None
        else:
            self.maximum_outdoor_temperature_in_heat_recovery_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_cooling_capacity_modifier_curve_name = None
        else:
            self.heat_recovery_cooling_capacity_modifier_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_heat_recovery_cooling_capacity_fraction = None
        else:
            self.initial_heat_recovery_cooling_capacity_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_cooling_capacity_time_constant = None
        else:
            self.heat_recovery_cooling_capacity_time_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_cooling_energy_modifier_curve_name = None
        else:
            self.heat_recovery_cooling_energy_modifier_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_heat_recovery_cooling_energy_fraction = None
        else:
            self.initial_heat_recovery_cooling_energy_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_cooling_energy_time_constant = None
        else:
            self.heat_recovery_cooling_energy_time_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_heating_capacity_modifier_curve_name = None
        else:
            self.heat_recovery_heating_capacity_modifier_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_heat_recovery_heating_capacity_fraction = None
        else:
            self.initial_heat_recovery_heating_capacity_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_heating_capacity_time_constant = None
        else:
            self.heat_recovery_heating_capacity_time_constant = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_heating_energy_modifier_curve_name = None
        else:
            self.heat_recovery_heating_energy_modifier_curve_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.initial_heat_recovery_heating_energy_fraction = None
        else:
            self.initial_heat_recovery_heating_energy_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heat_recovery_heating_energy_time_constant = None
        else:
            self.heat_recovery_heating_energy_time_constant = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def heat_pump_name(self):
        """Get heat_pump_name

        Returns:
            str: the value of `heat_pump_name` or None if not set
        """
        return self._data["Heat Pump Name"]

    @heat_pump_name.setter
    def heat_pump_name(self, value=None):
        """  Corresponds to IDD Field `heat_pump_name`
        Enter a unique name for this variable refrigerant flow heat pump.

        Args:
            value (str): value for IDD Field `heat_pump_name`
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
                                 'for field `heat_pump_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_pump_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_pump_name`')

        self._data["Heat Pump Name"] = value

    @property
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.
        Enter the name of a schedule that defines the availability of the unit.
        Schedule values of 0 denote the unit is off. All other values denote the unit is available.
        If this field is left blank, the unit is available the entire simulation.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
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
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def gross_rated_total_cooling_capacity(self):
        """Get gross_rated_total_cooling_capacity

        Returns:
            float: the value of `gross_rated_total_cooling_capacity` or None if not set
        """
        return self._data["Gross Rated Total Cooling Capacity"]

    @gross_rated_total_cooling_capacity.setter
    def gross_rated_total_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `gross_rated_total_cooling_capacity`
        Enter the total cooling capacity in watts at rated conditions or set to autosize.
        Total cooling capacity not accounting for the effect of supply air fan heat

        Args:
            value (float): value for IDD Field `gross_rated_total_cooling_capacity`
                Units: W
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
                                 'for field `gross_rated_total_cooling_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gross_rated_total_cooling_capacity`')

        self._data["Gross Rated Total Cooling Capacity"] = value

    @property
    def gross_rated_cooling_cop(self):
        """Get gross_rated_cooling_cop

        Returns:
            float: the value of `gross_rated_cooling_cop` or None if not set
        """
        return self._data["Gross Rated Cooling COP"]

    @gross_rated_cooling_cop.setter
    def gross_rated_cooling_cop(self, value=3.3 ):
        """  Corresponds to IDD Field `gross_rated_cooling_cop`
        Enter the coefficient of performance at rated conditions or leave blank to use default.
        COP includes compressor and condenser fan electrical energy input
        COP does not include supply fan heat or supply fan electric power input

        Args:
            value (float): value for IDD Field `gross_rated_cooling_cop`
                Units: W/W
                Default value: 3.3
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
                                 'for field `gross_rated_cooling_cop`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gross_rated_cooling_cop`')

        self._data["Gross Rated Cooling COP"] = value

    @property
    def minimum_outdoor_temperature_in_cooling_mode(self):
        """Get minimum_outdoor_temperature_in_cooling_mode

        Returns:
            float: the value of `minimum_outdoor_temperature_in_cooling_mode` or None if not set
        """
        return self._data["Minimum Outdoor Temperature in Cooling Mode"]

    @minimum_outdoor_temperature_in_cooling_mode.setter
    def minimum_outdoor_temperature_in_cooling_mode(self, value=-6.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_temperature_in_cooling_mode`
        Enter the minimum outdoor temperature allowed for cooling operation.
        Cooling is disabled below this temperature.

        Args:
            value (float): value for IDD Field `minimum_outdoor_temperature_in_cooling_mode`
                Units: C
                Default value: -6.0
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
                                 'for field `minimum_outdoor_temperature_in_cooling_mode`'.format(value))

        self._data["Minimum Outdoor Temperature in Cooling Mode"] = value

    @property
    def maximum_outdoor_temperature_in_cooling_mode(self):
        """Get maximum_outdoor_temperature_in_cooling_mode

        Returns:
            float: the value of `maximum_outdoor_temperature_in_cooling_mode` or None if not set
        """
        return self._data["Maximum Outdoor Temperature in Cooling Mode"]

    @maximum_outdoor_temperature_in_cooling_mode.setter
    def maximum_outdoor_temperature_in_cooling_mode(self, value=43.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_temperature_in_cooling_mode`
        Enter the maximum outdoor temperature allowed for cooling operation.
        Cooling is disabled above this temperature.

        Args:
            value (float): value for IDD Field `maximum_outdoor_temperature_in_cooling_mode`
                Units: C
                Default value: 43.0
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
                                 'for field `maximum_outdoor_temperature_in_cooling_mode`'.format(value))

        self._data["Maximum Outdoor Temperature in Cooling Mode"] = value

    @property
    def cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name(self):
        """Get cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name

        Returns:
            str: the value of `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name"]

    @cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name.setter
    def cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter a curve name that represents full load cooling capacity ratio as a
        function of outdoor dry-bulb temperature and indoor wet-bulb temperature.
        Up to two curves are allowed if the performance cannot be represented by a single curve.
        The following two fields are used if two curves are required.

        Args:
            value (str): value for IDD Field `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name`
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
                                 'for field `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name`')

        self._data["Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def cooling_capacity_ratio_boundary_curve_name(self):
        """Get cooling_capacity_ratio_boundary_curve_name

        Returns:
            str: the value of `cooling_capacity_ratio_boundary_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Ratio Boundary Curve Name"]

    @cooling_capacity_ratio_boundary_curve_name.setter
    def cooling_capacity_ratio_boundary_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_ratio_boundary_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve object is used to allow separate low and high cooling capacity ratio
        performance curves. This curve represents a line passing through the points where
        performance changes. The curve calculates outdoor dry-bulb temperature given weighted
        average indoor wet-bulb temperature. If a single performance curve is used,
        leave this field blank.

        Args:
            value (str): value for IDD Field `cooling_capacity_ratio_boundary_curve_name`
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
                                 'for field `cooling_capacity_ratio_boundary_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_ratio_boundary_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_capacity_ratio_boundary_curve_name`')

        self._data["Cooling Capacity Ratio Boundary Curve Name"] = value

    @property
    def cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name(self):
        """Get cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name

        Returns:
            str: the value of `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Capacity Ratio Modifier Function of High Temperature Curve Name"]

    @cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name.setter
    def cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        This curve object is used to describe the high outdoor temperature
        performance curve used to describe cooling capacity ratio.
        This curve is used when a single performance curve does not accurately describe
        cooling capacity ratio as a function of temperature.
        If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name`
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
                                 'for field `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name`')

        self._data["Cooling Capacity Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name(self):
        """Get cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter a curve name that represents cooling energy ratio as a function of
        outdoor dry-bulb temperature and indoor wet-bulb temperature

        Args:
            value (str): value for IDD Field `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name`
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
                                 'for field `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name`')

        self._data["Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def cooling_energy_input_ratio_boundary_curve_name(self):
        """Get cooling_energy_input_ratio_boundary_curve_name

        Returns:
            str: the value of `cooling_energy_input_ratio_boundary_curve_name` or None if not set
        """
        return self._data["Cooling Energy Input Ratio Boundary Curve Name"]

    @cooling_energy_input_ratio_boundary_curve_name.setter
    def cooling_energy_input_ratio_boundary_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_energy_input_ratio_boundary_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve object is used to allow separate low and high cooling energy input ratio
        performance curves. This curve represents a line passing through the points where
        performance changes. The curve calculates outdoor dry-bulb temperature given weighted
        average indoor wet-bulb temperature. If a single performance curve is used,
        leave this field blank.

        Args:
            value (str): value for IDD Field `cooling_energy_input_ratio_boundary_curve_name`
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
                                 'for field `cooling_energy_input_ratio_boundary_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_energy_input_ratio_boundary_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_energy_input_ratio_boundary_curve_name`')

        self._data["Cooling Energy Input Ratio Boundary Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name(self):
        """Get cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name` or None if not set
        """
        return self._data["Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        This curve object is used to describe the high outdoor temperature
        performance curve used to describe cooling energy ratio.
        This curve is used when a single performance curve does not accurately describe
        cooling energy ratio as a function of temperature

        Args:
            value (str): value for IDD Field `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name`
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
                                 'for field `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name`')

        self._data["Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(self):
        """Get cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name` or None if not set
        """
        return self._data["Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`
        Table:OneIndependentVariable object can also be used
        Enter a curve name that represents cooling energy ratio as a function of
        part-load ratio for part-load ratios less than or equal to 1.
        If this field is left blank, the model assumes energy is proportional to
        part-load ratio.

        Args:
            value (str): value for IDD Field `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`
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
                                 'for field `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`')

        self._data["Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(self):
        """Get cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name` or None if not set
        """
        return self._data["Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`
        Table:OneIndependentVariable object can also be used
        Enter a curve name that represents cooling energy ratio as a function of
        part-load ratio for part-load ratios greater than 1. Part-load ratios
        can exceed 1 in variable speed compresson systems.
        If this field is left blank, the model assumes energy is proportional to
        part-load ratio.

        Args:
            value (str): value for IDD Field `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`
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
                                 'for field `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`')

        self._data["Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"] = value

    @property
    def cooling_combination_ratio_correction_factor_curve_name(self):
        """Get cooling_combination_ratio_correction_factor_curve_name

        Returns:
            str: the value of `cooling_combination_ratio_correction_factor_curve_name` or None if not set
        """
        return self._data["Cooling Combination Ratio Correction Factor Curve Name"]

    @cooling_combination_ratio_correction_factor_curve_name.setter
    def cooling_combination_ratio_correction_factor_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_combination_ratio_correction_factor_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve defines how rated capacity changes when the total indoor terminal unit cooling
        capacity is greater than the Gross Rated Total Cooling Capacity defined in this object.
        If this field is left blank, the model assumes total indoor terminal unit cooling
        capacity is equal to the Gross Rated Total Cooling Capacity defined above.

        Args:
            value (str): value for IDD Field `cooling_combination_ratio_correction_factor_curve_name`
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
                                 'for field `cooling_combination_ratio_correction_factor_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_combination_ratio_correction_factor_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_combination_ratio_correction_factor_curve_name`')

        self._data["Cooling Combination Ratio Correction Factor Curve Name"] = value

    @property
    def cooling_partload_fraction_correlation_curve_name(self):
        """Get cooling_partload_fraction_correlation_curve_name

        Returns:
            str: the value of `cooling_partload_fraction_correlation_curve_name` or None if not set
        """
        return self._data["Cooling Part-Load Fraction Correlation Curve Name"]

    @cooling_partload_fraction_correlation_curve_name.setter
    def cooling_partload_fraction_correlation_curve_name(self, value=None):
        """  Corresponds to IDD Field `cooling_partload_fraction_correlation_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve defines the cycling losses when the heat pump compressor cycles on and off
        below the Minimum Heat Pump Part-Load Ratio specified in the field below.

        Args:
            value (str): value for IDD Field `cooling_partload_fraction_correlation_curve_name`
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
                                 'for field `cooling_partload_fraction_correlation_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_partload_fraction_correlation_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_partload_fraction_correlation_curve_name`')

        self._data["Cooling Part-Load Fraction Correlation Curve Name"] = value

    @property
    def gross_rated_heating_capacity(self):
        """Get gross_rated_heating_capacity

        Returns:
            float: the value of `gross_rated_heating_capacity` or None if not set
        """
        return self._data["Gross Rated Heating Capacity"]

    @gross_rated_heating_capacity.setter
    def gross_rated_heating_capacity(self, value=None):
        """  Corresponds to IDD Field `gross_rated_heating_capacity`
        Enter the heating capacity in watts at rated conditions or set to autosize.
        Heating capacity not accounting for the effect of supply air fan heat

        Args:
            value (float): value for IDD Field `gross_rated_heating_capacity`
                Units: W
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
                                 'for field `gross_rated_heating_capacity`'.format(value))

        self._data["Gross Rated Heating Capacity"] = value

    @property
    def rated_heating_capacity_sizing_ratio(self):
        """Get rated_heating_capacity_sizing_ratio

        Returns:
            float: the value of `rated_heating_capacity_sizing_ratio` or None if not set
        """
        return self._data["Rated Heating Capacity Sizing Ratio"]

    @rated_heating_capacity_sizing_ratio.setter
    def rated_heating_capacity_sizing_ratio(self, value=1.0 ):
        """  Corresponds to IDD Field `rated_heating_capacity_sizing_ratio`
        If the Gross Rated Heating Capacity is autosized, the heating capacity is sized
        to be equal to the cooling capacity multiplied by this sizing ratio. The zone
        terminal unit heating coils are also sized using this ratio unless the sizing
        ratio input in the ZoneHVAC:TerminalUnit:VariableRefrigerantFlow object is entered.

        Args:
            value (float): value for IDD Field `rated_heating_capacity_sizing_ratio`
                Units: W/W
                Default value: 1.0
                value >= 1.0
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
                                 'for field `rated_heating_capacity_sizing_ratio`'.format(value))
            if value < 1.0:
                raise ValueError('value need to be greater or equal 1.0 '
                                 'for field `rated_heating_capacity_sizing_ratio`')

        self._data["Rated Heating Capacity Sizing Ratio"] = value

    @property
    def gross_rated_heating_cop(self):
        """Get gross_rated_heating_cop

        Returns:
            float: the value of `gross_rated_heating_cop` or None if not set
        """
        return self._data["Gross Rated Heating COP"]

    @gross_rated_heating_cop.setter
    def gross_rated_heating_cop(self, value=3.4 ):
        """  Corresponds to IDD Field `gross_rated_heating_cop`
        COP includes compressor and condenser fan electrical energy input
        COP does not include supply fan heat or supply fan electrical energy input

        Args:
            value (float): value for IDD Field `gross_rated_heating_cop`
                Units: W/W
                Default value: 3.4
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
                                 'for field `gross_rated_heating_cop`'.format(value))

        self._data["Gross Rated Heating COP"] = value

    @property
    def minimum_outdoor_temperature_in_heating_mode(self):
        """Get minimum_outdoor_temperature_in_heating_mode

        Returns:
            float: the value of `minimum_outdoor_temperature_in_heating_mode` or None if not set
        """
        return self._data["Minimum Outdoor Temperature in Heating Mode"]

    @minimum_outdoor_temperature_in_heating_mode.setter
    def minimum_outdoor_temperature_in_heating_mode(self, value=-20.0 ):
        """  Corresponds to IDD Field `minimum_outdoor_temperature_in_heating_mode`
        Enter the minimum outdoor temperature allowed for cooling operation.

        Args:
            value (float): value for IDD Field `minimum_outdoor_temperature_in_heating_mode`
                Units: C
                Default value: -20.0
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
                                 'for field `minimum_outdoor_temperature_in_heating_mode`'.format(value))

        self._data["Minimum Outdoor Temperature in Heating Mode"] = value

    @property
    def maximum_outdoor_temperature_in_heating_mode(self):
        """Get maximum_outdoor_temperature_in_heating_mode

        Returns:
            float: the value of `maximum_outdoor_temperature_in_heating_mode` or None if not set
        """
        return self._data["Maximum Outdoor Temperature in Heating Mode"]

    @maximum_outdoor_temperature_in_heating_mode.setter
    def maximum_outdoor_temperature_in_heating_mode(self, value=16.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_temperature_in_heating_mode`
        Enter the maximum outdoor temperature allowed for heating operation.

        Args:
            value (float): value for IDD Field `maximum_outdoor_temperature_in_heating_mode`
                Units: C
                Default value: 16.0
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
                                 'for field `maximum_outdoor_temperature_in_heating_mode`'.format(value))

        self._data["Maximum Outdoor Temperature in Heating Mode"] = value

    @property
    def heating_capacity_ratio_modifier_function_of_low_temperature_curve_name(self):
        """Get heating_capacity_ratio_modifier_function_of_low_temperature_curve_name

        Returns:
            str: the value of `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name` or None if not set
        """
        return self._data["Heating Capacity Ratio Modifier Function of Low Temperature Curve Name"]

    @heating_capacity_ratio_modifier_function_of_low_temperature_curve_name.setter
    def heating_capacity_ratio_modifier_function_of_low_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter a curve name that represents full load heating capacity ratio as a
        function of outdoor wet-bulb temperature and indoor dry-bulb temperature.
        Outdoor dry-bulb temperature may be used if wet-bulb temperature data is unavailable.
        See Heating Performance Curve Outdoor Temperature Type input below to determine which
        outdoor temperature type to use.
        Up to two curves are allowed if the performance cannot be represented by a single curve.
        The following two fields are used if two curves are required.

        Args:
            value (str): value for IDD Field `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name`
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
                                 'for field `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name`')

        self._data["Heating Capacity Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def heating_capacity_ratio_boundary_curve_name(self):
        """Get heating_capacity_ratio_boundary_curve_name

        Returns:
            str: the value of `heating_capacity_ratio_boundary_curve_name` or None if not set
        """
        return self._data["Heating Capacity Ratio Boundary Curve Name"]

    @heating_capacity_ratio_boundary_curve_name.setter
    def heating_capacity_ratio_boundary_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_ratio_boundary_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve object is used to allow separate low and high heating capacity ratio
        performance curves. This curve represents a line passing through the points where
        performance changes. The curve calculates outdoor dry-bulb or wet-bulb temperature
        given weighted average indoor dry-bulb temperature. See Heating Performance Curve
        Outdoor Temperature Type input below to determine which outdoor temperature type to use.
        If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `heating_capacity_ratio_boundary_curve_name`
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
                                 'for field `heating_capacity_ratio_boundary_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_capacity_ratio_boundary_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_capacity_ratio_boundary_curve_name`')

        self._data["Heating Capacity Ratio Boundary Curve Name"] = value

    @property
    def heating_capacity_ratio_modifier_function_of_high_temperature_curve_name(self):
        """Get heating_capacity_ratio_modifier_function_of_high_temperature_curve_name

        Returns:
            str: the value of `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name` or None if not set
        """
        return self._data["Heating Capacity Ratio Modifier Function of High Temperature Curve Name"]

    @heating_capacity_ratio_modifier_function_of_high_temperature_curve_name.setter
    def heating_capacity_ratio_modifier_function_of_high_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        This curve object is used to describe the high outdoor temperature
        performance curve used to describe heating capacity ratio.
        This curve is used when a single performance curve does not accurately describe
        heating capacity ratio as a function of temperature.
        If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name`
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
                                 'for field `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name`')

        self._data["Heating Capacity Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name(self):
        """Get heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name` or None if not set
        """
        return self._data["Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter a curve name that represents heating energy ratio as a function of
        outdoor wet-bulb temperature and indoor dry-bulb temperature
        Outdoor dry-bulb temperature may be used if wet-bulb temperature data is unavailable.
        See Heating Performance Curve Outdoor Temperature Type input below to determine which
        outdoor temperature type to use.

        Args:
            value (str): value for IDD Field `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name`
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
                                 'for field `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name`')

        self._data["Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def heating_energy_input_ratio_boundary_curve_name(self):
        """Get heating_energy_input_ratio_boundary_curve_name

        Returns:
            str: the value of `heating_energy_input_ratio_boundary_curve_name` or None if not set
        """
        return self._data["Heating Energy Input Ratio Boundary Curve Name"]

    @heating_energy_input_ratio_boundary_curve_name.setter
    def heating_energy_input_ratio_boundary_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_energy_input_ratio_boundary_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve object is used to allow separate low and high heating energy input ratio
        performance curves. This curve represents a line passing through the points where
        performance changes. The curve calculates outdoor dry-bulb or wet-bulb temperature
        given weighted average indoor dry-bulb temperature. See Heating Performance Curve
        Outdoor Temperature Type input below to determine which outdoor temperature type to use.
        If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `heating_energy_input_ratio_boundary_curve_name`
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
                                 'for field `heating_energy_input_ratio_boundary_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_energy_input_ratio_boundary_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_energy_input_ratio_boundary_curve_name`')

        self._data["Heating Energy Input Ratio Boundary Curve Name"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name(self):
        """Get heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name` or None if not set
        """
        return self._data["Heating Energy Input Ratio Modifier Function of High Temperature Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        This curve object is used to allow separate performance curves for heating energy.
        If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name`
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
                                 'for field `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name`')

        self._data["Heating Energy Input Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def heating_performance_curve_outdoor_temperature_type(self):
        """Get heating_performance_curve_outdoor_temperature_type

        Returns:
            str: the value of `heating_performance_curve_outdoor_temperature_type` or None if not set
        """
        return self._data["Heating Performance Curve Outdoor Temperature Type"]

    @heating_performance_curve_outdoor_temperature_type.setter
    def heating_performance_curve_outdoor_temperature_type(self, value="WetBulbTemperature"):
        """  Corresponds to IDD Field `heating_performance_curve_outdoor_temperature_type`
        Determines temperature type for heating capacity curves and heating energy curves.
        This input determines whether the outdoor air dry-bulb or wet-bulb temperature
        is used to evaluate these curves.

        Args:
            value (str): value for IDD Field `heating_performance_curve_outdoor_temperature_type`
                Accepted values are:
                      - DryBulbTemperature
                      - WetBulbTemperature
                Default value: WetBulbTemperature
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
                                 'for field `heating_performance_curve_outdoor_temperature_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_performance_curve_outdoor_temperature_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_performance_curve_outdoor_temperature_type`')
            vals = {}
            vals["drybulbtemperature"] = "DryBulbTemperature"
            vals["wetbulbtemperature"] = "WetBulbTemperature"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heating_performance_curve_outdoor_temperature_type`'.format(value))
            value = vals[value_lower]

        self._data["Heating Performance Curve Outdoor Temperature Type"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(self):
        """Get heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name` or None if not set
        """
        return self._data["Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve represents the heating energy input ratio for part-load ratios less than 1.

        Args:
            value (str): value for IDD Field `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`
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
                                 'for field `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name`')

        self._data["Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(self):
        """Get heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name` or None if not set
        """
        return self._data["Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve represents the heating energy input ratio for part-load ratios greater than 1.

        Args:
            value (str): value for IDD Field `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`
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
                                 'for field `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name`')

        self._data["Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"] = value

    @property
    def heating_combination_ratio_correction_factor_curve_name(self):
        """Get heating_combination_ratio_correction_factor_curve_name

        Returns:
            str: the value of `heating_combination_ratio_correction_factor_curve_name` or None if not set
        """
        return self._data["Heating Combination Ratio Correction Factor Curve Name"]

    @heating_combination_ratio_correction_factor_curve_name.setter
    def heating_combination_ratio_correction_factor_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_combination_ratio_correction_factor_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve defines how rated capacity changes when the total indoor terminal unit heating
        capacity is greater than the Gross Rated Heating Capacity defined in this object.
        If this field is left blank, the model assumes total indoor terminal unit heating
        capacity is equal to the Gross Rated Heating Capacity defined above.

        Args:
            value (str): value for IDD Field `heating_combination_ratio_correction_factor_curve_name`
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
                                 'for field `heating_combination_ratio_correction_factor_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_combination_ratio_correction_factor_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_combination_ratio_correction_factor_curve_name`')

        self._data["Heating Combination Ratio Correction Factor Curve Name"] = value

    @property
    def heating_partload_fraction_correlation_curve_name(self):
        """Get heating_partload_fraction_correlation_curve_name

        Returns:
            str: the value of `heating_partload_fraction_correlation_curve_name` or None if not set
        """
        return self._data["Heating Part-Load Fraction Correlation Curve Name"]

    @heating_partload_fraction_correlation_curve_name.setter
    def heating_partload_fraction_correlation_curve_name(self, value=None):
        """  Corresponds to IDD Field `heating_partload_fraction_correlation_curve_name`
        Table:OneIndependentVariable object can also be used
        This curve defines the cycling losses when the heat pump compressor cycles on and off
        below the Minimum Heat Pump Part-Load Ratio specified in the following field.

        Args:
            value (str): value for IDD Field `heating_partload_fraction_correlation_curve_name`
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
                                 'for field `heating_partload_fraction_correlation_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_partload_fraction_correlation_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_partload_fraction_correlation_curve_name`')

        self._data["Heating Part-Load Fraction Correlation Curve Name"] = value

    @property
    def minimum_heat_pump_partload_ratio(self):
        """Get minimum_heat_pump_partload_ratio

        Returns:
            float: the value of `minimum_heat_pump_partload_ratio` or None if not set
        """
        return self._data["Minimum Heat Pump Part-Load Ratio"]

    @minimum_heat_pump_partload_ratio.setter
    def minimum_heat_pump_partload_ratio(self, value=0.15 ):
        """  Corresponds to IDD Field `minimum_heat_pump_partload_ratio`
        Enter the minimum heat pump part-load ratio (PLR). When the cooling or heating PLR is
        below this value, the heat pump compressor will cycle to meet the cooling or heating
        demand.

        Args:
            value (float): value for IDD Field `minimum_heat_pump_partload_ratio`
                Units: dimensionless
                Default value: 0.15
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
                                 'for field `minimum_heat_pump_partload_ratio`'.format(value))

        self._data["Minimum Heat Pump Part-Load Ratio"] = value

    @property
    def zone_name_for_master_thermostat_location(self):
        """Get zone_name_for_master_thermostat_location

        Returns:
            str: the value of `zone_name_for_master_thermostat_location` or None if not set
        """
        return self._data["Zone Name for Master Thermostat Location"]

    @zone_name_for_master_thermostat_location.setter
    def zone_name_for_master_thermostat_location(self, value=None):
        """  Corresponds to IDD Field `zone_name_for_master_thermostat_location`
        Enter the name of the zone where the master thermostat is located.

        Args:
            value (str): value for IDD Field `zone_name_for_master_thermostat_location`
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
                                 'for field `zone_name_for_master_thermostat_location`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name_for_master_thermostat_location`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name_for_master_thermostat_location`')

        self._data["Zone Name for Master Thermostat Location"] = value

    @property
    def master_thermostat_priority_control_type(self):
        """Get master_thermostat_priority_control_type

        Returns:
            str: the value of `master_thermostat_priority_control_type` or None if not set
        """
        return self._data["Master Thermostat Priority Control Type"]

    @master_thermostat_priority_control_type.setter
    def master_thermostat_priority_control_type(self, value="MasterThermostatPriority"):
        """  Corresponds to IDD Field `master_thermostat_priority_control_type`
        Choose a thermostat control logic scheme. If these control types fail to control zone
        temperature within a reasonable limit, consider using multiple VRF systems

        Args:
            value (str): value for IDD Field `master_thermostat_priority_control_type`
                Accepted values are:
                      - LoadPriority
                      - ZonePriority
                      - ThermostatOffsetPriority
                      - MasterThermostatPriority
                      - Scheduled
                Default value: MasterThermostatPriority
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
                                 'for field `master_thermostat_priority_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `master_thermostat_priority_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `master_thermostat_priority_control_type`')
            vals = {}
            vals["loadpriority"] = "LoadPriority"
            vals["zonepriority"] = "ZonePriority"
            vals["thermostatoffsetpriority"] = "ThermostatOffsetPriority"
            vals["masterthermostatpriority"] = "MasterThermostatPriority"
            vals["scheduled"] = "Scheduled"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `master_thermostat_priority_control_type`'.format(value))
            value = vals[value_lower]

        self._data["Master Thermostat Priority Control Type"] = value

    @property
    def thermostat_priority_schedule_name(self):
        """Get thermostat_priority_schedule_name

        Returns:
            str: the value of `thermostat_priority_schedule_name` or None if not set
        """
        return self._data["Thermostat Priority Schedule Name"]

    @thermostat_priority_schedule_name.setter
    def thermostat_priority_schedule_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_priority_schedule_name`
        this field is required if Master Thermostat Priority Control Type is Scheduled.
        Schedule values of 0 denote cooling, 1 for heating, and all other values disable the system.

        Args:
            value (str): value for IDD Field `thermostat_priority_schedule_name`
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
                                 'for field `thermostat_priority_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_priority_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_priority_schedule_name`')

        self._data["Thermostat Priority Schedule Name"] = value

    @property
    def zone_terminal_unit_list_name(self):
        """Get zone_terminal_unit_list_name

        Returns:
            str: the value of `zone_terminal_unit_list_name` or None if not set
        """
        return self._data["Zone Terminal Unit List Name"]

    @zone_terminal_unit_list_name.setter
    def zone_terminal_unit_list_name(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_list_name`
        Enter the name of a ZoneTerminalUnitList. This list connects zone terminal units to this
        heat pump.

        Args:
            value (str): value for IDD Field `zone_terminal_unit_list_name`
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
                                 'for field `zone_terminal_unit_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_list_name`')

        self._data["Zone Terminal Unit List Name"] = value

    @property
    def heat_pump_waste_heat_recovery(self):
        """Get heat_pump_waste_heat_recovery

        Returns:
            str: the value of `heat_pump_waste_heat_recovery` or None if not set
        """
        return self._data["Heat Pump Waste Heat Recovery"]

    @heat_pump_waste_heat_recovery.setter
    def heat_pump_waste_heat_recovery(self, value="No"):
        """  Corresponds to IDD Field `heat_pump_waste_heat_recovery`
        This field is reserved for future use. The only valid choice is No.

        Args:
            value (str): value for IDD Field `heat_pump_waste_heat_recovery`
                Accepted values are:
                      - No
                      - Yes
                Default value: No
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
                                 'for field `heat_pump_waste_heat_recovery`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_pump_waste_heat_recovery`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_pump_waste_heat_recovery`')
            vals = {}
            vals["no"] = "No"
            vals["yes"] = "Yes"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `heat_pump_waste_heat_recovery`'.format(value))
            value = vals[value_lower]

        self._data["Heat Pump Waste Heat Recovery"] = value

    @property
    def equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode(self):
        """Get equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode

        Returns:
            float: the value of `equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode` or None if not set
        """
        return self._data["Equivalent Piping Length used for Piping Correction Factor in Cooling Mode"]

    @equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode.setter
    def equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode(self, value=None):
        """  Corresponds to IDD Field `equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode`
        Enter the equivalent length of the farthest terminal unit from the condenser

        Args:
            value (float): value for IDD Field `equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode`
                Units: m
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
                                 'for field `equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode`'.format(value))

        self._data["Equivalent Piping Length used for Piping Correction Factor in Cooling Mode"] = value

    @property
    def vertical_height_used_for_piping_correction_factor(self):
        """Get vertical_height_used_for_piping_correction_factor

        Returns:
            float: the value of `vertical_height_used_for_piping_correction_factor` or None if not set
        """
        return self._data["Vertical Height used for Piping Correction Factor"]

    @vertical_height_used_for_piping_correction_factor.setter
    def vertical_height_used_for_piping_correction_factor(self, value=None):
        """  Corresponds to IDD Field `vertical_height_used_for_piping_correction_factor`
        Enter the height difference between the highest and lowest terminal unit

        Args:
            value (float): value for IDD Field `vertical_height_used_for_piping_correction_factor`
                Units: m
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
                                 'for field `vertical_height_used_for_piping_correction_factor`'.format(value))

        self._data["Vertical Height used for Piping Correction Factor"] = value

    @property
    def piping_correction_factor_for_length_in_cooling_mode_curve_name(self):
        """Get piping_correction_factor_for_length_in_cooling_mode_curve_name

        Returns:
            str: the value of `piping_correction_factor_for_length_in_cooling_mode_curve_name` or None if not set
        """
        return self._data["Piping Correction Factor for Length in Cooling Mode Curve Name"]

    @piping_correction_factor_for_length_in_cooling_mode_curve_name.setter
    def piping_correction_factor_for_length_in_cooling_mode_curve_name(self, value=None):
        """  Corresponds to IDD Field `piping_correction_factor_for_length_in_cooling_mode_curve_name`
        Table:OneIndependentVariable object can also be used
        Table:TwoIndependentVariables object can also be used
        PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR)
        where L = length and CR = combination ratio
        specifies coefficients for a0, a1, a2, and a3 in the PCF equation

        Args:
            value (str): value for IDD Field `piping_correction_factor_for_length_in_cooling_mode_curve_name`
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
                                 'for field `piping_correction_factor_for_length_in_cooling_mode_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `piping_correction_factor_for_length_in_cooling_mode_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `piping_correction_factor_for_length_in_cooling_mode_curve_name`')

        self._data["Piping Correction Factor for Length in Cooling Mode Curve Name"] = value

    @property
    def piping_correction_factor_for_height_in_cooling_mode_coefficient(self):
        """Get piping_correction_factor_for_height_in_cooling_mode_coefficient

        Returns:
            float: the value of `piping_correction_factor_for_height_in_cooling_mode_coefficient` or None if not set
        """
        return self._data["Piping Correction Factor for Height in Cooling Mode Coefficient"]

    @piping_correction_factor_for_height_in_cooling_mode_coefficient.setter
    def piping_correction_factor_for_height_in_cooling_mode_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `piping_correction_factor_for_height_in_cooling_mode_coefficient`
        PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H
        where L = length, H = height, and CR = combination ratio
        specifies coefficient a4 (or a6 for biquadratic) in the PCF equation

        Args:
            value (float): value for IDD Field `piping_correction_factor_for_height_in_cooling_mode_coefficient`
                Units: 1/m
                Default value: 0.0
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
                                 'for field `piping_correction_factor_for_height_in_cooling_mode_coefficient`'.format(value))

        self._data["Piping Correction Factor for Height in Cooling Mode Coefficient"] = value

    @property
    def equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode(self):
        """Get equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode

        Returns:
            float: the value of `equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode` or None if not set
        """
        return self._data["Equivalent Piping Length used for Piping Correction Factor in Heating Mode"]

    @equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode.setter
    def equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode(self, value=None):
        """  Corresponds to IDD Field `equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode`
        Enter the equivalent length of the farthest terminal unit from the condenser

        Args:
            value (float): value for IDD Field `equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode`
                Units: m
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
                                 'for field `equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode`'.format(value))

        self._data["Equivalent Piping Length used for Piping Correction Factor in Heating Mode"] = value

    @property
    def piping_correction_factor_for_length_in_heating_mode_curve_name(self):
        """Get piping_correction_factor_for_length_in_heating_mode_curve_name

        Returns:
            str: the value of `piping_correction_factor_for_length_in_heating_mode_curve_name` or None if not set
        """
        return self._data["Piping Correction Factor for Length in Heating Mode Curve Name"]

    @piping_correction_factor_for_length_in_heating_mode_curve_name.setter
    def piping_correction_factor_for_length_in_heating_mode_curve_name(self, value=None):
        """  Corresponds to IDD Field `piping_correction_factor_for_length_in_heating_mode_curve_name`
        Table:OneIndependentVariable object can also be used
        Table:TwoIndependentVariables object can also be used
        PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H
        where L = length and CR = combination ratio
        specifies coefficients for a0, a1, a2, and a3 (or a0-a5 for biquadratic) in the PCF equation

        Args:
            value (str): value for IDD Field `piping_correction_factor_for_length_in_heating_mode_curve_name`
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
                                 'for field `piping_correction_factor_for_length_in_heating_mode_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `piping_correction_factor_for_length_in_heating_mode_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `piping_correction_factor_for_length_in_heating_mode_curve_name`')

        self._data["Piping Correction Factor for Length in Heating Mode Curve Name"] = value

    @property
    def piping_correction_factor_for_height_in_heating_mode_coefficient(self):
        """Get piping_correction_factor_for_height_in_heating_mode_coefficient

        Returns:
            float: the value of `piping_correction_factor_for_height_in_heating_mode_coefficient` or None if not set
        """
        return self._data["Piping Correction Factor for Height in Heating Mode Coefficient"]

    @piping_correction_factor_for_height_in_heating_mode_coefficient.setter
    def piping_correction_factor_for_height_in_heating_mode_coefficient(self, value=0.0 ):
        """  Corresponds to IDD Field `piping_correction_factor_for_height_in_heating_mode_coefficient`
        PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H
        where L = length, H = height, and CR = combination ratio
        specifies coefficient a4 (or a6 for biquadratic) in the PCF equation

        Args:
            value (float): value for IDD Field `piping_correction_factor_for_height_in_heating_mode_coefficient`
                Units: 1/m
                Default value: 0.0
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
                                 'for field `piping_correction_factor_for_height_in_heating_mode_coefficient`'.format(value))

        self._data["Piping Correction Factor for Height in Heating Mode Coefficient"] = value

    @property
    def crankcase_heater_power_per_compressor(self):
        """Get crankcase_heater_power_per_compressor

        Returns:
            float: the value of `crankcase_heater_power_per_compressor` or None if not set
        """
        return self._data["Crankcase Heater Power per Compressor"]

    @crankcase_heater_power_per_compressor.setter
    def crankcase_heater_power_per_compressor(self, value=33.0 ):
        """  Corresponds to IDD Field `crankcase_heater_power_per_compressor`
        Enter the value of the resistive heater located in the compressor(s). This heater
        is used to warm the refrigerant and oil when the compressor is off.

        Args:
            value (float): value for IDD Field `crankcase_heater_power_per_compressor`
                Units: W
                Default value: 33.0
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
                                 'for field `crankcase_heater_power_per_compressor`'.format(value))

        self._data["Crankcase Heater Power per Compressor"] = value

    @property
    def number_of_compressors(self):
        """Get number_of_compressors

        Returns:
            int: the value of `number_of_compressors` or None if not set
        """
        return self._data["Number of Compressors"]

    @number_of_compressors.setter
    def number_of_compressors(self, value=2 ):
        """  Corresponds to IDD Field `number_of_compressors`
        Enter the total number of compressor. This input is used only for crankcase
        heater calculations.

        Args:
            value (int): value for IDD Field `number_of_compressors`
                Units: dimensionless
                Default value: 2
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
                                 'for field `number_of_compressors`'.format(value))

        self._data["Number of Compressors"] = value

    @property
    def ratio_of_compressor_size_to_total_compressor_capacity(self):
        """Get ratio_of_compressor_size_to_total_compressor_capacity

        Returns:
            float: the value of `ratio_of_compressor_size_to_total_compressor_capacity` or None if not set
        """
        return self._data["Ratio of Compressor Size to Total Compressor Capacity"]

    @ratio_of_compressor_size_to_total_compressor_capacity.setter
    def ratio_of_compressor_size_to_total_compressor_capacity(self, value=0.5 ):
        """  Corresponds to IDD Field `ratio_of_compressor_size_to_total_compressor_capacity`
        Enter the ratio of the first stage compressor to total compressor capacity.
        All other compressors are assumed to be equally sized. This inputs is used
        only for crankcase heater calculations.

        Args:
            value (float): value for IDD Field `ratio_of_compressor_size_to_total_compressor_capacity`
                Units: W/W
                Default value: 0.5
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
                                 'for field `ratio_of_compressor_size_to_total_compressor_capacity`'.format(value))

        self._data["Ratio of Compressor Size to Total Compressor Capacity"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_crankcase_heater(self):
        """Get maximum_outdoor_drybulb_temperature_for_crankcase_heater

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_crankcase_heater` or None if not set
        """
        return self._data["Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"]

    @maximum_outdoor_drybulb_temperature_for_crankcase_heater.setter
    def maximum_outdoor_drybulb_temperature_for_crankcase_heater(self, value=5.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_crankcase_heater`
        Enter the maximum outdoor temperature above which the crankcase heaters are disabled.

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_crankcase_heater`
                Units: C
                Default value: 5.0
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
                                 'for field `maximum_outdoor_drybulb_temperature_for_crankcase_heater`'.format(value))

        self._data["Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"] = value

    @property
    def defrost_strategy(self):
        """Get defrost_strategy

        Returns:
            str: the value of `defrost_strategy` or None if not set
        """
        return self._data["Defrost Strategy"]

    @defrost_strategy.setter
    def defrost_strategy(self, value="Resistive"):
        """  Corresponds to IDD Field `defrost_strategy`
        Select a defrost strategy. Reverse cycle reverses the operating mode from heating to cooling
        to melt frost formation on the condenser coil. The resistive strategy uses a resitive heater
        to melt the frost.

        Args:
            value (str): value for IDD Field `defrost_strategy`
                Accepted values are:
                      - ReverseCycle
                      - Resistive
                Default value: Resistive
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
                                 'for field `defrost_strategy`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_strategy`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_strategy`')
            vals = {}
            vals["reversecycle"] = "ReverseCycle"
            vals["resistive"] = "Resistive"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `defrost_strategy`'.format(value))
            value = vals[value_lower]

        self._data["Defrost Strategy"] = value

    @property
    def defrost_control(self):
        """Get defrost_control

        Returns:
            str: the value of `defrost_control` or None if not set
        """
        return self._data["Defrost Control"]

    @defrost_control.setter
    def defrost_control(self, value="Timed"):
        """  Corresponds to IDD Field `defrost_control`
        Choose a defrost control type. Either use a fixed Timed defrost period or select
        OnDemand to defrost only when necessary.

        Args:
            value (str): value for IDD Field `defrost_control`
                Accepted values are:
                      - Timed
                      - OnDemand
                Default value: Timed
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
                                 'for field `defrost_control`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_control`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_control`')
            vals = {}
            vals["timed"] = "Timed"
            vals["ondemand"] = "OnDemand"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `defrost_control`'.format(value))
            value = vals[value_lower]

        self._data["Defrost Control"] = value

    @property
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve_name(self):
        """Get defrost_energy_input_ratio_modifier_function_of_temperature_curve_name

        Returns:
            str: the value of `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name` or None if not set
        """
        return self._data["Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"]

    @defrost_energy_input_ratio_modifier_function_of_temperature_curve_name.setter
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve_name(self, value=None):
        """  Corresponds to IDD Field `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name`
        Table:TwoIndependentVariables object can also be used
        A valid performance curve must be used if reversecycle defrost strategy is selected.

        Args:
            value (str): value for IDD Field `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name`
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
                                 'for field `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name`')

        self._data["Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"] = value

    @property
    def defrost_time_period_fraction(self):
        """Get defrost_time_period_fraction

        Returns:
            float: the value of `defrost_time_period_fraction` or None if not set
        """
        return self._data["Defrost Time Period Fraction"]

    @defrost_time_period_fraction.setter
    def defrost_time_period_fraction(self, value=0.058333 ):
        """  Corresponds to IDD Field `defrost_time_period_fraction`
        Fraction of time in defrost mode.
        Only applicable if timed defrost control is specified.

        Args:
            value (float): value for IDD Field `defrost_time_period_fraction`
                Units: dimensionless
                Default value: 0.058333
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
                                 'for field `defrost_time_period_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `defrost_time_period_fraction`')

        self._data["Defrost Time Period Fraction"] = value

    @property
    def resistive_defrost_heater_capacity(self):
        """Get resistive_defrost_heater_capacity

        Returns:
            float: the value of `resistive_defrost_heater_capacity` or None if not set
        """
        return self._data["Resistive Defrost Heater Capacity"]

    @resistive_defrost_heater_capacity.setter
    def resistive_defrost_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `resistive_defrost_heater_capacity`
        Enter the size of the resistive defrost heating element.
        Only applicable if resistive defrost strategy is specified

        Args:
            value (float): value for IDD Field `resistive_defrost_heater_capacity`
                Units: W
                IP-Units: W
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
                                 'for field `resistive_defrost_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `resistive_defrost_heater_capacity`')

        self._data["Resistive Defrost Heater Capacity"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_defrost_operation(self):
        """Get maximum_outdoor_drybulb_temperature_for_defrost_operation

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_defrost_operation` or None if not set
        """
        return self._data["Maximum Outdoor Dry-bulb Temperature for Defrost Operation"]

    @maximum_outdoor_drybulb_temperature_for_defrost_operation.setter
    def maximum_outdoor_drybulb_temperature_for_defrost_operation(self, value=5.0 ):
        """  Corresponds to IDD Field `maximum_outdoor_drybulb_temperature_for_defrost_operation`
        Enter the maximum outdoor temperature above which the crankcase heaters are disabled.

        Args:
            value (float): value for IDD Field `maximum_outdoor_drybulb_temperature_for_defrost_operation`
                Units: C
                Default value: 5.0
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
                                 'for field `maximum_outdoor_drybulb_temperature_for_defrost_operation`'.format(value))

        self._data["Maximum Outdoor Dry-bulb Temperature for Defrost Operation"] = value

    @property
    def condenser_type(self):
        """Get condenser_type

        Returns:
            str: the value of `condenser_type` or None if not set
        """
        return self._data["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """  Corresponds to IDD Field `condenser_type`
        Select either an air-cooled, evaporatively-cooled or water-cooled condenser.

        Args:
            value (str): value for IDD Field `condenser_type`
                Accepted values are:
                      - AirCooled
                      - EvaporativelyCooled
                      - WaterCooled
                Default value: AirCooled
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
                                 'for field `condenser_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_type`')
            vals = {}
            vals["aircooled"] = "AirCooled"
            vals["evaporativelycooled"] = "EvaporativelyCooled"
            vals["watercooled"] = "WaterCooled"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `condenser_type`'.format(value))
            value = vals[value_lower]

        self._data["Condenser Type"] = value

    @property
    def condenser_inlet_node_name(self):
        """Get condenser_inlet_node_name

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set
        """
        return self._data["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_inlet_node_name`
        Choose an outside air node name or leave this field blank to use weather data.
        If this field is blank, the Condenser Type is assumed to be AirCooled.
        This input must be specified if Condenser Type = WaterCooled.

        Args:
            value (str): value for IDD Field `condenser_inlet_node_name`
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
                                 'for field `condenser_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_inlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_inlet_node_name`')

        self._data["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """Get condenser_outlet_node_name

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set
        """
        return self._data["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `condenser_outlet_node_name`
        Enter a water outlet node name if Condenser Type = WaterCooled.
        Leave this field blank if Condenser Type = Air or EvaporativelyCooled.

        Args:
            value (str): value for IDD Field `condenser_outlet_node_name`
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
                                 'for field `condenser_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `condenser_outlet_node_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `condenser_outlet_node_name`')

        self._data["Condenser Outlet Node Name"] = value

    @property
    def water_condenser_volume_flow_rate(self):
        """Get water_condenser_volume_flow_rate

        Returns:
            float: the value of `water_condenser_volume_flow_rate` or None if not set
        """
        return self._data["Water Condenser Volume Flow Rate"]

    @water_condenser_volume_flow_rate.setter
    def water_condenser_volume_flow_rate(self, value=None):
        """  Corresponds to IDD Field `water_condenser_volume_flow_rate`
        Only used when Condenser Type = WaterCooled.

        Args:
            value (float): value for IDD Field `water_condenser_volume_flow_rate`
                Units: m3/s
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
                                 'for field `water_condenser_volume_flow_rate`'.format(value))

        self._data["Water Condenser Volume Flow Rate"] = value

    @property
    def evaporative_condenser_effectiveness(self):
        """Get evaporative_condenser_effectiveness

        Returns:
            float: the value of `evaporative_condenser_effectiveness` or None if not set
        """
        return self._data["Evaporative Condenser Effectiveness"]

    @evaporative_condenser_effectiveness.setter
    def evaporative_condenser_effectiveness(self, value=0.9 ):
        """  Corresponds to IDD Field `evaporative_condenser_effectiveness`
        Enter the effectiveness of the evaporatively cooled condenser.
        This field is only used when the Condenser Type = EvaporativelyCooled.

        Args:
            value (float): value for IDD Field `evaporative_condenser_effectiveness`
                Units: dimensionless
                Default value: 0.9
                value >= 0.0
                value <= 1.0
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
                                 'for field `evaporative_condenser_effectiveness`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporative_condenser_effectiveness`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `evaporative_condenser_effectiveness`')

        self._data["Evaporative Condenser Effectiveness"] = value

    @property
    def evaporative_condenser_air_flow_rate(self):
        """Get evaporative_condenser_air_flow_rate

        Returns:
            float: the value of `evaporative_condenser_air_flow_rate` or None if not set
        """
        return self._data["Evaporative Condenser Air Flow Rate"]

    @evaporative_condenser_air_flow_rate.setter
    def evaporative_condenser_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `evaporative_condenser_air_flow_rate`
        Used to calculate evaporative condenser water use.
        This field is only used when the Condenser Type = EvaporativelyCooled.

        Args:
            value (float): value for IDD Field `evaporative_condenser_air_flow_rate`
                Units: m3/s
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
                                 'for field `evaporative_condenser_air_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `evaporative_condenser_air_flow_rate`')

        self._data["Evaporative Condenser Air Flow Rate"] = value

    @property
    def evaporative_condenser_pump_rated_power_consumption(self):
        """Get evaporative_condenser_pump_rated_power_consumption

        Returns:
            float: the value of `evaporative_condenser_pump_rated_power_consumption` or None if not set
        """
        return self._data["Evaporative Condenser Pump Rated Power Consumption"]

    @evaporative_condenser_pump_rated_power_consumption.setter
    def evaporative_condenser_pump_rated_power_consumption(self, value=0.0 ):
        """  Corresponds to IDD Field `evaporative_condenser_pump_rated_power_consumption`
        Rated power consumed by the evaporative condenser's water pump.
        This field is only used when the Condenser Type = EvaporativelyCooled.

        Args:
            value (float): value for IDD Field `evaporative_condenser_pump_rated_power_consumption`
                Units: W
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
                                 'for field `evaporative_condenser_pump_rated_power_consumption`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evaporative_condenser_pump_rated_power_consumption`')

        self._data["Evaporative Condenser Pump Rated Power Consumption"] = value

    @property
    def supply_water_storage_tank_name(self):
        """Get supply_water_storage_tank_name

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set
        """
        return self._data["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """  Corresponds to IDD Field `supply_water_storage_tank_name`
        A separate storage tank may be used to supply an evaporatively cooled condenser.

        Args:
            value (str): value for IDD Field `supply_water_storage_tank_name`
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
                                 'for field `supply_water_storage_tank_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_water_storage_tank_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_water_storage_tank_name`')

        self._data["Supply Water Storage Tank Name"] = value

    @property
    def basin_heater_capacity(self):
        """Get basin_heater_capacity

        Returns:
            float: the value of `basin_heater_capacity` or None if not set
        """
        return self._data["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=0.0 ):
        """  Corresponds to IDD Field `basin_heater_capacity`
        This field is only used for Condenser Type = EvaporativelyCooled and for periods
        when the basin heater is available (field Basin Heater Operating Schedule Name).
        For this situation, the heater maintains the basin water temperature at the basin heater
        setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        The basin heater only operates when the DX coil is off.

        Args:
            value (float): value for IDD Field `basin_heater_capacity`
                Units: W/K
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
                                 'for field `basin_heater_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `basin_heater_capacity`')

        self._data["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """Get basin_heater_setpoint_temperature

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set
        """
        return self._data["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0 ):
        """  Corresponds to IDD Field `basin_heater_setpoint_temperature`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Enter the outdoor dry-bulb temperature when the basin heater turns on.

        Args:
            value (float): value for IDD Field `basin_heater_setpoint_temperature`
                Units: C
                Default value: 2.0
                value >= 2.0
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
                                 'for field `basin_heater_setpoint_temperature`'.format(value))
            if value < 2.0:
                raise ValueError('value need to be greater or equal 2.0 '
                                 'for field `basin_heater_setpoint_temperature`')

        self._data["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """Get basin_heater_operating_schedule_name

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set
        """
        return self._data["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `basin_heater_operating_schedule_name`
        This field is only used for Condenser Type = EvaporativelyCooled.
        Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        air dry-bulb temperature is below the basin heater setpoint temperature.
        If a schedule name is not entered, the basin heater is allowed to operate
        throughout the entire simulation.

        Args:
            value (str): value for IDD Field `basin_heater_operating_schedule_name`
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
                                 'for field `basin_heater_operating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `basin_heater_operating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `basin_heater_operating_schedule_name`')

        self._data["Basin Heater Operating Schedule Name"] = value

    @property
    def fuel_type(self):
        """Get fuel_type

        Returns:
            str: the value of `fuel_type` or None if not set
        """
        return self._data["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value="Electricity"):
        """  Corresponds to IDD Field `fuel_type`

        Args:
            value (str): value for IDD Field `fuel_type`
                Accepted values are:
                      - Electricity
                      - NaturalGas
                      - PropaneGas
                      - Diesel
                      - Gasoline
                      - FuelOil#1
                      - FuelOil#2
                      - OtherFuel1
                      - OtherFuel2
                Default value: Electricity
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
                                 'for field `fuel_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fuel_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fuel_type`')
            vals = {}
            vals["electricity"] = "Electricity"
            vals["naturalgas"] = "NaturalGas"
            vals["propanegas"] = "PropaneGas"
            vals["diesel"] = "Diesel"
            vals["gasoline"] = "Gasoline"
            vals["fueloil#1"] = "FuelOil#1"
            vals["fueloil#2"] = "FuelOil#2"
            vals["otherfuel1"] = "OtherFuel1"
            vals["otherfuel2"] = "OtherFuel2"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `fuel_type`'.format(value))
            value = vals[value_lower]

        self._data["Fuel Type"] = value

    @property
    def minimum_outdoor_temperature_in_heat_recovery_mode(self):
        """Get minimum_outdoor_temperature_in_heat_recovery_mode

        Returns:
            float: the value of `minimum_outdoor_temperature_in_heat_recovery_mode` or None if not set
        """
        return self._data["Minimum Outdoor Temperature in Heat Recovery Mode"]

    @minimum_outdoor_temperature_in_heat_recovery_mode.setter
    def minimum_outdoor_temperature_in_heat_recovery_mode(self, value=None):
        """  Corresponds to IDD Field `minimum_outdoor_temperature_in_heat_recovery_mode`
        The minimum outdoor temperature below which heat
        recovery mode will not operate.

        Args:
            value (float): value for IDD Field `minimum_outdoor_temperature_in_heat_recovery_mode`
                Units: C
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
                                 'for field `minimum_outdoor_temperature_in_heat_recovery_mode`'.format(value))

        self._data["Minimum Outdoor Temperature in Heat Recovery Mode"] = value

    @property
    def maximum_outdoor_temperature_in_heat_recovery_mode(self):
        """Get maximum_outdoor_temperature_in_heat_recovery_mode

        Returns:
            float: the value of `maximum_outdoor_temperature_in_heat_recovery_mode` or None if not set
        """
        return self._data["Maximum Outdoor Temperature in Heat Recovery Mode"]

    @maximum_outdoor_temperature_in_heat_recovery_mode.setter
    def maximum_outdoor_temperature_in_heat_recovery_mode(self, value=None):
        """  Corresponds to IDD Field `maximum_outdoor_temperature_in_heat_recovery_mode`
        The maximum outdoor temperature above which heat
        recovery mode will not operate.

        Args:
            value (float): value for IDD Field `maximum_outdoor_temperature_in_heat_recovery_mode`
                Units: C
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
                                 'for field `maximum_outdoor_temperature_in_heat_recovery_mode`'.format(value))

        self._data["Maximum Outdoor Temperature in Heat Recovery Mode"] = value

    @property
    def heat_recovery_cooling_capacity_modifier_curve_name(self):
        """Get heat_recovery_cooling_capacity_modifier_curve_name

        Returns:
            str: the value of `heat_recovery_cooling_capacity_modifier_curve_name` or None if not set
        """
        return self._data["Heat Recovery Cooling Capacity Modifier Curve Name"]

    @heat_recovery_cooling_capacity_modifier_curve_name.setter
    def heat_recovery_cooling_capacity_modifier_curve_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_cooling_capacity_modifier_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter the name of a performance curve which represents
        the change in cooling capacity when heat recovery is active
        A default constant of 0.9 is used if this input is blank

        Args:
            value (str): value for IDD Field `heat_recovery_cooling_capacity_modifier_curve_name`
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
                                 'for field `heat_recovery_cooling_capacity_modifier_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_cooling_capacity_modifier_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_recovery_cooling_capacity_modifier_curve_name`')

        self._data["Heat Recovery Cooling Capacity Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_cooling_capacity_fraction(self):
        """Get initial_heat_recovery_cooling_capacity_fraction

        Returns:
            float: the value of `initial_heat_recovery_cooling_capacity_fraction` or None if not set
        """
        return self._data["Initial Heat Recovery Cooling Capacity Fraction"]

    @initial_heat_recovery_cooling_capacity_fraction.setter
    def initial_heat_recovery_cooling_capacity_fraction(self, value=0.5 ):
        """  Corresponds to IDD Field `initial_heat_recovery_cooling_capacity_fraction`
        Enter the fractional capacity available at the start
        of heat recovery mode. The capacity exponentially approaches
        the steady-state value according to the inputs for
        Heat Recovery Cooling Capacity Modifier and Heat Recovery
        Cooling Capacity Time Constant

        Args:
            value (float): value for IDD Field `initial_heat_recovery_cooling_capacity_fraction`
                Units: W/W
                Default value: 0.5
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
                                 'for field `initial_heat_recovery_cooling_capacity_fraction`'.format(value))

        self._data["Initial Heat Recovery Cooling Capacity Fraction"] = value

    @property
    def heat_recovery_cooling_capacity_time_constant(self):
        """Get heat_recovery_cooling_capacity_time_constant

        Returns:
            float: the value of `heat_recovery_cooling_capacity_time_constant` or None if not set
        """
        return self._data["Heat Recovery Cooling Capacity Time Constant"]

    @heat_recovery_cooling_capacity_time_constant.setter
    def heat_recovery_cooling_capacity_time_constant(self, value=0.15 ):
        """  Corresponds to IDD Field `heat_recovery_cooling_capacity_time_constant`
        Enter the time constant used to model the transition
        from cooling only mode to heat recovery mode

        Args:
            value (float): value for IDD Field `heat_recovery_cooling_capacity_time_constant`
                Units: hr
                Default value: 0.15
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
                                 'for field `heat_recovery_cooling_capacity_time_constant`'.format(value))

        self._data["Heat Recovery Cooling Capacity Time Constant"] = value

    @property
    def heat_recovery_cooling_energy_modifier_curve_name(self):
        """Get heat_recovery_cooling_energy_modifier_curve_name

        Returns:
            str: the value of `heat_recovery_cooling_energy_modifier_curve_name` or None if not set
        """
        return self._data["Heat Recovery Cooling Energy Modifier Curve Name"]

    @heat_recovery_cooling_energy_modifier_curve_name.setter
    def heat_recovery_cooling_energy_modifier_curve_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_cooling_energy_modifier_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter the name of a performance curve which represents
        the change in cooling energy when heat recovery is active
        A default constant of 1.1 is used if this input is blank

        Args:
            value (str): value for IDD Field `heat_recovery_cooling_energy_modifier_curve_name`
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
                                 'for field `heat_recovery_cooling_energy_modifier_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_cooling_energy_modifier_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_recovery_cooling_energy_modifier_curve_name`')

        self._data["Heat Recovery Cooling Energy Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_cooling_energy_fraction(self):
        """Get initial_heat_recovery_cooling_energy_fraction

        Returns:
            float: the value of `initial_heat_recovery_cooling_energy_fraction` or None if not set
        """
        return self._data["Initial Heat Recovery Cooling Energy Fraction"]

    @initial_heat_recovery_cooling_energy_fraction.setter
    def initial_heat_recovery_cooling_energy_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `initial_heat_recovery_cooling_energy_fraction`
        Enter the fractional electric consumption rate at the start
        of heat recovery mode. The electric consumption rate exponentially
        approaches the steady-state value according to the inputs for
        Heat Recovery Cooling Energy Modifier and Heat Recovery
        Cooling Energy Time Constant

        Args:
            value (float): value for IDD Field `initial_heat_recovery_cooling_energy_fraction`
                Units: W/W
                Default value: 1.0
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
                                 'for field `initial_heat_recovery_cooling_energy_fraction`'.format(value))

        self._data["Initial Heat Recovery Cooling Energy Fraction"] = value

    @property
    def heat_recovery_cooling_energy_time_constant(self):
        """Get heat_recovery_cooling_energy_time_constant

        Returns:
            float: the value of `heat_recovery_cooling_energy_time_constant` or None if not set
        """
        return self._data["Heat Recovery Cooling Energy Time Constant"]

    @heat_recovery_cooling_energy_time_constant.setter
    def heat_recovery_cooling_energy_time_constant(self, value=0.0 ):
        """  Corresponds to IDD Field `heat_recovery_cooling_energy_time_constant`
        Enter the time constant used to model the transition
        from cooling only mode to heat recovery mode

        Args:
            value (float): value for IDD Field `heat_recovery_cooling_energy_time_constant`
                Units: hr
                Default value: 0.0
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
                                 'for field `heat_recovery_cooling_energy_time_constant`'.format(value))

        self._data["Heat Recovery Cooling Energy Time Constant"] = value

    @property
    def heat_recovery_heating_capacity_modifier_curve_name(self):
        """Get heat_recovery_heating_capacity_modifier_curve_name

        Returns:
            str: the value of `heat_recovery_heating_capacity_modifier_curve_name` or None if not set
        """
        return self._data["Heat Recovery Heating Capacity Modifier Curve Name"]

    @heat_recovery_heating_capacity_modifier_curve_name.setter
    def heat_recovery_heating_capacity_modifier_curve_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_heating_capacity_modifier_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter the name of a performance curve which represents
        the change in heating capacity when heat recovery is active
        A default constant of 1.1 is used if this input is blank

        Args:
            value (str): value for IDD Field `heat_recovery_heating_capacity_modifier_curve_name`
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
                                 'for field `heat_recovery_heating_capacity_modifier_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_heating_capacity_modifier_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_recovery_heating_capacity_modifier_curve_name`')

        self._data["Heat Recovery Heating Capacity Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_heating_capacity_fraction(self):
        """Get initial_heat_recovery_heating_capacity_fraction

        Returns:
            float: the value of `initial_heat_recovery_heating_capacity_fraction` or None if not set
        """
        return self._data["Initial Heat Recovery Heating Capacity Fraction"]

    @initial_heat_recovery_heating_capacity_fraction.setter
    def initial_heat_recovery_heating_capacity_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `initial_heat_recovery_heating_capacity_fraction`
        Enter the fractional capacity available at the start
        of heat recovery mode. The capacity exponentially approaches
        the steady-state value according to the inputs for
        Heat Recovery Heating Capacity Modifier and Heat Recovery
        Heating Capacity Time Constant

        Args:
            value (float): value for IDD Field `initial_heat_recovery_heating_capacity_fraction`
                Units: W/W
                Default value: 1.0
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
                                 'for field `initial_heat_recovery_heating_capacity_fraction`'.format(value))

        self._data["Initial Heat Recovery Heating Capacity Fraction"] = value

    @property
    def heat_recovery_heating_capacity_time_constant(self):
        """Get heat_recovery_heating_capacity_time_constant

        Returns:
            float: the value of `heat_recovery_heating_capacity_time_constant` or None if not set
        """
        return self._data["Heat Recovery Heating Capacity Time Constant"]

    @heat_recovery_heating_capacity_time_constant.setter
    def heat_recovery_heating_capacity_time_constant(self, value=0.15 ):
        """  Corresponds to IDD Field `heat_recovery_heating_capacity_time_constant`
        Enter the time constant used to model the transition
        from cooling only mode to heat recovery mode

        Args:
            value (float): value for IDD Field `heat_recovery_heating_capacity_time_constant`
                Units: hr
                Default value: 0.15
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
                                 'for field `heat_recovery_heating_capacity_time_constant`'.format(value))

        self._data["Heat Recovery Heating Capacity Time Constant"] = value

    @property
    def heat_recovery_heating_energy_modifier_curve_name(self):
        """Get heat_recovery_heating_energy_modifier_curve_name

        Returns:
            str: the value of `heat_recovery_heating_energy_modifier_curve_name` or None if not set
        """
        return self._data["Heat Recovery Heating Energy Modifier Curve Name"]

    @heat_recovery_heating_energy_modifier_curve_name.setter
    def heat_recovery_heating_energy_modifier_curve_name(self, value=None):
        """  Corresponds to IDD Field `heat_recovery_heating_energy_modifier_curve_name`
        Table:TwoIndependentVariables object can also be used
        Enter the name of a performance curve which represents
        the change in heating electric consumption rate when heat recovery is active
        A default constant of 1.1 is used if this input is blank

        Args:
            value (str): value for IDD Field `heat_recovery_heating_energy_modifier_curve_name`
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
                                 'for field `heat_recovery_heating_energy_modifier_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heat_recovery_heating_energy_modifier_curve_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heat_recovery_heating_energy_modifier_curve_name`')

        self._data["Heat Recovery Heating Energy Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_heating_energy_fraction(self):
        """Get initial_heat_recovery_heating_energy_fraction

        Returns:
            float: the value of `initial_heat_recovery_heating_energy_fraction` or None if not set
        """
        return self._data["Initial Heat Recovery Heating Energy Fraction"]

    @initial_heat_recovery_heating_energy_fraction.setter
    def initial_heat_recovery_heating_energy_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `initial_heat_recovery_heating_energy_fraction`
        Enter the fractional electric consumption rate at the start
        of heat recovery mode. The electric consumption rate exponentially
        approaches the steady-state value according to the inputs for
        Heat Recovery Cooling Energy Modifier and Heat Recovery
        Cooling Energy Time Constant

        Args:
            value (float): value for IDD Field `initial_heat_recovery_heating_energy_fraction`
                Units: W/W
                Default value: 1.0
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
                                 'for field `initial_heat_recovery_heating_energy_fraction`'.format(value))

        self._data["Initial Heat Recovery Heating Energy Fraction"] = value

    @property
    def heat_recovery_heating_energy_time_constant(self):
        """Get heat_recovery_heating_energy_time_constant

        Returns:
            float: the value of `heat_recovery_heating_energy_time_constant` or None if not set
        """
        return self._data["Heat Recovery Heating Energy Time Constant"]

    @heat_recovery_heating_energy_time_constant.setter
    def heat_recovery_heating_energy_time_constant(self, value=0.0 ):
        """  Corresponds to IDD Field `heat_recovery_heating_energy_time_constant`
        Enter the time constant used to model the transition
        from cooling only mode to heat recovery mode

        Args:
            value (float): value for IDD Field `heat_recovery_heating_energy_time_constant`
                Units: hr
                Default value: 0.0
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
                                 'for field `heat_recovery_heating_energy_time_constant`'.format(value))

        self._data["Heat Recovery Heating Energy Time Constant"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ZoneTerminalUnitList(object):
    """ Corresponds to IDD object `ZoneTerminalUnitList`
        List of variable refrigerant flow (VRF) terminal units served by a given VRF condensing
        unit. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and
        AirConditioner:VariableRefrigerantFlow.
    
    """
    internal_name = "ZoneTerminalUnitList"
    field_count = 21
    required_fields = ["Zone Terminal Unit List Name", "Zone Terminal Unit Name 1"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneTerminalUnitList`
        """
        self._data = OrderedDict()
        self._data["Zone Terminal Unit List Name"] = None
        self._data["Zone Terminal Unit Name 1"] = None
        self._data["Zone Terminal Unit Name 2"] = None
        self._data["Zone Terminal Unit Name 3"] = None
        self._data["Zone Terminal Unit Name 4"] = None
        self._data["Zone Terminal Unit Name 5"] = None
        self._data["Zone Terminal Unit Name 6"] = None
        self._data["Zone Terminal Unit Name 7"] = None
        self._data["Zone Terminal Unit Name 8"] = None
        self._data["Zone Terminal Unit Name 9"] = None
        self._data["Zone Terminal Unit Name 10"] = None
        self._data["Zone Terminal Unit Name 11"] = None
        self._data["Zone Terminal Unit Name 12"] = None
        self._data["Zone Terminal Unit Name 13"] = None
        self._data["Zone Terminal Unit Name 14"] = None
        self._data["Zone Terminal Unit Name 15"] = None
        self._data["Zone Terminal Unit Name 16"] = None
        self._data["Zone Terminal Unit Name 17"] = None
        self._data["Zone Terminal Unit Name 18"] = None
        self._data["Zone Terminal Unit Name 19"] = None
        self._data["Zone Terminal Unit Name 20"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_terminal_unit_list_name = None
        else:
            self.zone_terminal_unit_list_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_1 = None
        else:
            self.zone_terminal_unit_name_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_2 = None
        else:
            self.zone_terminal_unit_name_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_3 = None
        else:
            self.zone_terminal_unit_name_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_4 = None
        else:
            self.zone_terminal_unit_name_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_5 = None
        else:
            self.zone_terminal_unit_name_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_6 = None
        else:
            self.zone_terminal_unit_name_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_7 = None
        else:
            self.zone_terminal_unit_name_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_8 = None
        else:
            self.zone_terminal_unit_name_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_9 = None
        else:
            self.zone_terminal_unit_name_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_10 = None
        else:
            self.zone_terminal_unit_name_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_11 = None
        else:
            self.zone_terminal_unit_name_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_12 = None
        else:
            self.zone_terminal_unit_name_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_13 = None
        else:
            self.zone_terminal_unit_name_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_14 = None
        else:
            self.zone_terminal_unit_name_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_15 = None
        else:
            self.zone_terminal_unit_name_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_16 = None
        else:
            self.zone_terminal_unit_name_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_17 = None
        else:
            self.zone_terminal_unit_name_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_18 = None
        else:
            self.zone_terminal_unit_name_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_19 = None
        else:
            self.zone_terminal_unit_name_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_terminal_unit_name_20 = None
        else:
            self.zone_terminal_unit_name_20 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_terminal_unit_list_name(self):
        """Get zone_terminal_unit_list_name

        Returns:
            str: the value of `zone_terminal_unit_list_name` or None if not set
        """
        return self._data["Zone Terminal Unit List Name"]

    @zone_terminal_unit_list_name.setter
    def zone_terminal_unit_list_name(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_list_name`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_list_name`
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
                                 'for field `zone_terminal_unit_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_list_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_list_name`')

        self._data["Zone Terminal Unit List Name"] = value

    @property
    def zone_terminal_unit_name_1(self):
        """Get zone_terminal_unit_name_1

        Returns:
            str: the value of `zone_terminal_unit_name_1` or None if not set
        """
        return self._data["Zone Terminal Unit Name 1"]

    @zone_terminal_unit_name_1.setter
    def zone_terminal_unit_name_1(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_1`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_1`
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
                                 'for field `zone_terminal_unit_name_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_1`')

        self._data["Zone Terminal Unit Name 1"] = value

    @property
    def zone_terminal_unit_name_2(self):
        """Get zone_terminal_unit_name_2

        Returns:
            str: the value of `zone_terminal_unit_name_2` or None if not set
        """
        return self._data["Zone Terminal Unit Name 2"]

    @zone_terminal_unit_name_2.setter
    def zone_terminal_unit_name_2(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_2`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_2`
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
                                 'for field `zone_terminal_unit_name_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_2`')

        self._data["Zone Terminal Unit Name 2"] = value

    @property
    def zone_terminal_unit_name_3(self):
        """Get zone_terminal_unit_name_3

        Returns:
            str: the value of `zone_terminal_unit_name_3` or None if not set
        """
        return self._data["Zone Terminal Unit Name 3"]

    @zone_terminal_unit_name_3.setter
    def zone_terminal_unit_name_3(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_3`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_3`
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
                                 'for field `zone_terminal_unit_name_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_3`')

        self._data["Zone Terminal Unit Name 3"] = value

    @property
    def zone_terminal_unit_name_4(self):
        """Get zone_terminal_unit_name_4

        Returns:
            str: the value of `zone_terminal_unit_name_4` or None if not set
        """
        return self._data["Zone Terminal Unit Name 4"]

    @zone_terminal_unit_name_4.setter
    def zone_terminal_unit_name_4(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_4`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_4`
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
                                 'for field `zone_terminal_unit_name_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_4`')

        self._data["Zone Terminal Unit Name 4"] = value

    @property
    def zone_terminal_unit_name_5(self):
        """Get zone_terminal_unit_name_5

        Returns:
            str: the value of `zone_terminal_unit_name_5` or None if not set
        """
        return self._data["Zone Terminal Unit Name 5"]

    @zone_terminal_unit_name_5.setter
    def zone_terminal_unit_name_5(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_5`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_5`
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
                                 'for field `zone_terminal_unit_name_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_5`')

        self._data["Zone Terminal Unit Name 5"] = value

    @property
    def zone_terminal_unit_name_6(self):
        """Get zone_terminal_unit_name_6

        Returns:
            str: the value of `zone_terminal_unit_name_6` or None if not set
        """
        return self._data["Zone Terminal Unit Name 6"]

    @zone_terminal_unit_name_6.setter
    def zone_terminal_unit_name_6(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_6`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_6`
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
                                 'for field `zone_terminal_unit_name_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_6`')

        self._data["Zone Terminal Unit Name 6"] = value

    @property
    def zone_terminal_unit_name_7(self):
        """Get zone_terminal_unit_name_7

        Returns:
            str: the value of `zone_terminal_unit_name_7` or None if not set
        """
        return self._data["Zone Terminal Unit Name 7"]

    @zone_terminal_unit_name_7.setter
    def zone_terminal_unit_name_7(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_7`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_7`
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
                                 'for field `zone_terminal_unit_name_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_7`')

        self._data["Zone Terminal Unit Name 7"] = value

    @property
    def zone_terminal_unit_name_8(self):
        """Get zone_terminal_unit_name_8

        Returns:
            str: the value of `zone_terminal_unit_name_8` or None if not set
        """
        return self._data["Zone Terminal Unit Name 8"]

    @zone_terminal_unit_name_8.setter
    def zone_terminal_unit_name_8(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_8`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_8`
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
                                 'for field `zone_terminal_unit_name_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_8`')

        self._data["Zone Terminal Unit Name 8"] = value

    @property
    def zone_terminal_unit_name_9(self):
        """Get zone_terminal_unit_name_9

        Returns:
            str: the value of `zone_terminal_unit_name_9` or None if not set
        """
        return self._data["Zone Terminal Unit Name 9"]

    @zone_terminal_unit_name_9.setter
    def zone_terminal_unit_name_9(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_9`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_9`
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
                                 'for field `zone_terminal_unit_name_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_9`')

        self._data["Zone Terminal Unit Name 9"] = value

    @property
    def zone_terminal_unit_name_10(self):
        """Get zone_terminal_unit_name_10

        Returns:
            str: the value of `zone_terminal_unit_name_10` or None if not set
        """
        return self._data["Zone Terminal Unit Name 10"]

    @zone_terminal_unit_name_10.setter
    def zone_terminal_unit_name_10(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_10`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_10`
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
                                 'for field `zone_terminal_unit_name_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_10`')

        self._data["Zone Terminal Unit Name 10"] = value

    @property
    def zone_terminal_unit_name_11(self):
        """Get zone_terminal_unit_name_11

        Returns:
            str: the value of `zone_terminal_unit_name_11` or None if not set
        """
        return self._data["Zone Terminal Unit Name 11"]

    @zone_terminal_unit_name_11.setter
    def zone_terminal_unit_name_11(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_11`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_11`
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
                                 'for field `zone_terminal_unit_name_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_11`')

        self._data["Zone Terminal Unit Name 11"] = value

    @property
    def zone_terminal_unit_name_12(self):
        """Get zone_terminal_unit_name_12

        Returns:
            str: the value of `zone_terminal_unit_name_12` or None if not set
        """
        return self._data["Zone Terminal Unit Name 12"]

    @zone_terminal_unit_name_12.setter
    def zone_terminal_unit_name_12(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_12`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_12`
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
                                 'for field `zone_terminal_unit_name_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_12`')

        self._data["Zone Terminal Unit Name 12"] = value

    @property
    def zone_terminal_unit_name_13(self):
        """Get zone_terminal_unit_name_13

        Returns:
            str: the value of `zone_terminal_unit_name_13` or None if not set
        """
        return self._data["Zone Terminal Unit Name 13"]

    @zone_terminal_unit_name_13.setter
    def zone_terminal_unit_name_13(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_13`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_13`
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
                                 'for field `zone_terminal_unit_name_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_13`')

        self._data["Zone Terminal Unit Name 13"] = value

    @property
    def zone_terminal_unit_name_14(self):
        """Get zone_terminal_unit_name_14

        Returns:
            str: the value of `zone_terminal_unit_name_14` or None if not set
        """
        return self._data["Zone Terminal Unit Name 14"]

    @zone_terminal_unit_name_14.setter
    def zone_terminal_unit_name_14(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_14`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_14`
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
                                 'for field `zone_terminal_unit_name_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_14`')

        self._data["Zone Terminal Unit Name 14"] = value

    @property
    def zone_terminal_unit_name_15(self):
        """Get zone_terminal_unit_name_15

        Returns:
            str: the value of `zone_terminal_unit_name_15` or None if not set
        """
        return self._data["Zone Terminal Unit Name 15"]

    @zone_terminal_unit_name_15.setter
    def zone_terminal_unit_name_15(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_15`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_15`
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
                                 'for field `zone_terminal_unit_name_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_15`')

        self._data["Zone Terminal Unit Name 15"] = value

    @property
    def zone_terminal_unit_name_16(self):
        """Get zone_terminal_unit_name_16

        Returns:
            str: the value of `zone_terminal_unit_name_16` or None if not set
        """
        return self._data["Zone Terminal Unit Name 16"]

    @zone_terminal_unit_name_16.setter
    def zone_terminal_unit_name_16(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_16`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_16`
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
                                 'for field `zone_terminal_unit_name_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_16`')

        self._data["Zone Terminal Unit Name 16"] = value

    @property
    def zone_terminal_unit_name_17(self):
        """Get zone_terminal_unit_name_17

        Returns:
            str: the value of `zone_terminal_unit_name_17` or None if not set
        """
        return self._data["Zone Terminal Unit Name 17"]

    @zone_terminal_unit_name_17.setter
    def zone_terminal_unit_name_17(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_17`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_17`
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
                                 'for field `zone_terminal_unit_name_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_17`')

        self._data["Zone Terminal Unit Name 17"] = value

    @property
    def zone_terminal_unit_name_18(self):
        """Get zone_terminal_unit_name_18

        Returns:
            str: the value of `zone_terminal_unit_name_18` or None if not set
        """
        return self._data["Zone Terminal Unit Name 18"]

    @zone_terminal_unit_name_18.setter
    def zone_terminal_unit_name_18(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_18`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_18`
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
                                 'for field `zone_terminal_unit_name_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_18`')

        self._data["Zone Terminal Unit Name 18"] = value

    @property
    def zone_terminal_unit_name_19(self):
        """Get zone_terminal_unit_name_19

        Returns:
            str: the value of `zone_terminal_unit_name_19` or None if not set
        """
        return self._data["Zone Terminal Unit Name 19"]

    @zone_terminal_unit_name_19.setter
    def zone_terminal_unit_name_19(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_19`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_19`
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
                                 'for field `zone_terminal_unit_name_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_19`')

        self._data["Zone Terminal Unit Name 19"] = value

    @property
    def zone_terminal_unit_name_20(self):
        """Get zone_terminal_unit_name_20

        Returns:
            str: the value of `zone_terminal_unit_name_20` or None if not set
        """
        return self._data["Zone Terminal Unit Name 20"]

    @zone_terminal_unit_name_20.setter
    def zone_terminal_unit_name_20(self, value=None):
        """  Corresponds to IDD Field `zone_terminal_unit_name_20`

        Args:
            value (str): value for IDD Field `zone_terminal_unit_name_20`
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
                                 'for field `zone_terminal_unit_name_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_terminal_unit_name_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_terminal_unit_name_20`')

        self._data["Zone Terminal Unit Name 20"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
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
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])