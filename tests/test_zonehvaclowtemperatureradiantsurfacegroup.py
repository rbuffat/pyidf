import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_radiative import ZoneHvacLowTemperatureRadiantSurfaceGroup
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacLowTemperatureRadiantSurfaceGroup(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvaclowtemperatureradiantsurfacegroup(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacLowTemperatureRadiantSurfaceGroup()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_surface_1_name = "object-list|Surface 1 Name"
        paras.append(var_surface_1_name)
        var_flow_fraction_for_surface_1 = 0.0
        paras.append(var_flow_fraction_for_surface_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvaclowtemperatureradiantsurfacegroups[0].name, var_name)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.zonehvaclowtemperatureradiantsurfacegroups[0].extensibles[0][index], var_surface_1_name)
        index = obj.extensible_field_index("Flow Fraction for Surface 1")
        self.assertAlmostEqual(idf2.zonehvaclowtemperatureradiantsurfacegroups[0].extensibles[0][index], var_flow_fraction_for_surface_1)