import os
import tempfile
import unittest
import pyidf
from pyidf.external_interface import ExternalInterfaceFunctionalMockupUnitExportFromVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestExternalInterfaceFunctionalMockupUnitExportFromVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfacefunctionalmockupunitexportfromvariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceFunctionalMockupUnitExportFromVariable()
        # alpha
        var_outputvariable_index_key_name = "Output:Variable Index Key Name"
        obj.outputvariable_index_key_name = var_outputvariable_index_key_name
        # external-list
        var_outputvariable_name = "external-list|Output:Variable Name"
        obj.outputvariable_name = var_outputvariable_name
        # alpha
        var_fmu_variable_name = "FMU Variable Name"
        obj.fmu_variable_name = var_fmu_variable_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexportfromvariables[0].outputvariable_index_key_name, var_outputvariable_index_key_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexportfromvariables[0].outputvariable_name, var_outputvariable_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitexportfromvariables[0].fmu_variable_name, var_fmu_variable_name)