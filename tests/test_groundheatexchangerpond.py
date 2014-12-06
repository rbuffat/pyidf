import os
import tempfile
import unittest
import pyidf
from pyidf.condenser_equipment_and_heat_exchangers import GroundHeatExchangerPond
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestGroundHeatExchangerPond(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheatexchangerpond(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatExchangerPond()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_fluid_inlet_node_name = "node|Fluid Inlet Node Name"
        obj.fluid_inlet_node_name = var_fluid_inlet_node_name
        # node
        var_fluid_outlet_node_name = "node|Fluid Outlet Node Name"
        obj.fluid_outlet_node_name = var_fluid_outlet_node_name
        # real
        var_pond_depth = 0.0001
        obj.pond_depth = var_pond_depth
        # real
        var_pond_area = 0.0001
        obj.pond_area = var_pond_area
        # real
        var_hydronic_tubing_inside_diameter = 0.0001
        obj.hydronic_tubing_inside_diameter = var_hydronic_tubing_inside_diameter
        # real
        var_hydronic_tubing_outside_diameter = 0.0001
        obj.hydronic_tubing_outside_diameter = var_hydronic_tubing_outside_diameter
        # real
        var_hydronic_tubing_thermal_conductivity = 0.0001
        obj.hydronic_tubing_thermal_conductivity = var_hydronic_tubing_thermal_conductivity
        # real
        var_ground_thermal_conductivity = 0.0001
        obj.ground_thermal_conductivity = var_ground_thermal_conductivity
        # integer
        var_number_of_tubing_circuits = 1
        obj.number_of_tubing_circuits = var_number_of_tubing_circuits
        # real
        var_length_of_each_tubing_circuit = 0.0
        obj.length_of_each_tubing_circuit = var_length_of_each_tubing_circuit

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheatexchangerponds[0].name, var_name)
        self.assertEqual(idf2.groundheatexchangerponds[0].fluid_inlet_node_name, var_fluid_inlet_node_name)
        self.assertEqual(idf2.groundheatexchangerponds[0].fluid_outlet_node_name, var_fluid_outlet_node_name)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].pond_depth, var_pond_depth)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].pond_area, var_pond_area)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].hydronic_tubing_inside_diameter, var_hydronic_tubing_inside_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].hydronic_tubing_outside_diameter, var_hydronic_tubing_outside_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].hydronic_tubing_thermal_conductivity, var_hydronic_tubing_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].ground_thermal_conductivity, var_ground_thermal_conductivity)
        self.assertEqual(idf2.groundheatexchangerponds[0].number_of_tubing_circuits, var_number_of_tubing_circuits)
        self.assertAlmostEqual(idf2.groundheatexchangerponds[0].length_of_each_tubing_circuit, var_length_of_each_tubing_circuit)