import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingGasMultiStage

log = logging.getLogger(__name__)

class TestCoilHeatingGasMultiStage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatinggasmultistage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingGasMultiStage()
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
        # node
        var_temperature_setpoint_node_name = "node|Temperature Setpoint Node Name"
        obj.temperature_setpoint_node_name = var_temperature_setpoint_node_name
        # object-list
        var_part_load_fraction_correlation_curve_name = "object-list|Part Load Fraction Correlation Curve Name"
        obj.part_load_fraction_correlation_curve_name = var_part_load_fraction_correlation_curve_name
        # real
        var_parasitic_gas_load = 7.7
        obj.parasitic_gas_load = var_parasitic_gas_load
        # integer
        var_number_of_stages = 2
        obj.number_of_stages = var_number_of_stages
        # real
        var_stage_1_gas_burner_efficiency = 0.0001
        obj.stage_1_gas_burner_efficiency = var_stage_1_gas_burner_efficiency
        # real
        var_stage_1_nominal_capacity = 0.0001
        obj.stage_1_nominal_capacity = var_stage_1_nominal_capacity
        # real
        var_stage_1_parasitic_electric_load = 11.11
        obj.stage_1_parasitic_electric_load = var_stage_1_parasitic_electric_load
        # real
        var_stage_2_gas_burner_efficiency = 0.0001
        obj.stage_2_gas_burner_efficiency = var_stage_2_gas_burner_efficiency
        # real
        var_stage_2_nominal_capacity = 0.0001
        obj.stage_2_nominal_capacity = var_stage_2_nominal_capacity
        # real
        var_stage_2_parasitic_electric_load = 14.14
        obj.stage_2_parasitic_electric_load = var_stage_2_parasitic_electric_load
        # real
        var_stage_3_gas_burner_efficiency = 0.0001
        obj.stage_3_gas_burner_efficiency = var_stage_3_gas_burner_efficiency
        # real
        var_stage_3_nominal_capacity = 0.0001
        obj.stage_3_nominal_capacity = var_stage_3_nominal_capacity
        # real
        var_stage_3_parasitic_electric_load = 17.17
        obj.stage_3_parasitic_electric_load = var_stage_3_parasitic_electric_load
        # real
        var_stage_4_gas_burner_efficiency = 0.0001
        obj.stage_4_gas_burner_efficiency = var_stage_4_gas_burner_efficiency
        # real
        var_stage_4_nominal_capacity = 0.0001
        obj.stage_4_nominal_capacity = var_stage_4_nominal_capacity
        # real
        var_stage_4_parasitic_electric_load = 20.2
        obj.stage_4_parasitic_electric_load = var_stage_4_parasitic_electric_load

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatinggasmultistages[0].name, var_name)
        self.assertEqual(idf2.coilheatinggasmultistages[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilheatinggasmultistages[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatinggasmultistages[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilheatinggasmultistages[0].temperature_setpoint_node_name, var_temperature_setpoint_node_name)
        self.assertEqual(idf2.coilheatinggasmultistages[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].parasitic_gas_load, var_parasitic_gas_load)
        self.assertEqual(idf2.coilheatinggasmultistages[0].number_of_stages, var_number_of_stages)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_1_gas_burner_efficiency, var_stage_1_gas_burner_efficiency)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_1_nominal_capacity, var_stage_1_nominal_capacity)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_1_parasitic_electric_load, var_stage_1_parasitic_electric_load)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_2_gas_burner_efficiency, var_stage_2_gas_burner_efficiency)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_2_nominal_capacity, var_stage_2_nominal_capacity)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_2_parasitic_electric_load, var_stage_2_parasitic_electric_load)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_3_gas_burner_efficiency, var_stage_3_gas_burner_efficiency)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_3_nominal_capacity, var_stage_3_nominal_capacity)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_3_parasitic_electric_load, var_stage_3_parasitic_electric_load)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_4_gas_burner_efficiency, var_stage_4_gas_burner_efficiency)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_4_nominal_capacity, var_stage_4_nominal_capacity)
        self.assertAlmostEqual(idf2.coilheatinggasmultistages[0].stage_4_parasitic_electric_load, var_stage_4_parasitic_electric_load)