import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.unitary_equipment import AirLoopHvacUnitaryHeatPumpWaterToAir

log = logging.getLogger(__name__)

class TestAirLoopHvacUnitaryHeatPumpWaterToAir(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_airloophvacunitaryheatpumpwatertoair(self):

        pyidf.validation_level = ValidationLevel.error

        obj = AirLoopHvacUnitaryHeatPumpWaterToAir()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # node
        var_air_inlet_node_name = "node|Air Inlet Node Name"
        obj.air_inlet_node_name = var_air_inlet_node_name
        # node
        var_air_outlet_node_name = "node|Air Outlet Node Name"
        obj.air_outlet_node_name = var_air_outlet_node_name
        # real
        var_supply_air_flow_rate = 0.0001
        obj.supply_air_flow_rate = var_supply_air_flow_rate
        # object-list
        var_controlling_zone_or_thermostat_location = "object-list|Controlling Zone or Thermostat Location"
        obj.controlling_zone_or_thermostat_location = var_controlling_zone_or_thermostat_location
        # alpha
        var_supply_air_fan_object_type = "Fan:OnOff"
        obj.supply_air_fan_object_type = var_supply_air_fan_object_type
        # object-list
        var_supply_air_fan_name = "object-list|Supply Air Fan Name"
        obj.supply_air_fan_name = var_supply_air_fan_name
        # alpha
        var_heating_coil_object_type = "Coil:Heating:WaterToAirHeatPump:ParameterEstimation"
        obj.heating_coil_object_type = var_heating_coil_object_type
        # object-list
        var_heating_coil_name = "object-list|Heating Coil Name"
        obj.heating_coil_name = var_heating_coil_name
        # real
        var_heating_convergence = 0.0001
        obj.heating_convergence = var_heating_convergence
        # alpha
        var_cooling_coil_object_type = "Coil:Cooling:WaterToAirHeatPump:ParameterEstimation"
        obj.cooling_coil_object_type = var_cooling_coil_object_type
        # object-list
        var_cooling_coil_name = "object-list|Cooling Coil Name"
        obj.cooling_coil_name = var_cooling_coil_name
        # real
        var_cooling_convergence = 0.0001
        obj.cooling_convergence = var_cooling_convergence
        # real
        var_maximum_cycling_rate = 2.5
        obj.maximum_cycling_rate = var_maximum_cycling_rate
        # real
        var_heat_pump_time_constant = 250.0
        obj.heat_pump_time_constant = var_heat_pump_time_constant
        # real
        var_fraction_of_oncycle_power_use = 0.025
        obj.fraction_of_oncycle_power_use = var_fraction_of_oncycle_power_use
        # real
        var_heat_pump_fan_delay_time = 0.0
        obj.heat_pump_fan_delay_time = var_heat_pump_fan_delay_time
        # alpha
        var_supplemental_heating_coil_object_type = "Coil:Heating:Gas"
        obj.supplemental_heating_coil_object_type = var_supplemental_heating_coil_object_type
        # object-list
        var_supplemental_heating_coil_name = "object-list|Supplemental Heating Coil Name"
        obj.supplemental_heating_coil_name = var_supplemental_heating_coil_name
        # real
        var_maximum_supply_air_temperature_from_supplemental_heater = 21.21
        obj.maximum_supply_air_temperature_from_supplemental_heater = var_maximum_supply_air_temperature_from_supplemental_heater
        # real
        var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = 21.0
        obj.maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation = var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation
        # node
        var_outdoor_drybulb_temperature_sensor_node_name = "node|Outdoor Dry-Bulb Temperature Sensor Node Name"
        obj.outdoor_drybulb_temperature_sensor_node_name = var_outdoor_drybulb_temperature_sensor_node_name
        # alpha
        var_fan_placement = "BlowThrough"
        obj.fan_placement = var_fan_placement
        # object-list
        var_supply_air_fan_operating_mode_schedule_name = "object-list|Supply Air Fan Operating Mode Schedule Name"
        obj.supply_air_fan_operating_mode_schedule_name = var_supply_air_fan_operating_mode_schedule_name
        # alpha
        var_dehumidification_control_type = "None"
        obj.dehumidification_control_type = var_dehumidification_control_type
        # alpha
        var_heat_pump_coil_water_flow_mode = "Constant"
        obj.heat_pump_coil_water_flow_mode = var_heat_pump_coil_water_flow_mode

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].name, var_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].air_inlet_node_name, var_air_inlet_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].air_outlet_node_name, var_air_outlet_node_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].supply_air_flow_rate, var_supply_air_flow_rate)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].controlling_zone_or_thermostat_location, var_controlling_zone_or_thermostat_location)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].supply_air_fan_object_type, var_supply_air_fan_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].supply_air_fan_name, var_supply_air_fan_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].heating_coil_object_type, var_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].heating_coil_name, var_heating_coil_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].heating_convergence, var_heating_convergence)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].cooling_coil_object_type, var_cooling_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].cooling_coil_name, var_cooling_coil_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].cooling_convergence, var_cooling_convergence)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].maximum_cycling_rate, var_maximum_cycling_rate)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].heat_pump_time_constant, var_heat_pump_time_constant)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].fraction_of_oncycle_power_use, var_fraction_of_oncycle_power_use)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].heat_pump_fan_delay_time, var_heat_pump_fan_delay_time)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].supplemental_heating_coil_object_type, var_supplemental_heating_coil_object_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].supplemental_heating_coil_name, var_supplemental_heating_coil_name)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].maximum_supply_air_temperature_from_supplemental_heater, var_maximum_supply_air_temperature_from_supplemental_heater)
        self.assertAlmostEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation, var_maximum_outdoor_drybulb_temperature_for_supplemental_heater_operation)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].outdoor_drybulb_temperature_sensor_node_name, var_outdoor_drybulb_temperature_sensor_node_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].fan_placement, var_fan_placement)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].supply_air_fan_operating_mode_schedule_name, var_supply_air_fan_operating_mode_schedule_name)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].dehumidification_control_type, var_dehumidification_control_type)
        self.assertEqual(idf2.airloophvacunitaryheatpumpwatertoairs[0].heat_pump_coil_water_flow_mode, var_heat_pump_coil_water_flow_mode)