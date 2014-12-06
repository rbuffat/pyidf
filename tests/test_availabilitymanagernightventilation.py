import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerNightVentilation

log = logging.getLogger(__name__)

class TestAvailabilityManagerNightVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagernightventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerNightVentilation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_applicability_schedule_name = "object-list|Applicability Schedule Name"
        obj.applicability_schedule_name = var_applicability_schedule_name
        # object-list
        var_fan_schedule_name = "object-list|Fan Schedule Name"
        obj.fan_schedule_name = var_fan_schedule_name
        # object-list
        var_ventilation_temperature_schedule_name = "object-list|Ventilation Temperature Schedule Name"
        obj.ventilation_temperature_schedule_name = var_ventilation_temperature_schedule_name
        # real
        var_ventilation_temperature_difference = 5.5
        obj.ventilation_temperature_difference = var_ventilation_temperature_difference
        # real
        var_ventilation_temperature_low_limit = 6.6
        obj.ventilation_temperature_low_limit = var_ventilation_temperature_low_limit
        # real
        var_night_venting_flow_fraction = 0.0
        obj.night_venting_flow_fraction = var_night_venting_flow_fraction
        # object-list
        var_control_zone_name = "object-list|Control Zone Name"
        obj.control_zone_name = var_control_zone_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagernightventilations[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagernightventilations[0].applicability_schedule_name, var_applicability_schedule_name)
        self.assertEqual(idf2.availabilitymanagernightventilations[0].fan_schedule_name, var_fan_schedule_name)
        self.assertEqual(idf2.availabilitymanagernightventilations[0].ventilation_temperature_schedule_name, var_ventilation_temperature_schedule_name)
        self.assertAlmostEqual(idf2.availabilitymanagernightventilations[0].ventilation_temperature_difference, var_ventilation_temperature_difference)
        self.assertAlmostEqual(idf2.availabilitymanagernightventilations[0].ventilation_temperature_low_limit, var_ventilation_temperature_low_limit)
        self.assertAlmostEqual(idf2.availabilitymanagernightventilations[0].night_venting_flow_fraction, var_night_venting_flow_fraction)
        self.assertEqual(idf2.availabilitymanagernightventilations[0].control_zone_name, var_control_zone_name)