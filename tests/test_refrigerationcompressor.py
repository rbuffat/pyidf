import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationCompressor

log = logging.getLogger(__name__)

class TestRefrigerationCompressor(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcompressor(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCompressor()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_refrigeration_compressor_power_curve_name = "object-list|Refrigeration Compressor Power Curve Name"
        obj.refrigeration_compressor_power_curve_name = var_refrigeration_compressor_power_curve_name
        # object-list
        var_refrigeration_compressor_capacity_curve_name = "object-list|Refrigeration Compressor Capacity Curve Name"
        obj.refrigeration_compressor_capacity_curve_name = var_refrigeration_compressor_capacity_curve_name
        # real
        var_rated_superheat = 4.4
        obj.rated_superheat = var_rated_superheat
        # real
        var_rated_return_gas_temperature = 5.5
        obj.rated_return_gas_temperature = var_rated_return_gas_temperature
        # real
        var_rated_liquid_temperature = 6.6
        obj.rated_liquid_temperature = var_rated_liquid_temperature
        # real
        var_rated_subcooling = 7.7
        obj.rated_subcooling = var_rated_subcooling
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # alpha
        var_mode_of_operation = "Subcritical"
        obj.mode_of_operation = var_mode_of_operation
        # object-list
        var_transcritical_compressor_power_curve_name = "object-list|Transcritical Compressor Power Curve Name"
        obj.transcritical_compressor_power_curve_name = var_transcritical_compressor_power_curve_name
        # object-list
        var_transcritical_compressor_capacity_curve_name = "object-list|Transcritical Compressor Capacity Curve Name"
        obj.transcritical_compressor_capacity_curve_name = var_transcritical_compressor_capacity_curve_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcompressors[0].name, var_name)
        self.assertEqual(idf2.refrigerationcompressors[0].refrigeration_compressor_power_curve_name, var_refrigeration_compressor_power_curve_name)
        self.assertEqual(idf2.refrigerationcompressors[0].refrigeration_compressor_capacity_curve_name, var_refrigeration_compressor_capacity_curve_name)
        self.assertAlmostEqual(idf2.refrigerationcompressors[0].rated_superheat, var_rated_superheat)
        self.assertAlmostEqual(idf2.refrigerationcompressors[0].rated_return_gas_temperature, var_rated_return_gas_temperature)
        self.assertAlmostEqual(idf2.refrigerationcompressors[0].rated_liquid_temperature, var_rated_liquid_temperature)
        self.assertAlmostEqual(idf2.refrigerationcompressors[0].rated_subcooling, var_rated_subcooling)
        self.assertEqual(idf2.refrigerationcompressors[0].enduse_subcategory, var_enduse_subcategory)
        self.assertEqual(idf2.refrigerationcompressors[0].mode_of_operation, var_mode_of_operation)
        self.assertEqual(idf2.refrigerationcompressors[0].transcritical_compressor_power_curve_name, var_transcritical_compressor_power_curve_name)
        self.assertEqual(idf2.refrigerationcompressors[0].transcritical_compressor_capacity_curve_name, var_transcritical_compressor_capacity_curve_name)