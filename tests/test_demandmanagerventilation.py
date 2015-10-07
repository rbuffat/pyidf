import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.demand_limiting_controls import DemandManagerVentilation

log = logging.getLogger(__name__)

class TestDemandManagerVentilation(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_demandmanagerventilation(self):

        pyidf.validation_level = ValidationLevel.error

        obj = DemandManagerVentilation()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_limit_control = "Off"
        obj.limit_control = var_limit_control
        # integer
        var_minimum_limit_duration = 1
        obj.minimum_limit_duration = var_minimum_limit_duration
        # real
        var_fixed_rate = 0.0
        obj.fixed_rate = var_fixed_rate
        # real
        var_reduction_ratio = 0.5
        obj.reduction_ratio = var_reduction_ratio
        # real
        var_limit_step_change = 7.7
        obj.limit_step_change = var_limit_step_change
        # alpha
        var_selection_control = "All"
        obj.selection_control = var_selection_control
        # integer
        var_rotation_duration = 0
        obj.rotation_duration = var_rotation_duration
        paras = []
        var_controller_outdoor_air_1_name = "object-list|Controller Outdoor Air 1 Name"
        paras.append(var_controller_outdoor_air_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.demandmanagerventilations[0].name, var_name)
        self.assertEqual(idf2.demandmanagerventilations[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.demandmanagerventilations[0].limit_control, var_limit_control)
        self.assertEqual(idf2.demandmanagerventilations[0].minimum_limit_duration, var_minimum_limit_duration)
        self.assertAlmostEqual(idf2.demandmanagerventilations[0].fixed_rate, var_fixed_rate)
        self.assertAlmostEqual(idf2.demandmanagerventilations[0].reduction_ratio, var_reduction_ratio)
        self.assertAlmostEqual(idf2.demandmanagerventilations[0].limit_step_change, var_limit_step_change)
        self.assertEqual(idf2.demandmanagerventilations[0].selection_control, var_selection_control)
        self.assertEqual(idf2.demandmanagerventilations[0].rotation_duration, var_rotation_duration)
        index = obj.extensible_field_index("Controller Outdoor Air 1 Name")
        self.assertEqual(idf2.demandmanagerventilations[0].extensibles[0][index], var_controller_outdoor_air_1_name)