import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.advanced_construction import ComplexFenestrationPropertySolarAbsorbedLayers

log = logging.getLogger(__name__)

class TestComplexFenestrationPropertySolarAbsorbedLayers(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_complexfenestrationpropertysolarabsorbedlayers(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ComplexFenestrationPropertySolarAbsorbedLayers()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_fenestration_surface = "object-list|Fenestration Surface"
        obj.fenestration_surface = var_fenestration_surface
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # object-list
        var_layer_1_solar_radiation_absorbed_schedule_name = "object-list|Layer 1 Solar Radiation Absorbed Schedule Name"
        obj.layer_1_solar_radiation_absorbed_schedule_name = var_layer_1_solar_radiation_absorbed_schedule_name
        # object-list
        var_layer_2_solar_radiation_absorbed_schedule_name = "object-list|Layer 2 Solar Radiation Absorbed Schedule Name"
        obj.layer_2_solar_radiation_absorbed_schedule_name = var_layer_2_solar_radiation_absorbed_schedule_name
        # object-list
        var_layer_3_solar_radiation_absorbed_schedule_name = "object-list|Layer 3 Solar Radiation Absorbed Schedule Name"
        obj.layer_3_solar_radiation_absorbed_schedule_name = var_layer_3_solar_radiation_absorbed_schedule_name
        # object-list
        var_layer_4_solar_radiation_absorbed_schedule_name = "object-list|Layer 4 Solar Radiation Absorbed Schedule Name"
        obj.layer_4_solar_radiation_absorbed_schedule_name = var_layer_4_solar_radiation_absorbed_schedule_name
        # object-list
        var_layer_5_solar_radiation_absorbed_schedule_name = "object-list|Layer 5 Solar Radiation Absorbed Schedule Name"
        obj.layer_5_solar_radiation_absorbed_schedule_name = var_layer_5_solar_radiation_absorbed_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].name, var_name)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].fenestration_surface, var_fenestration_surface)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].construction_name, var_construction_name)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].layer_1_solar_radiation_absorbed_schedule_name, var_layer_1_solar_radiation_absorbed_schedule_name)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].layer_2_solar_radiation_absorbed_schedule_name, var_layer_2_solar_radiation_absorbed_schedule_name)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].layer_3_solar_radiation_absorbed_schedule_name, var_layer_3_solar_radiation_absorbed_schedule_name)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].layer_4_solar_radiation_absorbed_schedule_name, var_layer_4_solar_radiation_absorbed_schedule_name)
        self.assertEqual(idf2.complexfenestrationpropertysolarabsorbedlayerss[0].layer_5_solar_radiation_absorbed_schedule_name, var_layer_5_solar_radiation_absorbed_schedule_name)