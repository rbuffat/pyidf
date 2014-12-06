import os
import tempfile
import unittest
import pyidf
from pyidf.natural_ventilation_and_duct_leakage import AirflowNetworkMultiZoneComponentDetailedOpening
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestAirflowNetworkMultiZoneComponentDetailedOpening(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airflownetworkmultizonecomponentdetailedopening(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirflowNetworkMultiZoneComponentDetailedOpening()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_air_mass_flow_coefficient_when_opening_is_closed = 0.0001
        obj.air_mass_flow_coefficient_when_opening_is_closed = var_air_mass_flow_coefficient_when_opening_is_closed
        # real
        var_air_mass_flow_exponent_when_opening_is_closed = 0.75
        obj.air_mass_flow_exponent_when_opening_is_closed = var_air_mass_flow_exponent_when_opening_is_closed
        # alpha
        var_type_of_rectanguler_large_vertical_opening_lvo = "NonPivoted"
        obj.type_of_rectanguler_large_vertical_opening_lvo = var_type_of_rectanguler_large_vertical_opening_lvo
        # real
        var_extra_crack_length_or_height_of_pivoting_axis = 0.0
        obj.extra_crack_length_or_height_of_pivoting_axis = var_extra_crack_length_or_height_of_pivoting_axis
        # integer
        var_number_of_sets_of_opening_factor_data = 3
        obj.number_of_sets_of_opening_factor_data = var_number_of_sets_of_opening_factor_data
        # real
        var_opening_factor_1 = 0.0
        obj.opening_factor_1 = var_opening_factor_1
        # real
        var_discharge_coefficient_for_opening_factor_1 = 0.50005
        obj.discharge_coefficient_for_opening_factor_1 = var_discharge_coefficient_for_opening_factor_1
        # real
        var_width_factor_for_opening_factor_1 = 0.5
        obj.width_factor_for_opening_factor_1 = var_width_factor_for_opening_factor_1
        # real
        var_height_factor_for_opening_factor_1 = 0.5
        obj.height_factor_for_opening_factor_1 = var_height_factor_for_opening_factor_1
        # real
        var_start_height_factor_for_opening_factor_1 = 0.5
        obj.start_height_factor_for_opening_factor_1 = var_start_height_factor_for_opening_factor_1
        # real
        var_opening_factor_2 = 0.50005
        obj.opening_factor_2 = var_opening_factor_2
        # real
        var_discharge_coefficient_for_opening_factor_2 = 0.50005
        obj.discharge_coefficient_for_opening_factor_2 = var_discharge_coefficient_for_opening_factor_2
        # real
        var_width_factor_for_opening_factor_2 = 0.50005
        obj.width_factor_for_opening_factor_2 = var_width_factor_for_opening_factor_2
        # real
        var_height_factor_for_opening_factor_2 = 0.50005
        obj.height_factor_for_opening_factor_2 = var_height_factor_for_opening_factor_2
        # real
        var_start_height_factor_for_opening_factor_2 = 0.49995
        obj.start_height_factor_for_opening_factor_2 = var_start_height_factor_for_opening_factor_2
        # real
        var_opening_factor_3 = 0.5
        obj.opening_factor_3 = var_opening_factor_3
        # real
        var_discharge_coefficient_for_opening_factor_3 = 0.5
        obj.discharge_coefficient_for_opening_factor_3 = var_discharge_coefficient_for_opening_factor_3
        # real
        var_width_factor_for_opening_factor_3 = 0.5
        obj.width_factor_for_opening_factor_3 = var_width_factor_for_opening_factor_3
        # real
        var_height_factor_for_opening_factor_3 = 0.5
        obj.height_factor_for_opening_factor_3 = var_height_factor_for_opening_factor_3
        # real
        var_start_height_factor_for_opening_factor_3 = 0.5
        obj.start_height_factor_for_opening_factor_3 = var_start_height_factor_for_opening_factor_3
        # real
        var_opening_factor_4 = 0.5
        obj.opening_factor_4 = var_opening_factor_4
        # real
        var_discharge_coefficient_for_opening_factor_4 = 0.5
        obj.discharge_coefficient_for_opening_factor_4 = var_discharge_coefficient_for_opening_factor_4
        # real
        var_width_factor_for_opening_factor_4 = 0.5
        obj.width_factor_for_opening_factor_4 = var_width_factor_for_opening_factor_4
        # real
        var_height_factor_for_opening_factor_4 = 0.5
        obj.height_factor_for_opening_factor_4 = var_height_factor_for_opening_factor_4
        # real
        var_start_height_factor_for_opening_factor_4 = 0.5
        obj.start_height_factor_for_opening_factor_4 = var_start_height_factor_for_opening_factor_4

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].name, var_name)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].air_mass_flow_coefficient_when_opening_is_closed, var_air_mass_flow_coefficient_when_opening_is_closed)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].air_mass_flow_exponent_when_opening_is_closed, var_air_mass_flow_exponent_when_opening_is_closed)
        self.assertEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].type_of_rectanguler_large_vertical_opening_lvo, var_type_of_rectanguler_large_vertical_opening_lvo)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].extra_crack_length_or_height_of_pivoting_axis, var_extra_crack_length_or_height_of_pivoting_axis)
        self.assertEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].number_of_sets_of_opening_factor_data, var_number_of_sets_of_opening_factor_data)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].opening_factor_1, var_opening_factor_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].discharge_coefficient_for_opening_factor_1, var_discharge_coefficient_for_opening_factor_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].width_factor_for_opening_factor_1, var_width_factor_for_opening_factor_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].height_factor_for_opening_factor_1, var_height_factor_for_opening_factor_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].start_height_factor_for_opening_factor_1, var_start_height_factor_for_opening_factor_1)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].opening_factor_2, var_opening_factor_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].discharge_coefficient_for_opening_factor_2, var_discharge_coefficient_for_opening_factor_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].width_factor_for_opening_factor_2, var_width_factor_for_opening_factor_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].height_factor_for_opening_factor_2, var_height_factor_for_opening_factor_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].start_height_factor_for_opening_factor_2, var_start_height_factor_for_opening_factor_2)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].opening_factor_3, var_opening_factor_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].discharge_coefficient_for_opening_factor_3, var_discharge_coefficient_for_opening_factor_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].width_factor_for_opening_factor_3, var_width_factor_for_opening_factor_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].height_factor_for_opening_factor_3, var_height_factor_for_opening_factor_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].start_height_factor_for_opening_factor_3, var_start_height_factor_for_opening_factor_3)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].opening_factor_4, var_opening_factor_4)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].discharge_coefficient_for_opening_factor_4, var_discharge_coefficient_for_opening_factor_4)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].width_factor_for_opening_factor_4, var_width_factor_for_opening_factor_4)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].height_factor_for_opening_factor_4, var_height_factor_for_opening_factor_4)
        self.assertAlmostEqual(idf2.airflownetworkmultizonecomponentdetailedopenings[0].start_height_factor_for_opening_factor_4, var_start_height_factor_for_opening_factor_4)