import os
import tempfile
import unittest
import pyidf
from pyidf.solar_collectors import SolarCollectorFlatPlatePhotovoltaicThermal
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestSolarCollectorFlatPlatePhotovoltaicThermal(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_solarcollectorflatplatephotovoltaicthermal(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SolarCollectorFlatPlatePhotovoltaicThermal()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_surface_name = "object-list|Surface Name"
        obj.surface_name = var_surface_name
        # object-list
        var_photovoltaicthermal_model_performance_name = "object-list|Photovoltaic-Thermal Model Performance Name"
        obj.photovoltaicthermal_model_performance_name = var_photovoltaicthermal_model_performance_name
        # object-list
        var_photovoltaic_name = "object-list|Photovoltaic Name"
        obj.photovoltaic_name = var_photovoltaic_name
        # alpha
        var_thermal_working_fluid_type = "Water"
        obj.thermal_working_fluid_type = var_thermal_working_fluid_type
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
        # real
        var_design_flow_rate = 10.1
        obj.design_flow_rate = var_design_flow_rate

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].name, var_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].surface_name, var_surface_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].photovoltaicthermal_model_performance_name, var_photovoltaicthermal_model_performance_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].photovoltaic_name, var_photovoltaic_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].thermal_working_fluid_type, var_thermal_working_fluid_type)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.solarcollectorflatplatephotovoltaicthermals[0].design_flow_rate, var_design_flow_rate)