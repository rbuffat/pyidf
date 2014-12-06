import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_air_loop_terminal_units import AirTerminalSingleDuctConstantVolumeCooledBeam
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirTerminalSingleDuctConstantVolumeCooledBeam(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airterminalsingleductconstantvolumecooledbeam(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirTerminalSingleDuctConstantVolumeCooledBeam()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_cooled_beam_type = "Active"
        obj.cooled_beam_type = var_cooled_beam_type
        # node
        var_supply_air_inlet_node_name = "node|Supply Air Inlet Node Name"
        obj.supply_air_inlet_node_name = var_supply_air_inlet_node_name
        # node
        var_supply_air_outlet_node_name = "node|Supply Air Outlet Node Name"
        obj.supply_air_outlet_node_name = var_supply_air_outlet_node_name
        # node
        var_chilled_water_inlet_node_name = "node|Chilled Water Inlet Node Name"
        obj.chilled_water_inlet_node_name = var_chilled_water_inlet_node_name
        # node
        var_chilled_water_outlet_node_name = "node|Chilled Water Outlet Node Name"
        obj.chilled_water_outlet_node_name = var_chilled_water_outlet_node_name
        # real
        var_supply_air_volumetric_flow_rate = 0.0
        obj.supply_air_volumetric_flow_rate = var_supply_air_volumetric_flow_rate
        # real
        var_maximum_total_chilled_water_volumetric_flow_rate = 0.0
        obj.maximum_total_chilled_water_volumetric_flow_rate = var_maximum_total_chilled_water_volumetric_flow_rate
        # integer
        var_number_of_beams = 1
        obj.number_of_beams = var_number_of_beams
        # real
        var_beam_length = 0.0001
        obj.beam_length = var_beam_length
        # real
        var_design_inlet_water_temperature = 0.0
        obj.design_inlet_water_temperature = var_design_inlet_water_temperature
        # real
        var_design_outlet_water_temperature = 0.0
        obj.design_outlet_water_temperature = var_design_outlet_water_temperature
        # real
        var_coil_surface_area_per_coil_length = 0.0
        obj.coil_surface_area_per_coil_length = var_coil_surface_area_per_coil_length
        # real
        var_model_parameter_a = 0.0
        obj.model_parameter_a = var_model_parameter_a
        # real
        var_model_parameter_n1 = 0.0
        obj.model_parameter_n1 = var_model_parameter_n1
        # real
        var_model_parameter_n2 = 0.0
        obj.model_parameter_n2 = var_model_parameter_n2
        # real
        var_model_parameter_n3 = 0.0
        obj.model_parameter_n3 = var_model_parameter_n3
        # real
        var_model_parameter_a0 = 0.0
        obj.model_parameter_a0 = var_model_parameter_a0
        # real
        var_model_parameter_k1 = 0.0
        obj.model_parameter_k1 = var_model_parameter_k1
        # real
        var_model_parameter_n = 0.0
        obj.model_parameter_n = var_model_parameter_n
        # real
        var_coefficient_of_induction_kin = 2.0
        obj.coefficient_of_induction_kin = var_coefficient_of_induction_kin
        # real
        var_leaving_pipe_inside_diameter = 0.0001
        obj.leaving_pipe_inside_diameter = var_leaving_pipe_inside_diameter

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].name, var_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].cooled_beam_type, var_cooled_beam_type)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].supply_air_inlet_node_name, var_supply_air_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].supply_air_outlet_node_name, var_supply_air_outlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].chilled_water_inlet_node_name, var_chilled_water_inlet_node_name)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].chilled_water_outlet_node_name, var_chilled_water_outlet_node_name)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].supply_air_volumetric_flow_rate, var_supply_air_volumetric_flow_rate)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].maximum_total_chilled_water_volumetric_flow_rate, var_maximum_total_chilled_water_volumetric_flow_rate)
        self.assertEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].number_of_beams, var_number_of_beams)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].beam_length, var_beam_length)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].design_inlet_water_temperature, var_design_inlet_water_temperature)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].design_outlet_water_temperature, var_design_outlet_water_temperature)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].coil_surface_area_per_coil_length, var_coil_surface_area_per_coil_length)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_a, var_model_parameter_a)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_n1, var_model_parameter_n1)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_n2, var_model_parameter_n2)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_n3, var_model_parameter_n3)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_a0, var_model_parameter_a0)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_k1, var_model_parameter_k1)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].model_parameter_n, var_model_parameter_n)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].coefficient_of_induction_kin, var_coefficient_of_induction_kin)
        self.assertAlmostEqual(idf2.airterminalsingleductconstantvolumecooledbeams[0].leaving_pipe_inside_diameter, var_leaving_pipe_inside_diameter)