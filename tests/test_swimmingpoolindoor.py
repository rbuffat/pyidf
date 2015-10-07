import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.internal_gains import SwimmingPoolIndoor

log = logging.getLogger(__name__)

class TestSwimmingPoolIndoor(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_swimmingpoolindoor(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SwimmingPoolIndoor()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # real
        var_average_depth = 3.3
        obj.average_depth = var_average_depth
        # object-list
        var_activity_factor_schedule_name = "object-list|Activity Factor Schedule Name"
        obj.activity_factor_schedule_name = var_activity_factor_schedule_name
        # object-list
        var_makeup_water_supply_schedule_name = "object-list|Make-up Water Supply Schedule Name"
        obj.makeup_water_supply_schedule_name = var_makeup_water_supply_schedule_name
        # object-list
        var_cover_schedule_name = "object-list|Cover Schedule Name"
        obj.cover_schedule_name = var_cover_schedule_name
        # real
        var_cover_evaporation_factor = 0.5
        obj.cover_evaporation_factor = var_cover_evaporation_factor
        # real
        var_cover_convection_factor = 0.5
        obj.cover_convection_factor = var_cover_convection_factor
        # real
        var_cover_shortwavelength_radiation_factor = 0.5
        obj.cover_shortwavelength_radiation_factor = var_cover_shortwavelength_radiation_factor
        # real
        var_cover_longwavelength_radiation_factor = 0.5
        obj.cover_longwavelength_radiation_factor = var_cover_longwavelength_radiation_factor
        # node
        var_pool_water_inlet_node = "node|Pool Water Inlet Node"
        obj.pool_water_inlet_node = var_pool_water_inlet_node
        # node
        var_pool_water_outlet_node = "node|Pool Water Outlet Node"
        obj.pool_water_outlet_node = var_pool_water_outlet_node
        # real
        var_pool_heating_system_maximum_water_flow_rate = 0.0
        obj.pool_heating_system_maximum_water_flow_rate = var_pool_heating_system_maximum_water_flow_rate
        # real
        var_pool_miscellaneous_equipment_power = 0.0
        obj.pool_miscellaneous_equipment_power = var_pool_miscellaneous_equipment_power
        # object-list
        var_setpoint_temperature_schedule = "object-list|Setpoint Temperature Schedule"
        obj.setpoint_temperature_schedule = var_setpoint_temperature_schedule
        # real
        var_maximum_number_of_people = 0.0
        obj.maximum_number_of_people = var_maximum_number_of_people
        # object-list
        var_people_schedule = "object-list|People Schedule"
        obj.people_schedule = var_people_schedule
        # object-list
        var_people_heat_gain_schedule = "object-list|People Heat Gain Schedule"
        obj.people_heat_gain_schedule = var_people_heat_gain_schedule

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.swimmingpoolindoors[0].name, var_name)
        self.assertEqual(idf2.swimmingpoolindoors[0].surface_name, var_surface_name)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].average_depth, var_average_depth)
        self.assertEqual(idf2.swimmingpoolindoors[0].activity_factor_schedule_name, var_activity_factor_schedule_name)
        self.assertEqual(idf2.swimmingpoolindoors[0].makeup_water_supply_schedule_name, var_makeup_water_supply_schedule_name)
        self.assertEqual(idf2.swimmingpoolindoors[0].cover_schedule_name, var_cover_schedule_name)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].cover_evaporation_factor, var_cover_evaporation_factor)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].cover_convection_factor, var_cover_convection_factor)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].cover_shortwavelength_radiation_factor, var_cover_shortwavelength_radiation_factor)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].cover_longwavelength_radiation_factor, var_cover_longwavelength_radiation_factor)
        self.assertEqual(idf2.swimmingpoolindoors[0].pool_water_inlet_node, var_pool_water_inlet_node)
        self.assertEqual(idf2.swimmingpoolindoors[0].pool_water_outlet_node, var_pool_water_outlet_node)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].pool_heating_system_maximum_water_flow_rate, var_pool_heating_system_maximum_water_flow_rate)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].pool_miscellaneous_equipment_power, var_pool_miscellaneous_equipment_power)
        self.assertEqual(idf2.swimmingpoolindoors[0].setpoint_temperature_schedule, var_setpoint_temperature_schedule)
        self.assertAlmostEqual(idf2.swimmingpoolindoors[0].maximum_number_of_people, var_maximum_number_of_people)
        self.assertEqual(idf2.swimmingpoolindoors[0].people_schedule, var_people_schedule)
        self.assertEqual(idf2.swimmingpoolindoors[0].people_heat_gain_schedule, var_people_heat_gain_schedule)