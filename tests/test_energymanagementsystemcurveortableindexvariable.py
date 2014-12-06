import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.energy_management_system import EnergyManagementSystemCurveOrTableIndexVariable

log = logging.getLogger(__name__)

class TestEnergyManagementSystemCurveOrTableIndexVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_energymanagementsystemcurveortableindexvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = EnergyManagementSystemCurveOrTableIndexVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_curve_or_table_object_name = "object-list|Curve or Table Object Name"
        obj.curve_or_table_object_name = var_curve_or_table_object_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.energymanagementsystemcurveortableindexvariables[0].name, var_name)
        self.assertEqual(idf2.energymanagementsystemcurveortableindexvariables[0].curve_or_table_object_name, var_curve_or_table_object_name)