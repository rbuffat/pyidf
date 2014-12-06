import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_heaters_and_thermal_storage import ThermalStorageChilledWaterMixed

log = logging.getLogger(__name__)

class TestThermalStorageChilledWaterMixed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_thermalstoragechilledwatermixed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ThermalStorageChilledWaterMixed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_tank_volume = 0.0001
        obj.tank_volume = var_tank_volume
        # object-list
        var_setpoint_temperature_schedule_name = "object-list|Setpoint Temperature Schedule Name"
        obj.setpoint_temperature_schedule_name = var_setpoint_temperature_schedule_name
        # real
        var_deadband_temperature_difference = 0.0001
        obj.deadband_temperature_difference = var_deadband_temperature_difference
        # real
        var_minimum_temperature_limit = 5.5
        obj.minimum_temperature_limit = var_minimum_temperature_limit
        # real
        var_nominal_cooling_capacity = 6.6
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
        var_heat_gain_coefficient_from_ambient_temperature = 0.0
        obj.heat_gain_coefficient_from_ambient_temperature = var_heat_gain_coefficient_from_ambient_temperature
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
        var_source_side_design_flow_rate = 0.0
        obj.source_side_design_flow_rate = var_source_side_design_flow_rate
        # real
        var_tank_recovery_time = 0.0001
        obj.tank_recovery_time = var_tank_recovery_time

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].name, var_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].tank_volume, var_tank_volume)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].setpoint_temperature_schedule_name, var_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].deadband_temperature_difference, var_deadband_temperature_difference)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].minimum_temperature_limit, var_minimum_temperature_limit)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].nominal_cooling_capacity, var_nominal_cooling_capacity)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].ambient_temperature_indicator, var_ambient_temperature_indicator)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].ambient_temperature_schedule_name, var_ambient_temperature_schedule_name)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].ambient_temperature_zone_name, var_ambient_temperature_zone_name)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].ambient_temperature_outdoor_air_node_name, var_ambient_temperature_outdoor_air_node_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].heat_gain_coefficient_from_ambient_temperature, var_heat_gain_coefficient_from_ambient_temperature)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].use_side_inlet_node_name, var_use_side_inlet_node_name)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].use_side_outlet_node_name, var_use_side_outlet_node_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].use_side_heat_transfer_effectiveness, var_use_side_heat_transfer_effectiveness)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].use_side_availability_schedule_name, var_use_side_availability_schedule_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].use_side_design_flow_rate, var_use_side_design_flow_rate)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].source_side_inlet_node_name, var_source_side_inlet_node_name)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].source_side_outlet_node_name, var_source_side_outlet_node_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].source_side_heat_transfer_effectiveness, var_source_side_heat_transfer_effectiveness)
        self.assertEqual(idf2.thermalstoragechilledwatermixeds[0].source_side_availability_schedule_name, var_source_side_availability_schedule_name)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].source_side_design_flow_rate, var_source_side_design_flow_rate)
        self.assertAlmostEqual(idf2.thermalstoragechilledwatermixeds[0].tank_recovery_time, var_tank_recovery_time)