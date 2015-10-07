import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneSurface

log = logging.getLogger(__name__)

class TestAirflowNetworkMultiZoneSurface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonesurface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneSurface()
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # object-list
        var_leakage_component_name = "object-list|Leakage Component Name"
        obj.leakage_component_name = var_leakage_component_name
        # object-list
        var_external_node_name = "object-list|External Node Name"
        obj.external_node_name = var_external_node_name
        # real
        var_window_or_door_opening_factor_or_crack_factor = 0.50005
        obj.window_or_door_opening_factor_or_crack_factor = var_window_or_door_opening_factor_or_crack_factor
        # alpha
        var_ventilation_control_mode = "Temperature"
        obj.ventilation_control_mode = var_ventilation_control_mode
        # object-list
        var_ventilation_control_zone_temperature_setpoint_schedule_name = "object-list|Ventilation Control Zone Temperature Setpoint Schedule Name"
        obj.ventilation_control_zone_temperature_setpoint_schedule_name = var_ventilation_control_zone_temperature_setpoint_schedule_name
        # real
        var_minimum_venting_open_factor = 0.5
        obj.minimum_venting_open_factor = var_minimum_venting_open_factor
        # real
        var_indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = 49.99995
        obj.indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor = var_indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor
        # real
        var_indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor = 0.0001
        obj.indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor = var_indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor
        # real
        var_indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = 149999.99995
        obj.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = var_indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor
        # real
        var_indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor = 0.0001
        obj.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor = var_indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor
        # object-list
        var_venting_availability_schedule_name = "object-list|Venting Availability Schedule Name"
        obj.venting_availability_schedule_name = var_venting_availability_schedule_name
        # object-list
        var_occupant_ventilation_control_name = "object-list|Occupant Ventilation Control Name"
        obj.occupant_ventilation_control_name = var_occupant_ventilation_control_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].surface_name, var_surface_name)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].leakage_component_name, var_leakage_component_name)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].external_node_name, var_external_node_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaces[0].window_or_door_opening_factor_or_crack_factor, var_window_or_door_opening_factor_or_crack_factor)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].ventilation_control_mode, var_ventilation_control_mode)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].ventilation_control_zone_temperature_setpoint_schedule_name, var_ventilation_control_zone_temperature_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaces[0].minimum_venting_open_factor, var_minimum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaces[0].indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor, var_indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaces[0].indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor, var_indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaces[0].indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor, var_indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonesurfaces[0].indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor, var_indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].venting_availability_schedule_name, var_venting_availability_schedule_name)
        self.assertEqual(idf2.airflownetworkmultizonesurfaces[0].occupant_ventilation_control_name, var_occupant_ventilation_control_name)