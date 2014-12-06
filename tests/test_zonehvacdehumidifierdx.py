import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_forced_air_units import ZoneHvacDehumidifierDx

log = logging.getLogger(__name__)

class TestZoneHvacDehumidifierDx(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvacdehumidifierdx(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacDehumidifierDx()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # real
        var_rated_water_removal = 0.0001
        obj.rated_water_removal = var_rated_water_removal
        # real
        var_rated_energy_factor = 0.0001
        obj.rated_energy_factor = var_rated_energy_factor
        # real
        var_rated_air_flow_rate = 0.0001
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # object-list
        var_water_removal_curve_name = "object-list|Water Removal Curve Name"
        obj.water_removal_curve_name = var_water_removal_curve_name
        # object-list
        var_energy_factor_curve_name = "object-list|Energy Factor Curve Name"
        obj.energy_factor_curve_name = var_energy_factor_curve_name
        # object-list
        var_part_load_fraction_correlation_curve_name = "object-list|Part Load Fraction Correlation Curve Name"
        obj.part_load_fraction_correlation_curve_name = var_part_load_fraction_correlation_curve_name
        # real
        var_minimum_drybulb_temperature_for_dehumidifier_operation = 11.11
        obj.minimum_drybulb_temperature_for_dehumidifier_operation = var_minimum_drybulb_temperature_for_dehumidifier_operation
        # real
        var_maximum_drybulb_temperature_for_dehumidifier_operation = 12.12
        obj.maximum_drybulb_temperature_for_dehumidifier_operation = var_maximum_drybulb_temperature_for_dehumidifier_operation
        # real
        var_offcycle_parasitic_electric_load = 0.0
        obj.offcycle_parasitic_electric_load = var_offcycle_parasitic_electric_load
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].name, var_name)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.zonehvacdehumidifierdxs[0].rated_water_removal, var_rated_water_removal)
        self.assertAlmostEqual(idf2.zonehvacdehumidifierdxs[0].rated_energy_factor, var_rated_energy_factor)
        self.assertAlmostEqual(idf2.zonehvacdehumidifierdxs[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].water_removal_curve_name, var_water_removal_curve_name)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].energy_factor_curve_name, var_energy_factor_curve_name)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].part_load_fraction_correlation_curve_name, var_part_load_fraction_correlation_curve_name)
        self.assertAlmostEqual(idf2.zonehvacdehumidifierdxs[0].minimum_drybulb_temperature_for_dehumidifier_operation, var_minimum_drybulb_temperature_for_dehumidifier_operation)
        self.assertAlmostEqual(idf2.zonehvacdehumidifierdxs[0].maximum_drybulb_temperature_for_dehumidifier_operation, var_maximum_drybulb_temperature_for_dehumidifier_operation)
        self.assertAlmostEqual(idf2.zonehvacdehumidifierdxs[0].offcycle_parasitic_electric_load, var_offcycle_parasitic_electric_load)
        self.assertEqual(idf2.zonehvacdehumidifierdxs[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)