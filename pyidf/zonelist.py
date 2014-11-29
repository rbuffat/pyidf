from collections import OrderedDict

class ZoneList(object):
    """ Corresponds to IDD object `ZoneList`
        Defines a list of thermal zones which can be referenced as a group. The ZoneList name
        may be used elsewhere in the input to apply a parameter to all zones in the list.
        ZoneLists can be used effectively with the following objects: People, Lights,
        ElectricEquipment, GasEquipment, HotWaterEquipment, ZoneInfiltration:DesignFlowRate,
        ZoneVentilation:DesignFlowRate, Sizing:Zone, ZoneControl:Thermostat, and others.
    """
    internal_name = "ZoneList"
    field_count = 141

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone 1 Name"] = None
        self._data["Zone 2 Name"] = None
        self._data["Zone 3 Name"] = None
        self._data["Zone 4 Name"] = None
        self._data["Zone 5 Name"] = None
        self._data["Zone 6 Name"] = None
        self._data["Zone 7 Name"] = None
        self._data["Zone 8 Name"] = None
        self._data["Zone 9 Name"] = None
        self._data["Zone 10 Name"] = None
        self._data["Zone 11 Name"] = None
        self._data["Zone 12 Name"] = None
        self._data["Zone 13 Name"] = None
        self._data["Zone 14 Name"] = None
        self._data["Zone 15 Name"] = None
        self._data["Zone 16 Name"] = None
        self._data["Zone 17 Name"] = None
        self._data["Zone 18 Name"] = None
        self._data["Zone 19 Name"] = None
        self._data["Zone 20 Name"] = None
        self._data["Zone 21 Name"] = None
        self._data["Zone 22 Name"] = None
        self._data["Zone 23 Name"] = None
        self._data["Zone 24 Name"] = None
        self._data["Zone 25 Name"] = None
        self._data["Zone 26 Name"] = None
        self._data["Zone 27 Name"] = None
        self._data["Zone 28 Name"] = None
        self._data["Zone 29 Name"] = None
        self._data["Zone 30 Name"] = None
        self._data["Zone 31 Name"] = None
        self._data["Zone 32 Name"] = None
        self._data["Zone 33 Name"] = None
        self._data["Zone 34 Name"] = None
        self._data["Zone 35 Name"] = None
        self._data["Zone 36 Name"] = None
        self._data["Zone 37 Name"] = None
        self._data["Zone 38 Name"] = None
        self._data["Zone 39 Name"] = None
        self._data["Zone 40 Name"] = None
        self._data["Zone 41 Name"] = None
        self._data["Zone 42 Name"] = None
        self._data["Zone 43 Name"] = None
        self._data["Zone 44 Name"] = None
        self._data["Zone 45 Name"] = None
        self._data["Zone 46 Name"] = None
        self._data["Zone 47 Name"] = None
        self._data["Zone 48 Name"] = None
        self._data["Zone 49 Name"] = None
        self._data["Zone 50 Name"] = None
        self._data["Zone 51 Name"] = None
        self._data["Zone 52 Name"] = None
        self._data["Zone 53 Name"] = None
        self._data["Zone 54 Name"] = None
        self._data["Zone 55 Name"] = None
        self._data["Zone 56 Name"] = None
        self._data["Zone 57 Name"] = None
        self._data["Zone 58 Name"] = None
        self._data["Zone 59 Name"] = None
        self._data["Zone 60 Name"] = None
        self._data["Zone 61 Name"] = None
        self._data["Zone 62 Name"] = None
        self._data["Zone 63 Name"] = None
        self._data["Zone 64 Name"] = None
        self._data["Zone 65 Name"] = None
        self._data["Zone 66 Name"] = None
        self._data["Zone 67 Name"] = None
        self._data["Zone 68 Name"] = None
        self._data["Zone 69 Name"] = None
        self._data["Zone 70 Name"] = None
        self._data["Zone 71 Name"] = None
        self._data["Zone 72 Name"] = None
        self._data["Zone 73 Name"] = None
        self._data["Zone 74 Name"] = None
        self._data["Zone 75 Name"] = None
        self._data["Zone 76 Name"] = None
        self._data["Zone 77 Name"] = None
        self._data["Zone 78 Name"] = None
        self._data["Zone 79 Name"] = None
        self._data["Zone 80 Name"] = None
        self._data["Zone 81 Name"] = None
        self._data["Zone 82 Name"] = None
        self._data["Zone 83 Name"] = None
        self._data["Zone 84 Name"] = None
        self._data["Zone 85 Name"] = None
        self._data["Zone 86 Name"] = None
        self._data["Zone 87 Name"] = None
        self._data["Zone 88 Name"] = None
        self._data["Zone 89 Name"] = None
        self._data["Zone 90 Name"] = None
        self._data["Zone 91 Name"] = None
        self._data["Zone 92 Name"] = None
        self._data["Zone 93 Name"] = None
        self._data["Zone 94 Name"] = None
        self._data["Zone 95 Name"] = None
        self._data["Zone 96 Name"] = None
        self._data["Zone 97 Name"] = None
        self._data["Zone 98 Name"] = None
        self._data["Zone 99 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None
        self._data["Zone 100 Name"] = None

    def read(self, vals):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_3_name = None
        else:
            self.zone_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_4_name = None
        else:
            self.zone_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_5_name = None
        else:
            self.zone_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_6_name = None
        else:
            self.zone_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_7_name = None
        else:
            self.zone_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_8_name = None
        else:
            self.zone_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_9_name = None
        else:
            self.zone_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_10_name = None
        else:
            self.zone_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_11_name = None
        else:
            self.zone_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_12_name = None
        else:
            self.zone_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_13_name = None
        else:
            self.zone_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_14_name = None
        else:
            self.zone_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_15_name = None
        else:
            self.zone_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_16_name = None
        else:
            self.zone_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_17_name = None
        else:
            self.zone_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_18_name = None
        else:
            self.zone_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_19_name = None
        else:
            self.zone_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_20_name = None
        else:
            self.zone_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_21_name = None
        else:
            self.zone_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_22_name = None
        else:
            self.zone_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_23_name = None
        else:
            self.zone_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_24_name = None
        else:
            self.zone_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_25_name = None
        else:
            self.zone_25_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_26_name = None
        else:
            self.zone_26_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_27_name = None
        else:
            self.zone_27_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_28_name = None
        else:
            self.zone_28_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_29_name = None
        else:
            self.zone_29_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_30_name = None
        else:
            self.zone_30_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_31_name = None
        else:
            self.zone_31_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_32_name = None
        else:
            self.zone_32_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_33_name = None
        else:
            self.zone_33_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_34_name = None
        else:
            self.zone_34_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_35_name = None
        else:
            self.zone_35_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_36_name = None
        else:
            self.zone_36_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_37_name = None
        else:
            self.zone_37_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_38_name = None
        else:
            self.zone_38_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_39_name = None
        else:
            self.zone_39_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_40_name = None
        else:
            self.zone_40_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_41_name = None
        else:
            self.zone_41_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_42_name = None
        else:
            self.zone_42_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_43_name = None
        else:
            self.zone_43_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_44_name = None
        else:
            self.zone_44_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_45_name = None
        else:
            self.zone_45_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_46_name = None
        else:
            self.zone_46_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_47_name = None
        else:
            self.zone_47_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_48_name = None
        else:
            self.zone_48_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_49_name = None
        else:
            self.zone_49_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_50_name = None
        else:
            self.zone_50_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_51_name = None
        else:
            self.zone_51_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_52_name = None
        else:
            self.zone_52_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_53_name = None
        else:
            self.zone_53_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_54_name = None
        else:
            self.zone_54_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_55_name = None
        else:
            self.zone_55_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_56_name = None
        else:
            self.zone_56_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_57_name = None
        else:
            self.zone_57_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_58_name = None
        else:
            self.zone_58_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_59_name = None
        else:
            self.zone_59_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_60_name = None
        else:
            self.zone_60_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_61_name = None
        else:
            self.zone_61_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_62_name = None
        else:
            self.zone_62_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_63_name = None
        else:
            self.zone_63_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_64_name = None
        else:
            self.zone_64_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_65_name = None
        else:
            self.zone_65_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_66_name = None
        else:
            self.zone_66_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_67_name = None
        else:
            self.zone_67_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_68_name = None
        else:
            self.zone_68_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_69_name = None
        else:
            self.zone_69_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_70_name = None
        else:
            self.zone_70_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_71_name = None
        else:
            self.zone_71_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_72_name = None
        else:
            self.zone_72_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_73_name = None
        else:
            self.zone_73_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_74_name = None
        else:
            self.zone_74_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_75_name = None
        else:
            self.zone_75_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_76_name = None
        else:
            self.zone_76_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_77_name = None
        else:
            self.zone_77_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_78_name = None
        else:
            self.zone_78_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_79_name = None
        else:
            self.zone_79_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_80_name = None
        else:
            self.zone_80_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_81_name = None
        else:
            self.zone_81_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_82_name = None
        else:
            self.zone_82_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_83_name = None
        else:
            self.zone_83_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_84_name = None
        else:
            self.zone_84_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_85_name = None
        else:
            self.zone_85_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_86_name = None
        else:
            self.zone_86_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_87_name = None
        else:
            self.zone_87_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_88_name = None
        else:
            self.zone_88_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_89_name = None
        else:
            self.zone_89_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_90_name = None
        else:
            self.zone_90_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_91_name = None
        else:
            self.zone_91_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_92_name = None
        else:
            self.zone_92_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_93_name = None
        else:
            self.zone_93_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_94_name = None
        else:
            self.zone_94_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_95_name = None
        else:
            self.zone_95_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_96_name = None
        else:
            self.zone_96_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_97_name = None
        else:
            self.zone_97_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_98_name = None
        else:
            self.zone_98_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_99_name = None
        else:
            self.zone_99_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_100_name = None
        else:
            self.zone_100_name = vals[i]
        i += 1

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `name`
        Name of the Zone List

        Args:
            value (str): value for IDD Field `name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_1_name(self):
        """Get zone_1_name

        Returns:
            str: the value of `zone_1_name` or None if not set
        """
        return self._data["Zone 1 Name"]

    @zone_1_name.setter
    def zone_1_name(self, value=None):
        """  Corresponds to IDD Field `zone_1_name`

        Args:
            value (str): value for IDD Field `zone_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_1_name`')

        self._data["Zone 1 Name"] = value

    @property
    def zone_2_name(self):
        """Get zone_2_name

        Returns:
            str: the value of `zone_2_name` or None if not set
        """
        return self._data["Zone 2 Name"]

    @zone_2_name.setter
    def zone_2_name(self, value=None):
        """  Corresponds to IDD Field `zone_2_name`

        Args:
            value (str): value for IDD Field `zone_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_2_name`')

        self._data["Zone 2 Name"] = value

    @property
    def zone_3_name(self):
        """Get zone_3_name

        Returns:
            str: the value of `zone_3_name` or None if not set
        """
        return self._data["Zone 3 Name"]

    @zone_3_name.setter
    def zone_3_name(self, value=None):
        """  Corresponds to IDD Field `zone_3_name`

        Args:
            value (str): value for IDD Field `zone_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_3_name`')

        self._data["Zone 3 Name"] = value

    @property
    def zone_4_name(self):
        """Get zone_4_name

        Returns:
            str: the value of `zone_4_name` or None if not set
        """
        return self._data["Zone 4 Name"]

    @zone_4_name.setter
    def zone_4_name(self, value=None):
        """  Corresponds to IDD Field `zone_4_name`

        Args:
            value (str): value for IDD Field `zone_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_4_name`')

        self._data["Zone 4 Name"] = value

    @property
    def zone_5_name(self):
        """Get zone_5_name

        Returns:
            str: the value of `zone_5_name` or None if not set
        """
        return self._data["Zone 5 Name"]

    @zone_5_name.setter
    def zone_5_name(self, value=None):
        """  Corresponds to IDD Field `zone_5_name`

        Args:
            value (str): value for IDD Field `zone_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_5_name`')

        self._data["Zone 5 Name"] = value

    @property
    def zone_6_name(self):
        """Get zone_6_name

        Returns:
            str: the value of `zone_6_name` or None if not set
        """
        return self._data["Zone 6 Name"]

    @zone_6_name.setter
    def zone_6_name(self, value=None):
        """  Corresponds to IDD Field `zone_6_name`

        Args:
            value (str): value for IDD Field `zone_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_6_name`')

        self._data["Zone 6 Name"] = value

    @property
    def zone_7_name(self):
        """Get zone_7_name

        Returns:
            str: the value of `zone_7_name` or None if not set
        """
        return self._data["Zone 7 Name"]

    @zone_7_name.setter
    def zone_7_name(self, value=None):
        """  Corresponds to IDD Field `zone_7_name`

        Args:
            value (str): value for IDD Field `zone_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_7_name`')

        self._data["Zone 7 Name"] = value

    @property
    def zone_8_name(self):
        """Get zone_8_name

        Returns:
            str: the value of `zone_8_name` or None if not set
        """
        return self._data["Zone 8 Name"]

    @zone_8_name.setter
    def zone_8_name(self, value=None):
        """  Corresponds to IDD Field `zone_8_name`

        Args:
            value (str): value for IDD Field `zone_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_8_name`')

        self._data["Zone 8 Name"] = value

    @property
    def zone_9_name(self):
        """Get zone_9_name

        Returns:
            str: the value of `zone_9_name` or None if not set
        """
        return self._data["Zone 9 Name"]

    @zone_9_name.setter
    def zone_9_name(self, value=None):
        """  Corresponds to IDD Field `zone_9_name`

        Args:
            value (str): value for IDD Field `zone_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_9_name`')

        self._data["Zone 9 Name"] = value

    @property
    def zone_10_name(self):
        """Get zone_10_name

        Returns:
            str: the value of `zone_10_name` or None if not set
        """
        return self._data["Zone 10 Name"]

    @zone_10_name.setter
    def zone_10_name(self, value=None):
        """  Corresponds to IDD Field `zone_10_name`

        Args:
            value (str): value for IDD Field `zone_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_10_name`')

        self._data["Zone 10 Name"] = value

    @property
    def zone_11_name(self):
        """Get zone_11_name

        Returns:
            str: the value of `zone_11_name` or None if not set
        """
        return self._data["Zone 11 Name"]

    @zone_11_name.setter
    def zone_11_name(self, value=None):
        """  Corresponds to IDD Field `zone_11_name`

        Args:
            value (str): value for IDD Field `zone_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_11_name`')

        self._data["Zone 11 Name"] = value

    @property
    def zone_12_name(self):
        """Get zone_12_name

        Returns:
            str: the value of `zone_12_name` or None if not set
        """
        return self._data["Zone 12 Name"]

    @zone_12_name.setter
    def zone_12_name(self, value=None):
        """  Corresponds to IDD Field `zone_12_name`

        Args:
            value (str): value for IDD Field `zone_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_12_name`')

        self._data["Zone 12 Name"] = value

    @property
    def zone_13_name(self):
        """Get zone_13_name

        Returns:
            str: the value of `zone_13_name` or None if not set
        """
        return self._data["Zone 13 Name"]

    @zone_13_name.setter
    def zone_13_name(self, value=None):
        """  Corresponds to IDD Field `zone_13_name`

        Args:
            value (str): value for IDD Field `zone_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_13_name`')

        self._data["Zone 13 Name"] = value

    @property
    def zone_14_name(self):
        """Get zone_14_name

        Returns:
            str: the value of `zone_14_name` or None if not set
        """
        return self._data["Zone 14 Name"]

    @zone_14_name.setter
    def zone_14_name(self, value=None):
        """  Corresponds to IDD Field `zone_14_name`

        Args:
            value (str): value for IDD Field `zone_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_14_name`')

        self._data["Zone 14 Name"] = value

    @property
    def zone_15_name(self):
        """Get zone_15_name

        Returns:
            str: the value of `zone_15_name` or None if not set
        """
        return self._data["Zone 15 Name"]

    @zone_15_name.setter
    def zone_15_name(self, value=None):
        """  Corresponds to IDD Field `zone_15_name`

        Args:
            value (str): value for IDD Field `zone_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_15_name`')

        self._data["Zone 15 Name"] = value

    @property
    def zone_16_name(self):
        """Get zone_16_name

        Returns:
            str: the value of `zone_16_name` or None if not set
        """
        return self._data["Zone 16 Name"]

    @zone_16_name.setter
    def zone_16_name(self, value=None):
        """  Corresponds to IDD Field `zone_16_name`

        Args:
            value (str): value for IDD Field `zone_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_16_name`')

        self._data["Zone 16 Name"] = value

    @property
    def zone_17_name(self):
        """Get zone_17_name

        Returns:
            str: the value of `zone_17_name` or None if not set
        """
        return self._data["Zone 17 Name"]

    @zone_17_name.setter
    def zone_17_name(self, value=None):
        """  Corresponds to IDD Field `zone_17_name`

        Args:
            value (str): value for IDD Field `zone_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_17_name`')

        self._data["Zone 17 Name"] = value

    @property
    def zone_18_name(self):
        """Get zone_18_name

        Returns:
            str: the value of `zone_18_name` or None if not set
        """
        return self._data["Zone 18 Name"]

    @zone_18_name.setter
    def zone_18_name(self, value=None):
        """  Corresponds to IDD Field `zone_18_name`

        Args:
            value (str): value for IDD Field `zone_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_18_name`')

        self._data["Zone 18 Name"] = value

    @property
    def zone_19_name(self):
        """Get zone_19_name

        Returns:
            str: the value of `zone_19_name` or None if not set
        """
        return self._data["Zone 19 Name"]

    @zone_19_name.setter
    def zone_19_name(self, value=None):
        """  Corresponds to IDD Field `zone_19_name`

        Args:
            value (str): value for IDD Field `zone_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_19_name`')

        self._data["Zone 19 Name"] = value

    @property
    def zone_20_name(self):
        """Get zone_20_name

        Returns:
            str: the value of `zone_20_name` or None if not set
        """
        return self._data["Zone 20 Name"]

    @zone_20_name.setter
    def zone_20_name(self, value=None):
        """  Corresponds to IDD Field `zone_20_name`

        Args:
            value (str): value for IDD Field `zone_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_20_name`')

        self._data["Zone 20 Name"] = value

    @property
    def zone_21_name(self):
        """Get zone_21_name

        Returns:
            str: the value of `zone_21_name` or None if not set
        """
        return self._data["Zone 21 Name"]

    @zone_21_name.setter
    def zone_21_name(self, value=None):
        """  Corresponds to IDD Field `zone_21_name`

        Args:
            value (str): value for IDD Field `zone_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_21_name`')

        self._data["Zone 21 Name"] = value

    @property
    def zone_22_name(self):
        """Get zone_22_name

        Returns:
            str: the value of `zone_22_name` or None if not set
        """
        return self._data["Zone 22 Name"]

    @zone_22_name.setter
    def zone_22_name(self, value=None):
        """  Corresponds to IDD Field `zone_22_name`

        Args:
            value (str): value for IDD Field `zone_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_22_name`')

        self._data["Zone 22 Name"] = value

    @property
    def zone_23_name(self):
        """Get zone_23_name

        Returns:
            str: the value of `zone_23_name` or None if not set
        """
        return self._data["Zone 23 Name"]

    @zone_23_name.setter
    def zone_23_name(self, value=None):
        """  Corresponds to IDD Field `zone_23_name`

        Args:
            value (str): value for IDD Field `zone_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_23_name`')

        self._data["Zone 23 Name"] = value

    @property
    def zone_24_name(self):
        """Get zone_24_name

        Returns:
            str: the value of `zone_24_name` or None if not set
        """
        return self._data["Zone 24 Name"]

    @zone_24_name.setter
    def zone_24_name(self, value=None):
        """  Corresponds to IDD Field `zone_24_name`

        Args:
            value (str): value for IDD Field `zone_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_24_name`')

        self._data["Zone 24 Name"] = value

    @property
    def zone_25_name(self):
        """Get zone_25_name

        Returns:
            str: the value of `zone_25_name` or None if not set
        """
        return self._data["Zone 25 Name"]

    @zone_25_name.setter
    def zone_25_name(self, value=None):
        """  Corresponds to IDD Field `zone_25_name`

        Args:
            value (str): value for IDD Field `zone_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_25_name`')

        self._data["Zone 25 Name"] = value

    @property
    def zone_26_name(self):
        """Get zone_26_name

        Returns:
            str: the value of `zone_26_name` or None if not set
        """
        return self._data["Zone 26 Name"]

    @zone_26_name.setter
    def zone_26_name(self, value=None):
        """  Corresponds to IDD Field `zone_26_name`

        Args:
            value (str): value for IDD Field `zone_26_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_26_name`')

        self._data["Zone 26 Name"] = value

    @property
    def zone_27_name(self):
        """Get zone_27_name

        Returns:
            str: the value of `zone_27_name` or None if not set
        """
        return self._data["Zone 27 Name"]

    @zone_27_name.setter
    def zone_27_name(self, value=None):
        """  Corresponds to IDD Field `zone_27_name`

        Args:
            value (str): value for IDD Field `zone_27_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_27_name`')

        self._data["Zone 27 Name"] = value

    @property
    def zone_28_name(self):
        """Get zone_28_name

        Returns:
            str: the value of `zone_28_name` or None if not set
        """
        return self._data["Zone 28 Name"]

    @zone_28_name.setter
    def zone_28_name(self, value=None):
        """  Corresponds to IDD Field `zone_28_name`

        Args:
            value (str): value for IDD Field `zone_28_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_28_name`')

        self._data["Zone 28 Name"] = value

    @property
    def zone_29_name(self):
        """Get zone_29_name

        Returns:
            str: the value of `zone_29_name` or None if not set
        """
        return self._data["Zone 29 Name"]

    @zone_29_name.setter
    def zone_29_name(self, value=None):
        """  Corresponds to IDD Field `zone_29_name`

        Args:
            value (str): value for IDD Field `zone_29_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_29_name`')

        self._data["Zone 29 Name"] = value

    @property
    def zone_30_name(self):
        """Get zone_30_name

        Returns:
            str: the value of `zone_30_name` or None if not set
        """
        return self._data["Zone 30 Name"]

    @zone_30_name.setter
    def zone_30_name(self, value=None):
        """  Corresponds to IDD Field `zone_30_name`

        Args:
            value (str): value for IDD Field `zone_30_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_30_name`')

        self._data["Zone 30 Name"] = value

    @property
    def zone_31_name(self):
        """Get zone_31_name

        Returns:
            str: the value of `zone_31_name` or None if not set
        """
        return self._data["Zone 31 Name"]

    @zone_31_name.setter
    def zone_31_name(self, value=None):
        """  Corresponds to IDD Field `zone_31_name`

        Args:
            value (str): value for IDD Field `zone_31_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_31_name`')

        self._data["Zone 31 Name"] = value

    @property
    def zone_32_name(self):
        """Get zone_32_name

        Returns:
            str: the value of `zone_32_name` or None if not set
        """
        return self._data["Zone 32 Name"]

    @zone_32_name.setter
    def zone_32_name(self, value=None):
        """  Corresponds to IDD Field `zone_32_name`

        Args:
            value (str): value for IDD Field `zone_32_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_32_name`')

        self._data["Zone 32 Name"] = value

    @property
    def zone_33_name(self):
        """Get zone_33_name

        Returns:
            str: the value of `zone_33_name` or None if not set
        """
        return self._data["Zone 33 Name"]

    @zone_33_name.setter
    def zone_33_name(self, value=None):
        """  Corresponds to IDD Field `zone_33_name`

        Args:
            value (str): value for IDD Field `zone_33_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_33_name`')

        self._data["Zone 33 Name"] = value

    @property
    def zone_34_name(self):
        """Get zone_34_name

        Returns:
            str: the value of `zone_34_name` or None if not set
        """
        return self._data["Zone 34 Name"]

    @zone_34_name.setter
    def zone_34_name(self, value=None):
        """  Corresponds to IDD Field `zone_34_name`

        Args:
            value (str): value for IDD Field `zone_34_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_34_name`')

        self._data["Zone 34 Name"] = value

    @property
    def zone_35_name(self):
        """Get zone_35_name

        Returns:
            str: the value of `zone_35_name` or None if not set
        """
        return self._data["Zone 35 Name"]

    @zone_35_name.setter
    def zone_35_name(self, value=None):
        """  Corresponds to IDD Field `zone_35_name`

        Args:
            value (str): value for IDD Field `zone_35_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_35_name`')

        self._data["Zone 35 Name"] = value

    @property
    def zone_36_name(self):
        """Get zone_36_name

        Returns:
            str: the value of `zone_36_name` or None if not set
        """
        return self._data["Zone 36 Name"]

    @zone_36_name.setter
    def zone_36_name(self, value=None):
        """  Corresponds to IDD Field `zone_36_name`

        Args:
            value (str): value for IDD Field `zone_36_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_36_name`')

        self._data["Zone 36 Name"] = value

    @property
    def zone_37_name(self):
        """Get zone_37_name

        Returns:
            str: the value of `zone_37_name` or None if not set
        """
        return self._data["Zone 37 Name"]

    @zone_37_name.setter
    def zone_37_name(self, value=None):
        """  Corresponds to IDD Field `zone_37_name`

        Args:
            value (str): value for IDD Field `zone_37_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_37_name`')

        self._data["Zone 37 Name"] = value

    @property
    def zone_38_name(self):
        """Get zone_38_name

        Returns:
            str: the value of `zone_38_name` or None if not set
        """
        return self._data["Zone 38 Name"]

    @zone_38_name.setter
    def zone_38_name(self, value=None):
        """  Corresponds to IDD Field `zone_38_name`

        Args:
            value (str): value for IDD Field `zone_38_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_38_name`')

        self._data["Zone 38 Name"] = value

    @property
    def zone_39_name(self):
        """Get zone_39_name

        Returns:
            str: the value of `zone_39_name` or None if not set
        """
        return self._data["Zone 39 Name"]

    @zone_39_name.setter
    def zone_39_name(self, value=None):
        """  Corresponds to IDD Field `zone_39_name`

        Args:
            value (str): value for IDD Field `zone_39_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_39_name`')

        self._data["Zone 39 Name"] = value

    @property
    def zone_40_name(self):
        """Get zone_40_name

        Returns:
            str: the value of `zone_40_name` or None if not set
        """
        return self._data["Zone 40 Name"]

    @zone_40_name.setter
    def zone_40_name(self, value=None):
        """  Corresponds to IDD Field `zone_40_name`

        Args:
            value (str): value for IDD Field `zone_40_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_40_name`')

        self._data["Zone 40 Name"] = value

    @property
    def zone_41_name(self):
        """Get zone_41_name

        Returns:
            str: the value of `zone_41_name` or None if not set
        """
        return self._data["Zone 41 Name"]

    @zone_41_name.setter
    def zone_41_name(self, value=None):
        """  Corresponds to IDD Field `zone_41_name`

        Args:
            value (str): value for IDD Field `zone_41_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_41_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_41_name`')

        self._data["Zone 41 Name"] = value

    @property
    def zone_42_name(self):
        """Get zone_42_name

        Returns:
            str: the value of `zone_42_name` or None if not set
        """
        return self._data["Zone 42 Name"]

    @zone_42_name.setter
    def zone_42_name(self, value=None):
        """  Corresponds to IDD Field `zone_42_name`

        Args:
            value (str): value for IDD Field `zone_42_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_42_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_42_name`')

        self._data["Zone 42 Name"] = value

    @property
    def zone_43_name(self):
        """Get zone_43_name

        Returns:
            str: the value of `zone_43_name` or None if not set
        """
        return self._data["Zone 43 Name"]

    @zone_43_name.setter
    def zone_43_name(self, value=None):
        """  Corresponds to IDD Field `zone_43_name`

        Args:
            value (str): value for IDD Field `zone_43_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_43_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_43_name`')

        self._data["Zone 43 Name"] = value

    @property
    def zone_44_name(self):
        """Get zone_44_name

        Returns:
            str: the value of `zone_44_name` or None if not set
        """
        return self._data["Zone 44 Name"]

    @zone_44_name.setter
    def zone_44_name(self, value=None):
        """  Corresponds to IDD Field `zone_44_name`

        Args:
            value (str): value for IDD Field `zone_44_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_44_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_44_name`')

        self._data["Zone 44 Name"] = value

    @property
    def zone_45_name(self):
        """Get zone_45_name

        Returns:
            str: the value of `zone_45_name` or None if not set
        """
        return self._data["Zone 45 Name"]

    @zone_45_name.setter
    def zone_45_name(self, value=None):
        """  Corresponds to IDD Field `zone_45_name`

        Args:
            value (str): value for IDD Field `zone_45_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_45_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_45_name`')

        self._data["Zone 45 Name"] = value

    @property
    def zone_46_name(self):
        """Get zone_46_name

        Returns:
            str: the value of `zone_46_name` or None if not set
        """
        return self._data["Zone 46 Name"]

    @zone_46_name.setter
    def zone_46_name(self, value=None):
        """  Corresponds to IDD Field `zone_46_name`

        Args:
            value (str): value for IDD Field `zone_46_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_46_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_46_name`')

        self._data["Zone 46 Name"] = value

    @property
    def zone_47_name(self):
        """Get zone_47_name

        Returns:
            str: the value of `zone_47_name` or None if not set
        """
        return self._data["Zone 47 Name"]

    @zone_47_name.setter
    def zone_47_name(self, value=None):
        """  Corresponds to IDD Field `zone_47_name`

        Args:
            value (str): value for IDD Field `zone_47_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_47_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_47_name`')

        self._data["Zone 47 Name"] = value

    @property
    def zone_48_name(self):
        """Get zone_48_name

        Returns:
            str: the value of `zone_48_name` or None if not set
        """
        return self._data["Zone 48 Name"]

    @zone_48_name.setter
    def zone_48_name(self, value=None):
        """  Corresponds to IDD Field `zone_48_name`

        Args:
            value (str): value for IDD Field `zone_48_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_48_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_48_name`')

        self._data["Zone 48 Name"] = value

    @property
    def zone_49_name(self):
        """Get zone_49_name

        Returns:
            str: the value of `zone_49_name` or None if not set
        """
        return self._data["Zone 49 Name"]

    @zone_49_name.setter
    def zone_49_name(self, value=None):
        """  Corresponds to IDD Field `zone_49_name`

        Args:
            value (str): value for IDD Field `zone_49_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_49_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_49_name`')

        self._data["Zone 49 Name"] = value

    @property
    def zone_50_name(self):
        """Get zone_50_name

        Returns:
            str: the value of `zone_50_name` or None if not set
        """
        return self._data["Zone 50 Name"]

    @zone_50_name.setter
    def zone_50_name(self, value=None):
        """  Corresponds to IDD Field `zone_50_name`

        Args:
            value (str): value for IDD Field `zone_50_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_50_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_50_name`')

        self._data["Zone 50 Name"] = value

    @property
    def zone_51_name(self):
        """Get zone_51_name

        Returns:
            str: the value of `zone_51_name` or None if not set
        """
        return self._data["Zone 51 Name"]

    @zone_51_name.setter
    def zone_51_name(self, value=None):
        """  Corresponds to IDD Field `zone_51_name`

        Args:
            value (str): value for IDD Field `zone_51_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_51_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_51_name`')

        self._data["Zone 51 Name"] = value

    @property
    def zone_52_name(self):
        """Get zone_52_name

        Returns:
            str: the value of `zone_52_name` or None if not set
        """
        return self._data["Zone 52 Name"]

    @zone_52_name.setter
    def zone_52_name(self, value=None):
        """  Corresponds to IDD Field `zone_52_name`

        Args:
            value (str): value for IDD Field `zone_52_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_52_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_52_name`')

        self._data["Zone 52 Name"] = value

    @property
    def zone_53_name(self):
        """Get zone_53_name

        Returns:
            str: the value of `zone_53_name` or None if not set
        """
        return self._data["Zone 53 Name"]

    @zone_53_name.setter
    def zone_53_name(self, value=None):
        """  Corresponds to IDD Field `zone_53_name`

        Args:
            value (str): value for IDD Field `zone_53_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_53_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_53_name`')

        self._data["Zone 53 Name"] = value

    @property
    def zone_54_name(self):
        """Get zone_54_name

        Returns:
            str: the value of `zone_54_name` or None if not set
        """
        return self._data["Zone 54 Name"]

    @zone_54_name.setter
    def zone_54_name(self, value=None):
        """  Corresponds to IDD Field `zone_54_name`

        Args:
            value (str): value for IDD Field `zone_54_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_54_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_54_name`')

        self._data["Zone 54 Name"] = value

    @property
    def zone_55_name(self):
        """Get zone_55_name

        Returns:
            str: the value of `zone_55_name` or None if not set
        """
        return self._data["Zone 55 Name"]

    @zone_55_name.setter
    def zone_55_name(self, value=None):
        """  Corresponds to IDD Field `zone_55_name`

        Args:
            value (str): value for IDD Field `zone_55_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_55_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_55_name`')

        self._data["Zone 55 Name"] = value

    @property
    def zone_56_name(self):
        """Get zone_56_name

        Returns:
            str: the value of `zone_56_name` or None if not set
        """
        return self._data["Zone 56 Name"]

    @zone_56_name.setter
    def zone_56_name(self, value=None):
        """  Corresponds to IDD Field `zone_56_name`

        Args:
            value (str): value for IDD Field `zone_56_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_56_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_56_name`')

        self._data["Zone 56 Name"] = value

    @property
    def zone_57_name(self):
        """Get zone_57_name

        Returns:
            str: the value of `zone_57_name` or None if not set
        """
        return self._data["Zone 57 Name"]

    @zone_57_name.setter
    def zone_57_name(self, value=None):
        """  Corresponds to IDD Field `zone_57_name`

        Args:
            value (str): value for IDD Field `zone_57_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_57_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_57_name`')

        self._data["Zone 57 Name"] = value

    @property
    def zone_58_name(self):
        """Get zone_58_name

        Returns:
            str: the value of `zone_58_name` or None if not set
        """
        return self._data["Zone 58 Name"]

    @zone_58_name.setter
    def zone_58_name(self, value=None):
        """  Corresponds to IDD Field `zone_58_name`

        Args:
            value (str): value for IDD Field `zone_58_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_58_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_58_name`')

        self._data["Zone 58 Name"] = value

    @property
    def zone_59_name(self):
        """Get zone_59_name

        Returns:
            str: the value of `zone_59_name` or None if not set
        """
        return self._data["Zone 59 Name"]

    @zone_59_name.setter
    def zone_59_name(self, value=None):
        """  Corresponds to IDD Field `zone_59_name`

        Args:
            value (str): value for IDD Field `zone_59_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_59_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_59_name`')

        self._data["Zone 59 Name"] = value

    @property
    def zone_60_name(self):
        """Get zone_60_name

        Returns:
            str: the value of `zone_60_name` or None if not set
        """
        return self._data["Zone 60 Name"]

    @zone_60_name.setter
    def zone_60_name(self, value=None):
        """  Corresponds to IDD Field `zone_60_name`

        Args:
            value (str): value for IDD Field `zone_60_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_60_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_60_name`')

        self._data["Zone 60 Name"] = value

    @property
    def zone_61_name(self):
        """Get zone_61_name

        Returns:
            str: the value of `zone_61_name` or None if not set
        """
        return self._data["Zone 61 Name"]

    @zone_61_name.setter
    def zone_61_name(self, value=None):
        """  Corresponds to IDD Field `zone_61_name`

        Args:
            value (str): value for IDD Field `zone_61_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_61_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_61_name`')

        self._data["Zone 61 Name"] = value

    @property
    def zone_62_name(self):
        """Get zone_62_name

        Returns:
            str: the value of `zone_62_name` or None if not set
        """
        return self._data["Zone 62 Name"]

    @zone_62_name.setter
    def zone_62_name(self, value=None):
        """  Corresponds to IDD Field `zone_62_name`

        Args:
            value (str): value for IDD Field `zone_62_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_62_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_62_name`')

        self._data["Zone 62 Name"] = value

    @property
    def zone_63_name(self):
        """Get zone_63_name

        Returns:
            str: the value of `zone_63_name` or None if not set
        """
        return self._data["Zone 63 Name"]

    @zone_63_name.setter
    def zone_63_name(self, value=None):
        """  Corresponds to IDD Field `zone_63_name`

        Args:
            value (str): value for IDD Field `zone_63_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_63_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_63_name`')

        self._data["Zone 63 Name"] = value

    @property
    def zone_64_name(self):
        """Get zone_64_name

        Returns:
            str: the value of `zone_64_name` or None if not set
        """
        return self._data["Zone 64 Name"]

    @zone_64_name.setter
    def zone_64_name(self, value=None):
        """  Corresponds to IDD Field `zone_64_name`

        Args:
            value (str): value for IDD Field `zone_64_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_64_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_64_name`')

        self._data["Zone 64 Name"] = value

    @property
    def zone_65_name(self):
        """Get zone_65_name

        Returns:
            str: the value of `zone_65_name` or None if not set
        """
        return self._data["Zone 65 Name"]

    @zone_65_name.setter
    def zone_65_name(self, value=None):
        """  Corresponds to IDD Field `zone_65_name`

        Args:
            value (str): value for IDD Field `zone_65_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_65_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_65_name`')

        self._data["Zone 65 Name"] = value

    @property
    def zone_66_name(self):
        """Get zone_66_name

        Returns:
            str: the value of `zone_66_name` or None if not set
        """
        return self._data["Zone 66 Name"]

    @zone_66_name.setter
    def zone_66_name(self, value=None):
        """  Corresponds to IDD Field `zone_66_name`

        Args:
            value (str): value for IDD Field `zone_66_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_66_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_66_name`')

        self._data["Zone 66 Name"] = value

    @property
    def zone_67_name(self):
        """Get zone_67_name

        Returns:
            str: the value of `zone_67_name` or None if not set
        """
        return self._data["Zone 67 Name"]

    @zone_67_name.setter
    def zone_67_name(self, value=None):
        """  Corresponds to IDD Field `zone_67_name`

        Args:
            value (str): value for IDD Field `zone_67_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_67_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_67_name`')

        self._data["Zone 67 Name"] = value

    @property
    def zone_68_name(self):
        """Get zone_68_name

        Returns:
            str: the value of `zone_68_name` or None if not set
        """
        return self._data["Zone 68 Name"]

    @zone_68_name.setter
    def zone_68_name(self, value=None):
        """  Corresponds to IDD Field `zone_68_name`

        Args:
            value (str): value for IDD Field `zone_68_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_68_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_68_name`')

        self._data["Zone 68 Name"] = value

    @property
    def zone_69_name(self):
        """Get zone_69_name

        Returns:
            str: the value of `zone_69_name` or None if not set
        """
        return self._data["Zone 69 Name"]

    @zone_69_name.setter
    def zone_69_name(self, value=None):
        """  Corresponds to IDD Field `zone_69_name`

        Args:
            value (str): value for IDD Field `zone_69_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_69_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_69_name`')

        self._data["Zone 69 Name"] = value

    @property
    def zone_70_name(self):
        """Get zone_70_name

        Returns:
            str: the value of `zone_70_name` or None if not set
        """
        return self._data["Zone 70 Name"]

    @zone_70_name.setter
    def zone_70_name(self, value=None):
        """  Corresponds to IDD Field `zone_70_name`

        Args:
            value (str): value for IDD Field `zone_70_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_70_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_70_name`')

        self._data["Zone 70 Name"] = value

    @property
    def zone_71_name(self):
        """Get zone_71_name

        Returns:
            str: the value of `zone_71_name` or None if not set
        """
        return self._data["Zone 71 Name"]

    @zone_71_name.setter
    def zone_71_name(self, value=None):
        """  Corresponds to IDD Field `zone_71_name`

        Args:
            value (str): value for IDD Field `zone_71_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_71_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_71_name`')

        self._data["Zone 71 Name"] = value

    @property
    def zone_72_name(self):
        """Get zone_72_name

        Returns:
            str: the value of `zone_72_name` or None if not set
        """
        return self._data["Zone 72 Name"]

    @zone_72_name.setter
    def zone_72_name(self, value=None):
        """  Corresponds to IDD Field `zone_72_name`

        Args:
            value (str): value for IDD Field `zone_72_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_72_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_72_name`')

        self._data["Zone 72 Name"] = value

    @property
    def zone_73_name(self):
        """Get zone_73_name

        Returns:
            str: the value of `zone_73_name` or None if not set
        """
        return self._data["Zone 73 Name"]

    @zone_73_name.setter
    def zone_73_name(self, value=None):
        """  Corresponds to IDD Field `zone_73_name`

        Args:
            value (str): value for IDD Field `zone_73_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_73_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_73_name`')

        self._data["Zone 73 Name"] = value

    @property
    def zone_74_name(self):
        """Get zone_74_name

        Returns:
            str: the value of `zone_74_name` or None if not set
        """
        return self._data["Zone 74 Name"]

    @zone_74_name.setter
    def zone_74_name(self, value=None):
        """  Corresponds to IDD Field `zone_74_name`

        Args:
            value (str): value for IDD Field `zone_74_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_74_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_74_name`')

        self._data["Zone 74 Name"] = value

    @property
    def zone_75_name(self):
        """Get zone_75_name

        Returns:
            str: the value of `zone_75_name` or None if not set
        """
        return self._data["Zone 75 Name"]

    @zone_75_name.setter
    def zone_75_name(self, value=None):
        """  Corresponds to IDD Field `zone_75_name`

        Args:
            value (str): value for IDD Field `zone_75_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_75_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_75_name`')

        self._data["Zone 75 Name"] = value

    @property
    def zone_76_name(self):
        """Get zone_76_name

        Returns:
            str: the value of `zone_76_name` or None if not set
        """
        return self._data["Zone 76 Name"]

    @zone_76_name.setter
    def zone_76_name(self, value=None):
        """  Corresponds to IDD Field `zone_76_name`

        Args:
            value (str): value for IDD Field `zone_76_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_76_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_76_name`')

        self._data["Zone 76 Name"] = value

    @property
    def zone_77_name(self):
        """Get zone_77_name

        Returns:
            str: the value of `zone_77_name` or None if not set
        """
        return self._data["Zone 77 Name"]

    @zone_77_name.setter
    def zone_77_name(self, value=None):
        """  Corresponds to IDD Field `zone_77_name`

        Args:
            value (str): value for IDD Field `zone_77_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_77_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_77_name`')

        self._data["Zone 77 Name"] = value

    @property
    def zone_78_name(self):
        """Get zone_78_name

        Returns:
            str: the value of `zone_78_name` or None if not set
        """
        return self._data["Zone 78 Name"]

    @zone_78_name.setter
    def zone_78_name(self, value=None):
        """  Corresponds to IDD Field `zone_78_name`

        Args:
            value (str): value for IDD Field `zone_78_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_78_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_78_name`')

        self._data["Zone 78 Name"] = value

    @property
    def zone_79_name(self):
        """Get zone_79_name

        Returns:
            str: the value of `zone_79_name` or None if not set
        """
        return self._data["Zone 79 Name"]

    @zone_79_name.setter
    def zone_79_name(self, value=None):
        """  Corresponds to IDD Field `zone_79_name`

        Args:
            value (str): value for IDD Field `zone_79_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_79_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_79_name`')

        self._data["Zone 79 Name"] = value

    @property
    def zone_80_name(self):
        """Get zone_80_name

        Returns:
            str: the value of `zone_80_name` or None if not set
        """
        return self._data["Zone 80 Name"]

    @zone_80_name.setter
    def zone_80_name(self, value=None):
        """  Corresponds to IDD Field `zone_80_name`

        Args:
            value (str): value for IDD Field `zone_80_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_80_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_80_name`')

        self._data["Zone 80 Name"] = value

    @property
    def zone_81_name(self):
        """Get zone_81_name

        Returns:
            str: the value of `zone_81_name` or None if not set
        """
        return self._data["Zone 81 Name"]

    @zone_81_name.setter
    def zone_81_name(self, value=None):
        """  Corresponds to IDD Field `zone_81_name`

        Args:
            value (str): value for IDD Field `zone_81_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_81_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_81_name`')

        self._data["Zone 81 Name"] = value

    @property
    def zone_82_name(self):
        """Get zone_82_name

        Returns:
            str: the value of `zone_82_name` or None if not set
        """
        return self._data["Zone 82 Name"]

    @zone_82_name.setter
    def zone_82_name(self, value=None):
        """  Corresponds to IDD Field `zone_82_name`

        Args:
            value (str): value for IDD Field `zone_82_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_82_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_82_name`')

        self._data["Zone 82 Name"] = value

    @property
    def zone_83_name(self):
        """Get zone_83_name

        Returns:
            str: the value of `zone_83_name` or None if not set
        """
        return self._data["Zone 83 Name"]

    @zone_83_name.setter
    def zone_83_name(self, value=None):
        """  Corresponds to IDD Field `zone_83_name`

        Args:
            value (str): value for IDD Field `zone_83_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_83_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_83_name`')

        self._data["Zone 83 Name"] = value

    @property
    def zone_84_name(self):
        """Get zone_84_name

        Returns:
            str: the value of `zone_84_name` or None if not set
        """
        return self._data["Zone 84 Name"]

    @zone_84_name.setter
    def zone_84_name(self, value=None):
        """  Corresponds to IDD Field `zone_84_name`

        Args:
            value (str): value for IDD Field `zone_84_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_84_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_84_name`')

        self._data["Zone 84 Name"] = value

    @property
    def zone_85_name(self):
        """Get zone_85_name

        Returns:
            str: the value of `zone_85_name` or None if not set
        """
        return self._data["Zone 85 Name"]

    @zone_85_name.setter
    def zone_85_name(self, value=None):
        """  Corresponds to IDD Field `zone_85_name`

        Args:
            value (str): value for IDD Field `zone_85_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_85_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_85_name`')

        self._data["Zone 85 Name"] = value

    @property
    def zone_86_name(self):
        """Get zone_86_name

        Returns:
            str: the value of `zone_86_name` or None if not set
        """
        return self._data["Zone 86 Name"]

    @zone_86_name.setter
    def zone_86_name(self, value=None):
        """  Corresponds to IDD Field `zone_86_name`

        Args:
            value (str): value for IDD Field `zone_86_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_86_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_86_name`')

        self._data["Zone 86 Name"] = value

    @property
    def zone_87_name(self):
        """Get zone_87_name

        Returns:
            str: the value of `zone_87_name` or None if not set
        """
        return self._data["Zone 87 Name"]

    @zone_87_name.setter
    def zone_87_name(self, value=None):
        """  Corresponds to IDD Field `zone_87_name`

        Args:
            value (str): value for IDD Field `zone_87_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_87_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_87_name`')

        self._data["Zone 87 Name"] = value

    @property
    def zone_88_name(self):
        """Get zone_88_name

        Returns:
            str: the value of `zone_88_name` or None if not set
        """
        return self._data["Zone 88 Name"]

    @zone_88_name.setter
    def zone_88_name(self, value=None):
        """  Corresponds to IDD Field `zone_88_name`

        Args:
            value (str): value for IDD Field `zone_88_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_88_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_88_name`')

        self._data["Zone 88 Name"] = value

    @property
    def zone_89_name(self):
        """Get zone_89_name

        Returns:
            str: the value of `zone_89_name` or None if not set
        """
        return self._data["Zone 89 Name"]

    @zone_89_name.setter
    def zone_89_name(self, value=None):
        """  Corresponds to IDD Field `zone_89_name`

        Args:
            value (str): value for IDD Field `zone_89_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_89_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_89_name`')

        self._data["Zone 89 Name"] = value

    @property
    def zone_90_name(self):
        """Get zone_90_name

        Returns:
            str: the value of `zone_90_name` or None if not set
        """
        return self._data["Zone 90 Name"]

    @zone_90_name.setter
    def zone_90_name(self, value=None):
        """  Corresponds to IDD Field `zone_90_name`

        Args:
            value (str): value for IDD Field `zone_90_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_90_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_90_name`')

        self._data["Zone 90 Name"] = value

    @property
    def zone_91_name(self):
        """Get zone_91_name

        Returns:
            str: the value of `zone_91_name` or None if not set
        """
        return self._data["Zone 91 Name"]

    @zone_91_name.setter
    def zone_91_name(self, value=None):
        """  Corresponds to IDD Field `zone_91_name`

        Args:
            value (str): value for IDD Field `zone_91_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_91_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_91_name`')

        self._data["Zone 91 Name"] = value

    @property
    def zone_92_name(self):
        """Get zone_92_name

        Returns:
            str: the value of `zone_92_name` or None if not set
        """
        return self._data["Zone 92 Name"]

    @zone_92_name.setter
    def zone_92_name(self, value=None):
        """  Corresponds to IDD Field `zone_92_name`

        Args:
            value (str): value for IDD Field `zone_92_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_92_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_92_name`')

        self._data["Zone 92 Name"] = value

    @property
    def zone_93_name(self):
        """Get zone_93_name

        Returns:
            str: the value of `zone_93_name` or None if not set
        """
        return self._data["Zone 93 Name"]

    @zone_93_name.setter
    def zone_93_name(self, value=None):
        """  Corresponds to IDD Field `zone_93_name`

        Args:
            value (str): value for IDD Field `zone_93_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_93_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_93_name`')

        self._data["Zone 93 Name"] = value

    @property
    def zone_94_name(self):
        """Get zone_94_name

        Returns:
            str: the value of `zone_94_name` or None if not set
        """
        return self._data["Zone 94 Name"]

    @zone_94_name.setter
    def zone_94_name(self, value=None):
        """  Corresponds to IDD Field `zone_94_name`

        Args:
            value (str): value for IDD Field `zone_94_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_94_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_94_name`')

        self._data["Zone 94 Name"] = value

    @property
    def zone_95_name(self):
        """Get zone_95_name

        Returns:
            str: the value of `zone_95_name` or None if not set
        """
        return self._data["Zone 95 Name"]

    @zone_95_name.setter
    def zone_95_name(self, value=None):
        """  Corresponds to IDD Field `zone_95_name`

        Args:
            value (str): value for IDD Field `zone_95_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_95_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_95_name`')

        self._data["Zone 95 Name"] = value

    @property
    def zone_96_name(self):
        """Get zone_96_name

        Returns:
            str: the value of `zone_96_name` or None if not set
        """
        return self._data["Zone 96 Name"]

    @zone_96_name.setter
    def zone_96_name(self, value=None):
        """  Corresponds to IDD Field `zone_96_name`

        Args:
            value (str): value for IDD Field `zone_96_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_96_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_96_name`')

        self._data["Zone 96 Name"] = value

    @property
    def zone_97_name(self):
        """Get zone_97_name

        Returns:
            str: the value of `zone_97_name` or None if not set
        """
        return self._data["Zone 97 Name"]

    @zone_97_name.setter
    def zone_97_name(self, value=None):
        """  Corresponds to IDD Field `zone_97_name`

        Args:
            value (str): value for IDD Field `zone_97_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_97_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_97_name`')

        self._data["Zone 97 Name"] = value

    @property
    def zone_98_name(self):
        """Get zone_98_name

        Returns:
            str: the value of `zone_98_name` or None if not set
        """
        return self._data["Zone 98 Name"]

    @zone_98_name.setter
    def zone_98_name(self, value=None):
        """  Corresponds to IDD Field `zone_98_name`

        Args:
            value (str): value for IDD Field `zone_98_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_98_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_98_name`')

        self._data["Zone 98 Name"] = value

    @property
    def zone_99_name(self):
        """Get zone_99_name

        Returns:
            str: the value of `zone_99_name` or None if not set
        """
        return self._data["Zone 99 Name"]

    @zone_99_name.setter
    def zone_99_name(self, value=None):
        """  Corresponds to IDD Field `zone_99_name`

        Args:
            value (str): value for IDD Field `zone_99_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_99_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_99_name`')

        self._data["Zone 99 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @property
    def zone_100_name(self):
        """Get zone_100_name

        Returns:
            str: the value of `zone_100_name` or None if not set
        """
        return self._data["Zone 100 Name"]

    @zone_100_name.setter
    def zone_100_name(self, value=None):
        """  Corresponds to IDD Field `zone_100_name`

        Args:
            value (str): value for IDD Field `zone_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_100_name`')

        self._data["Zone 100 Name"] = value

    @classmethod
    def _to_str(cls, value):
        """ Represents values either as string or None values as empty string

        Args:
            value: a value
        """
        if value is None:
            return ''
        else:
            return str(value)

    def __str__(self):
        out = []
        out.append(self._to_str(self.name))
        out.append(self._to_str(self.zone_1_name))
        out.append(self._to_str(self.zone_2_name))
        out.append(self._to_str(self.zone_3_name))
        out.append(self._to_str(self.zone_4_name))
        out.append(self._to_str(self.zone_5_name))
        out.append(self._to_str(self.zone_6_name))
        out.append(self._to_str(self.zone_7_name))
        out.append(self._to_str(self.zone_8_name))
        out.append(self._to_str(self.zone_9_name))
        out.append(self._to_str(self.zone_10_name))
        out.append(self._to_str(self.zone_11_name))
        out.append(self._to_str(self.zone_12_name))
        out.append(self._to_str(self.zone_13_name))
        out.append(self._to_str(self.zone_14_name))
        out.append(self._to_str(self.zone_15_name))
        out.append(self._to_str(self.zone_16_name))
        out.append(self._to_str(self.zone_17_name))
        out.append(self._to_str(self.zone_18_name))
        out.append(self._to_str(self.zone_19_name))
        out.append(self._to_str(self.zone_20_name))
        out.append(self._to_str(self.zone_21_name))
        out.append(self._to_str(self.zone_22_name))
        out.append(self._to_str(self.zone_23_name))
        out.append(self._to_str(self.zone_24_name))
        out.append(self._to_str(self.zone_25_name))
        out.append(self._to_str(self.zone_26_name))
        out.append(self._to_str(self.zone_27_name))
        out.append(self._to_str(self.zone_28_name))
        out.append(self._to_str(self.zone_29_name))
        out.append(self._to_str(self.zone_30_name))
        out.append(self._to_str(self.zone_31_name))
        out.append(self._to_str(self.zone_32_name))
        out.append(self._to_str(self.zone_33_name))
        out.append(self._to_str(self.zone_34_name))
        out.append(self._to_str(self.zone_35_name))
        out.append(self._to_str(self.zone_36_name))
        out.append(self._to_str(self.zone_37_name))
        out.append(self._to_str(self.zone_38_name))
        out.append(self._to_str(self.zone_39_name))
        out.append(self._to_str(self.zone_40_name))
        out.append(self._to_str(self.zone_41_name))
        out.append(self._to_str(self.zone_42_name))
        out.append(self._to_str(self.zone_43_name))
        out.append(self._to_str(self.zone_44_name))
        out.append(self._to_str(self.zone_45_name))
        out.append(self._to_str(self.zone_46_name))
        out.append(self._to_str(self.zone_47_name))
        out.append(self._to_str(self.zone_48_name))
        out.append(self._to_str(self.zone_49_name))
        out.append(self._to_str(self.zone_50_name))
        out.append(self._to_str(self.zone_51_name))
        out.append(self._to_str(self.zone_52_name))
        out.append(self._to_str(self.zone_53_name))
        out.append(self._to_str(self.zone_54_name))
        out.append(self._to_str(self.zone_55_name))
        out.append(self._to_str(self.zone_56_name))
        out.append(self._to_str(self.zone_57_name))
        out.append(self._to_str(self.zone_58_name))
        out.append(self._to_str(self.zone_59_name))
        out.append(self._to_str(self.zone_60_name))
        out.append(self._to_str(self.zone_61_name))
        out.append(self._to_str(self.zone_62_name))
        out.append(self._to_str(self.zone_63_name))
        out.append(self._to_str(self.zone_64_name))
        out.append(self._to_str(self.zone_65_name))
        out.append(self._to_str(self.zone_66_name))
        out.append(self._to_str(self.zone_67_name))
        out.append(self._to_str(self.zone_68_name))
        out.append(self._to_str(self.zone_69_name))
        out.append(self._to_str(self.zone_70_name))
        out.append(self._to_str(self.zone_71_name))
        out.append(self._to_str(self.zone_72_name))
        out.append(self._to_str(self.zone_73_name))
        out.append(self._to_str(self.zone_74_name))
        out.append(self._to_str(self.zone_75_name))
        out.append(self._to_str(self.zone_76_name))
        out.append(self._to_str(self.zone_77_name))
        out.append(self._to_str(self.zone_78_name))
        out.append(self._to_str(self.zone_79_name))
        out.append(self._to_str(self.zone_80_name))
        out.append(self._to_str(self.zone_81_name))
        out.append(self._to_str(self.zone_82_name))
        out.append(self._to_str(self.zone_83_name))
        out.append(self._to_str(self.zone_84_name))
        out.append(self._to_str(self.zone_85_name))
        out.append(self._to_str(self.zone_86_name))
        out.append(self._to_str(self.zone_87_name))
        out.append(self._to_str(self.zone_88_name))
        out.append(self._to_str(self.zone_89_name))
        out.append(self._to_str(self.zone_90_name))
        out.append(self._to_str(self.zone_91_name))
        out.append(self._to_str(self.zone_92_name))
        out.append(self._to_str(self.zone_93_name))
        out.append(self._to_str(self.zone_94_name))
        out.append(self._to_str(self.zone_95_name))
        out.append(self._to_str(self.zone_96_name))
        out.append(self._to_str(self.zone_97_name))
        out.append(self._to_str(self.zone_98_name))
        out.append(self._to_str(self.zone_99_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        out.append(self._to_str(self.zone_100_name))
        return ",".join(out)