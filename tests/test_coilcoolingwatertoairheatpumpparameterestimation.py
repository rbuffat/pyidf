import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilCoolingWaterToAirHeatPumpParameterEstimation

log = logging.getLogger(__name__)

class TestCoilCoolingWaterToAirHeatPumpParameterEstimation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingwatertoairheatpumpparameterestimation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingWaterToAirHeatPumpParameterEstimation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_compressor_type = "Reciprocating"
        obj.compressor_type = var_compressor_type
        # object-list
        var_refrigerant_type = "object-list|Refrigerant Type"
        obj.refrigerant_type = var_refrigerant_type
        # real
        var_design_source_side_flow_rate = 0.0001
        obj.design_source_side_flow_rate = var_design_source_side_flow_rate
        # real
        var_nominal_cooling_coil_capacity = 0.0001
        obj.nominal_cooling_coil_capacity = var_nominal_cooling_coil_capacity
        # real
        var_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.nominal_time_for_condensate_removal_to_begin = var_nominal_time_for_condensate_removal_to_begin
        # real
        var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity
        # real
        var_high_pressure_cutoff = 0.0001
        obj.high_pressure_cutoff = var_high_pressure_cutoff
        # real
        var_low_pressure_cutoff = 0.0
        obj.low_pressure_cutoff = var_low_pressure_cutoff
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # real
        var_load_side_total_heat_transfer_coefficient = 0.0001
        obj.load_side_total_heat_transfer_coefficient = var_load_side_total_heat_transfer_coefficient
        # real
        var_load_side_outside_surface_heat_transfer_coefficient = 0.0001
        obj.load_side_outside_surface_heat_transfer_coefficient = var_load_side_outside_surface_heat_transfer_coefficient
        # real
        var_superheat_temperature_at_the_evaporator_outlet = 0.0001
        obj.superheat_temperature_at_the_evaporator_outlet = var_superheat_temperature_at_the_evaporator_outlet
        # real
        var_compressor_power_losses = 0.0001
        obj.compressor_power_losses = var_compressor_power_losses
        # real
        var_compressor_efficiency = 0.0001
        obj.compressor_efficiency = var_compressor_efficiency
        # real
        var_compressor_piston_displacement = 0.0001
        obj.compressor_piston_displacement = var_compressor_piston_displacement
        # real
        var_compressor_suction_or_discharge_pressure_drop = 0.0001
        obj.compressor_suction_or_discharge_pressure_drop = var_compressor_suction_or_discharge_pressure_drop
        # real
        var_compressor_clearance_factor = 0.0001
        obj.compressor_clearance_factor = var_compressor_clearance_factor
        # real
        var_refrigerant_volume_flow_rate = 0.0001
        obj.refrigerant_volume_flow_rate = var_refrigerant_volume_flow_rate
        # real
        var_volume_ratio = 0.0001
        obj.volume_ratio = var_volume_ratio
        # real
        var_leak_rate_coefficient = 0.0
        obj.leak_rate_coefficient = var_leak_rate_coefficient
        # real
        var_source_side_heat_transfer_coefficient = 0.0
        obj.source_side_heat_transfer_coefficient = var_source_side_heat_transfer_coefficient
        # real
        var_source_side_heat_transfer_resistance1 = 0.0
        obj.source_side_heat_transfer_resistance1 = var_source_side_heat_transfer_resistance1
        # real
        var_source_side_heat_transfer_resistance2 = 0.0
        obj.source_side_heat_transfer_resistance2 = var_source_side_heat_transfer_resistance2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].name, var_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].compressor_type, var_compressor_type)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].refrigerant_type, var_refrigerant_type)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].design_source_side_flow_rate, var_design_source_side_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].nominal_cooling_coil_capacity, var_nominal_cooling_coil_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].nominal_time_for_condensate_removal_to_begin, var_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].high_pressure_cutoff, var_high_pressure_cutoff)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].low_pressure_cutoff, var_low_pressure_cutoff)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].load_side_total_heat_transfer_coefficient, var_load_side_total_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].load_side_outside_surface_heat_transfer_coefficient, var_load_side_outside_surface_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].superheat_temperature_at_the_evaporator_outlet, var_superheat_temperature_at_the_evaporator_outlet)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].compressor_power_losses, var_compressor_power_losses)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].compressor_efficiency, var_compressor_efficiency)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].compressor_piston_displacement, var_compressor_piston_displacement)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].compressor_suction_or_discharge_pressure_drop, var_compressor_suction_or_discharge_pressure_drop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].compressor_clearance_factor, var_compressor_clearance_factor)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].refrigerant_volume_flow_rate, var_refrigerant_volume_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].volume_ratio, var_volume_ratio)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].leak_rate_coefficient, var_leak_rate_coefficient)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].source_side_heat_transfer_coefficient, var_source_side_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].source_side_heat_transfer_resistance1, var_source_side_heat_transfer_resistance1)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpparameterestimations[0].source_side_heat_transfer_resistance2, var_source_side_heat_transfer_resistance2)