import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import GroundHeatExchangerSlinky

log = logging.getLogger(__name__)

class TestGroundHeatExchangerSlinky(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheatexchangerslinky(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatExchangerSlinky()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # real
        var_design_flow_rate = 0.0001
        obj.design_flow_rate = var_design_flow_rate
        # real
        var_soil_thermal_conductivity = 0.0001
        obj.soil_thermal_conductivity = var_soil_thermal_conductivity
        # real
        var_soil_density = 0.0001
        obj.soil_density = var_soil_density
        # real
        var_soil_specific_heat = 0.0001
        obj.soil_specific_heat = var_soil_specific_heat
        # real
        var_pipe_thermal_conductivity = 0.0001
        obj.pipe_thermal_conductivity = var_pipe_thermal_conductivity
        # real
        var_pipe_density = 0.0001
        obj.pipe_density = var_pipe_density
        # real
        var_pipe_specific_heat = 0.0001
        obj.pipe_specific_heat = var_pipe_specific_heat
        # real
        var_pipe_outer_diameter = 0.0001
        obj.pipe_outer_diameter = var_pipe_outer_diameter
        # real
        var_pipe_thickness = 0.0001
        obj.pipe_thickness = var_pipe_thickness
        # alpha
        var_heat_exchanger_configuration = "Vertical"
        obj.heat_exchanger_configuration = var_heat_exchanger_configuration
        # real
        var_coil_diameter = 0.0001
        obj.coil_diameter = var_coil_diameter
        # real
        var_coil_pitch = 0.0001
        obj.coil_pitch = var_coil_pitch
        # real
        var_trench_depth = 0.0001
        obj.trench_depth = var_trench_depth
        # real
        var_trench_length = 0.0001
        obj.trench_length = var_trench_length
        # integer
        var_number_of_trenches = 1
        obj.number_of_trenches = var_number_of_trenches
        # real
        var_horizontal_spacing_between_pipes = 0.0001
        obj.horizontal_spacing_between_pipes = var_horizontal_spacing_between_pipes
        # alpha
        var_undisturbed_ground_temperature_model_type = "Site:GroundTemperature:Undisturbed:FiniteDifference"
        obj.undisturbed_ground_temperature_model_type = var_undisturbed_ground_temperature_model_type
        # object-list
        var_undisturbed_ground_temperature_model_name = "object-list|Undisturbed Ground Temperature Model Name"
        obj.undisturbed_ground_temperature_model_name = var_undisturbed_ground_temperature_model_name
        # real
        var_maximum_length_of_simulation = 22.22
        obj.maximum_length_of_simulation = var_maximum_length_of_simulation

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].name, var_name)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].soil_thermal_conductivity, var_soil_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].soil_density, var_soil_density)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].soil_specific_heat, var_soil_specific_heat)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].pipe_thermal_conductivity, var_pipe_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].pipe_density, var_pipe_density)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].pipe_specific_heat, var_pipe_specific_heat)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].pipe_outer_diameter, var_pipe_outer_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].pipe_thickness, var_pipe_thickness)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].heat_exchanger_configuration, var_heat_exchanger_configuration)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].coil_diameter, var_coil_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].coil_pitch, var_coil_pitch)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].trench_depth, var_trench_depth)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].trench_length, var_trench_length)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].number_of_trenches, var_number_of_trenches)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].horizontal_spacing_between_pipes, var_horizontal_spacing_between_pipes)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].undisturbed_ground_temperature_model_type, var_undisturbed_ground_temperature_model_type)
        self.assertEqual(idf2.groundheatexchangerslinkys[0].undisturbed_ground_temperature_model_name, var_undisturbed_ground_temperature_model_name)
        self.assertAlmostEqual(idf2.groundheatexchangerslinkys[0].maximum_length_of_simulation, var_maximum_length_of_simulation)