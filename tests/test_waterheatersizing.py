import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.water_heaters_and_thermal_storage import WaterHeaterSizing

log = logging.getLogger(__name__)

class TestWaterHeaterSizing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_waterheatersizing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WaterHeaterSizing()
        # object-list
        var_waterheater_name = "object-list|WaterHeater Name"
        obj.waterheater_name = var_waterheater_name
        # alpha
        var_design_mode = "PeakDraw"
        obj.design_mode = var_design_mode
        # real
        var_time_storage_can_meet_peak_draw = 0.0
        obj.time_storage_can_meet_peak_draw = var_time_storage_can_meet_peak_draw
        # real
        var_time_for_tank_recovery = 0.0
        obj.time_for_tank_recovery = var_time_for_tank_recovery
        # real
        var_nominal_tank_volume_for_autosizing_plant_connections = 5.5
        obj.nominal_tank_volume_for_autosizing_plant_connections = var_nominal_tank_volume_for_autosizing_plant_connections
        # integer
        var_number_of_bedrooms = 1
        obj.number_of_bedrooms = var_number_of_bedrooms
        # integer
        var_number_of_bathrooms = 1
        obj.number_of_bathrooms = var_number_of_bathrooms
        # real
        var_storage_capacity_per_person = 0.0
        obj.storage_capacity_per_person = var_storage_capacity_per_person
        # real
        var_recovery_capacity_per_person = 0.0
        obj.recovery_capacity_per_person = var_recovery_capacity_per_person
        # real
        var_storage_capacity_per_floor_area = 0.0
        obj.storage_capacity_per_floor_area = var_storage_capacity_per_floor_area
        # real
        var_recovery_capacity_per_floor_area = 0.0
        obj.recovery_capacity_per_floor_area = var_recovery_capacity_per_floor_area
        # real
        var_number_of_units = 12.12
        obj.number_of_units = var_number_of_units
        # real
        var_storage_capacity_per_unit = 0.0
        obj.storage_capacity_per_unit = var_storage_capacity_per_unit
        # real
        var_recovery_capacity_perunit = 0.0
        obj.recovery_capacity_perunit = var_recovery_capacity_perunit
        # real
        var_storage_capacity_per_collector_area = 0.0
        obj.storage_capacity_per_collector_area = var_storage_capacity_per_collector_area
        # real
        var_height_aspect_ratio = 0.0
        obj.height_aspect_ratio = var_height_aspect_ratio

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.waterheatersizings[0].waterheater_name, var_waterheater_name)
        self.assertEqual(idf2.waterheatersizings[0].design_mode, var_design_mode)
        self.assertAlmostEqual(idf2.waterheatersizings[0].time_storage_can_meet_peak_draw, var_time_storage_can_meet_peak_draw)
        self.assertAlmostEqual(idf2.waterheatersizings[0].time_for_tank_recovery, var_time_for_tank_recovery)
        self.assertAlmostEqual(idf2.waterheatersizings[0].nominal_tank_volume_for_autosizing_plant_connections, var_nominal_tank_volume_for_autosizing_plant_connections)
        self.assertEqual(idf2.waterheatersizings[0].number_of_bedrooms, var_number_of_bedrooms)
        self.assertEqual(idf2.waterheatersizings[0].number_of_bathrooms, var_number_of_bathrooms)
        self.assertAlmostEqual(idf2.waterheatersizings[0].storage_capacity_per_person, var_storage_capacity_per_person)
        self.assertAlmostEqual(idf2.waterheatersizings[0].recovery_capacity_per_person, var_recovery_capacity_per_person)
        self.assertAlmostEqual(idf2.waterheatersizings[0].storage_capacity_per_floor_area, var_storage_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.waterheatersizings[0].recovery_capacity_per_floor_area, var_recovery_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.waterheatersizings[0].number_of_units, var_number_of_units)
        self.assertAlmostEqual(idf2.waterheatersizings[0].storage_capacity_per_unit, var_storage_capacity_per_unit)
        self.assertAlmostEqual(idf2.waterheatersizings[0].recovery_capacity_perunit, var_recovery_capacity_perunit)
        self.assertAlmostEqual(idf2.waterheatersizings[0].storage_capacity_per_collector_area, var_storage_capacity_per_collector_area)
        self.assertAlmostEqual(idf2.waterheatersizings[0].height_aspect_ratio, var_height_aspect_ratio)