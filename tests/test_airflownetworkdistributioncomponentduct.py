import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkDistributionComponentDuct
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkDistributionComponentDuct(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkdistributioncomponentduct(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkDistributionComponentDuct()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_duct_length = 0.0001
        obj.duct_length = var_duct_length
        # real
        var_hydraulic_diameter = 0.0001
        obj.hydraulic_diameter = var_hydraulic_diameter
        # real
        var_cross_section_area = 0.0001
        obj.cross_section_area = var_cross_section_area
        # real
        var_surface_roughness = 0.0001
        obj.surface_roughness = var_surface_roughness
        # real
        var_coefficient_for_local_dynamic_loss_due_to_fitting = 0.0
        obj.coefficient_for_local_dynamic_loss_due_to_fitting = var_coefficient_for_local_dynamic_loss_due_to_fitting
        # real
        var_overall_heat_transmittance_coefficient_ufactor_from_air_to_air = 0.0001
        obj.overall_heat_transmittance_coefficient_ufactor_from_air_to_air = var_overall_heat_transmittance_coefficient_ufactor_from_air_to_air
        # real
        var_overall_moisture_transmittance_coefficient_from_air_to_air = 0.0001
        obj.overall_moisture_transmittance_coefficient_from_air_to_air = var_overall_moisture_transmittance_coefficient_from_air_to_air

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkdistributioncomponentducts[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].duct_length, var_duct_length)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].hydraulic_diameter, var_hydraulic_diameter)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].cross_section_area, var_cross_section_area)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].surface_roughness, var_surface_roughness)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].coefficient_for_local_dynamic_loss_due_to_fitting, var_coefficient_for_local_dynamic_loss_due_to_fitting)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].overall_heat_transmittance_coefficient_ufactor_from_air_to_air, var_overall_heat_transmittance_coefficient_ufactor_from_air_to_air)
        self.assertAlmostEqual(idf2.airflownetworkdistributioncomponentducts[0].overall_moisture_transmittance_coefficient_from_air_to_air, var_overall_moisture_transmittance_coefficient_from_air_to_air)