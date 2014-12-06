import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilSystemHeatingDx
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilSystemHeatingDx(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilsystemheatingdx(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilSystemHeatingDx()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:DX:SingleSpeed"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilsystemheatingdxs[0].name, var_name)
        self.assertEqual(idf2.coilsystemheatingdxs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.coilsystemheatingdxs[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.coilsystemheatingdxs[0].heating_coil_name, var_heating_coil_name)