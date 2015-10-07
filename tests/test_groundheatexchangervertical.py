import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.condenser_equipment_and_heat_exchangers import GroundHeatExchangerVertical

log = logging.getLogger(__name__)

class TestGroundHeatExchangerVertical(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_groundheatexchangervertical(self):

        pyidf.validation_level = ValidationLevel.error

        obj = GroundHeatExchangerVertical()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # node
        var_inlet_node_name = "node|Inlet Node Name"
        obj.inlet_node_name = var_inlet_node_name
        # node
        var_outlet_node_name = "node|Outlet Node Name"
        obj.outlet_node_name = var_outlet_node_name
        # real
        var_design_flow_rate = 0.0001
        obj.design_flow_rate = var_design_flow_rate
        # real
        var_number_of_bore_holes = 0.0001
        obj.number_of_bore_holes = var_number_of_bore_holes
        # real
        var_bore_hole_length = 0.0001
        obj.bore_hole_length = var_bore_hole_length
        # real
        var_bore_hole_radius = 0.0001
        obj.bore_hole_radius = var_bore_hole_radius
        # real
        var_ground_thermal_conductivity = 0.0001
        obj.ground_thermal_conductivity = var_ground_thermal_conductivity
        # real
        var_ground_thermal_heat_capacity = 0.0001
        obj.ground_thermal_heat_capacity = var_ground_thermal_heat_capacity
        # real
        var_ground_temperature = 0.0001
        obj.ground_temperature = var_ground_temperature
        # real
        var_grout_thermal_conductivity = 0.0001
        obj.grout_thermal_conductivity = var_grout_thermal_conductivity
        # real
        var_pipe_thermal_conductivity = 0.0001
        obj.pipe_thermal_conductivity = var_pipe_thermal_conductivity
        # real
        var_pipe_out_diameter = 0.0001
        obj.pipe_out_diameter = var_pipe_out_diameter
        # real
        var_utube_distance = 0.0001
        obj.utube_distance = var_utube_distance
        # real
        var_pipe_thickness = 0.0001
        obj.pipe_thickness = var_pipe_thickness
        # real
        var_maximum_length_of_simulation = 0.0001
        obj.maximum_length_of_simulation = var_maximum_length_of_simulation
        # real
        var_gfunction_reference_ratio = 0.0001
        obj.gfunction_reference_ratio = var_gfunction_reference_ratio
        # real
        var_number_of_data_pairs_of_the_g_function = 50.00005
        obj.number_of_data_pairs_of_the_g_function = var_number_of_data_pairs_of_the_g_function
        # real
        var_gfunction_lnt_or_ts_value_1 = 19.19
        obj.gfunction_lnt_or_ts_value_1 = var_gfunction_lnt_or_ts_value_1
        # real
        var_gfunction_g_value_1 = 20.2
        obj.gfunction_g_value_1 = var_gfunction_g_value_1
        # real
        var_gfunction_lnt_or_ts_value_2 = 21.21
        obj.gfunction_lnt_or_ts_value_2 = var_gfunction_lnt_or_ts_value_2
        # real
        var_gfunction_g_value_2 = 22.22
        obj.gfunction_g_value_2 = var_gfunction_g_value_2
        # real
        var_gfunction_lnt_or_ts_value_3 = 23.23
        obj.gfunction_lnt_or_ts_value_3 = var_gfunction_lnt_or_ts_value_3
        # real
        var_gfunction_g_value_3 = 24.24
        obj.gfunction_g_value_3 = var_gfunction_g_value_3
        # real
        var_gfunction_lnt_or_ts_value_4 = 25.25
        obj.gfunction_lnt_or_ts_value_4 = var_gfunction_lnt_or_ts_value_4
        # real
        var_gfunction_g_value_4 = 26.26
        obj.gfunction_g_value_4 = var_gfunction_g_value_4
        # real
        var_gfunction_lnt_or_ts_value_5 = 27.27
        obj.gfunction_lnt_or_ts_value_5 = var_gfunction_lnt_or_ts_value_5
        # real
        var_gfunction_g_value_5 = 28.28
        obj.gfunction_g_value_5 = var_gfunction_g_value_5
        # real
        var_gfunction_lnt_or_ts_value_6 = 29.29
        obj.gfunction_lnt_or_ts_value_6 = var_gfunction_lnt_or_ts_value_6
        # real
        var_gfunction_g_value_6 = 30.3
        obj.gfunction_g_value_6 = var_gfunction_g_value_6
        # real
        var_gfunction_lnt_or_ts_value_7 = 31.31
        obj.gfunction_lnt_or_ts_value_7 = var_gfunction_lnt_or_ts_value_7
        # real
        var_gfunction_g_value_7 = 32.32
        obj.gfunction_g_value_7 = var_gfunction_g_value_7
        # real
        var_gfunction_lnt_or_ts_value_8 = 33.33
        obj.gfunction_lnt_or_ts_value_8 = var_gfunction_lnt_or_ts_value_8
        # real
        var_gfunction_g_value_8 = 34.34
        obj.gfunction_g_value_8 = var_gfunction_g_value_8
        # real
        var_gfunction_lnt_or_ts_value_9 = 35.35
        obj.gfunction_lnt_or_ts_value_9 = var_gfunction_lnt_or_ts_value_9
        # real
        var_gfunction_g_value_9 = 36.36
        obj.gfunction_g_value_9 = var_gfunction_g_value_9
        # real
        var_gfunction_lnt_or_ts_value_10 = 37.37
        obj.gfunction_lnt_or_ts_value_10 = var_gfunction_lnt_or_ts_value_10
        # real
        var_gfunction_g_value_10 = 38.38
        obj.gfunction_g_value_10 = var_gfunction_g_value_10
        # real
        var_gfunction_lnt_or_ts_value_11 = 39.39
        obj.gfunction_lnt_or_ts_value_11 = var_gfunction_lnt_or_ts_value_11
        # real
        var_gfunction_g_value_11 = 40.4
        obj.gfunction_g_value_11 = var_gfunction_g_value_11
        # real
        var_gfunction_lnt_or_ts_value_12 = 41.41
        obj.gfunction_lnt_or_ts_value_12 = var_gfunction_lnt_or_ts_value_12
        # real
        var_gfunction_g_value_12 = 42.42
        obj.gfunction_g_value_12 = var_gfunction_g_value_12
        # real
        var_gfunction_lnt_or_ts_value_13 = 43.43
        obj.gfunction_lnt_or_ts_value_13 = var_gfunction_lnt_or_ts_value_13
        # real
        var_gfunction_g_value_13 = 44.44
        obj.gfunction_g_value_13 = var_gfunction_g_value_13
        # real
        var_gfunction_lnt_or_ts_value_14 = 45.45
        obj.gfunction_lnt_or_ts_value_14 = var_gfunction_lnt_or_ts_value_14
        # real
        var_gfunction_g_value_14 = 46.46
        obj.gfunction_g_value_14 = var_gfunction_g_value_14
        # real
        var_gfunction_lnt_or_ts_value_15 = 47.47
        obj.gfunction_lnt_or_ts_value_15 = var_gfunction_lnt_or_ts_value_15
        # real
        var_gfunction_g_value_15 = 48.48
        obj.gfunction_g_value_15 = var_gfunction_g_value_15
        # real
        var_gfunction_lnt_or_ts_value_16 = 49.49
        obj.gfunction_lnt_or_ts_value_16 = var_gfunction_lnt_or_ts_value_16
        # real
        var_gfunction_g_value_16 = 50.5
        obj.gfunction_g_value_16 = var_gfunction_g_value_16
        # real
        var_gfunction_lnt_or_ts_value_17 = 51.51
        obj.gfunction_lnt_or_ts_value_17 = var_gfunction_lnt_or_ts_value_17
        # real
        var_gfunction_g_value_17 = 52.52
        obj.gfunction_g_value_17 = var_gfunction_g_value_17
        # real
        var_gfunction_lnt_or_ts_value_18 = 53.53
        obj.gfunction_lnt_or_ts_value_18 = var_gfunction_lnt_or_ts_value_18
        # real
        var_gfunction_g_value_18 = 54.54
        obj.gfunction_g_value_18 = var_gfunction_g_value_18
        # real
        var_gfunction_lnt_or_ts_value_19 = 55.55
        obj.gfunction_lnt_or_ts_value_19 = var_gfunction_lnt_or_ts_value_19
        # real
        var_gfunction_g_value_19 = 56.56
        obj.gfunction_g_value_19 = var_gfunction_g_value_19
        # real
        var_gfunction_lnt_or_ts_value_20 = 57.57
        obj.gfunction_lnt_or_ts_value_20 = var_gfunction_lnt_or_ts_value_20
        # real
        var_gfunction_g_value_20 = 58.58
        obj.gfunction_g_value_20 = var_gfunction_g_value_20
        # real
        var_gfunction_lnt_or_ts_value_21 = 59.59
        obj.gfunction_lnt_or_ts_value_21 = var_gfunction_lnt_or_ts_value_21
        # real
        var_gfunction_g_value_21 = 60.6
        obj.gfunction_g_value_21 = var_gfunction_g_value_21
        # real
        var_gfunction_lnt_or_ts_value_22 = 61.61
        obj.gfunction_lnt_or_ts_value_22 = var_gfunction_lnt_or_ts_value_22
        # real
        var_gfunction_g_value_22 = 62.62
        obj.gfunction_g_value_22 = var_gfunction_g_value_22
        # real
        var_gfunction_lnt_or_ts_value_23 = 63.63
        obj.gfunction_lnt_or_ts_value_23 = var_gfunction_lnt_or_ts_value_23
        # real
        var_gfunction_g_value_23 = 64.64
        obj.gfunction_g_value_23 = var_gfunction_g_value_23
        # real
        var_gfunction_lnt_or_ts_value_24 = 65.65
        obj.gfunction_lnt_or_ts_value_24 = var_gfunction_lnt_or_ts_value_24
        # real
        var_gfunction_g_value_24 = 66.66
        obj.gfunction_g_value_24 = var_gfunction_g_value_24
        # real
        var_gfunction_lnt_or_ts_value_25 = 67.67
        obj.gfunction_lnt_or_ts_value_25 = var_gfunction_lnt_or_ts_value_25
        # real
        var_gfunction_g_value_25 = 68.68
        obj.gfunction_g_value_25 = var_gfunction_g_value_25
        # real
        var_gfunction_lnt_or_ts_value_26 = 69.69
        obj.gfunction_lnt_or_ts_value_26 = var_gfunction_lnt_or_ts_value_26
        # real
        var_gfunction_g_value_26 = 70.7
        obj.gfunction_g_value_26 = var_gfunction_g_value_26
        # real
        var_gfunction_lnt_or_ts_value_27 = 71.71
        obj.gfunction_lnt_or_ts_value_27 = var_gfunction_lnt_or_ts_value_27
        # real
        var_gfunction_g_value_27 = 72.72
        obj.gfunction_g_value_27 = var_gfunction_g_value_27
        # real
        var_gfunction_lnt_or_ts_value_28 = 73.73
        obj.gfunction_lnt_or_ts_value_28 = var_gfunction_lnt_or_ts_value_28
        # real
        var_gfunction_g_value_28 = 74.74
        obj.gfunction_g_value_28 = var_gfunction_g_value_28
        # real
        var_gfunction_lnt_or_ts_value_29 = 75.75
        obj.gfunction_lnt_or_ts_value_29 = var_gfunction_lnt_or_ts_value_29
        # real
        var_gfunction_g_value_29 = 76.76
        obj.gfunction_g_value_29 = var_gfunction_g_value_29
        # real
        var_gfunction_lnt_or_ts_value_30 = 77.77
        obj.gfunction_lnt_or_ts_value_30 = var_gfunction_lnt_or_ts_value_30
        # real
        var_gfunction_g_value_30 = 78.78
        obj.gfunction_g_value_30 = var_gfunction_g_value_30
        # real
        var_gfunction_lnt_or_ts_value_31 = 79.79
        obj.gfunction_lnt_or_ts_value_31 = var_gfunction_lnt_or_ts_value_31
        # real
        var_gfunction_g_value_31 = 80.8
        obj.gfunction_g_value_31 = var_gfunction_g_value_31
        # real
        var_gfunction_lnt_or_ts_value_32 = 81.81
        obj.gfunction_lnt_or_ts_value_32 = var_gfunction_lnt_or_ts_value_32
        # real
        var_gfunction_g_value_32 = 82.82
        obj.gfunction_g_value_32 = var_gfunction_g_value_32
        # real
        var_gfunction_lnt_or_ts_value_33 = 83.83
        obj.gfunction_lnt_or_ts_value_33 = var_gfunction_lnt_or_ts_value_33
        # real
        var_gfunction_g_value_33 = 84.84
        obj.gfunction_g_value_33 = var_gfunction_g_value_33
        # real
        var_gfunction_lnt_or_ts_value_34 = 85.85
        obj.gfunction_lnt_or_ts_value_34 = var_gfunction_lnt_or_ts_value_34
        # real
        var_gfunction_g_value_34 = 86.86
        obj.gfunction_g_value_34 = var_gfunction_g_value_34
        # real
        var_gfunction_lnt_or_ts_value_35 = 87.87
        obj.gfunction_lnt_or_ts_value_35 = var_gfunction_lnt_or_ts_value_35
        # real
        var_gfunction_g_value_35 = 88.88
        obj.gfunction_g_value_35 = var_gfunction_g_value_35
        # real
        var_gfunction_lnt_or_ts_value_36 = 89.89
        obj.gfunction_lnt_or_ts_value_36 = var_gfunction_lnt_or_ts_value_36
        # real
        var_gfunction_g_value_36 = 90.9
        obj.gfunction_g_value_36 = var_gfunction_g_value_36
        # real
        var_gfunction_lnt_or_ts_value_37 = 91.91
        obj.gfunction_lnt_or_ts_value_37 = var_gfunction_lnt_or_ts_value_37
        # real
        var_gfunction_g_value_37 = 92.92
        obj.gfunction_g_value_37 = var_gfunction_g_value_37
        # real
        var_gfunction_lnt_or_ts_value_38 = 93.93
        obj.gfunction_lnt_or_ts_value_38 = var_gfunction_lnt_or_ts_value_38
        # real
        var_gfunction_g_value_38 = 94.94
        obj.gfunction_g_value_38 = var_gfunction_g_value_38
        # real
        var_gfunction_lnt_or_ts_value_39 = 95.95
        obj.gfunction_lnt_or_ts_value_39 = var_gfunction_lnt_or_ts_value_39
        # real
        var_gfunction_g_value_39 = 96.96
        obj.gfunction_g_value_39 = var_gfunction_g_value_39
        # real
        var_gfunction_lnt_or_ts_value_40 = 97.97
        obj.gfunction_lnt_or_ts_value_40 = var_gfunction_lnt_or_ts_value_40
        # real
        var_gfunction_g_value_40 = 98.98
        obj.gfunction_g_value_40 = var_gfunction_g_value_40
        # real
        var_gfunction_lnt_or_ts_value_41 = 99.99
        obj.gfunction_lnt_or_ts_value_41 = var_gfunction_lnt_or_ts_value_41
        # real
        var_gfunction_g_value_41 = 100.1
        obj.gfunction_g_value_41 = var_gfunction_g_value_41
        # real
        var_gfunction_lnt_or_ts_value_42 = 101.101
        obj.gfunction_lnt_or_ts_value_42 = var_gfunction_lnt_or_ts_value_42
        # real
        var_gfunction_g_value_42 = 102.102
        obj.gfunction_g_value_42 = var_gfunction_g_value_42
        # real
        var_gfunction_lnt_or_ts_value_43 = 103.103
        obj.gfunction_lnt_or_ts_value_43 = var_gfunction_lnt_or_ts_value_43
        # real
        var_gfunction_g_value_43 = 104.104
        obj.gfunction_g_value_43 = var_gfunction_g_value_43
        # real
        var_gfunction_lnt_or_ts_value_44 = 105.105
        obj.gfunction_lnt_or_ts_value_44 = var_gfunction_lnt_or_ts_value_44
        # real
        var_gfunction_g_value_44 = 106.106
        obj.gfunction_g_value_44 = var_gfunction_g_value_44
        # real
        var_gfunction_lnt_or_ts_value_45 = 107.107
        obj.gfunction_lnt_or_ts_value_45 = var_gfunction_lnt_or_ts_value_45
        # real
        var_gfunction_g_value_45 = 108.108
        obj.gfunction_g_value_45 = var_gfunction_g_value_45
        # real
        var_gfunction_lnt_or_ts_value_46 = 109.109
        obj.gfunction_lnt_or_ts_value_46 = var_gfunction_lnt_or_ts_value_46
        # real
        var_gfunction_g_value_46 = 110.11
        obj.gfunction_g_value_46 = var_gfunction_g_value_46
        # real
        var_gfunction_lnt_or_ts_value_47 = 111.111
        obj.gfunction_lnt_or_ts_value_47 = var_gfunction_lnt_or_ts_value_47
        # real
        var_gfunction_g_value_47 = 112.112
        obj.gfunction_g_value_47 = var_gfunction_g_value_47
        # real
        var_gfunction_lnt_or_ts_value_48 = 113.113
        obj.gfunction_lnt_or_ts_value_48 = var_gfunction_lnt_or_ts_value_48
        # real
        var_gfunction_g_value_48 = 114.114
        obj.gfunction_g_value_48 = var_gfunction_g_value_48
        # real
        var_gfunction_lnt_or_ts_value_49 = 115.115
        obj.gfunction_lnt_or_ts_value_49 = var_gfunction_lnt_or_ts_value_49
        # real
        var_gfunction_g_value_49 = 116.116
        obj.gfunction_g_value_49 = var_gfunction_g_value_49
        # real
        var_gfunction_lnt_or_ts_value_50 = 117.117
        obj.gfunction_lnt_or_ts_value_50 = var_gfunction_lnt_or_ts_value_50
        # real
        var_gfunction_g_value_50 = 118.118
        obj.gfunction_g_value_50 = var_gfunction_g_value_50
        # real
        var_gfunction_lnt_or_ts_value_51 = 119.119
        obj.gfunction_lnt_or_ts_value_51 = var_gfunction_lnt_or_ts_value_51
        # real
        var_gfunction_g_value_51 = 120.12
        obj.gfunction_g_value_51 = var_gfunction_g_value_51
        # real
        var_gfunction_lnt_or_ts_value_52 = 121.121
        obj.gfunction_lnt_or_ts_value_52 = var_gfunction_lnt_or_ts_value_52
        # real
        var_gfunction_g_value_52 = 122.122
        obj.gfunction_g_value_52 = var_gfunction_g_value_52
        # real
        var_gfunction_lnt_or_ts_value_53 = 123.123
        obj.gfunction_lnt_or_ts_value_53 = var_gfunction_lnt_or_ts_value_53
        # real
        var_gfunction_g_value_53 = 124.124
        obj.gfunction_g_value_53 = var_gfunction_g_value_53
        # real
        var_gfunction_lnt_or_ts_value_54 = 125.125
        obj.gfunction_lnt_or_ts_value_54 = var_gfunction_lnt_or_ts_value_54
        # real
        var_gfunction_g_value_54 = 126.126
        obj.gfunction_g_value_54 = var_gfunction_g_value_54
        # real
        var_gfunction_lnt_or_ts_value_55 = 127.127
        obj.gfunction_lnt_or_ts_value_55 = var_gfunction_lnt_or_ts_value_55
        # real
        var_gfunction_g_value_55 = 128.128
        obj.gfunction_g_value_55 = var_gfunction_g_value_55
        # real
        var_gfunction_lnt_or_ts_value_56 = 129.129
        obj.gfunction_lnt_or_ts_value_56 = var_gfunction_lnt_or_ts_value_56
        # real
        var_gfunction_g_value_56 = 130.13
        obj.gfunction_g_value_56 = var_gfunction_g_value_56
        # real
        var_gfunction_lnt_or_ts_value_57 = 131.131
        obj.gfunction_lnt_or_ts_value_57 = var_gfunction_lnt_or_ts_value_57
        # real
        var_gfunction_g_value_57 = 132.132
        obj.gfunction_g_value_57 = var_gfunction_g_value_57
        # real
        var_gfunction_lnt_or_ts_value_58 = 133.133
        obj.gfunction_lnt_or_ts_value_58 = var_gfunction_lnt_or_ts_value_58
        # real
        var_gfunction_g_value_58 = 134.134
        obj.gfunction_g_value_58 = var_gfunction_g_value_58
        # real
        var_gfunction_lnt_or_ts_value_59 = 135.135
        obj.gfunction_lnt_or_ts_value_59 = var_gfunction_lnt_or_ts_value_59
        # real
        var_gfunction_g_value_59 = 136.136
        obj.gfunction_g_value_59 = var_gfunction_g_value_59
        # real
        var_gfunction_lnt_or_ts_value_60 = 137.137
        obj.gfunction_lnt_or_ts_value_60 = var_gfunction_lnt_or_ts_value_60
        # real
        var_gfunction_g_value_60 = 138.138
        obj.gfunction_g_value_60 = var_gfunction_g_value_60
        # real
        var_gfunction_lnt_or_ts_value_61 = 139.139
        obj.gfunction_lnt_or_ts_value_61 = var_gfunction_lnt_or_ts_value_61
        # real
        var_gfunction_g_value_61 = 140.14
        obj.gfunction_g_value_61 = var_gfunction_g_value_61
        # real
        var_gfunction_lnt_or_ts_value_62 = 141.141
        obj.gfunction_lnt_or_ts_value_62 = var_gfunction_lnt_or_ts_value_62
        # real
        var_gfunction_g_value_62 = 142.142
        obj.gfunction_g_value_62 = var_gfunction_g_value_62
        # real
        var_gfunction_lnt_or_ts_value_63 = 143.143
        obj.gfunction_lnt_or_ts_value_63 = var_gfunction_lnt_or_ts_value_63
        # real
        var_gfunction_g_value_63 = 144.144
        obj.gfunction_g_value_63 = var_gfunction_g_value_63
        # real
        var_gfunction_lnt_or_ts_value_64 = 145.145
        obj.gfunction_lnt_or_ts_value_64 = var_gfunction_lnt_or_ts_value_64
        # real
        var_gfunction_g_value_64 = 146.146
        obj.gfunction_g_value_64 = var_gfunction_g_value_64
        # real
        var_gfunction_lnt_or_ts_value_65 = 147.147
        obj.gfunction_lnt_or_ts_value_65 = var_gfunction_lnt_or_ts_value_65
        # real
        var_gfunction_g_value_65 = 148.148
        obj.gfunction_g_value_65 = var_gfunction_g_value_65
        # real
        var_gfunction_lnt_or_ts_value_66 = 149.149
        obj.gfunction_lnt_or_ts_value_66 = var_gfunction_lnt_or_ts_value_66
        # real
        var_gfunction_g_value_66 = 150.15
        obj.gfunction_g_value_66 = var_gfunction_g_value_66
        # real
        var_gfunction_lnt_or_ts_value_67 = 151.151
        obj.gfunction_lnt_or_ts_value_67 = var_gfunction_lnt_or_ts_value_67
        # real
        var_gfunction_g_value_67 = 152.152
        obj.gfunction_g_value_67 = var_gfunction_g_value_67
        # real
        var_gfunction_lnt_or_ts_value_68 = 153.153
        obj.gfunction_lnt_or_ts_value_68 = var_gfunction_lnt_or_ts_value_68
        # real
        var_gfunction_g_value_68 = 154.154
        obj.gfunction_g_value_68 = var_gfunction_g_value_68
        # real
        var_gfunction_lnt_or_ts_value_69 = 155.155
        obj.gfunction_lnt_or_ts_value_69 = var_gfunction_lnt_or_ts_value_69
        # real
        var_gfunction_g_value_69 = 156.156
        obj.gfunction_g_value_69 = var_gfunction_g_value_69
        # real
        var_gfunction_lnt_or_ts_value_70 = 157.157
        obj.gfunction_lnt_or_ts_value_70 = var_gfunction_lnt_or_ts_value_70
        # real
        var_gfunction_g_value_70 = 158.158
        obj.gfunction_g_value_70 = var_gfunction_g_value_70
        # real
        var_gfunction_lnt_or_ts_value_71 = 159.159
        obj.gfunction_lnt_or_ts_value_71 = var_gfunction_lnt_or_ts_value_71
        # real
        var_gfunction_g_value_71 = 160.16
        obj.gfunction_g_value_71 = var_gfunction_g_value_71
        # real
        var_gfunction_lnt_or_ts_value_72 = 161.161
        obj.gfunction_lnt_or_ts_value_72 = var_gfunction_lnt_or_ts_value_72
        # real
        var_gfunction_g_value_72 = 162.162
        obj.gfunction_g_value_72 = var_gfunction_g_value_72
        # real
        var_gfunction_lnt_or_ts_value_73 = 163.163
        obj.gfunction_lnt_or_ts_value_73 = var_gfunction_lnt_or_ts_value_73
        # real
        var_gfunction_g_value_73 = 164.164
        obj.gfunction_g_value_73 = var_gfunction_g_value_73
        # real
        var_gfunction_lnt_or_ts_value_74 = 165.165
        obj.gfunction_lnt_or_ts_value_74 = var_gfunction_lnt_or_ts_value_74
        # real
        var_gfunction_g_value_74 = 166.166
        obj.gfunction_g_value_74 = var_gfunction_g_value_74
        # real
        var_gfunction_lnt_or_ts_value_75 = 167.167
        obj.gfunction_lnt_or_ts_value_75 = var_gfunction_lnt_or_ts_value_75
        # real
        var_gfunction_g_value_75 = 168.168
        obj.gfunction_g_value_75 = var_gfunction_g_value_75
        # real
        var_gfunction_lnt_or_ts_value_76 = 169.169
        obj.gfunction_lnt_or_ts_value_76 = var_gfunction_lnt_or_ts_value_76
        # real
        var_gfunction_g_value_76 = 170.17
        obj.gfunction_g_value_76 = var_gfunction_g_value_76
        # real
        var_gfunction_lnt_or_ts_value_77 = 171.171
        obj.gfunction_lnt_or_ts_value_77 = var_gfunction_lnt_or_ts_value_77
        # real
        var_gfunction_g_value_77 = 172.172
        obj.gfunction_g_value_77 = var_gfunction_g_value_77
        # real
        var_gfunction_lnt_or_ts_value_78 = 173.173
        obj.gfunction_lnt_or_ts_value_78 = var_gfunction_lnt_or_ts_value_78
        # real
        var_gfunction_g_value_78 = 174.174
        obj.gfunction_g_value_78 = var_gfunction_g_value_78
        # real
        var_gfunction_lnt_or_ts_value_79 = 175.175
        obj.gfunction_lnt_or_ts_value_79 = var_gfunction_lnt_or_ts_value_79
        # real
        var_gfunction_g_value_79 = 176.176
        obj.gfunction_g_value_79 = var_gfunction_g_value_79
        # real
        var_gfunction_lnt_or_ts_value_80 = 177.177
        obj.gfunction_lnt_or_ts_value_80 = var_gfunction_lnt_or_ts_value_80
        # real
        var_gfunction_g_value_80 = 178.178
        obj.gfunction_g_value_80 = var_gfunction_g_value_80
        # real
        var_gfunction_lnt_or_ts_value_81 = 179.179
        obj.gfunction_lnt_or_ts_value_81 = var_gfunction_lnt_or_ts_value_81
        # real
        var_gfunction_g_value_81 = 180.18
        obj.gfunction_g_value_81 = var_gfunction_g_value_81
        # real
        var_gfunction_lnt_or_ts_value_82 = 181.181
        obj.gfunction_lnt_or_ts_value_82 = var_gfunction_lnt_or_ts_value_82
        # real
        var_gfunction_g_value_82 = 182.182
        obj.gfunction_g_value_82 = var_gfunction_g_value_82
        # real
        var_gfunction_lnt_or_ts_value_83 = 183.183
        obj.gfunction_lnt_or_ts_value_83 = var_gfunction_lnt_or_ts_value_83
        # real
        var_gfunction_g_value_83 = 184.184
        obj.gfunction_g_value_83 = var_gfunction_g_value_83
        # real
        var_gfunction_lnt_or_ts_value_84 = 185.185
        obj.gfunction_lnt_or_ts_value_84 = var_gfunction_lnt_or_ts_value_84
        # real
        var_gfunction_g_value_84 = 186.186
        obj.gfunction_g_value_84 = var_gfunction_g_value_84
        # real
        var_gfunction_lnt_or_ts_value_85 = 187.187
        obj.gfunction_lnt_or_ts_value_85 = var_gfunction_lnt_or_ts_value_85
        # real
        var_gfunction_g_value_85 = 188.188
        obj.gfunction_g_value_85 = var_gfunction_g_value_85
        # real
        var_gfunction_lnt_or_ts_value_86 = 189.189
        obj.gfunction_lnt_or_ts_value_86 = var_gfunction_lnt_or_ts_value_86
        # real
        var_gfunction_g_value_86 = 190.19
        obj.gfunction_g_value_86 = var_gfunction_g_value_86
        # real
        var_gfunction_lnt_or_ts_value_87 = 191.191
        obj.gfunction_lnt_or_ts_value_87 = var_gfunction_lnt_or_ts_value_87
        # real
        var_gfunction_g_value_87 = 192.192
        obj.gfunction_g_value_87 = var_gfunction_g_value_87
        # real
        var_gfunction_lnt_or_ts_value_88 = 193.193
        obj.gfunction_lnt_or_ts_value_88 = var_gfunction_lnt_or_ts_value_88
        # real
        var_gfunction_g_value_88 = 194.194
        obj.gfunction_g_value_88 = var_gfunction_g_value_88
        # real
        var_gfunction_lnt_or_ts_value_89 = 195.195
        obj.gfunction_lnt_or_ts_value_89 = var_gfunction_lnt_or_ts_value_89
        # real
        var_gfunction_g_value_89 = 196.196
        obj.gfunction_g_value_89 = var_gfunction_g_value_89
        # real
        var_gfunction_lnt_or_ts_value_90 = 197.197
        obj.gfunction_lnt_or_ts_value_90 = var_gfunction_lnt_or_ts_value_90
        # real
        var_gfunction_g_value_90 = 198.198
        obj.gfunction_g_value_90 = var_gfunction_g_value_90
        # real
        var_gfunction_lnt_or_ts_value_91 = 199.199
        obj.gfunction_lnt_or_ts_value_91 = var_gfunction_lnt_or_ts_value_91
        # real
        var_gfunction_g_value_91 = 200.2
        obj.gfunction_g_value_91 = var_gfunction_g_value_91
        # real
        var_gfunction_lnt_or_ts_value_92 = 201.201
        obj.gfunction_lnt_or_ts_value_92 = var_gfunction_lnt_or_ts_value_92
        # real
        var_gfunction_g_value_92 = 202.202
        obj.gfunction_g_value_92 = var_gfunction_g_value_92
        # real
        var_gfunction_lnt_or_ts_value_93 = 203.203
        obj.gfunction_lnt_or_ts_value_93 = var_gfunction_lnt_or_ts_value_93
        # real
        var_gfunction_g_value_93 = 204.204
        obj.gfunction_g_value_93 = var_gfunction_g_value_93
        # real
        var_gfunction_lnt_or_ts_value_94 = 205.205
        obj.gfunction_lnt_or_ts_value_94 = var_gfunction_lnt_or_ts_value_94
        # real
        var_gfunction_g_value_94 = 206.206
        obj.gfunction_g_value_94 = var_gfunction_g_value_94
        # real
        var_gfunction_lnt_or_ts_value_95 = 207.207
        obj.gfunction_lnt_or_ts_value_95 = var_gfunction_lnt_or_ts_value_95
        # real
        var_gfunction_g_value_95 = 208.208
        obj.gfunction_g_value_95 = var_gfunction_g_value_95
        # real
        var_gfunction_lnt_or_ts_value_96 = 209.209
        obj.gfunction_lnt_or_ts_value_96 = var_gfunction_lnt_or_ts_value_96
        # real
        var_gfunction_g_value_96 = 210.21
        obj.gfunction_g_value_96 = var_gfunction_g_value_96
        # real
        var_gfunction_lnt_or_ts_value_97 = 211.211
        obj.gfunction_lnt_or_ts_value_97 = var_gfunction_lnt_or_ts_value_97
        # real
        var_gfunction_g_value_97 = 212.212
        obj.gfunction_g_value_97 = var_gfunction_g_value_97
        # real
        var_gfunction_lnt_or_ts_value_98 = 213.213
        obj.gfunction_lnt_or_ts_value_98 = var_gfunction_lnt_or_ts_value_98
        # real
        var_gfunction_g_value_98 = 214.214
        obj.gfunction_g_value_98 = var_gfunction_g_value_98
        # real
        var_gfunction_lnt_or_ts_value_99 = 215.215
        obj.gfunction_lnt_or_ts_value_99 = var_gfunction_lnt_or_ts_value_99
        # real
        var_gfunction_g_value_99 = 216.216
        obj.gfunction_g_value_99 = var_gfunction_g_value_99
        # real
        var_gfunction_lnt_or_ts_value_100 = 217.217
        obj.gfunction_lnt_or_ts_value_100 = var_gfunction_lnt_or_ts_value_100
        # real
        var_gfunction_g_value_100 = 218.218
        obj.gfunction_g_value_100 = var_gfunction_g_value_100

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.groundheatexchangerverticals[0].name, var_name)
        self.assertEqual(idf2.groundheatexchangerverticals[0].inlet_node_name, var_inlet_node_name)
        self.assertEqual(idf2.groundheatexchangerverticals[0].outlet_node_name, var_outlet_node_name)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].design_flow_rate, var_design_flow_rate)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].number_of_bore_holes, var_number_of_bore_holes)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].bore_hole_length, var_bore_hole_length)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].bore_hole_radius, var_bore_hole_radius)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].ground_thermal_conductivity, var_ground_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].ground_thermal_heat_capacity, var_ground_thermal_heat_capacity)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].ground_temperature, var_ground_temperature)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].grout_thermal_conductivity, var_grout_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].pipe_thermal_conductivity, var_pipe_thermal_conductivity)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].pipe_out_diameter, var_pipe_out_diameter)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].utube_distance, var_utube_distance)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].pipe_thickness, var_pipe_thickness)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].maximum_length_of_simulation, var_maximum_length_of_simulation)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_reference_ratio, var_gfunction_reference_ratio)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].number_of_data_pairs_of_the_g_function, var_number_of_data_pairs_of_the_g_function)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_1, var_gfunction_lnt_or_ts_value_1)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_1, var_gfunction_g_value_1)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_2, var_gfunction_lnt_or_ts_value_2)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_2, var_gfunction_g_value_2)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_3, var_gfunction_lnt_or_ts_value_3)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_3, var_gfunction_g_value_3)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_4, var_gfunction_lnt_or_ts_value_4)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_4, var_gfunction_g_value_4)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_5, var_gfunction_lnt_or_ts_value_5)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_5, var_gfunction_g_value_5)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_6, var_gfunction_lnt_or_ts_value_6)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_6, var_gfunction_g_value_6)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_7, var_gfunction_lnt_or_ts_value_7)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_7, var_gfunction_g_value_7)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_8, var_gfunction_lnt_or_ts_value_8)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_8, var_gfunction_g_value_8)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_9, var_gfunction_lnt_or_ts_value_9)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_9, var_gfunction_g_value_9)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_10, var_gfunction_lnt_or_ts_value_10)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_10, var_gfunction_g_value_10)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_11, var_gfunction_lnt_or_ts_value_11)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_11, var_gfunction_g_value_11)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_12, var_gfunction_lnt_or_ts_value_12)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_12, var_gfunction_g_value_12)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_13, var_gfunction_lnt_or_ts_value_13)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_13, var_gfunction_g_value_13)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_14, var_gfunction_lnt_or_ts_value_14)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_14, var_gfunction_g_value_14)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_15, var_gfunction_lnt_or_ts_value_15)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_15, var_gfunction_g_value_15)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_16, var_gfunction_lnt_or_ts_value_16)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_16, var_gfunction_g_value_16)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_17, var_gfunction_lnt_or_ts_value_17)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_17, var_gfunction_g_value_17)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_18, var_gfunction_lnt_or_ts_value_18)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_18, var_gfunction_g_value_18)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_19, var_gfunction_lnt_or_ts_value_19)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_19, var_gfunction_g_value_19)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_20, var_gfunction_lnt_or_ts_value_20)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_20, var_gfunction_g_value_20)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_21, var_gfunction_lnt_or_ts_value_21)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_21, var_gfunction_g_value_21)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_22, var_gfunction_lnt_or_ts_value_22)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_22, var_gfunction_g_value_22)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_23, var_gfunction_lnt_or_ts_value_23)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_23, var_gfunction_g_value_23)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_24, var_gfunction_lnt_or_ts_value_24)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_24, var_gfunction_g_value_24)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_25, var_gfunction_lnt_or_ts_value_25)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_25, var_gfunction_g_value_25)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_26, var_gfunction_lnt_or_ts_value_26)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_26, var_gfunction_g_value_26)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_27, var_gfunction_lnt_or_ts_value_27)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_27, var_gfunction_g_value_27)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_28, var_gfunction_lnt_or_ts_value_28)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_28, var_gfunction_g_value_28)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_29, var_gfunction_lnt_or_ts_value_29)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_29, var_gfunction_g_value_29)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_30, var_gfunction_lnt_or_ts_value_30)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_30, var_gfunction_g_value_30)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_31, var_gfunction_lnt_or_ts_value_31)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_31, var_gfunction_g_value_31)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_32, var_gfunction_lnt_or_ts_value_32)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_32, var_gfunction_g_value_32)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_33, var_gfunction_lnt_or_ts_value_33)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_33, var_gfunction_g_value_33)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_34, var_gfunction_lnt_or_ts_value_34)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_34, var_gfunction_g_value_34)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_35, var_gfunction_lnt_or_ts_value_35)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_35, var_gfunction_g_value_35)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_36, var_gfunction_lnt_or_ts_value_36)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_36, var_gfunction_g_value_36)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_37, var_gfunction_lnt_or_ts_value_37)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_37, var_gfunction_g_value_37)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_38, var_gfunction_lnt_or_ts_value_38)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_38, var_gfunction_g_value_38)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_39, var_gfunction_lnt_or_ts_value_39)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_39, var_gfunction_g_value_39)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_40, var_gfunction_lnt_or_ts_value_40)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_40, var_gfunction_g_value_40)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_41, var_gfunction_lnt_or_ts_value_41)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_41, var_gfunction_g_value_41)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_42, var_gfunction_lnt_or_ts_value_42)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_42, var_gfunction_g_value_42)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_43, var_gfunction_lnt_or_ts_value_43)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_43, var_gfunction_g_value_43)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_44, var_gfunction_lnt_or_ts_value_44)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_44, var_gfunction_g_value_44)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_45, var_gfunction_lnt_or_ts_value_45)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_45, var_gfunction_g_value_45)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_46, var_gfunction_lnt_or_ts_value_46)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_46, var_gfunction_g_value_46)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_47, var_gfunction_lnt_or_ts_value_47)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_47, var_gfunction_g_value_47)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_48, var_gfunction_lnt_or_ts_value_48)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_48, var_gfunction_g_value_48)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_49, var_gfunction_lnt_or_ts_value_49)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_49, var_gfunction_g_value_49)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_50, var_gfunction_lnt_or_ts_value_50)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_50, var_gfunction_g_value_50)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_51, var_gfunction_lnt_or_ts_value_51)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_51, var_gfunction_g_value_51)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_52, var_gfunction_lnt_or_ts_value_52)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_52, var_gfunction_g_value_52)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_53, var_gfunction_lnt_or_ts_value_53)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_53, var_gfunction_g_value_53)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_54, var_gfunction_lnt_or_ts_value_54)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_54, var_gfunction_g_value_54)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_55, var_gfunction_lnt_or_ts_value_55)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_55, var_gfunction_g_value_55)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_56, var_gfunction_lnt_or_ts_value_56)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_56, var_gfunction_g_value_56)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_57, var_gfunction_lnt_or_ts_value_57)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_57, var_gfunction_g_value_57)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_58, var_gfunction_lnt_or_ts_value_58)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_58, var_gfunction_g_value_58)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_59, var_gfunction_lnt_or_ts_value_59)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_59, var_gfunction_g_value_59)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_60, var_gfunction_lnt_or_ts_value_60)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_60, var_gfunction_g_value_60)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_61, var_gfunction_lnt_or_ts_value_61)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_61, var_gfunction_g_value_61)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_62, var_gfunction_lnt_or_ts_value_62)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_62, var_gfunction_g_value_62)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_63, var_gfunction_lnt_or_ts_value_63)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_63, var_gfunction_g_value_63)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_64, var_gfunction_lnt_or_ts_value_64)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_64, var_gfunction_g_value_64)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_65, var_gfunction_lnt_or_ts_value_65)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_65, var_gfunction_g_value_65)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_66, var_gfunction_lnt_or_ts_value_66)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_66, var_gfunction_g_value_66)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_67, var_gfunction_lnt_or_ts_value_67)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_67, var_gfunction_g_value_67)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_68, var_gfunction_lnt_or_ts_value_68)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_68, var_gfunction_g_value_68)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_69, var_gfunction_lnt_or_ts_value_69)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_69, var_gfunction_g_value_69)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_70, var_gfunction_lnt_or_ts_value_70)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_70, var_gfunction_g_value_70)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_71, var_gfunction_lnt_or_ts_value_71)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_71, var_gfunction_g_value_71)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_72, var_gfunction_lnt_or_ts_value_72)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_72, var_gfunction_g_value_72)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_73, var_gfunction_lnt_or_ts_value_73)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_73, var_gfunction_g_value_73)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_74, var_gfunction_lnt_or_ts_value_74)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_74, var_gfunction_g_value_74)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_75, var_gfunction_lnt_or_ts_value_75)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_75, var_gfunction_g_value_75)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_76, var_gfunction_lnt_or_ts_value_76)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_76, var_gfunction_g_value_76)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_77, var_gfunction_lnt_or_ts_value_77)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_77, var_gfunction_g_value_77)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_78, var_gfunction_lnt_or_ts_value_78)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_78, var_gfunction_g_value_78)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_79, var_gfunction_lnt_or_ts_value_79)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_79, var_gfunction_g_value_79)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_80, var_gfunction_lnt_or_ts_value_80)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_80, var_gfunction_g_value_80)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_81, var_gfunction_lnt_or_ts_value_81)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_81, var_gfunction_g_value_81)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_82, var_gfunction_lnt_or_ts_value_82)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_82, var_gfunction_g_value_82)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_83, var_gfunction_lnt_or_ts_value_83)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_83, var_gfunction_g_value_83)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_84, var_gfunction_lnt_or_ts_value_84)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_84, var_gfunction_g_value_84)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_85, var_gfunction_lnt_or_ts_value_85)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_85, var_gfunction_g_value_85)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_86, var_gfunction_lnt_or_ts_value_86)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_86, var_gfunction_g_value_86)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_87, var_gfunction_lnt_or_ts_value_87)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_87, var_gfunction_g_value_87)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_88, var_gfunction_lnt_or_ts_value_88)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_88, var_gfunction_g_value_88)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_89, var_gfunction_lnt_or_ts_value_89)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_89, var_gfunction_g_value_89)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_90, var_gfunction_lnt_or_ts_value_90)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_90, var_gfunction_g_value_90)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_91, var_gfunction_lnt_or_ts_value_91)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_91, var_gfunction_g_value_91)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_92, var_gfunction_lnt_or_ts_value_92)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_92, var_gfunction_g_value_92)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_93, var_gfunction_lnt_or_ts_value_93)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_93, var_gfunction_g_value_93)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_94, var_gfunction_lnt_or_ts_value_94)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_94, var_gfunction_g_value_94)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_95, var_gfunction_lnt_or_ts_value_95)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_95, var_gfunction_g_value_95)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_96, var_gfunction_lnt_or_ts_value_96)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_96, var_gfunction_g_value_96)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_97, var_gfunction_lnt_or_ts_value_97)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_97, var_gfunction_g_value_97)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_98, var_gfunction_lnt_or_ts_value_98)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_98, var_gfunction_g_value_98)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_99, var_gfunction_lnt_or_ts_value_99)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_99, var_gfunction_g_value_99)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_lnt_or_ts_value_100, var_gfunction_lnt_or_ts_value_100)
        self.assertAlmostEqual(idf2.groundheatexchangerverticals[0].gfunction_g_value_100, var_gfunction_g_value_100)