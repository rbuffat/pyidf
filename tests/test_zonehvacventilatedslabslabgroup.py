import os
import tempfile
import unittest
import pyidf
from pyidf.zone_hvac_radiative import ZoneHvacVentilatedSlabSlabGroup
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestZoneHvacVentilatedSlabSlabGroup(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacventilatedslabslabgroup(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacVentilatedSlabSlabGroup()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_zone_1_name = "object-list|Zone 1 Name"
        paras.append(var_zone_1_name)
        var_surface_1_name = "object-list|Surface 1 Name"
        paras.append(var_surface_1_name)
        var_core_diameter_for_surface_1 = 0.0
        paras.append(var_core_diameter_for_surface_1)
        var_core_length_for_surface_1 = 0.0
        paras.append(var_core_length_for_surface_1)
        var_core_numbers_for_surface_1 = 0.0
        paras.append(var_core_numbers_for_surface_1)
        var_slab_inlet_node_name_for_surface_1 = "node|Slab Inlet Node Name for Surface 1"
        paras.append(var_slab_inlet_node_name_for_surface_1)
        var_slab_outlet_node_name_for_surface_1 = "node|Slab Outlet Node Name for Surface 1"
        paras.append(var_slab_outlet_node_name_for_surface_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacventilatedslabslabgroups[0].name, var_name)
        index = obj.extensible_field_index("Zone 1 Name")
        self.assertEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_zone_1_name)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_surface_1_name)
        index = obj.extensible_field_index("Core Diameter for Surface 1")
        self.assertAlmostEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_core_diameter_for_surface_1)
        index = obj.extensible_field_index("Core Length for Surface 1")
        self.assertAlmostEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_core_length_for_surface_1)
        index = obj.extensible_field_index("Core Numbers for Surface 1")
        self.assertAlmostEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_core_numbers_for_surface_1)
        index = obj.extensible_field_index("Slab Inlet Node Name for Surface 1")
        self.assertEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_slab_inlet_node_name_for_surface_1)
        index = obj.extensible_field_index("Slab Outlet Node Name for Surface 1")
        self.assertEqual(idf2.zonehvacventilatedslabslabgroups[0].extensibles[0][index], var_slab_outlet_node_name_for_surface_1)