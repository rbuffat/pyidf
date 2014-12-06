import os
import tempfile
import unittest
import pyidf
from pyidf.external_interface import ExternalInterface
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestExternalInterface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterface()
        # alpha
        var_name_of_external_interface = "PtolemyServer"
        obj.name_of_external_interface = var_name_of_external_interface

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfaces[0].name_of_external_interface, var_name_of_external_interface)