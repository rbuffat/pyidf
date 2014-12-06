import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import ElectricLoadCenterInverterSimple

log = logging.getLogger(__name__)

class TestElectricLoadCenterInverterSimple(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcenterinvertersimple(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterInverterSimple()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_radiative_fraction = 0.5
        obj.radiative_fraction = var_radiative_fraction
        # real
        var_inverter_efficiency = 0.5
        obj.inverter_efficiency = var_inverter_efficiency

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcenterinvertersimples[0].name, var_name)
        self.assertEqual(idf2.electricloadcenterinvertersimples[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.electricloadcenterinvertersimples[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.electricloadcenterinvertersimples[0].radiative_fraction, var_radiative_fraction)
        self.assertAlmostEqual(idf2.electricloadcenterinvertersimples[0].inverter_efficiency, var_inverter_efficiency)