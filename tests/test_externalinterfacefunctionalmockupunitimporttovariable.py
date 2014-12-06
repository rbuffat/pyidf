import os
import tempfile
import unittest
import pyidf
from pyidf.external_interface import ExternalInterfaceFunctionalMockupUnitImportToVariable
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestExternalInterfaceFunctionalMockupUnitImportToVariable(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_externalinterfacefunctionalmockupunitimporttovariable(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ExternalInterfaceFunctionalMockupUnitImportToVariable()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_fmu_file_name = "object-list|FMU File Name"
        obj.fmu_file_name = var_fmu_file_name
        # alpha
        var_fmu_instance_name = "FMU Instance Name"
        obj.fmu_instance_name = var_fmu_instance_name
        # alpha
        var_fmu_variable_name = "FMU Variable Name"
        obj.fmu_variable_name = var_fmu_variable_name
        # real
        var_initial_value = 5.5
        obj.initial_value = var_initial_value

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttovariables[0].name, var_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttovariables[0].fmu_file_name, var_fmu_file_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttovariables[0].fmu_instance_name, var_fmu_instance_name)
        self.assertEqual(idf2.externalinterfacefunctionalmockupunitimporttovariables[0].fmu_variable_name, var_fmu_variable_name)
        self.assertAlmostEqual(idf2.externalinterfacefunctionalmockupunitimporttovariables[0].initial_value, var_initial_value)