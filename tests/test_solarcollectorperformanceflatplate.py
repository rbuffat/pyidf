import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.solar_collectors import SolarCollectorPerformanceFlatPlate

log = logging.getLogger(__name__)

class TestSolarCollectorPerformanceFlatPlate(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorperformanceflatplate(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorPerformanceFlatPlate()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_gross_area = 0.0001
        obj.gross_area = var_gross_area
        # alpha
        var_test_fluid = "Water"
        obj.test_fluid = var_test_fluid
        # real
        var_test_flow_rate = 0.0001
        obj.test_flow_rate = var_test_flow_rate
        # alpha
        var_test_correlation_type = "Inlet"
        obj.test_correlation_type = var_test_correlation_type
        # real
        var_coefficient_1_of_efficiency_equation = 6.6
        obj.coefficient_1_of_efficiency_equation = var_coefficient_1_of_efficiency_equation
        # real
        var_coefficient_2_of_efficiency_equation = 7.7
        obj.coefficient_2_of_efficiency_equation = var_coefficient_2_of_efficiency_equation
        # real
        var_coefficient_3_of_efficiency_equation = 8.8
        obj.coefficient_3_of_efficiency_equation = var_coefficient_3_of_efficiency_equation
        # real
        var_coefficient_2_of_incident_angle_modifier = 9.9
        obj.coefficient_2_of_incident_angle_modifier = var_coefficient_2_of_incident_angle_modifier
        # real
        var_coefficient_3_of_incident_angle_modifier = 10.1
        obj.coefficient_3_of_incident_angle_modifier = var_coefficient_3_of_incident_angle_modifier

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorperformanceflatplates[0].name, var_name)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].gross_area, var_gross_area)
        self.assertEqual(idf2.solarcollectorperformanceflatplates[0].test_fluid, var_test_fluid)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].test_flow_rate, var_test_flow_rate)
        self.assertEqual(idf2.solarcollectorperformanceflatplates[0].test_correlation_type, var_test_correlation_type)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].coefficient_1_of_efficiency_equation, var_coefficient_1_of_efficiency_equation)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].coefficient_2_of_efficiency_equation, var_coefficient_2_of_efficiency_equation)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].coefficient_3_of_efficiency_equation, var_coefficient_3_of_efficiency_equation)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].coefficient_2_of_incident_angle_modifier, var_coefficient_2_of_incident_angle_modifier)
        self.assertAlmostEqual(idf2.solarcollectorperformanceflatplates[0].coefficient_3_of_incident_angle_modifier, var_coefficient_3_of_incident_angle_modifier)