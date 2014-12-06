import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import ZoneAirContaminantBalance
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneAirContaminantBalance(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneaircontaminantbalance(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneAirContaminantBalance()
        # alpha
        var_carbon_dioxide_concentration = "Yes"
        obj.carbon_dioxide_concentration = var_carbon_dioxide_concentration
        # object-list
        var_outdoor_carbon_dioxide_schedule_name = "object-list|Outdoor Carbon Dioxide Schedule Name"
        obj.outdoor_carbon_dioxide_schedule_name = var_outdoor_carbon_dioxide_schedule_name
        # alpha
        var_generic_contaminant_concentration = "Yes"
        obj.generic_contaminant_concentration = var_generic_contaminant_concentration
        # object-list
        var_outdoor_generic_contaminant_schedule_name = "object-list|Outdoor Generic Contaminant Schedule Name"
        obj.outdoor_generic_contaminant_schedule_name = var_outdoor_generic_contaminant_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneaircontaminantbalances[0].carbon_dioxide_concentration, var_carbon_dioxide_concentration)
        self.assertEqual(idf2.zoneaircontaminantbalances[0].outdoor_carbon_dioxide_schedule_name, var_outdoor_carbon_dioxide_schedule_name)
        self.assertEqual(idf2.zoneaircontaminantbalances[0].generic_contaminant_concentration, var_generic_contaminant_concentration)
        self.assertEqual(idf2.zoneaircontaminantbalances[0].outdoor_generic_contaminant_schedule_name, var_outdoor_generic_contaminant_schedule_name)