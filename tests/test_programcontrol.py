import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import ProgramControl
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestProgramControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_programcontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ProgramControl()
        # integer
        var_number_of_threads_allowed = 0
        obj.number_of_threads_allowed = var_number_of_threads_allowed

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.programcontrols[0].number_of_threads_allowed, var_number_of_threads_allowed)