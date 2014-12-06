import os
import tempfile
import unittest
import pyidf
from pyidf.zone_airflow import ZoneEarthtube
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneEarthtube(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneearthtube(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneEarthtube()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_design_flow_rate = 0.0
        obj.design_flow_rate = var_design_flow_rate
        # real
        var_minimum_zone_temperature_when_cooling = 0.0
        obj.minimum_zone_temperature_when_cooling = var_minimum_zone_temperature_when_cooling
        # real
        var_maximum_zone_temperature_when_heating = 0.0
        obj.maximum_zone_temperature_when_heating = var_maximum_zone_temperature_when_heating
        # real
        var_delta_temperature = 0.0
        obj.delta_temperature = var_delta_temperature
        # alpha
        var_earthtube_type = "Natural"
        obj.earthtube_type = var_earthtube_type
        # real
        var_fan_pressure_rise = 0.0
        obj.fan_pressure_rise = var_fan_pressure_rise
        # real
        var_fan_total_efficiency = 0.0001
        obj.fan_total_efficiency = var_fan_total_efficiency
        # real
        var_pipe_radius = 0.0001
        obj.pipe_radius = var_pipe_radius
        # real
        var_pipe_thickness = 0.0001
        obj.pipe_thickness = var_pipe_thickness
        # real
        var_pipe_length = 0.0001
        obj.pipe_length = var_pipe_length
        # real
        var_pipe_thermal_conductivity = 0.0001
        obj.pipe_thermal_conductivity = var_pipe_thermal_conductivity
        # real
        var_pipe_depth_under_ground_surface = 0.0001
        obj.pipe_depth_under_ground_surface = var_pipe_depth_under_ground_surface
        # alpha
        var_soil_condition = "HeavyAndSaturated"
        obj.soil_condition = var_soil_condition
        # real
        var_average_soil_surface_temperature = 16.16
        obj.average_soil_surface_temperature = var_average_soil_surface_temperature
        # real
        var_amplitude_of_soil_surface_temperature = 0.0
        obj.amplitude_of_soil_surface_temperature = var_amplitude_of_soil_surface_temperature
        # real
        var_phase_constant_of_soil_surface_temperature = 0.0
        obj.phase_constant_of_soil_surface_temperature = var_phase_constant_of_soil_surface_temperature
        # real
        var_constant_term_flow_coefficient = 19.19
        obj.constant_term_flow_coefficient = var_constant_term_flow_coefficient
        # real
        var_temperature_term_flow_coefficient = 20.2
        obj.temperature_term_flow_coefficient = var_temperature_term_flow_coefficient
        # real
        var_velocity_term_flow_coefficient = 21.21
        obj.velocity_term_flow_coefficient = var_velocity_term_flow_coefficient
        # real
        var_velocity_squared_term_flow_coefficient = 22.22
        obj.velocity_squared_term_flow_coefficient = var_velocity_squared_term_flow_coefficient

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneearthtubes[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zoneearthtubes[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].minimum_zone_temperature_when_cooling, var_minimum_zone_temperature_when_cooling)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].maximum_zone_temperature_when_heating, var_maximum_zone_temperature_when_heating)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].delta_temperature, var_delta_temperature)
        self.assertEqual(idf2.zoneearthtubes[0].earthtube_type, var_earthtube_type)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].fan_pressure_rise, var_fan_pressure_rise)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].fan_total_efficiency, var_fan_total_efficiency)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].pipe_radius, var_pipe_radius)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].pipe_thickness, var_pipe_thickness)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].pipe_length, var_pipe_length)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].pipe_thermal_conductivity, var_pipe_thermal_conductivity)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].pipe_depth_under_ground_surface, var_pipe_depth_under_ground_surface)
        self.assertEqual(idf2.zoneearthtubes[0].soil_condition, var_soil_condition)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].average_soil_surface_temperature, var_average_soil_surface_temperature)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].amplitude_of_soil_surface_temperature, var_amplitude_of_soil_surface_temperature)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].phase_constant_of_soil_surface_temperature, var_phase_constant_of_soil_surface_temperature)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].constant_term_flow_coefficient, var_constant_term_flow_coefficient)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].temperature_term_flow_coefficient, var_temperature_term_flow_coefficient)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].velocity_term_flow_coefficient, var_velocity_term_flow_coefficient)
        self.assertAlmostEqual(idf2.zoneearthtubes[0].velocity_squared_term_flow_coefficient, var_velocity_squared_term_flow_coefficient)