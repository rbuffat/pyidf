import os
import tempfile
import unittest
import pyidf
from pyidf.surface_construction_elements import ConstructionComplexFenestrationState
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestConstructionComplexFenestrationState(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_constructioncomplexfenestrationstate(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ConstructionComplexFenestrationState()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_basis_type = "LBNLWINDOW"
        obj.basis_type = var_basis_type
        # alpha
        var_basis_symmetry_type = "Axisymmetric"
        obj.basis_symmetry_type = var_basis_symmetry_type
        # object-list
        var_window_thermal_model = "object-list|Window Thermal Model"
        obj.window_thermal_model = var_window_thermal_model
        # object-list
        var_basis_matrix_name = "object-list|Basis Matrix Name"
        obj.basis_matrix_name = var_basis_matrix_name
        # object-list
        var_solar_optical_complex_front_transmittance_matrix_name = "object-list|Solar Optical Complex Front Transmittance Matrix Name"
        obj.solar_optical_complex_front_transmittance_matrix_name = var_solar_optical_complex_front_transmittance_matrix_name
        # object-list
        var_solar_optical_complex_back_reflectance_matrix_name = "object-list|Solar Optical Complex Back Reflectance Matrix Name"
        obj.solar_optical_complex_back_reflectance_matrix_name = var_solar_optical_complex_back_reflectance_matrix_name
        # object-list
        var_visible_optical_complex_front_transmittance_matrix_name = "object-list|Visible Optical Complex Front Transmittance Matrix Name"
        obj.visible_optical_complex_front_transmittance_matrix_name = var_visible_optical_complex_front_transmittance_matrix_name
        # object-list
        var_visible_optical_complex_back_transmittance_matrix_name = "object-list|Visible Optical Complex Back Transmittance Matrix Name"
        obj.visible_optical_complex_back_transmittance_matrix_name = var_visible_optical_complex_back_transmittance_matrix_name
        # object-list
        var_outside_layer_name = "object-list|Outside Layer Name"
        obj.outside_layer_name = var_outside_layer_name
        # object-list
        var_outside_layer_directional_front_absoptance_matrix_name = "object-list|Outside Layer Directional Front Absoptance Matrix Name"
        obj.outside_layer_directional_front_absoptance_matrix_name = var_outside_layer_directional_front_absoptance_matrix_name
        # object-list
        var_outside_layer_directional_back_absoptance_matrix_name = "object-list|Outside Layer Directional Back Absoptance Matrix Name"
        obj.outside_layer_directional_back_absoptance_matrix_name = var_outside_layer_directional_back_absoptance_matrix_name
        # object-list
        var_gap_1_name = "object-list|Gap 1 Name"
        obj.gap_1_name = var_gap_1_name
        # object-list
        var_cfs_gap_1_directional_front_absoptance_matrix_name = "object-list|CFS Gap 1 Directional Front Absoptance Matrix Name"
        obj.cfs_gap_1_directional_front_absoptance_matrix_name = var_cfs_gap_1_directional_front_absoptance_matrix_name
        # object-list
        var_cfs_gap_1_directional_back_absoptance_matrix_name = "object-list|CFS Gap 1 Directional Back Absoptance Matrix Name"
        obj.cfs_gap_1_directional_back_absoptance_matrix_name = var_cfs_gap_1_directional_back_absoptance_matrix_name
        # object-list
        var_layer_2_name = "object-list|Layer 2 Name"
        obj.layer_2_name = var_layer_2_name
        # object-list
        var_layer_2_directional_front_absoptance_matrix_name = "object-list|Layer 2 Directional Front Absoptance Matrix Name"
        obj.layer_2_directional_front_absoptance_matrix_name = var_layer_2_directional_front_absoptance_matrix_name
        # object-list
        var_layer_2_directional_back_absoptance_matrix_name = "object-list|Layer 2 Directional Back Absoptance Matrix Name"
        obj.layer_2_directional_back_absoptance_matrix_name = var_layer_2_directional_back_absoptance_matrix_name
        # object-list
        var_gap_2_name = "object-list|Gap 2 Name"
        obj.gap_2_name = var_gap_2_name
        # object-list
        var_gap_2_directional_front_absoptance_matrix_name = "object-list|Gap 2 Directional Front Absoptance Matrix Name"
        obj.gap_2_directional_front_absoptance_matrix_name = var_gap_2_directional_front_absoptance_matrix_name
        # object-list
        var_gap_2_directional_back_absoptance_matrix_name = "object-list|Gap 2 Directional Back Absoptance Matrix Name"
        obj.gap_2_directional_back_absoptance_matrix_name = var_gap_2_directional_back_absoptance_matrix_name
        # object-list
        var_layer_3_material = "object-list|Layer 3 Material"
        obj.layer_3_material = var_layer_3_material
        # object-list
        var_layer_3_directional_front_absoptance_matrix_name = "object-list|Layer 3 Directional Front Absoptance Matrix Name"
        obj.layer_3_directional_front_absoptance_matrix_name = var_layer_3_directional_front_absoptance_matrix_name
        # object-list
        var_layer_3_directional_back_absoptance_matrix_name = "object-list|Layer 3 Directional Back Absoptance Matrix Name"
        obj.layer_3_directional_back_absoptance_matrix_name = var_layer_3_directional_back_absoptance_matrix_name
        # object-list
        var_gap_3_name = "object-list|Gap 3 Name"
        obj.gap_3_name = var_gap_3_name
        # object-list
        var_gap_3_directional_front_absoptance_matrix_name = "object-list|Gap 3 Directional Front Absoptance Matrix Name"
        obj.gap_3_directional_front_absoptance_matrix_name = var_gap_3_directional_front_absoptance_matrix_name
        # object-list
        var_gap_3_directional_back_absoptance_matrix_name = "object-list|Gap 3 Directional Back Absoptance Matrix Name"
        obj.gap_3_directional_back_absoptance_matrix_name = var_gap_3_directional_back_absoptance_matrix_name
        # object-list
        var_layer_4_name = "object-list|Layer 4 Name"
        obj.layer_4_name = var_layer_4_name
        # object-list
        var_layer_4_directional_front_absoptance_matrix_name = "object-list|Layer 4 Directional Front Absoptance Matrix Name"
        obj.layer_4_directional_front_absoptance_matrix_name = var_layer_4_directional_front_absoptance_matrix_name
        # object-list
        var_layer_4_directional_back_absoptance_matrix_name = "object-list|Layer 4 Directional Back Absoptance Matrix Name"
        obj.layer_4_directional_back_absoptance_matrix_name = var_layer_4_directional_back_absoptance_matrix_name
        # object-list
        var_gap_4_name = "object-list|Gap 4 Name"
        obj.gap_4_name = var_gap_4_name
        # object-list
        var_gap_4_directional_front_absoptance_matrix_name = "object-list|Gap 4 Directional Front Absoptance Matrix Name"
        obj.gap_4_directional_front_absoptance_matrix_name = var_gap_4_directional_front_absoptance_matrix_name
        # object-list
        var_gap_4_directional_back_absoptance_matrix_name = "object-list|Gap 4 Directional Back Absoptance Matrix Name"
        obj.gap_4_directional_back_absoptance_matrix_name = var_gap_4_directional_back_absoptance_matrix_name
        # object-list
        var_layer_5_name = "object-list|Layer 5 Name"
        obj.layer_5_name = var_layer_5_name
        # object-list
        var_layer_5_directional_front_absoptance_matrix_name = "object-list|Layer 5 Directional Front Absoptance Matrix Name"
        obj.layer_5_directional_front_absoptance_matrix_name = var_layer_5_directional_front_absoptance_matrix_name
        # alpha
        var_layer_5_directional_back_absoptance_matrix_name = "Layer 5 Directional Back Absoptance Matrix Name"
        obj.layer_5_directional_back_absoptance_matrix_name = var_layer_5_directional_back_absoptance_matrix_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].name, var_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].basis_type, var_basis_type)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].basis_symmetry_type, var_basis_symmetry_type)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].window_thermal_model, var_window_thermal_model)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].basis_matrix_name, var_basis_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].solar_optical_complex_front_transmittance_matrix_name, var_solar_optical_complex_front_transmittance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].solar_optical_complex_back_reflectance_matrix_name, var_solar_optical_complex_back_reflectance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].visible_optical_complex_front_transmittance_matrix_name, var_visible_optical_complex_front_transmittance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].visible_optical_complex_back_transmittance_matrix_name, var_visible_optical_complex_back_transmittance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].outside_layer_name, var_outside_layer_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].outside_layer_directional_front_absoptance_matrix_name, var_outside_layer_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].outside_layer_directional_back_absoptance_matrix_name, var_outside_layer_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_1_name, var_gap_1_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].cfs_gap_1_directional_front_absoptance_matrix_name, var_cfs_gap_1_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].cfs_gap_1_directional_back_absoptance_matrix_name, var_cfs_gap_1_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_2_name, var_layer_2_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_2_directional_front_absoptance_matrix_name, var_layer_2_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_2_directional_back_absoptance_matrix_name, var_layer_2_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_2_name, var_gap_2_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_2_directional_front_absoptance_matrix_name, var_gap_2_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_2_directional_back_absoptance_matrix_name, var_gap_2_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_3_material, var_layer_3_material)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_3_directional_front_absoptance_matrix_name, var_layer_3_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_3_directional_back_absoptance_matrix_name, var_layer_3_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_3_name, var_gap_3_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_3_directional_front_absoptance_matrix_name, var_gap_3_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_3_directional_back_absoptance_matrix_name, var_gap_3_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_4_name, var_layer_4_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_4_directional_front_absoptance_matrix_name, var_layer_4_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_4_directional_back_absoptance_matrix_name, var_layer_4_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_4_name, var_gap_4_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_4_directional_front_absoptance_matrix_name, var_gap_4_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].gap_4_directional_back_absoptance_matrix_name, var_gap_4_directional_back_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_5_name, var_layer_5_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_5_directional_front_absoptance_matrix_name, var_layer_5_directional_front_absoptance_matrix_name)
        self.assertEqual(idf2.constructioncomplexfenestrationstates[0].layer_5_directional_back_absoptance_matrix_name, var_layer_5_directional_back_absoptance_matrix_name)