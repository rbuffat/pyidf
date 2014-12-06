import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import ElectricLoadCenterDistribution
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestElectricLoadCenterDistribution(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcenterdistribution(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterDistribution()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_generator_list_name = "object-list|Generator List Name"
        obj.generator_list_name = var_generator_list_name
        # alpha
        var_generator_operation_scheme_type = "Baseload"
        obj.generator_operation_scheme_type = var_generator_operation_scheme_type
        # real
        var_demand_limit_scheme_purchased_electric_demand_limit = 4.4
        obj.demand_limit_scheme_purchased_electric_demand_limit = var_demand_limit_scheme_purchased_electric_demand_limit
        # object-list
        var_track_schedule_name_scheme_schedule_name = "object-list|Track Schedule Name Scheme Schedule Name"
        obj.track_schedule_name_scheme_schedule_name = var_track_schedule_name_scheme_schedule_name
        # external-list
        var_track_meter_scheme_meter_name = "external-list|Track Meter Scheme Meter Name"
        obj.track_meter_scheme_meter_name = var_track_meter_scheme_meter_name
        # alpha
        var_electrical_buss_type = "AlternatingCurrent"
        obj.electrical_buss_type = var_electrical_buss_type
        # object-list
        var_inverter_object_name = "object-list|Inverter Object Name"
        obj.inverter_object_name = var_inverter_object_name
        # object-list
        var_electrical_storage_object_name = "object-list|Electrical Storage Object Name"
        obj.electrical_storage_object_name = var_electrical_storage_object_name
        # object-list
        var_transformer_object_name = "object-list|Transformer Object Name"
        obj.transformer_object_name = var_transformer_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcenterdistributions[0].name, var_name)
        self.assertEqual(idf2.electricloadcenterdistributions[0].generator_list_name, var_generator_list_name)
        self.assertEqual(idf2.electricloadcenterdistributions[0].generator_operation_scheme_type, var_generator_operation_scheme_type)
        self.assertAlmostEqual(idf2.electricloadcenterdistributions[0].demand_limit_scheme_purchased_electric_demand_limit, var_demand_limit_scheme_purchased_electric_demand_limit)
        self.assertEqual(idf2.electricloadcenterdistributions[0].track_schedule_name_scheme_schedule_name, var_track_schedule_name_scheme_schedule_name)
        self.assertEqual(idf2.electricloadcenterdistributions[0].track_meter_scheme_meter_name, var_track_meter_scheme_meter_name)
        self.assertEqual(idf2.electricloadcenterdistributions[0].electrical_buss_type, var_electrical_buss_type)
        self.assertEqual(idf2.electricloadcenterdistributions[0].inverter_object_name, var_inverter_object_name)
        self.assertEqual(idf2.electricloadcenterdistributions[0].electrical_storage_object_name, var_electrical_storage_object_name)
        self.assertEqual(idf2.electricloadcenterdistributions[0].transformer_object_name, var_transformer_object_name)