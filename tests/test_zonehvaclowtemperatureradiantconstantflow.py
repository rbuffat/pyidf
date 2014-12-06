import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_radiative import ZoneHvacLowTemperatureRadiantConstantFlow

log = logging.getLogger(__name__)

class TestZoneHvacLowTemperatureRadiantConstantFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvaclowtemperatureradiantconstantflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacLowTemperatureRadiantConstantFlow()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_surface_name_or_radiant_surface_group_name = "object-list|Surface Name or Radiant Surface Group Name"
        obj.surface_name_or_radiant_surface_group_name = var_surface_name_or_radiant_surface_group_name
        # real
        var_hydronic_tubing_inside_diameter = 0.0001
        obj.hydronic_tubing_inside_diameter = var_hydronic_tubing_inside_diameter
        # real
        var_hydronic_tubing_length = 0.0001
        obj.hydronic_tubing_length = var_hydronic_tubing_length
        # alpha
        var_temperature_control_type = "MeanAirTemperature"
        obj.temperature_control_type = var_temperature_control_type
        # real
        var_rated_flow_rate = 8.8
        obj.rated_flow_rate = var_rated_flow_rate
        # object-list
        var_pump_flow_rate_schedule_name = "object-list|Pump Flow Rate Schedule Name"
        obj.pump_flow_rate_schedule_name = var_pump_flow_rate_schedule_name
        # real
        var_rated_pump_head = 10.1
        obj.rated_pump_head = var_rated_pump_head
        # real
        var_rated_power_consumption = 11.11
        obj.rated_power_consumption = var_rated_power_consumption
        # real
        var_motor_efficiency = 0.5
        obj.motor_efficiency = var_motor_efficiency
        # real
        var_fraction_of_motor_inefficiencies_to_fluid_stream = 0.5
        obj.fraction_of_motor_inefficiencies_to_fluid_stream = var_fraction_of_motor_inefficiencies_to_fluid_stream
        # node
        var_heating_water_inlet_node_name = "node|Heating Water Inlet Node Name"
        obj.heating_water_inlet_node_name = var_heating_water_inlet_node_name
        # node
        var_heating_water_outlet_node_name = "node|Heating Water Outlet Node Name"
        obj.heating_water_outlet_node_name = var_heating_water_outlet_node_name
        # object-list
        var_heating_high_water_temperature_schedule_name = "object-list|Heating High Water Temperature Schedule Name"
        obj.heating_high_water_temperature_schedule_name = var_heating_high_water_temperature_schedule_name
        # object-list
        var_heating_low_water_temperature_schedule_name = "object-list|Heating Low Water Temperature Schedule Name"
        obj.heating_low_water_temperature_schedule_name = var_heating_low_water_temperature_schedule_name
        # object-list
        var_heating_high_control_temperature_schedule_name = "object-list|Heating High Control Temperature Schedule Name"
        obj.heating_high_control_temperature_schedule_name = var_heating_high_control_temperature_schedule_name
        # object-list
        var_heating_low_control_temperature_schedule_name = "object-list|Heating Low Control Temperature Schedule Name"
        obj.heating_low_control_temperature_schedule_name = var_heating_low_control_temperature_schedule_name
        # node
        var_cooling_water_inlet_node_name = "node|Cooling Water Inlet Node Name"
        obj.cooling_water_inlet_node_name = var_cooling_water_inlet_node_name
        # node
        var_cooling_water_outlet_node_name = "node|Cooling Water Outlet Node Name"
        obj.cooling_water_outlet_node_name = var_cooling_water_outlet_node_name
        # object-list
        var_cooling_high_water_temperature_schedule_name = "object-list|Cooling High Water Temperature Schedule Name"
        obj.cooling_high_water_temperature_schedule_name = var_cooling_high_water_temperature_schedule_name
        # object-list
        var_cooling_low_water_temperature_schedule_name = "object-list|Cooling Low Water Temperature Schedule Name"
        obj.cooling_low_water_temperature_schedule_name = var_cooling_low_water_temperature_schedule_name
        # object-list
        var_cooling_high_control_temperature_schedule_name = "object-list|Cooling High Control Temperature Schedule Name"
        obj.cooling_high_control_temperature_schedule_name = var_cooling_high_control_temperature_schedule_name
        # object-list
        var_cooling_low_control_temperature_schedule_name = "object-list|Cooling Low Control Temperature Schedule Name"
        obj.cooling_low_control_temperature_schedule_name = var_cooling_low_control_temperature_schedule_name
        # alpha
        var_condensation_control_type = "Off"
        obj.condensation_control_type = var_condensation_control_type
        # real
        var_condensation_control_dewpoint_offset = 27.27
        obj.condensation_control_dewpoint_offset = var_condensation_control_dewpoint_offset
        # alpha
        var_number_of_circuits = "OnePerSurface"
        obj.number_of_circuits = var_number_of_circuits
        # real
        var_circuit_length = 29.29
        obj.circuit_length = var_circuit_length

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].name, var_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].surface_name_or_radiant_surface_group_name, var_surface_name_or_radiant_surface_group_name)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].hydronic_tubing_inside_diameter, var_hydronic_tubing_inside_diameter)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].hydronic_tubing_length, var_hydronic_tubing_length)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].temperature_control_type, var_temperature_control_type)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].rated_flow_rate, var_rated_flow_rate)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].pump_flow_rate_schedule_name, var_pump_flow_rate_schedule_name)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].rated_pump_head, var_rated_pump_head)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].rated_power_consumption, var_rated_power_consumption)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].motor_efficiency, var_motor_efficiency)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].fraction_of_motor_inefficiencies_to_fluid_stream, var_fraction_of_motor_inefficiencies_to_fluid_stream)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].heating_water_inlet_node_name, var_heating_water_inlet_node_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].heating_water_outlet_node_name, var_heating_water_outlet_node_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].heating_high_water_temperature_schedule_name, var_heating_high_water_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].heating_low_water_temperature_schedule_name, var_heating_low_water_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].heating_high_control_temperature_schedule_name, var_heating_high_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].heating_low_control_temperature_schedule_name, var_heating_low_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].cooling_water_inlet_node_name, var_cooling_water_inlet_node_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].cooling_water_outlet_node_name, var_cooling_water_outlet_node_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].cooling_high_water_temperature_schedule_name, var_cooling_high_water_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].cooling_low_water_temperature_schedule_name, var_cooling_low_water_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].cooling_high_control_temperature_schedule_name, var_cooling_high_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].cooling_low_control_temperature_schedule_name, var_cooling_low_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].condensation_control_type, var_condensation_control_type)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].condensation_control_dewpoint_offset, var_condensation_control_dewpoint_offset)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].number_of_circuits, var_number_of_circuits)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantconstantflows[0].circuit_length, var_circuit_length)