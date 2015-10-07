import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import DesignSpecificationZoneHvacSizing

log = logging.getLogger(__name__)

class TestDesignSpecificationZoneHvacSizing(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_designspecificationzonehvacsizing(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DesignSpecificationZoneHvacSizing()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_cooling_supply_air_flow_rate_method = "None"
        obj.cooling_supply_air_flow_rate_method = var_cooling_supply_air_flow_rate_method
        # real
        var_cooling_supply_air_flow_rate = 0.0
        obj.cooling_supply_air_flow_rate = var_cooling_supply_air_flow_rate
        # real
        var_cooling_supply_air_flow_rate_per_floor_area = 0.0
        obj.cooling_supply_air_flow_rate_per_floor_area = var_cooling_supply_air_flow_rate_per_floor_area
        # real
        var_cooling_fraction_of_autosized_cooling_supply_air_flow_rate = 0.0
        obj.cooling_fraction_of_autosized_cooling_supply_air_flow_rate = var_cooling_fraction_of_autosized_cooling_supply_air_flow_rate
        # real
        var_cooling_supply_air_flow_rate_per_unit_cooling_capacity = 0.0
        obj.cooling_supply_air_flow_rate_per_unit_cooling_capacity = var_cooling_supply_air_flow_rate_per_unit_cooling_capacity
        # alpha
        var_no_load_supply_air_flow_rate_method = "None"
        obj.no_load_supply_air_flow_rate_method = var_no_load_supply_air_flow_rate_method
        # real
        var_no_load_supply_air_flow_rate = 0.0
        obj.no_load_supply_air_flow_rate = var_no_load_supply_air_flow_rate
        # real
        var_no_load_supply_air_flow_rate_per_floor_area = 0.0
        obj.no_load_supply_air_flow_rate_per_floor_area = var_no_load_supply_air_flow_rate_per_floor_area
        # real
        var_no_load_fraction_of_cooling_supply_air_flow_rate = 0.0
        obj.no_load_fraction_of_cooling_supply_air_flow_rate = var_no_load_fraction_of_cooling_supply_air_flow_rate
        # real
        var_no_load_fraction_of_heating_supply_air_flow_rate = 0.0
        obj.no_load_fraction_of_heating_supply_air_flow_rate = var_no_load_fraction_of_heating_supply_air_flow_rate
        # alpha
        var_heating_supply_air_flow_rate_method = "None"
        obj.heating_supply_air_flow_rate_method = var_heating_supply_air_flow_rate_method
        # real
        var_heating_supply_air_flow_rate = 0.0
        obj.heating_supply_air_flow_rate = var_heating_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate_per_floor_area = 0.0
        obj.heating_supply_air_flow_rate_per_floor_area = var_heating_supply_air_flow_rate_per_floor_area
        # real
        var_heating_fraction_of_heating_supply_air_flow_rate = 0.0
        obj.heating_fraction_of_heating_supply_air_flow_rate = var_heating_fraction_of_heating_supply_air_flow_rate
        # real
        var_heating_supply_air_flow_rate_per_unit_heating_capacity = 0.0
        obj.heating_supply_air_flow_rate_per_unit_heating_capacity = var_heating_supply_air_flow_rate_per_unit_heating_capacity
        # alpha
        var_cooling_design_capacity_method = "None"
        obj.cooling_design_capacity_method = var_cooling_design_capacity_method
        # real
        var_cooling_design_capacity = 0.0
        obj.cooling_design_capacity = var_cooling_design_capacity
        # real
        var_cooling_design_capacity_per_floor_area = 0.0
        obj.cooling_design_capacity_per_floor_area = var_cooling_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_cooling_design_capacity = 0.0
        obj.fraction_of_autosized_cooling_design_capacity = var_fraction_of_autosized_cooling_design_capacity
        # alpha
        var_heating_design_capacity_method = "None"
        obj.heating_design_capacity_method = var_heating_design_capacity_method
        # real
        var_heating_design_capacity = 0.0
        obj.heating_design_capacity = var_heating_design_capacity
        # real
        var_heating_design_capacity_per_floor_area = 0.0
        obj.heating_design_capacity_per_floor_area = var_heating_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_heating_design_capacity = 0.0
        obj.fraction_of_autosized_heating_design_capacity = var_fraction_of_autosized_heating_design_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.designspecificationzonehvacsizings[0].name, var_name)
        self.assertEqual(idf2.designspecificationzonehvacsizings[0].cooling_supply_air_flow_rate_method, var_cooling_supply_air_flow_rate_method)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].cooling_supply_air_flow_rate, var_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].cooling_supply_air_flow_rate_per_floor_area, var_cooling_supply_air_flow_rate_per_floor_area)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].cooling_fraction_of_autosized_cooling_supply_air_flow_rate, var_cooling_fraction_of_autosized_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].cooling_supply_air_flow_rate_per_unit_cooling_capacity, var_cooling_supply_air_flow_rate_per_unit_cooling_capacity)
        self.assertEqual(idf2.designspecificationzonehvacsizings[0].no_load_supply_air_flow_rate_method, var_no_load_supply_air_flow_rate_method)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].no_load_supply_air_flow_rate, var_no_load_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].no_load_supply_air_flow_rate_per_floor_area, var_no_load_supply_air_flow_rate_per_floor_area)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].no_load_fraction_of_cooling_supply_air_flow_rate, var_no_load_fraction_of_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].no_load_fraction_of_heating_supply_air_flow_rate, var_no_load_fraction_of_heating_supply_air_flow_rate)
        self.assertEqual(idf2.designspecificationzonehvacsizings[0].heating_supply_air_flow_rate_method, var_heating_supply_air_flow_rate_method)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].heating_supply_air_flow_rate, var_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].heating_supply_air_flow_rate_per_floor_area, var_heating_supply_air_flow_rate_per_floor_area)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].heating_fraction_of_heating_supply_air_flow_rate, var_heating_fraction_of_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].heating_supply_air_flow_rate_per_unit_heating_capacity, var_heating_supply_air_flow_rate_per_unit_heating_capacity)
        self.assertEqual(idf2.designspecificationzonehvacsizings[0].cooling_design_capacity_method, var_cooling_design_capacity_method)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].cooling_design_capacity, var_cooling_design_capacity)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].cooling_design_capacity_per_floor_area, var_cooling_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].fraction_of_autosized_cooling_design_capacity, var_fraction_of_autosized_cooling_design_capacity)
        self.assertEqual(idf2.designspecificationzonehvacsizings[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.designspecificationzonehvacsizings[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)