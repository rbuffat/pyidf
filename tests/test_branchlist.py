import os
import tempfile
import unittest
import pyidf
from pyidf.pumps import BranchList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestBranchList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_branchlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = BranchList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_branch_name = "object-list|Branch Name"
        paras.append(var_branch_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.branchlists[0].name, var_name)
        index = obj.extensible_field_index("Branch Name")
        self.assertEqual(idf2.branchlists[0].extensibles[0][index], var_branch_name)