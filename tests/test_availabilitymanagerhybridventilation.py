import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.system_availability_managers import AvailabilityManagerHybridVentilation

log = logging.getLogger(__name__)

class TestAvailabilityManagerHybridVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagerhybridventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerHybridVentilation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_hvac_air_loop_name = "object-list|HVAC Air Loop Name"
        obj.hvac_air_loop_name = var_hvac_air_loop_name
        # object-list
        var_controlled_zone_name = "object-list|Controlled Zone Name"
        obj.controlled_zone_name = var_controlled_zone_name
        # object-list
        var_ventilation_control_mode_schedule_name = "object-list|Ventilation Control Mode Schedule Name"
        obj.ventilation_control_mode_schedule_name = var_ventilation_control_mode_schedule_name
        # alpha
        var_use_weather_file_rain_indicators = "Yes"
        obj.use_weather_file_rain_indicators = var_use_weather_file_rain_indicators
        # real
        var_maximum_wind_speed = 20.0
        obj.maximum_wind_speed = var_maximum_wind_speed
        # real
        var_minimum_outdoor_temperature = 0.0
        obj.minimum_outdoor_temperature = var_minimum_outdoor_temperature
        # real
        var_maximum_outdoor_temperature = 0.0
        obj.maximum_outdoor_temperature = var_maximum_outdoor_temperature
        # real
        var_minimum_outdoor_enthalpy = 150000.0
        obj.minimum_outdoor_enthalpy = var_minimum_outdoor_enthalpy
        # real
        var_maximum_outdoor_enthalpy = 150000.0
        obj.maximum_outdoor_enthalpy = var_maximum_outdoor_enthalpy
        # real
        var_minimum_outdoor_dewpoint = 0.0
        obj.minimum_outdoor_dewpoint = var_minimum_outdoor_dewpoint
        # real
        var_maximum_outdoor_dewpoint = 0.0
        obj.maximum_outdoor_dewpoint = var_maximum_outdoor_dewpoint
        # object-list
        var_minimum_outdoor_ventilation_air_schedule_name = "object-list|Minimum Outdoor Ventilation Air Schedule Name"
        obj.minimum_outdoor_ventilation_air_schedule_name = var_minimum_outdoor_ventilation_air_schedule_name
        # object-list
        var_opening_factor_function_of_wind_speed_curve_name = "object-list|Opening Factor Function of Wind Speed Curve Name"
        obj.opening_factor_function_of_wind_speed_curve_name = var_opening_factor_function_of_wind_speed_curve_name
        # object-list
        var_airflownetwork_control_type_schedule_name = "object-list|AirflowNetwork Control Type Schedule Name"
        obj.airflownetwork_control_type_schedule_name = var_airflownetwork_control_type_schedule_name
        # object-list
        var_simple_airflow_control_type_schedule_name = "object-list|Simple Airflow Control Type Schedule Name"
        obj.simple_airflow_control_type_schedule_name = var_simple_airflow_control_type_schedule_name
        # object-list
        var_zoneventilation_object_name = "object-list|ZoneVentilation Object Name"
        obj.zoneventilation_object_name = var_zoneventilation_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].name, var_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].hvac_air_loop_name, var_hvac_air_loop_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].controlled_zone_name, var_controlled_zone_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].ventilation_control_mode_schedule_name, var_ventilation_control_mode_schedule_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].use_weather_file_rain_indicators, var_use_weather_file_rain_indicators)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].maximum_wind_speed, var_maximum_wind_speed)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].minimum_outdoor_temperature, var_minimum_outdoor_temperature)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].maximum_outdoor_temperature, var_maximum_outdoor_temperature)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].minimum_outdoor_enthalpy, var_minimum_outdoor_enthalpy)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].maximum_outdoor_enthalpy, var_maximum_outdoor_enthalpy)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].minimum_outdoor_dewpoint, var_minimum_outdoor_dewpoint)
        self.assertAlmostEqual(idf2.availabilitymanagerhybridventilations[0].maximum_outdoor_dewpoint, var_maximum_outdoor_dewpoint)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].minimum_outdoor_ventilation_air_schedule_name, var_minimum_outdoor_ventilation_air_schedule_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].opening_factor_function_of_wind_speed_curve_name, var_opening_factor_function_of_wind_speed_curve_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].airflownetwork_control_type_schedule_name, var_airflownetwork_control_type_schedule_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].simple_airflow_control_type_schedule_name, var_simple_airflow_control_type_schedule_name)
        self.assertEqual(idf2.availabilitymanagerhybridventilations[0].zoneventilation_object_name, var_zoneventilation_object_name)