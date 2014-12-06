import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationCaseAndWalkInList

log = logging.getLogger(__name__)

class TestRefrigerationCaseAndWalkInList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationcaseandwalkinlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationCaseAndWalkInList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_case_or_walkin_1_name = "object-list|Case or WalkIn 1 Name"
        paras.append(var_case_or_walkin_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationcaseandwalkinlists[0].name, var_name)
        index = obj.extensible_field_index("Case or WalkIn 1 Name")
        self.assertEqual(idf2.refrigerationcaseandwalkinlists[0].extensibles[0][index], var_case_or_walkin_1_name)