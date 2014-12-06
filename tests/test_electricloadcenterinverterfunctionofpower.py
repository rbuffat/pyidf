import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import ElectricLoadCenterInverterFunctionOfPower

log = logging.getLogger(__name__)

class TestElectricLoadCenterInverterFunctionOfPower(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcenterinverterfunctionofpower(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterInverterFunctionOfPower()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_radiative_fraction = 4.4
        obj.radiative_fraction = var_radiative_fraction
        # alpha
        var_efficiency_function_of_power_curve_name = "Efficiency Function of Power Curve Name"
        obj.efficiency_function_of_power_curve_name = var_efficiency_function_of_power_curve_name
        # real
        var_rated_maximum_continuous_input_power = 6.6
        obj.rated_maximum_continuous_input_power = var_rated_maximum_continuous_input_power
        # real
        var_minimum_efficiency = 0.5
        obj.minimum_efficiency = var_minimum_efficiency
        # real
        var_maximum_efficiency = 0.5
        obj.maximum_efficiency = var_maximum_efficiency
        # real
        var_minimum_power_output = 9.9
        obj.minimum_power_output = var_minimum_power_output
        # real
        var_maximum_power_output = 10.1
        obj.maximum_power_output = var_maximum_power_output
        # real
        var_ancillary_power_consumed_in_standby = 11.11
        obj.ancillary_power_consumed_in_standby = var_ancillary_power_consumed_in_standby

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcenterinverterfunctionofpowers[0].name, var_name)
        self.assertEqual(idf2.electricloadcenterinverterfunctionofpowers[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.electricloadcenterinverterfunctionofpowers[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].radiative_fraction, var_radiative_fraction)
        self.assertEqual(idf2.electricloadcenterinverterfunctionofpowers[0].efficiency_function_of_power_curve_name, var_efficiency_function_of_power_curve_name)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].rated_maximum_continuous_input_power, var_rated_maximum_continuous_input_power)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].minimum_efficiency, var_minimum_efficiency)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].maximum_efficiency, var_maximum_efficiency)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].minimum_power_output, var_minimum_power_output)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].maximum_power_output, var_maximum_power_output)
        self.assertAlmostEqual(idf2.electricloadcenterinverterfunctionofpowers[0].ancillary_power_consumed_in_standby, var_ancillary_power_consumed_in_standby)