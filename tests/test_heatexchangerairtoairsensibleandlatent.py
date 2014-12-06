import os
import tempfile
import unittest
import pyidf
from pyidf.heat_recovery import HeatExchangerAirToAirSensibleAndLatent
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestHeatExchangerAirToAirSensibleAndLatent(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_heatexchangerairtoairsensibleandlatent(self):

        pyidf.validation_level = ValidationLevel.error

        obj = HeatExchangerAirToAirSensibleAndLatent()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # real
        var_nominal_supply_air_flow_rate = 0.0001
        obj.nominal_supply_air_flow_rate = var_nominal_supply_air_flow_rate
        # real
        var_sensible_effectiveness_at_100_heating_air_flow = 0.5
        obj.sensible_effectiveness_at_100_heating_air_flow = var_sensible_effectiveness_at_100_heating_air_flow
        # real
        var_latent_effectiveness_at_100_heating_air_flow = 0.5
        obj.latent_effectiveness_at_100_heating_air_flow = var_latent_effectiveness_at_100_heating_air_flow
        # real
        var_sensible_effectiveness_at_75_heating_air_flow = 0.5
        obj.sensible_effectiveness_at_75_heating_air_flow = var_sensible_effectiveness_at_75_heating_air_flow
        # real
        var_latent_effectiveness_at_75_heating_air_flow = 0.5
        obj.latent_effectiveness_at_75_heating_air_flow = var_latent_effectiveness_at_75_heating_air_flow
        # real
        var_sensible_effectiveness_at_100_cooling_air_flow = 0.5
        obj.sensible_effectiveness_at_100_cooling_air_flow = var_sensible_effectiveness_at_100_cooling_air_flow
        # real
        var_latent_effectiveness_at_100_cooling_air_flow = 0.5
        obj.latent_effectiveness_at_100_cooling_air_flow = var_latent_effectiveness_at_100_cooling_air_flow
        # real
        var_sensible_effectiveness_at_75_cooling_air_flow = 0.5
        obj.sensible_effectiveness_at_75_cooling_air_flow = var_sensible_effectiveness_at_75_cooling_air_flow
        # real
        var_latent_effectiveness_at_75_cooling_air_flow = 0.5
        obj.latent_effectiveness_at_75_cooling_air_flow = var_latent_effectiveness_at_75_cooling_air_flow
        # node
        var_supply_air_inlet_node_name = "node|Supply Air Inlet Node Name"
        obj.supply_air_inlet_node_name = var_supply_air_inlet_node_name
        # node
        var_supply_air_outlet_node_name = "node|Supply Air Outlet Node Name"
        obj.supply_air_outlet_node_name = var_supply_air_outlet_node_name
        # node
        var_exhaust_air_inlet_node_name = "node|Exhaust Air Inlet Node Name"
        obj.exhaust_air_inlet_node_name = var_exhaust_air_inlet_node_name
        # node
        var_exhaust_air_outlet_node_name = "node|Exhaust Air Outlet Node Name"
        obj.exhaust_air_outlet_node_name = var_exhaust_air_outlet_node_name
        # real
        var_nominal_electric_power = 0.0
        obj.nominal_electric_power = var_nominal_electric_power
        # alpha
        var_supply_air_outlet_temperature_control = "No"
        obj.supply_air_outlet_temperature_control = var_supply_air_outlet_temperature_control
        # alpha
        var_heat_exchanger_type = "Plate"
        obj.heat_exchanger_type = var_heat_exchanger_type
        # alpha
        var_frost_control_type = "None"
        obj.frost_control_type = var_frost_control_type
        # real
        var_threshold_temperature = 20.2
        obj.threshold_temperature = var_threshold_temperature
        # real
        var_initial_defrost_time_fraction = 0.5
        obj.initial_defrost_time_fraction = var_initial_defrost_time_fraction
        # real
        var_rate_of_defrost_time_fraction_increase = 0.0
        obj.rate_of_defrost_time_fraction_increase = var_rate_of_defrost_time_fraction_increase
        # alpha
        var_economizer_lockout = "Yes"
        obj.economizer_lockout = var_economizer_lockout

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].name, var_name)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].availability_schedule_name, var_availability_schedule_name)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].nominal_supply_air_flow_rate, var_nominal_supply_air_flow_rate)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].sensible_effectiveness_at_100_heating_air_flow, var_sensible_effectiveness_at_100_heating_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].latent_effectiveness_at_100_heating_air_flow, var_latent_effectiveness_at_100_heating_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].sensible_effectiveness_at_75_heating_air_flow, var_sensible_effectiveness_at_75_heating_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].latent_effectiveness_at_75_heating_air_flow, var_latent_effectiveness_at_75_heating_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].sensible_effectiveness_at_100_cooling_air_flow, var_sensible_effectiveness_at_100_cooling_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].latent_effectiveness_at_100_cooling_air_flow, var_latent_effectiveness_at_100_cooling_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].sensible_effectiveness_at_75_cooling_air_flow, var_sensible_effectiveness_at_75_cooling_air_flow)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].latent_effectiveness_at_75_cooling_air_flow, var_latent_effectiveness_at_75_cooling_air_flow)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].supply_air_inlet_node_name, var_supply_air_inlet_node_name)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].supply_air_outlet_node_name, var_supply_air_outlet_node_name)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].exhaust_air_inlet_node_name, var_exhaust_air_inlet_node_name)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].exhaust_air_outlet_node_name, var_exhaust_air_outlet_node_name)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].nominal_electric_power, var_nominal_electric_power)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].supply_air_outlet_temperature_control, var_supply_air_outlet_temperature_control)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].heat_exchanger_type, var_heat_exchanger_type)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].frost_control_type, var_frost_control_type)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].threshold_temperature, var_threshold_temperature)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].initial_defrost_time_fraction, var_initial_defrost_time_fraction)
        self.assertAlmostEqual(idf2.heatexchangerairtoairsensibleandlatents[0].rate_of_defrost_time_fraction_increase, var_rate_of_defrost_time_fraction_increase)
        self.assertEqual(idf2.heatexchangerairtoairsensibleandlatents[0].economizer_lockout, var_economizer_lockout)