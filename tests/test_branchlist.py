import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.node import BranchList

log = logging.getLogger(__name__)

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
        var_branch_1_name = "object-list|Branch 1 Name"
        paras.append(var_branch_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.branchlists[0].name, var_name)
        index = obj.extensible_field_index("Branch 1 Name")
        self.assertEqual(idf2.branchlists[0].extensibles[0][index], var_branch_1_name)