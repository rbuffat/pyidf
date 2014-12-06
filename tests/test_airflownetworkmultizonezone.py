import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneZone

log = logging.getLogger(__name__)

class TestAirflowNetworkMultiZoneZone(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonezone(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneZone()
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
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
        var_indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = 0.0001
        obj.indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor = var_indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor
        # real
        var_indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = 149999.99995
        obj.indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor = var_indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor
        # real
        var_indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = 0.0001
        obj.indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor = var_indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor
        # object-list
        var_venting_availability_schedule_name = "object-list|Venting Availability Schedule Name"
        obj.venting_availability_schedule_name = var_venting_availability_schedule_name
        # alpha
        var_single_sided_wind_pressure_coefficient_algorithm = "Advanced"
        obj.single_sided_wind_pressure_coefficient_algorithm = var_single_sided_wind_pressure_coefficient_algorithm
        # real
        var_facade_width = 0.0
        obj.facade_width = var_facade_width

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonezones[0].zone_name, var_zone_name)
        self.assertEqual(idf2.airflownetworkmultizonezones[0].ventilation_control_mode, var_ventilation_control_mode)
        self.assertEqual(idf2.airflownetworkmultizonezones[0].ventilation_control_zone_temperature_setpoint_schedule_name, var_ventilation_control_zone_temperature_setpoint_schedule_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonezones[0].minimum_venting_open_factor, var_minimum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonezones[0].indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor, var_indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonezones[0].indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor, var_indoor_and_outdoor_temperature_difference_upper_limit_for_minimun_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonezones[0].indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor, var_indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor)
        self.assertAlmostEqual(idf2.airflownetworkmultizonezones[0].indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor, var_indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimun_venting_open_factor)
        self.assertEqual(idf2.airflownetworkmultizonezones[0].venting_availability_schedule_name, var_venting_availability_schedule_name)
        self.assertEqual(idf2.airflownetworkmultizonezones[0].single_sided_wind_pressure_coefficient_algorithm, var_single_sided_wind_pressure_coefficient_algorithm)
        self.assertAlmostEqual(idf2.airflownetworkmultizonezones[0].facade_width, var_facade_width)