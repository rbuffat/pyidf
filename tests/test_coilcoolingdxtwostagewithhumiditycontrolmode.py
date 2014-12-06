import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingDxTwoStageWithHumidityControlMode

log = logging.getLogger(__name__)

class TestCoilCoolingDxTwoStageWithHumidityControlMode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingdxtwostagewithhumiditycontrolmode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingDxTwoStageWithHumidityControlMode()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # real
        var_crankcase_heater_capacity = 0.0
        obj.crankcase_heater_capacity = var_crankcase_heater_capacity
        # real
        var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = 0.0
        obj.maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation = var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation
        # integer
        var_number_of_capacity_stages = 1
        obj.number_of_capacity_stages = var_number_of_capacity_stages
        # integer
        var_number_of_enhanced_dehumidification_modes = 0
        obj.number_of_enhanced_dehumidification_modes = var_number_of_enhanced_dehumidification_modes
        # alpha
        var_normal_mode_stage_1_coil_performance_object_type = "CoilPerformance:DX:Cooling"
        obj.normal_mode_stage_1_coil_performance_object_type = var_normal_mode_stage_1_coil_performance_object_type
        # object-list
        var_normal_mode_stage_1_coil_performance_name = "object-list|Normal Mode Stage 1 Coil Performance Name"
        obj.normal_mode_stage_1_coil_performance_name = var_normal_mode_stage_1_coil_performance_name
        # alpha
        var_normal_mode_stage_12_coil_performance_object_type = "CoilPerformance:DX:Cooling"
        obj.normal_mode_stage_12_coil_performance_object_type = var_normal_mode_stage_12_coil_performance_object_type
        # object-list
        var_normal_mode_stage_12_coil_performance_name = "object-list|Normal Mode Stage 1+2 Coil Performance Name"
        obj.normal_mode_stage_12_coil_performance_name = var_normal_mode_stage_12_coil_performance_name
        # alpha
        var_dehumidification_mode_1_stage_1_coil_performance_object_type = "CoilPerformance:DX:Cooling"
        obj.dehumidification_mode_1_stage_1_coil_performance_object_type = var_dehumidification_mode_1_stage_1_coil_performance_object_type
        # object-list
        var_dehumidification_mode_1_stage_1_coil_performance_name = "object-list|Dehumidification Mode 1 Stage 1 Coil Performance Name"
        obj.dehumidification_mode_1_stage_1_coil_performance_name = var_dehumidification_mode_1_stage_1_coil_performance_name
        # alpha
        var_dehumidification_mode_1_stage_12_coil_performance_object_type = "CoilPerformance:DX:Cooling"
        obj.dehumidification_mode_1_stage_12_coil_performance_object_type = var_dehumidification_mode_1_stage_12_coil_performance_object_type
        # object-list
        var_dehumidification_mode_1_stage_12_coil_performance_name = "object-list|Dehumidification Mode 1 Stage 1+2 Coil Performance Name"
        obj.dehumidification_mode_1_stage_12_coil_performance_name = var_dehumidification_mode_1_stage_12_coil_performance_name
        # object-list
        var_supply_water_storage_tank_name = "object-list|Supply Water Storage Tank Name"
        obj.supply_water_storage_tank_name = var_supply_water_storage_tank_name
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].name, var_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].crankcase_heater_capacity, var_crankcase_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation, var_maximum_outdoor_drybulb_temperature_for_crankcase_heater_operation)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].number_of_capacity_stages, var_number_of_capacity_stages)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].number_of_enhanced_dehumidification_modes, var_number_of_enhanced_dehumidification_modes)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].normal_mode_stage_1_coil_performance_object_type, var_normal_mode_stage_1_coil_performance_object_type)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].normal_mode_stage_1_coil_performance_name, var_normal_mode_stage_1_coil_performance_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].normal_mode_stage_12_coil_performance_object_type, var_normal_mode_stage_12_coil_performance_object_type)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].normal_mode_stage_12_coil_performance_name, var_normal_mode_stage_12_coil_performance_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].dehumidification_mode_1_stage_1_coil_performance_object_type, var_dehumidification_mode_1_stage_1_coil_performance_object_type)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].dehumidification_mode_1_stage_1_coil_performance_name, var_dehumidification_mode_1_stage_1_coil_performance_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].dehumidification_mode_1_stage_12_coil_performance_object_type, var_dehumidification_mode_1_stage_12_coil_performance_object_type)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].dehumidification_mode_1_stage_12_coil_performance_name, var_dehumidification_mode_1_stage_12_coil_performance_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].supply_water_storage_tank_name, var_supply_water_storage_tank_name)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)
        self.assertAlmostEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.coilcoolingdxtwostagewithhumiditycontrolmodes[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)