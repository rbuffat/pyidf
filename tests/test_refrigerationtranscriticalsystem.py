import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationTranscriticalSystem
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationTranscriticalSystem(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationtranscriticalsystem(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationTranscriticalSystem()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_system_type = "SingleStage"
        obj.system_type = var_system_type
        # object-list
        var_medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = "object-list|Medium Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"
        obj.medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = var_medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name
        # object-list
        var_low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = "object-list|Low Temperature Refrigerated Case or Walkin or CaseAndWalkInList Name"
        obj.low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name = var_low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name
        # object-list
        var_refrigeration_gas_cooler_name = "object-list|Refrigeration Gas Cooler Name"
        obj.refrigeration_gas_cooler_name = var_refrigeration_gas_cooler_name
        # object-list
        var_high_pressure_compressor_or_compressorlist_name = "object-list|High Pressure Compressor or CompressorList Name"
        obj.high_pressure_compressor_or_compressorlist_name = var_high_pressure_compressor_or_compressorlist_name
        # object-list
        var_low_pressure_compressor_or_compressorlist_name = "object-list|Low Pressure Compressor or CompressorList Name"
        obj.low_pressure_compressor_or_compressorlist_name = var_low_pressure_compressor_or_compressorlist_name
        # real
        var_receiver_pressure = 8.8
        obj.receiver_pressure = var_receiver_pressure
        # real
        var_subcooler_effectiveness = 9.9
        obj.subcooler_effectiveness = var_subcooler_effectiveness
        # object-list
        var_refrigeration_system_working_fluid_type = "object-list|Refrigeration System Working Fluid Type"
        obj.refrigeration_system_working_fluid_type = var_refrigeration_system_working_fluid_type
        # real
        var_sum_ua_suction_piping_for_medium_temperature_loads = 11.11
        obj.sum_ua_suction_piping_for_medium_temperature_loads = var_sum_ua_suction_piping_for_medium_temperature_loads
        # object-list
        var_medium_temperature_suction_piping_zone_name = "object-list|Medium Temperature Suction Piping Zone Name"
        obj.medium_temperature_suction_piping_zone_name = var_medium_temperature_suction_piping_zone_name
        # real
        var_sum_ua_suction_piping_for_low_temperature_loads = 13.13
        obj.sum_ua_suction_piping_for_low_temperature_loads = var_sum_ua_suction_piping_for_low_temperature_loads
        # object-list
        var_low_temperature_suction_piping_zone_name = "object-list|Low Temperature Suction Piping Zone Name"
        obj.low_temperature_suction_piping_zone_name = var_low_temperature_suction_piping_zone_name
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].name, var_name)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].system_type, var_system_type)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name, var_medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name, var_low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].refrigeration_gas_cooler_name, var_refrigeration_gas_cooler_name)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].high_pressure_compressor_or_compressorlist_name, var_high_pressure_compressor_or_compressorlist_name)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].low_pressure_compressor_or_compressorlist_name, var_low_pressure_compressor_or_compressorlist_name)
        self.assertAlmostEqual(idf2.refrigerationtranscriticalsystems[0].receiver_pressure, var_receiver_pressure)
        self.assertAlmostEqual(idf2.refrigerationtranscriticalsystems[0].subcooler_effectiveness, var_subcooler_effectiveness)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].refrigeration_system_working_fluid_type, var_refrigeration_system_working_fluid_type)
        self.assertAlmostEqual(idf2.refrigerationtranscriticalsystems[0].sum_ua_suction_piping_for_medium_temperature_loads, var_sum_ua_suction_piping_for_medium_temperature_loads)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].medium_temperature_suction_piping_zone_name, var_medium_temperature_suction_piping_zone_name)
        self.assertAlmostEqual(idf2.refrigerationtranscriticalsystems[0].sum_ua_suction_piping_for_low_temperature_loads, var_sum_ua_suction_piping_for_low_temperature_loads)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].low_temperature_suction_piping_zone_name, var_low_temperature_suction_piping_zone_name)
        self.assertEqual(idf2.refrigerationtranscriticalsystems[0].enduse_subcategory, var_enduse_subcategory)