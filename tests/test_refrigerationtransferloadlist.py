import os
import tempfile
import unittest
import pyidf
from pyidf.refrigeration import RefrigerationTransferLoadList
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestRefrigerationTransferLoadList(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationtransferloadlist(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationTransferLoadList()
        # alpha
        var_name = "Name"
        obj.name = var_name
        paras = []
        var_cascade_condenser_name_or_secondary_system_1_name = "object-list|Cascade Condenser Name or Secondary System 1 Name"
        paras.append(var_cascade_condenser_name_or_secondary_system_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationtransferloadlists[0].name, var_name)
        index = obj.extensible_field_index("Cascade Condenser Name or Secondary System 1 Name")
        self.assertEqual(idf2.refrigerationtransferloadlists[0].extensibles[0][index], var_cascade_condenser_name_or_secondary_system_1_name)