import os
import tempfile
import unittest
import pyidf
from pyidf.zone_airflow import ZoneAirBalanceOutdoorAir
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneAirBalanceOutdoorAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneairbalanceoutdoorair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneAirBalanceOutdoorAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # alpha
        var_air_balance_method = "Quadrature"
        obj.air_balance_method = var_air_balance_method
        # real
        var_induced_outdoor_air_due_to_unbalanced_duct_leakage = 0.0
        obj.induced_outdoor_air_due_to_unbalanced_duct_leakage = var_induced_outdoor_air_due_to_unbalanced_duct_leakage
        # object-list
        var_induced_outdoor_air_schedule_name = "object-list|Induced Outdoor Air Schedule Name"
        obj.induced_outdoor_air_schedule_name = var_induced_outdoor_air_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneairbalanceoutdoorairs[0].name, var_name)
        self.assertEqual(idf2.zoneairbalanceoutdoorairs[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zoneairbalanceoutdoorairs[0].air_balance_method, var_air_balance_method)
        self.assertAlmostEqual(idf2.zoneairbalanceoutdoorairs[0].induced_outdoor_air_due_to_unbalanced_duct_leakage, var_induced_outdoor_air_due_to_unbalanced_duct_leakage)
        self.assertEqual(idf2.zoneairbalanceoutdoorairs[0].induced_outdoor_air_schedule_name, var_induced_outdoor_air_schedule_name)