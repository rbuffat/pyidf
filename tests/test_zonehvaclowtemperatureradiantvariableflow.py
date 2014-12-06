import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_radiative import ZoneHvacLowTemperatureRadiantVariableFlow

log = logging.getLogger(__name__)

class TestZoneHvacLowTemperatureRadiantVariableFlow(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvaclowtemperatureradiantvariableflow(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacLowTemperatureRadiantVariableFlow()
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
        # alpha
        var_heating_design_capacity_method = "HeatingDesignCapacity"
        obj.heating_design_capacity_method = var_heating_design_capacity_method
        # real
        var_heating_design_capacity = 0.0
        obj.heating_design_capacity = var_heating_design_capacity
        # real
        var_heating_design_capacity_per_floor_area = 0.0
        obj.heating_design_capacity_per_floor_area = var_heating_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_heating_design_capacity = 0.0
        obj.fraction_of_autosized_heating_design_capacity = var_fraction_of_autosized_heating_design_capacity
        # real
        var_maximum_hot_water_flow = 0.0
        obj.maximum_hot_water_flow = var_maximum_hot_water_flow
        # node
        var_heating_water_inlet_node_name = "node|Heating Water Inlet Node Name"
        obj.heating_water_inlet_node_name = var_heating_water_inlet_node_name
        # node
        var_heating_water_outlet_node_name = "node|Heating Water Outlet Node Name"
        obj.heating_water_outlet_node_name = var_heating_water_outlet_node_name
        # real
        var_heating_control_throttling_range = 0.5
        obj.heating_control_throttling_range = var_heating_control_throttling_range
        # object-list
        var_heating_control_temperature_schedule_name = "object-list|Heating Control Temperature Schedule Name"
        obj.heating_control_temperature_schedule_name = var_heating_control_temperature_schedule_name
        # alpha
        var_cooling_design_capacity_method = "None"
        obj.cooling_design_capacity_method = var_cooling_design_capacity_method
        # real
        var_cooling_design_capacity = 0.0
        obj.cooling_design_capacity = var_cooling_design_capacity
        # real
        var_cooling_design_capacity_per_floor_area = 0.0
        obj.cooling_design_capacity_per_floor_area = var_cooling_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_cooling_design_capacity = 0.0
        obj.fraction_of_autosized_cooling_design_capacity = var_fraction_of_autosized_cooling_design_capacity
        # real
        var_maximum_cold_water_flow = 0.0
        obj.maximum_cold_water_flow = var_maximum_cold_water_flow
        # node
        var_cooling_water_inlet_node_name = "node|Cooling Water Inlet Node Name"
        obj.cooling_water_inlet_node_name = var_cooling_water_inlet_node_name
        # node
        var_cooling_water_outlet_node_name = "node|Cooling Water Outlet Node Name"
        obj.cooling_water_outlet_node_name = var_cooling_water_outlet_node_name
        # real
        var_cooling_control_throttling_range = 0.5
        obj.cooling_control_throttling_range = var_cooling_control_throttling_range
        # object-list
        var_cooling_control_temperature_schedule_name = "object-list|Cooling Control Temperature Schedule Name"
        obj.cooling_control_temperature_schedule_name = var_cooling_control_temperature_schedule_name
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
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].name, var_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].surface_name_or_radiant_surface_group_name, var_surface_name_or_radiant_surface_group_name)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].hydronic_tubing_inside_diameter, var_hydronic_tubing_inside_diameter)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].hydronic_tubing_length, var_hydronic_tubing_length)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].temperature_control_type, var_temperature_control_type)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].maximum_hot_water_flow, var_maximum_hot_water_flow)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_water_inlet_node_name, var_heating_water_inlet_node_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_water_outlet_node_name, var_heating_water_outlet_node_name)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_control_throttling_range, var_heating_control_throttling_range)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].heating_control_temperature_schedule_name, var_heating_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_design_capacity_method, var_cooling_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_design_capacity, var_cooling_design_capacity)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_design_capacity_per_floor_area, var_cooling_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].fraction_of_autosized_cooling_design_capacity, var_fraction_of_autosized_cooling_design_capacity)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].maximum_cold_water_flow, var_maximum_cold_water_flow)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_water_inlet_node_name, var_cooling_water_inlet_node_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_water_outlet_node_name, var_cooling_water_outlet_node_name)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_control_throttling_range, var_cooling_control_throttling_range)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].cooling_control_temperature_schedule_name, var_cooling_control_temperature_schedule_name)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].condensation_control_type, var_condensation_control_type)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].condensation_control_dewpoint_offset, var_condensation_control_dewpoint_offset)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].number_of_circuits, var_number_of_circuits)
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantvariableflows[0].circuit_length, var_circuit_length)