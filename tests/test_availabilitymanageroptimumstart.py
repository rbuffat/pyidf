import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerOptimumStart

log = logging.getLogger(__name__)

class TestAvailabilityManagerOptimumStart(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanageroptimumstart(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerOptimumStart()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_applicability_schedule_name = "object-list|Applicability Schedule Name"
        obj.applicability_schedule_name = var_applicability_schedule_name
        # object-list
        var_fan_schedule_name = "object-list|Fan Schedule Name"
        obj.fan_schedule_name = var_fan_schedule_name
        # alpha
        var_control_type = "StayOff"
        obj.control_type = var_control_type
        # object-list
        var_control_zone_name = "object-list|Control Zone Name"
        obj.control_zone_name = var_control_zone_name
        # object-list
        var_zone_list_name = "object-list|Zone List Name"
        obj.zone_list_name = var_zone_list_name
        # real
        var_maximum_value_for_optimum_start_time = 7.7
        obj.maximum_value_for_optimum_start_time = var_maximum_value_for_optimum_start_time
        # alpha
        var_control_algorithm = "ConstantTemperatureGradient"
        obj.control_algorithm = var_control_algorithm
        # real
        var_constant_temperature_gradient_during_cooling = 9.9
        obj.constant_temperature_gradient_during_cooling = var_constant_temperature_gradient_during_cooling
        # real
        var_constant_temperature_gradient_during_heating = 10.1
        obj.constant_temperature_gradient_during_heating = var_constant_temperature_gradient_during_heating
        # real
        var_initial_temperature_gradient_during_cooling = 11.11
        obj.initial_temperature_gradient_during_cooling = var_initial_temperature_gradient_during_cooling
        # real
        var_initial_temperature_gradient_during_heating = 12.12
        obj.initial_temperature_gradient_during_heating = var_initial_temperature_gradient_during_heating
        # real
        var_constant_start_time = 13.13
        obj.constant_start_time = var_constant_start_time
        # integer
        var_number_of_previous_days = 3
        obj.number_of_previous_days = var_number_of_previous_days

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].name, var_name)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].applicability_schedule_name, var_applicability_schedule_name)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].fan_schedule_name, var_fan_schedule_name)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].control_type, var_control_type)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].control_zone_name, var_control_zone_name)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].zone_list_name, var_zone_list_name)
        self.assertAlmostEqual(idf2.availabilitymanageroptimumstarts[0].maximum_value_for_optimum_start_time, var_maximum_value_for_optimum_start_time)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].control_algorithm, var_control_algorithm)
        self.assertAlmostEqual(idf2.availabilitymanageroptimumstarts[0].constant_temperature_gradient_during_cooling, var_constant_temperature_gradient_during_cooling)
        self.assertAlmostEqual(idf2.availabilitymanageroptimumstarts[0].constant_temperature_gradient_during_heating, var_constant_temperature_gradient_during_heating)
        self.assertAlmostEqual(idf2.availabilitymanageroptimumstarts[0].initial_temperature_gradient_during_cooling, var_initial_temperature_gradient_during_cooling)
        self.assertAlmostEqual(idf2.availabilitymanageroptimumstarts[0].initial_temperature_gradient_during_heating, var_initial_temperature_gradient_during_heating)
        self.assertAlmostEqual(idf2.availabilitymanageroptimumstarts[0].constant_start_time, var_constant_start_time)
        self.assertEqual(idf2.availabilitymanageroptimumstarts[0].number_of_previous_days, var_number_of_previous_days)