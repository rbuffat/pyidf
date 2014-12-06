import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import HeatPumpWaterToWaterParameterEstimationCooling

log = logging.getLogger(__name__)

class TestHeatPumpWaterToWaterParameterEstimationCooling(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatpumpwatertowaterparameterestimationcooling(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatPumpWaterToWaterParameterEstimationCooling()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_source_side_inlet_node_name = "node|Source Side Inlet Node Name"
        obj.source_side_inlet_node_name = var_source_side_inlet_node_name
        # node
        var_source_side_outlet_node_name = "node|Source Side Outlet Node Name"
        obj.source_side_outlet_node_name = var_source_side_outlet_node_name
        # node
        var_load_side_inlet_node_name = "node|Load Side Inlet Node Name"
        obj.load_side_inlet_node_name = var_load_side_inlet_node_name
        # node
        var_load_side_outlet_node_name = "node|Load Side Outlet Node Name"
        obj.load_side_outlet_node_name = var_load_side_outlet_node_name
        # real
        var_nominal_cop = 0.0001
        obj.nominal_cop = var_nominal_cop
        # real
        var_nominal_capacity = 0.0001
        obj.nominal_capacity = var_nominal_capacity
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
        var_load_side_flow_rate = 0.0001
        obj.load_side_flow_rate = var_load_side_flow_rate
        # real
        var_source_side_flow_rate = 0.0001
        obj.source_side_flow_rate = var_source_side_flow_rate
        # real
        var_load_side_heat_transfer_coefficient = 0.0001
        obj.load_side_heat_transfer_coefficient = var_load_side_heat_transfer_coefficient
        # real
        var_source_side_heat_transfer_coefficient = 0.0001
        obj.source_side_heat_transfer_coefficient = var_source_side_heat_transfer_coefficient
        # real
        var_piston_displacement = 0.0001
        obj.piston_displacement = var_piston_displacement
        # real
        var_compressor_clearance_factor = 0.0001
        obj.compressor_clearance_factor = var_compressor_clearance_factor
        # real
        var_compressor_suction_and_discharge_pressure_drop = 0.0001
        obj.compressor_suction_and_discharge_pressure_drop = var_compressor_suction_and_discharge_pressure_drop
        # real
        var_superheating = 0.0001
        obj.superheating = var_superheating
        # real
        var_constant_part_of_electromechanical_power_losses = 0.0001
        obj.constant_part_of_electromechanical_power_losses = var_constant_part_of_electromechanical_power_losses
        # real
        var_loss_factor = 0.0001
        obj.loss_factor = var_loss_factor
        # real
        var_high_pressure_cut_off = 0.0
        obj.high_pressure_cut_off = var_high_pressure_cut_off
        # real
        var_low_pressure_cut_off = 0.0
        obj.low_pressure_cut_off = var_low_pressure_cut_off

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].name, var_name)
        self.assertEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].source_side_inlet_node_name, var_source_side_inlet_node_name)
        self.assertEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].source_side_outlet_node_name, var_source_side_outlet_node_name)
        self.assertEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].load_side_inlet_node_name, var_load_side_inlet_node_name)
        self.assertEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].load_side_outlet_node_name, var_load_side_outlet_node_name)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].nominal_cop, var_nominal_cop)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].minimum_part_load_ratio, var_minimum_part_load_ratio)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].maximum_part_load_ratio, var_maximum_part_load_ratio)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].optimum_part_load_ratio, var_optimum_part_load_ratio)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].load_side_flow_rate, var_load_side_flow_rate)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].source_side_flow_rate, var_source_side_flow_rate)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].load_side_heat_transfer_coefficient, var_load_side_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].source_side_heat_transfer_coefficient, var_source_side_heat_transfer_coefficient)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].piston_displacement, var_piston_displacement)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].compressor_clearance_factor, var_compressor_clearance_factor)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].compressor_suction_and_discharge_pressure_drop, var_compressor_suction_and_discharge_pressure_drop)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].superheating, var_superheating)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].constant_part_of_electromechanical_power_losses, var_constant_part_of_electromechanical_power_losses)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].loss_factor, var_loss_factor)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].high_pressure_cut_off, var_high_pressure_cut_off)
        self.assertAlmostEqual(idf2.heatpumpwatertowaterparameterestimationcoolings[0].low_pressure_cut_off, var_low_pressure_cut_off)