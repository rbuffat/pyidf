import os
import tempfile
import unittest
import pyidf
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferSlabBldgProps
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatTransferSlabBldgProps(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransferslabbldgprops(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferSlabBldgProps()
        # real
        var_iyrs_number_of_years_to_iterate = 1.0
        obj.iyrs_number_of_years_to_iterate = var_iyrs_number_of_years_to_iterate
        # real
        var_shape_slab_shape = 0.0
        obj.shape_slab_shape = var_shape_slab_shape
        # real
        var_hbldg_building_height = 0.0
        obj.hbldg_building_height = var_hbldg_building_height
        # real
        var_tin1_january_indoor_average_temperature_setpoint = 4.4
        obj.tin1_january_indoor_average_temperature_setpoint = var_tin1_january_indoor_average_temperature_setpoint
        # real
        var_tin2_february_indoor_average_temperature_setpoint = 5.5
        obj.tin2_february_indoor_average_temperature_setpoint = var_tin2_february_indoor_average_temperature_setpoint
        # real
        var_tin3_march_indoor_average_temperature_setpoint = 6.6
        obj.tin3_march_indoor_average_temperature_setpoint = var_tin3_march_indoor_average_temperature_setpoint
        # real
        var_tin4_april_indoor_average_temperature_setpoint = 7.7
        obj.tin4_april_indoor_average_temperature_setpoint = var_tin4_april_indoor_average_temperature_setpoint
        # real
        var_tin5_may_indoor_average_temperature_setpoint = 8.8
        obj.tin5_may_indoor_average_temperature_setpoint = var_tin5_may_indoor_average_temperature_setpoint
        # real
        var_tin6_june_indoor_average_temperature_setpoint = 9.9
        obj.tin6_june_indoor_average_temperature_setpoint = var_tin6_june_indoor_average_temperature_setpoint
        # real
        var_tin7_july_indoor_average_temperature_setpoint = 10.1
        obj.tin7_july_indoor_average_temperature_setpoint = var_tin7_july_indoor_average_temperature_setpoint
        # real
        var_tin8_august_indoor_average_temperature_setpoint = 11.11
        obj.tin8_august_indoor_average_temperature_setpoint = var_tin8_august_indoor_average_temperature_setpoint
        # real
        var_tin9_september_indoor_average_temperature_setpoint = 12.12
        obj.tin9_september_indoor_average_temperature_setpoint = var_tin9_september_indoor_average_temperature_setpoint
        # real
        var_tin10_october_indoor_average_temperature_setpoint = 13.13
        obj.tin10_october_indoor_average_temperature_setpoint = var_tin10_october_indoor_average_temperature_setpoint
        # real
        var_tin11_november_indoor_average_temperature_setpoint = 14.14
        obj.tin11_november_indoor_average_temperature_setpoint = var_tin11_november_indoor_average_temperature_setpoint
        # real
        var_tin12_december_indoor_average_temperature_setpoint = 15.15
        obj.tin12_december_indoor_average_temperature_setpoint = var_tin12_december_indoor_average_temperature_setpoint
        # real
        var_tinamp_daily_indoor_sine_wave_variation_amplitude = 16.16
        obj.tinamp_daily_indoor_sine_wave_variation_amplitude = var_tinamp_daily_indoor_sine_wave_variation_amplitude
        # real
        var_convtol_convergence_tolerance = 17.17
        obj.convtol_convergence_tolerance = var_convtol_convergence_tolerance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].iyrs_number_of_years_to_iterate, var_iyrs_number_of_years_to_iterate)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].shape_slab_shape, var_shape_slab_shape)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].hbldg_building_height, var_hbldg_building_height)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin1_january_indoor_average_temperature_setpoint, var_tin1_january_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin2_february_indoor_average_temperature_setpoint, var_tin2_february_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin3_march_indoor_average_temperature_setpoint, var_tin3_march_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin4_april_indoor_average_temperature_setpoint, var_tin4_april_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin5_may_indoor_average_temperature_setpoint, var_tin5_may_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin6_june_indoor_average_temperature_setpoint, var_tin6_june_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin7_july_indoor_average_temperature_setpoint, var_tin7_july_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin8_august_indoor_average_temperature_setpoint, var_tin8_august_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin9_september_indoor_average_temperature_setpoint, var_tin9_september_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin10_october_indoor_average_temperature_setpoint, var_tin10_october_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin11_november_indoor_average_temperature_setpoint, var_tin11_november_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tin12_december_indoor_average_temperature_setpoint, var_tin12_december_indoor_average_temperature_setpoint)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].tinamp_daily_indoor_sine_wave_variation_amplitude, var_tinamp_daily_indoor_sine_wave_variation_amplitude)
        self.assertAlmostEqual(idf2.groundheattransferslabbldgpropss[0].convtol_convergence_tolerance, var_convtol_convergence_tolerance)