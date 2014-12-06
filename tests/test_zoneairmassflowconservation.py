import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import ZoneAirMassFlowConservation
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneAirMassFlowConservation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zoneairmassflowconservation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneAirMassFlowConservation()
        # alpha
        var_adjust_zone_mixing_for_zone_air_mass_flow_balance = "Yes"
        obj.adjust_zone_mixing_for_zone_air_mass_flow_balance = var_adjust_zone_mixing_for_zone_air_mass_flow_balance
        # alpha
        var_source_zone_infiltration_treatment = "AddInfiltrationFlow"
        obj.source_zone_infiltration_treatment = var_source_zone_infiltration_treatment

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneairmassflowconservations[0].adjust_zone_mixing_for_zone_air_mass_flow_balance, var_adjust_zone_mixing_for_zone_air_mass_flow_balance)
        self.assertEqual(idf2.zoneairmassflowconservations[0].source_zone_infiltration_treatment, var_source_zone_infiltration_treatment)