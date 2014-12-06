import os
import tempfile
import unittest
import pyidf
from pyidf.electric_load_center import PhotovoltaicPerformanceSandia
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestPhotovoltaicPerformanceSandia(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_photovoltaicperformancesandia(self):

        pyidf.validation_level = ValidationLevel.error

        obj = PhotovoltaicPerformanceSandia()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_active_area = 0.0
        obj.active_area = var_active_area
        # integer
        var_number_of_cells_in_series = 1
        obj.number_of_cells_in_series = var_number_of_cells_in_series
        # integer
        var_number_of_cells_in_parallel = 1
        obj.number_of_cells_in_parallel = var_number_of_cells_in_parallel
        # real
        var_short_circuit_current = 5.5
        obj.short_circuit_current = var_short_circuit_current
        # real
        var_open_circuit_voltage = 6.6
        obj.open_circuit_voltage = var_open_circuit_voltage
        # real
        var_current_at_maximum_power_point = 7.7
        obj.current_at_maximum_power_point = var_current_at_maximum_power_point
        # real
        var_voltage_at_maximum_power_point = 8.8
        obj.voltage_at_maximum_power_point = var_voltage_at_maximum_power_point
        # real
        var_sandia_database_parameter_aisc = 9.9
        obj.sandia_database_parameter_aisc = var_sandia_database_parameter_aisc
        # real
        var_sandia_database_parameter_aimp = 10.1
        obj.sandia_database_parameter_aimp = var_sandia_database_parameter_aimp
        # real
        var_sandia_database_parameter_c0 = 11.11
        obj.sandia_database_parameter_c0 = var_sandia_database_parameter_c0
        # real
        var_sandia_database_parameter_c1 = 12.12
        obj.sandia_database_parameter_c1 = var_sandia_database_parameter_c1
        # real
        var_sandia_database_parameter_bvoc0 = 13.13
        obj.sandia_database_parameter_bvoc0 = var_sandia_database_parameter_bvoc0
        # real
        var_sandia_database_parameter_mbvoc = 14.14
        obj.sandia_database_parameter_mbvoc = var_sandia_database_parameter_mbvoc
        # real
        var_sandia_database_parameter_bvmp0 = 15.15
        obj.sandia_database_parameter_bvmp0 = var_sandia_database_parameter_bvmp0
        # real
        var_sandia_database_parameter_mbvmp = 16.16
        obj.sandia_database_parameter_mbvmp = var_sandia_database_parameter_mbvmp
        # real
        var_diode_factor = 17.17
        obj.diode_factor = var_diode_factor
        # real
        var_sandia_database_parameter_c2 = 18.18
        obj.sandia_database_parameter_c2 = var_sandia_database_parameter_c2
        # real
        var_sandia_database_parameter_c3 = 19.19
        obj.sandia_database_parameter_c3 = var_sandia_database_parameter_c3
        # real
        var_sandia_database_parameter_a0 = 20.2
        obj.sandia_database_parameter_a0 = var_sandia_database_parameter_a0
        # real
        var_sandia_database_parameter_a1 = 21.21
        obj.sandia_database_parameter_a1 = var_sandia_database_parameter_a1
        # real
        var_sandia_database_parameter_a2 = 22.22
        obj.sandia_database_parameter_a2 = var_sandia_database_parameter_a2
        # real
        var_sandia_database_parameter_a3 = 23.23
        obj.sandia_database_parameter_a3 = var_sandia_database_parameter_a3
        # real
        var_sandia_database_parameter_a4 = 24.24
        obj.sandia_database_parameter_a4 = var_sandia_database_parameter_a4
        # real
        var_sandia_database_parameter_b0 = 25.25
        obj.sandia_database_parameter_b0 = var_sandia_database_parameter_b0
        # real
        var_sandia_database_parameter_b1 = 26.26
        obj.sandia_database_parameter_b1 = var_sandia_database_parameter_b1
        # real
        var_sandia_database_parameter_b2 = 27.27
        obj.sandia_database_parameter_b2 = var_sandia_database_parameter_b2
        # real
        var_sandia_database_parameter_b3 = 28.28
        obj.sandia_database_parameter_b3 = var_sandia_database_parameter_b3
        # real
        var_sandia_database_parameter_b4 = 29.29
        obj.sandia_database_parameter_b4 = var_sandia_database_parameter_b4
        # real
        var_sandia_database_parameter_b5 = 30.3
        obj.sandia_database_parameter_b5 = var_sandia_database_parameter_b5
        # real
        var_sandia_database_parameter_deltatc = 31.31
        obj.sandia_database_parameter_deltatc = var_sandia_database_parameter_deltatc
        # real
        var_sandia_database_parameter_fd = 32.32
        obj.sandia_database_parameter_fd = var_sandia_database_parameter_fd
        # real
        var_sandia_database_parameter_a = 33.33
        obj.sandia_database_parameter_a = var_sandia_database_parameter_a
        # real
        var_sandia_database_parameter_b = 34.34
        obj.sandia_database_parameter_b = var_sandia_database_parameter_b
        # real
        var_sandia_database_parameter_c4 = 35.35
        obj.sandia_database_parameter_c4 = var_sandia_database_parameter_c4
        # real
        var_sandia_database_parameter_c5 = 36.36
        obj.sandia_database_parameter_c5 = var_sandia_database_parameter_c5
        # real
        var_sandia_database_parameter_ix0 = 37.37
        obj.sandia_database_parameter_ix0 = var_sandia_database_parameter_ix0
        # real
        var_sandia_database_parameter_ixx0 = 38.38
        obj.sandia_database_parameter_ixx0 = var_sandia_database_parameter_ixx0
        # real
        var_sandia_database_parameter_c6 = 39.39
        obj.sandia_database_parameter_c6 = var_sandia_database_parameter_c6
        # real
        var_sandia_database_parameter_c7 = 40.4
        obj.sandia_database_parameter_c7 = var_sandia_database_parameter_c7

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.photovoltaicperformancesandias[0].name, var_name)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].active_area, var_active_area)
        self.assertEqual(idf2.photovoltaicperformancesandias[0].number_of_cells_in_series, var_number_of_cells_in_series)
        self.assertEqual(idf2.photovoltaicperformancesandias[0].number_of_cells_in_parallel, var_number_of_cells_in_parallel)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].short_circuit_current, var_short_circuit_current)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].open_circuit_voltage, var_open_circuit_voltage)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].current_at_maximum_power_point, var_current_at_maximum_power_point)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].voltage_at_maximum_power_point, var_voltage_at_maximum_power_point)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_aisc, var_sandia_database_parameter_aisc)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_aimp, var_sandia_database_parameter_aimp)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c0, var_sandia_database_parameter_c0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c1, var_sandia_database_parameter_c1)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_bvoc0, var_sandia_database_parameter_bvoc0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_mbvoc, var_sandia_database_parameter_mbvoc)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_bvmp0, var_sandia_database_parameter_bvmp0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_mbvmp, var_sandia_database_parameter_mbvmp)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].diode_factor, var_diode_factor)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c2, var_sandia_database_parameter_c2)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c3, var_sandia_database_parameter_c3)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_a0, var_sandia_database_parameter_a0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_a1, var_sandia_database_parameter_a1)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_a2, var_sandia_database_parameter_a2)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_a3, var_sandia_database_parameter_a3)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_a4, var_sandia_database_parameter_a4)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b0, var_sandia_database_parameter_b0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b1, var_sandia_database_parameter_b1)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b2, var_sandia_database_parameter_b2)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b3, var_sandia_database_parameter_b3)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b4, var_sandia_database_parameter_b4)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b5, var_sandia_database_parameter_b5)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_deltatc, var_sandia_database_parameter_deltatc)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_fd, var_sandia_database_parameter_fd)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_a, var_sandia_database_parameter_a)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_b, var_sandia_database_parameter_b)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c4, var_sandia_database_parameter_c4)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c5, var_sandia_database_parameter_c5)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_ix0, var_sandia_database_parameter_ix0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_ixx0, var_sandia_database_parameter_ixx0)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c6, var_sandia_database_parameter_c6)
        self.assertAlmostEqual(idf2.photovoltaicperformancesandias[0].sandia_database_parameter_c7, var_sandia_database_parameter_c7)