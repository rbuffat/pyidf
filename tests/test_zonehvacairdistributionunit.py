import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_air_loop_terminal_units import ZoneHvacAirDistributionUnit

log = logging.getLogger(__name__)

class TestZoneHvacAirDistributionUnit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacairdistributionunit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacAirDistributionUnit()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_air_distribution_unit_outlet_node_name = "node|Air Distribution Unit Outlet Node Name"
        obj.air_distribution_unit_outlet_node_name = var_air_distribution_unit_outlet_node_name
        # alpha
        var_air_terminal_object_type = "AirTerminal:DualDuct:ConstantVolume"
        obj.air_terminal_object_type = var_air_terminal_object_type
        # alpha
        var_air_terminal_name = "Air Terminal Name"
        obj.air_terminal_name = var_air_terminal_name
        # real
        var_nominal_upstream_leakage_fraction = 0.15
        obj.nominal_upstream_leakage_fraction = var_nominal_upstream_leakage_fraction
        # real
        var_constant_downstream_leakage_fraction = 0.15
        obj.constant_downstream_leakage_fraction = var_constant_downstream_leakage_fraction

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacairdistributionunits[0].name, var_name)
        self.assertEqual(idf2.zonehvacairdistributionunits[0].air_distribution_unit_outlet_node_name, var_air_distribution_unit_outlet_node_name)
        self.assertEqual(idf2.zonehvacairdistributionunits[0].air_terminal_object_type, var_air_terminal_object_type)
        self.assertEqual(idf2.zonehvacairdistributionunits[0].air_terminal_name, var_air_terminal_name)
        self.assertAlmostEqual(idf2.zonehvacairdistributionunits[0].nominal_upstream_leakage_fraction, var_nominal_upstream_leakage_fraction)
        self.assertAlmostEqual(idf2.zonehvacairdistributionunits[0].constant_downstream_leakage_fraction, var_constant_downstream_leakage_fraction)