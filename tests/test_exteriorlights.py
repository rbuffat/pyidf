import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.exterior_equipment import ExteriorLights

log = logging.getLogger(__name__)

class TestExteriorLights(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_exteriorlights(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExteriorLights()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_schedule_name = "object-list|Schedule Name"
        obj.schedule_name = var_schedule_name
        # real
        var_design_level = 0.0
        obj.design_level = var_design_level
        # alpha
        var_control_option = "ScheduleNameOnly"
        obj.control_option = var_control_option
        # alpha
        var_enduse_subcategory = "End-Use Subcategory"
        obj.enduse_subcategory = var_enduse_subcategory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.exteriorlightss[0].name, var_name)
        self.assertEqual(idf2.exteriorlightss[0].schedule_name, var_schedule_name)
        self.assertAlmostEqual(idf2.exteriorlightss[0].design_level, var_design_level)
        self.assertEqual(idf2.exteriorlightss[0].control_option, var_control_option)
        self.assertEqual(idf2.exteriorlightss[0].enduse_subcategory, var_enduse_subcategory)