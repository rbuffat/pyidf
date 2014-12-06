import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.setpoint_managers import SetpointManagerCondenserEnteringResetIdeal

log = logging.getLogger(__name__)

class TestSetpointManagerCondenserEnteringResetIdeal(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_setpointmanagercondenserenteringresetideal(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SetpointManagerCondenserEnteringResetIdeal()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_control_variable = "Temperature"
        obj.control_variable = var_control_variable
        # real
        var_minimum_lift = 3.3
        obj.minimum_lift = var_minimum_lift
        # real
        var_maximum_condenser_entering_water_temperature = 4.4
        obj.maximum_condenser_entering_water_temperature = var_maximum_condenser_entering_water_temperature
        # node
        var_setpoint_node_or_nodelist_name = "node|Setpoint Node or NodeList Name"
        obj.setpoint_node_or_nodelist_name = var_setpoint_node_or_nodelist_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.setpointmanagercondenserenteringresetideals[0].name, var_name)
        self.assertEqual(idf2.setpointmanagercondenserenteringresetideals[0].control_variable, var_control_variable)
        self.assertAlmostEqual(idf2.setpointmanagercondenserenteringresetideals[0].minimum_lift, var_minimum_lift)
        self.assertAlmostEqual(idf2.setpointmanagercondenserenteringresetideals[0].maximum_condenser_entering_water_temperature, var_maximum_condenser_entering_water_temperature)
        self.assertEqual(idf2.setpointmanagercondenserenteringresetideals[0].setpoint_node_or_nodelist_name, var_setpoint_node_or_nodelist_name)