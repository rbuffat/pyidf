import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.coils import CoilHeatingWaterToAirHeatPumpEquationFit

log = logging.getLogger(__name__)

class TestCoilHeatingWaterToAirHeatPumpEquationFit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilheatingwatertoairheatpumpequationfit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilHeatingWaterToAirHeatPumpEquationFit()
        # alpha
        var_name = "Name"
        obj.name = var_name
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
        var_rated_air_flow_rate = 0.0001
        obj.rated_air_flow_rate = var_rated_air_flow_rate
        # real
        var_rated_water_flow_rate = 0.0001
        obj.rated_water_flow_rate = var_rated_water_flow_rate
        # real
        var_gross_rated_heating_capacity = 0.0001
        obj.gross_rated_heating_capacity = var_gross_rated_heating_capacity
        # real
        var_gross_rated_heating_cop = 0.0001
        obj.gross_rated_heating_cop = var_gross_rated_heating_cop
        # real
        var_heating_capacity_coefficient_1 = 10.1
        obj.heating_capacity_coefficient_1 = var_heating_capacity_coefficient_1
        # real
        var_heating_capacity_coefficient_2 = 11.11
        obj.heating_capacity_coefficient_2 = var_heating_capacity_coefficient_2
        # real
        var_heating_capacity_coefficient_3 = 12.12
        obj.heating_capacity_coefficient_3 = var_heating_capacity_coefficient_3
        # real
        var_heating_capacity_coefficient_4 = 13.13
        obj.heating_capacity_coefficient_4 = var_heating_capacity_coefficient_4
        # real
        var_heating_capacity_coefficient_5 = 14.14
        obj.heating_capacity_coefficient_5 = var_heating_capacity_coefficient_5
        # real
        var_heating_power_consumption_coefficient_1 = 15.15
        obj.heating_power_consumption_coefficient_1 = var_heating_power_consumption_coefficient_1
        # real
        var_heating_power_consumption_coefficient_2 = 16.16
        obj.heating_power_consumption_coefficient_2 = var_heating_power_consumption_coefficient_2
        # real
        var_heating_power_consumption_coefficient_3 = 17.17
        obj.heating_power_consumption_coefficient_3 = var_heating_power_consumption_coefficient_3
        # real
        var_heating_power_consumption_coefficient_4 = 18.18
        obj.heating_power_consumption_coefficient_4 = var_heating_power_consumption_coefficient_4
        # real
        var_heating_power_consumption_coefficient_5 = 19.19
        obj.heating_power_consumption_coefficient_5 = var_heating_power_consumption_coefficient_5

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].name, var_name)
        self.assertEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].rated_water_flow_rate, var_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].gross_rated_heating_capacity, var_gross_rated_heating_capacity)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].gross_rated_heating_cop, var_gross_rated_heating_cop)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_capacity_coefficient_1, var_heating_capacity_coefficient_1)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_capacity_coefficient_2, var_heating_capacity_coefficient_2)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_capacity_coefficient_3, var_heating_capacity_coefficient_3)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_capacity_coefficient_4, var_heating_capacity_coefficient_4)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_capacity_coefficient_5, var_heating_capacity_coefficient_5)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_power_consumption_coefficient_1, var_heating_power_consumption_coefficient_1)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_power_consumption_coefficient_2, var_heating_power_consumption_coefficient_2)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_power_consumption_coefficient_3, var_heating_power_consumption_coefficient_3)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_power_consumption_coefficient_4, var_heating_power_consumption_coefficient_4)
        self.assertAlmostEqual(idf2.coilheatingwatertoairheatpumpequationfits[0].heating_power_consumption_coefficient_5, var_heating_power_consumption_coefficient_5)