import os
import tempfile
import unittest
import pyidf
from pyidf.external_interface import ExternalInterfaceFunctionalMockupUnitImport
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestExternalInterfaceFunctionalMockupUnitImport(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfacefunctionalmockupunitimport(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceFunctionalMockupUnitImport()
        # alpha
        var_fmu_file_name = "FMU File Name"
        obj.fmu_file_name = var_fmu_file_name
        # real
        var_fmu_timeout = 2.2
        obj.fmu_timeout = var_fmu_timeout
        # integer
        var_fmu_loggingon = 3
        obj.fmu_loggingon = var_fmu_loggingon

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimports[0].fmu_file_name, var_fmu_file_name)
        self.assertAlmostEqual(idf2.externalinterfacefunctionalmockupunitimports[0].fmu_timeout, var_fmu_timeout)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimports[0].fmu_loggingon, var_fmu_loggingon)