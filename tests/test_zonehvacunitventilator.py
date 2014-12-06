import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_forced_air_units import ZoneHvacUnitVentilator
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacUnitVentilator(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacunitventilator(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacUnitVentilator()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_supply_air_flow_rate = 0.0001
        obj.maximum_supply_air_flow_rate = var_maximum_supply_air_flow_rate
        # alpha
        var_outdoor_air_control_type = "FixedAmount"
        obj.outdoor_air_control_type = var_outdoor_air_control_type
        # real
        var_minimum_outdoor_air_flow_rate = 0.0
        obj.minimum_outdoor_air_flow_rate = var_minimum_outdoor_air_flow_rate
        # object-list
        var_minimum_outdoor_air_schedule_name = "object-list|Minimum Outdoor Air Schedule Name"
        obj.minimum_outdoor_air_schedule_name = var_minimum_outdoor_air_schedule_name
        # real
        var_maximum_outdoor_air_flow_rate = 0.0
        obj.maximum_outdoor_air_flow_rate = var_maximum_outdoor_air_flow_rate
        # object-list
        var_maximum_outdoor_air_fraction_or_temperature_schedule_name = "object-list|Maximum Outdoor Air Fraction or Temperature Schedule Name"
        obj.maximum_outdoor_air_fraction_or_temperature_schedule_name = var_maximum_outdoor_air_fraction_or_temperature_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # node
        var_outdoor_air_node_name = "node|Outdoor Air Node Name"
        obj.outdoor_air_node_name = var_outdoor_air_node_name
        # node
        var_exhaust_air_node_name = "node|Exhaust Air Node Name"
        obj.exhaust_air_node_name = var_exhaust_air_node_name
        # node
        var_mixed_air_node_name = "node|Mixed Air Node Name"
        obj.mixed_air_node_name = var_mixed_air_node_name
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # alpha
        var_coil_option = "None"
        obj.coil_option = var_coil_option
        # alpha
        var_supply_air_fan_operating_mode_schedule_name = "Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:Water"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_heating_convergence_tolerance = 0.0001
        obj.heating_convergence_tolerance = var_heating_convergence_tolerance
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:Water"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # real
        var_cooling_convergence_tolerance = 0.0001
        obj.cooling_convergence_tolerance = var_cooling_convergence_tolerance
        # object-list
        var_availability_manager_list_name = "object-list|Availability Manager List Name"
        obj.availability_manager_list_name = var_availability_manager_list_name
        # object-list
        var_design_specification_zonehvac_sizing_object_name = "object-list|Design Specification ZoneHVAC Sizing Object Name"
        obj.design_specification_zonehvac_sizing_object_name = var_design_specification_zonehvac_sizing_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacunitventilators[0].name, var_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.zonehvacunitventilators[0].maximum_supply_air_flow_rate, var_maximum_supply_air_flow_rate)
        self.assertEqual(idf2.zonehvacunitventilators[0].outdoor_air_control_type, var_outdoor_air_control_type)
        self.assertAlmostEqual(idf2.zonehvacunitventilators[0].minimum_outdoor_air_flow_rate, var_minimum_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacunitventilators[0].minimum_outdoor_air_schedule_name, var_minimum_outdoor_air_schedule_name)
        self.assertAlmostEqual(idf2.zonehvacunitventilators[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacunitventilators[0].maximum_outdoor_air_fraction_or_temperature_schedule_name, var_maximum_outdoor_air_fraction_or_temperature_schedule_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].outdoor_air_node_name, var_outdoor_air_node_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].exhaust_air_node_name, var_exhaust_air_node_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].mixed_air_node_name, var_mixed_air_node_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacunitventilators[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].coil_option, var_coil_option)
        self.assertEqual(idf2.zonehvacunitventilators[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.zonehvacunitventilators[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.zonehvacunitventilators[0].heating_convergence_tolerance, var_heating_convergence_tolerance)
        self.assertEqual(idf2.zonehvacunitventilators[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacunitventilators[0].cooling_coil_name, var_cooling_coil_name)
        self.assertAlmostEqual(idf2.zonehvacunitventilators[0].cooling_convergence_tolerance, var_cooling_convergence_tolerance)
        self.assertEqual(idf2.zonehvacunitventilators[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacunitventilators[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)