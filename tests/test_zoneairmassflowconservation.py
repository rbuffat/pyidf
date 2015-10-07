import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import ZoneAirMassFlowConservation

log = logging.getLogger(__name__)

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
        var_infiltration_balancing_method = "AddInfiltrationFlow"
        obj.infiltration_balancing_method = var_infiltration_balancing_method
        # alpha
        var_infiltration_balancing_zones = "MixingSourceZonesOnly"
        obj.infiltration_balancing_zones = var_infiltration_balancing_zones

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zoneairmassflowconservations[0].adjust_zone_mixing_for_zone_air_mass_flow_balance, var_adjust_zone_mixing_for_zone_air_mass_flow_balance)
        self.assertEqual(idf2.zoneairmassflowconservations[0].infiltration_balancing_method, var_infiltration_balancing_method)
        self.assertEqual(idf2.zoneairmassflowconservations[0].infiltration_balancing_zones, var_infiltration_balancing_zones)