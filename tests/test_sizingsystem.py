import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import SizingSystem

log = logging.getLogger(__name__)

class TestSizingSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sizingsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SizingSystem()
        # object-list
        var_airloop_name = "object-list|AirLoop Name"
        obj.airloop_name = var_airloop_name
        # alpha
        var_type_of_load_to_size_on = "Sensible"
        obj.type_of_load_to_size_on = var_type_of_load_to_size_on
        # real
        var_design_outdoor_air_flow_rate = 0.0
        obj.design_outdoor_air_flow_rate = var_design_outdoor_air_flow_rate
        # real
        var_minimum_system_air_flow_ratio = 0.5
        obj.minimum_system_air_flow_ratio = var_minimum_system_air_flow_ratio
        # real
        var_preheat_design_temperature = 5.5
        obj.preheat_design_temperature = var_preheat_design_temperature
        # real
        var_preheat_design_humidity_ratio = 6.6
        obj.preheat_design_humidity_ratio = var_preheat_design_humidity_ratio
        # real
        var_precool_design_temperature = 7.7
        obj.precool_design_temperature = var_precool_design_temperature
        # real
        var_precool_design_humidity_ratio = 8.8
        obj.precool_design_humidity_ratio = var_precool_design_humidity_ratio
        # real
        var_central_cooling_design_supply_air_temperature = 9.9
        obj.central_cooling_design_supply_air_temperature = var_central_cooling_design_supply_air_temperature
        # real
        var_central_heating_design_supply_air_temperature = 10.1
        obj.central_heating_design_supply_air_temperature = var_central_heating_design_supply_air_temperature
        # alpha
        var_sizing_option = "Coincident"
        obj.sizing_option = var_sizing_option
        # alpha
        var_a_100_outdoor_air_in_cooling = "Yes"
        obj.a_100_outdoor_air_in_cooling = var_a_100_outdoor_air_in_cooling
        # alpha
        var_a_100_outdoor_air_in_heating = "Yes"
        obj.a_100_outdoor_air_in_heating = var_a_100_outdoor_air_in_heating
        # real
        var_central_cooling_design_supply_air_humidity_ratio = 14.14
        obj.central_cooling_design_supply_air_humidity_ratio = var_central_cooling_design_supply_air_humidity_ratio
        # real
        var_central_heating_design_supply_air_humidity_ratio = 15.15
        obj.central_heating_design_supply_air_humidity_ratio = var_central_heating_design_supply_air_humidity_ratio
        # alpha
        var_cooling_design_air_flow_method = "Flow/System"
        obj.cooling_design_air_flow_method = var_cooling_design_air_flow_method
        # real
        var_cooling_design_air_flow_rate = 0.0
        obj.cooling_design_air_flow_rate = var_cooling_design_air_flow_rate
        # real
        var_supply_air_flow_rate_per_floor_area_during_cooling_operation = 0.0
        obj.supply_air_flow_rate_per_floor_area_during_cooling_operation = var_supply_air_flow_rate_per_floor_area_during_cooling_operation
        # real
        var_fraction_of_autosized_design_cooling_supply_air_flow_rate = 0.0
        obj.fraction_of_autosized_design_cooling_supply_air_flow_rate = var_fraction_of_autosized_design_cooling_supply_air_flow_rate
        # real
        var_design_supply_air_flow_rate_per_unit_cooling_capacity = 0.0
        obj.design_supply_air_flow_rate_per_unit_cooling_capacity = var_design_supply_air_flow_rate_per_unit_cooling_capacity
        # alpha
        var_heating_design_air_flow_method = "Flow/System"
        obj.heating_design_air_flow_method = var_heating_design_air_flow_method
        # real
        var_heating_design_air_flow_rate = 0.0
        obj.heating_design_air_flow_rate = var_heating_design_air_flow_rate
        # real
        var_supply_air_flow_rate_per_floor_area_during_heating_operation = 0.0
        obj.supply_air_flow_rate_per_floor_area_during_heating_operation = var_supply_air_flow_rate_per_floor_area_during_heating_operation
        # real
        var_fraction_of_autosized_design_heating_supply_air_flow_rate = 0.0
        obj.fraction_of_autosized_design_heating_supply_air_flow_rate = var_fraction_of_autosized_design_heating_supply_air_flow_rate
        # real
        var_fraction_of_autosized_design_cooling_supply_air_flow_rate_v3 = 0.0
        obj.fraction_of_autosized_design_cooling_supply_air_flow_rate_v3 = var_fraction_of_autosized_design_cooling_supply_air_flow_rate_v3
        # real
        var_design_supply_air_flow_rate_per_unit_heating_capacity = 0.0
        obj.design_supply_air_flow_rate_per_unit_heating_capacity = var_design_supply_air_flow_rate_per_unit_heating_capacity
        # alpha
        var_system_outdoor_air_method = "ZoneSum"
        obj.system_outdoor_air_method = var_system_outdoor_air_method
        # real
        var_zone_maximum_outdoor_air_fraction = 0.0001
        obj.zone_maximum_outdoor_air_fraction = var_zone_maximum_outdoor_air_fraction
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
        self.assertEqual(idf2.sizingsystems[0].airloop_name, var_airloop_name)
        self.assertEqual(idf2.sizingsystems[0].type_of_load_to_size_on, var_type_of_load_to_size_on)
        self.assertAlmostEqual(idf2.sizingsystems[0].design_outdoor_air_flow_rate, var_design_outdoor_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingsystems[0].minimum_system_air_flow_ratio, var_minimum_system_air_flow_ratio)
        self.assertAlmostEqual(idf2.sizingsystems[0].preheat_design_temperature, var_preheat_design_temperature)
        self.assertAlmostEqual(idf2.sizingsystems[0].preheat_design_humidity_ratio, var_preheat_design_humidity_ratio)
        self.assertAlmostEqual(idf2.sizingsystems[0].precool_design_temperature, var_precool_design_temperature)
        self.assertAlmostEqual(idf2.sizingsystems[0].precool_design_humidity_ratio, var_precool_design_humidity_ratio)
        self.assertAlmostEqual(idf2.sizingsystems[0].central_cooling_design_supply_air_temperature, var_central_cooling_design_supply_air_temperature)
        self.assertAlmostEqual(idf2.sizingsystems[0].central_heating_design_supply_air_temperature, var_central_heating_design_supply_air_temperature)
        self.assertEqual(idf2.sizingsystems[0].sizing_option, var_sizing_option)
        self.assertEqual(idf2.sizingsystems[0].a_100_outdoor_air_in_cooling, var_a_100_outdoor_air_in_cooling)
        self.assertEqual(idf2.sizingsystems[0].a_100_outdoor_air_in_heating, var_a_100_outdoor_air_in_heating)
        self.assertAlmostEqual(idf2.sizingsystems[0].central_cooling_design_supply_air_humidity_ratio, var_central_cooling_design_supply_air_humidity_ratio)
        self.assertAlmostEqual(idf2.sizingsystems[0].central_heating_design_supply_air_humidity_ratio, var_central_heating_design_supply_air_humidity_ratio)
        self.assertEqual(idf2.sizingsystems[0].cooling_design_air_flow_method, var_cooling_design_air_flow_method)
        self.assertAlmostEqual(idf2.sizingsystems[0].cooling_design_air_flow_rate, var_cooling_design_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingsystems[0].supply_air_flow_rate_per_floor_area_during_cooling_operation, var_supply_air_flow_rate_per_floor_area_during_cooling_operation)
        self.assertAlmostEqual(idf2.sizingsystems[0].fraction_of_autosized_design_cooling_supply_air_flow_rate, var_fraction_of_autosized_design_cooling_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingsystems[0].design_supply_air_flow_rate_per_unit_cooling_capacity, var_design_supply_air_flow_rate_per_unit_cooling_capacity)
        self.assertEqual(idf2.sizingsystems[0].heating_design_air_flow_method, var_heating_design_air_flow_method)
        self.assertAlmostEqual(idf2.sizingsystems[0].heating_design_air_flow_rate, var_heating_design_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingsystems[0].supply_air_flow_rate_per_floor_area_during_heating_operation, var_supply_air_flow_rate_per_floor_area_during_heating_operation)
        self.assertAlmostEqual(idf2.sizingsystems[0].fraction_of_autosized_design_heating_supply_air_flow_rate, var_fraction_of_autosized_design_heating_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.sizingsystems[0].fraction_of_autosized_design_cooling_supply_air_flow_rate_v3, var_fraction_of_autosized_design_cooling_supply_air_flow_rate_v3)
        self.assertAlmostEqual(idf2.sizingsystems[0].design_supply_air_flow_rate_per_unit_heating_capacity, var_design_supply_air_flow_rate_per_unit_heating_capacity)
        self.assertEqual(idf2.sizingsystems[0].system_outdoor_air_method, var_system_outdoor_air_method)
        self.assertAlmostEqual(idf2.sizingsystems[0].zone_maximum_outdoor_air_fraction, var_zone_maximum_outdoor_air_fraction)
        self.assertEqual(idf2.sizingsystems[0].cooling_design_capacity_method, var_cooling_design_capacity_method)
        self.assertAlmostEqual(idf2.sizingsystems[0].cooling_design_capacity, var_cooling_design_capacity)
        self.assertAlmostEqual(idf2.sizingsystems[0].cooling_design_capacity_per_floor_area, var_cooling_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.sizingsystems[0].fraction_of_autosized_cooling_design_capacity, var_fraction_of_autosized_cooling_design_capacity)
        self.assertEqual(idf2.sizingsystems[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.sizingsystems[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.sizingsystems[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.sizingsystems[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)