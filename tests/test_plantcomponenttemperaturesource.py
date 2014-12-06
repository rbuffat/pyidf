import os
import tempfile
import unittest
import pyidf
from pyidf.plant_heating_and_cooling_equipment import PlantComponentTemperatureSource
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPlantComponentTemperatureSource(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_plantcomponenttemperaturesource(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PlantComponentTemperatureSource()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node = "node|Inlet Node"
        obj.inlet_node = var_inlet_node
        # node
        var_outlet_node = "node|Outlet Node"
        obj.outlet_node = var_outlet_node
        # real
        var_design_volume_flow_rate = 0.0001
        obj.design_volume_flow_rate = var_design_volume_flow_rate
        # alpha
        var_temperature_specification_type = "Constant"
        obj.temperature_specification_type = var_temperature_specification_type
        # real
        var_source_temperature = 6.6
        obj.source_temperature = var_source_temperature
        # object-list
        var_source_temperature_schedule_name = "object-list|Source Temperature Schedule Name"
        obj.source_temperature_schedule_name = var_source_temperature_schedule_name

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.plantcomponenttemperaturesources[0].name, var_name)
        self.assertEqual(idf2.plantcomponenttemperaturesources[0].inlet_node, var_inlet_node)
        self.assertEqual(idf2.plantcomponenttemperaturesources[0].outlet_node, var_outlet_node)
        self.assertAlmostEqual(idf2.plantcomponenttemperaturesources[0].design_volume_flow_rate, var_design_volume_flow_rate)
        self.assertEqual(idf2.plantcomponenttemperaturesources[0].temperature_specification_type, var_temperature_specification_type)
        self.assertAlmostEqual(idf2.plantcomponenttemperaturesources[0].source_temperature, var_source_temperature)
        self.assertEqual(idf2.plantcomponenttemperaturesources[0].source_temperature_schedule_name, var_source_temperature_schedule_name)