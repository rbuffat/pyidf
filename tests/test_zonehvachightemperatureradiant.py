import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.zone_hvac_radiative import ZoneHvacHighTemperatureRadiant

log = logging.getLogger(__name__)

class TestZoneHvacHighTemperatureRadiant(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_zonehvachightemperatureradiant(self):

        pyidf.validation_level = ValidationLevel.error

        obj = ZoneHvacHighTemperatureRadiant()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # object-list
        var_availability_schedule_name = "object-list|Availability Schedule Name"
        obj.availability_schedule_name = var_availability_schedule_name
        # object-list
        var_zone_name = "object-list|Zone Name"
        obj.zone_name = var_zone_name
        # alpha
        var_heating_design_capacity_method = "HeatingDesignCapacity"
        obj.heating_design_capacity_method = var_heating_design_capacity_method
        # real
        var_heating_design_capacity = 0.0
        obj.heating_design_capacity = var_heating_design_capacity
        # real
        var_heating_design_capacity_per_floor_area = 0.0
        obj.heating_design_capacity_per_floor_area = var_heating_design_capacity_per_floor_area
        # real
        var_fraction_of_autosized_heating_design_capacity = 0.0
        obj.fraction_of_autosized_heating_design_capacity = var_fraction_of_autosized_heating_design_capacity
        # alpha
        var_fuel_type = "NaturalGas"
        obj.fuel_type = var_fuel_type
        # real
        var_combustion_efficiency = 0.5
        obj.combustion_efficiency = var_combustion_efficiency
        # real
        var_fraction_of_input_converted_to_radiant_energy = 0.5
        obj.fraction_of_input_converted_to_radiant_energy = var_fraction_of_input_converted_to_radiant_energy
        # real
        var_fraction_of_input_converted_to_latent_energy = 0.5
        obj.fraction_of_input_converted_to_latent_energy = var_fraction_of_input_converted_to_latent_energy
        # real
        var_fraction_of_input_that_is_lost = 0.5
        obj.fraction_of_input_that_is_lost = var_fraction_of_input_that_is_lost
        # alpha
        var_temperature_control_type = "MeanAirTemperature"
        obj.temperature_control_type = var_temperature_control_type
        # real
        var_heating_throttling_range = 0.0
        obj.heating_throttling_range = var_heating_throttling_range
        # object-list
        var_heating_setpoint_temperature_schedule_name = "object-list|Heating Setpoint Temperature Schedule Name"
        obj.heating_setpoint_temperature_schedule_name = var_heating_setpoint_temperature_schedule_name
        # real
        var_fraction_of_radiant_energy_incident_on_people = 0.5
        obj.fraction_of_radiant_energy_incident_on_people = var_fraction_of_radiant_energy_incident_on_people
        paras = []
        var_surface_1_name = "object-list|Surface 1 Name"
        paras.append(var_surface_1_name)
        var_fraction_of_radiant_energy_to_surface_1 = 0.5
        paras.append(var_fraction_of_radiant_energy_to_surface_1)
        obj.add_extensible(*paras)
        

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].name, var_name)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].availability_schedule_name, var_availability_schedule_name)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].zone_name, var_zone_name)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].heating_design_capacity_method, var_heating_design_capacity_method)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].heating_design_capacity, var_heating_design_capacity)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].heating_design_capacity_per_floor_area, var_heating_design_capacity_per_floor_area)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].fraction_of_autosized_heating_design_capacity, var_fraction_of_autosized_heating_design_capacity)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].fuel_type, var_fuel_type)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].combustion_efficiency, var_combustion_efficiency)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].fraction_of_input_converted_to_radiant_energy, var_fraction_of_input_converted_to_radiant_energy)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].fraction_of_input_converted_to_latent_energy, var_fraction_of_input_converted_to_latent_energy)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].fraction_of_input_that_is_lost, var_fraction_of_input_that_is_lost)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].temperature_control_type, var_temperature_control_type)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].heating_throttling_range, var_heating_throttling_range)
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].heating_setpoint_temperature_schedule_name, var_heating_setpoint_temperature_schedule_name)
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].fraction_of_radiant_energy_incident_on_people, var_fraction_of_radiant_energy_incident_on_people)
        index = obj.extensible_field_index("Surface 1 Name")
        self.assertEqual(idf2.zonehvachightemperatureradiants[0].extensibles[0][index], var_surface_1_name)
        index = obj.extensible_field_index("Fraction of Radiant Energy to Surface 1")
        self.assertAlmostEqual(idf2.zonehvachightemperatureradiants[0].extensibles[0][index], var_fraction_of_radiant_energy_to_surface_1)