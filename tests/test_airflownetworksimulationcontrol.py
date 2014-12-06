import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkSimulationControl

log = logging.getLogger(__name__)

class TestAirflowNetworkSimulationControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworksimulationcontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkSimulationControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_airflownetwork_control = "MultizoneWithDistribution"
        obj.airflownetwork_control = var_airflownetwork_control
        # alpha
        var_wind_pressure_coefficient_type = "Input"
        obj.wind_pressure_coefficient_type = var_wind_pressure_coefficient_type
        # object-list
        var_airflownetwork_wind_pressure_coefficient_array_name = "object-list|AirflowNetwork Wind Pressure Coefficient Array Name"
        obj.airflownetwork_wind_pressure_coefficient_array_name = var_airflownetwork_wind_pressure_coefficient_array_name
        # alpha
        var_height_selection_for_local_wind_pressure_calculation = "ExternalNode"
        obj.height_selection_for_local_wind_pressure_calculation = var_height_selection_for_local_wind_pressure_calculation
        # alpha
        var_building_type = "LowRise"
        obj.building_type = var_building_type
        # integer
        var_maximum_number_of_iterations = 15005
        obj.maximum_number_of_iterations = var_maximum_number_of_iterations
        # alpha
        var_initialization_type = "LinearInitializationMethod"
        obj.initialization_type = var_initialization_type
        # real
        var_relative_airflow_convergence_tolerance = 0.0001
        obj.relative_airflow_convergence_tolerance = var_relative_airflow_convergence_tolerance
        # real
        var_absolute_airflow_convergence_tolerance = 0.0001
        obj.absolute_airflow_convergence_tolerance = var_absolute_airflow_convergence_tolerance
        # real
        var_convergence_acceleration_limit = 0.0
        obj.convergence_acceleration_limit = var_convergence_acceleration_limit
        # real
        var_azimuth_angle_of_long_axis_of_building = 90.0
        obj.azimuth_angle_of_long_axis_of_building = var_azimuth_angle_of_long_axis_of_building
        # real
        var_ratio_of_building_width_along_short_axis_to_width_along_long_axis = 0.50005
        obj.ratio_of_building_width_along_short_axis_to_width_along_long_axis = var_ratio_of_building_width_along_short_axis_to_width_along_long_axis
        # alpha
        var_height_dependence_of_external_node_temperature = "Yes"
        obj.height_dependence_of_external_node_temperature = var_height_dependence_of_external_node_temperature

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].name, var_name)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].airflownetwork_control, var_airflownetwork_control)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].wind_pressure_coefficient_type, var_wind_pressure_coefficient_type)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].airflownetwork_wind_pressure_coefficient_array_name, var_airflownetwork_wind_pressure_coefficient_array_name)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].height_selection_for_local_wind_pressure_calculation, var_height_selection_for_local_wind_pressure_calculation)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].building_type, var_building_type)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].maximum_number_of_iterations, var_maximum_number_of_iterations)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].initialization_type, var_initialization_type)
        self.assertAlmostEqual(idf2.airflownetworksimulationcontrols[0].relative_airflow_convergence_tolerance, var_relative_airflow_convergence_tolerance)
        self.assertAlmostEqual(idf2.airflownetworksimulationcontrols[0].absolute_airflow_convergence_tolerance, var_absolute_airflow_convergence_tolerance)
        self.assertAlmostEqual(idf2.airflownetworksimulationcontrols[0].convergence_acceleration_limit, var_convergence_acceleration_limit)
        self.assertAlmostEqual(idf2.airflownetworksimulationcontrols[0].azimuth_angle_of_long_axis_of_building, var_azimuth_angle_of_long_axis_of_building)
        self.assertAlmostEqual(idf2.airflownetworksimulationcontrols[0].ratio_of_building_width_along_short_axis_to_width_along_long_axis, var_ratio_of_building_width_along_short_axis_to_width_along_long_axis)
        self.assertEqual(idf2.airflownetworksimulationcontrols[0].height_dependence_of_external_node_temperature, var_height_dependence_of_external_node_temperature)