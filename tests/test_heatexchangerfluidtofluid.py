import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import HeatExchangerFluidToFluid

log = logging.getLogger(__name__)

class TestHeatExchangerFluidToFluid(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatexchangerfluidtofluid(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatExchangerFluidToFluid()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_loop_demand_side_inlet_node_name = "node|Loop Demand Side Inlet Node Name"
        obj.loop_demand_side_inlet_node_name = var_loop_demand_side_inlet_node_name
        # node
        var_loop_demand_side_outlet_node_name = "node|Loop Demand Side Outlet Node Name"
        obj.loop_demand_side_outlet_node_name = var_loop_demand_side_outlet_node_name
        # real
        var_loop_demand_side_design_flow_rate = 0.0001
        obj.loop_demand_side_design_flow_rate = var_loop_demand_side_design_flow_rate
        # node
        var_loop_supply_side_inlet_node_name = "node|Loop Supply Side Inlet Node Name"
        obj.loop_supply_side_inlet_node_name = var_loop_supply_side_inlet_node_name
        # node
        var_loop_supply_side_outlet_node_name = "node|Loop Supply Side Outlet Node Name"
        obj.loop_supply_side_outlet_node_name = var_loop_supply_side_outlet_node_name
        # real
        var_loop_supply_side_design_flow_rate = 0.0001
        obj.loop_supply_side_design_flow_rate = var_loop_supply_side_design_flow_rate
        # alpha
        var_heat_exchange_model_type = "CrossFlowBothUnMixed"
        obj.heat_exchange_model_type = var_heat_exchange_model_type
        # real
        var_heat_exchanger_ufactor_times_area_value = 0.0001
        obj.heat_exchanger_ufactor_times_area_value = var_heat_exchanger_ufactor_times_area_value
        # alpha
        var_control_type = "UncontrolledOn"
        obj.control_type = var_control_type
        # node
        var_heat_exchanger_setpoint_node_name = "node|Heat Exchanger Setpoint Node Name"
        obj.heat_exchanger_setpoint_node_name = var_heat_exchanger_setpoint_node_name
        # real
        var_minimum_temperature_difference_to_activate_heat_exchanger = 25.0
        obj.minimum_temperature_difference_to_activate_heat_exchanger = var_minimum_temperature_difference_to_activate_heat_exchanger
        # alpha
        var_heat_transfer_metering_end_use_type = "FreeCooling"
        obj.heat_transfer_metering_end_use_type = var_heat_transfer_metering_end_use_type
        # node
        var_component_override_loop_supply_side_inlet_node_name = "node|Component Override Loop Supply Side Inlet Node Name"
        obj.component_override_loop_supply_side_inlet_node_name = var_component_override_loop_supply_side_inlet_node_name
        # node
        var_component_override_loop_demand_side_inlet_node_name = "node|Component Override Loop Demand Side Inlet Node Name"
        obj.component_override_loop_demand_side_inlet_node_name = var_component_override_loop_demand_side_inlet_node_name
        # alpha
        var_component_override_cooling_control_temperature_mode = "WetBulbTemperature"
        obj.component_override_cooling_control_temperature_mode = var_component_override_cooling_control_temperature_mode
        # real
        var_sizing_factor = 0.0001
        obj.sizing_factor = var_sizing_factor
        # real
        var_operation_minimum_temperature_limit = 19.19
        obj.operation_minimum_temperature_limit = var_operation_minimum_temperature_limit
        # real
        var_operation_maximum_temperature_limit = 20.2
        obj.operation_maximum_temperature_limit = var_operation_maximum_temperature_limit

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].name, var_name)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].loop_demand_side_inlet_node_name, var_loop_demand_side_inlet_node_name)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].loop_demand_side_outlet_node_name, var_loop_demand_side_outlet_node_name)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].loop_demand_side_design_flow_rate, var_loop_demand_side_design_flow_rate)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].loop_supply_side_inlet_node_name, var_loop_supply_side_inlet_node_name)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].loop_supply_side_outlet_node_name, var_loop_supply_side_outlet_node_name)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].loop_supply_side_design_flow_rate, var_loop_supply_side_design_flow_rate)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].heat_exchange_model_type, var_heat_exchange_model_type)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].heat_exchanger_ufactor_times_area_value, var_heat_exchanger_ufactor_times_area_value)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].control_type, var_control_type)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].heat_exchanger_setpoint_node_name, var_heat_exchanger_setpoint_node_name)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].minimum_temperature_difference_to_activate_heat_exchanger, var_minimum_temperature_difference_to_activate_heat_exchanger)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].heat_transfer_metering_end_use_type, var_heat_transfer_metering_end_use_type)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].component_override_loop_supply_side_inlet_node_name, var_component_override_loop_supply_side_inlet_node_name)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].component_override_loop_demand_side_inlet_node_name, var_component_override_loop_demand_side_inlet_node_name)
        self.assertEqual(idf2.heatexchangerfluidtofluids[0].component_override_cooling_control_temperature_mode, var_component_override_cooling_control_temperature_mode)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].operation_minimum_temperature_limit, var_operation_minimum_temperature_limit)
        self.assertAlmostEqual(idf2.heatexchangerfluidtofluids[0].operation_maximum_temperature_limit, var_operation_maximum_temperature_limit)