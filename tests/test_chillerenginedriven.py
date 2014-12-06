import os
import tempfile
import unittest
import pyidf
from pyidf.plant_heating_and_cooling_equipment import ChillerEngineDriven
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestChillerEngineDriven(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerenginedriven(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerEngineDriven()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # real
        var_nominal_capacity = 0.0
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_nominal_cop = 0.0001
        obj.nominal_cop = var_nominal_cop
        # node
        var_chilled_water_inlet_node_name = "node|Chilled Water Inlet Node Name"
        obj.chilled_water_inlet_node_name = var_chilled_water_inlet_node_name
        # node
        var_chilled_water_outlet_node_name = "node|Chilled Water Outlet Node Name"
        obj.chilled_water_outlet_node_name = var_chilled_water_outlet_node_name
        # node
        var_condenser_inlet_node_name = "node|Condenser Inlet Node Name"
        obj.condenser_inlet_node_name = var_condenser_inlet_node_name
        # node
        var_condenser_outlet_node_name = "node|Condenser Outlet Node Name"
        obj.condenser_outlet_node_name = var_condenser_outlet_node_name
        # real
        var_minimum_part_load_ratio = 0.0
        obj.minimum_part_load_ratio = var_minimum_part_load_ratio
        # real
        var_maximum_part_load_ratio = 0.0
        obj.maximum_part_load_ratio = var_maximum_part_load_ratio
        # real
        var_optimum_part_load_ratio = 0.0
        obj.optimum_part_load_ratio = var_optimum_part_load_ratio
        # real
        var_design_condenser_inlet_temperature = 12.12
        obj.design_condenser_inlet_temperature = var_design_condenser_inlet_temperature
        # real
        var_temperature_rise_coefficient = 0.0001
        obj.temperature_rise_coefficient = var_temperature_rise_coefficient
        # real
        var_design_chilled_water_outlet_temperature = 14.14
        obj.design_chilled_water_outlet_temperature = var_design_chilled_water_outlet_temperature
        # real
        var_design_chilled_water_flow_rate = 0.0
        obj.design_chilled_water_flow_rate = var_design_chilled_water_flow_rate
        # real
        var_design_condenser_water_flow_rate = 0.0
        obj.design_condenser_water_flow_rate = var_design_condenser_water_flow_rate
        # real
        var_coefficient_1_of_capacity_ratio_curve = 17.17
        obj.coefficient_1_of_capacity_ratio_curve = var_coefficient_1_of_capacity_ratio_curve
        # real
        var_coefficient_2_of_capacity_ratio_curve = 18.18
        obj.coefficient_2_of_capacity_ratio_curve = var_coefficient_2_of_capacity_ratio_curve
        # real
        var_coefficient_3_of_capacity_ratio_curve = 19.19
        obj.coefficient_3_of_capacity_ratio_curve = var_coefficient_3_of_capacity_ratio_curve
        # real
        var_coefficient_1_of_power_ratio_curve = 20.2
        obj.coefficient_1_of_power_ratio_curve = var_coefficient_1_of_power_ratio_curve
        # real
        var_coefficient_2_of_power_ratio_curve = 21.21
        obj.coefficient_2_of_power_ratio_curve = var_coefficient_2_of_power_ratio_curve
        # real
        var_coefficient_3_of_power_ratio_curve = 22.22
        obj.coefficient_3_of_power_ratio_curve = var_coefficient_3_of_power_ratio_curve
        # real
        var_coefficient_1_of_full_load_ratio_curve = 23.23
        obj.coefficient_1_of_full_load_ratio_curve = var_coefficient_1_of_full_load_ratio_curve
        # real
        var_coefficient_2_of_full_load_ratio_curve = 24.24
        obj.coefficient_2_of_full_load_ratio_curve = var_coefficient_2_of_full_load_ratio_curve
        # real
        var_coefficient_3_of_full_load_ratio_curve = 25.25
        obj.coefficient_3_of_full_load_ratio_curve = var_coefficient_3_of_full_load_ratio_curve
        # real
        var_chilled_water_outlet_temperature_lower_limit = 26.26
        obj.chilled_water_outlet_temperature_lower_limit = var_chilled_water_outlet_temperature_lower_limit
        # object-list
        var_fuel_use_curve_name = "object-list|Fuel Use Curve Name"
        obj.fuel_use_curve_name = var_fuel_use_curve_name
        # object-list
        var_jacket_heat_recovery_curve_name = "object-list|Jacket Heat Recovery Curve Name"
        obj.jacket_heat_recovery_curve_name = var_jacket_heat_recovery_curve_name
        # object-list
        var_lube_heat_recovery_curve_name = "object-list|Lube Heat Recovery Curve Name"
        obj.lube_heat_recovery_curve_name = var_lube_heat_recovery_curve_name
        # object-list
        var_total_exhaust_energy_curve_name = "object-list|Total Exhaust Energy Curve Name"
        obj.total_exhaust_energy_curve_name = var_total_exhaust_energy_curve_name
        # object-list
        var_exhaust_temperature_curve_name = "object-list|Exhaust Temperature Curve Name"
        obj.exhaust_temperature_curve_name = var_exhaust_temperature_curve_name
        # real
        var_coefficient_1_of_ufactor_times_area_curve = 32.32
        obj.coefficient_1_of_ufactor_times_area_curve = var_coefficient_1_of_ufactor_times_area_curve
        # real
        var_coefficient_2_of_ufactor_times_area_curve = 2.0
        obj.coefficient_2_of_ufactor_times_area_curve = var_coefficient_2_of_ufactor_times_area_curve
        # real
        var_maximum_exhaust_flow_per_unit_of_power_output = 0.0
        obj.maximum_exhaust_flow_per_unit_of_power_output = var_maximum_exhaust_flow_per_unit_of_power_output
        # real
        var_design_minimum_exhaust_temperature = 35.35
        obj.design_minimum_exhaust_temperature = var_design_minimum_exhaust_temperature
        # alpha
        var_fuel_type = "NaturalGas"
        obj.fuel_type = var_fuel_type
        # real
        var_fuel_higher_heating_value = 37.37
        obj.fuel_higher_heating_value = var_fuel_higher_heating_value
        # real
        var_design_heat_recovery_water_flow_rate = 0.0
        obj.design_heat_recovery_water_flow_rate = var_design_heat_recovery_water_flow_rate
        # node
        var_heat_recovery_inlet_node_name = "node|Heat Recovery Inlet Node Name"
        obj.heat_recovery_inlet_node_name = var_heat_recovery_inlet_node_name
        # node
        var_heat_recovery_outlet_node_name = "node|Heat Recovery Outlet Node Name"
        obj.heat_recovery_outlet_node_name = var_heat_recovery_outlet_node_name
        # alpha
        var_chiller_flow_mode = "ConstantFlow"
        obj.chiller_flow_mode = var_chiller_flow_mode
        # real
        var_maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node = 50.0
        obj.maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node = var_maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor
        # real
        var_basin_heater_capacity = 0.0
        obj.basin_heater_capacity = var_basin_heater_capacity
        # real
        var_basin_heater_setpoint_temperature = 2.0
        obj.basin_heater_setpoint_temperature = var_basin_heater_setpoint_temperature
        # object-list
        var_basin_heater_operating_schedule_name = "object-list|Basin Heater Operating Schedule Name"
        obj.basin_heater_operating_schedule_name = var_basin_heater_operating_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.chillerenginedrivens[0].name, var_name)
        self.assertEqual(idf2.chillerenginedrivens[0].condenser_type, var_condenser_type)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].nominal_cop, var_nominal_cop)
        self.assertEqual(idf2.chillerenginedrivens[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.chillerenginedrivens[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.chillerenginedrivens[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.chillerenginedrivens[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].design_condenser_inlet_temperature, var_design_condenser_inlet_temperature)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].temperature_rise_coefficient, var_temperature_rise_coefficient)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].design_chilled_water_outlet_temperature, var_design_chilled_water_outlet_temperature)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].design_chilled_water_flow_rate, var_design_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].design_condenser_water_flow_rate, var_design_condenser_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_1_of_capacity_ratio_curve, var_coefficient_1_of_capacity_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_2_of_capacity_ratio_curve, var_coefficient_2_of_capacity_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_3_of_capacity_ratio_curve, var_coefficient_3_of_capacity_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_1_of_power_ratio_curve, var_coefficient_1_of_power_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_2_of_power_ratio_curve, var_coefficient_2_of_power_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_3_of_power_ratio_curve, var_coefficient_3_of_power_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_1_of_full_load_ratio_curve, var_coefficient_1_of_full_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_2_of_full_load_ratio_curve, var_coefficient_2_of_full_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_3_of_full_load_ratio_curve, var_coefficient_3_of_full_load_ratio_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].chilled_water_outlet_temperature_lower_limit, var_chilled_water_outlet_temperature_lower_limit)
        self.assertEqual(idf2.chillerenginedrivens[0].fuel_use_curve_name, var_fuel_use_curve_name)
        self.assertEqual(idf2.chillerenginedrivens[0].jacket_heat_recovery_curve_name, var_jacket_heat_recovery_curve_name)
        self.assertEqual(idf2.chillerenginedrivens[0].lube_heat_recovery_curve_name, var_lube_heat_recovery_curve_name)
        self.assertEqual(idf2.chillerenginedrivens[0].total_exhaust_energy_curve_name, var_total_exhaust_energy_curve_name)
        self.assertEqual(idf2.chillerenginedrivens[0].exhaust_temperature_curve_name, var_exhaust_temperature_curve_name)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_1_of_ufactor_times_area_curve, var_coefficient_1_of_ufactor_times_area_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].coefficient_2_of_ufactor_times_area_curve, var_coefficient_2_of_ufactor_times_area_curve)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].maximum_exhaust_flow_per_unit_of_power_output, var_maximum_exhaust_flow_per_unit_of_power_output)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].design_minimum_exhaust_temperature, var_design_minimum_exhaust_temperature)
        self.assertEqual(idf2.chillerenginedrivens[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].fuel_higher_heating_value, var_fuel_higher_heating_value)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].design_heat_recovery_water_flow_rate, var_design_heat_recovery_water_flow_rate)
        self.assertEqual(idf2.chillerenginedrivens[0].heat_recovery_inlet_node_name, var_heat_recovery_inlet_node_name)
        self.assertEqual(idf2.chillerenginedrivens[0].heat_recovery_outlet_node_name, var_heat_recovery_outlet_node_name)
        self.assertEqual(idf2.chillerenginedrivens[0].chiller_flow_mode, var_chiller_flow_mode)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node, var_maximum_temperature_for_heat_recovery_at_heat_recovery_outlet_node)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.chillerenginedrivens[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.chillerenginedrivens[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)