from collections import OrderedDict

class NodeList(object):
    """ Corresponds to IDD object `NodeList`
        This object is used in places where lists of nodes may be
        needed, e.g. ZoneHVAC:EquipmentConnections field Zone Air Inlet Node or NodeList Name
    """
    internal_name = "NodeList"
    field_count = 141

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `NodeList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Node 1 Name"] = None
        self._data["Node 2 Name"] = None
        self._data["Node 3 Name"] = None
        self._data["Node 4 Name"] = None
        self._data["Node 5 Name"] = None
        self._data["Node 6 Name"] = None
        self._data["Node 7 Name"] = None
        self._data["Node 8 Name"] = None
        self._data["Node 9 Name"] = None
        self._data["Node 10 Name"] = None
        self._data["Node 11 Name"] = None
        self._data["Node 12 Name"] = None
        self._data["Node 13 Name"] = None
        self._data["Node 14 Name"] = None
        self._data["Node 15 Name"] = None
        self._data["Node 16 Name"] = None
        self._data["Node 17 Name"] = None
        self._data["Node 18 Name"] = None
        self._data["Node 19 Name"] = None
        self._data["Node 20 Name"] = None
        self._data["Node 21 Name"] = None
        self._data["Node 22 Name"] = None
        self._data["Node 23 Name"] = None
        self._data["Node 24 Name"] = None
        self._data["Node 25 Name"] = None
        self._data["Node 26 Name"] = None
        self._data["Node 27 Name"] = None
        self._data["Node 28 Name"] = None
        self._data["Node 29 Name"] = None
        self._data["Node 30 Name"] = None
        self._data["Node 31 Name"] = None
        self._data["Node 32 Name"] = None
        self._data["Node 33 Name"] = None
        self._data["Node 34 Name"] = None
        self._data["Node 35 Name"] = None
        self._data["Node 36 Name"] = None
        self._data["Node 37 Name"] = None
        self._data["Node 38 Name"] = None
        self._data["Node 39 Name"] = None
        self._data["Node 40 Name"] = None
        self._data["Node 41 Name"] = None
        self._data["Node 42 Name"] = None
        self._data["Node 43 Name"] = None
        self._data["Node 44 Name"] = None
        self._data["Node 45 Name"] = None
        self._data["Node 46 Name"] = None
        self._data["Node 47 Name"] = None
        self._data["Node 48 Name"] = None
        self._data["Node 49 Name"] = None
        self._data["Node 50 Name"] = None
        self._data["Node 51 Name"] = None
        self._data["Node 52 Name"] = None
        self._data["Node 53 Name"] = None
        self._data["Node 54 Name"] = None
        self._data["Node 55 Name"] = None
        self._data["Node 56 Name"] = None
        self._data["Node 57 Name"] = None
        self._data["Node 58 Name"] = None
        self._data["Node 59 Name"] = None
        self._data["Node 60 Name"] = None
        self._data["Node 61 Name"] = None
        self._data["Node 62 Name"] = None
        self._data["Node 63 Name"] = None
        self._data["Node 64 Name"] = None
        self._data["Node 65 Name"] = None
        self._data["Node 66 Name"] = None
        self._data["Node 67 Name"] = None
        self._data["Node 68 Name"] = None
        self._data["Node 69 Name"] = None
        self._data["Node 70 Name"] = None
        self._data["Node 71 Name"] = None
        self._data["Node 72 Name"] = None
        self._data["Node 73 Name"] = None
        self._data["Node 74 Name"] = None
        self._data["Node 75 Name"] = None
        self._data["Node 76 Name"] = None
        self._data["Node 77 Name"] = None
        self._data["Node 78 Name"] = None
        self._data["Node 79 Name"] = None
        self._data["Node 80 Name"] = None
        self._data["Node 81 Name"] = None
        self._data["Node 82 Name"] = None
        self._data["Node 83 Name"] = None
        self._data["Node 84 Name"] = None
        self._data["Node 85 Name"] = None
        self._data["Node 86 Name"] = None
        self._data["Node 87 Name"] = None
        self._data["Node 88 Name"] = None
        self._data["Node 89 Name"] = None
        self._data["Node 90 Name"] = None
        self._data["Node 91 Name"] = None
        self._data["Node 92 Name"] = None
        self._data["Node 93 Name"] = None
        self._data["Node 94 Name"] = None
        self._data["Node 95 Name"] = None
        self._data["Node 96 Name"] = None
        self._data["Node 97 Name"] = None
        self._data["Node 98 Name"] = None
        self._data["Node 99 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None
        self._data["Node 100 Name"] = None

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
            self.node_1_name = None
        else:
            self.node_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_2_name = None
        else:
            self.node_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_3_name = None
        else:
            self.node_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_4_name = None
        else:
            self.node_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_5_name = None
        else:
            self.node_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_6_name = None
        else:
            self.node_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_7_name = None
        else:
            self.node_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_8_name = None
        else:
            self.node_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_9_name = None
        else:
            self.node_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_10_name = None
        else:
            self.node_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_11_name = None
        else:
            self.node_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_12_name = None
        else:
            self.node_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_13_name = None
        else:
            self.node_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_14_name = None
        else:
            self.node_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_15_name = None
        else:
            self.node_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_16_name = None
        else:
            self.node_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_17_name = None
        else:
            self.node_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_18_name = None
        else:
            self.node_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_19_name = None
        else:
            self.node_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_20_name = None
        else:
            self.node_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_21_name = None
        else:
            self.node_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_22_name = None
        else:
            self.node_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_23_name = None
        else:
            self.node_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_24_name = None
        else:
            self.node_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_25_name = None
        else:
            self.node_25_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_26_name = None
        else:
            self.node_26_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_27_name = None
        else:
            self.node_27_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_28_name = None
        else:
            self.node_28_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_29_name = None
        else:
            self.node_29_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_30_name = None
        else:
            self.node_30_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_31_name = None
        else:
            self.node_31_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_32_name = None
        else:
            self.node_32_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_33_name = None
        else:
            self.node_33_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_34_name = None
        else:
            self.node_34_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_35_name = None
        else:
            self.node_35_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_36_name = None
        else:
            self.node_36_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_37_name = None
        else:
            self.node_37_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_38_name = None
        else:
            self.node_38_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_39_name = None
        else:
            self.node_39_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_40_name = None
        else:
            self.node_40_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_41_name = None
        else:
            self.node_41_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_42_name = None
        else:
            self.node_42_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_43_name = None
        else:
            self.node_43_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_44_name = None
        else:
            self.node_44_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_45_name = None
        else:
            self.node_45_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_46_name = None
        else:
            self.node_46_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_47_name = None
        else:
            self.node_47_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_48_name = None
        else:
            self.node_48_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_49_name = None
        else:
            self.node_49_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_50_name = None
        else:
            self.node_50_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_51_name = None
        else:
            self.node_51_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_52_name = None
        else:
            self.node_52_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_53_name = None
        else:
            self.node_53_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_54_name = None
        else:
            self.node_54_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_55_name = None
        else:
            self.node_55_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_56_name = None
        else:
            self.node_56_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_57_name = None
        else:
            self.node_57_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_58_name = None
        else:
            self.node_58_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_59_name = None
        else:
            self.node_59_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_60_name = None
        else:
            self.node_60_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_61_name = None
        else:
            self.node_61_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_62_name = None
        else:
            self.node_62_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_63_name = None
        else:
            self.node_63_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_64_name = None
        else:
            self.node_64_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_65_name = None
        else:
            self.node_65_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_66_name = None
        else:
            self.node_66_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_67_name = None
        else:
            self.node_67_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_68_name = None
        else:
            self.node_68_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_69_name = None
        else:
            self.node_69_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_70_name = None
        else:
            self.node_70_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_71_name = None
        else:
            self.node_71_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_72_name = None
        else:
            self.node_72_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_73_name = None
        else:
            self.node_73_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_74_name = None
        else:
            self.node_74_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_75_name = None
        else:
            self.node_75_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_76_name = None
        else:
            self.node_76_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_77_name = None
        else:
            self.node_77_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_78_name = None
        else:
            self.node_78_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_79_name = None
        else:
            self.node_79_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_80_name = None
        else:
            self.node_80_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_81_name = None
        else:
            self.node_81_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_82_name = None
        else:
            self.node_82_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_83_name = None
        else:
            self.node_83_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_84_name = None
        else:
            self.node_84_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_85_name = None
        else:
            self.node_85_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_86_name = None
        else:
            self.node_86_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_87_name = None
        else:
            self.node_87_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_88_name = None
        else:
            self.node_88_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_89_name = None
        else:
            self.node_89_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_90_name = None
        else:
            self.node_90_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_91_name = None
        else:
            self.node_91_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_92_name = None
        else:
            self.node_92_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_93_name = None
        else:
            self.node_93_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_94_name = None
        else:
            self.node_94_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_95_name = None
        else:
            self.node_95_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_96_name = None
        else:
            self.node_96_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_97_name = None
        else:
            self.node_97_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_98_name = None
        else:
            self.node_98_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_99_name = None
        else:
            self.node_99_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.node_100_name = None
        else:
            self.node_100_name = vals[i]
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
    def node_1_name(self):
        """Get node_1_name

        Returns:
            str: the value of `node_1_name` or None if not set
        """
        return self._data["Node 1 Name"]

    @node_1_name.setter
    def node_1_name(self, value=None):
        """  Corresponds to IDD Field `node_1_name`

        Args:
            value (str): value for IDD Field `node_1_name`
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
                                 'for field `node_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_1_name`')

        self._data["Node 1 Name"] = value

    @property
    def node_2_name(self):
        """Get node_2_name

        Returns:
            str: the value of `node_2_name` or None if not set
        """
        return self._data["Node 2 Name"]

    @node_2_name.setter
    def node_2_name(self, value=None):
        """  Corresponds to IDD Field `node_2_name`

        Args:
            value (str): value for IDD Field `node_2_name`
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
                                 'for field `node_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_2_name`')

        self._data["Node 2 Name"] = value

    @property
    def node_3_name(self):
        """Get node_3_name

        Returns:
            str: the value of `node_3_name` or None if not set
        """
        return self._data["Node 3 Name"]

    @node_3_name.setter
    def node_3_name(self, value=None):
        """  Corresponds to IDD Field `node_3_name`

        Args:
            value (str): value for IDD Field `node_3_name`
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
                                 'for field `node_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_3_name`')

        self._data["Node 3 Name"] = value

    @property
    def node_4_name(self):
        """Get node_4_name

        Returns:
            str: the value of `node_4_name` or None if not set
        """
        return self._data["Node 4 Name"]

    @node_4_name.setter
    def node_4_name(self, value=None):
        """  Corresponds to IDD Field `node_4_name`

        Args:
            value (str): value for IDD Field `node_4_name`
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
                                 'for field `node_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_4_name`')

        self._data["Node 4 Name"] = value

    @property
    def node_5_name(self):
        """Get node_5_name

        Returns:
            str: the value of `node_5_name` or None if not set
        """
        return self._data["Node 5 Name"]

    @node_5_name.setter
    def node_5_name(self, value=None):
        """  Corresponds to IDD Field `node_5_name`

        Args:
            value (str): value for IDD Field `node_5_name`
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
                                 'for field `node_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_5_name`')

        self._data["Node 5 Name"] = value

    @property
    def node_6_name(self):
        """Get node_6_name

        Returns:
            str: the value of `node_6_name` or None if not set
        """
        return self._data["Node 6 Name"]

    @node_6_name.setter
    def node_6_name(self, value=None):
        """  Corresponds to IDD Field `node_6_name`

        Args:
            value (str): value for IDD Field `node_6_name`
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
                                 'for field `node_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_6_name`')

        self._data["Node 6 Name"] = value

    @property
    def node_7_name(self):
        """Get node_7_name

        Returns:
            str: the value of `node_7_name` or None if not set
        """
        return self._data["Node 7 Name"]

    @node_7_name.setter
    def node_7_name(self, value=None):
        """  Corresponds to IDD Field `node_7_name`

        Args:
            value (str): value for IDD Field `node_7_name`
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
                                 'for field `node_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_7_name`')

        self._data["Node 7 Name"] = value

    @property
    def node_8_name(self):
        """Get node_8_name

        Returns:
            str: the value of `node_8_name` or None if not set
        """
        return self._data["Node 8 Name"]

    @node_8_name.setter
    def node_8_name(self, value=None):
        """  Corresponds to IDD Field `node_8_name`

        Args:
            value (str): value for IDD Field `node_8_name`
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
                                 'for field `node_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_8_name`')

        self._data["Node 8 Name"] = value

    @property
    def node_9_name(self):
        """Get node_9_name

        Returns:
            str: the value of `node_9_name` or None if not set
        """
        return self._data["Node 9 Name"]

    @node_9_name.setter
    def node_9_name(self, value=None):
        """  Corresponds to IDD Field `node_9_name`

        Args:
            value (str): value for IDD Field `node_9_name`
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
                                 'for field `node_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_9_name`')

        self._data["Node 9 Name"] = value

    @property
    def node_10_name(self):
        """Get node_10_name

        Returns:
            str: the value of `node_10_name` or None if not set
        """
        return self._data["Node 10 Name"]

    @node_10_name.setter
    def node_10_name(self, value=None):
        """  Corresponds to IDD Field `node_10_name`

        Args:
            value (str): value for IDD Field `node_10_name`
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
                                 'for field `node_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_10_name`')

        self._data["Node 10 Name"] = value

    @property
    def node_11_name(self):
        """Get node_11_name

        Returns:
            str: the value of `node_11_name` or None if not set
        """
        return self._data["Node 11 Name"]

    @node_11_name.setter
    def node_11_name(self, value=None):
        """  Corresponds to IDD Field `node_11_name`

        Args:
            value (str): value for IDD Field `node_11_name`
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
                                 'for field `node_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_11_name`')

        self._data["Node 11 Name"] = value

    @property
    def node_12_name(self):
        """Get node_12_name

        Returns:
            str: the value of `node_12_name` or None if not set
        """
        return self._data["Node 12 Name"]

    @node_12_name.setter
    def node_12_name(self, value=None):
        """  Corresponds to IDD Field `node_12_name`

        Args:
            value (str): value for IDD Field `node_12_name`
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
                                 'for field `node_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_12_name`')

        self._data["Node 12 Name"] = value

    @property
    def node_13_name(self):
        """Get node_13_name

        Returns:
            str: the value of `node_13_name` or None if not set
        """
        return self._data["Node 13 Name"]

    @node_13_name.setter
    def node_13_name(self, value=None):
        """  Corresponds to IDD Field `node_13_name`

        Args:
            value (str): value for IDD Field `node_13_name`
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
                                 'for field `node_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_13_name`')

        self._data["Node 13 Name"] = value

    @property
    def node_14_name(self):
        """Get node_14_name

        Returns:
            str: the value of `node_14_name` or None if not set
        """
        return self._data["Node 14 Name"]

    @node_14_name.setter
    def node_14_name(self, value=None):
        """  Corresponds to IDD Field `node_14_name`

        Args:
            value (str): value for IDD Field `node_14_name`
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
                                 'for field `node_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_14_name`')

        self._data["Node 14 Name"] = value

    @property
    def node_15_name(self):
        """Get node_15_name

        Returns:
            str: the value of `node_15_name` or None if not set
        """
        return self._data["Node 15 Name"]

    @node_15_name.setter
    def node_15_name(self, value=None):
        """  Corresponds to IDD Field `node_15_name`

        Args:
            value (str): value for IDD Field `node_15_name`
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
                                 'for field `node_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_15_name`')

        self._data["Node 15 Name"] = value

    @property
    def node_16_name(self):
        """Get node_16_name

        Returns:
            str: the value of `node_16_name` or None if not set
        """
        return self._data["Node 16 Name"]

    @node_16_name.setter
    def node_16_name(self, value=None):
        """  Corresponds to IDD Field `node_16_name`

        Args:
            value (str): value for IDD Field `node_16_name`
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
                                 'for field `node_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_16_name`')

        self._data["Node 16 Name"] = value

    @property
    def node_17_name(self):
        """Get node_17_name

        Returns:
            str: the value of `node_17_name` or None if not set
        """
        return self._data["Node 17 Name"]

    @node_17_name.setter
    def node_17_name(self, value=None):
        """  Corresponds to IDD Field `node_17_name`

        Args:
            value (str): value for IDD Field `node_17_name`
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
                                 'for field `node_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_17_name`')

        self._data["Node 17 Name"] = value

    @property
    def node_18_name(self):
        """Get node_18_name

        Returns:
            str: the value of `node_18_name` or None if not set
        """
        return self._data["Node 18 Name"]

    @node_18_name.setter
    def node_18_name(self, value=None):
        """  Corresponds to IDD Field `node_18_name`

        Args:
            value (str): value for IDD Field `node_18_name`
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
                                 'for field `node_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_18_name`')

        self._data["Node 18 Name"] = value

    @property
    def node_19_name(self):
        """Get node_19_name

        Returns:
            str: the value of `node_19_name` or None if not set
        """
        return self._data["Node 19 Name"]

    @node_19_name.setter
    def node_19_name(self, value=None):
        """  Corresponds to IDD Field `node_19_name`

        Args:
            value (str): value for IDD Field `node_19_name`
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
                                 'for field `node_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_19_name`')

        self._data["Node 19 Name"] = value

    @property
    def node_20_name(self):
        """Get node_20_name

        Returns:
            str: the value of `node_20_name` or None if not set
        """
        return self._data["Node 20 Name"]

    @node_20_name.setter
    def node_20_name(self, value=None):
        """  Corresponds to IDD Field `node_20_name`

        Args:
            value (str): value for IDD Field `node_20_name`
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
                                 'for field `node_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_20_name`')

        self._data["Node 20 Name"] = value

    @property
    def node_21_name(self):
        """Get node_21_name

        Returns:
            str: the value of `node_21_name` or None if not set
        """
        return self._data["Node 21 Name"]

    @node_21_name.setter
    def node_21_name(self, value=None):
        """  Corresponds to IDD Field `node_21_name`

        Args:
            value (str): value for IDD Field `node_21_name`
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
                                 'for field `node_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_21_name`')

        self._data["Node 21 Name"] = value

    @property
    def node_22_name(self):
        """Get node_22_name

        Returns:
            str: the value of `node_22_name` or None if not set
        """
        return self._data["Node 22 Name"]

    @node_22_name.setter
    def node_22_name(self, value=None):
        """  Corresponds to IDD Field `node_22_name`

        Args:
            value (str): value for IDD Field `node_22_name`
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
                                 'for field `node_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_22_name`')

        self._data["Node 22 Name"] = value

    @property
    def node_23_name(self):
        """Get node_23_name

        Returns:
            str: the value of `node_23_name` or None if not set
        """
        return self._data["Node 23 Name"]

    @node_23_name.setter
    def node_23_name(self, value=None):
        """  Corresponds to IDD Field `node_23_name`

        Args:
            value (str): value for IDD Field `node_23_name`
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
                                 'for field `node_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_23_name`')

        self._data["Node 23 Name"] = value

    @property
    def node_24_name(self):
        """Get node_24_name

        Returns:
            str: the value of `node_24_name` or None if not set
        """
        return self._data["Node 24 Name"]

    @node_24_name.setter
    def node_24_name(self, value=None):
        """  Corresponds to IDD Field `node_24_name`

        Args:
            value (str): value for IDD Field `node_24_name`
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
                                 'for field `node_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_24_name`')

        self._data["Node 24 Name"] = value

    @property
    def node_25_name(self):
        """Get node_25_name

        Returns:
            str: the value of `node_25_name` or None if not set
        """
        return self._data["Node 25 Name"]

    @node_25_name.setter
    def node_25_name(self, value=None):
        """  Corresponds to IDD Field `node_25_name`

        Args:
            value (str): value for IDD Field `node_25_name`
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
                                 'for field `node_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_25_name`')

        self._data["Node 25 Name"] = value

    @property
    def node_26_name(self):
        """Get node_26_name

        Returns:
            str: the value of `node_26_name` or None if not set
        """
        return self._data["Node 26 Name"]

    @node_26_name.setter
    def node_26_name(self, value=None):
        """  Corresponds to IDD Field `node_26_name`

        Args:
            value (str): value for IDD Field `node_26_name`
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
                                 'for field `node_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_26_name`')

        self._data["Node 26 Name"] = value

    @property
    def node_27_name(self):
        """Get node_27_name

        Returns:
            str: the value of `node_27_name` or None if not set
        """
        return self._data["Node 27 Name"]

    @node_27_name.setter
    def node_27_name(self, value=None):
        """  Corresponds to IDD Field `node_27_name`

        Args:
            value (str): value for IDD Field `node_27_name`
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
                                 'for field `node_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_27_name`')

        self._data["Node 27 Name"] = value

    @property
    def node_28_name(self):
        """Get node_28_name

        Returns:
            str: the value of `node_28_name` or None if not set
        """
        return self._data["Node 28 Name"]

    @node_28_name.setter
    def node_28_name(self, value=None):
        """  Corresponds to IDD Field `node_28_name`

        Args:
            value (str): value for IDD Field `node_28_name`
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
                                 'for field `node_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_28_name`')

        self._data["Node 28 Name"] = value

    @property
    def node_29_name(self):
        """Get node_29_name

        Returns:
            str: the value of `node_29_name` or None if not set
        """
        return self._data["Node 29 Name"]

    @node_29_name.setter
    def node_29_name(self, value=None):
        """  Corresponds to IDD Field `node_29_name`

        Args:
            value (str): value for IDD Field `node_29_name`
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
                                 'for field `node_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_29_name`')

        self._data["Node 29 Name"] = value

    @property
    def node_30_name(self):
        """Get node_30_name

        Returns:
            str: the value of `node_30_name` or None if not set
        """
        return self._data["Node 30 Name"]

    @node_30_name.setter
    def node_30_name(self, value=None):
        """  Corresponds to IDD Field `node_30_name`

        Args:
            value (str): value for IDD Field `node_30_name`
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
                                 'for field `node_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_30_name`')

        self._data["Node 30 Name"] = value

    @property
    def node_31_name(self):
        """Get node_31_name

        Returns:
            str: the value of `node_31_name` or None if not set
        """
        return self._data["Node 31 Name"]

    @node_31_name.setter
    def node_31_name(self, value=None):
        """  Corresponds to IDD Field `node_31_name`

        Args:
            value (str): value for IDD Field `node_31_name`
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
                                 'for field `node_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_31_name`')

        self._data["Node 31 Name"] = value

    @property
    def node_32_name(self):
        """Get node_32_name

        Returns:
            str: the value of `node_32_name` or None if not set
        """
        return self._data["Node 32 Name"]

    @node_32_name.setter
    def node_32_name(self, value=None):
        """  Corresponds to IDD Field `node_32_name`

        Args:
            value (str): value for IDD Field `node_32_name`
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
                                 'for field `node_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_32_name`')

        self._data["Node 32 Name"] = value

    @property
    def node_33_name(self):
        """Get node_33_name

        Returns:
            str: the value of `node_33_name` or None if not set
        """
        return self._data["Node 33 Name"]

    @node_33_name.setter
    def node_33_name(self, value=None):
        """  Corresponds to IDD Field `node_33_name`

        Args:
            value (str): value for IDD Field `node_33_name`
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
                                 'for field `node_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_33_name`')

        self._data["Node 33 Name"] = value

    @property
    def node_34_name(self):
        """Get node_34_name

        Returns:
            str: the value of `node_34_name` or None if not set
        """
        return self._data["Node 34 Name"]

    @node_34_name.setter
    def node_34_name(self, value=None):
        """  Corresponds to IDD Field `node_34_name`

        Args:
            value (str): value for IDD Field `node_34_name`
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
                                 'for field `node_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_34_name`')

        self._data["Node 34 Name"] = value

    @property
    def node_35_name(self):
        """Get node_35_name

        Returns:
            str: the value of `node_35_name` or None if not set
        """
        return self._data["Node 35 Name"]

    @node_35_name.setter
    def node_35_name(self, value=None):
        """  Corresponds to IDD Field `node_35_name`

        Args:
            value (str): value for IDD Field `node_35_name`
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
                                 'for field `node_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_35_name`')

        self._data["Node 35 Name"] = value

    @property
    def node_36_name(self):
        """Get node_36_name

        Returns:
            str: the value of `node_36_name` or None if not set
        """
        return self._data["Node 36 Name"]

    @node_36_name.setter
    def node_36_name(self, value=None):
        """  Corresponds to IDD Field `node_36_name`

        Args:
            value (str): value for IDD Field `node_36_name`
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
                                 'for field `node_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_36_name`')

        self._data["Node 36 Name"] = value

    @property
    def node_37_name(self):
        """Get node_37_name

        Returns:
            str: the value of `node_37_name` or None if not set
        """
        return self._data["Node 37 Name"]

    @node_37_name.setter
    def node_37_name(self, value=None):
        """  Corresponds to IDD Field `node_37_name`

        Args:
            value (str): value for IDD Field `node_37_name`
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
                                 'for field `node_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_37_name`')

        self._data["Node 37 Name"] = value

    @property
    def node_38_name(self):
        """Get node_38_name

        Returns:
            str: the value of `node_38_name` or None if not set
        """
        return self._data["Node 38 Name"]

    @node_38_name.setter
    def node_38_name(self, value=None):
        """  Corresponds to IDD Field `node_38_name`

        Args:
            value (str): value for IDD Field `node_38_name`
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
                                 'for field `node_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_38_name`')

        self._data["Node 38 Name"] = value

    @property
    def node_39_name(self):
        """Get node_39_name

        Returns:
            str: the value of `node_39_name` or None if not set
        """
        return self._data["Node 39 Name"]

    @node_39_name.setter
    def node_39_name(self, value=None):
        """  Corresponds to IDD Field `node_39_name`

        Args:
            value (str): value for IDD Field `node_39_name`
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
                                 'for field `node_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_39_name`')

        self._data["Node 39 Name"] = value

    @property
    def node_40_name(self):
        """Get node_40_name

        Returns:
            str: the value of `node_40_name` or None if not set
        """
        return self._data["Node 40 Name"]

    @node_40_name.setter
    def node_40_name(self, value=None):
        """  Corresponds to IDD Field `node_40_name`

        Args:
            value (str): value for IDD Field `node_40_name`
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
                                 'for field `node_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_40_name`')

        self._data["Node 40 Name"] = value

    @property
    def node_41_name(self):
        """Get node_41_name

        Returns:
            str: the value of `node_41_name` or None if not set
        """
        return self._data["Node 41 Name"]

    @node_41_name.setter
    def node_41_name(self, value=None):
        """  Corresponds to IDD Field `node_41_name`

        Args:
            value (str): value for IDD Field `node_41_name`
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
                                 'for field `node_41_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_41_name`')

        self._data["Node 41 Name"] = value

    @property
    def node_42_name(self):
        """Get node_42_name

        Returns:
            str: the value of `node_42_name` or None if not set
        """
        return self._data["Node 42 Name"]

    @node_42_name.setter
    def node_42_name(self, value=None):
        """  Corresponds to IDD Field `node_42_name`

        Args:
            value (str): value for IDD Field `node_42_name`
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
                                 'for field `node_42_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_42_name`')

        self._data["Node 42 Name"] = value

    @property
    def node_43_name(self):
        """Get node_43_name

        Returns:
            str: the value of `node_43_name` or None if not set
        """
        return self._data["Node 43 Name"]

    @node_43_name.setter
    def node_43_name(self, value=None):
        """  Corresponds to IDD Field `node_43_name`

        Args:
            value (str): value for IDD Field `node_43_name`
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
                                 'for field `node_43_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_43_name`')

        self._data["Node 43 Name"] = value

    @property
    def node_44_name(self):
        """Get node_44_name

        Returns:
            str: the value of `node_44_name` or None if not set
        """
        return self._data["Node 44 Name"]

    @node_44_name.setter
    def node_44_name(self, value=None):
        """  Corresponds to IDD Field `node_44_name`

        Args:
            value (str): value for IDD Field `node_44_name`
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
                                 'for field `node_44_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_44_name`')

        self._data["Node 44 Name"] = value

    @property
    def node_45_name(self):
        """Get node_45_name

        Returns:
            str: the value of `node_45_name` or None if not set
        """
        return self._data["Node 45 Name"]

    @node_45_name.setter
    def node_45_name(self, value=None):
        """  Corresponds to IDD Field `node_45_name`

        Args:
            value (str): value for IDD Field `node_45_name`
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
                                 'for field `node_45_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_45_name`')

        self._data["Node 45 Name"] = value

    @property
    def node_46_name(self):
        """Get node_46_name

        Returns:
            str: the value of `node_46_name` or None if not set
        """
        return self._data["Node 46 Name"]

    @node_46_name.setter
    def node_46_name(self, value=None):
        """  Corresponds to IDD Field `node_46_name`

        Args:
            value (str): value for IDD Field `node_46_name`
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
                                 'for field `node_46_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_46_name`')

        self._data["Node 46 Name"] = value

    @property
    def node_47_name(self):
        """Get node_47_name

        Returns:
            str: the value of `node_47_name` or None if not set
        """
        return self._data["Node 47 Name"]

    @node_47_name.setter
    def node_47_name(self, value=None):
        """  Corresponds to IDD Field `node_47_name`

        Args:
            value (str): value for IDD Field `node_47_name`
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
                                 'for field `node_47_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_47_name`')

        self._data["Node 47 Name"] = value

    @property
    def node_48_name(self):
        """Get node_48_name

        Returns:
            str: the value of `node_48_name` or None if not set
        """
        return self._data["Node 48 Name"]

    @node_48_name.setter
    def node_48_name(self, value=None):
        """  Corresponds to IDD Field `node_48_name`

        Args:
            value (str): value for IDD Field `node_48_name`
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
                                 'for field `node_48_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_48_name`')

        self._data["Node 48 Name"] = value

    @property
    def node_49_name(self):
        """Get node_49_name

        Returns:
            str: the value of `node_49_name` or None if not set
        """
        return self._data["Node 49 Name"]

    @node_49_name.setter
    def node_49_name(self, value=None):
        """  Corresponds to IDD Field `node_49_name`

        Args:
            value (str): value for IDD Field `node_49_name`
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
                                 'for field `node_49_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_49_name`')

        self._data["Node 49 Name"] = value

    @property
    def node_50_name(self):
        """Get node_50_name

        Returns:
            str: the value of `node_50_name` or None if not set
        """
        return self._data["Node 50 Name"]

    @node_50_name.setter
    def node_50_name(self, value=None):
        """  Corresponds to IDD Field `node_50_name`

        Args:
            value (str): value for IDD Field `node_50_name`
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
                                 'for field `node_50_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_50_name`')

        self._data["Node 50 Name"] = value

    @property
    def node_51_name(self):
        """Get node_51_name

        Returns:
            str: the value of `node_51_name` or None if not set
        """
        return self._data["Node 51 Name"]

    @node_51_name.setter
    def node_51_name(self, value=None):
        """  Corresponds to IDD Field `node_51_name`

        Args:
            value (str): value for IDD Field `node_51_name`
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
                                 'for field `node_51_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_51_name`')

        self._data["Node 51 Name"] = value

    @property
    def node_52_name(self):
        """Get node_52_name

        Returns:
            str: the value of `node_52_name` or None if not set
        """
        return self._data["Node 52 Name"]

    @node_52_name.setter
    def node_52_name(self, value=None):
        """  Corresponds to IDD Field `node_52_name`

        Args:
            value (str): value for IDD Field `node_52_name`
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
                                 'for field `node_52_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_52_name`')

        self._data["Node 52 Name"] = value

    @property
    def node_53_name(self):
        """Get node_53_name

        Returns:
            str: the value of `node_53_name` or None if not set
        """
        return self._data["Node 53 Name"]

    @node_53_name.setter
    def node_53_name(self, value=None):
        """  Corresponds to IDD Field `node_53_name`

        Args:
            value (str): value for IDD Field `node_53_name`
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
                                 'for field `node_53_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_53_name`')

        self._data["Node 53 Name"] = value

    @property
    def node_54_name(self):
        """Get node_54_name

        Returns:
            str: the value of `node_54_name` or None if not set
        """
        return self._data["Node 54 Name"]

    @node_54_name.setter
    def node_54_name(self, value=None):
        """  Corresponds to IDD Field `node_54_name`

        Args:
            value (str): value for IDD Field `node_54_name`
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
                                 'for field `node_54_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_54_name`')

        self._data["Node 54 Name"] = value

    @property
    def node_55_name(self):
        """Get node_55_name

        Returns:
            str: the value of `node_55_name` or None if not set
        """
        return self._data["Node 55 Name"]

    @node_55_name.setter
    def node_55_name(self, value=None):
        """  Corresponds to IDD Field `node_55_name`

        Args:
            value (str): value for IDD Field `node_55_name`
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
                                 'for field `node_55_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_55_name`')

        self._data["Node 55 Name"] = value

    @property
    def node_56_name(self):
        """Get node_56_name

        Returns:
            str: the value of `node_56_name` or None if not set
        """
        return self._data["Node 56 Name"]

    @node_56_name.setter
    def node_56_name(self, value=None):
        """  Corresponds to IDD Field `node_56_name`

        Args:
            value (str): value for IDD Field `node_56_name`
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
                                 'for field `node_56_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_56_name`')

        self._data["Node 56 Name"] = value

    @property
    def node_57_name(self):
        """Get node_57_name

        Returns:
            str: the value of `node_57_name` or None if not set
        """
        return self._data["Node 57 Name"]

    @node_57_name.setter
    def node_57_name(self, value=None):
        """  Corresponds to IDD Field `node_57_name`

        Args:
            value (str): value for IDD Field `node_57_name`
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
                                 'for field `node_57_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_57_name`')

        self._data["Node 57 Name"] = value

    @property
    def node_58_name(self):
        """Get node_58_name

        Returns:
            str: the value of `node_58_name` or None if not set
        """
        return self._data["Node 58 Name"]

    @node_58_name.setter
    def node_58_name(self, value=None):
        """  Corresponds to IDD Field `node_58_name`

        Args:
            value (str): value for IDD Field `node_58_name`
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
                                 'for field `node_58_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_58_name`')

        self._data["Node 58 Name"] = value

    @property
    def node_59_name(self):
        """Get node_59_name

        Returns:
            str: the value of `node_59_name` or None if not set
        """
        return self._data["Node 59 Name"]

    @node_59_name.setter
    def node_59_name(self, value=None):
        """  Corresponds to IDD Field `node_59_name`

        Args:
            value (str): value for IDD Field `node_59_name`
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
                                 'for field `node_59_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_59_name`')

        self._data["Node 59 Name"] = value

    @property
    def node_60_name(self):
        """Get node_60_name

        Returns:
            str: the value of `node_60_name` or None if not set
        """
        return self._data["Node 60 Name"]

    @node_60_name.setter
    def node_60_name(self, value=None):
        """  Corresponds to IDD Field `node_60_name`

        Args:
            value (str): value for IDD Field `node_60_name`
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
                                 'for field `node_60_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_60_name`')

        self._data["Node 60 Name"] = value

    @property
    def node_61_name(self):
        """Get node_61_name

        Returns:
            str: the value of `node_61_name` or None if not set
        """
        return self._data["Node 61 Name"]

    @node_61_name.setter
    def node_61_name(self, value=None):
        """  Corresponds to IDD Field `node_61_name`

        Args:
            value (str): value for IDD Field `node_61_name`
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
                                 'for field `node_61_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_61_name`')

        self._data["Node 61 Name"] = value

    @property
    def node_62_name(self):
        """Get node_62_name

        Returns:
            str: the value of `node_62_name` or None if not set
        """
        return self._data["Node 62 Name"]

    @node_62_name.setter
    def node_62_name(self, value=None):
        """  Corresponds to IDD Field `node_62_name`

        Args:
            value (str): value for IDD Field `node_62_name`
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
                                 'for field `node_62_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_62_name`')

        self._data["Node 62 Name"] = value

    @property
    def node_63_name(self):
        """Get node_63_name

        Returns:
            str: the value of `node_63_name` or None if not set
        """
        return self._data["Node 63 Name"]

    @node_63_name.setter
    def node_63_name(self, value=None):
        """  Corresponds to IDD Field `node_63_name`

        Args:
            value (str): value for IDD Field `node_63_name`
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
                                 'for field `node_63_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_63_name`')

        self._data["Node 63 Name"] = value

    @property
    def node_64_name(self):
        """Get node_64_name

        Returns:
            str: the value of `node_64_name` or None if not set
        """
        return self._data["Node 64 Name"]

    @node_64_name.setter
    def node_64_name(self, value=None):
        """  Corresponds to IDD Field `node_64_name`

        Args:
            value (str): value for IDD Field `node_64_name`
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
                                 'for field `node_64_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_64_name`')

        self._data["Node 64 Name"] = value

    @property
    def node_65_name(self):
        """Get node_65_name

        Returns:
            str: the value of `node_65_name` or None if not set
        """
        return self._data["Node 65 Name"]

    @node_65_name.setter
    def node_65_name(self, value=None):
        """  Corresponds to IDD Field `node_65_name`

        Args:
            value (str): value for IDD Field `node_65_name`
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
                                 'for field `node_65_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_65_name`')

        self._data["Node 65 Name"] = value

    @property
    def node_66_name(self):
        """Get node_66_name

        Returns:
            str: the value of `node_66_name` or None if not set
        """
        return self._data["Node 66 Name"]

    @node_66_name.setter
    def node_66_name(self, value=None):
        """  Corresponds to IDD Field `node_66_name`

        Args:
            value (str): value for IDD Field `node_66_name`
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
                                 'for field `node_66_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_66_name`')

        self._data["Node 66 Name"] = value

    @property
    def node_67_name(self):
        """Get node_67_name

        Returns:
            str: the value of `node_67_name` or None if not set
        """
        return self._data["Node 67 Name"]

    @node_67_name.setter
    def node_67_name(self, value=None):
        """  Corresponds to IDD Field `node_67_name`

        Args:
            value (str): value for IDD Field `node_67_name`
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
                                 'for field `node_67_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_67_name`')

        self._data["Node 67 Name"] = value

    @property
    def node_68_name(self):
        """Get node_68_name

        Returns:
            str: the value of `node_68_name` or None if not set
        """
        return self._data["Node 68 Name"]

    @node_68_name.setter
    def node_68_name(self, value=None):
        """  Corresponds to IDD Field `node_68_name`

        Args:
            value (str): value for IDD Field `node_68_name`
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
                                 'for field `node_68_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_68_name`')

        self._data["Node 68 Name"] = value

    @property
    def node_69_name(self):
        """Get node_69_name

        Returns:
            str: the value of `node_69_name` or None if not set
        """
        return self._data["Node 69 Name"]

    @node_69_name.setter
    def node_69_name(self, value=None):
        """  Corresponds to IDD Field `node_69_name`

        Args:
            value (str): value for IDD Field `node_69_name`
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
                                 'for field `node_69_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_69_name`')

        self._data["Node 69 Name"] = value

    @property
    def node_70_name(self):
        """Get node_70_name

        Returns:
            str: the value of `node_70_name` or None if not set
        """
        return self._data["Node 70 Name"]

    @node_70_name.setter
    def node_70_name(self, value=None):
        """  Corresponds to IDD Field `node_70_name`

        Args:
            value (str): value for IDD Field `node_70_name`
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
                                 'for field `node_70_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_70_name`')

        self._data["Node 70 Name"] = value

    @property
    def node_71_name(self):
        """Get node_71_name

        Returns:
            str: the value of `node_71_name` or None if not set
        """
        return self._data["Node 71 Name"]

    @node_71_name.setter
    def node_71_name(self, value=None):
        """  Corresponds to IDD Field `node_71_name`

        Args:
            value (str): value for IDD Field `node_71_name`
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
                                 'for field `node_71_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_71_name`')

        self._data["Node 71 Name"] = value

    @property
    def node_72_name(self):
        """Get node_72_name

        Returns:
            str: the value of `node_72_name` or None if not set
        """
        return self._data["Node 72 Name"]

    @node_72_name.setter
    def node_72_name(self, value=None):
        """  Corresponds to IDD Field `node_72_name`

        Args:
            value (str): value for IDD Field `node_72_name`
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
                                 'for field `node_72_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_72_name`')

        self._data["Node 72 Name"] = value

    @property
    def node_73_name(self):
        """Get node_73_name

        Returns:
            str: the value of `node_73_name` or None if not set
        """
        return self._data["Node 73 Name"]

    @node_73_name.setter
    def node_73_name(self, value=None):
        """  Corresponds to IDD Field `node_73_name`

        Args:
            value (str): value for IDD Field `node_73_name`
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
                                 'for field `node_73_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_73_name`')

        self._data["Node 73 Name"] = value

    @property
    def node_74_name(self):
        """Get node_74_name

        Returns:
            str: the value of `node_74_name` or None if not set
        """
        return self._data["Node 74 Name"]

    @node_74_name.setter
    def node_74_name(self, value=None):
        """  Corresponds to IDD Field `node_74_name`

        Args:
            value (str): value for IDD Field `node_74_name`
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
                                 'for field `node_74_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_74_name`')

        self._data["Node 74 Name"] = value

    @property
    def node_75_name(self):
        """Get node_75_name

        Returns:
            str: the value of `node_75_name` or None if not set
        """
        return self._data["Node 75 Name"]

    @node_75_name.setter
    def node_75_name(self, value=None):
        """  Corresponds to IDD Field `node_75_name`

        Args:
            value (str): value for IDD Field `node_75_name`
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
                                 'for field `node_75_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_75_name`')

        self._data["Node 75 Name"] = value

    @property
    def node_76_name(self):
        """Get node_76_name

        Returns:
            str: the value of `node_76_name` or None if not set
        """
        return self._data["Node 76 Name"]

    @node_76_name.setter
    def node_76_name(self, value=None):
        """  Corresponds to IDD Field `node_76_name`

        Args:
            value (str): value for IDD Field `node_76_name`
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
                                 'for field `node_76_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_76_name`')

        self._data["Node 76 Name"] = value

    @property
    def node_77_name(self):
        """Get node_77_name

        Returns:
            str: the value of `node_77_name` or None if not set
        """
        return self._data["Node 77 Name"]

    @node_77_name.setter
    def node_77_name(self, value=None):
        """  Corresponds to IDD Field `node_77_name`

        Args:
            value (str): value for IDD Field `node_77_name`
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
                                 'for field `node_77_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_77_name`')

        self._data["Node 77 Name"] = value

    @property
    def node_78_name(self):
        """Get node_78_name

        Returns:
            str: the value of `node_78_name` or None if not set
        """
        return self._data["Node 78 Name"]

    @node_78_name.setter
    def node_78_name(self, value=None):
        """  Corresponds to IDD Field `node_78_name`

        Args:
            value (str): value for IDD Field `node_78_name`
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
                                 'for field `node_78_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_78_name`')

        self._data["Node 78 Name"] = value

    @property
    def node_79_name(self):
        """Get node_79_name

        Returns:
            str: the value of `node_79_name` or None if not set
        """
        return self._data["Node 79 Name"]

    @node_79_name.setter
    def node_79_name(self, value=None):
        """  Corresponds to IDD Field `node_79_name`

        Args:
            value (str): value for IDD Field `node_79_name`
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
                                 'for field `node_79_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_79_name`')

        self._data["Node 79 Name"] = value

    @property
    def node_80_name(self):
        """Get node_80_name

        Returns:
            str: the value of `node_80_name` or None if not set
        """
        return self._data["Node 80 Name"]

    @node_80_name.setter
    def node_80_name(self, value=None):
        """  Corresponds to IDD Field `node_80_name`

        Args:
            value (str): value for IDD Field `node_80_name`
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
                                 'for field `node_80_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_80_name`')

        self._data["Node 80 Name"] = value

    @property
    def node_81_name(self):
        """Get node_81_name

        Returns:
            str: the value of `node_81_name` or None if not set
        """
        return self._data["Node 81 Name"]

    @node_81_name.setter
    def node_81_name(self, value=None):
        """  Corresponds to IDD Field `node_81_name`

        Args:
            value (str): value for IDD Field `node_81_name`
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
                                 'for field `node_81_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_81_name`')

        self._data["Node 81 Name"] = value

    @property
    def node_82_name(self):
        """Get node_82_name

        Returns:
            str: the value of `node_82_name` or None if not set
        """
        return self._data["Node 82 Name"]

    @node_82_name.setter
    def node_82_name(self, value=None):
        """  Corresponds to IDD Field `node_82_name`

        Args:
            value (str): value for IDD Field `node_82_name`
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
                                 'for field `node_82_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_82_name`')

        self._data["Node 82 Name"] = value

    @property
    def node_83_name(self):
        """Get node_83_name

        Returns:
            str: the value of `node_83_name` or None if not set
        """
        return self._data["Node 83 Name"]

    @node_83_name.setter
    def node_83_name(self, value=None):
        """  Corresponds to IDD Field `node_83_name`

        Args:
            value (str): value for IDD Field `node_83_name`
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
                                 'for field `node_83_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_83_name`')

        self._data["Node 83 Name"] = value

    @property
    def node_84_name(self):
        """Get node_84_name

        Returns:
            str: the value of `node_84_name` or None if not set
        """
        return self._data["Node 84 Name"]

    @node_84_name.setter
    def node_84_name(self, value=None):
        """  Corresponds to IDD Field `node_84_name`

        Args:
            value (str): value for IDD Field `node_84_name`
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
                                 'for field `node_84_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_84_name`')

        self._data["Node 84 Name"] = value

    @property
    def node_85_name(self):
        """Get node_85_name

        Returns:
            str: the value of `node_85_name` or None if not set
        """
        return self._data["Node 85 Name"]

    @node_85_name.setter
    def node_85_name(self, value=None):
        """  Corresponds to IDD Field `node_85_name`

        Args:
            value (str): value for IDD Field `node_85_name`
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
                                 'for field `node_85_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_85_name`')

        self._data["Node 85 Name"] = value

    @property
    def node_86_name(self):
        """Get node_86_name

        Returns:
            str: the value of `node_86_name` or None if not set
        """
        return self._data["Node 86 Name"]

    @node_86_name.setter
    def node_86_name(self, value=None):
        """  Corresponds to IDD Field `node_86_name`

        Args:
            value (str): value for IDD Field `node_86_name`
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
                                 'for field `node_86_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_86_name`')

        self._data["Node 86 Name"] = value

    @property
    def node_87_name(self):
        """Get node_87_name

        Returns:
            str: the value of `node_87_name` or None if not set
        """
        return self._data["Node 87 Name"]

    @node_87_name.setter
    def node_87_name(self, value=None):
        """  Corresponds to IDD Field `node_87_name`

        Args:
            value (str): value for IDD Field `node_87_name`
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
                                 'for field `node_87_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_87_name`')

        self._data["Node 87 Name"] = value

    @property
    def node_88_name(self):
        """Get node_88_name

        Returns:
            str: the value of `node_88_name` or None if not set
        """
        return self._data["Node 88 Name"]

    @node_88_name.setter
    def node_88_name(self, value=None):
        """  Corresponds to IDD Field `node_88_name`

        Args:
            value (str): value for IDD Field `node_88_name`
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
                                 'for field `node_88_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_88_name`')

        self._data["Node 88 Name"] = value

    @property
    def node_89_name(self):
        """Get node_89_name

        Returns:
            str: the value of `node_89_name` or None if not set
        """
        return self._data["Node 89 Name"]

    @node_89_name.setter
    def node_89_name(self, value=None):
        """  Corresponds to IDD Field `node_89_name`

        Args:
            value (str): value for IDD Field `node_89_name`
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
                                 'for field `node_89_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_89_name`')

        self._data["Node 89 Name"] = value

    @property
    def node_90_name(self):
        """Get node_90_name

        Returns:
            str: the value of `node_90_name` or None if not set
        """
        return self._data["Node 90 Name"]

    @node_90_name.setter
    def node_90_name(self, value=None):
        """  Corresponds to IDD Field `node_90_name`

        Args:
            value (str): value for IDD Field `node_90_name`
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
                                 'for field `node_90_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_90_name`')

        self._data["Node 90 Name"] = value

    @property
    def node_91_name(self):
        """Get node_91_name

        Returns:
            str: the value of `node_91_name` or None if not set
        """
        return self._data["Node 91 Name"]

    @node_91_name.setter
    def node_91_name(self, value=None):
        """  Corresponds to IDD Field `node_91_name`

        Args:
            value (str): value for IDD Field `node_91_name`
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
                                 'for field `node_91_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_91_name`')

        self._data["Node 91 Name"] = value

    @property
    def node_92_name(self):
        """Get node_92_name

        Returns:
            str: the value of `node_92_name` or None if not set
        """
        return self._data["Node 92 Name"]

    @node_92_name.setter
    def node_92_name(self, value=None):
        """  Corresponds to IDD Field `node_92_name`

        Args:
            value (str): value for IDD Field `node_92_name`
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
                                 'for field `node_92_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_92_name`')

        self._data["Node 92 Name"] = value

    @property
    def node_93_name(self):
        """Get node_93_name

        Returns:
            str: the value of `node_93_name` or None if not set
        """
        return self._data["Node 93 Name"]

    @node_93_name.setter
    def node_93_name(self, value=None):
        """  Corresponds to IDD Field `node_93_name`

        Args:
            value (str): value for IDD Field `node_93_name`
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
                                 'for field `node_93_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_93_name`')

        self._data["Node 93 Name"] = value

    @property
    def node_94_name(self):
        """Get node_94_name

        Returns:
            str: the value of `node_94_name` or None if not set
        """
        return self._data["Node 94 Name"]

    @node_94_name.setter
    def node_94_name(self, value=None):
        """  Corresponds to IDD Field `node_94_name`

        Args:
            value (str): value for IDD Field `node_94_name`
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
                                 'for field `node_94_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_94_name`')

        self._data["Node 94 Name"] = value

    @property
    def node_95_name(self):
        """Get node_95_name

        Returns:
            str: the value of `node_95_name` or None if not set
        """
        return self._data["Node 95 Name"]

    @node_95_name.setter
    def node_95_name(self, value=None):
        """  Corresponds to IDD Field `node_95_name`

        Args:
            value (str): value for IDD Field `node_95_name`
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
                                 'for field `node_95_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_95_name`')

        self._data["Node 95 Name"] = value

    @property
    def node_96_name(self):
        """Get node_96_name

        Returns:
            str: the value of `node_96_name` or None if not set
        """
        return self._data["Node 96 Name"]

    @node_96_name.setter
    def node_96_name(self, value=None):
        """  Corresponds to IDD Field `node_96_name`

        Args:
            value (str): value for IDD Field `node_96_name`
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
                                 'for field `node_96_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_96_name`')

        self._data["Node 96 Name"] = value

    @property
    def node_97_name(self):
        """Get node_97_name

        Returns:
            str: the value of `node_97_name` or None if not set
        """
        return self._data["Node 97 Name"]

    @node_97_name.setter
    def node_97_name(self, value=None):
        """  Corresponds to IDD Field `node_97_name`

        Args:
            value (str): value for IDD Field `node_97_name`
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
                                 'for field `node_97_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_97_name`')

        self._data["Node 97 Name"] = value

    @property
    def node_98_name(self):
        """Get node_98_name

        Returns:
            str: the value of `node_98_name` or None if not set
        """
        return self._data["Node 98 Name"]

    @node_98_name.setter
    def node_98_name(self, value=None):
        """  Corresponds to IDD Field `node_98_name`

        Args:
            value (str): value for IDD Field `node_98_name`
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
                                 'for field `node_98_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_98_name`')

        self._data["Node 98 Name"] = value

    @property
    def node_99_name(self):
        """Get node_99_name

        Returns:
            str: the value of `node_99_name` or None if not set
        """
        return self._data["Node 99 Name"]

    @node_99_name.setter
    def node_99_name(self, value=None):
        """  Corresponds to IDD Field `node_99_name`

        Args:
            value (str): value for IDD Field `node_99_name`
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
                                 'for field `node_99_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_99_name`')

        self._data["Node 99 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

    @property
    def node_100_name(self):
        """Get node_100_name

        Returns:
            str: the value of `node_100_name` or None if not set
        """
        return self._data["Node 100 Name"]

    @node_100_name.setter
    def node_100_name(self, value=None):
        """  Corresponds to IDD Field `node_100_name`

        Args:
            value (str): value for IDD Field `node_100_name`
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
                                 'for field `node_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `node_100_name`')

        self._data["Node 100 Name"] = value

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
        out.append(self._to_str(self.node_1_name))
        out.append(self._to_str(self.node_2_name))
        out.append(self._to_str(self.node_3_name))
        out.append(self._to_str(self.node_4_name))
        out.append(self._to_str(self.node_5_name))
        out.append(self._to_str(self.node_6_name))
        out.append(self._to_str(self.node_7_name))
        out.append(self._to_str(self.node_8_name))
        out.append(self._to_str(self.node_9_name))
        out.append(self._to_str(self.node_10_name))
        out.append(self._to_str(self.node_11_name))
        out.append(self._to_str(self.node_12_name))
        out.append(self._to_str(self.node_13_name))
        out.append(self._to_str(self.node_14_name))
        out.append(self._to_str(self.node_15_name))
        out.append(self._to_str(self.node_16_name))
        out.append(self._to_str(self.node_17_name))
        out.append(self._to_str(self.node_18_name))
        out.append(self._to_str(self.node_19_name))
        out.append(self._to_str(self.node_20_name))
        out.append(self._to_str(self.node_21_name))
        out.append(self._to_str(self.node_22_name))
        out.append(self._to_str(self.node_23_name))
        out.append(self._to_str(self.node_24_name))
        out.append(self._to_str(self.node_25_name))
        out.append(self._to_str(self.node_26_name))
        out.append(self._to_str(self.node_27_name))
        out.append(self._to_str(self.node_28_name))
        out.append(self._to_str(self.node_29_name))
        out.append(self._to_str(self.node_30_name))
        out.append(self._to_str(self.node_31_name))
        out.append(self._to_str(self.node_32_name))
        out.append(self._to_str(self.node_33_name))
        out.append(self._to_str(self.node_34_name))
        out.append(self._to_str(self.node_35_name))
        out.append(self._to_str(self.node_36_name))
        out.append(self._to_str(self.node_37_name))
        out.append(self._to_str(self.node_38_name))
        out.append(self._to_str(self.node_39_name))
        out.append(self._to_str(self.node_40_name))
        out.append(self._to_str(self.node_41_name))
        out.append(self._to_str(self.node_42_name))
        out.append(self._to_str(self.node_43_name))
        out.append(self._to_str(self.node_44_name))
        out.append(self._to_str(self.node_45_name))
        out.append(self._to_str(self.node_46_name))
        out.append(self._to_str(self.node_47_name))
        out.append(self._to_str(self.node_48_name))
        out.append(self._to_str(self.node_49_name))
        out.append(self._to_str(self.node_50_name))
        out.append(self._to_str(self.node_51_name))
        out.append(self._to_str(self.node_52_name))
        out.append(self._to_str(self.node_53_name))
        out.append(self._to_str(self.node_54_name))
        out.append(self._to_str(self.node_55_name))
        out.append(self._to_str(self.node_56_name))
        out.append(self._to_str(self.node_57_name))
        out.append(self._to_str(self.node_58_name))
        out.append(self._to_str(self.node_59_name))
        out.append(self._to_str(self.node_60_name))
        out.append(self._to_str(self.node_61_name))
        out.append(self._to_str(self.node_62_name))
        out.append(self._to_str(self.node_63_name))
        out.append(self._to_str(self.node_64_name))
        out.append(self._to_str(self.node_65_name))
        out.append(self._to_str(self.node_66_name))
        out.append(self._to_str(self.node_67_name))
        out.append(self._to_str(self.node_68_name))
        out.append(self._to_str(self.node_69_name))
        out.append(self._to_str(self.node_70_name))
        out.append(self._to_str(self.node_71_name))
        out.append(self._to_str(self.node_72_name))
        out.append(self._to_str(self.node_73_name))
        out.append(self._to_str(self.node_74_name))
        out.append(self._to_str(self.node_75_name))
        out.append(self._to_str(self.node_76_name))
        out.append(self._to_str(self.node_77_name))
        out.append(self._to_str(self.node_78_name))
        out.append(self._to_str(self.node_79_name))
        out.append(self._to_str(self.node_80_name))
        out.append(self._to_str(self.node_81_name))
        out.append(self._to_str(self.node_82_name))
        out.append(self._to_str(self.node_83_name))
        out.append(self._to_str(self.node_84_name))
        out.append(self._to_str(self.node_85_name))
        out.append(self._to_str(self.node_86_name))
        out.append(self._to_str(self.node_87_name))
        out.append(self._to_str(self.node_88_name))
        out.append(self._to_str(self.node_89_name))
        out.append(self._to_str(self.node_90_name))
        out.append(self._to_str(self.node_91_name))
        out.append(self._to_str(self.node_92_name))
        out.append(self._to_str(self.node_93_name))
        out.append(self._to_str(self.node_94_name))
        out.append(self._to_str(self.node_95_name))
        out.append(self._to_str(self.node_96_name))
        out.append(self._to_str(self.node_97_name))
        out.append(self._to_str(self.node_98_name))
        out.append(self._to_str(self.node_99_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        out.append(self._to_str(self.node_100_name))
        return ",".join(out)