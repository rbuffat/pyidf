import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacWindowAirConditioner

log = logging.getLogger(__name__)

class TestZoneHvacWindowAirConditioner(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacwindowairconditioner(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacWindowAirConditioner()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_supply_air_flow_rate = 3.3
        obj.maximum_supply_air_flow_rate = var_maximum_supply_air_flow_rate
        # real
        var_maximum_outdoor_air_flow_rate = 4.4
        obj.maximum_outdoor_air_flow_rate = var_maximum_outdoor_air_flow_rate
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # alpha
        var_outdoor_air_mixer_object_type = "OutdoorAir:Mixer"
        obj.outdoor_air_mixer_object_type = var_outdoor_air_mixer_object_type
        # object-list
        var_outdoor_air_mixer_name = "object-list|Outdoor Air Mixer Name"
        obj.outdoor_air_mixer_name = var_outdoor_air_mixer_name
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_dx_cooling_coil_name = "object-list|DX Cooling Coil Name"
        obj.dx_cooling_coil_name = var_dx_cooling_coil_name
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
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
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].name, var_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.zonehvacwindowairconditioners[0].maximum_supply_air_flow_rate, var_maximum_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.zonehvacwindowairconditioners[0].maximum_outdoor_air_flow_rate, var_maximum_outdoor_air_flow_rate)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].outdoor_air_mixer_object_type, var_outdoor_air_mixer_object_type)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].outdoor_air_mixer_name, var_outdoor_air_mixer_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].dx_cooling_coil_name, var_dx_cooling_coil_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].fan_placement, var_fan_placement)
        self.assertAlmostEqual(idf2.zonehvacwindowairconditioners[0].cooling_convergence_tolerance, var_cooling_convergence_tolerance)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].availability_manager_list_name, var_availability_manager_list_name)
        self.assertEqual(idf2.zonehvacwindowairconditioners[0].design_specification_zonehvac_sizing_object_name, var_design_specification_zonehvac_sizing_object_name)