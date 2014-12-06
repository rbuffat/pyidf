import os
import tempfile
import unittest
import pyidf
from pyidf.internal_gains import ElectricEquipment
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestElectricEquipment(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricequipment(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricEquipment()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_zone_or_zonelist_name = "object-list|Zone or ZoneList Name"
        obj.zone_or_zonelist_name = var_zone_or_zonelist_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # alpha
        var_design_level_calculation_method = "EquipmentLevel"
        obj.design_level_calculation_method = var_design_level_calculation_method
        # real
        var_design_level = 0.0
        obj.design_level = var_design_level
        # real
        var_watts_per_zone_floor_area = 0.0
        obj.watts_per_zone_floor_area = var_watts_per_zone_floor_area
        # real
        var_watts_per_person = 0.0
        obj.watts_per_person = var_watts_per_person
        # real
        var_fraction_latent = 0.5
        obj.fraction_latent = var_fraction_latent
        # real
        var_fraction_radiant = 0.5
        obj.fraction_radiant = var_fraction_radiant
        # real
        var_fraction_lost = 0.5
        obj.fraction_lost = var_fraction_lost
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricequipments[0].name, var_name)
        self.assertEqual(idf2.electricequipments[0].zone_or_zonelist_name, var_zone_or_zonelist_name)
        self.assertEqual(idf2.electricequipments[0].schedule_name, var_schedule_name)
        self.assertEqual(idf2.electricequipments[0].design_level_calculation_method, var_design_level_calculation_method)
        self.assertAlmostEqual(idf2.electricequipments[0].design_level, var_design_level)
        self.assertAlmostEqual(idf2.electricequipments[0].watts_per_zone_floor_area, var_watts_per_zone_floor_area)
        self.assertAlmostEqual(idf2.electricequipments[0].watts_per_person, var_watts_per_person)
        self.assertAlmostEqual(idf2.electricequipments[0].fraction_latent, var_fraction_latent)
        self.assertAlmostEqual(idf2.electricequipments[0].fraction_radiant, var_fraction_radiant)
        self.assertAlmostEqual(idf2.electricequipments[0].fraction_lost, var_fraction_lost)
        self.assertEqual(idf2.electricequipments[0].enduse_subcategory, var_enduse_subcategory)