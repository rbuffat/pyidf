import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctConstantVolumeFourPipeBeam

log = logging.getLogger(__name__)

class TestAirTerminalSingleDuctConstantVolumeFourPipeBeam(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductconstantvolumefourpipebeam(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctConstantVolumeFourPipeBeam()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_primary_air_availability_schedule_name = "object-list|Primary Air Availability Schedule Name"
        obj.primary_air_availability_schedule_name = var_primary_air_availability_schedule_name
        # object-list
        var_cooling_availability_schedule_name = "object-list|Cooling Availability Schedule Name"
        obj.cooling_availability_schedule_name = var_cooling_availability_schedule_name
        # object-list
        var_heating_availability_schedule_name = "object-list|Heating Availability Schedule Name"
        obj.heating_availability_schedule_name = var_heating_availability_schedule_name
        # node
        var_primary_air_inlet_node_name = "node|Primary Air Inlet Node Name"
        obj.primary_air_inlet_node_name = var_primary_air_inlet_node_name
        # node
        var_primary_air_outlet_node_name = "node|Primary Air Outlet Node Name"
        obj.primary_air_outlet_node_name = var_primary_air_outlet_node_name
        # node
        var_chilled_water_inlet_node_name = "node|Chilled Water Inlet Node Name"
        obj.chilled_water_inlet_node_name = var_chilled_water_inlet_node_name
        # node
        var_chilled_water_outlet_node_name = "node|Chilled Water Outlet Node Name"
        obj.chilled_water_outlet_node_name = var_chilled_water_outlet_node_name
        # node
        var_hot_water_inlet_node_name = "node|Hot Water Inlet Node Name"
        obj.hot_water_inlet_node_name = var_hot_water_inlet_node_name
        # node
        var_hot_water_outlet_node_name = "node|Hot Water Outlet Node Name"
        obj.hot_water_outlet_node_name = var_hot_water_outlet_node_name
        # real
        var_design_primary_air_volume_flow_rate = 0.0
        obj.design_primary_air_volume_flow_rate = var_design_primary_air_volume_flow_rate
        # real
        var_design_chilled_water_volume_flow_rate = 0.0
        obj.design_chilled_water_volume_flow_rate = var_design_chilled_water_volume_flow_rate
        # real
        var_design_hot_water_volume_flow_rate = 0.0
        obj.design_hot_water_volume_flow_rate = var_design_hot_water_volume_flow_rate
        # real
        var_zone_total_beam_length = 0.0001
        obj.zone_total_beam_length = var_zone_total_beam_length
        # real
        var_rated_primary_air_flow_rate_per_beam_length = 0.0001
        obj.rated_primary_air_flow_rate_per_beam_length = var_rated_primary_air_flow_rate_per_beam_length
        # real
        var_beam_rated_cooling_capacity_per_beam_length = 0.0001
        obj.beam_rated_cooling_capacity_per_beam_length = var_beam_rated_cooling_capacity_per_beam_length
        # real
        var_beam_rated_cooling_room_air_chilled_water_temperature_difference = 0.0001
        obj.beam_rated_cooling_room_air_chilled_water_temperature_difference = var_beam_rated_cooling_room_air_chilled_water_temperature_difference
        # real
        var_beam_rated_chilled_water_volume_flow_rate_per_beam_length = 0.0001
        obj.beam_rated_chilled_water_volume_flow_rate_per_beam_length = var_beam_rated_chilled_water_volume_flow_rate_per_beam_length
        # object-list
        var_beam_cooling_capacity_temperature_difference_modification_factor_curve_name = "object-list|Beam Cooling Capacity Temperature Difference Modification Factor Curve Name"
        obj.beam_cooling_capacity_temperature_difference_modification_factor_curve_name = var_beam_cooling_capacity_temperature_difference_modification_factor_curve_name
        # object-list
        var_beam_cooling_capacity_air_flow_modification_factor_curve_name = "object-list|Beam Cooling Capacity Air Flow Modification Factor Curve Name"
        obj.beam_cooling_capacity_air_flow_modification_factor_curve_name = var_beam_cooling_capacity_air_flow_modification_factor_curve_name
        # object-list
        var_beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name = "object-list|Beam Cooling Capacity Chilled Water Flow Modification Factor Curve Name"
        obj.beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name = var_beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name
        # real
        var_beam_rated_heating_capacity_per_beam_length = 0.0001
        obj.beam_rated_heating_capacity_per_beam_length = var_beam_rated_heating_capacity_per_beam_length
        # real
        var_beam_rated_heating_room_air_hot_water_temperature_difference = 0.0001
        obj.beam_rated_heating_room_air_hot_water_temperature_difference = var_beam_rated_heating_room_air_hot_water_temperature_difference
        # real
        var_beam_rated_hot_water_volume_flow_rate_per_beam_length = 0.0001
        obj.beam_rated_hot_water_volume_flow_rate_per_beam_length = var_beam_rated_hot_water_volume_flow_rate_per_beam_length
        # object-list
        var_beam_heating_capacity_temperature_difference_modification_factor_curve_name = "object-list|Beam Heating Capacity Temperature Difference Modification Factor Curve Name"
        obj.beam_heating_capacity_temperature_difference_modification_factor_curve_name = var_beam_heating_capacity_temperature_difference_modification_factor_curve_name
        # object-list
        var_beam_heating_capacity_air_flow_modification_factor_curve_name = "object-list|Beam Heating Capacity Air Flow Modification Factor Curve Name"
        obj.beam_heating_capacity_air_flow_modification_factor_curve_name = var_beam_heating_capacity_air_flow_modification_factor_curve_name
        # object-list
        var_beam_heating_capacity_hot_water_flow_modification_factor_curve_name = "object-list|Beam Heating Capacity Hot Water Flow Modification Factor Curve Name"
        obj.beam_heating_capacity_hot_water_flow_modification_factor_curve_name = var_beam_heating_capacity_hot_water_flow_modification_factor_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].primary_air_availability_schedule_name, var_primary_air_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].cooling_availability_schedule_name, var_cooling_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].heating_availability_schedule_name, var_heating_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].primary_air_inlet_node_name, var_primary_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].primary_air_outlet_node_name, var_primary_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].hot_water_inlet_node_name, var_hot_water_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].hot_water_outlet_node_name, var_hot_water_outlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].design_primary_air_volume_flow_rate, var_design_primary_air_volume_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].design_chilled_water_volume_flow_rate, var_design_chilled_water_volume_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].design_hot_water_volume_flow_rate, var_design_hot_water_volume_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].zone_total_beam_length, var_zone_total_beam_length)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].rated_primary_air_flow_rate_per_beam_length, var_rated_primary_air_flow_rate_per_beam_length)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_rated_cooling_capacity_per_beam_length, var_beam_rated_cooling_capacity_per_beam_length)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_rated_cooling_room_air_chilled_water_temperature_difference, var_beam_rated_cooling_room_air_chilled_water_temperature_difference)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_rated_chilled_water_volume_flow_rate_per_beam_length, var_beam_rated_chilled_water_volume_flow_rate_per_beam_length)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_cooling_capacity_temperature_difference_modification_factor_curve_name, var_beam_cooling_capacity_temperature_difference_modification_factor_curve_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_cooling_capacity_air_flow_modification_factor_curve_name, var_beam_cooling_capacity_air_flow_modification_factor_curve_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name, var_beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_rated_heating_capacity_per_beam_length, var_beam_rated_heating_capacity_per_beam_length)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_rated_heating_room_air_hot_water_temperature_difference, var_beam_rated_heating_room_air_hot_water_temperature_difference)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_rated_hot_water_volume_flow_rate_per_beam_length, var_beam_rated_hot_water_volume_flow_rate_per_beam_length)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_heating_capacity_temperature_difference_modification_factor_curve_name, var_beam_heating_capacity_temperature_difference_modification_factor_curve_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_heating_capacity_air_flow_modification_factor_curve_name, var_beam_heating_capacity_air_flow_modification_factor_curve_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumefourpipebeams[0].beam_heating_capacity_hot_water_flow_modification_factor_curve_name, var_beam_heating_capacity_hot_water_flow_modification_factor_curve_name)