import os
import tempfile
import unittest
import pyidf
from pyidf.output_reporting import EnvironmentalImpactFactors
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestEnvironmentalImpactFactors(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_environmentalimpactfactors(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnvironmentalImpactFactors()
        # real
        var_district_heating_efficiency = 0.0001
        obj.district_heating_efficiency = var_district_heating_efficiency
        # real
        var_district_cooling_cop = 0.0001
        obj.district_cooling_cop = var_district_cooling_cop
        # real
        var_steam_conversion_efficiency = 0.0001
        obj.steam_conversion_efficiency = var_steam_conversion_efficiency
        # real
        var_total_carbon_equivalent_emission_factor_from_n2o = 4.4
        obj.total_carbon_equivalent_emission_factor_from_n2o = var_total_carbon_equivalent_emission_factor_from_n2o
        # real
        var_total_carbon_equivalent_emission_factor_from_ch4 = 5.5
        obj.total_carbon_equivalent_emission_factor_from_ch4 = var_total_carbon_equivalent_emission_factor_from_ch4
        # real
        var_total_carbon_equivalent_emission_factor_from_co2 = 6.6
        obj.total_carbon_equivalent_emission_factor_from_co2 = var_total_carbon_equivalent_emission_factor_from_co2

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.environmentalimpactfactorss[0].district_heating_efficiency, var_district_heating_efficiency)
        self.assertAlmostEqual(idf2.environmentalimpactfactorss[0].district_cooling_cop, var_district_cooling_cop)
        self.assertAlmostEqual(idf2.environmentalimpactfactorss[0].steam_conversion_efficiency, var_steam_conversion_efficiency)
        self.assertAlmostEqual(idf2.environmentalimpactfactorss[0].total_carbon_equivalent_emission_factor_from_n2o, var_total_carbon_equivalent_emission_factor_from_n2o)
        self.assertAlmostEqual(idf2.environmentalimpactfactorss[0].total_carbon_equivalent_emission_factor_from_ch4, var_total_carbon_equivalent_emission_factor_from_ch4)
        self.assertAlmostEqual(idf2.environmentalimpactfactorss[0].total_carbon_equivalent_emission_factor_from_co2, var_total_carbon_equivalent_emission_factor_from_co2)