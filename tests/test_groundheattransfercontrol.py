import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.detailed_ground_heat_transfer import GroundHeatTransferControl

log = logging.getLogger(__name__)

class TestGroundHeatTransferControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheattransfercontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatTransferControl()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_run_basement_preprocessor = "Yes"
        obj.run_basement_preprocessor = var_run_basement_preprocessor
        # alpha
        var_run_slab_preprocessor = "Yes"
        obj.run_slab_preprocessor = var_run_slab_preprocessor

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheattransfercontrols[0].name, var_name)
        self.assertEqual(idf2.groundheattransfercontrols[0].run_basement_preprocessor, var_run_basement_preprocessor)
        self.assertEqual(idf2.groundheattransfercontrols[0].run_slab_preprocessor, var_run_slab_preprocessor)