import os
import tempfile
import unittest
import pyidf
from pyidf.non import LoadProfilePlant
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestLoadProfilePlant(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_loadprofileplant(self):

        pyidf.validation_level = ValidationLevel.error

        obj = LoadProfilePlant()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # object-list
        var_load_schedule_name = "object-list|Load Schedule Name"
        obj.load_schedule_name = var_load_schedule_name
        # real
        var_peak_flow_rate = 5.5
        obj.peak_flow_rate = var_peak_flow_rate
        # object-list
        var_flow_rate_fraction_schedule_name = "object-list|Flow Rate Fraction Schedule Name"
        obj.flow_rate_fraction_schedule_name = var_flow_rate_fraction_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.loadprofileplants[0].name, var_name)
        self.assertEqual(idf2.loadprofileplants[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.loadprofileplants[0].outlet_node_name, var_outlet_node_name)
        self.assertEqual(idf2.loadprofileplants[0].load_schedule_name, var_load_schedule_name)
        self.assertAlmostEqual(idf2.loadprofileplants[0].peak_flow_rate, var_peak_flow_rate)
        self.assertEqual(idf2.loadprofileplants[0].flow_rate_fraction_schedule_name, var_flow_rate_fraction_schedule_name)