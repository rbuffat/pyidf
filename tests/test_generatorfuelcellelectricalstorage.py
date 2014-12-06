import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.electric_load_center import GeneratorFuelCellElectricalStorage

log = logging.getLogger(__name__)

class TestGeneratorFuelCellElectricalStorage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_generatorfuelcellelectricalstorage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GeneratorFuelCellElectricalStorage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_choice_of_model = "SimpleEfficiencyWithConstraints"
        obj.choice_of_model = var_choice_of_model
        # real
        var_nominal_charging_energetic_efficiency = 0.5
        obj.nominal_charging_energetic_efficiency = var_nominal_charging_energetic_efficiency
        # real
        var_nominal_discharging_energetic_efficiency = 0.5
        obj.nominal_discharging_energetic_efficiency = var_nominal_discharging_energetic_efficiency
        # real
        var_simple_maximum_capacity = 5.5
        obj.simple_maximum_capacity = var_simple_maximum_capacity
        # real
        var_simple_maximum_power_draw = 6.6
        obj.simple_maximum_power_draw = var_simple_maximum_power_draw
        # real
        var_simple_maximum_power_store = 7.7
        obj.simple_maximum_power_store = var_simple_maximum_power_store
        # real
        var_initial_charge_state = 8.8
        obj.initial_charge_state = var_initial_charge_state

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.generatorfuelcellelectricalstorages[0].name, var_name)
        self.assertEqual(idf2.generatorfuelcellelectricalstorages[0].choice_of_model, var_choice_of_model)
        self.assertAlmostEqual(idf2.generatorfuelcellelectricalstorages[0].nominal_charging_energetic_efficiency, var_nominal_charging_energetic_efficiency)
        self.assertAlmostEqual(idf2.generatorfuelcellelectricalstorages[0].nominal_discharging_energetic_efficiency, var_nominal_discharging_energetic_efficiency)
        self.assertAlmostEqual(idf2.generatorfuelcellelectricalstorages[0].simple_maximum_capacity, var_simple_maximum_capacity)
        self.assertAlmostEqual(idf2.generatorfuelcellelectricalstorages[0].simple_maximum_power_draw, var_simple_maximum_power_draw)
        self.assertAlmostEqual(idf2.generatorfuelcellelectricalstorages[0].simple_maximum_power_store, var_simple_maximum_power_store)
        self.assertAlmostEqual(idf2.generatorfuelcellelectricalstorages[0].initial_charge_state, var_initial_charge_state)