import os
import tempfile
import unittest
import pyidf
from pyidf.fluid_properties import FluidPropertiesTemperatures
from pyidf import ValidationLevel
from pyidf.idf import IDF


class TestFluidPropertiesTemperatures(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_fluidpropertiestemperatures(self):

        pyidf.validation_level = ValidationLevel.error

        obj = FluidPropertiesTemperatures()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # real
        var_temperature_1 = 2.2
        obj.temperature_1 = var_temperature_1
        # real
        var_temperature_2 = 3.3
        obj.temperature_2 = var_temperature_2
        # real
        var_temperature_3 = 4.4
        obj.temperature_3 = var_temperature_3
        # real
        var_temperature_4 = 5.5
        obj.temperature_4 = var_temperature_4
        # real
        var_temperature_5 = 6.6
        obj.temperature_5 = var_temperature_5
        # real
        var_temperature_6 = 7.7
        obj.temperature_6 = var_temperature_6
        # real
        var_temperature_7 = 8.8
        obj.temperature_7 = var_temperature_7
        # real
        var_temperature_8 = 9.9
        obj.temperature_8 = var_temperature_8
        # real
        var_temperature_9 = 10.1
        obj.temperature_9 = var_temperature_9
        # real
        var_temperature_10 = 11.11
        obj.temperature_10 = var_temperature_10
        # real
        var_temperature_11 = 12.12
        obj.temperature_11 = var_temperature_11
        # real
        var_temperature_12 = 13.13
        obj.temperature_12 = var_temperature_12
        # real
        var_temperature_13 = 14.14
        obj.temperature_13 = var_temperature_13
        # real
        var_temperature_14 = 15.15
        obj.temperature_14 = var_temperature_14
        # real
        var_temperature_15 = 16.16
        obj.temperature_15 = var_temperature_15
        # real
        var_temperature_16 = 17.17
        obj.temperature_16 = var_temperature_16
        # real
        var_temperature_17 = 18.18
        obj.temperature_17 = var_temperature_17
        # real
        var_temperature_18 = 19.19
        obj.temperature_18 = var_temperature_18
        # real
        var_temperature_19 = 20.2
        obj.temperature_19 = var_temperature_19
        # real
        var_temperature_20 = 21.21
        obj.temperature_20 = var_temperature_20
        # real
        var_temperature_21 = 22.22
        obj.temperature_21 = var_temperature_21
        # real
        var_temperature_22 = 23.23
        obj.temperature_22 = var_temperature_22
        # real
        var_temperature_23 = 24.24
        obj.temperature_23 = var_temperature_23
        # real
        var_temperature_24 = 25.25
        obj.temperature_24 = var_temperature_24
        # real
        var_temperature_25 = 26.26
        obj.temperature_25 = var_temperature_25
        # real
        var_temperature_26 = 27.27
        obj.temperature_26 = var_temperature_26
        # real
        var_temperature_27 = 28.28
        obj.temperature_27 = var_temperature_27
        # real
        var_temperature_28 = 29.29
        obj.temperature_28 = var_temperature_28
        # real
        var_temperature_29 = 30.3
        obj.temperature_29 = var_temperature_29
        # real
        var_temperature_30 = 31.31
        obj.temperature_30 = var_temperature_30
        # real
        var_temperature_31 = 32.32
        obj.temperature_31 = var_temperature_31
        # real
        var_temperature_32 = 33.33
        obj.temperature_32 = var_temperature_32
        # real
        var_temperature_33 = 34.34
        obj.temperature_33 = var_temperature_33
        # real
        var_temperature_34 = 35.35
        obj.temperature_34 = var_temperature_34
        # real
        var_temperature_35 = 36.36
        obj.temperature_35 = var_temperature_35
        # real
        var_temperature_36 = 37.37
        obj.temperature_36 = var_temperature_36
        # real
        var_temperature_37 = 38.38
        obj.temperature_37 = var_temperature_37
        # real
        var_temperature_38 = 39.39
        obj.temperature_38 = var_temperature_38
        # real
        var_temperature_39 = 40.4
        obj.temperature_39 = var_temperature_39
        # real
        var_temperature_40 = 41.41
        obj.temperature_40 = var_temperature_40
        # real
        var_temperature_41 = 42.42
        obj.temperature_41 = var_temperature_41
        # real
        var_temperature_42 = 43.43
        obj.temperature_42 = var_temperature_42
        # real
        var_temperature_43 = 44.44
        obj.temperature_43 = var_temperature_43
        # real
        var_temperature_44 = 45.45
        obj.temperature_44 = var_temperature_44
        # real
        var_temperature_45 = 46.46
        obj.temperature_45 = var_temperature_45
        # real
        var_temperature_46 = 47.47
        obj.temperature_46 = var_temperature_46
        # real
        var_temperature_47 = 48.48
        obj.temperature_47 = var_temperature_47
        # real
        var_temperature_48 = 49.49
        obj.temperature_48 = var_temperature_48
        # real
        var_temperature_49 = 50.5
        obj.temperature_49 = var_temperature_49
        # real
        var_temperature_50 = 51.51
        obj.temperature_50 = var_temperature_50
        # real
        var_temperature_51 = 52.52
        obj.temperature_51 = var_temperature_51
        # real
        var_temperature_52 = 53.53
        obj.temperature_52 = var_temperature_52
        # real
        var_temperature_53 = 54.54
        obj.temperature_53 = var_temperature_53
        # real
        var_temperature_54 = 55.55
        obj.temperature_54 = var_temperature_54
        # real
        var_temperature_55 = 56.56
        obj.temperature_55 = var_temperature_55
        # real
        var_temperature_56 = 57.57
        obj.temperature_56 = var_temperature_56
        # real
        var_temperature_57 = 58.58
        obj.temperature_57 = var_temperature_57
        # real
        var_temperature_58 = 59.59
        obj.temperature_58 = var_temperature_58
        # real
        var_temperature_59 = 60.6
        obj.temperature_59 = var_temperature_59
        # real
        var_temperature_60 = 61.61
        obj.temperature_60 = var_temperature_60
        # real
        var_temperature_61 = 62.62
        obj.temperature_61 = var_temperature_61
        # real
        var_temperature_62 = 63.63
        obj.temperature_62 = var_temperature_62
        # real
        var_temperature_63 = 64.64
        obj.temperature_63 = var_temperature_63
        # real
        var_temperature_64 = 65.65
        obj.temperature_64 = var_temperature_64
        # real
        var_temperature_65 = 66.66
        obj.temperature_65 = var_temperature_65
        # real
        var_temperature_66 = 67.67
        obj.temperature_66 = var_temperature_66
        # real
        var_temperature_67 = 68.68
        obj.temperature_67 = var_temperature_67
        # real
        var_temperature_68 = 69.69
        obj.temperature_68 = var_temperature_68
        # real
        var_temperature_69 = 70.7
        obj.temperature_69 = var_temperature_69
        # real
        var_temperature_70 = 71.71
        obj.temperature_70 = var_temperature_70
        # real
        var_temperature_71 = 72.72
        obj.temperature_71 = var_temperature_71
        # real
        var_temperature_72 = 73.73
        obj.temperature_72 = var_temperature_72
        # real
        var_temperature_73 = 74.74
        obj.temperature_73 = var_temperature_73
        # real
        var_temperature_74 = 75.75
        obj.temperature_74 = var_temperature_74
        # real
        var_temperature_75 = 76.76
        obj.temperature_75 = var_temperature_75
        # real
        var_temperature_76 = 77.77
        obj.temperature_76 = var_temperature_76
        # real
        var_temperature_77 = 78.78
        obj.temperature_77 = var_temperature_77
        # real
        var_temperature_78 = 79.79
        obj.temperature_78 = var_temperature_78
        # real
        var_temperature_79 = 80.8
        obj.temperature_79 = var_temperature_79
        # real
        var_temperature_80 = 81.81
        obj.temperature_80 = var_temperature_80
        # real
        var_temperature_81 = 82.82
        obj.temperature_81 = var_temperature_81
        # real
        var_temperature_82 = 83.83
        obj.temperature_82 = var_temperature_82
        # real
        var_temperature_83 = 84.84
        obj.temperature_83 = var_temperature_83
        # real
        var_temperature_84 = 85.85
        obj.temperature_84 = var_temperature_84
        # real
        var_temperature_85 = 86.86
        obj.temperature_85 = var_temperature_85
        # real
        var_temperature_86 = 87.87
        obj.temperature_86 = var_temperature_86
        # real
        var_temperature_87 = 88.88
        obj.temperature_87 = var_temperature_87
        # real
        var_temperature_88 = 89.89
        obj.temperature_88 = var_temperature_88
        # real
        var_temperature_89 = 90.9
        obj.temperature_89 = var_temperature_89
        # real
        var_temperature_90 = 91.91
        obj.temperature_90 = var_temperature_90
        # real
        var_temperature_91 = 92.92
        obj.temperature_91 = var_temperature_91
        # real
        var_temperature_92 = 93.93
        obj.temperature_92 = var_temperature_92
        # real
        var_temperature_93 = 94.94
        obj.temperature_93 = var_temperature_93
        # real
        var_temperature_94 = 95.95
        obj.temperature_94 = var_temperature_94
        # real
        var_temperature_95 = 96.96
        obj.temperature_95 = var_temperature_95
        # real
        var_temperature_96 = 97.97
        obj.temperature_96 = var_temperature_96
        # real
        var_temperature_97 = 98.98
        obj.temperature_97 = var_temperature_97
        # real
        var_temperature_98 = 99.99
        obj.temperature_98 = var_temperature_98
        # real
        var_temperature_99 = 100.1
        obj.temperature_99 = var_temperature_99
        # real
        var_temperature_100 = 101.101
        obj.temperature_100 = var_temperature_100
        # real
        var_temperature_101 = 102.102
        obj.temperature_101 = var_temperature_101
        # real
        var_temperature_102 = 103.103
        obj.temperature_102 = var_temperature_102
        # real
        var_temperature_103 = 104.104
        obj.temperature_103 = var_temperature_103
        # real
        var_temperature_104 = 105.105
        obj.temperature_104 = var_temperature_104
        # real
        var_temperature_105 = 106.106
        obj.temperature_105 = var_temperature_105
        # real
        var_temperature_106 = 107.107
        obj.temperature_106 = var_temperature_106
        # real
        var_temperature_107 = 108.108
        obj.temperature_107 = var_temperature_107
        # real
        var_temperature_108 = 109.109
        obj.temperature_108 = var_temperature_108
        # real
        var_temperature_109 = 110.11
        obj.temperature_109 = var_temperature_109
        # real
        var_temperature_110 = 111.111
        obj.temperature_110 = var_temperature_110
        # real
        var_temperature_111 = 112.112
        obj.temperature_111 = var_temperature_111
        # real
        var_temperature_112 = 113.113
        obj.temperature_112 = var_temperature_112
        # real
        var_temperature_113 = 114.114
        obj.temperature_113 = var_temperature_113
        # real
        var_temperature_114 = 115.115
        obj.temperature_114 = var_temperature_114
        # real
        var_temperature_115 = 116.116
        obj.temperature_115 = var_temperature_115
        # real
        var_temperature_116 = 117.117
        obj.temperature_116 = var_temperature_116
        # real
        var_temperature_117 = 118.118
        obj.temperature_117 = var_temperature_117
        # real
        var_temperature_118 = 119.119
        obj.temperature_118 = var_temperature_118
        # real
        var_temperature_119 = 120.12
        obj.temperature_119 = var_temperature_119
        # real
        var_temperature_120 = 121.121
        obj.temperature_120 = var_temperature_120
        # real
        var_temperature_121 = 122.122
        obj.temperature_121 = var_temperature_121
        # real
        var_temperature_122 = 123.123
        obj.temperature_122 = var_temperature_122
        # real
        var_temperature_123 = 124.124
        obj.temperature_123 = var_temperature_123
        # real
        var_temperature_124 = 125.125
        obj.temperature_124 = var_temperature_124
        # real
        var_temperature_125 = 126.126
        obj.temperature_125 = var_temperature_125
        # real
        var_temperature_126 = 127.127
        obj.temperature_126 = var_temperature_126
        # real
        var_temperature_127 = 128.128
        obj.temperature_127 = var_temperature_127
        # real
        var_temperature_128 = 129.129
        obj.temperature_128 = var_temperature_128
        # real
        var_temperature_129 = 130.13
        obj.temperature_129 = var_temperature_129
        # real
        var_temperature_130 = 131.131
        obj.temperature_130 = var_temperature_130
        # real
        var_temperature_131 = 132.132
        obj.temperature_131 = var_temperature_131
        # real
        var_temperature_132 = 133.133
        obj.temperature_132 = var_temperature_132
        # real
        var_temperature_133 = 134.134
        obj.temperature_133 = var_temperature_133
        # real
        var_temperature_134 = 135.135
        obj.temperature_134 = var_temperature_134
        # real
        var_temperature_135 = 136.136
        obj.temperature_135 = var_temperature_135
        # real
        var_temperature_136 = 137.137
        obj.temperature_136 = var_temperature_136
        # real
        var_temperature_137 = 138.138
        obj.temperature_137 = var_temperature_137
        # real
        var_temperature_138 = 139.139
        obj.temperature_138 = var_temperature_138
        # real
        var_temperature_139 = 140.14
        obj.temperature_139 = var_temperature_139
        # real
        var_temperature_140 = 141.141
        obj.temperature_140 = var_temperature_140
        # real
        var_temperature_141 = 142.142
        obj.temperature_141 = var_temperature_141
        # real
        var_temperature_142 = 143.143
        obj.temperature_142 = var_temperature_142
        # real
        var_temperature_143 = 144.144
        obj.temperature_143 = var_temperature_143
        # real
        var_temperature_144 = 145.145
        obj.temperature_144 = var_temperature_144
        # real
        var_temperature_145 = 146.146
        obj.temperature_145 = var_temperature_145
        # real
        var_temperature_146 = 147.147
        obj.temperature_146 = var_temperature_146
        # real
        var_temperature_147 = 148.148
        obj.temperature_147 = var_temperature_147
        # real
        var_temperature_148 = 149.149
        obj.temperature_148 = var_temperature_148
        # real
        var_temperature_149 = 150.15
        obj.temperature_149 = var_temperature_149
        # real
        var_temperature_150 = 151.151
        obj.temperature_150 = var_temperature_150
        # real
        var_temperature_151 = 152.152
        obj.temperature_151 = var_temperature_151
        # real
        var_temperature_152 = 153.153
        obj.temperature_152 = var_temperature_152
        # real
        var_temperature_153 = 154.154
        obj.temperature_153 = var_temperature_153
        # real
        var_temperature_154 = 155.155
        obj.temperature_154 = var_temperature_154
        # real
        var_temperature_155 = 156.156
        obj.temperature_155 = var_temperature_155
        # real
        var_temperature_156 = 157.157
        obj.temperature_156 = var_temperature_156
        # real
        var_temperature_157 = 158.158
        obj.temperature_157 = var_temperature_157
        # real
        var_temperature_158 = 159.159
        obj.temperature_158 = var_temperature_158
        # real
        var_temperature_159 = 160.16
        obj.temperature_159 = var_temperature_159
        # real
        var_temperature_160 = 161.161
        obj.temperature_160 = var_temperature_160
        # real
        var_temperature_161 = 162.162
        obj.temperature_161 = var_temperature_161
        # real
        var_temperature_162 = 163.163
        obj.temperature_162 = var_temperature_162
        # real
        var_temperature_163 = 164.164
        obj.temperature_163 = var_temperature_163
        # real
        var_temperature_164 = 165.165
        obj.temperature_164 = var_temperature_164
        # real
        var_temperature_165 = 166.166
        obj.temperature_165 = var_temperature_165
        # real
        var_temperature_166 = 167.167
        obj.temperature_166 = var_temperature_166
        # real
        var_temperature_167 = 168.168
        obj.temperature_167 = var_temperature_167
        # real
        var_temperature_168 = 169.169
        obj.temperature_168 = var_temperature_168
        # real
        var_temperature_169 = 170.17
        obj.temperature_169 = var_temperature_169
        # real
        var_temperature_170 = 171.171
        obj.temperature_170 = var_temperature_170
        # real
        var_temperature_171 = 172.172
        obj.temperature_171 = var_temperature_171
        # real
        var_temperature_172 = 173.173
        obj.temperature_172 = var_temperature_172
        # real
        var_temperature_173 = 174.174
        obj.temperature_173 = var_temperature_173
        # real
        var_temperature_174 = 175.175
        obj.temperature_174 = var_temperature_174
        # real
        var_temperature_175 = 176.176
        obj.temperature_175 = var_temperature_175
        # real
        var_temperature_176 = 177.177
        obj.temperature_176 = var_temperature_176
        # real
        var_temperature_177 = 178.178
        obj.temperature_177 = var_temperature_177
        # real
        var_temperature_178 = 179.179
        obj.temperature_178 = var_temperature_178
        # real
        var_temperature_179 = 180.18
        obj.temperature_179 = var_temperature_179
        # real
        var_temperature_180 = 181.181
        obj.temperature_180 = var_temperature_180
        # real
        var_temperature_181 = 182.182
        obj.temperature_181 = var_temperature_181
        # real
        var_temperature_182 = 183.183
        obj.temperature_182 = var_temperature_182
        # real
        var_temperature_183 = 184.184
        obj.temperature_183 = var_temperature_183
        # real
        var_temperature_184 = 185.185
        obj.temperature_184 = var_temperature_184
        # real
        var_temperature_185 = 186.186
        obj.temperature_185 = var_temperature_185
        # real
        var_temperature_186 = 187.187
        obj.temperature_186 = var_temperature_186
        # real
        var_temperature_187 = 188.188
        obj.temperature_187 = var_temperature_187
        # real
        var_temperature_188 = 189.189
        obj.temperature_188 = var_temperature_188
        # real
        var_temperature_189 = 190.19
        obj.temperature_189 = var_temperature_189
        # real
        var_temperature_190 = 191.191
        obj.temperature_190 = var_temperature_190
        # real
        var_temperature_191 = 192.192
        obj.temperature_191 = var_temperature_191
        # real
        var_temperature_192 = 193.193
        obj.temperature_192 = var_temperature_192
        # real
        var_temperature_193 = 194.194
        obj.temperature_193 = var_temperature_193
        # real
        var_temperature_194 = 195.195
        obj.temperature_194 = var_temperature_194
        # real
        var_temperature_195 = 196.196
        obj.temperature_195 = var_temperature_195
        # real
        var_temperature_196 = 197.197
        obj.temperature_196 = var_temperature_196
        # real
        var_temperature_197 = 198.198
        obj.temperature_197 = var_temperature_197
        # real
        var_temperature_198 = 199.199
        obj.temperature_198 = var_temperature_198
        # real
        var_temperature_199 = 200.2
        obj.temperature_199 = var_temperature_199
        # real
        var_temperature_200 = 201.201
        obj.temperature_200 = var_temperature_200
        # real
        var_temperature_201 = 202.202
        obj.temperature_201 = var_temperature_201
        # real
        var_temperature_202 = 203.203
        obj.temperature_202 = var_temperature_202
        # real
        var_temperature_203 = 204.204
        obj.temperature_203 = var_temperature_203
        # real
        var_temperature_204 = 205.205
        obj.temperature_204 = var_temperature_204
        # real
        var_temperature_205 = 206.206
        obj.temperature_205 = var_temperature_205
        # real
        var_temperature_206 = 207.207
        obj.temperature_206 = var_temperature_206
        # real
        var_temperature_207 = 208.208
        obj.temperature_207 = var_temperature_207
        # real
        var_temperature_208 = 209.209
        obj.temperature_208 = var_temperature_208
        # real
        var_temperature_209 = 210.21
        obj.temperature_209 = var_temperature_209
        # real
        var_temperature_210 = 211.211
        obj.temperature_210 = var_temperature_210
        # real
        var_temperature_211 = 212.212
        obj.temperature_211 = var_temperature_211
        # real
        var_temperature_212 = 213.213
        obj.temperature_212 = var_temperature_212
        # real
        var_temperature_213 = 214.214
        obj.temperature_213 = var_temperature_213
        # real
        var_temperature_214 = 215.215
        obj.temperature_214 = var_temperature_214
        # real
        var_temperature_215 = 216.216
        obj.temperature_215 = var_temperature_215
        # real
        var_temperature_216 = 217.217
        obj.temperature_216 = var_temperature_216
        # real
        var_temperature_217 = 218.218
        obj.temperature_217 = var_temperature_217
        # real
        var_temperature_218 = 219.219
        obj.temperature_218 = var_temperature_218
        # real
        var_temperature_219 = 220.22
        obj.temperature_219 = var_temperature_219
        # real
        var_temperature_220 = 221.221
        obj.temperature_220 = var_temperature_220
        # real
        var_temperature_221 = 222.222
        obj.temperature_221 = var_temperature_221
        # real
        var_temperature_222 = 223.223
        obj.temperature_222 = var_temperature_222
        # real
        var_temperature_223 = 224.224
        obj.temperature_223 = var_temperature_223
        # real
        var_temperature_224 = 225.225
        obj.temperature_224 = var_temperature_224
        # real
        var_temperature_225 = 226.226
        obj.temperature_225 = var_temperature_225
        # real
        var_temperature_226 = 227.227
        obj.temperature_226 = var_temperature_226
        # real
        var_temperature_227 = 228.228
        obj.temperature_227 = var_temperature_227
        # real
        var_temperature_228 = 229.229
        obj.temperature_228 = var_temperature_228
        # real
        var_temperature_229 = 230.23
        obj.temperature_229 = var_temperature_229
        # real
        var_temperature_230 = 231.231
        obj.temperature_230 = var_temperature_230
        # real
        var_temperature_231 = 232.232
        obj.temperature_231 = var_temperature_231
        # real
        var_temperature_232 = 233.233
        obj.temperature_232 = var_temperature_232
        # real
        var_temperature_233 = 234.234
        obj.temperature_233 = var_temperature_233
        # real
        var_temperature_234 = 235.235
        obj.temperature_234 = var_temperature_234
        # real
        var_temperature_235 = 236.236
        obj.temperature_235 = var_temperature_235
        # real
        var_temperature_236 = 237.237
        obj.temperature_236 = var_temperature_236
        # real
        var_temperature_237 = 238.238
        obj.temperature_237 = var_temperature_237
        # real
        var_temperature_238 = 239.239
        obj.temperature_238 = var_temperature_238
        # real
        var_temperature_239 = 240.24
        obj.temperature_239 = var_temperature_239
        # real
        var_temperature_240 = 241.241
        obj.temperature_240 = var_temperature_240
        # real
        var_temperature_241 = 242.242
        obj.temperature_241 = var_temperature_241
        # real
        var_temperature_242 = 243.243
        obj.temperature_242 = var_temperature_242
        # real
        var_temperature_243 = 244.244
        obj.temperature_243 = var_temperature_243
        # real
        var_temperature_244 = 245.245
        obj.temperature_244 = var_temperature_244
        # real
        var_temperature_245 = 246.246
        obj.temperature_245 = var_temperature_245
        # real
        var_temperature_246 = 247.247
        obj.temperature_246 = var_temperature_246
        # real
        var_temperature_247 = 248.248
        obj.temperature_247 = var_temperature_247
        # real
        var_temperature_248 = 249.249
        obj.temperature_248 = var_temperature_248
        # real
        var_temperature_249 = 250.25
        obj.temperature_249 = var_temperature_249
        # real
        var_temperature_250 = 251.251
        obj.temperature_250 = var_temperature_250

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                print line.strip()

        idf2 = IDF(self.path)
        self.assertEqual(idf2.fluidpropertiestemperaturess[0].name, var_name)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_1, var_temperature_1)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_2, var_temperature_2)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_3, var_temperature_3)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_4, var_temperature_4)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_5, var_temperature_5)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_6, var_temperature_6)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_7, var_temperature_7)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_8, var_temperature_8)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_9, var_temperature_9)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_10, var_temperature_10)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_11, var_temperature_11)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_12, var_temperature_12)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_13, var_temperature_13)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_14, var_temperature_14)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_15, var_temperature_15)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_16, var_temperature_16)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_17, var_temperature_17)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_18, var_temperature_18)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_19, var_temperature_19)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_20, var_temperature_20)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_21, var_temperature_21)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_22, var_temperature_22)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_23, var_temperature_23)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_24, var_temperature_24)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_25, var_temperature_25)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_26, var_temperature_26)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_27, var_temperature_27)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_28, var_temperature_28)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_29, var_temperature_29)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_30, var_temperature_30)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_31, var_temperature_31)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_32, var_temperature_32)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_33, var_temperature_33)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_34, var_temperature_34)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_35, var_temperature_35)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_36, var_temperature_36)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_37, var_temperature_37)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_38, var_temperature_38)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_39, var_temperature_39)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_40, var_temperature_40)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_41, var_temperature_41)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_42, var_temperature_42)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_43, var_temperature_43)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_44, var_temperature_44)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_45, var_temperature_45)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_46, var_temperature_46)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_47, var_temperature_47)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_48, var_temperature_48)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_49, var_temperature_49)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_50, var_temperature_50)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_51, var_temperature_51)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_52, var_temperature_52)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_53, var_temperature_53)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_54, var_temperature_54)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_55, var_temperature_55)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_56, var_temperature_56)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_57, var_temperature_57)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_58, var_temperature_58)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_59, var_temperature_59)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_60, var_temperature_60)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_61, var_temperature_61)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_62, var_temperature_62)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_63, var_temperature_63)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_64, var_temperature_64)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_65, var_temperature_65)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_66, var_temperature_66)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_67, var_temperature_67)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_68, var_temperature_68)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_69, var_temperature_69)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_70, var_temperature_70)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_71, var_temperature_71)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_72, var_temperature_72)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_73, var_temperature_73)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_74, var_temperature_74)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_75, var_temperature_75)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_76, var_temperature_76)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_77, var_temperature_77)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_78, var_temperature_78)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_79, var_temperature_79)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_80, var_temperature_80)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_81, var_temperature_81)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_82, var_temperature_82)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_83, var_temperature_83)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_84, var_temperature_84)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_85, var_temperature_85)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_86, var_temperature_86)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_87, var_temperature_87)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_88, var_temperature_88)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_89, var_temperature_89)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_90, var_temperature_90)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_91, var_temperature_91)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_92, var_temperature_92)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_93, var_temperature_93)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_94, var_temperature_94)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_95, var_temperature_95)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_96, var_temperature_96)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_97, var_temperature_97)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_98, var_temperature_98)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_99, var_temperature_99)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_100, var_temperature_100)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_101, var_temperature_101)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_102, var_temperature_102)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_103, var_temperature_103)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_104, var_temperature_104)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_105, var_temperature_105)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_106, var_temperature_106)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_107, var_temperature_107)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_108, var_temperature_108)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_109, var_temperature_109)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_110, var_temperature_110)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_111, var_temperature_111)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_112, var_temperature_112)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_113, var_temperature_113)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_114, var_temperature_114)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_115, var_temperature_115)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_116, var_temperature_116)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_117, var_temperature_117)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_118, var_temperature_118)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_119, var_temperature_119)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_120, var_temperature_120)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_121, var_temperature_121)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_122, var_temperature_122)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_123, var_temperature_123)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_124, var_temperature_124)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_125, var_temperature_125)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_126, var_temperature_126)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_127, var_temperature_127)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_128, var_temperature_128)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_129, var_temperature_129)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_130, var_temperature_130)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_131, var_temperature_131)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_132, var_temperature_132)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_133, var_temperature_133)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_134, var_temperature_134)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_135, var_temperature_135)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_136, var_temperature_136)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_137, var_temperature_137)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_138, var_temperature_138)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_139, var_temperature_139)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_140, var_temperature_140)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_141, var_temperature_141)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_142, var_temperature_142)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_143, var_temperature_143)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_144, var_temperature_144)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_145, var_temperature_145)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_146, var_temperature_146)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_147, var_temperature_147)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_148, var_temperature_148)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_149, var_temperature_149)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_150, var_temperature_150)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_151, var_temperature_151)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_152, var_temperature_152)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_153, var_temperature_153)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_154, var_temperature_154)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_155, var_temperature_155)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_156, var_temperature_156)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_157, var_temperature_157)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_158, var_temperature_158)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_159, var_temperature_159)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_160, var_temperature_160)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_161, var_temperature_161)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_162, var_temperature_162)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_163, var_temperature_163)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_164, var_temperature_164)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_165, var_temperature_165)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_166, var_temperature_166)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_167, var_temperature_167)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_168, var_temperature_168)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_169, var_temperature_169)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_170, var_temperature_170)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_171, var_temperature_171)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_172, var_temperature_172)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_173, var_temperature_173)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_174, var_temperature_174)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_175, var_temperature_175)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_176, var_temperature_176)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_177, var_temperature_177)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_178, var_temperature_178)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_179, var_temperature_179)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_180, var_temperature_180)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_181, var_temperature_181)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_182, var_temperature_182)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_183, var_temperature_183)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_184, var_temperature_184)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_185, var_temperature_185)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_186, var_temperature_186)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_187, var_temperature_187)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_188, var_temperature_188)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_189, var_temperature_189)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_190, var_temperature_190)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_191, var_temperature_191)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_192, var_temperature_192)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_193, var_temperature_193)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_194, var_temperature_194)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_195, var_temperature_195)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_196, var_temperature_196)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_197, var_temperature_197)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_198, var_temperature_198)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_199, var_temperature_199)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_200, var_temperature_200)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_201, var_temperature_201)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_202, var_temperature_202)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_203, var_temperature_203)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_204, var_temperature_204)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_205, var_temperature_205)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_206, var_temperature_206)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_207, var_temperature_207)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_208, var_temperature_208)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_209, var_temperature_209)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_210, var_temperature_210)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_211, var_temperature_211)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_212, var_temperature_212)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_213, var_temperature_213)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_214, var_temperature_214)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_215, var_temperature_215)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_216, var_temperature_216)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_217, var_temperature_217)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_218, var_temperature_218)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_219, var_temperature_219)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_220, var_temperature_220)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_221, var_temperature_221)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_222, var_temperature_222)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_223, var_temperature_223)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_224, var_temperature_224)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_225, var_temperature_225)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_226, var_temperature_226)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_227, var_temperature_227)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_228, var_temperature_228)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_229, var_temperature_229)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_230, var_temperature_230)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_231, var_temperature_231)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_232, var_temperature_232)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_233, var_temperature_233)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_234, var_temperature_234)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_235, var_temperature_235)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_236, var_temperature_236)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_237, var_temperature_237)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_238, var_temperature_238)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_239, var_temperature_239)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_240, var_temperature_240)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_241, var_temperature_241)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_242, var_temperature_242)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_243, var_temperature_243)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_244, var_temperature_244)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_245, var_temperature_245)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_246, var_temperature_246)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_247, var_temperature_247)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_248, var_temperature_248)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_249, var_temperature_249)
        self.assertAlmostEqual(idf2.fluidpropertiestemperaturess[0].temperature_250, var_temperature_250)