import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationSystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_refrigerated_case_or_walkin_or_caseandwalkinlist_name = "object-list|Refrigerated Case or Walkin or CaseAndWalkInList Name"
        obj.refrigerated_case_or_walkin_or_caseandwalkinlist_name = var_refrigerated_case_or_walkin_or_caseandwalkinlist_name
        # object-list
        var_refrigeration_transfer_load_or_transferload_list_name = "object-list|Refrigeration Transfer Load or TransferLoad List Name"
        obj.refrigeration_transfer_load_or_transferload_list_name = var_refrigeration_transfer_load_or_transferload_list_name
        # object-list
        var_refrigeration_condenser_name = "object-list|Refrigeration Condenser Name"
        obj.refrigeration_condenser_name = var_refrigeration_condenser_name
        # object-list
        var_compressor_or_compressorlist_name = "object-list|Compressor or CompressorList Name"
        obj.compressor_or_compressorlist_name = var_compressor_or_compressorlist_name
        # real
        var_minimum_condensing_temperature = 6.6
        obj.minimum_condensing_temperature = var_minimum_condensing_temperature
        # object-list
        var_refrigeration_system_working_fluid_type = "object-list|Refrigeration System Working Fluid Type"
        obj.refrigeration_system_working_fluid_type = var_refrigeration_system_working_fluid_type
        # alpha
        var_suction_temperature_control_type = "FloatSuctionTemperature"
        obj.suction_temperature_control_type = var_suction_temperature_control_type
        # object-list
        var_mechanical_subcooler_name = "object-list|Mechanical Subcooler Name"
        obj.mechanical_subcooler_name = var_mechanical_subcooler_name
        # object-list
        var_liquid_suction_heat_exchanger_subcooler_name = "object-list|Liquid Suction Heat Exchanger Subcooler Name"
        obj.liquid_suction_heat_exchanger_subcooler_name = var_liquid_suction_heat_exchanger_subcooler_name
        # real
        var_sum_ua_suction_piping = 11.11
        obj.sum_ua_suction_piping = var_sum_ua_suction_piping
        # object-list
        var_suction_piping_zone_name = "object-list|Suction Piping Zone Name"
        obj.suction_piping_zone_name = var_suction_piping_zone_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory
        # integer
        var_number_of_compressor_stages = 1
        obj.number_of_compressor_stages = var_number_of_compressor_stages
        # alpha
        var_intercooler_type = "None"
        obj.intercooler_type = var_intercooler_type
        # real
        var_shellandcoil_intercooler_effectiveness = 16.16
        obj.shellandcoil_intercooler_effectiveness = var_shellandcoil_intercooler_effectiveness
        # object-list
        var_highstage_compressor_or_compressorlist_name = "object-list|High-Stage Compressor or CompressorList Name"
        obj.highstage_compressor_or_compressorlist_name = var_highstage_compressor_or_compressorlist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationsystems[0].name, var_name)
        self.assertEqual(idf2.refrigerationsystems[0].refrigerated_case_or_walkin_or_caseandwalkinlist_name, var_refrigerated_case_or_walkin_or_caseandwalkinlist_name)
        self.assertEqual(idf2.refrigerationsystems[0].refrigeration_transfer_load_or_transferload_list_name, var_refrigeration_transfer_load_or_transferload_list_name)
        self.assertEqual(idf2.refrigerationsystems[0].refrigeration_condenser_name, var_refrigeration_condenser_name)
        self.assertEqual(idf2.refrigerationsystems[0].compressor_or_compressorlist_name, var_compressor_or_compressorlist_name)
        self.assertAlmostEqual(idf2.refrigerationsystems[0].minimum_condensing_temperature, var_minimum_condensing_temperature)
        self.assertEqual(idf2.refrigerationsystems[0].refrigeration_system_working_fluid_type, var_refrigeration_system_working_fluid_type)
        self.assertEqual(idf2.refrigerationsystems[0].suction_temperature_control_type, var_suction_temperature_control_type)
        self.assertEqual(idf2.refrigerationsystems[0].mechanical_subcooler_name, var_mechanical_subcooler_name)
        self.assertEqual(idf2.refrigerationsystems[0].liquid_suction_heat_exchanger_subcooler_name, var_liquid_suction_heat_exchanger_subcooler_name)
        self.assertAlmostEqual(idf2.refrigerationsystems[0].sum_ua_suction_piping, var_sum_ua_suction_piping)
        self.assertEqual(idf2.refrigerationsystems[0].suction_piping_zone_name, var_suction_piping_zone_name)
        self.assertEqual(idf2.refrigerationsystems[0].enduse_subcategory, var_enduse_subcategory)
        self.assertEqual(idf2.refrigerationsystems[0].number_of_compressor_stages, var_number_of_compressor_stages)
        self.assertEqual(idf2.refrigerationsystems[0].intercooler_type, var_intercooler_type)
        self.assertAlmostEqual(idf2.refrigerationsystems[0].shellandcoil_intercooler_effectiveness, var_shellandcoil_intercooler_effectiveness)
        self.assertEqual(idf2.refrigerationsystems[0].highstage_compressor_or_compressorlist_name, var_highstage_compressor_or_compressorlist_name)