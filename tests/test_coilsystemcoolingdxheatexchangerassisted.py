import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilSystemCoolingDxHeatExchangerAssisted

log = logging.getLogger(__name__)

class TestCoilSystemCoolingDxHeatExchangerAssisted(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilsystemcoolingdxheatexchangerassisted(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilSystemCoolingDxHeatExchangerAssisted()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_heat_exchanger_object_type = "HeatExchanger:AirToAir:FlatPlate"
        obj.heat_exchanger_object_type = var_heat_exchanger_object_type
        # object-list
        var_heat_exchanger_name = "object-list|Heat Exchanger Name"
        obj.heat_exchanger_name = var_heat_exchanger_name
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:DX:SingleSpeed"
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
        self.assertEqual(idf2.coilsystemcoolingdxheatexchangerassisteds[0].name, var_name)
        self.assertEqual(idf2.coilsystemcoolingdxheatexchangerassisteds[0].heat_exchanger_object_type, var_heat_exchanger_object_type)
        self.assertEqual(idf2.coilsystemcoolingdxheatexchangerassisteds[0].heat_exchanger_name, var_heat_exchanger_name)
        self.assertEqual(idf2.coilsystemcoolingdxheatexchangerassisteds[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.coilsystemcoolingdxheatexchangerassisteds[0].cooling_coil_name, var_cooling_coil_name)