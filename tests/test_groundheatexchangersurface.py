import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import GroundHeatExchangerSurface

log = logging.getLogger(__name__)

class TestGroundHeatExchangerSurface(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheatexchangersurface(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatExchangerSurface()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_construction_name = "object-list|Construction Name"
        obj.construction_name = var_construction_name
        # node
        var_fluid_inlet_node_name = "node|Fluid Inlet Node Name"
        obj.fluid_inlet_node_name = var_fluid_inlet_node_name
        # node
        var_fluid_outlet_node_name = "node|Fluid Outlet Node Name"
        obj.fluid_outlet_node_name = var_fluid_outlet_node_name
        # real
        var_hydronic_tubing_inside_diameter = 0.0001
        obj.hydronic_tubing_inside_diameter = var_hydronic_tubing_inside_diameter
        # integer
        var_number_of_tubing_circuits = 1
        obj.number_of_tubing_circuits = var_number_of_tubing_circuits
        # real
        var_hydronic_tube_spacing = 0.0001
        obj.hydronic_tube_spacing = var_hydronic_tube_spacing
        # real
        var_surface_length = 0.0001
        obj.surface_length = var_surface_length
        # real
        var_surface_width = 0.0001
        obj.surface_width = var_surface_width
        # alpha
        var_lower_surface_environment = "Ground"
        obj.lower_surface_environment = var_lower_surface_environment

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheatexchangersurfaces[0].name, var_name)
        self.assertEqual(idf2.groundheatexchangersurfaces[0].construction_name, var_construction_name)
        self.assertEqual(idf2.groundheatexchangersurfaces[0].fluid_inlet_node_name, var_fluid_inlet_node_name)
        self.assertEqual(idf2.groundheatexchangersurfaces[0].fluid_outlet_node_name, var_fluid_outlet_node_name)
        self.assertAlmostEqual(idf2.groundheatexchangersurfaces[0].hydronic_tubing_inside_diameter, var_hydronic_tubing_inside_diameter)
        self.assertEqual(idf2.groundheatexchangersurfaces[0].number_of_tubing_circuits, var_number_of_tubing_circuits)
        self.assertAlmostEqual(idf2.groundheatexchangersurfaces[0].hydronic_tube_spacing, var_hydronic_tube_spacing)
        self.assertAlmostEqual(idf2.groundheatexchangersurfaces[0].surface_length, var_surface_length)
        self.assertAlmostEqual(idf2.groundheatexchangersurfaces[0].surface_width, var_surface_width)
        self.assertEqual(idf2.groundheatexchangersurfaces[0].lower_surface_environment, var_lower_surface_environment)