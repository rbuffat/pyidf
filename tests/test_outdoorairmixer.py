import os
import tempfile
import unittest
import pyidf
from pyidf.air_distribution import OutdoorAirMixer
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestOutdoorAirMixer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_outdoorairmixer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = OutdoorAirMixer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_mixed_air_node_name = "node|Mixed Air Node Name"
        obj.mixed_air_node_name = var_mixed_air_node_name
        # node
        var_outdoor_air_stream_node_name = "node|Outdoor Air Stream Node Name"
        obj.outdoor_air_stream_node_name = var_outdoor_air_stream_node_name
        # node
        var_relief_air_stream_node_name = "node|Relief Air Stream Node Name"
        obj.relief_air_stream_node_name = var_relief_air_stream_node_name
        # node
        var_return_air_stream_node_name = "node|Return Air Stream Node Name"
        obj.return_air_stream_node_name = var_return_air_stream_node_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.outdoorairmixers[0].name, var_name)
        self.assertEqual(idf2.outdoorairmixers[0].mixed_air_node_name, var_mixed_air_node_name)
        self.assertEqual(idf2.outdoorairmixers[0].outdoor_air_stream_node_name, var_outdoor_air_stream_node_name)
        self.assertEqual(idf2.outdoorairmixers[0].relief_air_stream_node_name, var_relief_air_stream_node_name)
        self.assertEqual(idf2.outdoorairmixers[0].return_air_stream_node_name, var_return_air_stream_node_name)