import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import ElectricLoadCenterInverterLookUpTable

log = logging.getLogger(__name__)

class TestElectricLoadCenterInverterLookUpTable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcenterinverterlookuptable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterInverterLookUpTable()
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
        var_radiative_fraction = 0.5
        obj.radiative_fraction = var_radiative_fraction
        # real
        var_rated_maximum_continuous_output_power = 5.5
        obj.rated_maximum_continuous_output_power = var_rated_maximum_continuous_output_power
        # real
        var_night_tare_loss_power = 6.6
        obj.night_tare_loss_power = var_night_tare_loss_power
        # real
        var_nominal_voltage_input = 7.7
        obj.nominal_voltage_input = var_nominal_voltage_input
        # real
        var_efficiency_at_10_power_and_nominal_voltage = 0.5
        obj.efficiency_at_10_power_and_nominal_voltage = var_efficiency_at_10_power_and_nominal_voltage
        # real
        var_efficiency_at_20_power_and_nominal_voltage = 0.5
        obj.efficiency_at_20_power_and_nominal_voltage = var_efficiency_at_20_power_and_nominal_voltage
        # real
        var_efficiency_at_30_power_and_nominal_voltage = 0.5
        obj.efficiency_at_30_power_and_nominal_voltage = var_efficiency_at_30_power_and_nominal_voltage
        # real
        var_efficiency_at_50_power_and_nominal_voltage = 0.5
        obj.efficiency_at_50_power_and_nominal_voltage = var_efficiency_at_50_power_and_nominal_voltage
        # real
        var_efficiency_at_75_power_and_nominal_voltage = 0.5
        obj.efficiency_at_75_power_and_nominal_voltage = var_efficiency_at_75_power_and_nominal_voltage
        # real
        var_efficiency_at_100_power_and_nominal_voltage = 0.5
        obj.efficiency_at_100_power_and_nominal_voltage = var_efficiency_at_100_power_and_nominal_voltage

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcenterinverterlookuptables[0].name, var_name)
        self.assertEqual(idf2.electricloadcenterinverterlookuptables[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.electricloadcenterinverterlookuptables[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].radiative_fraction, var_radiative_fraction)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].rated_maximum_continuous_output_power, var_rated_maximum_continuous_output_power)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].night_tare_loss_power, var_night_tare_loss_power)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].nominal_voltage_input, var_nominal_voltage_input)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].efficiency_at_10_power_and_nominal_voltage, var_efficiency_at_10_power_and_nominal_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].efficiency_at_20_power_and_nominal_voltage, var_efficiency_at_20_power_and_nominal_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].efficiency_at_30_power_and_nominal_voltage, var_efficiency_at_30_power_and_nominal_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].efficiency_at_50_power_and_nominal_voltage, var_efficiency_at_50_power_and_nominal_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].efficiency_at_75_power_and_nominal_voltage, var_efficiency_at_75_power_and_nominal_voltage)
        self.assertAlmostEqual(idf2.electricloadcenterinverterlookuptables[0].efficiency_at_100_power_and_nominal_voltage, var_efficiency_at_100_power_and_nominal_voltage)