import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxSingleSpeedThermalStorage

log = logging.getLogger(__name__)

class TestCoilCoolingDxSingleSpeedThermalStorage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxsinglespeedthermalstorage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxSingleSpeedThermalStorage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_operating_mode_control_method = "ScheduledModes"
        obj.operating_mode_control_method = var_operating_mode_control_method
        # object-list
        var_operation_mode_control_schedule_name = "object-list|Operation Mode Control Schedule Name"
        obj.operation_mode_control_schedule_name = var_operation_mode_control_schedule_name
        # alpha
        var_storage_type = "Water"
        obj.storage_type = var_storage_type
        # object-list
        var_user_defined_fluid_type = "object-list|User Defined Fluid Type"
        obj.user_defined_fluid_type = var_user_defined_fluid_type
        # real
        var_fluid_storage_volume = 0.0001
        obj.fluid_storage_volume = var_fluid_storage_volume
        # real
        var_ice_storage_capacity = 0.0001
        obj.ice_storage_capacity = var_ice_storage_capacity
        # real
        var_storage_capacity_sizing_factor = 9.9
        obj.storage_capacity_sizing_factor = var_storage_capacity_sizing_factor
        # node
        var_storage_tank_ambient_temperature_node_name = "node|Storage Tank Ambient Temperature Node Name"
        obj.storage_tank_ambient_temperature_node_name = var_storage_tank_ambient_temperature_node_name
        # real
        var_storage_tank_to_ambient_uvalue_times_area_heat_transfer_coefficient = 0.0001
        obj.storage_tank_to_ambient_uvalue_times_area_heat_transfer_coefficient = var_storage_tank_to_ambient_uvalue_times_area_heat_transfer_coefficient
        # real
        var_fluid_storage_tank_rating_temperature = 12.12
        obj.fluid_storage_tank_rating_temperature = var_fluid_storage_tank_rating_temperature
        # real
        var_rated_evaporator_air_flow_rate = 0.0001
        obj.rated_evaporator_air_flow_rate = var_rated_evaporator_air_flow_rate
        # node
        var_evaporator_air_inlet_node_name = "node|Evaporator Air Inlet Node Name"
        obj.evaporator_air_inlet_node_name = var_evaporator_air_inlet_node_name
        # node
        var_evaporator_air_outlet_node_name = "node|Evaporator Air Outlet Node Name"
        obj.evaporator_air_outlet_node_name = var_evaporator_air_outlet_node_name
        # alpha
        var_cooling_only_mode_available = "Yes"
        obj.cooling_only_mode_available = var_cooling_only_mode_available
        # real
        var_cooling_only_mode_rated_total_evaporator_cooling_capacity = 0.0
        obj.cooling_only_mode_rated_total_evaporator_cooling_capacity = var_cooling_only_mode_rated_total_evaporator_cooling_capacity
        # real
        var_cooling_only_mode_rated_sensible_heat_ratio = 0.5
        obj.cooling_only_mode_rated_sensible_heat_ratio = var_cooling_only_mode_rated_sensible_heat_ratio
        # real
        var_cooling_only_mode_rated_cop = 0.0
        obj.cooling_only_mode_rated_cop = var_cooling_only_mode_rated_cop
        # object-list
        var_cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name = "object-list|Cooling Only Mode Total Evaporator Cooling Capacity Function of Temperature Curve Name"
        obj.cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name = var_cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Cooling Only Mode Total Evaporator Cooling Capacity Function of Flow Fraction Curve Name"
        obj.cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name = var_cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name = "object-list|Cooling Only Mode Energy Input Ratio Function of Temperature Curve Name"
        obj.cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name = var_cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling Only Mode Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name = var_cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_only_mode_part_load_fraction_correlation_curve_name = "object-list|Cooling Only Mode Part Load Fraction Correlation Curve Name"
        obj.cooling_only_mode_part_load_fraction_correlation_curve_name = var_cooling_only_mode_part_load_fraction_correlation_curve_name
        # object-list
        var_cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Cooling Only Mode Sensible Heat Ratio Function of Temperature Curve Name"
        obj.cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name = var_cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling Only Mode Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = var_cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        # alpha
        var_cooling_and_charge_mode_available = "Yes"
        obj.cooling_and_charge_mode_available = var_cooling_and_charge_mode_available
        # real
        var_cooling_and_charge_mode_rated_total_evaporator_cooling_capacity = 0.0
        obj.cooling_and_charge_mode_rated_total_evaporator_cooling_capacity = var_cooling_and_charge_mode_rated_total_evaporator_cooling_capacity
        # real
        var_cooling_and_charge_mode_capacity_sizing_factor = 29.29
        obj.cooling_and_charge_mode_capacity_sizing_factor = var_cooling_and_charge_mode_capacity_sizing_factor
        # real
        var_cooling_and_charge_mode_rated_storage_charging_capacity = 0.0
        obj.cooling_and_charge_mode_rated_storage_charging_capacity = var_cooling_and_charge_mode_rated_storage_charging_capacity
        # real
        var_cooling_and_charge_mode_storage_capacity_sizing_factor = 31.31
        obj.cooling_and_charge_mode_storage_capacity_sizing_factor = var_cooling_and_charge_mode_storage_capacity_sizing_factor
        # real
        var_cooling_and_charge_mode_rated_sensible_heat_ratio = 0.5
        obj.cooling_and_charge_mode_rated_sensible_heat_ratio = var_cooling_and_charge_mode_rated_sensible_heat_ratio
        # real
        var_cooling_and_charge_mode_cooling_rated_cop = 0.0
        obj.cooling_and_charge_mode_cooling_rated_cop = var_cooling_and_charge_mode_cooling_rated_cop
        # real
        var_cooling_and_charge_mode_charging_rated_cop = 0.0
        obj.cooling_and_charge_mode_charging_rated_cop = var_cooling_and_charge_mode_charging_rated_cop
        # object-list
        var_cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name = "object-list|Cooling And Charge Mode Total Evaporator Cooling Capacity Function of Temperature Curve Name"
        obj.cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name = var_cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Cooling And Charge Mode Total Evaporator Cooling Capacity Function of Flow Fraction Curve Name"
        obj.cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name = var_cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name = "object-list|Cooling And Charge Mode Evaporator Energy Input Ratio Function of Temperature Curve Name"
        obj.cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name = var_cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling And Charge Mode Evaporator Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name = var_cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name = "object-list|Cooling And Charge Mode Evaporator Part Load Fraction Correlation Curve Name"
        obj.cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name = var_cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name
        # object-list
        var_cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name = "object-list|Cooling And Charge Mode Storage Charge Capacity Function of Temperature Curve Name"
        obj.cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name = var_cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name
        # object-list
        var_cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name = "object-list|Cooling And Charge Mode Storage Charge Capacity Function of Total Evaporator PLR Curve Name"
        obj.cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name = var_cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name
        # object-list
        var_cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name = "object-list|Cooling And Charge Mode Storage Energy Input Ratio Function of Temperature Curve Name"
        obj.cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name = var_cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling And Charge Mode Storage Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name = var_cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name = "object-list|Cooling And Charge Mode Storage Energy Part Load Fraction Correlation Curve Name"
        obj.cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name = var_cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name
        # object-list
        var_cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Cooling And Charge Mode Sensible Heat Ratio Function of Temperature Curve Name"
        obj.cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name = var_cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling And Charge Mode Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = var_cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        # alpha
        var_cooling_and_discharge_mode_available = "Yes"
        obj.cooling_and_discharge_mode_available = var_cooling_and_discharge_mode_available
        # real
        var_cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity = 0.0
        obj.cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity = var_cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity
        # real
        var_cooling_and_discharge_mode_evaporator_capacity_sizing_factor = 49.49
        obj.cooling_and_discharge_mode_evaporator_capacity_sizing_factor = var_cooling_and_discharge_mode_evaporator_capacity_sizing_factor
        # real
        var_cooling_and_discharge_mode_rated_storage_discharging_capacity = 0.0
        obj.cooling_and_discharge_mode_rated_storage_discharging_capacity = var_cooling_and_discharge_mode_rated_storage_discharging_capacity
        # real
        var_cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor = 51.51
        obj.cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor = var_cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor
        # real
        var_cooling_and_discharge_mode_rated_sensible_heat_ratio = 0.5
        obj.cooling_and_discharge_mode_rated_sensible_heat_ratio = var_cooling_and_discharge_mode_rated_sensible_heat_ratio
        # real
        var_cooling_and_discharge_mode_cooling_rated_cop = 0.0
        obj.cooling_and_discharge_mode_cooling_rated_cop = var_cooling_and_discharge_mode_cooling_rated_cop
        # real
        var_cooling_and_discharge_mode_discharging_rated_cop = 0.0
        obj.cooling_and_discharge_mode_discharging_rated_cop = var_cooling_and_discharge_mode_discharging_rated_cop
        # object-list
        var_cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name = "object-list|Cooling And Discharge Mode Total Evaporator Cooling Capacity Function of Temperature Curve Name"
        obj.cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name = var_cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name
        # object-list
        var_cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name = "object-list|Cooling And Discharge Mode Total Evaporator Cooling Capacity Function of Flow Fraction Curve Name"
        obj.cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name = var_cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name = "object-list|Cooling And Discharge Mode Evaporator Energy Input Ratio Function of Temperature Curve Name"
        obj.cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name = var_cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling And Discharge Mode Evaporator Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name = var_cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name = "object-list|Cooling And Discharge Mode Evaporator Part Load Fraction Correlation Curve Name"
        obj.cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name = var_cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name
        # object-list
        var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name = "object-list|Cooling And Discharge Mode Storage Discharge Capacity Function of Temperature Curve Name"
        obj.cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name = var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name
        # object-list
        var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name = "object-list|Cooling And Discharge Mode Storage Discharge Capacity Function of Flow Fraction Curve Name"
        obj.cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name = var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name = "object-list|Cooling And Discharge Mode Storage Discharge Capacity Function of Total Evaporator PLR Curve Name"
        obj.cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name = var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name
        # object-list
        var_cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name = "object-list|Cooling And Discharge Mode Storage Energy Input Ratio Function of Temperature Curve Name"
        obj.cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name = var_cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling And Discharge Mode Storage Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name = var_cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name = "object-list|Cooling And Discharge Mode Storage Energy Part Load Fraction Correlation Curve Name"
        obj.cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name = var_cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name
        # object-list
        var_cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Cooling And Discharge Mode Sensible Heat Ratio Function of Temperature Curve Name"
        obj.cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name = var_cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Cooling And Discharge Mode Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = var_cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        # alpha
        var_charge_only_mode_available = "Yes"
        obj.charge_only_mode_available = var_charge_only_mode_available
        # real
        var_charge_only_mode_rated_storage_charging_capacity = 0.0
        obj.charge_only_mode_rated_storage_charging_capacity = var_charge_only_mode_rated_storage_charging_capacity
        # real
        var_charge_only_mode_capacity_sizing_factor = 70.7
        obj.charge_only_mode_capacity_sizing_factor = var_charge_only_mode_capacity_sizing_factor
        # real
        var_charge_only_mode_charging_rated_cop = 0.0
        obj.charge_only_mode_charging_rated_cop = var_charge_only_mode_charging_rated_cop
        # object-list
        var_charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name = "object-list|Charge Only Mode Storage Charge Capacity Function of Temperature Curve Name"
        obj.charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name = var_charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name
        # object-list
        var_charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name = "object-list|Charge Only Mode Storage Energy Input Ratio Function of Temperature Curve Name"
        obj.charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name = var_charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name
        # alpha
        var_discharge_only_mode_available = "Yes"
        obj.discharge_only_mode_available = var_discharge_only_mode_available
        # real
        var_discharge_only_mode_rated_storage_discharging_capacity = 0.0
        obj.discharge_only_mode_rated_storage_discharging_capacity = var_discharge_only_mode_rated_storage_discharging_capacity
        # real
        var_discharge_only_mode_capacity_sizing_factor = 76.76
        obj.discharge_only_mode_capacity_sizing_factor = var_discharge_only_mode_capacity_sizing_factor
        # real
        var_discharge_only_mode_rated_sensible_heat_ratio = 0.5
        obj.discharge_only_mode_rated_sensible_heat_ratio = var_discharge_only_mode_rated_sensible_heat_ratio
        # real
        var_discharge_only_mode_rated_cop = 0.0
        obj.discharge_only_mode_rated_cop = var_discharge_only_mode_rated_cop
        # object-list
        var_discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name = "object-list|Discharge Only Mode Storage Discharge Capacity Function of Temperature Curve Name"
        obj.discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name = var_discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name
        # object-list
        var_discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name = "object-list|Discharge Only Mode Storage Discharge Capacity Function of Flow Fraction Curve Name"
        obj.discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name = var_discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name
        # object-list
        var_discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name = "object-list|Discharge Only Mode Energy Input Ratio Function of Temperature Curve Name"
        obj.discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name = var_discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name
        # object-list
        var_discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name = "object-list|Discharge Only Mode Energy Input Ratio Function of Flow Fraction Curve Name"
        obj.discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name = var_discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name
        # object-list
        var_discharge_only_mode_part_load_fraction_correlation_curve_name = "object-list|Discharge Only Mode Part Load Fraction Correlation Curve Name"
        obj.discharge_only_mode_part_load_fraction_correlation_curve_name = var_discharge_only_mode_part_load_fraction_correlation_curve_name
        # object-list
        var_discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name = "object-list|Discharge Only Mode Sensible Heat Ratio Function of Temperature Curve Name"
        obj.discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name = var_discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name
        # object-list
        var_discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = "object-list|Discharge Only Mode Sensible Heat Ratio Function of Flow Fraction Curve Name"
        obj.discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name = var_discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        # real
        var_ancillary_electric_power = 0.0
        obj.ancillary_electric_power = var_ancillary_electric_power
        # real
        var_cold_weather_operation_minimum_outdoor_air_temperature = 87.87
        obj.cold_weather_operation_minimum_outdoor_air_temperature = var_cold_weather_operation_minimum_outdoor_air_temperature
        # real
        var_cold_weather_operation_ancillary_power = 0.0
        obj.cold_weather_operation_ancillary_power = var_cold_weather_operation_ancillary_power
        # node
        var_condenser_air_inlet_node_name = "node|Condenser Air Inlet Node Name"
        obj.condenser_air_inlet_node_name = var_condenser_air_inlet_node_name
        # node
        var_condenser_air_outlet_node_name = "node|Condenser Air Outlet Node Name"
        obj.condenser_air_outlet_node_name = var_condenser_air_outlet_node_name
        # real
        var_condenser_design_air_flow_rate = 0.0001
        obj.condenser_design_air_flow_rate = var_condenser_design_air_flow_rate
        # real
        var_condenser_air_flow_sizing_factor = 92.92
        obj.condenser_air_flow_sizing_factor = var_condenser_air_flow_sizing_factor
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_evaporative_condenser_effectiveness = 0.50005
        obj.evaporative_condenser_effectiveness = var_evaporative_condenser_effectiveness
        # real
        var_evaporative_condenser_pump_rated_power_consumption = 0.0
        obj.evaporative_condenser_pump_rated_power_consumption = var_evaporative_condenser_pump_rated_power_consumption
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # object-list
        var_basin_heater_availability_schedule_name = "object-list|Basin Heater Availability Schedule Name"
        obj.basin_heater_availability_schedule_name = var_basin_heater_availability_schedule_name
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name
        # node
        var_storage_tank_plant_connection_inlet_node_name = "node|Storage Tank Plant Connection Inlet Node Name"
        obj.storage_tank_plant_connection_inlet_node_name = var_storage_tank_plant_connection_inlet_node_name
        # node
        var_storage_tank_plant_connection_outlet_node_name = "node|Storage Tank Plant Connection Outlet Node Name"
        obj.storage_tank_plant_connection_outlet_node_name = var_storage_tank_plant_connection_outlet_node_name
        # real
        var_storage_tank_plant_connection_design_flow_rate = 0.0
        obj.storage_tank_plant_connection_design_flow_rate = var_storage_tank_plant_connection_design_flow_rate
        # real
        var_storage_tank_plant_connection_heat_transfer_effectiveness = 0.5
        obj.storage_tank_plant_connection_heat_transfer_effectiveness = var_storage_tank_plant_connection_heat_transfer_effectiveness
        # real
        var_storage_tank_minimum_operating_limit_fluid_temperature = 105.105
        obj.storage_tank_minimum_operating_limit_fluid_temperature = var_storage_tank_minimum_operating_limit_fluid_temperature
        # real
        var_storage_tank_maximum_operating_limit_fluid_temperature = 106.106
        obj.storage_tank_maximum_operating_limit_fluid_temperature = var_storage_tank_maximum_operating_limit_fluid_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].operating_mode_control_method, var_operating_mode_control_method)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].operation_mode_control_schedule_name, var_operation_mode_control_schedule_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_type, var_storage_type)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].user_defined_fluid_type, var_user_defined_fluid_type)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].fluid_storage_volume, var_fluid_storage_volume)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].ice_storage_capacity, var_ice_storage_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_capacity_sizing_factor, var_storage_capacity_sizing_factor)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_ambient_temperature_node_name, var_storage_tank_ambient_temperature_node_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_to_ambient_uvalue_times_area_heat_transfer_coefficient, var_storage_tank_to_ambient_uvalue_times_area_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].fluid_storage_tank_rating_temperature, var_fluid_storage_tank_rating_temperature)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].rated_evaporator_air_flow_rate, var_rated_evaporator_air_flow_rate)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].evaporator_air_inlet_node_name, var_evaporator_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].evaporator_air_outlet_node_name, var_evaporator_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_available, var_cooling_only_mode_available)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_rated_total_evaporator_cooling_capacity, var_cooling_only_mode_rated_total_evaporator_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_rated_sensible_heat_ratio, var_cooling_only_mode_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_rated_cop, var_cooling_only_mode_rated_cop)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name, var_cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name, var_cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name, var_cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name, var_cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_part_load_fraction_correlation_curve_name, var_cooling_only_mode_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name, var_cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name, var_cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_available, var_cooling_and_charge_mode_available)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_rated_total_evaporator_cooling_capacity, var_cooling_and_charge_mode_rated_total_evaporator_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_capacity_sizing_factor, var_cooling_and_charge_mode_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_rated_storage_charging_capacity, var_cooling_and_charge_mode_rated_storage_charging_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_storage_capacity_sizing_factor, var_cooling_and_charge_mode_storage_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_rated_sensible_heat_ratio, var_cooling_and_charge_mode_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_cooling_rated_cop, var_cooling_and_charge_mode_cooling_rated_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_charging_rated_cop, var_cooling_and_charge_mode_charging_rated_cop)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name, var_cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name, var_cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name, var_cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name, var_cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name, var_cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name, var_cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name, var_cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name, var_cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name, var_cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name, var_cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name, var_cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name, var_cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_available, var_cooling_and_discharge_mode_available)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity, var_cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_evaporator_capacity_sizing_factor, var_cooling_and_discharge_mode_evaporator_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_rated_storage_discharging_capacity, var_cooling_and_discharge_mode_rated_storage_discharging_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor, var_cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_rated_sensible_heat_ratio, var_cooling_and_discharge_mode_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_cooling_rated_cop, var_cooling_and_discharge_mode_cooling_rated_cop)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_discharging_rated_cop, var_cooling_and_discharge_mode_discharging_rated_cop)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name, var_cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name, var_cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name, var_cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name, var_cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name, var_cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name, var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name, var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name, var_cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name, var_cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name, var_cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name, var_cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name, var_cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name, var_cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].charge_only_mode_available, var_charge_only_mode_available)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].charge_only_mode_rated_storage_charging_capacity, var_charge_only_mode_rated_storage_charging_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].charge_only_mode_capacity_sizing_factor, var_charge_only_mode_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].charge_only_mode_charging_rated_cop, var_charge_only_mode_charging_rated_cop)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name, var_charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name, var_charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_available, var_discharge_only_mode_available)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_rated_storage_discharging_capacity, var_discharge_only_mode_rated_storage_discharging_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_capacity_sizing_factor, var_discharge_only_mode_capacity_sizing_factor)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_rated_sensible_heat_ratio, var_discharge_only_mode_rated_sensible_heat_ratio)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_rated_cop, var_discharge_only_mode_rated_cop)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name, var_discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name, var_discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name, var_discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name, var_discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_part_load_fraction_correlation_curve_name, var_discharge_only_mode_part_load_fraction_correlation_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name, var_discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name, var_discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].ancillary_electric_power, var_ancillary_electric_power)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cold_weather_operation_minimum_outdoor_air_temperature, var_cold_weather_operation_minimum_outdoor_air_temperature)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].cold_weather_operation_ancillary_power, var_cold_weather_operation_ancillary_power)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].condenser_air_inlet_node_name, var_condenser_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].condenser_air_outlet_node_name, var_condenser_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].condenser_design_air_flow_rate, var_condenser_design_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].condenser_air_flow_sizing_factor, var_condenser_air_flow_sizing_factor)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].evaporative_condenser_effectiveness, var_evaporative_condenser_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].evaporative_condenser_pump_rated_power_consumption, var_evaporative_condenser_pump_rated_power_consumption)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].basin_heater_availability_schedule_name, var_basin_heater_availability_schedule_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_plant_connection_inlet_node_name, var_storage_tank_plant_connection_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_plant_connection_outlet_node_name, var_storage_tank_plant_connection_outlet_node_name)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_plant_connection_design_flow_rate, var_storage_tank_plant_connection_design_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_plant_connection_heat_transfer_effectiveness, var_storage_tank_plant_connection_heat_transfer_effectiveness)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_minimum_operating_limit_fluid_temperature, var_storage_tank_minimum_operating_limit_fluid_temperature)
        self.assertAlmostEqual(idf2.coilcoolingdxsinglespeedthermalstorages[0].storage_tank_maximum_operating_limit_fluid_temperature, var_storage_tank_maximum_operating_limit_fluid_temperature)