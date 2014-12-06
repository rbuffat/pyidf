import os
import tempfile
import unittest
import pyidf
from pyidf.water_heaters_and_thermal_storage import ThermalStorageChilledWaterStratified
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestThermalStorageChilledWaterStratified(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermalstoragechilledwaterstratified(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermalStorageChilledWaterStratified()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_tank_volume = 0.0001
        obj.tank_volume = var_tank_volume
        # real
        var_tank_height = 0.0001
        obj.tank_height = var_tank_height
        # alpha
        var_tank_shape = "VerticalCylinder"
        obj.tank_shape = var_tank_shape
        # real
        var_tank_perimeter = 0.0
        obj.tank_perimeter = var_tank_perimeter
        # object-list
        var_setpoint_temperature_schedule_name = "object-list|Setpoint Temperature Schedule Name"
        obj.setpoint_temperature_schedule_name = var_setpoint_temperature_schedule_name
        # real
        var_deadband_temperature_difference = 0.0
        obj.deadband_temperature_difference = var_deadband_temperature_difference
        # real
        var_temperature_sensor_height = 0.0
        obj.temperature_sensor_height = var_temperature_sensor_height
        # real
        var_minimum_temperature_limit = 9.9
        obj.minimum_temperature_limit = var_minimum_temperature_limit
        # real
        var_nominal_cooling_capacity = 10.1
        obj.nominal_cooling_capacity = var_nominal_cooling_capacity
        # alpha
        var_ambient_temperature_indicator = "Schedule"
        obj.ambient_temperature_indicator = var_ambient_temperature_indicator
        # object-list
        var_ambient_temperature_schedule_name = "object-list|Ambient Temperature Schedule Name"
        obj.ambient_temperature_schedule_name = var_ambient_temperature_schedule_name
        # object-list
        var_ambient_temperature_zone_name = "object-list|Ambient Temperature Zone Name"
        obj.ambient_temperature_zone_name = var_ambient_temperature_zone_name
        # node
        var_ambient_temperature_outdoor_air_node_name = "node|Ambient Temperature Outdoor Air Node Name"
        obj.ambient_temperature_outdoor_air_node_name = var_ambient_temperature_outdoor_air_node_name
        # real
        var_uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = 0.0
        obj.uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature = var_uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature
        # node
        var_use_side_inlet_node_name = "node|Use Side Inlet Node Name"
        obj.use_side_inlet_node_name = var_use_side_inlet_node_name
        # node
        var_use_side_outlet_node_name = "node|Use Side Outlet Node Name"
        obj.use_side_outlet_node_name = var_use_side_outlet_node_name
        # real
        var_use_side_heat_transfer_effectiveness = 0.5
        obj.use_side_heat_transfer_effectiveness = var_use_side_heat_transfer_effectiveness
        # object-list
        var_use_side_availability_schedule_name = "object-list|Use Side Availability Schedule Name"
        obj.use_side_availability_schedule_name = var_use_side_availability_schedule_name
        # real
        var_use_side_inlet_height = 0.0
        obj.use_side_inlet_height = var_use_side_inlet_height
        # real
        var_use_side_outlet_height = 0.0
        obj.use_side_outlet_height = var_use_side_outlet_height
        # real
        var_use_side_design_flow_rate = 0.0
        obj.use_side_design_flow_rate = var_use_side_design_flow_rate
        # node
        var_source_side_inlet_node_name = "node|Source Side Inlet Node Name"
        obj.source_side_inlet_node_name = var_source_side_inlet_node_name
        # node
        var_source_side_outlet_node_name = "node|Source Side Outlet Node Name"
        obj.source_side_outlet_node_name = var_source_side_outlet_node_name
        # real
        var_source_side_heat_transfer_effectiveness = 0.5
        obj.source_side_heat_transfer_effectiveness = var_source_side_heat_transfer_effectiveness
        # object-list
        var_source_side_availability_schedule_name = "object-list|Source Side Availability Schedule Name"
        obj.source_side_availability_schedule_name = var_source_side_availability_schedule_name
        # real
        var_source_side_inlet_height = 0.0
        obj.source_side_inlet_height = var_source_side_inlet_height
        # real
        var_source_side_outlet_height = 0.0
        obj.source_side_outlet_height = var_source_side_outlet_height
        # real
        var_source_side_design_flow_rate = 0.0
        obj.source_side_design_flow_rate = var_source_side_design_flow_rate
        # real
        var_tank_recovery_time = 0.0001
        obj.tank_recovery_time = var_tank_recovery_time
        # alpha
        var_inlet_mode = "Fixed"
        obj.inlet_mode = var_inlet_mode
        # integer
        var_number_of_nodes = 5
        obj.number_of_nodes = var_number_of_nodes
        # real
        var_additional_destratification_conductivity = 0.0
        obj.additional_destratification_conductivity = var_additional_destratification_conductivity
        # real
        var_node_1_additional_loss_coefficient = 34.34
        obj.node_1_additional_loss_coefficient = var_node_1_additional_loss_coefficient
        # real
        var_node_2_additional_loss_coefficient = 35.35
        obj.node_2_additional_loss_coefficient = var_node_2_additional_loss_coefficient
        # real
        var_node_3_additional_loss_coefficient = 36.36
        obj.node_3_additional_loss_coefficient = var_node_3_additional_loss_coefficient
        # real
        var_node_4_additional_loss_coefficient = 37.37
        obj.node_4_additional_loss_coefficient = var_node_4_additional_loss_coefficient
        # real
        var_node_5_additional_loss_coefficient = 38.38
        obj.node_5_additional_loss_coefficient = var_node_5_additional_loss_coefficient
        # real
        var_node_6_additional_loss_coefficient = 39.39
        obj.node_6_additional_loss_coefficient = var_node_6_additional_loss_coefficient
        # real
        var_node_7_additional_loss_coefficient = 40.4
        obj.node_7_additional_loss_coefficient = var_node_7_additional_loss_coefficient
        # real
        var_node_8_additional_loss_coefficient = 41.41
        obj.node_8_additional_loss_coefficient = var_node_8_additional_loss_coefficient
        # real
        var_node_9_additional_loss_coefficient = 42.42
        obj.node_9_additional_loss_coefficient = var_node_9_additional_loss_coefficient
        # real
        var_node_10_additional_loss_coefficient = 43.43
        obj.node_10_additional_loss_coefficient = var_node_10_additional_loss_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].name, var_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].tank_volume, var_tank_volume)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].tank_height, var_tank_height)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].tank_shape, var_tank_shape)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].tank_perimeter, var_tank_perimeter)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].setpoint_temperature_schedule_name, var_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].deadband_temperature_difference, var_deadband_temperature_difference)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].temperature_sensor_height, var_temperature_sensor_height)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].minimum_temperature_limit, var_minimum_temperature_limit)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].nominal_cooling_capacity, var_nominal_cooling_capacity)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].ambient_temperature_indicator, var_ambient_temperature_indicator)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].ambient_temperature_schedule_name, var_ambient_temperature_schedule_name)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].ambient_temperature_zone_name, var_ambient_temperature_zone_name)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].ambient_temperature_outdoor_air_node_name, var_ambient_temperature_outdoor_air_node_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature, var_uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_inlet_node_name, var_use_side_inlet_node_name)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_outlet_node_name, var_use_side_outlet_node_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_heat_transfer_effectiveness, var_use_side_heat_transfer_effectiveness)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_availability_schedule_name, var_use_side_availability_schedule_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_inlet_height, var_use_side_inlet_height)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_outlet_height, var_use_side_outlet_height)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].use_side_design_flow_rate, var_use_side_design_flow_rate)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_inlet_node_name, var_source_side_inlet_node_name)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_outlet_node_name, var_source_side_outlet_node_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_heat_transfer_effectiveness, var_source_side_heat_transfer_effectiveness)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_availability_schedule_name, var_source_side_availability_schedule_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_inlet_height, var_source_side_inlet_height)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_outlet_height, var_source_side_outlet_height)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].source_side_design_flow_rate, var_source_side_design_flow_rate)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].tank_recovery_time, var_tank_recovery_time)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].inlet_mode, var_inlet_mode)
        self.assertEqual(idf2.thermalstoragechilledwaterstratifieds[0].number_of_nodes, var_number_of_nodes)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].additional_destratification_conductivity, var_additional_destratification_conductivity)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_1_additional_loss_coefficient, var_node_1_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_2_additional_loss_coefficient, var_node_2_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_3_additional_loss_coefficient, var_node_3_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_4_additional_loss_coefficient, var_node_4_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_5_additional_loss_coefficient, var_node_5_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_6_additional_loss_coefficient, var_node_6_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_7_additional_loss_coefficient, var_node_7_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_8_additional_loss_coefficient, var_node_8_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_9_additional_loss_coefficient, var_node_9_additional_loss_coefficient)
        self.assertAlmostEqual(idf2.thermalstoragechilledwaterstratifieds[0].node_10_additional_loss_coefficient, var_node_10_additional_loss_coefficient)