import os
import tempfile
import unittest
import pyidf
from pyidf.coils import CoilCoolingWaterToAirHeatPumpEquationFit
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestCoilCoolingWaterToAirHeatPumpEquationFit(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_coilcoolingwatertoairheatpumpequationfit(self):

        pyidf.validation_level = ValidationLevel.error

        obj = CoilCoolingWaterToAirHeatPumpEquationFit()
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
        var_gross_rated_total_cooling_capacity = 0.0001
        obj.gross_rated_total_cooling_capacity = var_gross_rated_total_cooling_capacity
        # real
        var_gross_rated_sensible_cooling_capacity = 0.0001
        obj.gross_rated_sensible_cooling_capacity = var_gross_rated_sensible_cooling_capacity
        # real
        var_gross_rated_cooling_cop = 0.0001
        obj.gross_rated_cooling_cop = var_gross_rated_cooling_cop
        # real
        var_total_cooling_capacity_coefficient_1 = 11.11
        obj.total_cooling_capacity_coefficient_1 = var_total_cooling_capacity_coefficient_1
        # real
        var_total_cooling_capacity_coefficient_2 = 12.12
        obj.total_cooling_capacity_coefficient_2 = var_total_cooling_capacity_coefficient_2
        # real
        var_total_cooling_capacity_coefficient_3 = 13.13
        obj.total_cooling_capacity_coefficient_3 = var_total_cooling_capacity_coefficient_3
        # real
        var_total_cooling_capacity_coefficient_4 = 14.14
        obj.total_cooling_capacity_coefficient_4 = var_total_cooling_capacity_coefficient_4
        # real
        var_total_cooling_capacity_coefficient_5 = 15.15
        obj.total_cooling_capacity_coefficient_5 = var_total_cooling_capacity_coefficient_5
        # real
        var_sensible_cooling_capacity_coefficient_1 = 16.16
        obj.sensible_cooling_capacity_coefficient_1 = var_sensible_cooling_capacity_coefficient_1
        # real
        var_sensible_cooling_capacity_coefficient_2 = 17.17
        obj.sensible_cooling_capacity_coefficient_2 = var_sensible_cooling_capacity_coefficient_2
        # real
        var_sensible_cooling_capacity_coefficient_3 = 18.18
        obj.sensible_cooling_capacity_coefficient_3 = var_sensible_cooling_capacity_coefficient_3
        # real
        var_sensible_cooling_capacity_coefficient_4 = 19.19
        obj.sensible_cooling_capacity_coefficient_4 = var_sensible_cooling_capacity_coefficient_4
        # real
        var_sensible_cooling_capacity_coefficient_5 = 20.2
        obj.sensible_cooling_capacity_coefficient_5 = var_sensible_cooling_capacity_coefficient_5
        # real
        var_sensible_cooling_capacity_coefficient_6 = 21.21
        obj.sensible_cooling_capacity_coefficient_6 = var_sensible_cooling_capacity_coefficient_6
        # real
        var_cooling_power_consumption_coefficient_1 = 22.22
        obj.cooling_power_consumption_coefficient_1 = var_cooling_power_consumption_coefficient_1
        # real
        var_cooling_power_consumption_coefficient_2 = 23.23
        obj.cooling_power_consumption_coefficient_2 = var_cooling_power_consumption_coefficient_2
        # real
        var_cooling_power_consumption_coefficient_3 = 24.24
        obj.cooling_power_consumption_coefficient_3 = var_cooling_power_consumption_coefficient_3
        # real
        var_cooling_power_consumption_coefficient_4 = 25.25
        obj.cooling_power_consumption_coefficient_4 = var_cooling_power_consumption_coefficient_4
        # real
        var_cooling_power_consumption_coefficient_5 = 26.26
        obj.cooling_power_consumption_coefficient_5 = var_cooling_power_consumption_coefficient_5
        # real
        var_nominal_time_for_condensate_removal_to_begin = 1500.0
        obj.nominal_time_for_condensate_removal_to_begin = var_nominal_time_for_condensate_removal_to_begin
        # real
        var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = 2.5
        obj.ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity = var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].name, var_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].water_inlet_node_name, var_water_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].water_outlet_node_name, var_water_outlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].rated_air_flow_rate, var_rated_air_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].rated_water_flow_rate, var_rated_water_flow_rate)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].gross_rated_total_cooling_capacity, var_gross_rated_total_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].gross_rated_sensible_cooling_capacity, var_gross_rated_sensible_cooling_capacity)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].gross_rated_cooling_cop, var_gross_rated_cooling_cop)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].total_cooling_capacity_coefficient_1, var_total_cooling_capacity_coefficient_1)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].total_cooling_capacity_coefficient_2, var_total_cooling_capacity_coefficient_2)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].total_cooling_capacity_coefficient_3, var_total_cooling_capacity_coefficient_3)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].total_cooling_capacity_coefficient_4, var_total_cooling_capacity_coefficient_4)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].total_cooling_capacity_coefficient_5, var_total_cooling_capacity_coefficient_5)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].sensible_cooling_capacity_coefficient_1, var_sensible_cooling_capacity_coefficient_1)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].sensible_cooling_capacity_coefficient_2, var_sensible_cooling_capacity_coefficient_2)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].sensible_cooling_capacity_coefficient_3, var_sensible_cooling_capacity_coefficient_3)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].sensible_cooling_capacity_coefficient_4, var_sensible_cooling_capacity_coefficient_4)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].sensible_cooling_capacity_coefficient_5, var_sensible_cooling_capacity_coefficient_5)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].sensible_cooling_capacity_coefficient_6, var_sensible_cooling_capacity_coefficient_6)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].cooling_power_consumption_coefficient_1, var_cooling_power_consumption_coefficient_1)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].cooling_power_consumption_coefficient_2, var_cooling_power_consumption_coefficient_2)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].cooling_power_consumption_coefficient_3, var_cooling_power_consumption_coefficient_3)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].cooling_power_consumption_coefficient_4, var_cooling_power_consumption_coefficient_4)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].cooling_power_consumption_coefficient_5, var_cooling_power_consumption_coefficient_5)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].nominal_time_for_condensate_removal_to_begin, var_nominal_time_for_condensate_removal_to_begin)
        self.assertAlmostEqual(idf2.coilcoolingwatertoairheatpumpequationfits[0].ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity, var_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity)