import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.thermal_zones_and_surfaces import WindowPropertyAirflowControl

log = logging.getLogger(__name__)

class TestWindowPropertyAirflowControl(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_windowpropertyairflowcontrol(self):

        pyidf.validation_level = ValidationLevel.error

        obj = WindowPropertyAirflowControl()
        # object-list
        var_name = "object-list|Name"
        obj.name = var_name
        # alpha
        var_airflow_source = "IndoorAir"
        obj.airflow_source = var_airflow_source
        # alpha
        var_airflow_destination = "IndoorAir"
        obj.airflow_destination = var_airflow_destination
        # real
        var_maximum_flow_rate = 0.0
        obj.maximum_flow_rate = var_maximum_flow_rate
        # alpha
        var_airflow_control_type = "AlwaysOnAtMaximumFlow"
        obj.airflow_control_type = var_airflow_control_type
        # alpha
        var_airflow_is_scheduled = "Yes"
        obj.airflow_is_scheduled = var_airflow_is_scheduled
        # object-list
        var_airflow_multiplier_schedule_name = "object-list|Airflow Multiplier Schedule Name"
        obj.airflow_multiplier_schedule_name = var_airflow_multiplier_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.windowpropertyairflowcontrols[0].name, var_name)
        self.assertEqual(idf2.windowpropertyairflowcontrols[0].airflow_source, var_airflow_source)
        self.assertEqual(idf2.windowpropertyairflowcontrols[0].airflow_destination, var_airflow_destination)
        self.assertAlmostEqual(idf2.windowpropertyairflowcontrols[0].maximum_flow_rate, var_maximum_flow_rate)
        self.assertEqual(idf2.windowpropertyairflowcontrols[0].airflow_control_type, var_airflow_control_type)
        self.assertEqual(idf2.windowpropertyairflowcontrols[0].airflow_is_scheduled, var_airflow_is_scheduled)
        self.assertEqual(idf2.windowpropertyairflowcontrols[0].airflow_multiplier_schedule_name, var_airflow_multiplier_schedule_name)