import os
import tempfile
import unittest
import pyidf
from pyidf.unitary_equipment import UnitarySystemPerformanceHeatPumpMultispeed
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestUnitarySystemPerformanceHeatPumpMultispeed(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_unitarysystemperformanceheatpumpmultispeed(self):

        pyidf.validation_level = ValidationLevel.error

        obj = UnitarySystemPerformanceHeatPumpMultispeed()
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
        var_speed_1_supply_air_flow_ratio_during_heating_operation = 0.0001
        paras.append(var_speed_1_supply_air_flow_ratio_during_heating_operation)
        var_speed_1_supply_air_flow_ratio_during_cooling_operation = 0.0001
        paras.append(var_speed_1_supply_air_flow_ratio_during_cooling_operation)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.unitarysystemperformanceheatpumpmultispeeds[0].name, var_name)
        self.assertEqual(idf2.unitarysystemperformanceheatpumpmultispeeds[0].number_of_speeds_for_heating, var_number_of_speeds_for_heating)
        self.assertEqual(idf2.unitarysystemperformanceheatpumpmultispeeds[0].number_of_speeds_for_cooling, var_number_of_speeds_for_cooling)
        index = obj.extensible_field_index("Speed 1 Supply Air Flow Ratio During Heating Operation")
        self.assertAlmostEqual(idf2.unitarysystemperformanceheatpumpmultispeeds[0].extensibles[0][index], var_speed_1_supply_air_flow_ratio_during_heating_operation)
        index = obj.extensible_field_index("Speed 1 Supply Air Flow Ratio During Cooling Operation")
        self.assertAlmostEqual(idf2.unitarysystemperformanceheatpumpmultispeeds[0].extensibles[0][index], var_speed_1_supply_air_flow_ratio_during_cooling_operation)