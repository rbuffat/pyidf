import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import ElectricLoadCenterTransformer
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestElectricLoadCenterTransformer(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_electricloadcentertransformer(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ElectricLoadCenterTransformer()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_transformer_usage = "PowerInFromGrid"
        obj.transformer_usage = var_transformer_usage
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # real
        var_radiative_fraction = 0.5
        obj.radiative_fraction = var_radiative_fraction
        # real
        var_rated_capacity = 0.0
        obj.rated_capacity = var_rated_capacity
        # integer
        var_phase = 1
        obj.phase = var_phase
        # alpha
        var_conductor_material = "Copper"
        obj.conductor_material = var_conductor_material
        # real
        var_full_load_temperature_rise = 115.0
        obj.full_load_temperature_rise = var_full_load_temperature_rise
        # real
        var_fraction_of_eddy_current_losses = 0.5
        obj.fraction_of_eddy_current_losses = var_fraction_of_eddy_current_losses
        # alpha
        var_performance_input_method = "RatedLosses"
        obj.performance_input_method = var_performance_input_method
        # real
        var_rated_no_load_loss = 0.0001
        obj.rated_no_load_loss = var_rated_no_load_loss
        # real
        var_rated_load_loss = 0.0
        obj.rated_load_loss = var_rated_load_loss
        # real
        var_nameplate_efficiency = 0.50005
        obj.nameplate_efficiency = var_nameplate_efficiency
        # real
        var_per_unit_load_for_nameplate_efficiency = 0.50005
        obj.per_unit_load_for_nameplate_efficiency = var_per_unit_load_for_nameplate_efficiency
        # real
        var_reference_temperature_for_nameplate_efficiency = 85.0
        obj.reference_temperature_for_nameplate_efficiency = var_reference_temperature_for_nameplate_efficiency
        # real
        var_per_unit_load_for_maximum_efficiency = 0.50005
        obj.per_unit_load_for_maximum_efficiency = var_per_unit_load_for_maximum_efficiency
        # alpha
        var_consider_transformer_loss_for_utility_cost = "Yes"
        obj.consider_transformer_loss_for_utility_cost = var_consider_transformer_loss_for_utility_cost
        paras = []
        var_meter_1_name = "external-list|Meter 1 Name"
        paras.append(var_meter_1_name)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.electricloadcentertransformers[0].name, var_name)
        self.assertEqual(idf2.electricloadcentertransformers[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.electricloadcentertransformers[0].transformer_usage, var_transformer_usage)
        self.assertEqual(idf2.electricloadcentertransformers[0].zone_name, var_zone_name)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].radiative_fraction, var_radiative_fraction)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].rated_capacity, var_rated_capacity)
        self.assertEqual(idf2.electricloadcentertransformers[0].phase, var_phase)
        self.assertEqual(idf2.electricloadcentertransformers[0].conductor_material, var_conductor_material)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].full_load_temperature_rise, var_full_load_temperature_rise)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].fraction_of_eddy_current_losses, var_fraction_of_eddy_current_losses)
        self.assertEqual(idf2.electricloadcentertransformers[0].performance_input_method, var_performance_input_method)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].rated_no_load_loss, var_rated_no_load_loss)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].rated_load_loss, var_rated_load_loss)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].nameplate_efficiency, var_nameplate_efficiency)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].per_unit_load_for_nameplate_efficiency, var_per_unit_load_for_nameplate_efficiency)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].reference_temperature_for_nameplate_efficiency, var_reference_temperature_for_nameplate_efficiency)
        self.assertAlmostEqual(idf2.electricloadcentertransformers[0].per_unit_load_for_maximum_efficiency, var_per_unit_load_for_maximum_efficiency)
        self.assertEqual(idf2.electricloadcentertransformers[0].consider_transformer_loss_for_utility_cost, var_consider_transformer_loss_for_utility_cost)
        index = obj.extensible_field_index("Meter 1 Name")
        self.assertEqual(idf2.electricloadcentertransformers[0].extensibles[0][index], var_meter_1_name)