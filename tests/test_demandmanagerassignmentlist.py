import os
import tempfile
import unittest
import pyidf
from pyidf.demand_limiting_controls import DemandManagerAssignmentList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestDemandManagerAssignmentList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_demandmanagerassignmentlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DemandManagerAssignmentList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # external-list
        var_meter_name = "external-list|Meter Name"
        obj.meter_name = var_meter_name
        # object-list
        var_demand_limit_schedule_name = "object-list|Demand Limit Schedule Name"
        obj.demand_limit_schedule_name = var_demand_limit_schedule_name
        # real
        var_demand_limit_safety_fraction = 0.0
        obj.demand_limit_safety_fraction = var_demand_limit_safety_fraction
        # object-list
        var_billing_period_schedule_name = "object-list|Billing Period Schedule Name"
        obj.billing_period_schedule_name = var_billing_period_schedule_name
        # object-list
        var_peak_period_schedule_name = "object-list|Peak Period Schedule Name"
        obj.peak_period_schedule_name = var_peak_period_schedule_name
        # integer
        var_demand_window_length = 1
        obj.demand_window_length = var_demand_window_length
        # alpha
        var_demand_manager_priority = "Sequential"
        obj.demand_manager_priority = var_demand_manager_priority
        paras = []
        var_demandmanager_1_object_type = "DemandManager:ExteriorLights"
        paras.append(var_demandmanager_1_object_type)
        var_demandmanager_1_name = "object-list|DemandManager 1 Name"
        paras.append(var_demandmanager_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].name, var_name)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].meter_name, var_meter_name)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].demand_limit_schedule_name, var_demand_limit_schedule_name)
        self.assertAlmostEqual(idf2.demandmanagerassignmentlists[0].demand_limit_safety_fraction, var_demand_limit_safety_fraction)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].billing_period_schedule_name, var_billing_period_schedule_name)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].peak_period_schedule_name, var_peak_period_schedule_name)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].demand_window_length, var_demand_window_length)
        self.assertEqual(idf2.demandmanagerassignmentlists[0].demand_manager_priority, var_demand_manager_priority)
        index = obj.extensible_field_index("DemandManager 1 Object Type")
        self.assertEqual(idf2.demandmanagerassignmentlists[0].extensibles[0][index], var_demandmanager_1_object_type)
        index = obj.extensible_field_index("DemandManager 1 Name")
        self.assertEqual(idf2.demandmanagerassignmentlists[0].extensibles[0][index], var_demandmanager_1_name)