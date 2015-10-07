""" Data objects in group "Variable Refrigerant Flow Equipment"
"""

from collections import OrderedDict
import logging
from pyidf.helper import DataObject

logger = logging.getLogger("pyidf")
logger.addHandler(logging.NullHandler())



class AirConditionerVariableRefrigerantFlow(DataObject):

    """ Corresponds to IDD object `AirConditioner:VariableRefrigerantFlow`
        Variable refrigerant flow (VRF) air-to-air heat pump condensing unit (includes one
        or more electric compressors and outdoor fan). Serves one or more VRF zone terminal
        units. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and ZoneTerminalUnitList.
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'heat pump name',
                                       {'name': u'Heat Pump Name',
                                        'pyname': u'heat_pump_name',
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
                                      (u'gross rated total cooling capacity',
                                       {'name': u'Gross Rated Total Cooling Capacity',
                                        'pyname': u'gross_rated_total_cooling_capacity',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'gross rated cooling cop',
                                       {'name': u'Gross Rated Cooling COP',
                                        'pyname': u'gross_rated_cooling_cop',
                                        'default': 3.3,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'minimum outdoor temperature in cooling mode',
                                       {'name': u'Minimum Outdoor Temperature in Cooling Mode',
                                        'pyname': u'minimum_outdoor_temperature_in_cooling_mode',
                                        'default': -6.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor temperature in cooling mode',
                                       {'name': u'Maximum Outdoor Temperature in Cooling Mode',
                                        'pyname': u'maximum_outdoor_temperature_in_cooling_mode',
                                        'default': 43.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'cooling capacity ratio modifier function of low temperature curve name',
                                       {'name': u'Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name',
                                        'pyname': u'cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling capacity ratio boundary curve name',
                                       {'name': u'Cooling Capacity Ratio Boundary Curve Name',
                                        'pyname': u'cooling_capacity_ratio_boundary_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling capacity ratio modifier function of high temperature curve name',
                                       {'name': u'Cooling Capacity Ratio Modifier Function of High Temperature Curve Name',
                                        'pyname': u'cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling energy input ratio modifier function of low temperature curve name',
                                       {'name': u'Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name',
                                        'pyname': u'cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling energy input ratio boundary curve name',
                                       {'name': u'Cooling Energy Input Ratio Boundary Curve Name',
                                        'pyname': u'cooling_energy_input_ratio_boundary_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling energy input ratio modifier function of high temperature curve name',
                                       {'name': u'Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name',
                                        'pyname': u'cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling energy input ratio modifier function of low part-load ratio curve name',
                                       {'name': u'Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name',
                                        'pyname': u'cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling energy input ratio modifier function of high part-load ratio curve name',
                                       {'name': u'Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name',
                                        'pyname': u'cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling combination ratio correction factor curve name',
                                       {'name': u'Cooling Combination Ratio Correction Factor Curve Name',
                                        'pyname': u'cooling_combination_ratio_correction_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'cooling part-load fraction correlation curve name',
                                       {'name': u'Cooling Part-Load Fraction Correlation Curve Name',
                                        'pyname': u'cooling_partload_fraction_correlation_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'gross rated heating capacity',
                                       {'name': u'Gross Rated Heating Capacity',
                                        'pyname': u'gross_rated_heating_capacity',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated heating capacity sizing ratio',
                                       {'name': u'Rated Heating Capacity Sizing Ratio',
                                        'pyname': u'rated_heating_capacity_sizing_ratio',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 1.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'gross rated heating cop',
                                       {'name': u'Gross Rated Heating COP',
                                        'pyname': u'gross_rated_heating_cop',
                                        'default': 3.4,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'minimum outdoor temperature in heating mode',
                                       {'name': u'Minimum Outdoor Temperature in Heating Mode',
                                        'pyname': u'minimum_outdoor_temperature_in_heating_mode',
                                        'default': -20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor temperature in heating mode',
                                       {'name': u'Maximum Outdoor Temperature in Heating Mode',
                                        'pyname': u'maximum_outdoor_temperature_in_heating_mode',
                                        'default': 16.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'heating capacity ratio modifier function of low temperature curve name',
                                       {'name': u'Heating Capacity Ratio Modifier Function of Low Temperature Curve Name',
                                        'pyname': u'heating_capacity_ratio_modifier_function_of_low_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating capacity ratio boundary curve name',
                                       {'name': u'Heating Capacity Ratio Boundary Curve Name',
                                        'pyname': u'heating_capacity_ratio_boundary_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating capacity ratio modifier function of high temperature curve name',
                                       {'name': u'Heating Capacity Ratio Modifier Function of High Temperature Curve Name',
                                        'pyname': u'heating_capacity_ratio_modifier_function_of_high_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating energy input ratio modifier function of low temperature curve name',
                                       {'name': u'Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name',
                                        'pyname': u'heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating energy input ratio boundary curve name',
                                       {'name': u'Heating Energy Input Ratio Boundary Curve Name',
                                        'pyname': u'heating_energy_input_ratio_boundary_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating energy input ratio modifier function of high temperature curve name',
                                       {'name': u'Heating Energy Input Ratio Modifier Function of High Temperature Curve Name',
                                        'pyname': u'heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating performance curve outdoor temperature type',
                                       {'name': u'Heating Performance Curve Outdoor Temperature Type',
                                        'pyname': u'heating_performance_curve_outdoor_temperature_type',
                                        'default': u'WetBulbTemperature',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'DryBulbTemperature',
                                                            u'WetBulbTemperature'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'heating energy input ratio modifier function of low part-load ratio curve name',
                                       {'name': u'Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name',
                                        'pyname': u'heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating energy input ratio modifier function of high part-load ratio curve name',
                                       {'name': u'Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name',
                                        'pyname': u'heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating combination ratio correction factor curve name',
                                       {'name': u'Heating Combination Ratio Correction Factor Curve Name',
                                        'pyname': u'heating_combination_ratio_correction_factor_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heating part-load fraction correlation curve name',
                                       {'name': u'Heating Part-Load Fraction Correlation Curve Name',
                                        'pyname': u'heating_partload_fraction_correlation_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'minimum heat pump part-load ratio',
                                       {'name': u'Minimum Heat Pump Part-Load Ratio',
                                        'pyname': u'minimum_heat_pump_partload_ratio',
                                        'default': 0.15,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'zone name for master thermostat location',
                                       {'name': u'Zone Name for Master Thermostat Location',
                                        'pyname': u'zone_name_for_master_thermostat_location',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'master thermostat priority control type',
                                       {'name': u'Master Thermostat Priority Control Type',
                                        'pyname': u'master_thermostat_priority_control_type',
                                        'default': u'MasterThermostatPriority',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'LoadPriority',
                                                            u'ZonePriority',
                                                            u'ThermostatOffsetPriority',
                                                            u'MasterThermostatPriority',
                                                            u'Scheduled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'thermostat priority schedule name',
                                       {'name': u'Thermostat Priority Schedule Name',
                                        'pyname': u'thermostat_priority_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'zone terminal unit list name',
                                       {'name': u'Zone Terminal Unit List Name',
                                        'pyname': u'zone_terminal_unit_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'heat pump waste heat recovery',
                                       {'name': u'Heat Pump Waste Heat Recovery',
                                        'pyname': u'heat_pump_waste_heat_recovery',
                                        'default': u'No',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'No',
                                                            u'Yes'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'equivalent piping length used for piping correction factor in cooling mode',
                                       {'name': u'Equivalent Piping Length used for Piping Correction Factor in Cooling Mode',
                                        'pyname': u'equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'vertical height used for piping correction factor',
                                       {'name': u'Vertical Height used for Piping Correction Factor',
                                        'pyname': u'vertical_height_used_for_piping_correction_factor',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'piping correction factor for length in cooling mode curve name',
                                       {'name': u'Piping Correction Factor for Length in Cooling Mode Curve Name',
                                        'pyname': u'piping_correction_factor_for_length_in_cooling_mode_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'piping correction factor for height in cooling mode coefficient',
                                       {'name': u'Piping Correction Factor for Height in Cooling Mode Coefficient',
                                        'pyname': u'piping_correction_factor_for_height_in_cooling_mode_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/m'}),
                                      (u'equivalent piping length used for piping correction factor in heating mode',
                                       {'name': u'Equivalent Piping Length used for Piping Correction Factor in Heating Mode',
                                        'pyname': u'equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'piping correction factor for length in heating mode curve name',
                                       {'name': u'Piping Correction Factor for Length in Heating Mode Curve Name',
                                        'pyname': u'piping_correction_factor_for_length_in_heating_mode_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'piping correction factor for height in heating mode coefficient',
                                       {'name': u'Piping Correction Factor for Height in Heating Mode Coefficient',
                                        'pyname': u'piping_correction_factor_for_height_in_heating_mode_coefficient',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'1/m'}),
                                      (u'crankcase heater power per compressor',
                                       {'name': u'Crankcase Heater Power per Compressor',
                                        'pyname': u'crankcase_heater_power_per_compressor',
                                        'default': 33.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'number of compressors',
                                       {'name': u'Number of Compressors',
                                        'pyname': u'number_of_compressors',
                                        'default': 2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer',
                                        'unit': u'dimensionless'}),
                                      (u'ratio of compressor size to total compressor capacity',
                                       {'name': u'Ratio of Compressor Size to Total Compressor Capacity',
                                        'pyname': u'ratio_of_compressor_size_to_total_compressor_capacity',
                                        'default': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'maximum outdoor dry-bulb temperature for crankcase heater',
                                       {'name': u'Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_crankcase_heater',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'defrost strategy',
                                       {'name': u'Defrost Strategy',
                                        'pyname': u'defrost_strategy',
                                        'default': u'Resistive',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ReverseCycle',
                                                            u'Resistive'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost control',
                                       {'name': u'Defrost Control',
                                        'pyname': u'defrost_control',
                                        'default': u'Timed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timed',
                                                            u'OnDemand'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost energy input ratio modifier function of temperature curve name',
                                       {'name': u'Defrost Energy Input Ratio Modifier Function of Temperature Curve Name',
                                        'pyname': u'defrost_energy_input_ratio_modifier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost time period fraction',
                                       {'name': u'Defrost Time Period Fraction',
                                        'pyname': u'defrost_time_period_fraction',
                                        'default': 0.058333,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'resistive defrost heater capacity',
                                       {'name': u'Resistive Defrost Heater Capacity',
                                        'pyname': u'resistive_defrost_heater_capacity',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'maximum outdoor dry-bulb temperature for defrost operation',
                                       {'name': u'Maximum Outdoor Dry-bulb Temperature for Defrost Operation',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_defrost_operation',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'condenser type',
                                       {'name': u'Condenser Type',
                                        'pyname': u'condenser_type',
                                        'default': u'AirCooled',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'AirCooled',
                                                            u'EvaporativelyCooled',
                                                            u'WaterCooled'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'condenser inlet node name',
                                       {'name': u'Condenser Inlet Node Name',
                                        'pyname': u'condenser_inlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'condenser outlet node name',
                                       {'name': u'Condenser Outlet Node Name',
                                        'pyname': u'condenser_outlet_node_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'node'}),
                                      (u'water condenser volume flow rate',
                                       {'name': u'Water Condenser Volume Flow Rate',
                                        'pyname': u'water_condenser_volume_flow_rate',
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'evaporative condenser effectiveness',
                                       {'name': u'Evaporative Condenser Effectiveness',
                                        'pyname': u'evaporative_condenser_effectiveness',
                                        'default': 0.9,
                                        'maximum': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'evaporative condenser air flow rate',
                                       {'name': u'Evaporative Condenser Air Flow Rate',
                                        'pyname': u'evaporative_condenser_air_flow_rate',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s'}),
                                      (u'evaporative condenser pump rated power consumption',
                                       {'name': u'Evaporative Condenser Pump Rated Power Consumption',
                                        'pyname': u'evaporative_condenser_pump_rated_power_consumption',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'supply water storage tank name',
                                       {'name': u'Supply Water Storage Tank Name',
                                        'pyname': u'supply_water_storage_tank_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'basin heater capacity',
                                       {'name': u'Basin Heater Capacity',
                                        'pyname': u'basin_heater_capacity',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/K'}),
                                      (u'basin heater setpoint temperature',
                                       {'name': u'Basin Heater Setpoint Temperature',
                                        'pyname': u'basin_heater_setpoint_temperature',
                                        'default': 2.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 2.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'basin heater operating schedule name',
                                       {'name': u'Basin Heater Operating Schedule Name',
                                        'pyname': u'basin_heater_operating_schedule_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'fuel type',
                                       {'name': u'Fuel Type',
                                        'pyname': u'fuel_type',
                                        'default': u'Electricity',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Electricity',
                                                            u'NaturalGas',
                                                            u'PropaneGas',
                                                            u'Diesel',
                                                            u'Gasoline',
                                                            u'FuelOil#1',
                                                            u'FuelOil#2',
                                                            u'OtherFuel1',
                                                            u'OtherFuel2'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'minimum outdoor temperature in heat recovery mode',
                                       {'name': u'Minimum Outdoor Temperature in Heat Recovery Mode',
                                        'pyname': u'minimum_outdoor_temperature_in_heat_recovery_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor temperature in heat recovery mode',
                                       {'name': u'Maximum Outdoor Temperature in Heat Recovery Mode',
                                        'pyname': u'maximum_outdoor_temperature_in_heat_recovery_mode',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'heat recovery cooling capacity modifier curve name',
                                       {'name': u'Heat Recovery Cooling Capacity Modifier Curve Name',
                                        'pyname': u'heat_recovery_cooling_capacity_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initial heat recovery cooling capacity fraction',
                                       {'name': u'Initial Heat Recovery Cooling Capacity Fraction',
                                        'pyname': u'initial_heat_recovery_cooling_capacity_fraction',
                                        'default': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'heat recovery cooling capacity time constant',
                                       {'name': u'Heat Recovery Cooling Capacity Time Constant',
                                        'pyname': u'heat_recovery_cooling_capacity_time_constant',
                                        'default': 0.15,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'heat recovery cooling energy modifier curve name',
                                       {'name': u'Heat Recovery Cooling Energy Modifier Curve Name',
                                        'pyname': u'heat_recovery_cooling_energy_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initial heat recovery cooling energy fraction',
                                       {'name': u'Initial Heat Recovery Cooling Energy Fraction',
                                        'pyname': u'initial_heat_recovery_cooling_energy_fraction',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'heat recovery cooling energy time constant',
                                       {'name': u'Heat Recovery Cooling Energy Time Constant',
                                        'pyname': u'heat_recovery_cooling_energy_time_constant',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'heat recovery heating capacity modifier curve name',
                                       {'name': u'Heat Recovery Heating Capacity Modifier Curve Name',
                                        'pyname': u'heat_recovery_heating_capacity_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initial heat recovery heating capacity fraction',
                                       {'name': u'Initial Heat Recovery Heating Capacity Fraction',
                                        'pyname': u'initial_heat_recovery_heating_capacity_fraction',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'heat recovery heating capacity time constant',
                                       {'name': u'Heat Recovery Heating Capacity Time Constant',
                                        'pyname': u'heat_recovery_heating_capacity_time_constant',
                                        'default': 0.15,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'}),
                                      (u'heat recovery heating energy modifier curve name',
                                       {'name': u'Heat Recovery Heating Energy Modifier Curve Name',
                                        'pyname': u'heat_recovery_heating_energy_modifier_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'initial heat recovery heating energy fraction',
                                       {'name': u'Initial Heat Recovery Heating Energy Fraction',
                                        'pyname': u'initial_heat_recovery_heating_energy_fraction',
                                        'default': 1.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'heat recovery heating energy time constant',
                                       {'name': u'Heat Recovery Heating Energy Time Constant',
                                        'pyname': u'heat_recovery_heating_energy_time_constant',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'hr'})]),
               'format': None,
               'group': u'Variable Refrigerant Flow Equipment',
               'min-fields': 37,
               'name': u'AirConditioner:VariableRefrigerantFlow',
               'pyname': u'AirConditionerVariableRefrigerantFlow',
               'required-object': False,
               'unique-object': False}

    @property
    def heat_pump_name(self):
        """field `Heat Pump Name`

        |  Enter a unique name for this variable refrigerant flow heat pump.

        Args:
            value (str): value for IDD Field `Heat Pump Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_pump_name` or None if not set

        """
        return self["Heat Pump Name"]

    @heat_pump_name.setter
    def heat_pump_name(self, value=None):
        """Corresponds to IDD field `Heat Pump Name`"""
        self["Heat Pump Name"] = value

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Availability schedule name for this system. Schedule value > 0 means the system is available.
        |  If this field is blank, the system is always available.
        |  Enter the name of a schedule that defines the availability of the unit.
        |  Schedule values of 0 denote the unit is off. All other values denote the unit is available.
        |  If this field is left blank, the unit is available the entire simulation.

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
    def gross_rated_total_cooling_capacity(self):
        """field `Gross Rated Total Cooling Capacity`

        |  Enter the total cooling capacity in watts at rated conditions or set to autosize.
        |  Total cooling capacity not accounting for the effect of supply air fan heat
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Gross Rated Total Cooling Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `gross_rated_total_cooling_capacity` or None if not set

        """
        return self["Gross Rated Total Cooling Capacity"]

    @gross_rated_total_cooling_capacity.setter
    def gross_rated_total_cooling_capacity(self, value=None):
        """Corresponds to IDD field `Gross Rated Total Cooling Capacity`"""
        self["Gross Rated Total Cooling Capacity"] = value

    @property
    def gross_rated_cooling_cop(self):
        """field `Gross Rated Cooling COP`

        |  Enter the coefficient of performance at rated conditions or leave blank to use default.
        |  COP includes compressor and condenser fan electrical energy input
        |  COP does not include supply fan heat or supply fan electric power input
        |  Units: W/W
        |  Default value: 3.3

        Args:
            value (float): value for IDD Field `Gross Rated Cooling COP`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gross_rated_cooling_cop` or None if not set

        """
        return self["Gross Rated Cooling COP"]

    @gross_rated_cooling_cop.setter
    def gross_rated_cooling_cop(self, value=3.3):
        """Corresponds to IDD field `Gross Rated Cooling COP`"""
        self["Gross Rated Cooling COP"] = value

    @property
    def minimum_outdoor_temperature_in_cooling_mode(self):
        """field `Minimum Outdoor Temperature in Cooling Mode`

        |  Enter the minimum outdoor temperature allowed for cooling operation.
        |  Cooling is disabled below this temperature.
        |  Units: C
        |  Default value: -6.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Temperature in Cooling Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_temperature_in_cooling_mode` or None if not set

        """
        return self["Minimum Outdoor Temperature in Cooling Mode"]

    @minimum_outdoor_temperature_in_cooling_mode.setter
    def minimum_outdoor_temperature_in_cooling_mode(self, value=-6.0):
        """Corresponds to IDD field `Minimum Outdoor Temperature in Cooling
        Mode`"""
        self["Minimum Outdoor Temperature in Cooling Mode"] = value

    @property
    def maximum_outdoor_temperature_in_cooling_mode(self):
        """field `Maximum Outdoor Temperature in Cooling Mode`

        |  Enter the maximum outdoor temperature allowed for cooling operation.
        |  Cooling is disabled above this temperature.
        |  Units: C
        |  Default value: 43.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Temperature in Cooling Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_temperature_in_cooling_mode` or None if not set

        """
        return self["Maximum Outdoor Temperature in Cooling Mode"]

    @maximum_outdoor_temperature_in_cooling_mode.setter
    def maximum_outdoor_temperature_in_cooling_mode(self, value=43.0):
        """Corresponds to IDD field `Maximum Outdoor Temperature in Cooling
        Mode`"""
        self["Maximum Outdoor Temperature in Cooling Mode"] = value

    @property
    def cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name(
            self):
        """field `Cooling Capacity Ratio Modifier Function of Low Temperature
        Curve Name`

        |  Enter a curve name that represents full load cooling capacity ratio as a
        |  function of outdoor dry-bulb temperature and indoor wet-bulb temperature.
        |  Up to two curves are allowed if the performance cannot be represented by a single curve.
        |  The following two fields are used if two curves are required.

        Args:
            value (str): value for IDD Field `Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name` or None if not set

        """
        return self[
            "Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name"]

    @cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name.setter
    def cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Capacity Ratio Modifier Function
        of Low Temperature Curve Name`"""
        self[
            "Cooling Capacity Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def cooling_capacity_ratio_boundary_curve_name(self):
        """field `Cooling Capacity Ratio Boundary Curve Name`

        |  This curve object is used to allow separate low and high cooling capacity ratio
        |  performance curves. This curve represents a line passing through the points where
        |  performance changes. The curve calculates outdoor dry-bulb temperature given weighted
        |  average indoor wet-bulb temperature. If a single performance curve is used,
        |  leave this field blank.

        Args:
            value (str): value for IDD Field `Cooling Capacity Ratio Boundary Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_capacity_ratio_boundary_curve_name` or None if not set

        """
        return self["Cooling Capacity Ratio Boundary Curve Name"]

    @cooling_capacity_ratio_boundary_curve_name.setter
    def cooling_capacity_ratio_boundary_curve_name(self, value=None):
        """Corresponds to IDD field `Cooling Capacity Ratio Boundary Curve
        Name`"""
        self["Cooling Capacity Ratio Boundary Curve Name"] = value

    @property
    def cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name(
            self):
        """field `Cooling Capacity Ratio Modifier Function of High Temperature
        Curve Name`

        |  This curve object is used to describe the high outdoor temperature
        |  performance curve used to describe cooling capacity ratio.
        |  This curve is used when a single performance curve does not accurately describe
        |  cooling capacity ratio as a function of temperature.
        |  If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `Cooling Capacity Ratio Modifier Function of High Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name` or None if not set

        """
        return self[
            "Cooling Capacity Ratio Modifier Function of High Temperature Curve Name"]

    @cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name.setter
    def cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Capacity Ratio Modifier Function
        of High Temperature Curve Name`"""
        self[
            "Cooling Capacity Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name(
            self):
        """field `Cooling Energy Input Ratio Modifier Function of Low
        Temperature Curve Name`

        |  Enter a curve name that represents cooling energy ratio as a function of
        |  outdoor dry-bulb temperature and indoor wet-bulb temperature

        Args:
            value (str): value for IDD Field `Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name` or None if not set

        """
        return self[
            "Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Energy Input Ratio Modifier
        Function of Low Temperature Curve Name`"""
        self[
            "Cooling Energy Input Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def cooling_energy_input_ratio_boundary_curve_name(self):
        """field `Cooling Energy Input Ratio Boundary Curve Name`

        |  This curve object is used to allow separate low and high cooling energy input ratio
        |  performance curves. This curve represents a line passing through the points where
        |  performance changes. The curve calculates outdoor dry-bulb temperature given weighted
        |  average indoor wet-bulb temperature. If a single performance curve is used,
        |  leave this field blank.

        Args:
            value (str): value for IDD Field `Cooling Energy Input Ratio Boundary Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_energy_input_ratio_boundary_curve_name` or None if not set

        """
        return self["Cooling Energy Input Ratio Boundary Curve Name"]

    @cooling_energy_input_ratio_boundary_curve_name.setter
    def cooling_energy_input_ratio_boundary_curve_name(self, value=None):
        """Corresponds to IDD field `Cooling Energy Input Ratio Boundary Curve
        Name`"""
        self["Cooling Energy Input Ratio Boundary Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name(
            self):
        """field `Cooling Energy Input Ratio Modifier Function of High
        Temperature Curve Name`

        |  This curve object is used to describe the high outdoor temperature
        |  performance curve used to describe cooling energy ratio.
        |  This curve is used when a single performance curve does not accurately describe
        |  cooling energy ratio as a function of temperature

        Args:
            value (str): value for IDD Field `Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name` or None if not set

        """
        return self[
            "Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Energy Input Ratio Modifier
        Function of High Temperature Curve Name`"""
        self[
            "Cooling Energy Input Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(
            self):
        """field `Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name`

        |  Enter a curve name that represents cooling energy ratio as a function of
        |  part-load ratio for part-load ratios less than or equal to 1.
        |  If this field is left blank, the model assumes energy is proportional to
        |  part-load ratio.

        Args:
            value (str): value for IDD Field `Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name` or None if not set
        """
        return self[
            "Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name`

        """
        self[
            "Cooling Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"] = value

    @property
    def cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(
            self):
        """field `Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name`

        |  Enter a curve name that represents cooling energy ratio as a function of
        |  part-load ratio for part-load ratios greater than 1. Part-load ratios
        |  can exceed 1 in variable speed compression systems.
        |  If this field is left blank, the model assumes energy is proportional to
        |  part-load ratio.

        Args:
            value (str): value for IDD Field `Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name` or None if not set
        """
        return self[
            "Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"]

    @cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name.setter
    def cooling_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name`

        """
        self[
            "Cooling Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"] = value

    @property
    def cooling_combination_ratio_correction_factor_curve_name(self):
        """field `Cooling Combination Ratio Correction Factor Curve Name`

        |  This curve defines how rated capacity changes when the total indoor terminal unit cooling
        |  capacity is greater than the Gross Rated Total Cooling Capacity defined in this object.
        |  If this field is left blank, the model assumes total indoor terminal unit cooling
        |  capacity is equal to the Gross Rated Total Cooling Capacity defined above.

        Args:
            value (str): value for IDD Field `Cooling Combination Ratio Correction Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_combination_ratio_correction_factor_curve_name` or None if not set

        """
        return self["Cooling Combination Ratio Correction Factor Curve Name"]

    @cooling_combination_ratio_correction_factor_curve_name.setter
    def cooling_combination_ratio_correction_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Cooling Combination Ratio Correction
        Factor Curve Name`"""
        self["Cooling Combination Ratio Correction Factor Curve Name"] = value

    @property
    def cooling_partload_fraction_correlation_curve_name(self):
        """field `Cooling Part-Load Fraction Correlation Curve Name`

        |  This curve defines the cycling losses when the heat pump compressor cycles on and off
        |  below the Minimum Heat Pump Part-Load Ratio specified in the field below.

        Args:
            value (str): value for IDD Field `Cooling Part-Load Fraction Correlation Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `cooling_partload_fraction_correlation_curve_name` or None if not set
        """
        return self["Cooling Part-Load Fraction Correlation Curve Name"]

    @cooling_partload_fraction_correlation_curve_name.setter
    def cooling_partload_fraction_correlation_curve_name(self, value=None):
        """  Corresponds to IDD field `Cooling Part-Load Fraction Correlation Curve Name`

        """
        self["Cooling Part-Load Fraction Correlation Curve Name"] = value

    @property
    def gross_rated_heating_capacity(self):
        """field `Gross Rated Heating Capacity`

        |  Enter the heating capacity in watts at rated conditions or set to autosize.
        |  Heating capacity not accounting for the effect of supply air fan heat
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Gross Rated Heating Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `gross_rated_heating_capacity` or None if not set

        """
        return self["Gross Rated Heating Capacity"]

    @gross_rated_heating_capacity.setter
    def gross_rated_heating_capacity(self, value=None):
        """Corresponds to IDD field `Gross Rated Heating Capacity`"""
        self["Gross Rated Heating Capacity"] = value

    @property
    def rated_heating_capacity_sizing_ratio(self):
        """field `Rated Heating Capacity Sizing Ratio`

        |  If the Gross Rated Heating Capacity is autosized, the heating capacity is sized
        |  to be equal to the cooling capacity multiplied by this sizing ratio. The zone
        |  terminal unit heating coils are also sized using this ratio unless the sizing
        |  ratio input in the ZoneHVAC:TerminalUnit:VariableRefrigerantFlow object is entered.
        |  Units: W/W
        |  Default value: 1.0
        |  value >= 1.0

        Args:
            value (float): value for IDD Field `Rated Heating Capacity Sizing Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_heating_capacity_sizing_ratio` or None if not set

        """
        return self["Rated Heating Capacity Sizing Ratio"]

    @rated_heating_capacity_sizing_ratio.setter
    def rated_heating_capacity_sizing_ratio(self, value=1.0):
        """Corresponds to IDD field `Rated Heating Capacity Sizing Ratio`"""
        self["Rated Heating Capacity Sizing Ratio"] = value

    @property
    def gross_rated_heating_cop(self):
        """field `Gross Rated Heating COP`

        |  COP includes compressor and condenser fan electrical energy input
        |  COP does not include supply fan heat or supply fan electrical energy input
        |  Units: W/W
        |  Default value: 3.4

        Args:
            value (float): value for IDD Field `Gross Rated Heating COP`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `gross_rated_heating_cop` or None if not set

        """
        return self["Gross Rated Heating COP"]

    @gross_rated_heating_cop.setter
    def gross_rated_heating_cop(self, value=3.4):
        """Corresponds to IDD field `Gross Rated Heating COP`"""
        self["Gross Rated Heating COP"] = value

    @property
    def minimum_outdoor_temperature_in_heating_mode(self):
        """field `Minimum Outdoor Temperature in Heating Mode`

        |  Enter the minimum outdoor temperature allowed for heating operation.
        |  Units: C
        |  Default value: -20.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Temperature in Heating Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_temperature_in_heating_mode` or None if not set

        """
        return self["Minimum Outdoor Temperature in Heating Mode"]

    @minimum_outdoor_temperature_in_heating_mode.setter
    def minimum_outdoor_temperature_in_heating_mode(self, value=-20.0):
        """Corresponds to IDD field `Minimum Outdoor Temperature in Heating
        Mode`"""
        self["Minimum Outdoor Temperature in Heating Mode"] = value

    @property
    def maximum_outdoor_temperature_in_heating_mode(self):
        """field `Maximum Outdoor Temperature in Heating Mode`

        |  Enter the maximum outdoor temperature allowed for heating operation.
        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Temperature in Heating Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_temperature_in_heating_mode` or None if not set

        """
        return self["Maximum Outdoor Temperature in Heating Mode"]

    @maximum_outdoor_temperature_in_heating_mode.setter
    def maximum_outdoor_temperature_in_heating_mode(self, value=16.0):
        """Corresponds to IDD field `Maximum Outdoor Temperature in Heating
        Mode`"""
        self["Maximum Outdoor Temperature in Heating Mode"] = value

    @property
    def heating_capacity_ratio_modifier_function_of_low_temperature_curve_name(
            self):
        """field `Heating Capacity Ratio Modifier Function of Low Temperature
        Curve Name`

        |  Enter a curve name that represents full load heating capacity ratio as a
        |  function of outdoor wet-bulb temperature and indoor dry-bulb temperature.
        |  Outdoor dry-bulb temperature may be used if wet-bulb temperature data is unavailable.
        |  See Heating Performance Curve Outdoor Temperature Type input below to determine which
        |  outdoor temperature type to use.
        |  Up to two curves are allowed if the performance cannot be represented by a single curve.
        |  The following two fields are used if two curves are required.

        Args:
            value (str): value for IDD Field `Heating Capacity Ratio Modifier Function of Low Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_capacity_ratio_modifier_function_of_low_temperature_curve_name` or None if not set

        """
        return self[
            "Heating Capacity Ratio Modifier Function of Low Temperature Curve Name"]

    @heating_capacity_ratio_modifier_function_of_low_temperature_curve_name.setter
    def heating_capacity_ratio_modifier_function_of_low_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Heating Capacity Ratio Modifier Function
        of Low Temperature Curve Name`"""
        self[
            "Heating Capacity Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def heating_capacity_ratio_boundary_curve_name(self):
        """field `Heating Capacity Ratio Boundary Curve Name`

        |  This curve object is used to allow separate low and high heating capacity ratio
        |  performance curves. This curve represents a line passing through the points where
        |  performance changes. The curve calculates outdoor dry-bulb or wet-bulb temperature
        |  given weighted average indoor dry-bulb temperature. See Heating Performance Curve
        |  Outdoor Temperature Type input below to determine which outdoor temperature type to use.
        |  If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `Heating Capacity Ratio Boundary Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_capacity_ratio_boundary_curve_name` or None if not set

        """
        return self["Heating Capacity Ratio Boundary Curve Name"]

    @heating_capacity_ratio_boundary_curve_name.setter
    def heating_capacity_ratio_boundary_curve_name(self, value=None):
        """Corresponds to IDD field `Heating Capacity Ratio Boundary Curve
        Name`"""
        self["Heating Capacity Ratio Boundary Curve Name"] = value

    @property
    def heating_capacity_ratio_modifier_function_of_high_temperature_curve_name(
            self):
        """field `Heating Capacity Ratio Modifier Function of High Temperature
        Curve Name`

        |  This curve object is used to describe the high outdoor temperature
        |  performance curve used to describe heating capacity ratio.
        |  This curve is used when a single performance curve does not accurately describe
        |  heating capacity ratio as a function of temperature.
        |  If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `Heating Capacity Ratio Modifier Function of High Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_capacity_ratio_modifier_function_of_high_temperature_curve_name` or None if not set

        """
        return self[
            "Heating Capacity Ratio Modifier Function of High Temperature Curve Name"]

    @heating_capacity_ratio_modifier_function_of_high_temperature_curve_name.setter
    def heating_capacity_ratio_modifier_function_of_high_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Heating Capacity Ratio Modifier Function
        of High Temperature Curve Name`"""
        self[
            "Heating Capacity Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name(
            self):
        """field `Heating Energy Input Ratio Modifier Function of Low
        Temperature Curve Name`

        |  Enter a curve name that represents heating energy ratio as a function of
        |  outdoor wet-bulb temperature and indoor dry-bulb temperature
        |  Outdoor dry-bulb temperature may be used if wet-bulb temperature data is unavailable.
        |  See Heating Performance Curve Outdoor Temperature Type input below to determine which
        |  outdoor temperature type to use.

        Args:
            value (str): value for IDD Field `Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name` or None if not set

        """
        return self[
            "Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Heating Energy Input Ratio Modifier
        Function of Low Temperature Curve Name`"""
        self[
            "Heating Energy Input Ratio Modifier Function of Low Temperature Curve Name"] = value

    @property
    def heating_energy_input_ratio_boundary_curve_name(self):
        """field `Heating Energy Input Ratio Boundary Curve Name`

        |  This curve object is used to allow separate low and high heating energy input ratio
        |  performance curves. This curve represents a line passing through the points where
        |  performance changes. The curve calculates outdoor dry-bulb or wet-bulb temperature
        |  given weighted average indoor dry-bulb temperature. See Heating Performance Curve
        |  Outdoor Temperature Type input below to determine which outdoor temperature type to use.
        |  If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `Heating Energy Input Ratio Boundary Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_energy_input_ratio_boundary_curve_name` or None if not set

        """
        return self["Heating Energy Input Ratio Boundary Curve Name"]

    @heating_energy_input_ratio_boundary_curve_name.setter
    def heating_energy_input_ratio_boundary_curve_name(self, value=None):
        """Corresponds to IDD field `Heating Energy Input Ratio Boundary Curve
        Name`"""
        self["Heating Energy Input Ratio Boundary Curve Name"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name(
            self):
        """field `Heating Energy Input Ratio Modifier Function of High
        Temperature Curve Name`

        |  This curve object is used to allow separate performance curves for heating energy.
        |  If a single performance curve is used, leave this field blank.

        Args:
            value (str): value for IDD Field `Heating Energy Input Ratio Modifier Function of High Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name` or None if not set

        """
        return self[
            "Heating Energy Input Ratio Modifier Function of High Temperature Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Heating Energy Input Ratio Modifier
        Function of High Temperature Curve Name`"""
        self[
            "Heating Energy Input Ratio Modifier Function of High Temperature Curve Name"] = value

    @property
    def heating_performance_curve_outdoor_temperature_type(self):
        """field `Heating Performance Curve Outdoor Temperature Type`

        |  Determines temperature type for heating capacity curves and heating energy curves.
        |  This input determines whether the outdoor air dry-bulb or wet-bulb temperature
        |  is used to evaluate these curves.
        |  Default value: WetBulbTemperature

        Args:
            value (str): value for IDD Field `Heating Performance Curve Outdoor Temperature Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_performance_curve_outdoor_temperature_type` or None if not set

        """
        return self["Heating Performance Curve Outdoor Temperature Type"]

    @heating_performance_curve_outdoor_temperature_type.setter
    def heating_performance_curve_outdoor_temperature_type(
            self,
            value="WetBulbTemperature"):
        """Corresponds to IDD field `Heating Performance Curve Outdoor
        Temperature Type`"""
        self["Heating Performance Curve Outdoor Temperature Type"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(
            self):
        """field `Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name`

        |  This curve represents the heating energy input ratio for part-load ratios less than 1.

        Args:
            value (str): value for IDD Field `Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name` or None if not set
        """
        return self[
            "Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_low_partload_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name`

        """
        self[
            "Heating Energy Input Ratio Modifier Function of Low Part-Load Ratio Curve Name"] = value

    @property
    def heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(
            self):
        """field `Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name`

        |  This curve represents the heating energy input ratio for part-load ratios greater than 1.

        Args:
            value (str): value for IDD Field `Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name` or None if not set
        """
        return self[
            "Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"]

    @heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name.setter
    def heating_energy_input_ratio_modifier_function_of_high_partload_ratio_curve_name(
            self,
            value=None):
        """  Corresponds to IDD field `Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name`

        """
        self[
            "Heating Energy Input Ratio Modifier Function of High Part-Load Ratio Curve Name"] = value

    @property
    def heating_combination_ratio_correction_factor_curve_name(self):
        """field `Heating Combination Ratio Correction Factor Curve Name`

        |  This curve defines how rated capacity changes when the total indoor terminal unit heating
        |  capacity is greater than the Gross Rated Heating Capacity defined in this object.
        |  If this field is left blank, the model assumes total indoor terminal unit heating
        |  capacity is equal to the Gross Rated Heating Capacity defined above.

        Args:
            value (str): value for IDD Field `Heating Combination Ratio Correction Factor Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_combination_ratio_correction_factor_curve_name` or None if not set

        """
        return self["Heating Combination Ratio Correction Factor Curve Name"]

    @heating_combination_ratio_correction_factor_curve_name.setter
    def heating_combination_ratio_correction_factor_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Heating Combination Ratio Correction
        Factor Curve Name`"""
        self["Heating Combination Ratio Correction Factor Curve Name"] = value

    @property
    def heating_partload_fraction_correlation_curve_name(self):
        """field `Heating Part-Load Fraction Correlation Curve Name`

        |  This curve defines the cycling losses when the heat pump compressor cycles on and off
        |  below the Minimum Heat Pump Part-Load Ratio specified in the following field.

        Args:
            value (str): value for IDD Field `Heating Part-Load Fraction Correlation Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heating_partload_fraction_correlation_curve_name` or None if not set
        """
        return self["Heating Part-Load Fraction Correlation Curve Name"]

    @heating_partload_fraction_correlation_curve_name.setter
    def heating_partload_fraction_correlation_curve_name(self, value=None):
        """  Corresponds to IDD field `Heating Part-Load Fraction Correlation Curve Name`

        """
        self["Heating Part-Load Fraction Correlation Curve Name"] = value

    @property
    def minimum_heat_pump_partload_ratio(self):
        """field `Minimum Heat Pump Part-Load Ratio`

        |  Enter the minimum heat pump part-load ratio (PLR). When the cooling or heating PLR is
        |  below this value, the heat pump compressor will cycle to meet the cooling or heating
        |  demand.
        |  Units: dimensionless
        |  Default value: 0.15

        Args:
            value (float): value for IDD Field `Minimum Heat Pump Part-Load Ratio`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_heat_pump_partload_ratio` or None if not set
        """
        return self["Minimum Heat Pump Part-Load Ratio"]

    @minimum_heat_pump_partload_ratio.setter
    def minimum_heat_pump_partload_ratio(self, value=0.15):
        """  Corresponds to IDD field `Minimum Heat Pump Part-Load Ratio`

        """
        self["Minimum Heat Pump Part-Load Ratio"] = value

    @property
    def zone_name_for_master_thermostat_location(self):
        """field `Zone Name for Master Thermostat Location`

        |  Enter the name of the zone where the master thermostat is located.

        Args:
            value (str): value for IDD Field `Zone Name for Master Thermostat Location`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_name_for_master_thermostat_location` or None if not set

        """
        return self["Zone Name for Master Thermostat Location"]

    @zone_name_for_master_thermostat_location.setter
    def zone_name_for_master_thermostat_location(self, value=None):
        """Corresponds to IDD field `Zone Name for Master Thermostat
        Location`"""
        self["Zone Name for Master Thermostat Location"] = value

    @property
    def master_thermostat_priority_control_type(self):
        """field `Master Thermostat Priority Control Type`

        |  Choose a thermostat control logic scheme. If these control types fail to control zone
        |  temperature within a reasonable limit, consider using multiple VRF systems
        |  Default value: MasterThermostatPriority

        Args:
            value (str): value for IDD Field `Master Thermostat Priority Control Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `master_thermostat_priority_control_type` or None if not set

        """
        return self["Master Thermostat Priority Control Type"]

    @master_thermostat_priority_control_type.setter
    def master_thermostat_priority_control_type(
            self,
            value="MasterThermostatPriority"):
        """Corresponds to IDD field `Master Thermostat Priority Control
        Type`"""
        self["Master Thermostat Priority Control Type"] = value

    @property
    def thermostat_priority_schedule_name(self):
        """field `Thermostat Priority Schedule Name`

        |  this field is required if Master Thermostat Priority Control Type is Scheduled.
        |  Schedule values of 0 denote cooling, 1 for heating, and all other values disable the system.

        Args:
            value (str): value for IDD Field `Thermostat Priority Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `thermostat_priority_schedule_name` or None if not set

        """
        return self["Thermostat Priority Schedule Name"]

    @thermostat_priority_schedule_name.setter
    def thermostat_priority_schedule_name(self, value=None):
        """Corresponds to IDD field `Thermostat Priority Schedule Name`"""
        self["Thermostat Priority Schedule Name"] = value

    @property
    def zone_terminal_unit_list_name(self):
        """field `Zone Terminal Unit List Name`

        |  Enter the name of a ZoneTerminalUnitList. This list connects zone terminal units to this
        |  heat pump.

        Args:
            value (str): value for IDD Field `Zone Terminal Unit List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_terminal_unit_list_name` or None if not set

        """
        return self["Zone Terminal Unit List Name"]

    @zone_terminal_unit_list_name.setter
    def zone_terminal_unit_list_name(self, value=None):
        """Corresponds to IDD field `Zone Terminal Unit List Name`"""
        self["Zone Terminal Unit List Name"] = value

    @property
    def heat_pump_waste_heat_recovery(self):
        """field `Heat Pump Waste Heat Recovery`

        |  This field enables heat recovery operation within this VRF outdoor unit.
        |  Default value: No

        Args:
            value (str): value for IDD Field `Heat Pump Waste Heat Recovery`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_pump_waste_heat_recovery` or None if not set

        """
        return self["Heat Pump Waste Heat Recovery"]

    @heat_pump_waste_heat_recovery.setter
    def heat_pump_waste_heat_recovery(self, value="No"):
        """Corresponds to IDD field `Heat Pump Waste Heat Recovery`"""
        self["Heat Pump Waste Heat Recovery"] = value

    @property
    def equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode(
            self):
        """field `Equivalent Piping Length used for Piping Correction Factor in
        Cooling Mode`

        |  Enter the equivalent length of the farthest terminal unit from the condenser
        |  Units: m

        Args:
            value (float): value for IDD Field `Equivalent Piping Length used for Piping Correction Factor in Cooling Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode` or None if not set

        """
        return self[
            "Equivalent Piping Length used for Piping Correction Factor in Cooling Mode"]

    @equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode.setter
    def equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode(
            self,
            value=None):
        """Corresponds to IDD field `Equivalent Piping Length used for Piping
        Correction Factor in Cooling Mode`"""
        self[
            "Equivalent Piping Length used for Piping Correction Factor in Cooling Mode"] = value

    @property
    def vertical_height_used_for_piping_correction_factor(self):
        """field `Vertical Height used for Piping Correction Factor`

        |  Enter the height difference between the highest and lowest terminal unit
        |  Units: m

        Args:
            value (float): value for IDD Field `Vertical Height used for Piping Correction Factor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `vertical_height_used_for_piping_correction_factor` or None if not set

        """
        return self["Vertical Height used for Piping Correction Factor"]

    @vertical_height_used_for_piping_correction_factor.setter
    def vertical_height_used_for_piping_correction_factor(self, value=None):
        """Corresponds to IDD field `Vertical Height used for Piping Correction
        Factor`"""
        self["Vertical Height used for Piping Correction Factor"] = value

    @property
    def piping_correction_factor_for_length_in_cooling_mode_curve_name(self):
        """field `Piping Correction Factor for Length in Cooling Mode Curve
        Name`

        |  PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        |  PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR)
        |  where L = length and CR = combination ratio
        |  specifies coefficients for a0, a1, a2, and a3 in the PCF equation

        Args:
            value (str): value for IDD Field `Piping Correction Factor for Length in Cooling Mode Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `piping_correction_factor_for_length_in_cooling_mode_curve_name` or None if not set

        """
        return self[
            "Piping Correction Factor for Length in Cooling Mode Curve Name"]

    @piping_correction_factor_for_length_in_cooling_mode_curve_name.setter
    def piping_correction_factor_for_length_in_cooling_mode_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Piping Correction Factor for Length in
        Cooling Mode Curve Name`"""
        self[
            "Piping Correction Factor for Length in Cooling Mode Curve Name"] = value

    @property
    def piping_correction_factor_for_height_in_cooling_mode_coefficient(self):
        """field `Piping Correction Factor for Height in Cooling Mode
        Coefficient`

        |  PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        |  PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H
        |  where L = length, H = height, and CR = combination ratio
        |  specifies coefficient a4 (or a6 for biquadratic) in the PCF equation
        |  Units: 1/m

        Args:
            value (float): value for IDD Field `Piping Correction Factor for Height in Cooling Mode Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `piping_correction_factor_for_height_in_cooling_mode_coefficient` or None if not set

        """
        return self[
            "Piping Correction Factor for Height in Cooling Mode Coefficient"]

    @piping_correction_factor_for_height_in_cooling_mode_coefficient.setter
    def piping_correction_factor_for_height_in_cooling_mode_coefficient(
            self,
            value=None):
        """Corresponds to IDD field `Piping Correction Factor for Height in
        Cooling Mode Coefficient`"""
        self[
            "Piping Correction Factor for Height in Cooling Mode Coefficient"] = value

    @property
    def equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode(
            self):
        """field `Equivalent Piping Length used for Piping Correction Factor in
        Heating Mode`

        |  Enter the equivalent length of the farthest terminal unit from the condenser
        |  Units: m

        Args:
            value (float): value for IDD Field `Equivalent Piping Length used for Piping Correction Factor in Heating Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode` or None if not set

        """
        return self[
            "Equivalent Piping Length used for Piping Correction Factor in Heating Mode"]

    @equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode.setter
    def equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode(
            self,
            value=None):
        """Corresponds to IDD field `Equivalent Piping Length used for Piping
        Correction Factor in Heating Mode`"""
        self[
            "Equivalent Piping Length used for Piping Correction Factor in Heating Mode"] = value

    @property
    def piping_correction_factor_for_length_in_heating_mode_curve_name(self):
        """field `Piping Correction Factor for Length in Heating Mode Curve
        Name`

        |  PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        |  PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H
        |  where L = length and CR = combination ratio
        |  specifies coefficients for a0, a1, a2, and a3 (or a0-a5 for biquadratic) in the PCF equation

        Args:
            value (str): value for IDD Field `Piping Correction Factor for Length in Heating Mode Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `piping_correction_factor_for_length_in_heating_mode_curve_name` or None if not set

        """
        return self[
            "Piping Correction Factor for Length in Heating Mode Curve Name"]

    @piping_correction_factor_for_length_in_heating_mode_curve_name.setter
    def piping_correction_factor_for_length_in_heating_mode_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Piping Correction Factor for Length in
        Heating Mode Curve Name`"""
        self[
            "Piping Correction Factor for Length in Heating Mode Curve Name"] = value

    @property
    def piping_correction_factor_for_height_in_heating_mode_coefficient(self):
        """field `Piping Correction Factor for Height in Heating Mode
        Coefficient`

        |  PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H
        |  PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H
        |  where L = length, H = height, and CR = combination ratio
        |  specifies coefficient a4 (or a6 for biquadratic) in the PCF equation
        |  Units: 1/m

        Args:
            value (float): value for IDD Field `Piping Correction Factor for Height in Heating Mode Coefficient`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `piping_correction_factor_for_height_in_heating_mode_coefficient` or None if not set

        """
        return self[
            "Piping Correction Factor for Height in Heating Mode Coefficient"]

    @piping_correction_factor_for_height_in_heating_mode_coefficient.setter
    def piping_correction_factor_for_height_in_heating_mode_coefficient(
            self,
            value=None):
        """Corresponds to IDD field `Piping Correction Factor for Height in
        Heating Mode Coefficient`"""
        self[
            "Piping Correction Factor for Height in Heating Mode Coefficient"] = value

    @property
    def crankcase_heater_power_per_compressor(self):
        """field `Crankcase Heater Power per Compressor`

        |  Enter the value of the resistive heater located in the compressor(s). This heater
        |  is used to warm the refrigerant and oil when the compressor is off.
        |  Units: W
        |  Default value: 33.0

        Args:
            value (float): value for IDD Field `Crankcase Heater Power per Compressor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `crankcase_heater_power_per_compressor` or None if not set

        """
        return self["Crankcase Heater Power per Compressor"]

    @crankcase_heater_power_per_compressor.setter
    def crankcase_heater_power_per_compressor(self, value=33.0):
        """Corresponds to IDD field `Crankcase Heater Power per Compressor`"""
        self["Crankcase Heater Power per Compressor"] = value

    @property
    def number_of_compressors(self):
        """field `Number of Compressors`

        |  Enter the total number of compressor. This input is used only for crankcase
        |  heater calculations.
        |  Units: dimensionless
        |  Default value: 2

        Args:
            value (int): value for IDD Field `Number of Compressors`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_compressors` or None if not set

        """
        return self["Number of Compressors"]

    @number_of_compressors.setter
    def number_of_compressors(self, value=2):
        """Corresponds to IDD field `Number of Compressors`"""
        self["Number of Compressors"] = value

    @property
    def ratio_of_compressor_size_to_total_compressor_capacity(self):
        """field `Ratio of Compressor Size to Total Compressor Capacity`

        |  Enter the ratio of the first stage compressor to total compressor capacity.
        |  All other compressors are assumed to be equally sized. This inputs is used
        |  only for crankcase heater calculations.
        |  Units: W/W
        |  Default value: 0.5

        Args:
            value (float): value for IDD Field `Ratio of Compressor Size to Total Compressor Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ratio_of_compressor_size_to_total_compressor_capacity` or None if not set

        """
        return self["Ratio of Compressor Size to Total Compressor Capacity"]

    @ratio_of_compressor_size_to_total_compressor_capacity.setter
    def ratio_of_compressor_size_to_total_compressor_capacity(self, value=0.5):
        """Corresponds to IDD field `Ratio of Compressor Size to Total
        Compressor Capacity`"""
        self["Ratio of Compressor Size to Total Compressor Capacity"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_crankcase_heater(self):
        """field `Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater`

        |  Enter the maximum outdoor temperature above which the crankcase heaters are disabled.
        |  Units: C
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_crankcase_heater` or None if not set
        """
        return self[
            "Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"]

    @maximum_outdoor_drybulb_temperature_for_crankcase_heater.setter
    def maximum_outdoor_drybulb_temperature_for_crankcase_heater(
            self,
            value=5.0):
        """  Corresponds to IDD field `Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater`

        """
        self[
            "Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"] = value

    @property
    def defrost_strategy(self):
        """field `Defrost Strategy`

        |  Select a defrost strategy. Reverse cycle reverses the operating mode from heating to cooling
        |  to melt frost formation on the condenser coil. The resistive strategy uses a resistive heater
        |  to melt the frost.
        |  Default value: Resistive

        Args:
            value (str): value for IDD Field `Defrost Strategy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_strategy` or None if not set

        """
        return self["Defrost Strategy"]

    @defrost_strategy.setter
    def defrost_strategy(self, value="Resistive"):
        """Corresponds to IDD field `Defrost Strategy`"""
        self["Defrost Strategy"] = value

    @property
    def defrost_control(self):
        """field `Defrost Control`

        |  Choose a defrost control type. Either use a fixed Timed defrost period or select
        |  OnDemand to defrost only when necessary.
        |  Default value: Timed

        Args:
            value (str): value for IDD Field `Defrost Control`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_control` or None if not set

        """
        return self["Defrost Control"]

    @defrost_control.setter
    def defrost_control(self, value="Timed"):
        """Corresponds to IDD field `Defrost Control`"""
        self["Defrost Control"] = value

    @property
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve_name(
            self):
        """field `Defrost Energy Input Ratio Modifier Function of Temperature
        Curve Name`

        |  A valid performance curve must be used if reversecycle defrost strategy is selected.

        Args:
            value (str): value for IDD Field `Defrost Energy Input Ratio Modifier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"]

    @defrost_energy_input_ratio_modifier_function_of_temperature_curve_name.setter
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Defrost Energy Input Ratio Modifier
        Function of Temperature Curve Name`"""
        self[
            "Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"] = value

    @property
    def defrost_time_period_fraction(self):
        """field `Defrost Time Period Fraction`

        |  Fraction of time in defrost mode.
        |  Only applicable if timed defrost control is specified.
        |  Units: dimensionless
        |  Default value: 0.058333

        Args:
            value (float): value for IDD Field `Defrost Time Period Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `defrost_time_period_fraction` or None if not set

        """
        return self["Defrost Time Period Fraction"]

    @defrost_time_period_fraction.setter
    def defrost_time_period_fraction(self, value=0.058333):
        """Corresponds to IDD field `Defrost Time Period Fraction`"""
        self["Defrost Time Period Fraction"] = value

    @property
    def resistive_defrost_heater_capacity(self):
        """field `Resistive Defrost Heater Capacity`

        |  Enter the size of the resistive defrost heating element.
        |  Only applicable if resistive defrost strategy is specified
        |  Units: W
        |  IP-Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Resistive Defrost Heater Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `resistive_defrost_heater_capacity` or None if not set

        """
        return self["Resistive Defrost Heater Capacity"]

    @resistive_defrost_heater_capacity.setter
    def resistive_defrost_heater_capacity(self, value=None):
        """Corresponds to IDD field `Resistive Defrost Heater Capacity`"""
        self["Resistive Defrost Heater Capacity"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_defrost_operation(self):
        """field `Maximum Outdoor Dry-bulb Temperature for Defrost Operation`

        |  Enter the maximum outdoor temperature above which defrost operation is disabled.
        |  Units: C
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-bulb Temperature for Defrost Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_defrost_operation` or None if not set
        """
        return self[
            "Maximum Outdoor Dry-bulb Temperature for Defrost Operation"]

    @maximum_outdoor_drybulb_temperature_for_defrost_operation.setter
    def maximum_outdoor_drybulb_temperature_for_defrost_operation(
            self,
            value=5.0):
        """  Corresponds to IDD field `Maximum Outdoor Dry-bulb Temperature for Defrost Operation`

        """
        self[
            "Maximum Outdoor Dry-bulb Temperature for Defrost Operation"] = value

    @property
    def condenser_type(self):
        """field `Condenser Type`

        |  Select either an air-cooled, evaporatively-cooled or water-cooled condenser.
        |  Default value: AirCooled

        Args:
            value (str): value for IDD Field `Condenser Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_type` or None if not set

        """
        return self["Condenser Type"]

    @condenser_type.setter
    def condenser_type(self, value="AirCooled"):
        """Corresponds to IDD field `Condenser Type`"""
        self["Condenser Type"] = value

    @property
    def condenser_inlet_node_name(self):
        """field `Condenser Inlet Node Name`

        |  Choose an outside air node name or leave this field blank to use weather data.
        |  If this field is blank, the Condenser Type is assumed to be AirCooled.
        |  This input must be specified if Condenser Type = WaterCooled.

        Args:
            value (str): value for IDD Field `Condenser Inlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_inlet_node_name` or None if not set

        """
        return self["Condenser Inlet Node Name"]

    @condenser_inlet_node_name.setter
    def condenser_inlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Inlet Node Name`"""
        self["Condenser Inlet Node Name"] = value

    @property
    def condenser_outlet_node_name(self):
        """field `Condenser Outlet Node Name`

        |  Enter a water outlet node name if Condenser Type = WaterCooled.
        |  Leave this field blank if Condenser Type = Air or EvaporativelyCooled.

        Args:
            value (str): value for IDD Field `Condenser Outlet Node Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `condenser_outlet_node_name` or None if not set

        """
        return self["Condenser Outlet Node Name"]

    @condenser_outlet_node_name.setter
    def condenser_outlet_node_name(self, value=None):
        """Corresponds to IDD field `Condenser Outlet Node Name`"""
        self["Condenser Outlet Node Name"] = value

    @property
    def water_condenser_volume_flow_rate(self):
        """field `Water Condenser Volume Flow Rate`

        |  Only used when Condenser Type = WaterCooled.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Water Condenser Volume Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `water_condenser_volume_flow_rate` or None if not set

        """
        return self["Water Condenser Volume Flow Rate"]

    @water_condenser_volume_flow_rate.setter
    def water_condenser_volume_flow_rate(self, value=None):
        """Corresponds to IDD field `Water Condenser Volume Flow Rate`"""
        self["Water Condenser Volume Flow Rate"] = value

    @property
    def evaporative_condenser_effectiveness(self):
        """field `Evaporative Condenser Effectiveness`

        |  Enter the effectiveness of the evaporatively cooled condenser.
        |  This field is only used when the Condenser Type = EvaporativelyCooled.
        |  Units: dimensionless
        |  Default value: 0.9
        |  value <= 1.0

        Args:
            value (float): value for IDD Field `Evaporative Condenser Effectiveness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `evaporative_condenser_effectiveness` or None if not set

        """
        return self["Evaporative Condenser Effectiveness"]

    @evaporative_condenser_effectiveness.setter
    def evaporative_condenser_effectiveness(self, value=0.9):
        """Corresponds to IDD field `Evaporative Condenser Effectiveness`"""
        self["Evaporative Condenser Effectiveness"] = value

    @property
    def evaporative_condenser_air_flow_rate(self):
        """field `Evaporative Condenser Air Flow Rate`

        |  Used to calculate evaporative condenser water use.
        |  This field is only used when the Condenser Type = EvaporativelyCooled.
        |  Units: m3/s

        Args:
            value (float or "Autosize"): value for IDD Field `Evaporative Condenser Air Flow Rate`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `evaporative_condenser_air_flow_rate` or None if not set

        """
        return self["Evaporative Condenser Air Flow Rate"]

    @evaporative_condenser_air_flow_rate.setter
    def evaporative_condenser_air_flow_rate(self, value=None):
        """Corresponds to IDD field `Evaporative Condenser Air Flow Rate`"""
        self["Evaporative Condenser Air Flow Rate"] = value

    @property
    def evaporative_condenser_pump_rated_power_consumption(self):
        """field `Evaporative Condenser Pump Rated Power Consumption`

        |  Rated power consumed by the evaporative condenser's water pump.
        |  This field is only used when the Condenser Type = EvaporativelyCooled.
        |  Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Evaporative Condenser Pump Rated Power Consumption`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `evaporative_condenser_pump_rated_power_consumption` or None if not set

        """
        return self["Evaporative Condenser Pump Rated Power Consumption"]

    @evaporative_condenser_pump_rated_power_consumption.setter
    def evaporative_condenser_pump_rated_power_consumption(self, value=None):
        """Corresponds to IDD field `Evaporative Condenser Pump Rated Power
        Consumption`"""
        self["Evaporative Condenser Pump Rated Power Consumption"] = value

    @property
    def supply_water_storage_tank_name(self):
        """field `Supply Water Storage Tank Name`

        |  A separate storage tank may be used to supply an evaporatively cooled condenser.

        Args:
            value (str): value for IDD Field `Supply Water Storage Tank Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `supply_water_storage_tank_name` or None if not set

        """
        return self["Supply Water Storage Tank Name"]

    @supply_water_storage_tank_name.setter
    def supply_water_storage_tank_name(self, value=None):
        """Corresponds to IDD field `Supply Water Storage Tank Name`"""
        self["Supply Water Storage Tank Name"] = value

    @property
    def basin_heater_capacity(self):
        """field `Basin Heater Capacity`

        |  This field is only used for Condenser Type = EvaporativelyCooled and for periods
        |  when the basin heater is available (field Basin Heater Operating Schedule Name).
        |  For this situation, the heater maintains the basin water temperature at the basin heater
        |  setpoint temperature when the outdoor air temperature falls below the setpoint temperature.
        |  The basin heater only operates when the DX coil is off.
        |  Units: W/K

        Args:
            value (float): value for IDD Field `Basin Heater Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basin_heater_capacity` or None if not set

        """
        return self["Basin Heater Capacity"]

    @basin_heater_capacity.setter
    def basin_heater_capacity(self, value=None):
        """Corresponds to IDD field `Basin Heater Capacity`"""
        self["Basin Heater Capacity"] = value

    @property
    def basin_heater_setpoint_temperature(self):
        """field `Basin Heater Setpoint Temperature`

        |  This field is only used for Condenser Type = EvaporativelyCooled.
        |  Enter the outdoor dry-bulb temperature when the basin heater turns on.
        |  Units: C
        |  Default value: 2.0
        |  value >= 2.0

        Args:
            value (float): value for IDD Field `Basin Heater Setpoint Temperature`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `basin_heater_setpoint_temperature` or None if not set

        """
        return self["Basin Heater Setpoint Temperature"]

    @basin_heater_setpoint_temperature.setter
    def basin_heater_setpoint_temperature(self, value=2.0):
        """Corresponds to IDD field `Basin Heater Setpoint Temperature`"""
        self["Basin Heater Setpoint Temperature"] = value

    @property
    def basin_heater_operating_schedule_name(self):
        """field `Basin Heater Operating Schedule Name`

        |  This field is only used for Condenser Type = EvaporativelyCooled.
        |  Schedule values greater than 0 allow the basin heater to operate whenever the outdoor
        |  air dry-bulb temperature is below the basin heater setpoint temperature.
        |  If a schedule name is not entered, the basin heater is allowed to operate
        |  throughout the entire simulation.

        Args:
            value (str): value for IDD Field `Basin Heater Operating Schedule Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `basin_heater_operating_schedule_name` or None if not set

        """
        return self["Basin Heater Operating Schedule Name"]

    @basin_heater_operating_schedule_name.setter
    def basin_heater_operating_schedule_name(self, value=None):
        """Corresponds to IDD field `Basin Heater Operating Schedule Name`"""
        self["Basin Heater Operating Schedule Name"] = value

    @property
    def fuel_type(self):
        """field `Fuel Type`

        |  Default value: Electricity

        Args:
            value (str): value for IDD Field `Fuel Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `fuel_type` or None if not set

        """
        return self["Fuel Type"]

    @fuel_type.setter
    def fuel_type(self, value="Electricity"):
        """Corresponds to IDD field `Fuel Type`"""
        self["Fuel Type"] = value

    @property
    def minimum_outdoor_temperature_in_heat_recovery_mode(self):
        """field `Minimum Outdoor Temperature in Heat Recovery Mode`

        |  The minimum outdoor temperature below which heat
        |  recovery mode will not operate.
        |  Units: C

        Args:
            value (float): value for IDD Field `Minimum Outdoor Temperature in Heat Recovery Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_temperature_in_heat_recovery_mode` or None if not set

        """
        return self["Minimum Outdoor Temperature in Heat Recovery Mode"]

    @minimum_outdoor_temperature_in_heat_recovery_mode.setter
    def minimum_outdoor_temperature_in_heat_recovery_mode(self, value=None):
        """Corresponds to IDD field `Minimum Outdoor Temperature in Heat
        Recovery Mode`"""
        self["Minimum Outdoor Temperature in Heat Recovery Mode"] = value

    @property
    def maximum_outdoor_temperature_in_heat_recovery_mode(self):
        """field `Maximum Outdoor Temperature in Heat Recovery Mode`

        |  The maximum outdoor temperature above which heat
        |  recovery mode will not operate.
        |  Units: C

        Args:
            value (float): value for IDD Field `Maximum Outdoor Temperature in Heat Recovery Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_temperature_in_heat_recovery_mode` or None if not set

        """
        return self["Maximum Outdoor Temperature in Heat Recovery Mode"]

    @maximum_outdoor_temperature_in_heat_recovery_mode.setter
    def maximum_outdoor_temperature_in_heat_recovery_mode(self, value=None):
        """Corresponds to IDD field `Maximum Outdoor Temperature in Heat
        Recovery Mode`"""
        self["Maximum Outdoor Temperature in Heat Recovery Mode"] = value

    @property
    def heat_recovery_cooling_capacity_modifier_curve_name(self):
        """field `Heat Recovery Cooling Capacity Modifier Curve Name`

        |  Enter the name of a performance curve which represents
        |  the change in cooling capacity when heat recovery is active
        |  A default constant of 0.9 is used if this input is blank

        Args:
            value (str): value for IDD Field `Heat Recovery Cooling Capacity Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_cooling_capacity_modifier_curve_name` or None if not set

        """
        return self["Heat Recovery Cooling Capacity Modifier Curve Name"]

    @heat_recovery_cooling_capacity_modifier_curve_name.setter
    def heat_recovery_cooling_capacity_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Cooling Capacity Modifier
        Curve Name`"""
        self["Heat Recovery Cooling Capacity Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_cooling_capacity_fraction(self):
        """field `Initial Heat Recovery Cooling Capacity Fraction`

        |  Enter the fractional capacity available at the start
        |  of heat recovery mode. The capacity exponentially approaches
        |  the steady-state value according to the inputs for
        |  Heat Recovery Cooling Capacity Modifier and Heat Recovery
        |  Cooling Capacity Time Constant
        |  Units: W/W
        |  Default value: 0.5

        Args:
            value (float): value for IDD Field `Initial Heat Recovery Cooling Capacity Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_heat_recovery_cooling_capacity_fraction` or None if not set

        """
        return self["Initial Heat Recovery Cooling Capacity Fraction"]

    @initial_heat_recovery_cooling_capacity_fraction.setter
    def initial_heat_recovery_cooling_capacity_fraction(self, value=0.5):
        """Corresponds to IDD field `Initial Heat Recovery Cooling Capacity
        Fraction`"""
        self["Initial Heat Recovery Cooling Capacity Fraction"] = value

    @property
    def heat_recovery_cooling_capacity_time_constant(self):
        """field `Heat Recovery Cooling Capacity Time Constant`

        |  Enter the time constant used to model the transition
        |  from cooling only mode to heat recovery mode
        |  Units: hr
        |  Default value: 0.15

        Args:
            value (float): value for IDD Field `Heat Recovery Cooling Capacity Time Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_recovery_cooling_capacity_time_constant` or None if not set

        """
        return self["Heat Recovery Cooling Capacity Time Constant"]

    @heat_recovery_cooling_capacity_time_constant.setter
    def heat_recovery_cooling_capacity_time_constant(self, value=0.15):
        """Corresponds to IDD field `Heat Recovery Cooling Capacity Time
        Constant`"""
        self["Heat Recovery Cooling Capacity Time Constant"] = value

    @property
    def heat_recovery_cooling_energy_modifier_curve_name(self):
        """field `Heat Recovery Cooling Energy Modifier Curve Name`

        |  Enter the name of a performance curve which represents
        |  the change in cooling energy when heat recovery is active
        |  A default constant of 1.1 is used if this input is blank

        Args:
            value (str): value for IDD Field `Heat Recovery Cooling Energy Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_cooling_energy_modifier_curve_name` or None if not set

        """
        return self["Heat Recovery Cooling Energy Modifier Curve Name"]

    @heat_recovery_cooling_energy_modifier_curve_name.setter
    def heat_recovery_cooling_energy_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Cooling Energy Modifier
        Curve Name`"""
        self["Heat Recovery Cooling Energy Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_cooling_energy_fraction(self):
        """field `Initial Heat Recovery Cooling Energy Fraction`

        |  Enter the fractional electric consumption rate at the start
        |  of heat recovery mode. The electric consumption rate exponentially
        |  approaches the steady-state value according to the inputs for
        |  Heat Recovery Cooling Energy Modifier and Heat Recovery
        |  Cooling Energy Time Constant
        |  Units: W/W
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Initial Heat Recovery Cooling Energy Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_heat_recovery_cooling_energy_fraction` or None if not set

        """
        return self["Initial Heat Recovery Cooling Energy Fraction"]

    @initial_heat_recovery_cooling_energy_fraction.setter
    def initial_heat_recovery_cooling_energy_fraction(self, value=1.0):
        """Corresponds to IDD field `Initial Heat Recovery Cooling Energy
        Fraction`"""
        self["Initial Heat Recovery Cooling Energy Fraction"] = value

    @property
    def heat_recovery_cooling_energy_time_constant(self):
        """field `Heat Recovery Cooling Energy Time Constant`

        |  Enter the time constant used to model the transition
        |  from cooling only mode to heat recovery mode
        |  Units: hr

        Args:
            value (float): value for IDD Field `Heat Recovery Cooling Energy Time Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_recovery_cooling_energy_time_constant` or None if not set

        """
        return self["Heat Recovery Cooling Energy Time Constant"]

    @heat_recovery_cooling_energy_time_constant.setter
    def heat_recovery_cooling_energy_time_constant(self, value=None):
        """Corresponds to IDD field `Heat Recovery Cooling Energy Time
        Constant`"""
        self["Heat Recovery Cooling Energy Time Constant"] = value

    @property
    def heat_recovery_heating_capacity_modifier_curve_name(self):
        """field `Heat Recovery Heating Capacity Modifier Curve Name`

        |  Enter the name of a performance curve which represents
        |  the change in heating capacity when heat recovery is active
        |  A default constant of 1.1 is used if this input is blank

        Args:
            value (str): value for IDD Field `Heat Recovery Heating Capacity Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_heating_capacity_modifier_curve_name` or None if not set

        """
        return self["Heat Recovery Heating Capacity Modifier Curve Name"]

    @heat_recovery_heating_capacity_modifier_curve_name.setter
    def heat_recovery_heating_capacity_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Heating Capacity Modifier
        Curve Name`"""
        self["Heat Recovery Heating Capacity Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_heating_capacity_fraction(self):
        """field `Initial Heat Recovery Heating Capacity Fraction`

        |  Enter the fractional capacity available at the start
        |  of heat recovery mode. The capacity exponentially approaches
        |  the steady-state value according to the inputs for
        |  Heat Recovery Heating Capacity Modifier and Heat Recovery
        |  Heating Capacity Time Constant
        |  Units: W/W
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Initial Heat Recovery Heating Capacity Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_heat_recovery_heating_capacity_fraction` or None if not set

        """
        return self["Initial Heat Recovery Heating Capacity Fraction"]

    @initial_heat_recovery_heating_capacity_fraction.setter
    def initial_heat_recovery_heating_capacity_fraction(self, value=1.0):
        """Corresponds to IDD field `Initial Heat Recovery Heating Capacity
        Fraction`"""
        self["Initial Heat Recovery Heating Capacity Fraction"] = value

    @property
    def heat_recovery_heating_capacity_time_constant(self):
        """field `Heat Recovery Heating Capacity Time Constant`

        |  Enter the time constant used to model the transition
        |  from cooling only mode to heat recovery mode
        |  Units: hr
        |  Default value: 0.15

        Args:
            value (float): value for IDD Field `Heat Recovery Heating Capacity Time Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_recovery_heating_capacity_time_constant` or None if not set

        """
        return self["Heat Recovery Heating Capacity Time Constant"]

    @heat_recovery_heating_capacity_time_constant.setter
    def heat_recovery_heating_capacity_time_constant(self, value=0.15):
        """Corresponds to IDD field `Heat Recovery Heating Capacity Time
        Constant`"""
        self["Heat Recovery Heating Capacity Time Constant"] = value

    @property
    def heat_recovery_heating_energy_modifier_curve_name(self):
        """field `Heat Recovery Heating Energy Modifier Curve Name`

        |  Enter the name of a performance curve which represents
        |  the change in heating electric consumption rate when heat recovery is active
        |  A default constant of 1.1 is used if this input is blank

        Args:
            value (str): value for IDD Field `Heat Recovery Heating Energy Modifier Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_recovery_heating_energy_modifier_curve_name` or None if not set

        """
        return self["Heat Recovery Heating Energy Modifier Curve Name"]

    @heat_recovery_heating_energy_modifier_curve_name.setter
    def heat_recovery_heating_energy_modifier_curve_name(self, value=None):
        """Corresponds to IDD field `Heat Recovery Heating Energy Modifier
        Curve Name`"""
        self["Heat Recovery Heating Energy Modifier Curve Name"] = value

    @property
    def initial_heat_recovery_heating_energy_fraction(self):
        """field `Initial Heat Recovery Heating Energy Fraction`

        |  Enter the fractional electric consumption rate at the start
        |  of heat recovery mode. The electric consumption rate exponentially
        |  approaches the steady-state value according to the inputs for
        |  Heat Recovery Cooling Energy Modifier and Heat Recovery
        |  Cooling Energy Time Constant
        |  Units: W/W
        |  Default value: 1.0

        Args:
            value (float): value for IDD Field `Initial Heat Recovery Heating Energy Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `initial_heat_recovery_heating_energy_fraction` or None if not set

        """
        return self["Initial Heat Recovery Heating Energy Fraction"]

    @initial_heat_recovery_heating_energy_fraction.setter
    def initial_heat_recovery_heating_energy_fraction(self, value=1.0):
        """Corresponds to IDD field `Initial Heat Recovery Heating Energy
        Fraction`"""
        self["Initial Heat Recovery Heating Energy Fraction"] = value

    @property
    def heat_recovery_heating_energy_time_constant(self):
        """field `Heat Recovery Heating Energy Time Constant`

        |  Enter the time constant used to model the transition
        |  from cooling only mode to heat recovery mode
        |  Units: hr

        Args:
            value (float): value for IDD Field `Heat Recovery Heating Energy Time Constant`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `heat_recovery_heating_energy_time_constant` or None if not set

        """
        return self["Heat Recovery Heating Energy Time Constant"]

    @heat_recovery_heating_energy_time_constant.setter
    def heat_recovery_heating_energy_time_constant(self, value=None):
        """Corresponds to IDD field `Heat Recovery Heating Energy Time
        Constant`"""
        self["Heat Recovery Heating Energy Time Constant"] = value




class AirConditionerVariableRefrigerantFlowFluidTemperatureControl(DataObject):

    """ Corresponds to IDD object `AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl`
        This is a key object in the new physics based VRF model applicable for Fluid
        Temperature Control
        It describes the Variable Refrigerant Flow system excluding the performance of indoor units
        Indoor units are modeled separately, see ZoneHVAC:TerminalUnit:VariableRefrigerantFlow
    """
    _schema = {'extensible-fields': OrderedDict(),
               'fields': OrderedDict([(u'heat pump name',
                                       {'name': u'Heat Pump Name',
                                        'pyname': u'heat_pump_name',
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
                                      (u'zone terminal unit list name',
                                       {'name': u'Zone Terminal Unit List Name',
                                        'pyname': u'zone_terminal_unit_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'refrigerant type',
                                       {'name': u'Refrigerant Type',
                                        'pyname': u'refrigerant_type',
                                        'default': u'R410A',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'rated evaporative capacity',
                                       {'name': u'Rated Evaporative Capacity',
                                        'pyname': u'rated_evaporative_capacity',
                                        'default': 40000.0,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'rated compressor power per unit of rated evaporative capacity',
                                       {'name': u'Rated Compressor Power Per Unit of Rated Evaporative Capacity',
                                        'pyname': u'rated_compressor_power_per_unit_of_rated_evaporative_capacity',
                                        'default': 0.35,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'minimum outdoor air temperature in cooling mode',
                                       {'name': u'Minimum Outdoor Air Temperature in Cooling Mode',
                                        'pyname': u'minimum_outdoor_air_temperature_in_cooling_mode',
                                        'default': -6.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor air temperature in cooling mode',
                                       {'name': u'Maximum Outdoor Air Temperature in Cooling Mode',
                                        'pyname': u'maximum_outdoor_air_temperature_in_cooling_mode',
                                        'default': 43.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'minimum outdoor air temperature in heating mode',
                                       {'name': u'Minimum Outdoor Air Temperature in Heating Mode',
                                        'pyname': u'minimum_outdoor_air_temperature_in_heating_mode',
                                        'default': -20.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'maximum outdoor air temperature in heating mode',
                                       {'name': u'Maximum Outdoor Air Temperature in Heating Mode',
                                        'pyname': u'maximum_outdoor_air_temperature_in_heating_mode',
                                        'default': 16.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'reference outdoor unit superheating',
                                       {'name': u'Reference Outdoor Unit Superheating',
                                        'pyname': u'reference_outdoor_unit_superheating',
                                        'default': 3.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'reference outdoor unit subcooling',
                                       {'name': u'Reference Outdoor Unit Subcooling',
                                        'pyname': u'reference_outdoor_unit_subcooling',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'deltaC'}),
                                      (u'refrigerant temperature control algorithm for indoor unit',
                                       {'name': u'Refrigerant Temperature Control Algorithm for Indoor Unit',
                                        'pyname': u'refrigerant_temperature_control_algorithm_for_indoor_unit',
                                        'default': u'VariableTemp',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ConstantTemp',
                                                            u'VariableTemp'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'reference evaporating temperature for indoor unit',
                                       {'name': u'Reference Evaporating Temperature for Indoor Unit',
                                        'pyname': u'reference_evaporating_temperature_for_indoor_unit',
                                        'default': 6.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'reference condensing temperature for indoor unit',
                                       {'name': u'Reference Condensing Temperature for Indoor Unit',
                                        'pyname': u'reference_condensing_temperature_for_indoor_unit',
                                        'default': 44.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'variable evaporating temperature minimum for indoor unit',
                                       {'name': u'Variable Evaporating Temperature Minimum for Indoor Unit',
                                        'pyname': u'variable_evaporating_temperature_minimum_for_indoor_unit',
                                        'default': 4.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'variable evaporating temperature maximum for indoor unit',
                                       {'name': u'Variable Evaporating Temperature Maximum for Indoor Unit',
                                        'pyname': u'variable_evaporating_temperature_maximum_for_indoor_unit',
                                        'default': 13.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'variable condensing temperature minimum for indoor unit',
                                       {'name': u'Variable Condensing Temperature Minimum for Indoor Unit',
                                        'pyname': u'variable_condensing_temperature_minimum_for_indoor_unit',
                                        'default': 42.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'variable condensing temperature maximum for indoor unit',
                                       {'name': u'Variable Condensing Temperature Maximum for Indoor Unit',
                                        'pyname': u'variable_condensing_temperature_maximum_for_indoor_unit',
                                        'default': 46.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'outdoor unit fan power per unit of rated evaporative capacity',
                                       {'name': u'Outdoor Unit Fan Power Per Unit of Rated Evaporative Capacity',
                                        'pyname': u'outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity',
                                        'default': 0.00425,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'dimensionless'}),
                                      (u'outdoor unit fan flow rate per unit of rated evaporative capacity',
                                       {'name': u'Outdoor Unit Fan Flow Rate Per Unit of Rated Evaporative Capacity',
                                        'pyname': u'outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity',
                                        'default': 7.5e-05,
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm3/s-W'}),
                                      (u'outdoor unit evaporating temperature function of superheating curve name',
                                       {'name': u'Outdoor Unit Evaporating Temperature Function of Superheating Curve Name',
                                        'pyname': u'outdoor_unit_evaporating_temperature_function_of_superheating_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'outdoor unit condensing temperature function of subcooling curve name',
                                       {'name': u'Outdoor Unit Condensing Temperature Function of Subcooling Curve Name',
                                        'pyname': u'outdoor_unit_condensing_temperature_function_of_subcooling_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'diameter of main pipe connecting outdoor unit to indoor units',
                                       {'name': u'Diameter of Main Pipe Connecting Outdoor Unit to Indoor Units',
                                        'pyname': u'diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units',
                                        'default': 0.0762,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'length of main pipe connecting outdoor unit to indoor units',
                                       {'name': u'Length of Main Pipe Connecting Outdoor Unit to Indoor Units',
                                        'pyname': u'length_of_main_pipe_connecting_outdoor_unit_to_indoor_units',
                                        'default': 30.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'equivalent length of main pipe connecting outdoor unit to indoor units',
                                       {'name': u'Equivalent Length of Main Pipe Connecting Outdoor Unit to Indoor Units',
                                        'pyname': u'equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units',
                                        'default': 36.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'height difference between outdoor unit and indoor units',
                                       {'name': u'Height Difference Between Outdoor Unit and Indoor Units',
                                        'pyname': u'height_difference_between_outdoor_unit_and_indoor_units',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'main pipe insulation thickness',
                                       {'name': u'Main Pipe Insulation Thickness',
                                        'pyname': u'main_pipe_insulation_thickness',
                                        'default': 0.02,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'm'}),
                                      (u'main pipe insulation thermal conductivity',
                                       {'name': u'Main Pipe Insulation Thermal Conductivity',
                                        'pyname': u'main_pipe_insulation_thermal_conductivity',
                                        'default': 0.032,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/m-K'}),
                                      (u'crankcase heater power per compressor',
                                       {'name': u'Crankcase Heater Power per Compressor',
                                        'pyname': u'crankcase_heater_power_per_compressor',
                                        'default': 33.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'number of compressors',
                                       {'name': u'Number of Compressors',
                                        'pyname': u'number_of_compressors',
                                        'default': 2,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'integer',
                                        'unit': u'dimensionless'}),
                                      (u'ratio of compressor size to total compressor capacity',
                                       {'name': u'Ratio of Compressor Size to Total Compressor Capacity',
                                        'pyname': u'ratio_of_compressor_size_to_total_compressor_capacity',
                                        'default': 0.5,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W/W'}),
                                      (u'maximum outdoor dry-bulb temperature for crankcase heater',
                                       {'name': u'Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_crankcase_heater',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'defrost strategy',
                                       {'name': u'Defrost Strategy',
                                        'pyname': u'defrost_strategy',
                                        'default': u'Resistive',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'ReverseCycle',
                                                            u'Resistive'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost control',
                                       {'name': u'Defrost Control',
                                        'pyname': u'defrost_control',
                                        'default': u'Timed',
                                        'required-field': False,
                                        'autosizable': False,
                                        'accepted-values': [u'Timed',
                                                            u'OnDemand'],
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'defrost energy input ratio modifier function of temperature curve name',
                                       {'name': u'Defrost Energy Input Ratio Modifier Function of Temperature Curve Name',
                                        'pyname': u'defrost_energy_input_ratio_modifier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'defrost time period fraction',
                                       {'name': u'Defrost Time Period Fraction',
                                        'pyname': u'defrost_time_period_fraction',
                                        'default': 0.058333,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real'}),
                                      (u'resistive defrost heater capacity',
                                       {'name': u'Resistive Defrost Heater Capacity',
                                        'pyname': u'resistive_defrost_heater_capacity',
                                        'default': 0.0,
                                        'required-field': False,
                                        'autosizable': True,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'W'}),
                                      (u'maximum outdoor dry-bulb temperature for defrost operation',
                                       {'name': u'Maximum Outdoor Dry-bulb Temperature for Defrost Operation',
                                        'pyname': u'maximum_outdoor_drybulb_temperature_for_defrost_operation',
                                        'default': 5.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'C'}),
                                      (u'compressor maximum delta pressure',
                                       {'name': u'Compressor maximum delta Pressure',
                                        'pyname': u'compressor_maximum_delta_pressure',
                                        'default': 4500000.0,
                                        'maximum': 50000000.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'minimum': 0.0,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'Pa'}),
                                      (u'number of compressor loading index entries',
                                       {'name': u'Number of Compressor Loading Index Entries',
                                        'pyname': u'number_of_compressor_loading_index_entries',
                                        'default': 2,
                                        'maximum': 9,
                                        'required-field': True,
                                        'autosizable': False,
                                        'minimum': 2,
                                        'autocalculatable': False,
                                        'type': u'integer'}),
                                      (u'compressor speed at loading index 1',
                                       {'name': u'Compressor Speed at Loading Index 1',
                                        'pyname': u'compressor_speed_at_loading_index_1',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 1 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 1 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 1 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 1 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 2',
                                       {'name': u'Compressor Speed at Loading Index 2',
                                        'pyname': u'compressor_speed_at_loading_index_2',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 2 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 2 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 2 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 2 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 3',
                                       {'name': u'Compressor Speed at Loading Index 3',
                                        'pyname': u'compressor_speed_at_loading_index_3',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 3 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 3 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 3 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 3 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 4',
                                       {'name': u'Compressor Speed at Loading Index 4',
                                        'pyname': u'compressor_speed_at_loading_index_4',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 4 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 4 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 4 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 4 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 5',
                                       {'name': u'Compressor Speed at Loading Index 5',
                                        'pyname': u'compressor_speed_at_loading_index_5',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 5 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 5 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 5 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 5 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 6',
                                       {'name': u'Compressor Speed at Loading Index 6',
                                        'pyname': u'compressor_speed_at_loading_index_6',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 6 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 6 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 6 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 6 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 7',
                                       {'name': u'Compressor Speed at Loading Index 7',
                                        'pyname': u'compressor_speed_at_loading_index_7',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 7 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 7 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 7 list',
                                       {'name': u'Loading Index 7 list',
                                        'pyname': u'loading_index_7_list',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': 'alpha'}),
                                      (u'compressor speed at loading index 8',
                                       {'name': u'Compressor Speed at Loading Index 8',
                                        'pyname': u'compressor_speed_at_loading_index_8',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 8 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 8 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 8 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 8 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'compressor speed at loading index 9',
                                       {'name': u'Compressor Speed at Loading Index 9',
                                        'pyname': u'compressor_speed_at_loading_index_9',
                                        'minimum>': 0.0,
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'real',
                                        'unit': u'rev/min'}),
                                      (u'loading index 9 evaporative capacity multiplier function of temperature curve name',
                                       {'name': u'Loading Index 9 Evaporative Capacity Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'}),
                                      (u'loading index 9 compressor power multiplier function of temperature curve name',
                                       {'name': u'Loading Index 9 Compressor Power Multiplier Function of Temperature Curve Name',
                                        'pyname': u'loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name',
                                        'required-field': False,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'object-list'})]),
               'format': None,
               'group': u'Variable Refrigerant Flow Equipment',
               'min-fields': 9,
               'name': u'AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl',
               'pyname': u'AirConditionerVariableRefrigerantFlowFluidTemperatureControl',
               'required-object': False,
               'unique-object': False}

    @property
    def heat_pump_name(self):
        """field `Heat Pump Name`

        |  Enter a unique name for this variable refrigerant flow heat pump

        Args:
            value (str): value for IDD Field `Heat Pump Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `heat_pump_name` or None if not set

        """
        return self["Heat Pump Name"]

    @heat_pump_name.setter
    def heat_pump_name(self, value=None):
        """Corresponds to IDD field `Heat Pump Name`"""
        self["Heat Pump Name"] = value

    @property
    def availability_schedule_name(self):
        """field `Availability Schedule Name`

        |  Enter the name of a schedule that defines the availability of the unit
        |  Schedule values of 0 denote the unit is off. All other values denote the unit is available
        |  If this field is left blank, the unit is available the entire simulation

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
    def zone_terminal_unit_list_name(self):
        """field `Zone Terminal Unit List Name`

        |  Enter the name of a ZoneTerminalUnitList. This list connects zone terminal units to this
        |  heat pump

        Args:
            value (str): value for IDD Field `Zone Terminal Unit List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_terminal_unit_list_name` or None if not set

        """
        return self["Zone Terminal Unit List Name"]

    @zone_terminal_unit_list_name.setter
    def zone_terminal_unit_list_name(self, value=None):
        """Corresponds to IDD field `Zone Terminal Unit List Name`"""
        self["Zone Terminal Unit List Name"] = value

    @property
    def refrigerant_type(self):
        """field `Refrigerant Type`

        |  Default value: R410A

        Args:
            value (str): value for IDD Field `Refrigerant Type`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigerant_type` or None if not set

        """
        return self["Refrigerant Type"]

    @refrigerant_type.setter
    def refrigerant_type(self, value="R410A"):
        """Corresponds to IDD field `Refrigerant Type`"""
        self["Refrigerant Type"] = value

    @property
    def rated_evaporative_capacity(self):
        """field `Rated Evaporative Capacity`

        |  Enter the total evaporative capacity in watts at rated conditions
        |  This is the capacity corresponding to the max compressor speed at rated conditions
        |  The actual evaporative capacity is obtained by multiplying the
        |  rated capacity with the modification factor calculated by Evaporative
        |  Capacity Multiplier Function of Temperature Curve
        |  Units: W
        |  Default value: 40000.0

        Args:
            value (float): value for IDD Field `Rated Evaporative Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_evaporative_capacity` or None if not set

        """
        return self["Rated Evaporative Capacity"]

    @rated_evaporative_capacity.setter
    def rated_evaporative_capacity(self, value=40000.0):
        """Corresponds to IDD field `Rated Evaporative Capacity`"""
        self["Rated Evaporative Capacity"] = value

    @property
    def rated_compressor_power_per_unit_of_rated_evaporative_capacity(self):
        """field `Rated Compressor Power Per Unit of Rated Evaporative
        Capacity`

        |  Enter the rated compressor power per Watt of rated evaporative capacity [W/W]
        |  Rated compressor power corresponds to the max compressor speed at rated conditions
        |  The actual compressor power is obtained by multiplying the
        |  rated power with the modification factor calculated by Compressor
        |  Power Multiplier Function of Temperature Curve
        |  Units: dimensionless
        |  Default value: 0.35

        Args:
            value (float): value for IDD Field `Rated Compressor Power Per Unit of Rated Evaporative Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `rated_compressor_power_per_unit_of_rated_evaporative_capacity` or None if not set

        """
        return self[
            "Rated Compressor Power Per Unit of Rated Evaporative Capacity"]

    @rated_compressor_power_per_unit_of_rated_evaporative_capacity.setter
    def rated_compressor_power_per_unit_of_rated_evaporative_capacity(
            self,
            value=0.35):
        """Corresponds to IDD field `Rated Compressor Power Per Unit of Rated
        Evaporative Capacity`"""
        self[
            "Rated Compressor Power Per Unit of Rated Evaporative Capacity"] = value

    @property
    def minimum_outdoor_air_temperature_in_cooling_mode(self):
        """field `Minimum Outdoor Air Temperature in Cooling Mode`

        |  Enter the minimum outdoor temperature allowed for cooling operation
        |  Cooling is disabled below this temperature
        |  Units: C
        |  Default value: -6.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Air Temperature in Cooling Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_air_temperature_in_cooling_mode` or None if not set

        """
        return self["Minimum Outdoor Air Temperature in Cooling Mode"]

    @minimum_outdoor_air_temperature_in_cooling_mode.setter
    def minimum_outdoor_air_temperature_in_cooling_mode(self, value=-6.0):
        """Corresponds to IDD field `Minimum Outdoor Air Temperature in Cooling
        Mode`"""
        self["Minimum Outdoor Air Temperature in Cooling Mode"] = value

    @property
    def maximum_outdoor_air_temperature_in_cooling_mode(self):
        """field `Maximum Outdoor Air Temperature in Cooling Mode`

        |  Enter the maximum outdoor temperature allowed for cooling operation
        |  Cooling is disabled above this temperature
        |  Units: C
        |  Default value: 43.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Air Temperature in Cooling Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_air_temperature_in_cooling_mode` or None if not set

        """
        return self["Maximum Outdoor Air Temperature in Cooling Mode"]

    @maximum_outdoor_air_temperature_in_cooling_mode.setter
    def maximum_outdoor_air_temperature_in_cooling_mode(self, value=43.0):
        """Corresponds to IDD field `Maximum Outdoor Air Temperature in Cooling
        Mode`"""
        self["Maximum Outdoor Air Temperature in Cooling Mode"] = value

    @property
    def minimum_outdoor_air_temperature_in_heating_mode(self):
        """field `Minimum Outdoor Air Temperature in Heating Mode`

        |  Enter the minimum outdoor temperature allowed for heating operation
        |  Heating is disabled below this temperature
        |  Units: C
        |  Default value: -20.0

        Args:
            value (float): value for IDD Field `Minimum Outdoor Air Temperature in Heating Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `minimum_outdoor_air_temperature_in_heating_mode` or None if not set

        """
        return self["Minimum Outdoor Air Temperature in Heating Mode"]

    @minimum_outdoor_air_temperature_in_heating_mode.setter
    def minimum_outdoor_air_temperature_in_heating_mode(self, value=-20.0):
        """Corresponds to IDD field `Minimum Outdoor Air Temperature in Heating
        Mode`"""
        self["Minimum Outdoor Air Temperature in Heating Mode"] = value

    @property
    def maximum_outdoor_air_temperature_in_heating_mode(self):
        """field `Maximum Outdoor Air Temperature in Heating Mode`

        |  Enter the maximum outdoor temperature allowed for heating operation
        |  Heating is disabled below this temperature
        |  Units: C
        |  Default value: 16.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Air Temperature in Heating Mode`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_air_temperature_in_heating_mode` or None if not set

        """
        return self["Maximum Outdoor Air Temperature in Heating Mode"]

    @maximum_outdoor_air_temperature_in_heating_mode.setter
    def maximum_outdoor_air_temperature_in_heating_mode(self, value=16.0):
        """Corresponds to IDD field `Maximum Outdoor Air Temperature in Heating
        Mode`"""
        self["Maximum Outdoor Air Temperature in Heating Mode"] = value

    @property
    def reference_outdoor_unit_superheating(self):
        """field `Reference Outdoor Unit Superheating`

        |  Units: deltaC
        |  Default value: 3.0

        Args:
            value (float): value for IDD Field `Reference Outdoor Unit Superheating`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `reference_outdoor_unit_superheating` or None if not set

        """
        return self["Reference Outdoor Unit Superheating"]

    @reference_outdoor_unit_superheating.setter
    def reference_outdoor_unit_superheating(self, value=3.0):
        """Corresponds to IDD field `Reference Outdoor Unit Superheating`"""
        self["Reference Outdoor Unit Superheating"] = value

    @property
    def reference_outdoor_unit_subcooling(self):
        """field `Reference Outdoor Unit Subcooling`

        |  Units: deltaC
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Reference Outdoor Unit Subcooling`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `reference_outdoor_unit_subcooling` or None if not set

        """
        return self["Reference Outdoor Unit Subcooling"]

    @reference_outdoor_unit_subcooling.setter
    def reference_outdoor_unit_subcooling(self, value=5.0):
        """Corresponds to IDD field `Reference Outdoor Unit Subcooling`"""
        self["Reference Outdoor Unit Subcooling"] = value

    @property
    def refrigerant_temperature_control_algorithm_for_indoor_unit(self):
        """field `Refrigerant Temperature Control Algorithm for Indoor Unit`

        |  Default value: VariableTemp

        Args:
            value (str): value for IDD Field `Refrigerant Temperature Control Algorithm for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `refrigerant_temperature_control_algorithm_for_indoor_unit` or None if not set

        """
        return self[
            "Refrigerant Temperature Control Algorithm for Indoor Unit"]

    @refrigerant_temperature_control_algorithm_for_indoor_unit.setter
    def refrigerant_temperature_control_algorithm_for_indoor_unit(
            self,
            value="VariableTemp"):
        """Corresponds to IDD field `Refrigerant Temperature Control Algorithm
        for Indoor Unit`"""
        self[
            "Refrigerant Temperature Control Algorithm for Indoor Unit"] = value

    @property
    def reference_evaporating_temperature_for_indoor_unit(self):
        """field `Reference Evaporating Temperature for Indoor Unit`

        |  This field is used if Refrigerant Temperature Control Algorithm
        |  is ConstantTemp
        |  Evaporating temperature is the refrigerant temperature, not air temperature
        |  Units: C
        |  Default value: 6.0

        Args:
            value (float): value for IDD Field `Reference Evaporating Temperature for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `reference_evaporating_temperature_for_indoor_unit` or None if not set

        """
        return self["Reference Evaporating Temperature for Indoor Unit"]

    @reference_evaporating_temperature_for_indoor_unit.setter
    def reference_evaporating_temperature_for_indoor_unit(self, value=6.0):
        """Corresponds to IDD field `Reference Evaporating Temperature for
        Indoor Unit`"""
        self["Reference Evaporating Temperature for Indoor Unit"] = value

    @property
    def reference_condensing_temperature_for_indoor_unit(self):
        """field `Reference Condensing Temperature for Indoor Unit`

        |  This field is used if Refrigerant Temperature Control Algorithm
        |  is ConstantTemp
        |  Condensing temperature is the refrigerant temperature, not air temperature
        |  Units: C
        |  Default value: 44.0

        Args:
            value (float): value for IDD Field `Reference Condensing Temperature for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `reference_condensing_temperature_for_indoor_unit` or None if not set

        """
        return self["Reference Condensing Temperature for Indoor Unit"]

    @reference_condensing_temperature_for_indoor_unit.setter
    def reference_condensing_temperature_for_indoor_unit(self, value=44.0):
        """Corresponds to IDD field `Reference Condensing Temperature for
        Indoor Unit`"""
        self["Reference Condensing Temperature for Indoor Unit"] = value

    @property
    def variable_evaporating_temperature_minimum_for_indoor_unit(self):
        """field `Variable Evaporating Temperature Minimum for Indoor Unit`

        |  This field is used if Refrigerant Temperature Control Algorithm
        |  is VariableTemp
        |  Evaporating temperature is the refrigerant temperature, not air temperature
        |  Units: C
        |  Default value: 4.0

        Args:
            value (float): value for IDD Field `Variable Evaporating Temperature Minimum for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `variable_evaporating_temperature_minimum_for_indoor_unit` or None if not set

        """
        return self["Variable Evaporating Temperature Minimum for Indoor Unit"]

    @variable_evaporating_temperature_minimum_for_indoor_unit.setter
    def variable_evaporating_temperature_minimum_for_indoor_unit(
            self,
            value=4.0):
        """Corresponds to IDD field `Variable Evaporating Temperature Minimum
        for Indoor Unit`"""
        self[
            "Variable Evaporating Temperature Minimum for Indoor Unit"] = value

    @property
    def variable_evaporating_temperature_maximum_for_indoor_unit(self):
        """field `Variable Evaporating Temperature Maximum for Indoor Unit`

        |  This field is used if Refrigerant Temperature Control Algorithm
        |  is VariableTemp
        |  Evaporating temperature is the refrigerant temperature, not air temperature
        |  Units: C
        |  Default value: 13.0

        Args:
            value (float): value for IDD Field `Variable Evaporating Temperature Maximum for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `variable_evaporating_temperature_maximum_for_indoor_unit` or None if not set

        """
        return self["Variable Evaporating Temperature Maximum for Indoor Unit"]

    @variable_evaporating_temperature_maximum_for_indoor_unit.setter
    def variable_evaporating_temperature_maximum_for_indoor_unit(
            self,
            value=13.0):
        """Corresponds to IDD field `Variable Evaporating Temperature Maximum
        for Indoor Unit`"""
        self[
            "Variable Evaporating Temperature Maximum for Indoor Unit"] = value

    @property
    def variable_condensing_temperature_minimum_for_indoor_unit(self):
        """field `Variable Condensing Temperature Minimum for Indoor Unit`

        |  This field is used if Refrigerant Temperature Control Algorithm
        |  is VariableTemp
        |  Condensing temperature is the refrigerant temperature, not air temperature
        |  Units: C
        |  Default value: 42.0

        Args:
            value (float): value for IDD Field `Variable Condensing Temperature Minimum for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `variable_condensing_temperature_minimum_for_indoor_unit` or None if not set

        """
        return self["Variable Condensing Temperature Minimum for Indoor Unit"]

    @variable_condensing_temperature_minimum_for_indoor_unit.setter
    def variable_condensing_temperature_minimum_for_indoor_unit(
            self,
            value=42.0):
        """Corresponds to IDD field `Variable Condensing Temperature Minimum
        for Indoor Unit`"""
        self["Variable Condensing Temperature Minimum for Indoor Unit"] = value

    @property
    def variable_condensing_temperature_maximum_for_indoor_unit(self):
        """field `Variable Condensing Temperature Maximum for Indoor Unit`

        |  This field is used if Refrigerant Temperature Control Algorithm
        |  is VariableTemp
        |  Condensing temperature is the refrigerant temperature, not air temperature
        |  Units: C
        |  Default value: 46.0

        Args:
            value (float): value for IDD Field `Variable Condensing Temperature Maximum for Indoor Unit`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `variable_condensing_temperature_maximum_for_indoor_unit` or None if not set

        """
        return self["Variable Condensing Temperature Maximum for Indoor Unit"]

    @variable_condensing_temperature_maximum_for_indoor_unit.setter
    def variable_condensing_temperature_maximum_for_indoor_unit(
            self,
            value=46.0):
        """Corresponds to IDD field `Variable Condensing Temperature Maximum
        for Indoor Unit`"""
        self["Variable Condensing Temperature Maximum for Indoor Unit"] = value

    @property
    def outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity(self):
        """field `Outdoor Unit Fan Power Per Unit of Rated Evaporative
        Capacity`

        |  Enter the outdoor unit fan power per Watt of rated evaporative capacity [W/W]
        |  Units: dimensionless
        |  Default value: 0.00425

        Args:
            value (float): value for IDD Field `Outdoor Unit Fan Power Per Unit of Rated Evaporative Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity` or None if not set

        """
        return self[
            "Outdoor Unit Fan Power Per Unit of Rated Evaporative Capacity"]

    @outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity.setter
    def outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity(
            self,
            value=0.00425):
        """Corresponds to IDD field `Outdoor Unit Fan Power Per Unit of Rated
        Evaporative Capacity`"""
        self[
            "Outdoor Unit Fan Power Per Unit of Rated Evaporative Capacity"] = value

    @property
    def outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity(
            self):
        """field `Outdoor Unit Fan Flow Rate Per Unit of Rated Evaporative
        Capacity`

        |  This field is only used if the previous is set to autocalculate and performance input method is NominalCapacity
        |  Units: m3/s-W
        |  Default value: 7.5e-05

        Args:
            value (float): value for IDD Field `Outdoor Unit Fan Flow Rate Per Unit of Rated Evaporative Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity` or None if not set

        """
        return self[
            "Outdoor Unit Fan Flow Rate Per Unit of Rated Evaporative Capacity"]

    @outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity.setter
    def outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity(
            self,
            value=7.5e-05):
        """Corresponds to IDD field `Outdoor Unit Fan Flow Rate Per Unit of
        Rated Evaporative Capacity`"""
        self[
            "Outdoor Unit Fan Flow Rate Per Unit of Rated Evaporative Capacity"] = value

    @property
    def outdoor_unit_evaporating_temperature_function_of_superheating_curve_name(
            self):
        """field `Outdoor Unit Evaporating Temperature Function of Superheating
        Curve Name`

        Args:
            value (str): value for IDD Field `Outdoor Unit Evaporating Temperature Function of Superheating Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_unit_evaporating_temperature_function_of_superheating_curve_name` or None if not set

        """
        return self[
            "Outdoor Unit Evaporating Temperature Function of Superheating Curve Name"]

    @outdoor_unit_evaporating_temperature_function_of_superheating_curve_name.setter
    def outdoor_unit_evaporating_temperature_function_of_superheating_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Outdoor Unit Evaporating Temperature
        Function of Superheating Curve Name`"""
        self[
            "Outdoor Unit Evaporating Temperature Function of Superheating Curve Name"] = value

    @property
    def outdoor_unit_condensing_temperature_function_of_subcooling_curve_name(
            self):
        """field `Outdoor Unit Condensing Temperature Function of Subcooling
        Curve Name`

        Args:
            value (str): value for IDD Field `Outdoor Unit Condensing Temperature Function of Subcooling Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `outdoor_unit_condensing_temperature_function_of_subcooling_curve_name` or None if not set

        """
        return self[
            "Outdoor Unit Condensing Temperature Function of Subcooling Curve Name"]

    @outdoor_unit_condensing_temperature_function_of_subcooling_curve_name.setter
    def outdoor_unit_condensing_temperature_function_of_subcooling_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Outdoor Unit Condensing Temperature
        Function of Subcooling Curve Name`"""
        self[
            "Outdoor Unit Condensing Temperature Function of Subcooling Curve Name"] = value

    @property
    def diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units(self):
        """field `Diameter of Main Pipe Connecting Outdoor Unit to Indoor
        Units`

        |  used to calculate the piping loss
        |  Units: m
        |  Default value: 0.0762

        Args:
            value (float): value for IDD Field `Diameter of Main Pipe Connecting Outdoor Unit to Indoor Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units` or None if not set

        """
        return self[
            "Diameter of Main Pipe Connecting Outdoor Unit to Indoor Units"]

    @diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units.setter
    def diameter_of_main_pipe_connecting_outdoor_unit_to_indoor_units(
            self,
            value=0.0762):
        """Corresponds to IDD field `Diameter of Main Pipe Connecting Outdoor
        Unit to Indoor Units`"""
        self[
            "Diameter of Main Pipe Connecting Outdoor Unit to Indoor Units"] = value

    @property
    def length_of_main_pipe_connecting_outdoor_unit_to_indoor_units(self):
        """field `Length of Main Pipe Connecting Outdoor Unit to Indoor Units`

        |  used to calculate the heat loss of the main pipe
        |  Units: m
        |  Default value: 30.0

        Args:
            value (float): value for IDD Field `Length of Main Pipe Connecting Outdoor Unit to Indoor Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `length_of_main_pipe_connecting_outdoor_unit_to_indoor_units` or None if not set

        """
        return self[
            "Length of Main Pipe Connecting Outdoor Unit to Indoor Units"]

    @length_of_main_pipe_connecting_outdoor_unit_to_indoor_units.setter
    def length_of_main_pipe_connecting_outdoor_unit_to_indoor_units(
            self,
            value=30.0):
        """Corresponds to IDD field `Length of Main Pipe Connecting Outdoor
        Unit to Indoor Units`"""
        self[
            "Length of Main Pipe Connecting Outdoor Unit to Indoor Units"] = value

    @property
    def equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units(
            self):
        """field `Equivalent Length of Main Pipe Connecting Outdoor Unit to
        Indoor Units`

        |  used to calculate the refrigerant pressure drop of the main pipe
        |  Units: m
        |  Default value: 36.0

        Args:
            value (float): value for IDD Field `Equivalent Length of Main Pipe Connecting Outdoor Unit to Indoor Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units` or None if not set

        """
        return self[
            "Equivalent Length of Main Pipe Connecting Outdoor Unit to Indoor Units"]

    @equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units.setter
    def equivalent_length_of_main_pipe_connecting_outdoor_unit_to_indoor_units(
            self,
            value=36.0):
        """Corresponds to IDD field `Equivalent Length of Main Pipe Connecting
        Outdoor Unit to Indoor Units`"""
        self[
            "Equivalent Length of Main Pipe Connecting Outdoor Unit to Indoor Units"] = value

    @property
    def height_difference_between_outdoor_unit_and_indoor_units(self):
        """field `Height Difference Between Outdoor Unit and Indoor Units`

        |  Difference between outdoor unit height and indoor unit height
        |  Positive means outdoor unit is higher than indoor unit
        |  Negative means outdoor unit is lower than indoor unit
        |  Units: m
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Height Difference Between Outdoor Unit and Indoor Units`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `height_difference_between_outdoor_unit_and_indoor_units` or None if not set

        """
        return self["Height Difference Between Outdoor Unit and Indoor Units"]

    @height_difference_between_outdoor_unit_and_indoor_units.setter
    def height_difference_between_outdoor_unit_and_indoor_units(
            self,
            value=5.0):
        """Corresponds to IDD field `Height Difference Between Outdoor Unit and
        Indoor Units`"""
        self["Height Difference Between Outdoor Unit and Indoor Units"] = value

    @property
    def main_pipe_insulation_thickness(self):
        """field `Main Pipe Insulation Thickness`

        |  Units: m
        |  Default value: 0.02

        Args:
            value (float): value for IDD Field `Main Pipe Insulation Thickness`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `main_pipe_insulation_thickness` or None if not set

        """
        return self["Main Pipe Insulation Thickness"]

    @main_pipe_insulation_thickness.setter
    def main_pipe_insulation_thickness(self, value=0.02):
        """Corresponds to IDD field `Main Pipe Insulation Thickness`"""
        self["Main Pipe Insulation Thickness"] = value

    @property
    def main_pipe_insulation_thermal_conductivity(self):
        """field `Main Pipe Insulation Thermal Conductivity`

        |  Units: W/m-K
        |  Default value: 0.032

        Args:
            value (float): value for IDD Field `Main Pipe Insulation Thermal Conductivity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `main_pipe_insulation_thermal_conductivity` or None if not set

        """
        return self["Main Pipe Insulation Thermal Conductivity"]

    @main_pipe_insulation_thermal_conductivity.setter
    def main_pipe_insulation_thermal_conductivity(self, value=0.032):
        """Corresponds to IDD field `Main Pipe Insulation Thermal
        Conductivity`"""
        self["Main Pipe Insulation Thermal Conductivity"] = value

    @property
    def crankcase_heater_power_per_compressor(self):
        """field `Crankcase Heater Power per Compressor`

        |  Enter the value of the resistive heater located in the compressor(s). This heater
        |  is used to warm the refrigerant and oil when the compressor is off
        |  Units: W
        |  Default value: 33.0

        Args:
            value (float): value for IDD Field `Crankcase Heater Power per Compressor`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `crankcase_heater_power_per_compressor` or None if not set

        """
        return self["Crankcase Heater Power per Compressor"]

    @crankcase_heater_power_per_compressor.setter
    def crankcase_heater_power_per_compressor(self, value=33.0):
        """Corresponds to IDD field `Crankcase Heater Power per Compressor`"""
        self["Crankcase Heater Power per Compressor"] = value

    @property
    def number_of_compressors(self):
        """field `Number of Compressors`

        |  Enter the total number of compressor. This input is used only for crankcase
        |  heater calculations.
        |  Units: dimensionless
        |  Default value: 2

        Args:
            value (int): value for IDD Field `Number of Compressors`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_compressors` or None if not set

        """
        return self["Number of Compressors"]

    @number_of_compressors.setter
    def number_of_compressors(self, value=2):
        """Corresponds to IDD field `Number of Compressors`"""
        self["Number of Compressors"] = value

    @property
    def ratio_of_compressor_size_to_total_compressor_capacity(self):
        """field `Ratio of Compressor Size to Total Compressor Capacity`

        |  Enter the ratio of the first stage compressor to total compressor capacity
        |  All other compressors are assumed to be equally sized. This inputs is used
        |  only for crankcase heater calculations
        |  Units: W/W
        |  Default value: 0.5

        Args:
            value (float): value for IDD Field `Ratio of Compressor Size to Total Compressor Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `ratio_of_compressor_size_to_total_compressor_capacity` or None if not set

        """
        return self["Ratio of Compressor Size to Total Compressor Capacity"]

    @ratio_of_compressor_size_to_total_compressor_capacity.setter
    def ratio_of_compressor_size_to_total_compressor_capacity(self, value=0.5):
        """Corresponds to IDD field `Ratio of Compressor Size to Total
        Compressor Capacity`"""
        self["Ratio of Compressor Size to Total Compressor Capacity"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_crankcase_heater(self):
        """field `Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater`

        |  Enter the maximum outdoor temperature above which the crankcase heaters are disabled
        |  Units: C
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_crankcase_heater` or None if not set
        """
        return self[
            "Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"]

    @maximum_outdoor_drybulb_temperature_for_crankcase_heater.setter
    def maximum_outdoor_drybulb_temperature_for_crankcase_heater(
            self,
            value=5.0):
        """  Corresponds to IDD field `Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater`

        """
        self[
            "Maximum Outdoor Dry-Bulb Temperature for Crankcase Heater"] = value

    @property
    def defrost_strategy(self):
        """field `Defrost Strategy`

        |  Select a defrost strategy.
        |  Reverse cycle reverses the operating mode from heating to
        |  cooling to melt frost formation on the condenser coil
        |  The resistive strategy uses a resistive heater
        |  to melt the frost.
        |  Default value: Resistive

        Args:
            value (str): value for IDD Field `Defrost Strategy`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_strategy` or None if not set

        """
        return self["Defrost Strategy"]

    @defrost_strategy.setter
    def defrost_strategy(self, value="Resistive"):
        """Corresponds to IDD field `Defrost Strategy`"""
        self["Defrost Strategy"] = value

    @property
    def defrost_control(self):
        """field `Defrost Control`

        |  Choose a defrost control type
        |  Either use a fixed Timed defrost period or select
        |  OnDemand to defrost only when necessary
        |  Default value: Timed

        Args:
            value (str): value for IDD Field `Defrost Control`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_control` or None if not set

        """
        return self["Defrost Control"]

    @defrost_control.setter
    def defrost_control(self, value="Timed"):
        """Corresponds to IDD field `Defrost Control`"""
        self["Defrost Control"] = value

    @property
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve_name(
            self):
        """field `Defrost Energy Input Ratio Modifier Function of Temperature
        Curve Name`

        |  A valid performance curve must be used if ReverseCycle defrost strategy is selected

        Args:
            value (str): value for IDD Field `Defrost Energy Input Ratio Modifier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `defrost_energy_input_ratio_modifier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"]

    @defrost_energy_input_ratio_modifier_function_of_temperature_curve_name.setter
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Defrost Energy Input Ratio Modifier
        Function of Temperature Curve Name`"""
        self[
            "Defrost Energy Input Ratio Modifier Function of Temperature Curve Name"] = value

    @property
    def defrost_time_period_fraction(self):
        """field `Defrost Time Period Fraction`

        |  Fraction of time in defrost mode
        |  Only applicable if timed defrost control is specified
        |  Default value: 0.058333

        Args:
            value (float): value for IDD Field `Defrost Time Period Fraction`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `defrost_time_period_fraction` or None if not set

        """
        return self["Defrost Time Period Fraction"]

    @defrost_time_period_fraction.setter
    def defrost_time_period_fraction(self, value=0.058333):
        """Corresponds to IDD field `Defrost Time Period Fraction`"""
        self["Defrost Time Period Fraction"] = value

    @property
    def resistive_defrost_heater_capacity(self):
        """field `Resistive Defrost Heater Capacity`

        |  Enter the size of the resistive defrost heating element
        |  Only applicable if resistive defrost strategy is specified
        |  Units: W
        |  IP-Units: W

        Args:
            value (float or "Autosize"): value for IDD Field `Resistive Defrost Heater Capacity`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float or "Autosize": the value of `resistive_defrost_heater_capacity` or None if not set

        """
        return self["Resistive Defrost Heater Capacity"]

    @resistive_defrost_heater_capacity.setter
    def resistive_defrost_heater_capacity(self, value=None):
        """Corresponds to IDD field `Resistive Defrost Heater Capacity`"""
        self["Resistive Defrost Heater Capacity"] = value

    @property
    def maximum_outdoor_drybulb_temperature_for_defrost_operation(self):
        """field `Maximum Outdoor Dry-bulb Temperature for Defrost Operation`

        |  Enter the maximum outdoor temperature above which the defrost operation is disabled
        |  Units: C
        |  Default value: 5.0

        Args:
            value (float): value for IDD Field `Maximum Outdoor Dry-bulb Temperature for Defrost Operation`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `maximum_outdoor_drybulb_temperature_for_defrost_operation` or None if not set
        """
        return self[
            "Maximum Outdoor Dry-bulb Temperature for Defrost Operation"]

    @maximum_outdoor_drybulb_temperature_for_defrost_operation.setter
    def maximum_outdoor_drybulb_temperature_for_defrost_operation(
            self,
            value=5.0):
        """  Corresponds to IDD field `Maximum Outdoor Dry-bulb Temperature for Defrost Operation`

        """
        self[
            "Maximum Outdoor Dry-bulb Temperature for Defrost Operation"] = value

    @property
    def compressor_maximum_delta_pressure(self):
        """field `Compressor maximum delta Pressure`

        |  Units: Pa
        |  Default value: 4500000.0
        |  value <= 50000000.0

        Args:
            value (float): value for IDD Field `Compressor maximum delta Pressure`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_maximum_delta_pressure` or None if not set

        """
        return self["Compressor maximum delta Pressure"]

    @compressor_maximum_delta_pressure.setter
    def compressor_maximum_delta_pressure(self, value=4500000.0):
        """Corresponds to IDD field `Compressor maximum delta Pressure`"""
        self["Compressor maximum delta Pressure"] = value

    @property
    def number_of_compressor_loading_index_entries(self):
        """field `Number of Compressor Loading Index Entries`

        |  First index represents minimal capacity operation
        |  Last index represents full capacity operation
        |  Default value: 2
        |  value >= 2
        |  value <= 9

        Args:
            value (int): value for IDD Field `Number of Compressor Loading Index Entries`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            int: the value of `number_of_compressor_loading_index_entries` or None if not set

        """
        return self["Number of Compressor Loading Index Entries"]

    @number_of_compressor_loading_index_entries.setter
    def number_of_compressor_loading_index_entries(self, value=2):
        """Corresponds to IDD field `Number of Compressor Loading Index
        Entries`"""
        self["Number of Compressor Loading Index Entries"] = value

    @property
    def compressor_speed_at_loading_index_1(self):
        """field `Compressor Speed at Loading Index 1`

        |  Minimum compressor speed
        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 1`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_1` or None if not set

        """
        return self["Compressor Speed at Loading Index 1"]

    @compressor_speed_at_loading_index_1.setter
    def compressor_speed_at_loading_index_1(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 1`"""
        self["Compressor Speed at Loading Index 1"] = value

    @property
    def loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 1 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 1 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 1 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_1_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 1 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 1 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 1 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 1 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 1 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_1_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 1 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 1 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_2(self):
        """field `Compressor Speed at Loading Index 2`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 2`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_2` or None if not set

        """
        return self["Compressor Speed at Loading Index 2"]

    @compressor_speed_at_loading_index_2.setter
    def compressor_speed_at_loading_index_2(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 2`"""
        self["Compressor Speed at Loading Index 2"] = value

    @property
    def loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 2 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 2 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 2 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_2_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 2 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 2 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 2 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 2 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 2 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_2_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 2 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 2 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_3(self):
        """field `Compressor Speed at Loading Index 3`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 3`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_3` or None if not set

        """
        return self["Compressor Speed at Loading Index 3"]

    @compressor_speed_at_loading_index_3.setter
    def compressor_speed_at_loading_index_3(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 3`"""
        self["Compressor Speed at Loading Index 3"] = value

    @property
    def loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 3 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 3 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 3 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_3_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 3 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 3 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 3 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 3 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 3 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_3_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 3 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 3 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_4(self):
        """field `Compressor Speed at Loading Index 4`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 4`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_4` or None if not set

        """
        return self["Compressor Speed at Loading Index 4"]

    @compressor_speed_at_loading_index_4.setter
    def compressor_speed_at_loading_index_4(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 4`"""
        self["Compressor Speed at Loading Index 4"] = value

    @property
    def loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 4 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 4 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 4 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_4_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 4 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 4 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 4 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 4 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 4 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_4_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 4 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 4 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_5(self):
        """field `Compressor Speed at Loading Index 5`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 5`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_5` or None if not set

        """
        return self["Compressor Speed at Loading Index 5"]

    @compressor_speed_at_loading_index_5.setter
    def compressor_speed_at_loading_index_5(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 5`"""
        self["Compressor Speed at Loading Index 5"] = value

    @property
    def loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 5 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 5 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 5 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_5_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 5 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 5 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 5 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 5 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 5 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_5_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 5 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 5 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_6(self):
        """field `Compressor Speed at Loading Index 6`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 6`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_6` or None if not set

        """
        return self["Compressor Speed at Loading Index 6"]

    @compressor_speed_at_loading_index_6.setter
    def compressor_speed_at_loading_index_6(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 6`"""
        self["Compressor Speed at Loading Index 6"] = value

    @property
    def loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 6 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 6 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 6 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_6_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 6 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 6 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 6 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 6 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 6 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_6_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 6 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 6 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_7(self):
        """field `Compressor Speed at Loading Index 7`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 7`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_7` or None if not set

        """
        return self["Compressor Speed at Loading Index 7"]

    @compressor_speed_at_loading_index_7.setter
    def compressor_speed_at_loading_index_7(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 7`"""
        self["Compressor Speed at Loading Index 7"] = value

    @property
    def loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 7 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 7 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 7 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_7_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 7 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 7 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_7_list(self):
        """field `Loading Index 7 list`

        Args:
            value (str): value for IDD Field `Loading Index 7 list`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_7_list` or None if not set

        """
        return self["Loading Index 7 list"]

    @loading_index_7_list.setter
    def loading_index_7_list(self, value=None):
        """Corresponds to IDD field `Loading Index 7 list`"""
        self["Loading Index 7 list"] = value

    @property
    def compressor_speed_at_loading_index_8(self):
        """field `Compressor Speed at Loading Index 8`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 8`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_8` or None if not set

        """
        return self["Compressor Speed at Loading Index 8"]

    @compressor_speed_at_loading_index_8.setter
    def compressor_speed_at_loading_index_8(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 8`"""
        self["Compressor Speed at Loading Index 8"] = value

    @property
    def loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 8 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 8 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 8 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_8_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 8 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 8 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 8 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 8 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 8 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_8_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 8 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 8 Compressor Power Multiplier Function of Temperature Curve Name"] = value

    @property
    def compressor_speed_at_loading_index_9(self):
        """field `Compressor Speed at Loading Index 9`

        |  Units: rev/min

        Args:
            value (float): value for IDD Field `Compressor Speed at Loading Index 9`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            float: the value of `compressor_speed_at_loading_index_9` or None if not set

        """
        return self["Compressor Speed at Loading Index 9"]

    @compressor_speed_at_loading_index_9.setter
    def compressor_speed_at_loading_index_9(self, value=None):
        """Corresponds to IDD field `Compressor Speed at Loading Index 9`"""
        self["Compressor Speed at Loading Index 9"] = value

    @property
    def loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 9 Evaporative Capacity Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 9 Evaporative Capacity Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 9 Evaporative Capacity Multiplier Function of Temperature Curve Name"]

    @loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name.setter
    def loading_index_9_evaporative_capacity_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 9 Evaporative Capacity
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 9 Evaporative Capacity Multiplier Function of Temperature Curve Name"] = value

    @property
    def loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name(
            self):
        """field `Loading Index 9 Compressor Power Multiplier Function of
        Temperature Curve Name`

        Args:
            value (str): value for IDD Field `Loading Index 9 Compressor Power Multiplier Function of Temperature Curve Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name` or None if not set

        """
        return self[
            "Loading Index 9 Compressor Power Multiplier Function of Temperature Curve Name"]

    @loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name.setter
    def loading_index_9_compressor_power_multiplier_function_of_temperature_curve_name(
            self,
            value=None):
        """Corresponds to IDD field `Loading Index 9 Compressor Power
        Multiplier Function of Temperature Curve Name`"""
        self[
            "Loading Index 9 Compressor Power Multiplier Function of Temperature Curve Name"] = value




class ZoneTerminalUnitList(DataObject):

    """Corresponds to IDD object `ZoneTerminalUnitList` List of variable
    refrigerant flow (VRF) terminal units served by a given VRF condensing
    unit.

    See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and
    AirConditioner:VariableRefrigerantFlow.

    """
    _schema = {'extensible-fields': OrderedDict([(u'zone terminal unit name 1',
                                                  {'name': u'Zone Terminal Unit Name 1',
                                                   'pyname': u'zone_terminal_unit_name_1',
                                                   'required-field': True,
                                                   'autosizable': False,
                                                   'autocalculatable': False,
                                                   'type': u'object-list'})]),
               'fields': OrderedDict([(u'zone terminal unit list name',
                                       {'name': u'Zone Terminal Unit List Name',
                                        'pyname': u'zone_terminal_unit_list_name',
                                        'required-field': True,
                                        'autosizable': False,
                                        'autocalculatable': False,
                                        'type': u'alpha'})]),
               'format': None,
               'group': u'Variable Refrigerant Flow Equipment',
               'min-fields': 2,
               'name': u'ZoneTerminalUnitList',
               'pyname': u'ZoneTerminalUnitList',
               'required-object': False,
               'unique-object': False}

    @property
    def zone_terminal_unit_list_name(self):
        """field `Zone Terminal Unit List Name`

        Args:
            value (str): value for IDD Field `Zone Terminal Unit List Name`

        Raises:
            ValueError: if `value` is not a valid value

        Returns:
            str: the value of `zone_terminal_unit_list_name` or None if not set

        """
        return self["Zone Terminal Unit List Name"]

    @zone_terminal_unit_list_name.setter
    def zone_terminal_unit_list_name(self, value=None):
        """Corresponds to IDD field `Zone Terminal Unit List Name`"""
        self["Zone Terminal Unit List Name"] = value

    def add_extensible(self,
                       zone_terminal_unit_name_1=None,
                       ):
        """Add values for extensible fields.

        Args:

            zone_terminal_unit_name_1 (str): value for IDD Field `Zone Terminal Unit Name 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        """
        vals = []
        zone_terminal_unit_name_1 = self.check_value(
            "Zone Terminal Unit Name 1",
            zone_terminal_unit_name_1)
        vals.append(zone_terminal_unit_name_1)
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


