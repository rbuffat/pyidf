import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.refrigeration import RefrigerationAirChiller

log = logging.getLogger(__name__)

class TestRefrigerationAirChiller(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_refrigerationairchiller(self):

        pyidf.validation_level = ValidationLevel.error

        obj = RefrigerationAirChiller()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # alpha
        var_capacity_rating_type = "UnitLoadFactorSensibleOnly"
        obj.capacity_rating_type = var_capacity_rating_type
        # real
        var_rated_unit_load_factor = 4.4
        obj.rated_unit_load_factor = var_rated_unit_load_factor
        # real
        var_rated_capacity = 5.5
        obj.rated_capacity = var_rated_capacity
        # real
        var_rated_relative_humidity = 100.0
        obj.rated_relative_humidity = var_rated_relative_humidity
        # real
        var_rated_cooling_source_temperature = -15.0
        obj.rated_cooling_source_temperature = var_rated_cooling_source_temperature
        # real
        var_rated_temperature_difference_dt1 = 10.0
        obj.rated_temperature_difference_dt1 = var_rated_temperature_difference_dt1
        # real
        var_maximum_temperature_difference_between_inlet_air_and_evaporating_temperature = 12.5
        obj.maximum_temperature_difference_between_inlet_air_and_evaporating_temperature = var_maximum_temperature_difference_between_inlet_air_and_evaporating_temperature
        # real
        var_coil_material_correction_factor = 10.1
        obj.coil_material_correction_factor = var_coil_material_correction_factor
        # real
        var_refrigerant_correction_factor = 11.11
        obj.refrigerant_correction_factor = var_refrigerant_correction_factor
        # alpha
        var_capacity_correction_curve_type = "LinearSHR60"
        obj.capacity_correction_curve_type = var_capacity_correction_curve_type
        # object-list
        var_capacity_correction_curve_name = "object-list|Capacity Correction Curve Name"
        obj.capacity_correction_curve_name = var_capacity_correction_curve_name
        # real
        var_shr60_correction_factor = 1.67
        obj.shr60_correction_factor = var_shr60_correction_factor
        # real
        var_rated_total_heating_power = 15.15
        obj.rated_total_heating_power = var_rated_total_heating_power
        # object-list
        var_heating_power_schedule_name = "object-list|Heating Power Schedule Name"
        obj.heating_power_schedule_name = var_heating_power_schedule_name
        # alpha
        var_fan_speed_control_type = "Fixed"
        obj.fan_speed_control_type = var_fan_speed_control_type
        # real
        var_rated_fan_power = 0.0
        obj.rated_fan_power = var_rated_fan_power
        # real
        var_rated_air_flow = 19.19
        obj.rated_air_flow = var_rated_air_flow
        # real
        var_minimum_fan_air_flow_ratio = 0.0
        obj.minimum_fan_air_flow_ratio = var_minimum_fan_air_flow_ratio
        # alpha
        var_defrost_type = "HotFluid"
        obj.defrost_type = var_defrost_type
        # alpha
        var_defrost_control_type = "TimeSchedule"
        obj.defrost_control_type = var_defrost_control_type
        # object-list
        var_defrost_schedule_name = "object-list|Defrost Schedule Name"
        obj.defrost_schedule_name = var_defrost_schedule_name
        # object-list
        var_defrost_dripdown_schedule_name = "object-list|Defrost Drip-Down Schedule Name"
        obj.defrost_dripdown_schedule_name = var_defrost_dripdown_schedule_name
        # real
        var_defrost_power = 0.0
        obj.defrost_power = var_defrost_power
        # real
        var_temperature_termination_defrost_fraction_to_ice = 0.50005
        obj.temperature_termination_defrost_fraction_to_ice = var_temperature_termination_defrost_fraction_to_ice
        # alpha
        var_vertical_location = "Ceiling"
        obj.vertical_location = var_vertical_location
        # real
        var_average_refrigerant_charge_inventory = 28.28
        obj.average_refrigerant_charge_inventory = var_average_refrigerant_charge_inventory

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.refrigerationairchillers[0].name, var_name)
        self.assertEqual(idf2.refrigerationairchillers[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.refrigerationairchillers[0].capacity_rating_type, var_capacity_rating_type)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_unit_load_factor, var_rated_unit_load_factor)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_capacity, var_rated_capacity)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_relative_humidity, var_rated_relative_humidity)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_cooling_source_temperature, var_rated_cooling_source_temperature)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_temperature_difference_dt1, var_rated_temperature_difference_dt1)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].maximum_temperature_difference_between_inlet_air_and_evaporating_temperature, var_maximum_temperature_difference_between_inlet_air_and_evaporating_temperature)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].coil_material_correction_factor, var_coil_material_correction_factor)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].refrigerant_correction_factor, var_refrigerant_correction_factor)
        self.assertEqual(idf2.refrigerationairchillers[0].capacity_correction_curve_type, var_capacity_correction_curve_type)
        self.assertEqual(idf2.refrigerationairchillers[0].capacity_correction_curve_name, var_capacity_correction_curve_name)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].shr60_correction_factor, var_shr60_correction_factor)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_total_heating_power, var_rated_total_heating_power)
        self.assertEqual(idf2.refrigerationairchillers[0].heating_power_schedule_name, var_heating_power_schedule_name)
        self.assertEqual(idf2.refrigerationairchillers[0].fan_speed_control_type, var_fan_speed_control_type)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_fan_power, var_rated_fan_power)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].rated_air_flow, var_rated_air_flow)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].minimum_fan_air_flow_ratio, var_minimum_fan_air_flow_ratio)
        self.assertEqual(idf2.refrigerationairchillers[0].defrost_type, var_defrost_type)
        self.assertEqual(idf2.refrigerationairchillers[0].defrost_control_type, var_defrost_control_type)
        self.assertEqual(idf2.refrigerationairchillers[0].defrost_schedule_name, var_defrost_schedule_name)
        self.assertEqual(idf2.refrigerationairchillers[0].defrost_dripdown_schedule_name, var_defrost_dripdown_schedule_name)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].defrost_power, var_defrost_power)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].temperature_termination_defrost_fraction_to_ice, var_temperature_termination_defrost_fraction_to_ice)
        self.assertEqual(idf2.refrigerationairchillers[0].vertical_location, var_vertical_location)
        self.assertAlmostEqual(idf2.refrigerationairchillers[0].average_refrigerant_charge_inventory, var_average_refrigerant_charge_inventory)