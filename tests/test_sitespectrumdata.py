import os
import tempfile
import unittest
import logging
from pyidf import ValidationLevel
import pyidf
from pyidf.idf import IDF
from pyidf.location_and_climate import SiteSpectrumData

log = logging.getLogger(__name__)

class TestSiteSpectrumData(unittest.TestCase):

    def setUp(self):
        self.fd, self.path = tempfile.mkstemp()

    def tearDown(self):
        os.remove(self.path)

    def test_create_sitespectrumdata(self):

        pyidf.validation_level = ValidationLevel.error

        obj = SiteSpectrumData()
        # alpha
        var_name = "Name"
        obj.name = var_name
        # alpha
        var_spectrum_data_type = "Solar"
        obj.spectrum_data_type = var_spectrum_data_type
        # real
        var_wavelength_1 = 3.3
        obj.wavelength_1 = var_wavelength_1
        # real
        var_spectrum_1 = 4.4
        obj.spectrum_1 = var_spectrum_1
        # real
        var_wavelength_2 = 5.5
        obj.wavelength_2 = var_wavelength_2
        # real
        var_spectrum_2 = 6.6
        obj.spectrum_2 = var_spectrum_2
        # real
        var_wavelength_3 = 7.7
        obj.wavelength_3 = var_wavelength_3
        # real
        var_spectrum_3 = 8.8
        obj.spectrum_3 = var_spectrum_3
        # real
        var_wavelength_4 = 9.9
        obj.wavelength_4 = var_wavelength_4
        # real
        var_spectrum_4 = 10.1
        obj.spectrum_4 = var_spectrum_4
        # real
        var_wavelength_5 = 11.11
        obj.wavelength_5 = var_wavelength_5
        # real
        var_spectrum_5 = 12.12
        obj.spectrum_5 = var_spectrum_5
        # real
        var_wavelength_6 = 13.13
        obj.wavelength_6 = var_wavelength_6
        # real
        var_spectrum_6 = 14.14
        obj.spectrum_6 = var_spectrum_6
        # real
        var_wavelength_7 = 15.15
        obj.wavelength_7 = var_wavelength_7
        # real
        var_spectrum_7 = 16.16
        obj.spectrum_7 = var_spectrum_7
        # real
        var_wavelength_8 = 17.17
        obj.wavelength_8 = var_wavelength_8
        # real
        var_spectrum_8 = 18.18
        obj.spectrum_8 = var_spectrum_8
        # real
        var_wavelength_9 = 19.19
        obj.wavelength_9 = var_wavelength_9
        # real
        var_spectrum_9 = 20.2
        obj.spectrum_9 = var_spectrum_9
        # real
        var_wavelength_10 = 21.21
        obj.wavelength_10 = var_wavelength_10
        # real
        var_spectrum_10 = 22.22
        obj.spectrum_10 = var_spectrum_10
        # real
        var_wavelength_11 = 23.23
        obj.wavelength_11 = var_wavelength_11
        # real
        var_spectrum_11 = 24.24
        obj.spectrum_11 = var_spectrum_11
        # real
        var_wavelength_12 = 25.25
        obj.wavelength_12 = var_wavelength_12
        # real
        var_spectrum_12 = 26.26
        obj.spectrum_12 = var_spectrum_12
        # real
        var_wavelength_13 = 27.27
        obj.wavelength_13 = var_wavelength_13
        # real
        var_spectrum_13 = 28.28
        obj.spectrum_13 = var_spectrum_13
        # real
        var_wavelength_14 = 29.29
        obj.wavelength_14 = var_wavelength_14
        # real
        var_spectrum_14 = 30.3
        obj.spectrum_14 = var_spectrum_14
        # real
        var_wavelength_15 = 31.31
        obj.wavelength_15 = var_wavelength_15
        # real
        var_spectrum_15 = 32.32
        obj.spectrum_15 = var_spectrum_15
        # real
        var_wavelength_16 = 33.33
        obj.wavelength_16 = var_wavelength_16
        # real
        var_spectrum_16 = 34.34
        obj.spectrum_16 = var_spectrum_16
        # real
        var_wavelength_17 = 35.35
        obj.wavelength_17 = var_wavelength_17
        # real
        var_spectrum_17 = 36.36
        obj.spectrum_17 = var_spectrum_17
        # real
        var_wavelength_18 = 37.37
        obj.wavelength_18 = var_wavelength_18
        # real
        var_spectrum_18 = 38.38
        obj.spectrum_18 = var_spectrum_18
        # real
        var_wavelength_19 = 39.39
        obj.wavelength_19 = var_wavelength_19
        # real
        var_spectrum_19 = 40.4
        obj.spectrum_19 = var_spectrum_19
        # real
        var_wavelength_20 = 41.41
        obj.wavelength_20 = var_wavelength_20
        # real
        var_spectrum_20 = 42.42
        obj.spectrum_20 = var_spectrum_20
        # real
        var_wavelength_21 = 43.43
        obj.wavelength_21 = var_wavelength_21
        # real
        var_spectrum_21 = 44.44
        obj.spectrum_21 = var_spectrum_21
        # real
        var_wavelength_22 = 45.45
        obj.wavelength_22 = var_wavelength_22
        # real
        var_spectrum_22 = 46.46
        obj.spectrum_22 = var_spectrum_22
        # real
        var_wavelength_23 = 47.47
        obj.wavelength_23 = var_wavelength_23
        # real
        var_spectrum_23 = 48.48
        obj.spectrum_23 = var_spectrum_23
        # real
        var_wavelength_24 = 49.49
        obj.wavelength_24 = var_wavelength_24
        # real
        var_spectrum_24 = 50.5
        obj.spectrum_24 = var_spectrum_24
        # real
        var_wavelength_25 = 51.51
        obj.wavelength_25 = var_wavelength_25
        # real
        var_spectrum_25 = 52.52
        obj.spectrum_25 = var_spectrum_25
        # real
        var_wavelength_26 = 53.53
        obj.wavelength_26 = var_wavelength_26
        # real
        var_spectrum_26 = 54.54
        obj.spectrum_26 = var_spectrum_26
        # real
        var_wavelength_27 = 55.55
        obj.wavelength_27 = var_wavelength_27
        # real
        var_spectrum_27 = 56.56
        obj.spectrum_27 = var_spectrum_27
        # real
        var_wavelength_28 = 57.57
        obj.wavelength_28 = var_wavelength_28
        # real
        var_spectrum_28 = 58.58
        obj.spectrum_28 = var_spectrum_28
        # real
        var_wavelength_29 = 59.59
        obj.wavelength_29 = var_wavelength_29
        # real
        var_spectrum_29 = 60.6
        obj.spectrum_29 = var_spectrum_29
        # real
        var_wavelength_30 = 61.61
        obj.wavelength_30 = var_wavelength_30
        # real
        var_spectrum_30 = 62.62
        obj.spectrum_30 = var_spectrum_30
        # real
        var_wavelength_31 = 63.63
        obj.wavelength_31 = var_wavelength_31
        # real
        var_spectrum_31 = 64.64
        obj.spectrum_31 = var_spectrum_31
        # real
        var_wavelength_32 = 65.65
        obj.wavelength_32 = var_wavelength_32
        # real
        var_spectrum_32 = 66.66
        obj.spectrum_32 = var_spectrum_32
        # real
        var_wavelength_33 = 67.67
        obj.wavelength_33 = var_wavelength_33
        # real
        var_spectrum_33 = 68.68
        obj.spectrum_33 = var_spectrum_33
        # real
        var_wavelength_34 = 69.69
        obj.wavelength_34 = var_wavelength_34
        # real
        var_spectrum_34 = 70.7
        obj.spectrum_34 = var_spectrum_34
        # real
        var_wavelength_35 = 71.71
        obj.wavelength_35 = var_wavelength_35
        # real
        var_spectrum_35 = 72.72
        obj.spectrum_35 = var_spectrum_35
        # real
        var_wavelength_36 = 73.73
        obj.wavelength_36 = var_wavelength_36
        # real
        var_spectrum_36 = 74.74
        obj.spectrum_36 = var_spectrum_36
        # real
        var_wavelength_37 = 75.75
        obj.wavelength_37 = var_wavelength_37
        # real
        var_spectrum_37 = 76.76
        obj.spectrum_37 = var_spectrum_37
        # real
        var_wavelength_38 = 77.77
        obj.wavelength_38 = var_wavelength_38
        # real
        var_spectrum_38 = 78.78
        obj.spectrum_38 = var_spectrum_38
        # real
        var_wavelength_39 = 79.79
        obj.wavelength_39 = var_wavelength_39
        # real
        var_spectrum_39 = 80.8
        obj.spectrum_39 = var_spectrum_39
        # real
        var_wavelength_40 = 81.81
        obj.wavelength_40 = var_wavelength_40
        # real
        var_spectrum_40 = 82.82
        obj.spectrum_40 = var_spectrum_40
        # real
        var_wavelength_41 = 83.83
        obj.wavelength_41 = var_wavelength_41
        # real
        var_spectrum_41 = 84.84
        obj.spectrum_41 = var_spectrum_41
        # real
        var_wavelength_42 = 85.85
        obj.wavelength_42 = var_wavelength_42
        # real
        var_spectrum_42 = 86.86
        obj.spectrum_42 = var_spectrum_42
        # real
        var_wavelength_43 = 87.87
        obj.wavelength_43 = var_wavelength_43
        # real
        var_spectrum_43 = 88.88
        obj.spectrum_43 = var_spectrum_43
        # real
        var_wavelength_44 = 89.89
        obj.wavelength_44 = var_wavelength_44
        # real
        var_spectrum_44 = 90.9
        obj.spectrum_44 = var_spectrum_44
        # real
        var_wavelength_45 = 91.91
        obj.wavelength_45 = var_wavelength_45
        # real
        var_spectrum_45 = 92.92
        obj.spectrum_45 = var_spectrum_45
        # real
        var_wavelength_46 = 93.93
        obj.wavelength_46 = var_wavelength_46
        # real
        var_spectrum_46 = 94.94
        obj.spectrum_46 = var_spectrum_46
        # real
        var_wavelength_47 = 95.95
        obj.wavelength_47 = var_wavelength_47
        # real
        var_spectrum_47 = 96.96
        obj.spectrum_47 = var_spectrum_47
        # real
        var_wavelength_48 = 97.97
        obj.wavelength_48 = var_wavelength_48
        # real
        var_spectrum_48 = 98.98
        obj.spectrum_48 = var_spectrum_48
        # real
        var_wavelength_49 = 99.99
        obj.wavelength_49 = var_wavelength_49
        # real
        var_spectrum_49 = 100.1
        obj.spectrum_49 = var_spectrum_49
        # real
        var_wavelength_50 = 101.101
        obj.wavelength_50 = var_wavelength_50
        # real
        var_spectrum_50 = 102.102
        obj.spectrum_50 = var_spectrum_50
        # real
        var_wavelength_51 = 103.103
        obj.wavelength_51 = var_wavelength_51
        # real
        var_spectrum_51 = 104.104
        obj.spectrum_51 = var_spectrum_51
        # real
        var_wavelength_52 = 105.105
        obj.wavelength_52 = var_wavelength_52
        # real
        var_spectrum_52 = 106.106
        obj.spectrum_52 = var_spectrum_52
        # real
        var_wavelength_53 = 107.107
        obj.wavelength_53 = var_wavelength_53
        # real
        var_spectrum_53 = 108.108
        obj.spectrum_53 = var_spectrum_53
        # real
        var_wavelength_54 = 109.109
        obj.wavelength_54 = var_wavelength_54
        # real
        var_spectrum_54 = 110.11
        obj.spectrum_54 = var_spectrum_54
        # real
        var_wavelength_55 = 111.111
        obj.wavelength_55 = var_wavelength_55
        # real
        var_spectrum_55 = 112.112
        obj.spectrum_55 = var_spectrum_55
        # real
        var_wavelength_56 = 113.113
        obj.wavelength_56 = var_wavelength_56
        # real
        var_spectrum_56 = 114.114
        obj.spectrum_56 = var_spectrum_56
        # real
        var_wavelength_57 = 115.115
        obj.wavelength_57 = var_wavelength_57
        # real
        var_spectrum_57 = 116.116
        obj.spectrum_57 = var_spectrum_57
        # real
        var_wavelength_58 = 117.117
        obj.wavelength_58 = var_wavelength_58
        # real
        var_spectrum_58 = 118.118
        obj.spectrum_58 = var_spectrum_58
        # real
        var_wavelength_59 = 119.119
        obj.wavelength_59 = var_wavelength_59
        # real
        var_spectrum_59 = 120.12
        obj.spectrum_59 = var_spectrum_59
        # real
        var_wavelength_60 = 121.121
        obj.wavelength_60 = var_wavelength_60
        # real
        var_spectrum_60 = 122.122
        obj.spectrum_60 = var_spectrum_60
        # real
        var_wavelength_61 = 123.123
        obj.wavelength_61 = var_wavelength_61
        # real
        var_spectrum_61 = 124.124
        obj.spectrum_61 = var_spectrum_61
        # real
        var_wavelength_62 = 125.125
        obj.wavelength_62 = var_wavelength_62
        # real
        var_spectrum_62 = 126.126
        obj.spectrum_62 = var_spectrum_62
        # real
        var_wavelength_63 = 127.127
        obj.wavelength_63 = var_wavelength_63
        # real
        var_spectrum_63 = 128.128
        obj.spectrum_63 = var_spectrum_63
        # real
        var_wavelength_64 = 129.129
        obj.wavelength_64 = var_wavelength_64
        # real
        var_spectrum_64 = 130.13
        obj.spectrum_64 = var_spectrum_64
        # real
        var_wavelength_65 = 131.131
        obj.wavelength_65 = var_wavelength_65
        # real
        var_spectrum_65 = 132.132
        obj.spectrum_65 = var_spectrum_65
        # real
        var_wavelength_66 = 133.133
        obj.wavelength_66 = var_wavelength_66
        # real
        var_spectrum_66 = 134.134
        obj.spectrum_66 = var_spectrum_66
        # real
        var_wavelength_67 = 135.135
        obj.wavelength_67 = var_wavelength_67
        # real
        var_spectrum_67 = 136.136
        obj.spectrum_67 = var_spectrum_67
        # real
        var_wavelength_68 = 137.137
        obj.wavelength_68 = var_wavelength_68
        # real
        var_spectrum_68 = 138.138
        obj.spectrum_68 = var_spectrum_68
        # real
        var_wavelength_69 = 139.139
        obj.wavelength_69 = var_wavelength_69
        # real
        var_spectrum_69 = 140.14
        obj.spectrum_69 = var_spectrum_69
        # real
        var_wavelength_70 = 141.141
        obj.wavelength_70 = var_wavelength_70
        # real
        var_spectrum_70 = 142.142
        obj.spectrum_70 = var_spectrum_70
        # real
        var_wavelength_71 = 143.143
        obj.wavelength_71 = var_wavelength_71
        # real
        var_spectrum_71 = 144.144
        obj.spectrum_71 = var_spectrum_71
        # real
        var_wavelength_72 = 145.145
        obj.wavelength_72 = var_wavelength_72
        # real
        var_spectrum_72 = 146.146
        obj.spectrum_72 = var_spectrum_72
        # real
        var_wavelength_73 = 147.147
        obj.wavelength_73 = var_wavelength_73
        # real
        var_spectrum_73 = 148.148
        obj.spectrum_73 = var_spectrum_73
        # real
        var_wavelength_74 = 149.149
        obj.wavelength_74 = var_wavelength_74
        # real
        var_spectrum_74 = 150.15
        obj.spectrum_74 = var_spectrum_74
        # real
        var_wavelength_75 = 151.151
        obj.wavelength_75 = var_wavelength_75
        # real
        var_spectrum_75 = 152.152
        obj.spectrum_75 = var_spectrum_75
        # real
        var_wavelength_76 = 153.153
        obj.wavelength_76 = var_wavelength_76
        # real
        var_spectrum_76 = 154.154
        obj.spectrum_76 = var_spectrum_76
        # real
        var_wavelength_77 = 155.155
        obj.wavelength_77 = var_wavelength_77
        # real
        var_spectrum_77 = 156.156
        obj.spectrum_77 = var_spectrum_77
        # real
        var_wavelength_78 = 157.157
        obj.wavelength_78 = var_wavelength_78
        # real
        var_spectrum_78 = 158.158
        obj.spectrum_78 = var_spectrum_78
        # real
        var_wavelength_79 = 159.159
        obj.wavelength_79 = var_wavelength_79
        # real
        var_spectrum_79 = 160.16
        obj.spectrum_79 = var_spectrum_79
        # real
        var_wavelength_80 = 161.161
        obj.wavelength_80 = var_wavelength_80
        # real
        var_spectrum_80 = 162.162
        obj.spectrum_80 = var_spectrum_80
        # real
        var_wavelength_81 = 163.163
        obj.wavelength_81 = var_wavelength_81
        # real
        var_spectrum_81 = 164.164
        obj.spectrum_81 = var_spectrum_81
        # real
        var_wavelength_82 = 165.165
        obj.wavelength_82 = var_wavelength_82
        # real
        var_spectrum_82 = 166.166
        obj.spectrum_82 = var_spectrum_82
        # real
        var_wavelength_83 = 167.167
        obj.wavelength_83 = var_wavelength_83
        # real
        var_spectrum_83 = 168.168
        obj.spectrum_83 = var_spectrum_83
        # real
        var_wavelength_84 = 169.169
        obj.wavelength_84 = var_wavelength_84
        # real
        var_spectrum_84 = 170.17
        obj.spectrum_84 = var_spectrum_84
        # real
        var_wavelength_85 = 171.171
        obj.wavelength_85 = var_wavelength_85
        # real
        var_spectrum_85 = 172.172
        obj.spectrum_85 = var_spectrum_85
        # real
        var_wavelength_86 = 173.173
        obj.wavelength_86 = var_wavelength_86
        # real
        var_spectrum_86 = 174.174
        obj.spectrum_86 = var_spectrum_86
        # real
        var_wavelength_87 = 175.175
        obj.wavelength_87 = var_wavelength_87
        # real
        var_spectrum_87 = 176.176
        obj.spectrum_87 = var_spectrum_87
        # real
        var_wavelength_88 = 177.177
        obj.wavelength_88 = var_wavelength_88
        # real
        var_spectrum_88 = 178.178
        obj.spectrum_88 = var_spectrum_88
        # real
        var_wavelength_89 = 179.179
        obj.wavelength_89 = var_wavelength_89
        # real
        var_spectrum_89 = 180.18
        obj.spectrum_89 = var_spectrum_89
        # real
        var_wavelength_90 = 181.181
        obj.wavelength_90 = var_wavelength_90
        # real
        var_spectrum_90 = 182.182
        obj.spectrum_90 = var_spectrum_90
        # real
        var_wavelength_91 = 183.183
        obj.wavelength_91 = var_wavelength_91
        # real
        var_spectrum_91 = 184.184
        obj.spectrum_91 = var_spectrum_91
        # real
        var_wavelength_92 = 185.185
        obj.wavelength_92 = var_wavelength_92
        # real
        var_spectrum_92 = 186.186
        obj.spectrum_92 = var_spectrum_92
        # real
        var_wavelength_93 = 187.187
        obj.wavelength_93 = var_wavelength_93
        # real
        var_spectrum_93 = 188.188
        obj.spectrum_93 = var_spectrum_93
        # real
        var_wavelength_94 = 189.189
        obj.wavelength_94 = var_wavelength_94
        # real
        var_spectrum_94 = 190.19
        obj.spectrum_94 = var_spectrum_94
        # real
        var_wavelength_95 = 191.191
        obj.wavelength_95 = var_wavelength_95
        # real
        var_spectrum_95 = 192.192
        obj.spectrum_95 = var_spectrum_95
        # real
        var_wavelength_96 = 193.193
        obj.wavelength_96 = var_wavelength_96
        # real
        var_spectrum_96 = 194.194
        obj.spectrum_96 = var_spectrum_96
        # real
        var_wavelength_97 = 195.195
        obj.wavelength_97 = var_wavelength_97
        # real
        var_spectrum_97 = 196.196
        obj.spectrum_97 = var_spectrum_97
        # real
        var_wavelength_98 = 197.197
        obj.wavelength_98 = var_wavelength_98
        # real
        var_spectrum_98 = 198.198
        obj.spectrum_98 = var_spectrum_98
        # real
        var_wavelength_99 = 199.199
        obj.wavelength_99 = var_wavelength_99
        # real
        var_spectrum_99 = 200.2
        obj.spectrum_99 = var_spectrum_99
        # real
        var_wavelength_100 = 201.201
        obj.wavelength_100 = var_wavelength_100
        # real
        var_spectrum_100 = 202.202
        obj.spectrum_100 = var_spectrum_100
        # real
        var_wavelength_101 = 203.203
        obj.wavelength_101 = var_wavelength_101
        # real
        var_spectrum_101 = 204.204
        obj.spectrum_101 = var_spectrum_101
        # real
        var_wavelength_102 = 205.205
        obj.wavelength_102 = var_wavelength_102
        # real
        var_spectrum_102 = 206.206
        obj.spectrum_102 = var_spectrum_102
        # real
        var_wavelength_103 = 207.207
        obj.wavelength_103 = var_wavelength_103
        # real
        var_spectrum_103 = 208.208
        obj.spectrum_103 = var_spectrum_103
        # real
        var_wavelength_104 = 209.209
        obj.wavelength_104 = var_wavelength_104
        # real
        var_spectrum_104 = 210.21
        obj.spectrum_104 = var_spectrum_104
        # real
        var_wavelength_105 = 211.211
        obj.wavelength_105 = var_wavelength_105
        # real
        var_spectrum_105 = 212.212
        obj.spectrum_105 = var_spectrum_105
        # real
        var_wavelength_106 = 213.213
        obj.wavelength_106 = var_wavelength_106
        # real
        var_spectrum_106 = 214.214
        obj.spectrum_106 = var_spectrum_106
        # real
        var_wavelength_107 = 215.215
        obj.wavelength_107 = var_wavelength_107
        # real
        var_spectrum_107 = 216.216
        obj.spectrum_107 = var_spectrum_107

        idf = IDF()
        idf.add(obj)
        idf.save(self.path, check=False)

        with open(self.path, mode='r') as f:
            for line in f:
                log.debug(line.strip())

        idf2 = IDF(self.path)
        self.assertEqual(idf2.sitespectrumdatas[0].name, var_name)
        self.assertEqual(idf2.sitespectrumdatas[0].spectrum_data_type, var_spectrum_data_type)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_1, var_wavelength_1)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_1, var_spectrum_1)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_2, var_wavelength_2)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_2, var_spectrum_2)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_3, var_wavelength_3)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_3, var_spectrum_3)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_4, var_wavelength_4)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_4, var_spectrum_4)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_5, var_wavelength_5)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_5, var_spectrum_5)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_6, var_wavelength_6)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_6, var_spectrum_6)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_7, var_wavelength_7)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_7, var_spectrum_7)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_8, var_wavelength_8)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_8, var_spectrum_8)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_9, var_wavelength_9)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_9, var_spectrum_9)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_10, var_wavelength_10)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_10, var_spectrum_10)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_11, var_wavelength_11)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_11, var_spectrum_11)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_12, var_wavelength_12)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_12, var_spectrum_12)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_13, var_wavelength_13)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_13, var_spectrum_13)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_14, var_wavelength_14)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_14, var_spectrum_14)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_15, var_wavelength_15)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_15, var_spectrum_15)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_16, var_wavelength_16)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_16, var_spectrum_16)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_17, var_wavelength_17)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_17, var_spectrum_17)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_18, var_wavelength_18)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_18, var_spectrum_18)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_19, var_wavelength_19)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_19, var_spectrum_19)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_20, var_wavelength_20)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_20, var_spectrum_20)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_21, var_wavelength_21)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_21, var_spectrum_21)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_22, var_wavelength_22)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_22, var_spectrum_22)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_23, var_wavelength_23)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_23, var_spectrum_23)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_24, var_wavelength_24)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_24, var_spectrum_24)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_25, var_wavelength_25)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_25, var_spectrum_25)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_26, var_wavelength_26)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_26, var_spectrum_26)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_27, var_wavelength_27)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_27, var_spectrum_27)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_28, var_wavelength_28)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_28, var_spectrum_28)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_29, var_wavelength_29)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_29, var_spectrum_29)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_30, var_wavelength_30)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_30, var_spectrum_30)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_31, var_wavelength_31)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_31, var_spectrum_31)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_32, var_wavelength_32)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_32, var_spectrum_32)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_33, var_wavelength_33)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_33, var_spectrum_33)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_34, var_wavelength_34)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_34, var_spectrum_34)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_35, var_wavelength_35)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_35, var_spectrum_35)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_36, var_wavelength_36)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_36, var_spectrum_36)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_37, var_wavelength_37)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_37, var_spectrum_37)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_38, var_wavelength_38)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_38, var_spectrum_38)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_39, var_wavelength_39)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_39, var_spectrum_39)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_40, var_wavelength_40)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_40, var_spectrum_40)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_41, var_wavelength_41)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_41, var_spectrum_41)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_42, var_wavelength_42)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_42, var_spectrum_42)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_43, var_wavelength_43)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_43, var_spectrum_43)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_44, var_wavelength_44)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_44, var_spectrum_44)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_45, var_wavelength_45)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_45, var_spectrum_45)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_46, var_wavelength_46)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_46, var_spectrum_46)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_47, var_wavelength_47)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_47, var_spectrum_47)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_48, var_wavelength_48)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_48, var_spectrum_48)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_49, var_wavelength_49)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_49, var_spectrum_49)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_50, var_wavelength_50)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_50, var_spectrum_50)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_51, var_wavelength_51)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_51, var_spectrum_51)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_52, var_wavelength_52)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_52, var_spectrum_52)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_53, var_wavelength_53)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_53, var_spectrum_53)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_54, var_wavelength_54)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_54, var_spectrum_54)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_55, var_wavelength_55)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_55, var_spectrum_55)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_56, var_wavelength_56)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_56, var_spectrum_56)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_57, var_wavelength_57)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_57, var_spectrum_57)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_58, var_wavelength_58)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_58, var_spectrum_58)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_59, var_wavelength_59)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_59, var_spectrum_59)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_60, var_wavelength_60)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_60, var_spectrum_60)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_61, var_wavelength_61)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_61, var_spectrum_61)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_62, var_wavelength_62)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_62, var_spectrum_62)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_63, var_wavelength_63)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_63, var_spectrum_63)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_64, var_wavelength_64)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_64, var_spectrum_64)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_65, var_wavelength_65)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_65, var_spectrum_65)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_66, var_wavelength_66)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_66, var_spectrum_66)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_67, var_wavelength_67)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_67, var_spectrum_67)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_68, var_wavelength_68)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_68, var_spectrum_68)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_69, var_wavelength_69)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_69, var_spectrum_69)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_70, var_wavelength_70)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_70, var_spectrum_70)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_71, var_wavelength_71)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_71, var_spectrum_71)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_72, var_wavelength_72)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_72, var_spectrum_72)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_73, var_wavelength_73)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_73, var_spectrum_73)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_74, var_wavelength_74)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_74, var_spectrum_74)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_75, var_wavelength_75)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_75, var_spectrum_75)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_76, var_wavelength_76)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_76, var_spectrum_76)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_77, var_wavelength_77)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_77, var_spectrum_77)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_78, var_wavelength_78)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_78, var_spectrum_78)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_79, var_wavelength_79)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_79, var_spectrum_79)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_80, var_wavelength_80)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_80, var_spectrum_80)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_81, var_wavelength_81)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_81, var_spectrum_81)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_82, var_wavelength_82)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_82, var_spectrum_82)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_83, var_wavelength_83)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_83, var_spectrum_83)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_84, var_wavelength_84)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_84, var_spectrum_84)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_85, var_wavelength_85)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_85, var_spectrum_85)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_86, var_wavelength_86)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_86, var_spectrum_86)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_87, var_wavelength_87)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_87, var_spectrum_87)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_88, var_wavelength_88)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_88, var_spectrum_88)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_89, var_wavelength_89)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_89, var_spectrum_89)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_90, var_wavelength_90)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_90, var_spectrum_90)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_91, var_wavelength_91)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_91, var_spectrum_91)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_92, var_wavelength_92)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_92, var_spectrum_92)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_93, var_wavelength_93)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_93, var_spectrum_93)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_94, var_wavelength_94)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_94, var_spectrum_94)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_95, var_wavelength_95)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_95, var_spectrum_95)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_96, var_wavelength_96)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_96, var_spectrum_96)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_97, var_wavelength_97)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_97, var_spectrum_97)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_98, var_wavelength_98)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_98, var_spectrum_98)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_99, var_wavelength_99)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_99, var_spectrum_99)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_100, var_wavelength_100)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_100, var_spectrum_100)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_101, var_wavelength_101)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_101, var_spectrum_101)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_102, var_wavelength_102)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_102, var_spectrum_102)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_103, var_wavelength_103)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_103, var_spectrum_103)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_104, var_wavelength_104)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_104, var_spectrum_104)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_105, var_wavelength_105)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_105, var_spectrum_105)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_106, var_wavelength_106)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_106, var_spectrum_106)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].wavelength_107, var_wavelength_107)
        self.assertAlmostEqual(idf2.sitespectrumdatas[0].spectrum_107, var_spectrum_107)