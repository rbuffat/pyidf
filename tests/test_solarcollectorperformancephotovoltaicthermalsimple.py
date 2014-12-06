import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.solar_collectors import SolarCollectorPerformancePhotovoltaicThermalSimple

log = logging.getLogger(__name__)

class TestSolarCollectorPerformancePhotovoltaicThermalSimple(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorperformancephotovoltaicthermalsimple(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorPerformancePhotovoltaicThermalSimple()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_fraction_of_surface_area_with_active_thermal_collector = 0.50005
        obj.fraction_of_surface_area_with_active_thermal_collector = var_fraction_of_surface_area_with_active_thermal_collector
        # alpha
        var_thermal_conversion_efficiency_input_mode_type = "Fixed"
        obj.thermal_conversion_efficiency_input_mode_type = var_thermal_conversion_efficiency_input_mode_type
        # real
        var_value_for_thermal_conversion_efficiency_if_fixed = 0.5
        obj.value_for_thermal_conversion_efficiency_if_fixed = var_value_for_thermal_conversion_efficiency_if_fixed
        # object-list
        var_thermal_conversion_efficiency_schedule_name = "object-list|Thermal Conversion Efficiency Schedule Name"
        obj.thermal_conversion_efficiency_schedule_name = var_thermal_conversion_efficiency_schedule_name
        # real
        var_front_surface_emittance = 0.5
        obj.front_surface_emittance = var_front_surface_emittance

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorperformancephotovoltaicthermalsimples[0].name, var_name)
        self.assertAlmostEqual(idf2.solarcollectorperformancephotovoltaicthermalsimples[0].fraction_of_surface_area_with_active_thermal_collector, var_fraction_of_surface_area_with_active_thermal_collector)
        self.assertEqual(idf2.solarcollectorperformancephotovoltaicthermalsimples[0].thermal_conversion_efficiency_input_mode_type, var_thermal_conversion_efficiency_input_mode_type)
        self.assertAlmostEqual(idf2.solarcollectorperformancephotovoltaicthermalsimples[0].value_for_thermal_conversion_efficiency_if_fixed, var_value_for_thermal_conversion_efficiency_if_fixed)
        self.assertEqual(idf2.solarcollectorperformancephotovoltaicthermalsimples[0].thermal_conversion_efficiency_schedule_name, var_thermal_conversion_efficiency_schedule_name)
        self.assertAlmostEqual(idf2.solarcollectorperformancephotovoltaicthermalsimples[0].front_surface_emittance, var_front_surface_emittance)