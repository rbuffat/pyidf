import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.output_reporting import FuelFactors

log = logging.getLogger(__name__)

class TestFuelFactors(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fuelfactors(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FuelFactors()
        # alpha
        var_existing_fuel_resource_name = "Electricity"
        obj.existing_fuel_resource_name = var_existing_fuel_resource_name
        # alpha
        var_units_of_measure = "Units of Measure"
        obj.units_of_measure = var_units_of_measure
        # real
        var_energy_per_unit_factor = 3.3
        obj.energy_per_unit_factor = var_energy_per_unit_factor
        # real
        var_source_energy_factor = 4.4
        obj.source_energy_factor = var_source_energy_factor
        # object-list
        var_source_energy_schedule_name = "object-list|Source Energy Schedule Name"
        obj.source_energy_schedule_name = var_source_energy_schedule_name
        # real
        var_co2_emission_factor = 6.6
        obj.co2_emission_factor = var_co2_emission_factor
        # object-list
        var_co2_emission_factor_schedule_name = "object-list|CO2 Emission Factor Schedule Name"
        obj.co2_emission_factor_schedule_name = var_co2_emission_factor_schedule_name
        # real
        var_co_emission_factor = 8.8
        obj.co_emission_factor = var_co_emission_factor
        # object-list
        var_co_emission_factor_schedule_name = "object-list|CO Emission Factor Schedule Name"
        obj.co_emission_factor_schedule_name = var_co_emission_factor_schedule_name
        # real
        var_ch4_emission_factor = 10.1
        obj.ch4_emission_factor = var_ch4_emission_factor
        # object-list
        var_ch4_emission_factor_schedule_name = "object-list|CH4 Emission Factor Schedule Name"
        obj.ch4_emission_factor_schedule_name = var_ch4_emission_factor_schedule_name
        # real
        var_nox_emission_factor = 12.12
        obj.nox_emission_factor = var_nox_emission_factor
        # object-list
        var_nox_emission_factor_schedule_name = "object-list|NOx Emission Factor Schedule Name"
        obj.nox_emission_factor_schedule_name = var_nox_emission_factor_schedule_name
        # real
        var_n2o_emission_factor = 14.14
        obj.n2o_emission_factor = var_n2o_emission_factor
        # object-list
        var_n2o_emission_factor_schedule_name = "object-list|N2O Emission Factor Schedule Name"
        obj.n2o_emission_factor_schedule_name = var_n2o_emission_factor_schedule_name
        # real
        var_so2_emission_factor = 16.16
        obj.so2_emission_factor = var_so2_emission_factor
        # object-list
        var_so2_emission_factor_schedule_name = "object-list|SO2 Emission Factor Schedule Name"
        obj.so2_emission_factor_schedule_name = var_so2_emission_factor_schedule_name
        # real
        var_pm_emission_factor = 18.18
        obj.pm_emission_factor = var_pm_emission_factor
        # object-list
        var_pm_emission_factor_schedule_name = "object-list|PM Emission Factor Schedule Name"
        obj.pm_emission_factor_schedule_name = var_pm_emission_factor_schedule_name
        # real
        var_pm10_emission_factor = 20.2
        obj.pm10_emission_factor = var_pm10_emission_factor
        # object-list
        var_pm10_emission_factor_schedule_name = "object-list|PM10 Emission Factor Schedule Name"
        obj.pm10_emission_factor_schedule_name = var_pm10_emission_factor_schedule_name
        # real
        var_pm2_5_emission_factor = 22.22
        obj.pm2_5_emission_factor = var_pm2_5_emission_factor
        # object-list
        var_pm2_5_emission_factor_schedule_name = "object-list|PM2.5 Emission Factor Schedule Name"
        obj.pm2_5_emission_factor_schedule_name = var_pm2_5_emission_factor_schedule_name
        # real
        var_nh3_emission_factor = 24.24
        obj.nh3_emission_factor = var_nh3_emission_factor
        # object-list
        var_nh3_emission_factor_schedule_name = "object-list|NH3 Emission Factor Schedule Name"
        obj.nh3_emission_factor_schedule_name = var_nh3_emission_factor_schedule_name
        # real
        var_nmvoc_emission_factor = 26.26
        obj.nmvoc_emission_factor = var_nmvoc_emission_factor
        # object-list
        var_nmvoc_emission_factor_schedule_name = "object-list|NMVOC Emission Factor Schedule Name"
        obj.nmvoc_emission_factor_schedule_name = var_nmvoc_emission_factor_schedule_name
        # real
        var_hg_emission_factor = 28.28
        obj.hg_emission_factor = var_hg_emission_factor
        # object-list
        var_hg_emission_factor_schedule_name = "object-list|Hg Emission Factor Schedule Name"
        obj.hg_emission_factor_schedule_name = var_hg_emission_factor_schedule_name
        # real
        var_pb_emission_factor = 30.3
        obj.pb_emission_factor = var_pb_emission_factor
        # object-list
        var_pb_emission_factor_schedule_name = "object-list|Pb Emission Factor Schedule Name"
        obj.pb_emission_factor_schedule_name = var_pb_emission_factor_schedule_name
        # real
        var_water_emission_factor = 32.32
        obj.water_emission_factor = var_water_emission_factor
        # object-list
        var_water_emission_factor_schedule_name = "object-list|Water Emission Factor Schedule Name"
        obj.water_emission_factor_schedule_name = var_water_emission_factor_schedule_name
        # real
        var_nuclear_high_level_emission_factor = 34.34
        obj.nuclear_high_level_emission_factor = var_nuclear_high_level_emission_factor
        # object-list
        var_nuclear_high_level_emission_factor_schedule_name = "object-list|Nuclear High Level Emission Factor Schedule Name"
        obj.nuclear_high_level_emission_factor_schedule_name = var_nuclear_high_level_emission_factor_schedule_name
        # real
        var_nuclear_low_level_emission_factor = 36.36
        obj.nuclear_low_level_emission_factor = var_nuclear_low_level_emission_factor
        # object-list
        var_nuclear_low_level_emission_factor_schedule_name = "object-list|Nuclear Low Level Emission Factor Schedule Name"
        obj.nuclear_low_level_emission_factor_schedule_name = var_nuclear_low_level_emission_factor_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fuelfactorss[0].existing_fuel_resource_name, var_existing_fuel_resource_name)
        self.assertEqual(idf2.fuelfactorss[0].units_of_measure, var_units_of_measure)
        self.assertAlmostEqual(idf2.fuelfactorss[0].energy_per_unit_factor, var_energy_per_unit_factor)
        self.assertAlmostEqual(idf2.fuelfactorss[0].source_energy_factor, var_source_energy_factor)
        self.assertEqual(idf2.fuelfactorss[0].source_energy_schedule_name, var_source_energy_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].co2_emission_factor, var_co2_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].co2_emission_factor_schedule_name, var_co2_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].co_emission_factor, var_co_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].co_emission_factor_schedule_name, var_co_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].ch4_emission_factor, var_ch4_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].ch4_emission_factor_schedule_name, var_ch4_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].nox_emission_factor, var_nox_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].nox_emission_factor_schedule_name, var_nox_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].n2o_emission_factor, var_n2o_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].n2o_emission_factor_schedule_name, var_n2o_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].so2_emission_factor, var_so2_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].so2_emission_factor_schedule_name, var_so2_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].pm_emission_factor, var_pm_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].pm_emission_factor_schedule_name, var_pm_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].pm10_emission_factor, var_pm10_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].pm10_emission_factor_schedule_name, var_pm10_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].pm2_5_emission_factor, var_pm2_5_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].pm2_5_emission_factor_schedule_name, var_pm2_5_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].nh3_emission_factor, var_nh3_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].nh3_emission_factor_schedule_name, var_nh3_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].nmvoc_emission_factor, var_nmvoc_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].nmvoc_emission_factor_schedule_name, var_nmvoc_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].hg_emission_factor, var_hg_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].hg_emission_factor_schedule_name, var_hg_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].pb_emission_factor, var_pb_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].pb_emission_factor_schedule_name, var_pb_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].water_emission_factor, var_water_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].water_emission_factor_schedule_name, var_water_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].nuclear_high_level_emission_factor, var_nuclear_high_level_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].nuclear_high_level_emission_factor_schedule_name, var_nuclear_high_level_emission_factor_schedule_name)
        self.assertAlmostEqual(idf2.fuelfactorss[0].nuclear_low_level_emission_factor, var_nuclear_low_level_emission_factor)
        self.assertEqual(idf2.fuelfactorss[0].nuclear_low_level_emission_factor_schedule_name, var_nuclear_low_level_emission_factor_schedule_name)