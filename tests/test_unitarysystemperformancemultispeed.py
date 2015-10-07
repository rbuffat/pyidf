import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.unitary_equipment import UnitarySystemPerformanceMultispeed

log = logging.getLogger(__name__)

class TestUnitarySystemPerformanceMultispeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_unitarysystemperformancemultispeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UnitarySystemPerformanceMultispeed()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # integer
        var_number_of_speeds_for_heating = 5
        obj.number_of_speeds_for_heating = var_number_of_speeds_for_heating
        # integer
        var_number_of_speeds_for_cooling = 5
        obj.number_of_speeds_for_cooling = var_number_of_speeds_for_cooling
        paras = []
        var_heating_speed_1_supply_air_flow_ratio = 0.0001
        paras.append(var_heating_speed_1_supply_air_flow_ratio)
        var_cooling_speed_1_supply_air_flow_ratio = 0.0001
        paras.append(var_cooling_speed_1_supply_air_flow_ratio)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.unitarysystemperformancemultispeeds[0].name, var_name)
        self.assertEqual(idf2.unitarysystemperformancemultispeeds[0].number_of_speeds_for_heating, var_number_of_speeds_for_heating)
        self.assertEqual(idf2.unitarysystemperformancemultispeeds[0].number_of_speeds_for_cooling, var_number_of_speeds_for_cooling)
        index = obj.extensible_field_index("Heating Speed 1 Supply Air Flow Ratio")
        self.assertAlmostEqual(idf2.unitarysystemperformancemultispeeds[0].extensibles[0][index], var_heating_speed_1_supply_air_flow_ratio)
        index = obj.extensible_field_index("Cooling Speed 1 Supply Air Flow Ratio")
        self.assertAlmostEqual(idf2.unitarysystemperformancemultispeeds[0].extensibles[0][index], var_cooling_speed_1_supply_air_flow_ratio)