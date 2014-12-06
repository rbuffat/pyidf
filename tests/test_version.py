import os
import tempfile
import unittest
import pyidf
from pyidf.simulation_parameters import Version
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestVersion(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_version(self):

        pyidf.validation_level = ValidationLevel.error

        obj = Version()
        # alpha
        var_version_identifier = "Version Identifier"
        obj.version_identifier = var_version_identifier

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.versions[0].version_identifier, var_version_identifier)