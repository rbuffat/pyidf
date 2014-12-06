import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferBasementComBldg
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferBasementComBldg(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferbasementcombldg(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferBasementComBldg()
        # real
        var_january_average_temperature = 1.1
        obj.january_average_temperature = var_january_average_temperature
        # real
        var_february_average_temperature = 2.2
        obj.february_average_temperature = var_february_average_temperature
        # real
        var_march_average_temperature = 3.3
        obj.march_average_temperature = var_march_average_temperature
        # real
        var_april_average_temperature = 4.4
        obj.april_average_temperature = var_april_average_temperature
        # real
        var_may_average_temperature = 5.5
        obj.may_average_temperature = var_may_average_temperature
        # real
        var_june_average_temperature = 6.6
        obj.june_average_temperature = var_june_average_temperature
        # real
        var_july_average_temperature = 7.7
        obj.july_average_temperature = var_july_average_temperature
        # real
        var_august_average_temperature = 8.8
        obj.august_average_temperature = var_august_average_temperature
        # real
        var_september_average_temperature = 9.9
        obj.september_average_temperature = var_september_average_temperature
        # real
        var_october_average_temperature = 10.1
        obj.october_average_temperature = var_october_average_temperature
        # real
        var_november_average_temperature = 11.11
        obj.november_average_temperature = var_november_average_temperature
        # real
        var_december_average_temperature = 12.12
        obj.december_average_temperature = var_december_average_temperature
        # real
        var_daily_variation_sine_wave_amplitude = 13.13
        obj.daily_variation_sine_wave_amplitude = var_daily_variation_sine_wave_amplitude

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].january_average_temperature, var_january_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].february_average_temperature, var_february_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].march_average_temperature, var_march_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].april_average_temperature, var_april_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].may_average_temperature, var_may_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].june_average_temperature, var_june_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].july_average_temperature, var_july_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].august_average_temperature, var_august_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].september_average_temperature, var_september_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].october_average_temperature, var_october_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].november_average_temperature, var_november_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].december_average_temperature, var_december_average_temperature)
        self.assertAlmostEqual(idf2.groundheattransferbasementcombldgs[0].daily_variation_sine_wave_amplitude, var_daily_variation_sine_wave_amplitude)