import os
import tempfile
import unittest
import pyidf
from pyidf.fans import FanComponentModel
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFanComponentModel(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fancomponentmodel(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FanComponentModel()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_flow_rate = 0.0
        obj.maximum_flow_rate = var_maximum_flow_rate
        # real
        var_minimum_flow_rate = 0.0
        obj.minimum_flow_rate = var_minimum_flow_rate
        # real
        var_fan_sizing_factor = 1.0
        obj.fan_sizing_factor = var_fan_sizing_factor
        # real
        var_fan_wheel_diameter = 0.0001
        obj.fan_wheel_diameter = var_fan_wheel_diameter
        # real
        var_fan_outlet_area = 0.0001
        obj.fan_outlet_area = var_fan_outlet_area
        # real
        var_maximum_fan_static_efficiency = 0.50005
        obj.maximum_fan_static_efficiency = var_maximum_fan_static_efficiency
        # real
        var_euler_number_at_maximum_fan_static_efficiency = 0.0001
        obj.euler_number_at_maximum_fan_static_efficiency = var_euler_number_at_maximum_fan_static_efficiency
        # real
        var_maximum_dimensionless_fan_airflow = 0.0001
        obj.maximum_dimensionless_fan_airflow = var_maximum_dimensionless_fan_airflow
        # real
        var_motor_fan_pulley_ratio = 0.0001
        obj.motor_fan_pulley_ratio = var_motor_fan_pulley_ratio
        # real
        var_belt_maximum_torque = 0.0001
        obj.belt_maximum_torque = var_belt_maximum_torque
        # real
        var_belt_sizing_factor = 1.0
        obj.belt_sizing_factor = var_belt_sizing_factor
        # real
        var_belt_fractional_torque_transition = 0.5
        obj.belt_fractional_torque_transition = var_belt_fractional_torque_transition
        # real
        var_motor_maximum_speed = 0.0001
        obj.motor_maximum_speed = var_motor_maximum_speed
        # real
        var_maximum_motor_output_power = 0.0001
        obj.maximum_motor_output_power = var_maximum_motor_output_power
        # real
        var_motor_sizing_factor = 1.0
        obj.motor_sizing_factor = var_motor_sizing_factor
        # real
        var_motor_in_airstream_fraction = 0.5
        obj.motor_in_airstream_fraction = var_motor_in_airstream_fraction
        # alpha
        var_vfd_efficiency_type = "Speed"
        obj.vfd_efficiency_type = var_vfd_efficiency_type
        # real
        var_maximum_vfd_output_power = 0.0001
        obj.maximum_vfd_output_power = var_maximum_vfd_output_power
        # real
        var_vfd_sizing_factor = 1.0
        obj.vfd_sizing_factor = var_vfd_sizing_factor
        # object-list
        var_fan_pressure_rise_curve_name = "object-list|Fan Pressure Rise Curve Name"
        obj.fan_pressure_rise_curve_name = var_fan_pressure_rise_curve_name
        # object-list
        var_duct_static_pressure_reset_curve_name = "object-list|Duct Static Pressure Reset Curve Name"
        obj.duct_static_pressure_reset_curve_name = var_duct_static_pressure_reset_curve_name
        # object-list
        var_normalized_fan_static_efficiency_curve_namenonstall_region = "object-list|Normalized Fan Static Efficiency Curve Name-Non-Stall Region"
        obj.normalized_fan_static_efficiency_curve_namenonstall_region = var_normalized_fan_static_efficiency_curve_namenonstall_region
        # object-list
        var_normalized_fan_static_efficiency_curve_namestall_region = "object-list|Normalized Fan Static Efficiency Curve Name-Stall Region"
        obj.normalized_fan_static_efficiency_curve_namestall_region = var_normalized_fan_static_efficiency_curve_namestall_region
        # object-list
        var_normalized_dimensionless_airflow_curve_namenonstall_region = "object-list|Normalized Dimensionless Airflow Curve Name-Non-Stall Region"
        obj.normalized_dimensionless_airflow_curve_namenonstall_region = var_normalized_dimensionless_airflow_curve_namenonstall_region
        # object-list
        var_normalized_dimensionless_airflow_curve_namestall_region = "object-list|Normalized Dimensionless Airflow Curve Name-Stall Region"
        obj.normalized_dimensionless_airflow_curve_namestall_region = var_normalized_dimensionless_airflow_curve_namestall_region
        # object-list
        var_maximum_belt_efficiency_curve_name = "object-list|Maximum Belt Efficiency Curve Name"
        obj.maximum_belt_efficiency_curve_name = var_maximum_belt_efficiency_curve_name
        # object-list
        var_normalized_belt_efficiency_curve_name_region_1 = "object-list|Normalized Belt Efficiency Curve Name - Region 1"
        obj.normalized_belt_efficiency_curve_name_region_1 = var_normalized_belt_efficiency_curve_name_region_1
        # object-list
        var_normalized_belt_efficiency_curve_name_region_2 = "object-list|Normalized Belt Efficiency Curve Name - Region 2"
        obj.normalized_belt_efficiency_curve_name_region_2 = var_normalized_belt_efficiency_curve_name_region_2
        # object-list
        var_normalized_belt_efficiency_curve_name_region_3 = "object-list|Normalized Belt Efficiency Curve Name - Region 3"
        obj.normalized_belt_efficiency_curve_name_region_3 = var_normalized_belt_efficiency_curve_name_region_3
        # object-list
        var_maximum_motor_efficiency_curve_name = "object-list|Maximum Motor Efficiency Curve Name"
        obj.maximum_motor_efficiency_curve_name = var_maximum_motor_efficiency_curve_name
        # object-list
        var_normalized_motor_efficiency_curve_name = "object-list|Normalized Motor Efficiency Curve Name"
        obj.normalized_motor_efficiency_curve_name = var_normalized_motor_efficiency_curve_name
        # object-list
        var_vfd_efficiency_curve_name = "object-list|VFD Efficiency Curve Name"
        obj.vfd_efficiency_curve_name = var_vfd_efficiency_curve_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fancomponentmodels[0].name, var_name)
        self.assertEqual(idf2.fancomponentmodels[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.fancomponentmodels[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.fancomponentmodels[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].minimum_flow_rate, var_minimum_flow_rate)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].fan_sizing_factor, var_fan_sizing_factor)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].fan_wheel_diameter, var_fan_wheel_diameter)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].fan_outlet_area, var_fan_outlet_area)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].maximum_fan_static_efficiency, var_maximum_fan_static_efficiency)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].euler_number_at_maximum_fan_static_efficiency, var_euler_number_at_maximum_fan_static_efficiency)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].maximum_dimensionless_fan_airflow, var_maximum_dimensionless_fan_airflow)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].motor_fan_pulley_ratio, var_motor_fan_pulley_ratio)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].belt_maximum_torque, var_belt_maximum_torque)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].belt_sizing_factor, var_belt_sizing_factor)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].belt_fractional_torque_transition, var_belt_fractional_torque_transition)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].motor_maximum_speed, var_motor_maximum_speed)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].maximum_motor_output_power, var_maximum_motor_output_power)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].motor_sizing_factor, var_motor_sizing_factor)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].motor_in_airstream_fraction, var_motor_in_airstream_fraction)
        self.assertEqual(idf2.fancomponentmodels[0].vfd_efficiency_type, var_vfd_efficiency_type)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].maximum_vfd_output_power, var_maximum_vfd_output_power)
        self.assertAlmostEqual(idf2.fancomponentmodels[0].vfd_sizing_factor, var_vfd_sizing_factor)
        self.assertEqual(idf2.fancomponentmodels[0].fan_pressure_rise_curve_name, var_fan_pressure_rise_curve_name)
        self.assertEqual(idf2.fancomponentmodels[0].duct_static_pressure_reset_curve_name, var_duct_static_pressure_reset_curve_name)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_fan_static_efficiency_curve_namenonstall_region, var_normalized_fan_static_efficiency_curve_namenonstall_region)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_fan_static_efficiency_curve_namestall_region, var_normalized_fan_static_efficiency_curve_namestall_region)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_dimensionless_airflow_curve_namenonstall_region, var_normalized_dimensionless_airflow_curve_namenonstall_region)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_dimensionless_airflow_curve_namestall_region, var_normalized_dimensionless_airflow_curve_namestall_region)
        self.assertEqual(idf2.fancomponentmodels[0].maximum_belt_efficiency_curve_name, var_maximum_belt_efficiency_curve_name)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_belt_efficiency_curve_name_region_1, var_normalized_belt_efficiency_curve_name_region_1)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_belt_efficiency_curve_name_region_2, var_normalized_belt_efficiency_curve_name_region_2)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_belt_efficiency_curve_name_region_3, var_normalized_belt_efficiency_curve_name_region_3)
        self.assertEqual(idf2.fancomponentmodels[0].maximum_motor_efficiency_curve_name, var_maximum_motor_efficiency_curve_name)
        self.assertEqual(idf2.fancomponentmodels[0].normalized_motor_efficiency_curve_name, var_normalized_motor_efficiency_curve_name)
        self.assertEqual(idf2.fancomponentmodels[0].vfd_efficiency_curve_name, var_vfd_efficiency_curve_name)
        self.assertEqual(idf2.fancomponentmodels[0].enduse_subcategory, var_enduse_subcategory)