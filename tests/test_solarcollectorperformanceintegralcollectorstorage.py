import os
import tempfile
import unittest
import pyidf
from pyidf.solar_collectors import SolarCollectorPerformanceIntegralCollectorStorage
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSolarCollectorPerformanceIntegralCollectorStorage(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorperformanceintegralcollectorstorage(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorPerformanceIntegralCollectorStorage()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_ics_collector_type = "RectangularTank"
        obj.ics_collector_type = var_ics_collector_type
        # real
        var_gross_area = 0.0001
        obj.gross_area = var_gross_area
        # real
        var_collector_water_volume = 0.0001
        obj.collector_water_volume = var_collector_water_volume
        # real
        var_bottom_heat_loss_conductance = 0.0001
        obj.bottom_heat_loss_conductance = var_bottom_heat_loss_conductance
        # real
        var_side_heat_loss_conductance = 0.0001
        obj.side_heat_loss_conductance = var_side_heat_loss_conductance
        # real
        var_aspect_ratio = 0.75
        obj.aspect_ratio = var_aspect_ratio
        # real
        var_collector_side_height = 0.15
        obj.collector_side_height = var_collector_side_height
        # real
        var_thermal_mass_of_absorber_plate = 0.0
        obj.thermal_mass_of_absorber_plate = var_thermal_mass_of_absorber_plate
        # integer
        var_number_of_covers = 1
        obj.number_of_covers = var_number_of_covers
        # real
        var_cover_spacing = 0.10005
        obj.cover_spacing = var_cover_spacing
        # real
        var_refractive_index_of_outer_cover = 1.5
        obj.refractive_index_of_outer_cover = var_refractive_index_of_outer_cover
        # real
        var_extinction_coefficient_times_thickness_of_outer_cover = 0.0
        obj.extinction_coefficient_times_thickness_of_outer_cover = var_extinction_coefficient_times_thickness_of_outer_cover
        # real
        var_emissivity_of_outer_cover = 0.5
        obj.emissivity_of_outer_cover = var_emissivity_of_outer_cover
        # real
        var_refractive_index_of_inner_cover = 1.5
        obj.refractive_index_of_inner_cover = var_refractive_index_of_inner_cover
        # real
        var_extinction_coefficient_times_thickness_of_the_inner_cover = 0.0
        obj.extinction_coefficient_times_thickness_of_the_inner_cover = var_extinction_coefficient_times_thickness_of_the_inner_cover
        # real
        var_emmissivity_of_inner_cover = 0.5
        obj.emmissivity_of_inner_cover = var_emmissivity_of_inner_cover
        # real
        var_absorptance_of_absorber_plate = 0.5
        obj.absorptance_of_absorber_plate = var_absorptance_of_absorber_plate
        # real
        var_emissivity_of_absorber_plate = 0.5
        obj.emissivity_of_absorber_plate = var_emissivity_of_absorber_plate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].name, var_name)
        self.assertEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].ics_collector_type, var_ics_collector_type)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].gross_area, var_gross_area)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].collector_water_volume, var_collector_water_volume)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].bottom_heat_loss_conductance, var_bottom_heat_loss_conductance)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].side_heat_loss_conductance, var_side_heat_loss_conductance)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].aspect_ratio, var_aspect_ratio)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].collector_side_height, var_collector_side_height)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].thermal_mass_of_absorber_plate, var_thermal_mass_of_absorber_plate)
        self.assertEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].number_of_covers, var_number_of_covers)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].cover_spacing, var_cover_spacing)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].refractive_index_of_outer_cover, var_refractive_index_of_outer_cover)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].extinction_coefficient_times_thickness_of_outer_cover, var_extinction_coefficient_times_thickness_of_outer_cover)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].emissivity_of_outer_cover, var_emissivity_of_outer_cover)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].refractive_index_of_inner_cover, var_refractive_index_of_inner_cover)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].extinction_coefficient_times_thickness_of_the_inner_cover, var_extinction_coefficient_times_thickness_of_the_inner_cover)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].emmissivity_of_inner_cover, var_emmissivity_of_inner_cover)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].absorptance_of_absorber_plate, var_absorptance_of_absorber_plate)
        self.assertAlmostEqual(idf2.solarcollectorperformanceintegralcollectorstorages[0].emissivity_of_absorber_plate, var_emissivity_of_absorber_plate)