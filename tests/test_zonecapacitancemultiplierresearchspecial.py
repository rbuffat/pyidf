import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.simulation_parameters import ZoneCapacitanceMultiplierResearchSpecial

log = logging.getLogger(__name__)

class TestZoneCapacitanceMultiplierResearchSpecial(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonecapacitancemultiplierresearchspecial(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneCapacitanceMultiplierResearchSpecial()
        # real
        var_temperature_capacity_multiplier = 0.0001
        obj.temperature_capacity_multiplier = var_temperature_capacity_multiplier
        # real
        var_humidity_capacity_multiplier = 0.0001
        obj.humidity_capacity_multiplier = var_humidity_capacity_multiplier
        # real
        var_carbon_dioxide_capacity_multiplier = 0.0001
        obj.carbon_dioxide_capacity_multiplier = var_carbon_dioxide_capacity_multiplier
        # real
        var_generic_contaminant_capacity_multiplier = 0.0001
        obj.generic_contaminant_capacity_multiplier = var_generic_contaminant_capacity_multiplier

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertAlmostEqual(idf2.zonecapacitancemultiplierresearchspecials[0].temperature_capacity_multiplier, var_temperature_capacity_multiplier)
        self.assertAlmostEqual(idf2.zonecapacitancemultiplierresearchspecials[0].humidity_capacity_multiplier, var_humidity_capacity_multiplier)
        self.assertAlmostEqual(idf2.zonecapacitancemultiplierresearchspecials[0].carbon_dioxide_capacity_multiplier, var_carbon_dioxide_capacity_multiplier)
        self.assertAlmostEqual(idf2.zonecapacitancemultiplierresearchspecials[0].generic_contaminant_capacity_multiplier, var_generic_contaminant_capacity_multiplier)