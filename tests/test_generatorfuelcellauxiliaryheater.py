import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import GeneratorFuelCellAuxiliaryHeater

log = logging.getLogger(__name__)

class TestGeneratorFuelCellAuxiliaryHeater(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellauxiliaryheater(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellAuxiliaryHeater()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_excess_air_ratio = 2.2
        obj.excess_air_ratio = var_excess_air_ratio
        # real
        var_ancillary_power_constant_term = 3.3
        obj.ancillary_power_constant_term = var_ancillary_power_constant_term
        # real
        var_ancillary_power_linear_term = 4.4
        obj.ancillary_power_linear_term = var_ancillary_power_linear_term
        # real
        var_skin_loss_ufactor_times_area_value = 5.5
        obj.skin_loss_ufactor_times_area_value = var_skin_loss_ufactor_times_area_value
        # alpha
        var_skin_loss_destination = "SurroundingZone"
        obj.skin_loss_destination = var_skin_loss_destination
        # object-list
        var_zone_name_to_receive_skin_losses = "object-list|Zone Name to Receive Skin Losses"
        obj.zone_name_to_receive_skin_losses = var_zone_name_to_receive_skin_losses
        # alpha
        var_heating_capacity_units = "Watts"
        obj.heating_capacity_units = var_heating_capacity_units
        # real
        var_maximum_heating_capacity_in_watts = 9.9
        obj.maximum_heating_capacity_in_watts = var_maximum_heating_capacity_in_watts
        # real
        var_minimum_heating_capacity_in_watts = 10.1
        obj.minimum_heating_capacity_in_watts = var_minimum_heating_capacity_in_watts
        # real
        var_maximum_heating_capacity_in_kmol_per_second = 11.11
        obj.maximum_heating_capacity_in_kmol_per_second = var_maximum_heating_capacity_in_kmol_per_second
        # real
        var_minimum_heating_capacity_in_kmol_per_second = 12.12
        obj.minimum_heating_capacity_in_kmol_per_second = var_minimum_heating_capacity_in_kmol_per_second

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellauxiliaryheaters[0].name, var_name)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].excess_air_ratio, var_excess_air_ratio)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].ancillary_power_constant_term, var_ancillary_power_constant_term)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].ancillary_power_linear_term, var_ancillary_power_linear_term)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].skin_loss_ufactor_times_area_value, var_skin_loss_ufactor_times_area_value)
        self.assertEqual(idf2.generatorfuelcellauxiliaryheaters[0].skin_loss_destination, var_skin_loss_destination)
        self.assertEqual(idf2.generatorfuelcellauxiliaryheaters[0].zone_name_to_receive_skin_losses, var_zone_name_to_receive_skin_losses)
        self.assertEqual(idf2.generatorfuelcellauxiliaryheaters[0].heating_capacity_units, var_heating_capacity_units)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].maximum_heating_capacity_in_watts, var_maximum_heating_capacity_in_watts)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].minimum_heating_capacity_in_watts, var_minimum_heating_capacity_in_watts)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].maximum_heating_capacity_in_kmol_per_second, var_maximum_heating_capacity_in_kmol_per_second)
        self.assertAlmostEqual(idf2.generatorfuelcellauxiliaryheaters[0].minimum_heating_capacity_in_kmol_per_second, var_minimum_heating_capacity_in_kmol_per_second)