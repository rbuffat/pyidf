import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.fluid_properties import FluidPropertiesSuperheated

log = logging.getLogger(__name__)

class TestFluidPropertiesSuperheated(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fluidpropertiessuperheated(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FluidPropertiesSuperheated()
        # object-list
        var_fluid_name = "object-list|Fluid Name"
        obj.fluid_name = var_fluid_name
        # alpha
        var_fluid_property_type = "Enthalpy"
        obj.fluid_property_type = var_fluid_property_type
        # object-list
        var_temperature_values_name = "object-list|Temperature Values Name"
        obj.temperature_values_name = var_temperature_values_name
        # real
        var_pressure = 0.0001
        obj.pressure = var_pressure
        # real
        var_property_value_1 = 5.5
        obj.property_value_1 = var_property_value_1
        # real
        var_property_value_2 = 6.6
        obj.property_value_2 = var_property_value_2
        # real
        var_property_value_3 = 7.7
        obj.property_value_3 = var_property_value_3
        # real
        var_property_value_4 = 8.8
        obj.property_value_4 = var_property_value_4
        # real
        var_property_value_5 = 9.9
        obj.property_value_5 = var_property_value_5
        # real
        var_property_value_6 = 10.1
        obj.property_value_6 = var_property_value_6
        # real
        var_property_value_7 = 11.11
        obj.property_value_7 = var_property_value_7
        # real
        var_property_value_8 = 12.12
        obj.property_value_8 = var_property_value_8
        # real
        var_property_value_9 = 13.13
        obj.property_value_9 = var_property_value_9
        # real
        var_property_value_10 = 14.14
        obj.property_value_10 = var_property_value_10
        # real
        var_property_value_11 = 15.15
        obj.property_value_11 = var_property_value_11
        # real
        var_property_value_12 = 16.16
        obj.property_value_12 = var_property_value_12
        # real
        var_property_value_13 = 17.17
        obj.property_value_13 = var_property_value_13
        # real
        var_property_value_14 = 18.18
        obj.property_value_14 = var_property_value_14
        # real
        var_property_value_15 = 19.19
        obj.property_value_15 = var_property_value_15
        # real
        var_property_value_16 = 20.2
        obj.property_value_16 = var_property_value_16
        # real
        var_property_value_17 = 21.21
        obj.property_value_17 = var_property_value_17
        # real
        var_property_value_18 = 22.22
        obj.property_value_18 = var_property_value_18
        # real
        var_property_value_19 = 23.23
        obj.property_value_19 = var_property_value_19
        # real
        var_property_value_20 = 24.24
        obj.property_value_20 = var_property_value_20
        # real
        var_property_value_21 = 25.25
        obj.property_value_21 = var_property_value_21
        # real
        var_property_value_22 = 26.26
        obj.property_value_22 = var_property_value_22
        # real
        var_property_value_23 = 27.27
        obj.property_value_23 = var_property_value_23
        # real
        var_property_value_24 = 28.28
        obj.property_value_24 = var_property_value_24
        # real
        var_property_value_25 = 29.29
        obj.property_value_25 = var_property_value_25
        # real
        var_property_value_26 = 30.3
        obj.property_value_26 = var_property_value_26
        # real
        var_property_value_27 = 31.31
        obj.property_value_27 = var_property_value_27
        # real
        var_property_value_28 = 32.32
        obj.property_value_28 = var_property_value_28
        # real
        var_property_value_29 = 33.33
        obj.property_value_29 = var_property_value_29
        # real
        var_property_value_30 = 34.34
        obj.property_value_30 = var_property_value_30
        # real
        var_property_value_31 = 35.35
        obj.property_value_31 = var_property_value_31
        # real
        var_property_value_32 = 36.36
        obj.property_value_32 = var_property_value_32
        # real
        var_property_value_33 = 37.37
        obj.property_value_33 = var_property_value_33
        # real
        var_property_value_34 = 38.38
        obj.property_value_34 = var_property_value_34
        # real
        var_property_value_35 = 39.39
        obj.property_value_35 = var_property_value_35
        # real
        var_property_value_36 = 40.4
        obj.property_value_36 = var_property_value_36
        # real
        var_property_value_37 = 41.41
        obj.property_value_37 = var_property_value_37
        # real
        var_property_value_38 = 42.42
        obj.property_value_38 = var_property_value_38
        # real
        var_property_value_39 = 43.43
        obj.property_value_39 = var_property_value_39
        # real
        var_property_value_40 = 44.44
        obj.property_value_40 = var_property_value_40
        # real
        var_property_value_41 = 45.45
        obj.property_value_41 = var_property_value_41
        # real
        var_property_value_42 = 46.46
        obj.property_value_42 = var_property_value_42
        # real
        var_property_value_43 = 47.47
        obj.property_value_43 = var_property_value_43
        # real
        var_property_value_44 = 48.48
        obj.property_value_44 = var_property_value_44
        # real
        var_property_value_45 = 49.49
        obj.property_value_45 = var_property_value_45
        # real
        var_property_value_46 = 50.5
        obj.property_value_46 = var_property_value_46
        # real
        var_property_value_47 = 51.51
        obj.property_value_47 = var_property_value_47
        # real
        var_property_value_48 = 52.52
        obj.property_value_48 = var_property_value_48
        # real
        var_property_value_49 = 53.53
        obj.property_value_49 = var_property_value_49
        # real
        var_property_value_50 = 54.54
        obj.property_value_50 = var_property_value_50
        # real
        var_property_value_51 = 55.55
        obj.property_value_51 = var_property_value_51
        # real
        var_property_value_52 = 56.56
        obj.property_value_52 = var_property_value_52
        # real
        var_property_value_53 = 57.57
        obj.property_value_53 = var_property_value_53
        # real
        var_property_value_54 = 58.58
        obj.property_value_54 = var_property_value_54
        # real
        var_property_value_55 = 59.59
        obj.property_value_55 = var_property_value_55
        # real
        var_property_value_56 = 60.6
        obj.property_value_56 = var_property_value_56
        # real
        var_property_value_57 = 61.61
        obj.property_value_57 = var_property_value_57
        # real
        var_property_value_58 = 62.62
        obj.property_value_58 = var_property_value_58
        # real
        var_property_value_59 = 63.63
        obj.property_value_59 = var_property_value_59
        # real
        var_property_value_60 = 64.64
        obj.property_value_60 = var_property_value_60
        # real
        var_property_value_61 = 65.65
        obj.property_value_61 = var_property_value_61
        # real
        var_property_value_62 = 66.66
        obj.property_value_62 = var_property_value_62
        # real
        var_property_value_63 = 67.67
        obj.property_value_63 = var_property_value_63
        # real
        var_property_value_64 = 68.68
        obj.property_value_64 = var_property_value_64
        # real
        var_property_value_65 = 69.69
        obj.property_value_65 = var_property_value_65
        # real
        var_property_value_66 = 70.7
        obj.property_value_66 = var_property_value_66
        # real
        var_property_value_67 = 71.71
        obj.property_value_67 = var_property_value_67
        # real
        var_property_value_68 = 72.72
        obj.property_value_68 = var_property_value_68
        # real
        var_property_value_69 = 73.73
        obj.property_value_69 = var_property_value_69
        # real
        var_property_value_70 = 74.74
        obj.property_value_70 = var_property_value_70
        # real
        var_property_value_71 = 75.75
        obj.property_value_71 = var_property_value_71
        # real
        var_property_value_72 = 76.76
        obj.property_value_72 = var_property_value_72
        # real
        var_property_value_73 = 77.77
        obj.property_value_73 = var_property_value_73
        # real
        var_property_value_74 = 78.78
        obj.property_value_74 = var_property_value_74
        # real
        var_property_value_75 = 79.79
        obj.property_value_75 = var_property_value_75
        # real
        var_property_value_76 = 80.8
        obj.property_value_76 = var_property_value_76
        # real
        var_property_value_77 = 81.81
        obj.property_value_77 = var_property_value_77
        # real
        var_property_value_78 = 82.82
        obj.property_value_78 = var_property_value_78
        # real
        var_property_value_79 = 83.83
        obj.property_value_79 = var_property_value_79
        # real
        var_property_value_80 = 84.84
        obj.property_value_80 = var_property_value_80
        # real
        var_property_value_81 = 85.85
        obj.property_value_81 = var_property_value_81
        # real
        var_property_value_82 = 86.86
        obj.property_value_82 = var_property_value_82
        # real
        var_property_value_83 = 87.87
        obj.property_value_83 = var_property_value_83
        # real
        var_property_value_84 = 88.88
        obj.property_value_84 = var_property_value_84
        # real
        var_property_value_85 = 89.89
        obj.property_value_85 = var_property_value_85
        # real
        var_property_value_86 = 90.9
        obj.property_value_86 = var_property_value_86
        # real
        var_property_value_87 = 91.91
        obj.property_value_87 = var_property_value_87
        # real
        var_property_value_88 = 92.92
        obj.property_value_88 = var_property_value_88
        # real
        var_property_value_89 = 93.93
        obj.property_value_89 = var_property_value_89
        # real
        var_property_value_90 = 94.94
        obj.property_value_90 = var_property_value_90
        # real
        var_property_value_91 = 95.95
        obj.property_value_91 = var_property_value_91
        # real
        var_property_value_92 = 96.96
        obj.property_value_92 = var_property_value_92
        # real
        var_property_value_93 = 97.97
        obj.property_value_93 = var_property_value_93
        # real
        var_property_value_94 = 98.98
        obj.property_value_94 = var_property_value_94
        # real
        var_property_value_95 = 99.99
        obj.property_value_95 = var_property_value_95
        # real
        var_property_value_96 = 100.1
        obj.property_value_96 = var_property_value_96
        # real
        var_property_value_97 = 101.101
        obj.property_value_97 = var_property_value_97
        # real
        var_property_value_98 = 102.102
        obj.property_value_98 = var_property_value_98
        # real
        var_property_value_99 = 103.103
        obj.property_value_99 = var_property_value_99
        # real
        var_property_value_100 = 104.104
        obj.property_value_100 = var_property_value_100
        # real
        var_property_value_101 = 105.105
        obj.property_value_101 = var_property_value_101
        # real
        var_property_value_102 = 106.106
        obj.property_value_102 = var_property_value_102
        # real
        var_property_value_103 = 107.107
        obj.property_value_103 = var_property_value_103
        # real
        var_property_value_104 = 108.108
        obj.property_value_104 = var_property_value_104
        # real
        var_property_value_105 = 109.109
        obj.property_value_105 = var_property_value_105
        # real
        var_property_value_106 = 110.11
        obj.property_value_106 = var_property_value_106
        # real
        var_property_value_107 = 111.111
        obj.property_value_107 = var_property_value_107
        # real
        var_property_value_108 = 112.112
        obj.property_value_108 = var_property_value_108
        # real
        var_property_value_109 = 113.113
        obj.property_value_109 = var_property_value_109
        # real
        var_property_value_110 = 114.114
        obj.property_value_110 = var_property_value_110
        # real
        var_property_value_111 = 115.115
        obj.property_value_111 = var_property_value_111
        # real
        var_property_value_112 = 116.116
        obj.property_value_112 = var_property_value_112
        # real
        var_property_value_113 = 117.117
        obj.property_value_113 = var_property_value_113
        # real
        var_property_value_114 = 118.118
        obj.property_value_114 = var_property_value_114
        # real
        var_property_value_115 = 119.119
        obj.property_value_115 = var_property_value_115
        # real
        var_property_value_116 = 120.12
        obj.property_value_116 = var_property_value_116
        # real
        var_property_value_117 = 121.121
        obj.property_value_117 = var_property_value_117
        # real
        var_property_value_118 = 122.122
        obj.property_value_118 = var_property_value_118
        # real
        var_property_value_119 = 123.123
        obj.property_value_119 = var_property_value_119
        # real
        var_property_value_120 = 124.124
        obj.property_value_120 = var_property_value_120
        # real
        var_property_value_121 = 125.125
        obj.property_value_121 = var_property_value_121
        # real
        var_property_value_122 = 126.126
        obj.property_value_122 = var_property_value_122
        # real
        var_property_value_123 = 127.127
        obj.property_value_123 = var_property_value_123
        # real
        var_property_value_124 = 128.128
        obj.property_value_124 = var_property_value_124
        # real
        var_property_value_125 = 129.129
        obj.property_value_125 = var_property_value_125
        # real
        var_property_value_126 = 130.13
        obj.property_value_126 = var_property_value_126
        # real
        var_property_value_127 = 131.131
        obj.property_value_127 = var_property_value_127
        # real
        var_property_value_128 = 132.132
        obj.property_value_128 = var_property_value_128
        # real
        var_property_value_129 = 133.133
        obj.property_value_129 = var_property_value_129
        # real
        var_property_value_130 = 134.134
        obj.property_value_130 = var_property_value_130
        # real
        var_property_value_131 = 135.135
        obj.property_value_131 = var_property_value_131
        # real
        var_property_value_132 = 136.136
        obj.property_value_132 = var_property_value_132
        # real
        var_property_value_133 = 137.137
        obj.property_value_133 = var_property_value_133
        # real
        var_property_value_134 = 138.138
        obj.property_value_134 = var_property_value_134
        # real
        var_property_value_135 = 139.139
        obj.property_value_135 = var_property_value_135
        # real
        var_property_value_136 = 140.14
        obj.property_value_136 = var_property_value_136
        # real
        var_property_value_137 = 141.141
        obj.property_value_137 = var_property_value_137
        # real
        var_property_value_138 = 142.142
        obj.property_value_138 = var_property_value_138
        # real
        var_property_value_139 = 143.143
        obj.property_value_139 = var_property_value_139
        # real
        var_property_value_140 = 144.144
        obj.property_value_140 = var_property_value_140
        # real
        var_property_value_141 = 145.145
        obj.property_value_141 = var_property_value_141
        # real
        var_property_value_142 = 146.146
        obj.property_value_142 = var_property_value_142
        # real
        var_property_value_143 = 147.147
        obj.property_value_143 = var_property_value_143
        # real
        var_property_value_144 = 148.148
        obj.property_value_144 = var_property_value_144
        # real
        var_property_value_145 = 149.149
        obj.property_value_145 = var_property_value_145
        # real
        var_property_value_146 = 150.15
        obj.property_value_146 = var_property_value_146
        # real
        var_property_value_147 = 151.151
        obj.property_value_147 = var_property_value_147
        # real
        var_property_value_148 = 152.152
        obj.property_value_148 = var_property_value_148
        # real
        var_property_value_149 = 153.153
        obj.property_value_149 = var_property_value_149
        # real
        var_property_value_150 = 154.154
        obj.property_value_150 = var_property_value_150
        # real
        var_property_value_151 = 155.155
        obj.property_value_151 = var_property_value_151
        # real
        var_property_value_152 = 156.156
        obj.property_value_152 = var_property_value_152
        # real
        var_property_value_153 = 157.157
        obj.property_value_153 = var_property_value_153
        # real
        var_property_value_154 = 158.158
        obj.property_value_154 = var_property_value_154
        # real
        var_property_value_155 = 159.159
        obj.property_value_155 = var_property_value_155
        # real
        var_property_value_156 = 160.16
        obj.property_value_156 = var_property_value_156
        # real
        var_property_value_157 = 161.161
        obj.property_value_157 = var_property_value_157
        # real
        var_property_value_158 = 162.162
        obj.property_value_158 = var_property_value_158
        # real
        var_property_value_159 = 163.163
        obj.property_value_159 = var_property_value_159
        # real
        var_property_value_160 = 164.164
        obj.property_value_160 = var_property_value_160
        # real
        var_property_value_161 = 165.165
        obj.property_value_161 = var_property_value_161
        # real
        var_property_value_162 = 166.166
        obj.property_value_162 = var_property_value_162
        # real
        var_property_value_163 = 167.167
        obj.property_value_163 = var_property_value_163
        # real
        var_property_value_164 = 168.168
        obj.property_value_164 = var_property_value_164
        # real
        var_property_value_165 = 169.169
        obj.property_value_165 = var_property_value_165
        # real
        var_property_value_166 = 170.17
        obj.property_value_166 = var_property_value_166
        # real
        var_property_value_167 = 171.171
        obj.property_value_167 = var_property_value_167
        # real
        var_property_value_168 = 172.172
        obj.property_value_168 = var_property_value_168
        # real
        var_property_value_169 = 173.173
        obj.property_value_169 = var_property_value_169
        # real
        var_property_value_170 = 174.174
        obj.property_value_170 = var_property_value_170
        # real
        var_property_value_171 = 175.175
        obj.property_value_171 = var_property_value_171
        # real
        var_property_value_172 = 176.176
        obj.property_value_172 = var_property_value_172
        # real
        var_property_value_173 = 177.177
        obj.property_value_173 = var_property_value_173
        # real
        var_property_value_174 = 178.178
        obj.property_value_174 = var_property_value_174
        # real
        var_property_value_175 = 179.179
        obj.property_value_175 = var_property_value_175
        # real
        var_property_value_176 = 180.18
        obj.property_value_176 = var_property_value_176
        # real
        var_property_value_177 = 181.181
        obj.property_value_177 = var_property_value_177
        # real
        var_property_value_178 = 182.182
        obj.property_value_178 = var_property_value_178
        # real
        var_property_value_179 = 183.183
        obj.property_value_179 = var_property_value_179
        # real
        var_property_value_180 = 184.184
        obj.property_value_180 = var_property_value_180
        # real
        var_property_value_181 = 185.185
        obj.property_value_181 = var_property_value_181
        # real
        var_property_value_182 = 186.186
        obj.property_value_182 = var_property_value_182
        # real
        var_property_value_183 = 187.187
        obj.property_value_183 = var_property_value_183
        # real
        var_property_value_184 = 188.188
        obj.property_value_184 = var_property_value_184
        # real
        var_property_value_185 = 189.189
        obj.property_value_185 = var_property_value_185
        # real
        var_property_value_186 = 190.19
        obj.property_value_186 = var_property_value_186
        # real
        var_property_value_187 = 191.191
        obj.property_value_187 = var_property_value_187
        # real
        var_property_value_188 = 192.192
        obj.property_value_188 = var_property_value_188
        # real
        var_property_value_189 = 193.193
        obj.property_value_189 = var_property_value_189
        # real
        var_property_value_190 = 194.194
        obj.property_value_190 = var_property_value_190
        # real
        var_property_value_191 = 195.195
        obj.property_value_191 = var_property_value_191
        # real
        var_property_value_192 = 196.196
        obj.property_value_192 = var_property_value_192
        # real
        var_property_value_193 = 197.197
        obj.property_value_193 = var_property_value_193
        # real
        var_property_value_194 = 198.198
        obj.property_value_194 = var_property_value_194
        # real
        var_property_value_195 = 199.199
        obj.property_value_195 = var_property_value_195
        # real
        var_property_value_196 = 200.2
        obj.property_value_196 = var_property_value_196
        # real
        var_property_value_197 = 201.201
        obj.property_value_197 = var_property_value_197
        # real
        var_property_value_198 = 202.202
        obj.property_value_198 = var_property_value_198
        # real
        var_property_value_199 = 203.203
        obj.property_value_199 = var_property_value_199
        # real
        var_property_value_200 = 204.204
        obj.property_value_200 = var_property_value_200
        # real
        var_property_value_201 = 205.205
        obj.property_value_201 = var_property_value_201
        # real
        var_property_value_202 = 206.206
        obj.property_value_202 = var_property_value_202
        # real
        var_property_value_203 = 207.207
        obj.property_value_203 = var_property_value_203
        # real
        var_property_value_204 = 208.208
        obj.property_value_204 = var_property_value_204
        # real
        var_property_value_205 = 209.209
        obj.property_value_205 = var_property_value_205
        # real
        var_property_value_206 = 210.21
        obj.property_value_206 = var_property_value_206
        # real
        var_property_value_207 = 211.211
        obj.property_value_207 = var_property_value_207
        # real
        var_property_value_208 = 212.212
        obj.property_value_208 = var_property_value_208
        # real
        var_property_value_209 = 213.213
        obj.property_value_209 = var_property_value_209
        # real
        var_property_value_210 = 214.214
        obj.property_value_210 = var_property_value_210
        # real
        var_property_value_211 = 215.215
        obj.property_value_211 = var_property_value_211
        # real
        var_property_value_212 = 216.216
        obj.property_value_212 = var_property_value_212
        # real
        var_property_value_213 = 217.217
        obj.property_value_213 = var_property_value_213
        # real
        var_property_value_214 = 218.218
        obj.property_value_214 = var_property_value_214
        # real
        var_property_value_215 = 219.219
        obj.property_value_215 = var_property_value_215
        # real
        var_property_value_216 = 220.22
        obj.property_value_216 = var_property_value_216
        # real
        var_property_value_217 = 221.221
        obj.property_value_217 = var_property_value_217
        # real
        var_property_value_218 = 222.222
        obj.property_value_218 = var_property_value_218
        # real
        var_property_value_219 = 223.223
        obj.property_value_219 = var_property_value_219
        # real
        var_property_value_220 = 224.224
        obj.property_value_220 = var_property_value_220
        # real
        var_property_value_221 = 225.225
        obj.property_value_221 = var_property_value_221
        # real
        var_property_value_222 = 226.226
        obj.property_value_222 = var_property_value_222
        # real
        var_property_value_223 = 227.227
        obj.property_value_223 = var_property_value_223
        # real
        var_property_value_224 = 228.228
        obj.property_value_224 = var_property_value_224
        # real
        var_property_value_225 = 229.229
        obj.property_value_225 = var_property_value_225
        # real
        var_property_value_226 = 230.23
        obj.property_value_226 = var_property_value_226
        # real
        var_property_value_227 = 231.231
        obj.property_value_227 = var_property_value_227
        # real
        var_property_value_228 = 232.232
        obj.property_value_228 = var_property_value_228
        # real
        var_property_value_229 = 233.233
        obj.property_value_229 = var_property_value_229
        # real
        var_property_value_230 = 234.234
        obj.property_value_230 = var_property_value_230
        # real
        var_property_value_231 = 235.235
        obj.property_value_231 = var_property_value_231
        # real
        var_property_value_232 = 236.236
        obj.property_value_232 = var_property_value_232
        # real
        var_property_value_233 = 237.237
        obj.property_value_233 = var_property_value_233
        # real
        var_property_value_234 = 238.238
        obj.property_value_234 = var_property_value_234
        # real
        var_property_value_235 = 239.239
        obj.property_value_235 = var_property_value_235
        # real
        var_property_value_236 = 240.24
        obj.property_value_236 = var_property_value_236
        # real
        var_property_value_237 = 241.241
        obj.property_value_237 = var_property_value_237
        # real
        var_property_value_238 = 242.242
        obj.property_value_238 = var_property_value_238
        # real
        var_property_value_239 = 243.243
        obj.property_value_239 = var_property_value_239
        # real
        var_property_value_240 = 244.244
        obj.property_value_240 = var_property_value_240
        # real
        var_property_value_241 = 245.245
        obj.property_value_241 = var_property_value_241
        # real
        var_property_value_242 = 246.246
        obj.property_value_242 = var_property_value_242
        # real
        var_property_value_243 = 247.247
        obj.property_value_243 = var_property_value_243
        # real
        var_property_value_244 = 248.248
        obj.property_value_244 = var_property_value_244
        # real
        var_property_value_245 = 249.249
        obj.property_value_245 = var_property_value_245
        # real
        var_property_value_246 = 250.25
        obj.property_value_246 = var_property_value_246
        # real
        var_property_value_247 = 251.251
        obj.property_value_247 = var_property_value_247
        # real
        var_property_value_248 = 252.252
        obj.property_value_248 = var_property_value_248
        # real
        var_property_value_249 = 253.253
        obj.property_value_249 = var_property_value_249
        # real
        var_property_value_250 = 254.254
        obj.property_value_250 = var_property_value_250

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fluidpropertiessuperheateds[0].fluid_name, var_fluid_name)
        self.assertEqual(idf2.fluidpropertiessuperheateds[0].fluid_property_type, var_fluid_property_type)
        self.assertEqual(idf2.fluidpropertiessuperheateds[0].temperature_values_name, var_temperature_values_name)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].pressure, var_pressure)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_1, var_property_value_1)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_2, var_property_value_2)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_3, var_property_value_3)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_4, var_property_value_4)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_5, var_property_value_5)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_6, var_property_value_6)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_7, var_property_value_7)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_8, var_property_value_8)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_9, var_property_value_9)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_10, var_property_value_10)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_11, var_property_value_11)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_12, var_property_value_12)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_13, var_property_value_13)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_14, var_property_value_14)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_15, var_property_value_15)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_16, var_property_value_16)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_17, var_property_value_17)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_18, var_property_value_18)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_19, var_property_value_19)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_20, var_property_value_20)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_21, var_property_value_21)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_22, var_property_value_22)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_23, var_property_value_23)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_24, var_property_value_24)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_25, var_property_value_25)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_26, var_property_value_26)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_27, var_property_value_27)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_28, var_property_value_28)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_29, var_property_value_29)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_30, var_property_value_30)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_31, var_property_value_31)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_32, var_property_value_32)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_33, var_property_value_33)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_34, var_property_value_34)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_35, var_property_value_35)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_36, var_property_value_36)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_37, var_property_value_37)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_38, var_property_value_38)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_39, var_property_value_39)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_40, var_property_value_40)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_41, var_property_value_41)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_42, var_property_value_42)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_43, var_property_value_43)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_44, var_property_value_44)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_45, var_property_value_45)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_46, var_property_value_46)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_47, var_property_value_47)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_48, var_property_value_48)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_49, var_property_value_49)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_50, var_property_value_50)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_51, var_property_value_51)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_52, var_property_value_52)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_53, var_property_value_53)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_54, var_property_value_54)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_55, var_property_value_55)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_56, var_property_value_56)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_57, var_property_value_57)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_58, var_property_value_58)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_59, var_property_value_59)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_60, var_property_value_60)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_61, var_property_value_61)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_62, var_property_value_62)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_63, var_property_value_63)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_64, var_property_value_64)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_65, var_property_value_65)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_66, var_property_value_66)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_67, var_property_value_67)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_68, var_property_value_68)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_69, var_property_value_69)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_70, var_property_value_70)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_71, var_property_value_71)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_72, var_property_value_72)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_73, var_property_value_73)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_74, var_property_value_74)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_75, var_property_value_75)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_76, var_property_value_76)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_77, var_property_value_77)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_78, var_property_value_78)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_79, var_property_value_79)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_80, var_property_value_80)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_81, var_property_value_81)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_82, var_property_value_82)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_83, var_property_value_83)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_84, var_property_value_84)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_85, var_property_value_85)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_86, var_property_value_86)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_87, var_property_value_87)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_88, var_property_value_88)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_89, var_property_value_89)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_90, var_property_value_90)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_91, var_property_value_91)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_92, var_property_value_92)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_93, var_property_value_93)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_94, var_property_value_94)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_95, var_property_value_95)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_96, var_property_value_96)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_97, var_property_value_97)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_98, var_property_value_98)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_99, var_property_value_99)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_100, var_property_value_100)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_101, var_property_value_101)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_102, var_property_value_102)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_103, var_property_value_103)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_104, var_property_value_104)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_105, var_property_value_105)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_106, var_property_value_106)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_107, var_property_value_107)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_108, var_property_value_108)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_109, var_property_value_109)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_110, var_property_value_110)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_111, var_property_value_111)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_112, var_property_value_112)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_113, var_property_value_113)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_114, var_property_value_114)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_115, var_property_value_115)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_116, var_property_value_116)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_117, var_property_value_117)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_118, var_property_value_118)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_119, var_property_value_119)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_120, var_property_value_120)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_121, var_property_value_121)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_122, var_property_value_122)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_123, var_property_value_123)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_124, var_property_value_124)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_125, var_property_value_125)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_126, var_property_value_126)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_127, var_property_value_127)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_128, var_property_value_128)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_129, var_property_value_129)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_130, var_property_value_130)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_131, var_property_value_131)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_132, var_property_value_132)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_133, var_property_value_133)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_134, var_property_value_134)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_135, var_property_value_135)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_136, var_property_value_136)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_137, var_property_value_137)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_138, var_property_value_138)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_139, var_property_value_139)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_140, var_property_value_140)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_141, var_property_value_141)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_142, var_property_value_142)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_143, var_property_value_143)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_144, var_property_value_144)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_145, var_property_value_145)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_146, var_property_value_146)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_147, var_property_value_147)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_148, var_property_value_148)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_149, var_property_value_149)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_150, var_property_value_150)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_151, var_property_value_151)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_152, var_property_value_152)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_153, var_property_value_153)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_154, var_property_value_154)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_155, var_property_value_155)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_156, var_property_value_156)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_157, var_property_value_157)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_158, var_property_value_158)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_159, var_property_value_159)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_160, var_property_value_160)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_161, var_property_value_161)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_162, var_property_value_162)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_163, var_property_value_163)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_164, var_property_value_164)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_165, var_property_value_165)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_166, var_property_value_166)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_167, var_property_value_167)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_168, var_property_value_168)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_169, var_property_value_169)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_170, var_property_value_170)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_171, var_property_value_171)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_172, var_property_value_172)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_173, var_property_value_173)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_174, var_property_value_174)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_175, var_property_value_175)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_176, var_property_value_176)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_177, var_property_value_177)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_178, var_property_value_178)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_179, var_property_value_179)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_180, var_property_value_180)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_181, var_property_value_181)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_182, var_property_value_182)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_183, var_property_value_183)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_184, var_property_value_184)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_185, var_property_value_185)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_186, var_property_value_186)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_187, var_property_value_187)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_188, var_property_value_188)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_189, var_property_value_189)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_190, var_property_value_190)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_191, var_property_value_191)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_192, var_property_value_192)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_193, var_property_value_193)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_194, var_property_value_194)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_195, var_property_value_195)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_196, var_property_value_196)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_197, var_property_value_197)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_198, var_property_value_198)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_199, var_property_value_199)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_200, var_property_value_200)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_201, var_property_value_201)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_202, var_property_value_202)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_203, var_property_value_203)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_204, var_property_value_204)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_205, var_property_value_205)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_206, var_property_value_206)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_207, var_property_value_207)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_208, var_property_value_208)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_209, var_property_value_209)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_210, var_property_value_210)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_211, var_property_value_211)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_212, var_property_value_212)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_213, var_property_value_213)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_214, var_property_value_214)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_215, var_property_value_215)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_216, var_property_value_216)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_217, var_property_value_217)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_218, var_property_value_218)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_219, var_property_value_219)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_220, var_property_value_220)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_221, var_property_value_221)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_222, var_property_value_222)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_223, var_property_value_223)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_224, var_property_value_224)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_225, var_property_value_225)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_226, var_property_value_226)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_227, var_property_value_227)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_228, var_property_value_228)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_229, var_property_value_229)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_230, var_property_value_230)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_231, var_property_value_231)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_232, var_property_value_232)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_233, var_property_value_233)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_234, var_property_value_234)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_235, var_property_value_235)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_236, var_property_value_236)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_237, var_property_value_237)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_238, var_property_value_238)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_239, var_property_value_239)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_240, var_property_value_240)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_241, var_property_value_241)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_242, var_property_value_242)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_243, var_property_value_243)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_244, var_property_value_244)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_245, var_property_value_245)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_246, var_property_value_246)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_247, var_property_value_247)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_248, var_property_value_248)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_249, var_property_value_249)
        self.assertAlmostEqual(idf2.fluidpropertiessuperheateds[0].property_value_250, var_property_value_250)