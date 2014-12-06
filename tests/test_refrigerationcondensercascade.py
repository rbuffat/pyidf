import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationCondenserCascade
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationCondenserCascade(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcondensercascade(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCondenserCascade()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_rated_condensing_temperature = 2.2
        obj.rated_condensing_temperature = var_rated_condensing_temperature
        # real
        var_rated_approach_temperature_difference = 0.0001
        obj.rated_approach_temperature_difference = var_rated_approach_temperature_difference
        # real
        var_rated_effective_total_heat_rejection_rate = 0.0001
        obj.rated_effective_total_heat_rejection_rate = var_rated_effective_total_heat_rejection_rate
        # alpha
        var_condensing_temperature_control_type = "Fixed"
        obj.condensing_temperature_control_type = var_condensing_temperature_control_type
        # real
        var_condenser_refrigerant_operating_charge_inventory = 6.6
        obj.condenser_refrigerant_operating_charge_inventory = var_condenser_refrigerant_operating_charge_inventory
        # real
        var_condensate_receiver_refrigerant_inventory = 7.7
        obj.condensate_receiver_refrigerant_inventory = var_condensate_receiver_refrigerant_inventory
        # real
        var_condensate_piping_refrigerant_inventory = 8.8
        obj.condensate_piping_refrigerant_inventory = var_condensate_piping_refrigerant_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcondensercascades[0].name, var_name)
        self.assertAlmostEqual(idf2.refrigerationcondensercascades[0].rated_condensing_temperature, var_rated_condensing_temperature)
        self.assertAlmostEqual(idf2.refrigerationcondensercascades[0].rated_approach_temperature_difference, var_rated_approach_temperature_difference)
        self.assertAlmostEqual(idf2.refrigerationcondensercascades[0].rated_effective_total_heat_rejection_rate, var_rated_effective_total_heat_rejection_rate)
        self.assertEqual(idf2.refrigerationcondensercascades[0].condensing_temperature_control_type, var_condensing_temperature_control_type)
        self.assertAlmostEqual(idf2.refrigerationcondensercascades[0].condenser_refrigerant_operating_charge_inventory, var_condenser_refrigerant_operating_charge_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondensercascades[0].condensate_receiver_refrigerant_inventory, var_condensate_receiver_refrigerant_inventory)
        self.assertAlmostEqual(idf2.refrigerationcondensercascades[0].condensate_piping_refrigerant_inventory, var_condensate_piping_refrigerant_inventory)