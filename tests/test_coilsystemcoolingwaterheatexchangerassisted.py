import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilSystemCoolingWaterHeatExchangerAssisted

log = logging.getLogger(__name__)

class TestCoilSystemCoolingWaterHeatExchangerAssisted(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilsystemcoolingwaterheatexchangerassisted(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilSystemCoolingWaterHeatExchangerAssisted()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_heat_exchanger_object_type = "HeatExchanger:AirToAir:FlatPlate"
        obj.heat_exchanger_object_type = var_heat_exchanger_object_type
        # alpha
        var_heat_exchanger_name = "Heat Exchanger Name"
        obj.heat_exchanger_name = var_heat_exchanger_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:Water"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilsystemcoolingwaterheatexchangerassisteds[0].name, var_name)
        self.assertEqual(idf2.coilsystemcoolingwaterheatexchangerassisteds[0].heat_exchanger_object_type, var_heat_exchanger_object_type)
        self.assertEqual(idf2.coilsystemcoolingwaterheatexchangerassisteds[0].heat_exchanger_name, var_heat_exchanger_name)
        self.assertEqual(idf2.coilsystemcoolingwaterheatexchangerassisteds[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.coilsystemcoolingwaterheatexchangerassisteds[0].cooling_coil_name, var_cooling_coil_name)