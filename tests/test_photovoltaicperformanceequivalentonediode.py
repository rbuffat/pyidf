import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import PhotovoltaicPerformanceEquivalentOneDiode
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPhotovoltaicPerformanceEquivalentOneDiode(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_photovoltaicperformanceequivalentonediode(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PhotovoltaicPerformanceEquivalentOneDiode()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_cell_type = "CrystallineSilicon"
        obj.cell_type = var_cell_type
        # integer
        var_number_of_cells_in_series = 0
        obj.number_of_cells_in_series = var_number_of_cells_in_series
        # real
        var_active_area = 0.1
        obj.active_area = var_active_area
        # real
        var_transmittance_absorptance_product = 0.5
        obj.transmittance_absorptance_product = var_transmittance_absorptance_product
        # real
        var_semiconductor_bandgap = 0.0
        obj.semiconductor_bandgap = var_semiconductor_bandgap
        # real
        var_shunt_resistance = 0.0
        obj.shunt_resistance = var_shunt_resistance
        # real
        var_short_circuit_current = 0.0
        obj.short_circuit_current = var_short_circuit_current
        # real
        var_open_circuit_voltage = 0.0
        obj.open_circuit_voltage = var_open_circuit_voltage
        # real
        var_reference_temperature = 0.0
        obj.reference_temperature = var_reference_temperature
        # real
        var_reference_insolation = 0.0
        obj.reference_insolation = var_reference_insolation
        # real
        var_module_current_at_maximum_power = 0.0
        obj.module_current_at_maximum_power = var_module_current_at_maximum_power
        # real
        var_module_voltage_at_maximum_power = 0.0
        obj.module_voltage_at_maximum_power = var_module_voltage_at_maximum_power
        # real
        var_temperature_coefficient_of_short_circuit_current = 14.14
        obj.temperature_coefficient_of_short_circuit_current = var_temperature_coefficient_of_short_circuit_current
        # real
        var_temperature_coefficient_of_open_circuit_voltage = 15.15
        obj.temperature_coefficient_of_open_circuit_voltage = var_temperature_coefficient_of_open_circuit_voltage
        # real
        var_nominal_operating_cell_temperature_test_ambient_temperature = 0.0
        obj.nominal_operating_cell_temperature_test_ambient_temperature = var_nominal_operating_cell_temperature_test_ambient_temperature
        # real
        var_nominal_operating_cell_temperature_test_cell_temperature = 0.0
        obj.nominal_operating_cell_temperature_test_cell_temperature = var_nominal_operating_cell_temperature_test_cell_temperature
        # real
        var_nominal_operating_cell_temperature_test_insolation = 0.0
        obj.nominal_operating_cell_temperature_test_insolation = var_nominal_operating_cell_temperature_test_insolation
        # real
        var_module_heat_loss_coefficient = 0.0
        obj.module_heat_loss_coefficient = var_module_heat_loss_coefficient
        # real
        var_total_heat_capacity = 0.0
        obj.total_heat_capacity = var_total_heat_capacity

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.photovoltaicperformanceequivalentonediodes[0].name, var_name)
        self.assertEqual(idf2.photovoltaicperformanceequivalentonediodes[0].cell_type, var_cell_type)
        self.assertEqual(idf2.photovoltaicperformanceequivalentonediodes[0].number_of_cells_in_series, var_number_of_cells_in_series)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].active_area, var_active_area)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].transmittance_absorptance_product, var_transmittance_absorptance_product)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].semiconductor_bandgap, var_semiconductor_bandgap)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].shunt_resistance, var_shunt_resistance)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].short_circuit_current, var_short_circuit_current)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].open_circuit_voltage, var_open_circuit_voltage)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].reference_temperature, var_reference_temperature)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].reference_insolation, var_reference_insolation)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].module_current_at_maximum_power, var_module_current_at_maximum_power)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].module_voltage_at_maximum_power, var_module_voltage_at_maximum_power)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].temperature_coefficient_of_short_circuit_current, var_temperature_coefficient_of_short_circuit_current)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].temperature_coefficient_of_open_circuit_voltage, var_temperature_coefficient_of_open_circuit_voltage)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].nominal_operating_cell_temperature_test_ambient_temperature, var_nominal_operating_cell_temperature_test_ambient_temperature)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].nominal_operating_cell_temperature_test_cell_temperature, var_nominal_operating_cell_temperature_test_cell_temperature)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].nominal_operating_cell_temperature_test_insolation, var_nominal_operating_cell_temperature_test_insolation)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].module_heat_loss_coefficient, var_module_heat_loss_coefficient)
        self.assertAlmostEqual(idf2.photovoltaicperformanceequivalentonediodes[0].total_heat_capacity, var_total_heat_capacity)