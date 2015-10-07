import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkOccupantVentilationControl

log = logging.getLogger(__name__)

class TestAirflowNetworkOccupantVentilationControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkoccupantventilationcontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkOccupantVentilationControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_minimum_opening_time = 0.0
        obj.minimum_opening_time = var_minimum_opening_time
        # real
        var_minimum_closing_time = 0.0
        obj.minimum_closing_time = var_minimum_closing_time
        # object-list
        var_thermal_comfort_low_temperature_curve_name = "object-list|Thermal Comfort Low Temperature Curve Name"
        obj.thermal_comfort_low_temperature_curve_name = var_thermal_comfort_low_temperature_curve_name
        # real
        var_thermal_comfort_temperature_boundary_point = 0.0
        obj.thermal_comfort_temperature_boundary_point = var_thermal_comfort_temperature_boundary_point
        # object-list
        var_thermal_comfort_high_temperature_curve_name = "object-list|Thermal Comfort High Temperature Curve Name"
        obj.thermal_comfort_high_temperature_curve_name = var_thermal_comfort_high_temperature_curve_name
        # real
        var_maximum_threshold_for_persons_dissatisfied_ppd = 50.0
        obj.maximum_threshold_for_persons_dissatisfied_ppd = var_maximum_threshold_for_persons_dissatisfied_ppd
        # alpha
        var_occupancy_check = "Yes"
        obj.occupancy_check = var_occupancy_check
        # object-list
        var_opening_probability_schedule_name = "object-list|Opening Probability Schedule Name"
        obj.opening_probability_schedule_name = var_opening_probability_schedule_name
        # object-list
        var_closing_probability_schedule_name = "object-list|Closing Probability Schedule Name"
        obj.closing_probability_schedule_name = var_closing_probability_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkoccupantventilationcontrols[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkoccupantventilationcontrols[0].minimum_opening_time, var_minimum_opening_time)
        self.assertAlmostEqual(idf2.airflownetworkoccupantventilationcontrols[0].minimum_closing_time, var_minimum_closing_time)
        self.assertEqual(idf2.airflownetworkoccupantventilationcontrols[0].thermal_comfort_low_temperature_curve_name, var_thermal_comfort_low_temperature_curve_name)
        self.assertAlmostEqual(idf2.airflownetworkoccupantventilationcontrols[0].thermal_comfort_temperature_boundary_point, var_thermal_comfort_temperature_boundary_point)
        self.assertEqual(idf2.airflownetworkoccupantventilationcontrols[0].thermal_comfort_high_temperature_curve_name, var_thermal_comfort_high_temperature_curve_name)
        self.assertAlmostEqual(idf2.airflownetworkoccupantventilationcontrols[0].maximum_threshold_for_persons_dissatisfied_ppd, var_maximum_threshold_for_persons_dissatisfied_ppd)
        self.assertEqual(idf2.airflownetworkoccupantventilationcontrols[0].occupancy_check, var_occupancy_check)
        self.assertEqual(idf2.airflownetworkoccupantventilationcontrols[0].opening_probability_schedule_name, var_opening_probability_schedule_name)
        self.assertEqual(idf2.airflownetworkoccupantventilationcontrols[0].closing_probability_schedule_name, var_closing_probability_schedule_name)