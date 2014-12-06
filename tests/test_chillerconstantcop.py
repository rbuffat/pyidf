import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.plant_heating_and_cooling_equipment import ChillerConstantCop

log = logging.getLogger(__name__)

class TestChillerConstantCop(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_chillerconstantcop(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ChillerConstantCop()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_nominal_capacity = 0.0
        obj.nominal_capacity = var_nominal_capacity
        # real
        var_nominal_cop = 0.0001
        obj.nominal_cop = var_nominal_cop
        # real
        var_design_chilled_water_flow_rate = 0.0
        obj.design_chilled_water_flow_rate = var_design_chilled_water_flow_rate
        # real
        var_design_condenser_water_flow_rate = 0.0
        obj.design_condenser_water_flow_rate = var_design_condenser_water_flow_rate
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
        # alpha
        var_condenser_type = "AirCooled"
        obj.condenser_type = var_condenser_type
        # alpha
        var_chiller_flow_mode = "ConstantFlow"
        obj.chiller_flow_mode = var_chiller_flow_mode
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.chillerconstantcops[0].name, var_name)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].nominal_capacity, var_nominal_capacity)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].nominal_cop, var_nominal_cop)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].design_chilled_water_flow_rate, var_design_chilled_water_flow_rate)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].design_condenser_water_flow_rate, var_design_condenser_water_flow_rate)
        self.assertEqual(idf2.chillerconstantcops[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.chillerconstantcops[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.chillerconstantcops[0].condenser_inlet_node_name, var_condenser_inlet_node_name)
        self.assertEqual(idf2.chillerconstantcops[0].condenser_outlet_node_name, var_condenser_outlet_node_name)
        self.assertEqual(idf2.chillerconstantcops[0].condenser_type, var_condenser_type)
        self.assertEqual(idf2.chillerconstantcops[0].chiller_flow_mode, var_chiller_flow_mode)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].sizing_factor, var_sizing_factor)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].basin_heater_capacity, var_basin_heater_capacity)
        self.assertAlmostEqual(idf2.chillerconstantcops[0].basin_heater_setpoint_temperature, var_basin_heater_setpoint_temperature)
        self.assertEqual(idf2.chillerconstantcops[0].basin_heater_operating_schedule_name, var_basin_heater_operating_schedule_name)