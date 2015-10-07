import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilWaterHeatingDesuperheater

log = logging.getLogger(__name__)

class TestCoilWaterHeatingDesuperheater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilwaterheatingdesuperheater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilWaterHeatingDesuperheater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_setpoint_temperature_schedule_name = "object-list|Setpoint Temperature Schedule Name"
        obj.setpoint_temperature_schedule_name = var_setpoint_temperature_schedule_name
        # real
        var_dead_band_temperature_difference = 10.00005
        obj.dead_band_temperature_difference = var_dead_band_temperature_difference
        # real
        var_rated_heat_reclaim_recovery_efficiency = 0.0001
        obj.rated_heat_reclaim_recovery_efficiency = var_rated_heat_reclaim_recovery_efficiency
        # real
        var_rated_inlet_water_temperature = 6.6
        obj.rated_inlet_water_temperature = var_rated_inlet_water_temperature
        # real
        var_rated_outdoor_air_temperature = 7.7
        obj.rated_outdoor_air_temperature = var_rated_outdoor_air_temperature
        # real
        var_maximum_inlet_water_temperature_for_heat_reclaim = 8.8
        obj.maximum_inlet_water_temperature_for_heat_reclaim = var_maximum_inlet_water_temperature_for_heat_reclaim
        # object-list
        var_heat_reclaim_efficiency_function_of_temperature_curve_name = "object-list|Heat Reclaim Efficiency Function of Temperature Curve Name"
        obj.heat_reclaim_efficiency_function_of_temperature_curve_name = var_heat_reclaim_efficiency_function_of_temperature_curve_name
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # alpha
        var_tank_object_type = "WaterHeater:Mixed"
        obj.tank_object_type = var_tank_object_type
        # object-list
        var_tank_name = "object-list|Tank Name"
        obj.tank_name = var_tank_name
        # alpha
        var_heating_source_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.heating_source_object_type = var_heating_source_object_type
        # object-list
        var_heating_source_name = "object-list|Heating Source Name"
        obj.heating_source_name = var_heating_source_name
        # real
        var_water_flow_rate = 0.0001
        obj.water_flow_rate = var_water_flow_rate
        # real
        var_water_pump_power = 0.0
        obj.water_pump_power = var_water_pump_power
        # real
        var_fraction_of_pump_heat_to_water = 0.5
        obj.fraction_of_pump_heat_to_water = var_fraction_of_pump_heat_to_water
        # real
        var_oncycle_parasitic_electric_load = 0.0
        obj.oncycle_parasitic_electric_load = var_oncycle_parasitic_electric_load
        # real
        var_offcycle_parasitic_electric_load = 0.0
        obj.offcycle_parasitic_electric_load = var_offcycle_parasitic_electric_load

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].name, var_name)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].setpoint_temperature_schedule_name, var_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].dead_band_temperature_difference, var_dead_band_temperature_difference)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].rated_heat_reclaim_recovery_efficiency, var_rated_heat_reclaim_recovery_efficiency)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].rated_inlet_water_temperature, var_rated_inlet_water_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].rated_outdoor_air_temperature, var_rated_outdoor_air_temperature)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].maximum_inlet_water_temperature_for_heat_reclaim, var_maximum_inlet_water_temperature_for_heat_reclaim)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].heat_reclaim_efficiency_function_of_temperature_curve_name, var_heat_reclaim_efficiency_function_of_temperature_curve_name)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].tank_object_type, var_tank_object_type)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].tank_name, var_tank_name)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].heating_source_object_type, var_heating_source_object_type)
        self.assertEqual(idf2.coilwaterheatingdesuperheaters[0].heating_source_name, var_heating_source_name)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].water_flow_rate, var_water_flow_rate)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].water_pump_power, var_water_pump_power)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].fraction_of_pump_heat_to_water, var_fraction_of_pump_heat_to_water)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].oncycle_parasitic_electric_load, var_oncycle_parasitic_electric_load)
        self.assertAlmostEqual(idf2.coilwaterheatingdesuperheaters[0].offcycle_parasitic_electric_load, var_offcycle_parasitic_electric_load)