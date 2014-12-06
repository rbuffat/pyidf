import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.hvac_design_objects import SizingPlant

log = logging.getLogger(__name__)

class TestSizingPlant(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sizingplant(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SizingPlant()
        # object-list
        var_plant_or_condenser_loop_name = "object-list|Plant or Condenser Loop Name"
        obj.plant_or_condenser_loop_name = var_plant_or_condenser_loop_name
        # alpha
        var_loop_type = "Heating"
        obj.loop_type = var_loop_type
        # real
        var_design_loop_exit_temperature = 3.3
        obj.design_loop_exit_temperature = var_design_loop_exit_temperature
        # real
        var_loop_design_temperature_difference = 0.0001
        obj.loop_design_temperature_difference = var_loop_design_temperature_difference

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sizingplants[0].plant_or_condenser_loop_name, var_plant_or_condenser_loop_name)
        self.assertEqual(idf2.sizingplants[0].loop_type, var_loop_type)
        self.assertAlmostEqual(idf2.sizingplants[0].design_loop_exit_temperature, var_design_loop_exit_temperature)
        self.assertAlmostEqual(idf2.sizingplants[0].loop_design_temperature_difference, var_loop_design_temperature_difference)