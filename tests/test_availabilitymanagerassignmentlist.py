import os
import tempfile
import unittest
import pyidf
from pyidf.system_availability_managers import AvailabilityManagerAssignmentList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAvailabilityManagerAssignmentList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_availabilitymanagerassignmentlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AvailabilityManagerAssignmentList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_availability_manager_1_object_type = "AvailabilityManager:Scheduled"
        paras.append(var_availability_manager_1_object_type)
        var_availability_manager_1_name = "object-list|Availability Manager 1 Name"
        paras.append(var_availability_manager_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.availabilitymanagerassignmentlists[0].name, var_name)
        index = obj.extensible_field_index("Availability Manager 1 Object Type")
        self.assertEqual(idf2.availabilitymanagerassignmentlists[0].extensibles[0][index], var_availability_manager_1_object_type)
        index = obj.extensible_field_index("Availability Manager 1 Name")
        self.assertEqual(idf2.availabilitymanagerassignmentlists[0].extensibles[0][index], var_availability_manager_1_name)