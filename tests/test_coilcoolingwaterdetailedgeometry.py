import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilCoolingWaterDetailedGeometry
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilCoolingWaterDetailedGeometry(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingwaterdetailedgeometry(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingWaterDetailedGeometry()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_maximum_water_flow_rate = 3.3
        obj.maximum_water_flow_rate = var_maximum_water_flow_rate
        # real
        var_tube_outside_surface_area = 4.4
        obj.tube_outside_surface_area = var_tube_outside_surface_area
        # real
        var_total_tube_inside_area = 0.0001
        obj.total_tube_inside_area = var_total_tube_inside_area
        # real
        var_fin_surface_area = 6.6
        obj.fin_surface_area = var_fin_surface_area
        # real
        var_minimum_airflow_area = 0.0001
        obj.minimum_airflow_area = var_minimum_airflow_area
        # real
        var_coil_depth = 0.0001
        obj.coil_depth = var_coil_depth
        # real
        var_fin_diameter = 0.0001
        obj.fin_diameter = var_fin_diameter
        # real
        var_fin_thickness = 0.0001
        obj.fin_thickness = var_fin_thickness
        # real
        var_tube_inside_diameter = 0.0001
        obj.tube_inside_diameter = var_tube_inside_diameter
        # real
        var_tube_outside_diameter = 0.0001
        obj.tube_outside_diameter = var_tube_outside_diameter
        # real
        var_tube_thermal_conductivity = 1.0
        obj.tube_thermal_conductivity = var_tube_thermal_conductivity
        # real
        var_fin_thermal_conductivity = 1.0
        obj.fin_thermal_conductivity = var_fin_thermal_conductivity
        # real
        var_fin_spacing = 0.0001
        obj.fin_spacing = var_fin_spacing
        # real
        var_tube_depth_spacing = 0.0001
        obj.tube_depth_spacing = var_tube_depth_spacing
        # real
        var_number_of_tube_rows = 0.0001
        obj.number_of_tube_rows = var_number_of_tube_rows
        # real
        var_number_of_tubes_per_row = 0.0001
        obj.number_of_tubes_per_row = var_number_of_tubes_per_row
        # node
        var_water_inlet_node_name = "node|Water Inlet Node Name"
        obj.water_inlet_node_name = var_water_inlet_node_name
        # node
        var_water_outlet_node_name = "node|Water Outlet Node Name"
        obj.water_outlet_node_name = var_water_outlet_node_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # object-list
        var_condensate_collection_water_storage_tank_name = "object-list|Condensate Collection Water Storage Tank Name"
        obj.condensate_collection_water_storage_tank_name = var_condensate_collection_water_storage_tank_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].name, var_name)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].maximum_water_flow_rate, var_maximum_water_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].tube_outside_surface_area, var_tube_outside_surface_area)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].total_tube_inside_area, var_total_tube_inside_area)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].fin_surface_area, var_fin_surface_area)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].minimum_airflow_area, var_minimum_airflow_area)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].coil_depth, var_coil_depth)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].fin_diameter, var_fin_diameter)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].fin_thickness, var_fin_thickness)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].tube_inside_diameter, var_tube_inside_diameter)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].tube_outside_diameter, var_tube_outside_diameter)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].tube_thermal_conductivity, var_tube_thermal_conductivity)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].fin_thermal_conductivity, var_fin_thermal_conductivity)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].fin_spacing, var_fin_spacing)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].tube_depth_spacing, var_tube_depth_spacing)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].number_of_tube_rows, var_number_of_tube_rows)
        self.assertAlmostEqual(idf2.coilcoolingwaterdetailedgeometrys[0].number_of_tubes_per_row, var_number_of_tubes_per_row)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwaterdetailedgeometrys[0].condensate_collection_water_storage_tank_name, var_condensate_collection_water_storage_tank_name)