from collections import OrderedDict

class BranchList(object):
    """ Corresponds to IDD object `BranchList`
        Branches MUST be listed in Flow order: Inlet branch, then parallel branches, then Outlet branch.
        Branches are simulated in the order listed.  Branch names cannot be duplicated within a single branch list.
    """
    internal_name = "BranchList"
    field_count = 141

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `BranchList`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Branch 1 Name"] = None
        self._data["Branch 2 Name"] = None
        self._data["Branch 3 Name"] = None
        self._data["Branch 4 Name"] = None
        self._data["Branch 5 Name"] = None
        self._data["Branch 6 Name"] = None
        self._data["Branch 7 Name"] = None
        self._data["Branch 8 Name"] = None
        self._data["Branch 9 Name"] = None
        self._data["Branch 10 Name"] = None
        self._data["Branch 11 Name"] = None
        self._data["Branch 12 Name"] = None
        self._data["Branch 13 Name"] = None
        self._data["Branch 14 Name"] = None
        self._data["Branch 15 Name"] = None
        self._data["Branch 16 Name"] = None
        self._data["Branch 17 Name"] = None
        self._data["Branch 18 Name"] = None
        self._data["Branch 19 Name"] = None
        self._data["Branch 20 Name"] = None
        self._data["Branch 21 Name"] = None
        self._data["Branch 22 Name"] = None
        self._data["Branch 23 Name"] = None
        self._data["Branch 24 Name"] = None
        self._data["Branch 25 Name"] = None
        self._data["Branch 26 Name"] = None
        self._data["Branch 27 Name"] = None
        self._data["Branch 28 Name"] = None
        self._data["Branch 29 Name"] = None
        self._data["Branch 30 Name"] = None
        self._data["Branch 31 Name"] = None
        self._data["Branch 32 Name"] = None
        self._data["Branch 33 Name"] = None
        self._data["Branch 34 Name"] = None
        self._data["Branch 35 Name"] = None
        self._data["Branch 36 Name"] = None
        self._data["Branch 37 Name"] = None
        self._data["Branch 38 Name"] = None
        self._data["Branch 39 Name"] = None
        self._data["Branch 40 Name"] = None
        self._data["Branch 41 Name"] = None
        self._data["Branch 42 Name"] = None
        self._data["Branch 43 Name"] = None
        self._data["Branch 44 Name"] = None
        self._data["Branch 45 Name"] = None
        self._data["Branch 46 Name"] = None
        self._data["Branch 47 Name"] = None
        self._data["Branch 48 Name"] = None
        self._data["Branch 49 Name"] = None
        self._data["Branch 50 Name"] = None
        self._data["Branch 51 Name"] = None
        self._data["Branch 52 Name"] = None
        self._data["Branch 53 Name"] = None
        self._data["Branch 54 Name"] = None
        self._data["Branch 55 Name"] = None
        self._data["Branch 56 Name"] = None
        self._data["Branch 57 Name"] = None
        self._data["Branch 58 Name"] = None
        self._data["Branch 59 Name"] = None
        self._data["Branch 60 Name"] = None
        self._data["Branch 61 Name"] = None
        self._data["Branch 62 Name"] = None
        self._data["Branch 63 Name"] = None
        self._data["Branch 64 Name"] = None
        self._data["Branch 65 Name"] = None
        self._data["Branch 66 Name"] = None
        self._data["Branch 67 Name"] = None
        self._data["Branch 68 Name"] = None
        self._data["Branch 69 Name"] = None
        self._data["Branch 70 Name"] = None
        self._data["Branch 71 Name"] = None
        self._data["Branch 72 Name"] = None
        self._data["Branch 73 Name"] = None
        self._data["Branch 74 Name"] = None
        self._data["Branch 75 Name"] = None
        self._data["Branch 76 Name"] = None
        self._data["Branch 77 Name"] = None
        self._data["Branch 78 Name"] = None
        self._data["Branch 79 Name"] = None
        self._data["Branch 80 Name"] = None
        self._data["Branch 81 Name"] = None
        self._data["Branch 82 Name"] = None
        self._data["Branch 83 Name"] = None
        self._data["Branch 84 Name"] = None
        self._data["Branch 85 Name"] = None
        self._data["Branch 86 Name"] = None
        self._data["Branch 87 Name"] = None
        self._data["Branch 88 Name"] = None
        self._data["Branch 89 Name"] = None
        self._data["Branch 90 Name"] = None
        self._data["Branch 91 Name"] = None
        self._data["Branch 92 Name"] = None
        self._data["Branch 93 Name"] = None
        self._data["Branch 94 Name"] = None
        self._data["Branch 95 Name"] = None
        self._data["Branch 96 Name"] = None
        self._data["Branch 97 Name"] = None
        self._data["Branch 98 Name"] = None
        self._data["Branch 99 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None
        self._data["Branch 100 Name"] = None

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
            self.branch_1_name = None
        else:
            self.branch_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_2_name = None
        else:
            self.branch_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_3_name = None
        else:
            self.branch_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_4_name = None
        else:
            self.branch_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_5_name = None
        else:
            self.branch_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_6_name = None
        else:
            self.branch_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_7_name = None
        else:
            self.branch_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_8_name = None
        else:
            self.branch_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_9_name = None
        else:
            self.branch_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_10_name = None
        else:
            self.branch_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_11_name = None
        else:
            self.branch_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_12_name = None
        else:
            self.branch_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_13_name = None
        else:
            self.branch_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_14_name = None
        else:
            self.branch_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_15_name = None
        else:
            self.branch_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_16_name = None
        else:
            self.branch_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_17_name = None
        else:
            self.branch_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_18_name = None
        else:
            self.branch_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_19_name = None
        else:
            self.branch_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_20_name = None
        else:
            self.branch_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_21_name = None
        else:
            self.branch_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_22_name = None
        else:
            self.branch_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_23_name = None
        else:
            self.branch_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_24_name = None
        else:
            self.branch_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_25_name = None
        else:
            self.branch_25_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_26_name = None
        else:
            self.branch_26_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_27_name = None
        else:
            self.branch_27_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_28_name = None
        else:
            self.branch_28_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_29_name = None
        else:
            self.branch_29_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_30_name = None
        else:
            self.branch_30_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_31_name = None
        else:
            self.branch_31_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_32_name = None
        else:
            self.branch_32_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_33_name = None
        else:
            self.branch_33_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_34_name = None
        else:
            self.branch_34_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_35_name = None
        else:
            self.branch_35_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_36_name = None
        else:
            self.branch_36_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_37_name = None
        else:
            self.branch_37_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_38_name = None
        else:
            self.branch_38_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_39_name = None
        else:
            self.branch_39_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_40_name = None
        else:
            self.branch_40_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_41_name = None
        else:
            self.branch_41_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_42_name = None
        else:
            self.branch_42_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_43_name = None
        else:
            self.branch_43_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_44_name = None
        else:
            self.branch_44_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_45_name = None
        else:
            self.branch_45_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_46_name = None
        else:
            self.branch_46_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_47_name = None
        else:
            self.branch_47_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_48_name = None
        else:
            self.branch_48_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_49_name = None
        else:
            self.branch_49_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_50_name = None
        else:
            self.branch_50_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_51_name = None
        else:
            self.branch_51_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_52_name = None
        else:
            self.branch_52_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_53_name = None
        else:
            self.branch_53_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_54_name = None
        else:
            self.branch_54_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_55_name = None
        else:
            self.branch_55_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_56_name = None
        else:
            self.branch_56_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_57_name = None
        else:
            self.branch_57_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_58_name = None
        else:
            self.branch_58_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_59_name = None
        else:
            self.branch_59_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_60_name = None
        else:
            self.branch_60_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_61_name = None
        else:
            self.branch_61_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_62_name = None
        else:
            self.branch_62_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_63_name = None
        else:
            self.branch_63_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_64_name = None
        else:
            self.branch_64_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_65_name = None
        else:
            self.branch_65_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_66_name = None
        else:
            self.branch_66_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_67_name = None
        else:
            self.branch_67_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_68_name = None
        else:
            self.branch_68_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_69_name = None
        else:
            self.branch_69_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_70_name = None
        else:
            self.branch_70_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_71_name = None
        else:
            self.branch_71_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_72_name = None
        else:
            self.branch_72_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_73_name = None
        else:
            self.branch_73_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_74_name = None
        else:
            self.branch_74_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_75_name = None
        else:
            self.branch_75_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_76_name = None
        else:
            self.branch_76_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_77_name = None
        else:
            self.branch_77_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_78_name = None
        else:
            self.branch_78_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_79_name = None
        else:
            self.branch_79_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_80_name = None
        else:
            self.branch_80_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_81_name = None
        else:
            self.branch_81_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_82_name = None
        else:
            self.branch_82_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_83_name = None
        else:
            self.branch_83_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_84_name = None
        else:
            self.branch_84_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_85_name = None
        else:
            self.branch_85_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_86_name = None
        else:
            self.branch_86_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_87_name = None
        else:
            self.branch_87_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_88_name = None
        else:
            self.branch_88_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_89_name = None
        else:
            self.branch_89_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_90_name = None
        else:
            self.branch_90_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_91_name = None
        else:
            self.branch_91_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_92_name = None
        else:
            self.branch_92_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_93_name = None
        else:
            self.branch_93_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_94_name = None
        else:
            self.branch_94_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_95_name = None
        else:
            self.branch_95_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_96_name = None
        else:
            self.branch_96_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_97_name = None
        else:
            self.branch_97_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_98_name = None
        else:
            self.branch_98_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_99_name = None
        else:
            self.branch_99_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.branch_100_name = None
        else:
            self.branch_100_name = vals[i]
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
    def branch_1_name(self):
        """Get branch_1_name

        Returns:
            str: the value of `branch_1_name` or None if not set
        """
        return self._data["Branch 1 Name"]

    @branch_1_name.setter
    def branch_1_name(self, value=None):
        """  Corresponds to IDD Field `branch_1_name`

        Args:
            value (str): value for IDD Field `branch_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_1_name`')

        self._data["Branch 1 Name"] = value

    @property
    def branch_2_name(self):
        """Get branch_2_name

        Returns:
            str: the value of `branch_2_name` or None if not set
        """
        return self._data["Branch 2 Name"]

    @branch_2_name.setter
    def branch_2_name(self, value=None):
        """  Corresponds to IDD Field `branch_2_name`

        Args:
            value (str): value for IDD Field `branch_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_2_name`')

        self._data["Branch 2 Name"] = value

    @property
    def branch_3_name(self):
        """Get branch_3_name

        Returns:
            str: the value of `branch_3_name` or None if not set
        """
        return self._data["Branch 3 Name"]

    @branch_3_name.setter
    def branch_3_name(self, value=None):
        """  Corresponds to IDD Field `branch_3_name`

        Args:
            value (str): value for IDD Field `branch_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_3_name`')

        self._data["Branch 3 Name"] = value

    @property
    def branch_4_name(self):
        """Get branch_4_name

        Returns:
            str: the value of `branch_4_name` or None if not set
        """
        return self._data["Branch 4 Name"]

    @branch_4_name.setter
    def branch_4_name(self, value=None):
        """  Corresponds to IDD Field `branch_4_name`

        Args:
            value (str): value for IDD Field `branch_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_4_name`')

        self._data["Branch 4 Name"] = value

    @property
    def branch_5_name(self):
        """Get branch_5_name

        Returns:
            str: the value of `branch_5_name` or None if not set
        """
        return self._data["Branch 5 Name"]

    @branch_5_name.setter
    def branch_5_name(self, value=None):
        """  Corresponds to IDD Field `branch_5_name`

        Args:
            value (str): value for IDD Field `branch_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_5_name`')

        self._data["Branch 5 Name"] = value

    @property
    def branch_6_name(self):
        """Get branch_6_name

        Returns:
            str: the value of `branch_6_name` or None if not set
        """
        return self._data["Branch 6 Name"]

    @branch_6_name.setter
    def branch_6_name(self, value=None):
        """  Corresponds to IDD Field `branch_6_name`

        Args:
            value (str): value for IDD Field `branch_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_6_name`')

        self._data["Branch 6 Name"] = value

    @property
    def branch_7_name(self):
        """Get branch_7_name

        Returns:
            str: the value of `branch_7_name` or None if not set
        """
        return self._data["Branch 7 Name"]

    @branch_7_name.setter
    def branch_7_name(self, value=None):
        """  Corresponds to IDD Field `branch_7_name`

        Args:
            value (str): value for IDD Field `branch_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_7_name`')

        self._data["Branch 7 Name"] = value

    @property
    def branch_8_name(self):
        """Get branch_8_name

        Returns:
            str: the value of `branch_8_name` or None if not set
        """
        return self._data["Branch 8 Name"]

    @branch_8_name.setter
    def branch_8_name(self, value=None):
        """  Corresponds to IDD Field `branch_8_name`

        Args:
            value (str): value for IDD Field `branch_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_8_name`')

        self._data["Branch 8 Name"] = value

    @property
    def branch_9_name(self):
        """Get branch_9_name

        Returns:
            str: the value of `branch_9_name` or None if not set
        """
        return self._data["Branch 9 Name"]

    @branch_9_name.setter
    def branch_9_name(self, value=None):
        """  Corresponds to IDD Field `branch_9_name`

        Args:
            value (str): value for IDD Field `branch_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_9_name`')

        self._data["Branch 9 Name"] = value

    @property
    def branch_10_name(self):
        """Get branch_10_name

        Returns:
            str: the value of `branch_10_name` or None if not set
        """
        return self._data["Branch 10 Name"]

    @branch_10_name.setter
    def branch_10_name(self, value=None):
        """  Corresponds to IDD Field `branch_10_name`

        Args:
            value (str): value for IDD Field `branch_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_10_name`')

        self._data["Branch 10 Name"] = value

    @property
    def branch_11_name(self):
        """Get branch_11_name

        Returns:
            str: the value of `branch_11_name` or None if not set
        """
        return self._data["Branch 11 Name"]

    @branch_11_name.setter
    def branch_11_name(self, value=None):
        """  Corresponds to IDD Field `branch_11_name`

        Args:
            value (str): value for IDD Field `branch_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_11_name`')

        self._data["Branch 11 Name"] = value

    @property
    def branch_12_name(self):
        """Get branch_12_name

        Returns:
            str: the value of `branch_12_name` or None if not set
        """
        return self._data["Branch 12 Name"]

    @branch_12_name.setter
    def branch_12_name(self, value=None):
        """  Corresponds to IDD Field `branch_12_name`

        Args:
            value (str): value for IDD Field `branch_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_12_name`')

        self._data["Branch 12 Name"] = value

    @property
    def branch_13_name(self):
        """Get branch_13_name

        Returns:
            str: the value of `branch_13_name` or None if not set
        """
        return self._data["Branch 13 Name"]

    @branch_13_name.setter
    def branch_13_name(self, value=None):
        """  Corresponds to IDD Field `branch_13_name`

        Args:
            value (str): value for IDD Field `branch_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_13_name`')

        self._data["Branch 13 Name"] = value

    @property
    def branch_14_name(self):
        """Get branch_14_name

        Returns:
            str: the value of `branch_14_name` or None if not set
        """
        return self._data["Branch 14 Name"]

    @branch_14_name.setter
    def branch_14_name(self, value=None):
        """  Corresponds to IDD Field `branch_14_name`

        Args:
            value (str): value for IDD Field `branch_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_14_name`')

        self._data["Branch 14 Name"] = value

    @property
    def branch_15_name(self):
        """Get branch_15_name

        Returns:
            str: the value of `branch_15_name` or None if not set
        """
        return self._data["Branch 15 Name"]

    @branch_15_name.setter
    def branch_15_name(self, value=None):
        """  Corresponds to IDD Field `branch_15_name`

        Args:
            value (str): value for IDD Field `branch_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_15_name`')

        self._data["Branch 15 Name"] = value

    @property
    def branch_16_name(self):
        """Get branch_16_name

        Returns:
            str: the value of `branch_16_name` or None if not set
        """
        return self._data["Branch 16 Name"]

    @branch_16_name.setter
    def branch_16_name(self, value=None):
        """  Corresponds to IDD Field `branch_16_name`

        Args:
            value (str): value for IDD Field `branch_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_16_name`')

        self._data["Branch 16 Name"] = value

    @property
    def branch_17_name(self):
        """Get branch_17_name

        Returns:
            str: the value of `branch_17_name` or None if not set
        """
        return self._data["Branch 17 Name"]

    @branch_17_name.setter
    def branch_17_name(self, value=None):
        """  Corresponds to IDD Field `branch_17_name`

        Args:
            value (str): value for IDD Field `branch_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_17_name`')

        self._data["Branch 17 Name"] = value

    @property
    def branch_18_name(self):
        """Get branch_18_name

        Returns:
            str: the value of `branch_18_name` or None if not set
        """
        return self._data["Branch 18 Name"]

    @branch_18_name.setter
    def branch_18_name(self, value=None):
        """  Corresponds to IDD Field `branch_18_name`

        Args:
            value (str): value for IDD Field `branch_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_18_name`')

        self._data["Branch 18 Name"] = value

    @property
    def branch_19_name(self):
        """Get branch_19_name

        Returns:
            str: the value of `branch_19_name` or None if not set
        """
        return self._data["Branch 19 Name"]

    @branch_19_name.setter
    def branch_19_name(self, value=None):
        """  Corresponds to IDD Field `branch_19_name`

        Args:
            value (str): value for IDD Field `branch_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_19_name`')

        self._data["Branch 19 Name"] = value

    @property
    def branch_20_name(self):
        """Get branch_20_name

        Returns:
            str: the value of `branch_20_name` or None if not set
        """
        return self._data["Branch 20 Name"]

    @branch_20_name.setter
    def branch_20_name(self, value=None):
        """  Corresponds to IDD Field `branch_20_name`

        Args:
            value (str): value for IDD Field `branch_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_20_name`')

        self._data["Branch 20 Name"] = value

    @property
    def branch_21_name(self):
        """Get branch_21_name

        Returns:
            str: the value of `branch_21_name` or None if not set
        """
        return self._data["Branch 21 Name"]

    @branch_21_name.setter
    def branch_21_name(self, value=None):
        """  Corresponds to IDD Field `branch_21_name`

        Args:
            value (str): value for IDD Field `branch_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_21_name`')

        self._data["Branch 21 Name"] = value

    @property
    def branch_22_name(self):
        """Get branch_22_name

        Returns:
            str: the value of `branch_22_name` or None if not set
        """
        return self._data["Branch 22 Name"]

    @branch_22_name.setter
    def branch_22_name(self, value=None):
        """  Corresponds to IDD Field `branch_22_name`

        Args:
            value (str): value for IDD Field `branch_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_22_name`')

        self._data["Branch 22 Name"] = value

    @property
    def branch_23_name(self):
        """Get branch_23_name

        Returns:
            str: the value of `branch_23_name` or None if not set
        """
        return self._data["Branch 23 Name"]

    @branch_23_name.setter
    def branch_23_name(self, value=None):
        """  Corresponds to IDD Field `branch_23_name`

        Args:
            value (str): value for IDD Field `branch_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_23_name`')

        self._data["Branch 23 Name"] = value

    @property
    def branch_24_name(self):
        """Get branch_24_name

        Returns:
            str: the value of `branch_24_name` or None if not set
        """
        return self._data["Branch 24 Name"]

    @branch_24_name.setter
    def branch_24_name(self, value=None):
        """  Corresponds to IDD Field `branch_24_name`

        Args:
            value (str): value for IDD Field `branch_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_24_name`')

        self._data["Branch 24 Name"] = value

    @property
    def branch_25_name(self):
        """Get branch_25_name

        Returns:
            str: the value of `branch_25_name` or None if not set
        """
        return self._data["Branch 25 Name"]

    @branch_25_name.setter
    def branch_25_name(self, value=None):
        """  Corresponds to IDD Field `branch_25_name`

        Args:
            value (str): value for IDD Field `branch_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_25_name`')

        self._data["Branch 25 Name"] = value

    @property
    def branch_26_name(self):
        """Get branch_26_name

        Returns:
            str: the value of `branch_26_name` or None if not set
        """
        return self._data["Branch 26 Name"]

    @branch_26_name.setter
    def branch_26_name(self, value=None):
        """  Corresponds to IDD Field `branch_26_name`

        Args:
            value (str): value for IDD Field `branch_26_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_26_name`')

        self._data["Branch 26 Name"] = value

    @property
    def branch_27_name(self):
        """Get branch_27_name

        Returns:
            str: the value of `branch_27_name` or None if not set
        """
        return self._data["Branch 27 Name"]

    @branch_27_name.setter
    def branch_27_name(self, value=None):
        """  Corresponds to IDD Field `branch_27_name`

        Args:
            value (str): value for IDD Field `branch_27_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_27_name`')

        self._data["Branch 27 Name"] = value

    @property
    def branch_28_name(self):
        """Get branch_28_name

        Returns:
            str: the value of `branch_28_name` or None if not set
        """
        return self._data["Branch 28 Name"]

    @branch_28_name.setter
    def branch_28_name(self, value=None):
        """  Corresponds to IDD Field `branch_28_name`

        Args:
            value (str): value for IDD Field `branch_28_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_28_name`')

        self._data["Branch 28 Name"] = value

    @property
    def branch_29_name(self):
        """Get branch_29_name

        Returns:
            str: the value of `branch_29_name` or None if not set
        """
        return self._data["Branch 29 Name"]

    @branch_29_name.setter
    def branch_29_name(self, value=None):
        """  Corresponds to IDD Field `branch_29_name`

        Args:
            value (str): value for IDD Field `branch_29_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_29_name`')

        self._data["Branch 29 Name"] = value

    @property
    def branch_30_name(self):
        """Get branch_30_name

        Returns:
            str: the value of `branch_30_name` or None if not set
        """
        return self._data["Branch 30 Name"]

    @branch_30_name.setter
    def branch_30_name(self, value=None):
        """  Corresponds to IDD Field `branch_30_name`

        Args:
            value (str): value for IDD Field `branch_30_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_30_name`')

        self._data["Branch 30 Name"] = value

    @property
    def branch_31_name(self):
        """Get branch_31_name

        Returns:
            str: the value of `branch_31_name` or None if not set
        """
        return self._data["Branch 31 Name"]

    @branch_31_name.setter
    def branch_31_name(self, value=None):
        """  Corresponds to IDD Field `branch_31_name`

        Args:
            value (str): value for IDD Field `branch_31_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_31_name`')

        self._data["Branch 31 Name"] = value

    @property
    def branch_32_name(self):
        """Get branch_32_name

        Returns:
            str: the value of `branch_32_name` or None if not set
        """
        return self._data["Branch 32 Name"]

    @branch_32_name.setter
    def branch_32_name(self, value=None):
        """  Corresponds to IDD Field `branch_32_name`

        Args:
            value (str): value for IDD Field `branch_32_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_32_name`')

        self._data["Branch 32 Name"] = value

    @property
    def branch_33_name(self):
        """Get branch_33_name

        Returns:
            str: the value of `branch_33_name` or None if not set
        """
        return self._data["Branch 33 Name"]

    @branch_33_name.setter
    def branch_33_name(self, value=None):
        """  Corresponds to IDD Field `branch_33_name`

        Args:
            value (str): value for IDD Field `branch_33_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_33_name`')

        self._data["Branch 33 Name"] = value

    @property
    def branch_34_name(self):
        """Get branch_34_name

        Returns:
            str: the value of `branch_34_name` or None if not set
        """
        return self._data["Branch 34 Name"]

    @branch_34_name.setter
    def branch_34_name(self, value=None):
        """  Corresponds to IDD Field `branch_34_name`

        Args:
            value (str): value for IDD Field `branch_34_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_34_name`')

        self._data["Branch 34 Name"] = value

    @property
    def branch_35_name(self):
        """Get branch_35_name

        Returns:
            str: the value of `branch_35_name` or None if not set
        """
        return self._data["Branch 35 Name"]

    @branch_35_name.setter
    def branch_35_name(self, value=None):
        """  Corresponds to IDD Field `branch_35_name`

        Args:
            value (str): value for IDD Field `branch_35_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_35_name`')

        self._data["Branch 35 Name"] = value

    @property
    def branch_36_name(self):
        """Get branch_36_name

        Returns:
            str: the value of `branch_36_name` or None if not set
        """
        return self._data["Branch 36 Name"]

    @branch_36_name.setter
    def branch_36_name(self, value=None):
        """  Corresponds to IDD Field `branch_36_name`

        Args:
            value (str): value for IDD Field `branch_36_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_36_name`')

        self._data["Branch 36 Name"] = value

    @property
    def branch_37_name(self):
        """Get branch_37_name

        Returns:
            str: the value of `branch_37_name` or None if not set
        """
        return self._data["Branch 37 Name"]

    @branch_37_name.setter
    def branch_37_name(self, value=None):
        """  Corresponds to IDD Field `branch_37_name`

        Args:
            value (str): value for IDD Field `branch_37_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_37_name`')

        self._data["Branch 37 Name"] = value

    @property
    def branch_38_name(self):
        """Get branch_38_name

        Returns:
            str: the value of `branch_38_name` or None if not set
        """
        return self._data["Branch 38 Name"]

    @branch_38_name.setter
    def branch_38_name(self, value=None):
        """  Corresponds to IDD Field `branch_38_name`

        Args:
            value (str): value for IDD Field `branch_38_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_38_name`')

        self._data["Branch 38 Name"] = value

    @property
    def branch_39_name(self):
        """Get branch_39_name

        Returns:
            str: the value of `branch_39_name` or None if not set
        """
        return self._data["Branch 39 Name"]

    @branch_39_name.setter
    def branch_39_name(self, value=None):
        """  Corresponds to IDD Field `branch_39_name`

        Args:
            value (str): value for IDD Field `branch_39_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_39_name`')

        self._data["Branch 39 Name"] = value

    @property
    def branch_40_name(self):
        """Get branch_40_name

        Returns:
            str: the value of `branch_40_name` or None if not set
        """
        return self._data["Branch 40 Name"]

    @branch_40_name.setter
    def branch_40_name(self, value=None):
        """  Corresponds to IDD Field `branch_40_name`

        Args:
            value (str): value for IDD Field `branch_40_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_40_name`')

        self._data["Branch 40 Name"] = value

    @property
    def branch_41_name(self):
        """Get branch_41_name

        Returns:
            str: the value of `branch_41_name` or None if not set
        """
        return self._data["Branch 41 Name"]

    @branch_41_name.setter
    def branch_41_name(self, value=None):
        """  Corresponds to IDD Field `branch_41_name`

        Args:
            value (str): value for IDD Field `branch_41_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_41_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_41_name`')

        self._data["Branch 41 Name"] = value

    @property
    def branch_42_name(self):
        """Get branch_42_name

        Returns:
            str: the value of `branch_42_name` or None if not set
        """
        return self._data["Branch 42 Name"]

    @branch_42_name.setter
    def branch_42_name(self, value=None):
        """  Corresponds to IDD Field `branch_42_name`

        Args:
            value (str): value for IDD Field `branch_42_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_42_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_42_name`')

        self._data["Branch 42 Name"] = value

    @property
    def branch_43_name(self):
        """Get branch_43_name

        Returns:
            str: the value of `branch_43_name` or None if not set
        """
        return self._data["Branch 43 Name"]

    @branch_43_name.setter
    def branch_43_name(self, value=None):
        """  Corresponds to IDD Field `branch_43_name`

        Args:
            value (str): value for IDD Field `branch_43_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_43_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_43_name`')

        self._data["Branch 43 Name"] = value

    @property
    def branch_44_name(self):
        """Get branch_44_name

        Returns:
            str: the value of `branch_44_name` or None if not set
        """
        return self._data["Branch 44 Name"]

    @branch_44_name.setter
    def branch_44_name(self, value=None):
        """  Corresponds to IDD Field `branch_44_name`

        Args:
            value (str): value for IDD Field `branch_44_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_44_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_44_name`')

        self._data["Branch 44 Name"] = value

    @property
    def branch_45_name(self):
        """Get branch_45_name

        Returns:
            str: the value of `branch_45_name` or None if not set
        """
        return self._data["Branch 45 Name"]

    @branch_45_name.setter
    def branch_45_name(self, value=None):
        """  Corresponds to IDD Field `branch_45_name`

        Args:
            value (str): value for IDD Field `branch_45_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_45_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_45_name`')

        self._data["Branch 45 Name"] = value

    @property
    def branch_46_name(self):
        """Get branch_46_name

        Returns:
            str: the value of `branch_46_name` or None if not set
        """
        return self._data["Branch 46 Name"]

    @branch_46_name.setter
    def branch_46_name(self, value=None):
        """  Corresponds to IDD Field `branch_46_name`

        Args:
            value (str): value for IDD Field `branch_46_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_46_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_46_name`')

        self._data["Branch 46 Name"] = value

    @property
    def branch_47_name(self):
        """Get branch_47_name

        Returns:
            str: the value of `branch_47_name` or None if not set
        """
        return self._data["Branch 47 Name"]

    @branch_47_name.setter
    def branch_47_name(self, value=None):
        """  Corresponds to IDD Field `branch_47_name`

        Args:
            value (str): value for IDD Field `branch_47_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_47_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_47_name`')

        self._data["Branch 47 Name"] = value

    @property
    def branch_48_name(self):
        """Get branch_48_name

        Returns:
            str: the value of `branch_48_name` or None if not set
        """
        return self._data["Branch 48 Name"]

    @branch_48_name.setter
    def branch_48_name(self, value=None):
        """  Corresponds to IDD Field `branch_48_name`

        Args:
            value (str): value for IDD Field `branch_48_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_48_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_48_name`')

        self._data["Branch 48 Name"] = value

    @property
    def branch_49_name(self):
        """Get branch_49_name

        Returns:
            str: the value of `branch_49_name` or None if not set
        """
        return self._data["Branch 49 Name"]

    @branch_49_name.setter
    def branch_49_name(self, value=None):
        """  Corresponds to IDD Field `branch_49_name`

        Args:
            value (str): value for IDD Field `branch_49_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_49_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_49_name`')

        self._data["Branch 49 Name"] = value

    @property
    def branch_50_name(self):
        """Get branch_50_name

        Returns:
            str: the value of `branch_50_name` or None if not set
        """
        return self._data["Branch 50 Name"]

    @branch_50_name.setter
    def branch_50_name(self, value=None):
        """  Corresponds to IDD Field `branch_50_name`

        Args:
            value (str): value for IDD Field `branch_50_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_50_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_50_name`')

        self._data["Branch 50 Name"] = value

    @property
    def branch_51_name(self):
        """Get branch_51_name

        Returns:
            str: the value of `branch_51_name` or None if not set
        """
        return self._data["Branch 51 Name"]

    @branch_51_name.setter
    def branch_51_name(self, value=None):
        """  Corresponds to IDD Field `branch_51_name`

        Args:
            value (str): value for IDD Field `branch_51_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_51_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_51_name`')

        self._data["Branch 51 Name"] = value

    @property
    def branch_52_name(self):
        """Get branch_52_name

        Returns:
            str: the value of `branch_52_name` or None if not set
        """
        return self._data["Branch 52 Name"]

    @branch_52_name.setter
    def branch_52_name(self, value=None):
        """  Corresponds to IDD Field `branch_52_name`

        Args:
            value (str): value for IDD Field `branch_52_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_52_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_52_name`')

        self._data["Branch 52 Name"] = value

    @property
    def branch_53_name(self):
        """Get branch_53_name

        Returns:
            str: the value of `branch_53_name` or None if not set
        """
        return self._data["Branch 53 Name"]

    @branch_53_name.setter
    def branch_53_name(self, value=None):
        """  Corresponds to IDD Field `branch_53_name`

        Args:
            value (str): value for IDD Field `branch_53_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_53_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_53_name`')

        self._data["Branch 53 Name"] = value

    @property
    def branch_54_name(self):
        """Get branch_54_name

        Returns:
            str: the value of `branch_54_name` or None if not set
        """
        return self._data["Branch 54 Name"]

    @branch_54_name.setter
    def branch_54_name(self, value=None):
        """  Corresponds to IDD Field `branch_54_name`

        Args:
            value (str): value for IDD Field `branch_54_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_54_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_54_name`')

        self._data["Branch 54 Name"] = value

    @property
    def branch_55_name(self):
        """Get branch_55_name

        Returns:
            str: the value of `branch_55_name` or None if not set
        """
        return self._data["Branch 55 Name"]

    @branch_55_name.setter
    def branch_55_name(self, value=None):
        """  Corresponds to IDD Field `branch_55_name`

        Args:
            value (str): value for IDD Field `branch_55_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_55_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_55_name`')

        self._data["Branch 55 Name"] = value

    @property
    def branch_56_name(self):
        """Get branch_56_name

        Returns:
            str: the value of `branch_56_name` or None if not set
        """
        return self._data["Branch 56 Name"]

    @branch_56_name.setter
    def branch_56_name(self, value=None):
        """  Corresponds to IDD Field `branch_56_name`

        Args:
            value (str): value for IDD Field `branch_56_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_56_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_56_name`')

        self._data["Branch 56 Name"] = value

    @property
    def branch_57_name(self):
        """Get branch_57_name

        Returns:
            str: the value of `branch_57_name` or None if not set
        """
        return self._data["Branch 57 Name"]

    @branch_57_name.setter
    def branch_57_name(self, value=None):
        """  Corresponds to IDD Field `branch_57_name`

        Args:
            value (str): value for IDD Field `branch_57_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_57_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_57_name`')

        self._data["Branch 57 Name"] = value

    @property
    def branch_58_name(self):
        """Get branch_58_name

        Returns:
            str: the value of `branch_58_name` or None if not set
        """
        return self._data["Branch 58 Name"]

    @branch_58_name.setter
    def branch_58_name(self, value=None):
        """  Corresponds to IDD Field `branch_58_name`

        Args:
            value (str): value for IDD Field `branch_58_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_58_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_58_name`')

        self._data["Branch 58 Name"] = value

    @property
    def branch_59_name(self):
        """Get branch_59_name

        Returns:
            str: the value of `branch_59_name` or None if not set
        """
        return self._data["Branch 59 Name"]

    @branch_59_name.setter
    def branch_59_name(self, value=None):
        """  Corresponds to IDD Field `branch_59_name`

        Args:
            value (str): value for IDD Field `branch_59_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_59_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_59_name`')

        self._data["Branch 59 Name"] = value

    @property
    def branch_60_name(self):
        """Get branch_60_name

        Returns:
            str: the value of `branch_60_name` or None if not set
        """
        return self._data["Branch 60 Name"]

    @branch_60_name.setter
    def branch_60_name(self, value=None):
        """  Corresponds to IDD Field `branch_60_name`

        Args:
            value (str): value for IDD Field `branch_60_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_60_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_60_name`')

        self._data["Branch 60 Name"] = value

    @property
    def branch_61_name(self):
        """Get branch_61_name

        Returns:
            str: the value of `branch_61_name` or None if not set
        """
        return self._data["Branch 61 Name"]

    @branch_61_name.setter
    def branch_61_name(self, value=None):
        """  Corresponds to IDD Field `branch_61_name`

        Args:
            value (str): value for IDD Field `branch_61_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_61_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_61_name`')

        self._data["Branch 61 Name"] = value

    @property
    def branch_62_name(self):
        """Get branch_62_name

        Returns:
            str: the value of `branch_62_name` or None if not set
        """
        return self._data["Branch 62 Name"]

    @branch_62_name.setter
    def branch_62_name(self, value=None):
        """  Corresponds to IDD Field `branch_62_name`

        Args:
            value (str): value for IDD Field `branch_62_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_62_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_62_name`')

        self._data["Branch 62 Name"] = value

    @property
    def branch_63_name(self):
        """Get branch_63_name

        Returns:
            str: the value of `branch_63_name` or None if not set
        """
        return self._data["Branch 63 Name"]

    @branch_63_name.setter
    def branch_63_name(self, value=None):
        """  Corresponds to IDD Field `branch_63_name`

        Args:
            value (str): value for IDD Field `branch_63_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_63_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_63_name`')

        self._data["Branch 63 Name"] = value

    @property
    def branch_64_name(self):
        """Get branch_64_name

        Returns:
            str: the value of `branch_64_name` or None if not set
        """
        return self._data["Branch 64 Name"]

    @branch_64_name.setter
    def branch_64_name(self, value=None):
        """  Corresponds to IDD Field `branch_64_name`

        Args:
            value (str): value for IDD Field `branch_64_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_64_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_64_name`')

        self._data["Branch 64 Name"] = value

    @property
    def branch_65_name(self):
        """Get branch_65_name

        Returns:
            str: the value of `branch_65_name` or None if not set
        """
        return self._data["Branch 65 Name"]

    @branch_65_name.setter
    def branch_65_name(self, value=None):
        """  Corresponds to IDD Field `branch_65_name`

        Args:
            value (str): value for IDD Field `branch_65_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_65_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_65_name`')

        self._data["Branch 65 Name"] = value

    @property
    def branch_66_name(self):
        """Get branch_66_name

        Returns:
            str: the value of `branch_66_name` or None if not set
        """
        return self._data["Branch 66 Name"]

    @branch_66_name.setter
    def branch_66_name(self, value=None):
        """  Corresponds to IDD Field `branch_66_name`

        Args:
            value (str): value for IDD Field `branch_66_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_66_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_66_name`')

        self._data["Branch 66 Name"] = value

    @property
    def branch_67_name(self):
        """Get branch_67_name

        Returns:
            str: the value of `branch_67_name` or None if not set
        """
        return self._data["Branch 67 Name"]

    @branch_67_name.setter
    def branch_67_name(self, value=None):
        """  Corresponds to IDD Field `branch_67_name`

        Args:
            value (str): value for IDD Field `branch_67_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_67_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_67_name`')

        self._data["Branch 67 Name"] = value

    @property
    def branch_68_name(self):
        """Get branch_68_name

        Returns:
            str: the value of `branch_68_name` or None if not set
        """
        return self._data["Branch 68 Name"]

    @branch_68_name.setter
    def branch_68_name(self, value=None):
        """  Corresponds to IDD Field `branch_68_name`

        Args:
            value (str): value for IDD Field `branch_68_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_68_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_68_name`')

        self._data["Branch 68 Name"] = value

    @property
    def branch_69_name(self):
        """Get branch_69_name

        Returns:
            str: the value of `branch_69_name` or None if not set
        """
        return self._data["Branch 69 Name"]

    @branch_69_name.setter
    def branch_69_name(self, value=None):
        """  Corresponds to IDD Field `branch_69_name`

        Args:
            value (str): value for IDD Field `branch_69_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_69_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_69_name`')

        self._data["Branch 69 Name"] = value

    @property
    def branch_70_name(self):
        """Get branch_70_name

        Returns:
            str: the value of `branch_70_name` or None if not set
        """
        return self._data["Branch 70 Name"]

    @branch_70_name.setter
    def branch_70_name(self, value=None):
        """  Corresponds to IDD Field `branch_70_name`

        Args:
            value (str): value for IDD Field `branch_70_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_70_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_70_name`')

        self._data["Branch 70 Name"] = value

    @property
    def branch_71_name(self):
        """Get branch_71_name

        Returns:
            str: the value of `branch_71_name` or None if not set
        """
        return self._data["Branch 71 Name"]

    @branch_71_name.setter
    def branch_71_name(self, value=None):
        """  Corresponds to IDD Field `branch_71_name`

        Args:
            value (str): value for IDD Field `branch_71_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_71_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_71_name`')

        self._data["Branch 71 Name"] = value

    @property
    def branch_72_name(self):
        """Get branch_72_name

        Returns:
            str: the value of `branch_72_name` or None if not set
        """
        return self._data["Branch 72 Name"]

    @branch_72_name.setter
    def branch_72_name(self, value=None):
        """  Corresponds to IDD Field `branch_72_name`

        Args:
            value (str): value for IDD Field `branch_72_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_72_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_72_name`')

        self._data["Branch 72 Name"] = value

    @property
    def branch_73_name(self):
        """Get branch_73_name

        Returns:
            str: the value of `branch_73_name` or None if not set
        """
        return self._data["Branch 73 Name"]

    @branch_73_name.setter
    def branch_73_name(self, value=None):
        """  Corresponds to IDD Field `branch_73_name`

        Args:
            value (str): value for IDD Field `branch_73_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_73_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_73_name`')

        self._data["Branch 73 Name"] = value

    @property
    def branch_74_name(self):
        """Get branch_74_name

        Returns:
            str: the value of `branch_74_name` or None if not set
        """
        return self._data["Branch 74 Name"]

    @branch_74_name.setter
    def branch_74_name(self, value=None):
        """  Corresponds to IDD Field `branch_74_name`

        Args:
            value (str): value for IDD Field `branch_74_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_74_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_74_name`')

        self._data["Branch 74 Name"] = value

    @property
    def branch_75_name(self):
        """Get branch_75_name

        Returns:
            str: the value of `branch_75_name` or None if not set
        """
        return self._data["Branch 75 Name"]

    @branch_75_name.setter
    def branch_75_name(self, value=None):
        """  Corresponds to IDD Field `branch_75_name`

        Args:
            value (str): value for IDD Field `branch_75_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_75_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_75_name`')

        self._data["Branch 75 Name"] = value

    @property
    def branch_76_name(self):
        """Get branch_76_name

        Returns:
            str: the value of `branch_76_name` or None if not set
        """
        return self._data["Branch 76 Name"]

    @branch_76_name.setter
    def branch_76_name(self, value=None):
        """  Corresponds to IDD Field `branch_76_name`

        Args:
            value (str): value for IDD Field `branch_76_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_76_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_76_name`')

        self._data["Branch 76 Name"] = value

    @property
    def branch_77_name(self):
        """Get branch_77_name

        Returns:
            str: the value of `branch_77_name` or None if not set
        """
        return self._data["Branch 77 Name"]

    @branch_77_name.setter
    def branch_77_name(self, value=None):
        """  Corresponds to IDD Field `branch_77_name`

        Args:
            value (str): value for IDD Field `branch_77_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_77_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_77_name`')

        self._data["Branch 77 Name"] = value

    @property
    def branch_78_name(self):
        """Get branch_78_name

        Returns:
            str: the value of `branch_78_name` or None if not set
        """
        return self._data["Branch 78 Name"]

    @branch_78_name.setter
    def branch_78_name(self, value=None):
        """  Corresponds to IDD Field `branch_78_name`

        Args:
            value (str): value for IDD Field `branch_78_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_78_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_78_name`')

        self._data["Branch 78 Name"] = value

    @property
    def branch_79_name(self):
        """Get branch_79_name

        Returns:
            str: the value of `branch_79_name` or None if not set
        """
        return self._data["Branch 79 Name"]

    @branch_79_name.setter
    def branch_79_name(self, value=None):
        """  Corresponds to IDD Field `branch_79_name`

        Args:
            value (str): value for IDD Field `branch_79_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_79_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_79_name`')

        self._data["Branch 79 Name"] = value

    @property
    def branch_80_name(self):
        """Get branch_80_name

        Returns:
            str: the value of `branch_80_name` or None if not set
        """
        return self._data["Branch 80 Name"]

    @branch_80_name.setter
    def branch_80_name(self, value=None):
        """  Corresponds to IDD Field `branch_80_name`

        Args:
            value (str): value for IDD Field `branch_80_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_80_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_80_name`')

        self._data["Branch 80 Name"] = value

    @property
    def branch_81_name(self):
        """Get branch_81_name

        Returns:
            str: the value of `branch_81_name` or None if not set
        """
        return self._data["Branch 81 Name"]

    @branch_81_name.setter
    def branch_81_name(self, value=None):
        """  Corresponds to IDD Field `branch_81_name`

        Args:
            value (str): value for IDD Field `branch_81_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_81_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_81_name`')

        self._data["Branch 81 Name"] = value

    @property
    def branch_82_name(self):
        """Get branch_82_name

        Returns:
            str: the value of `branch_82_name` or None if not set
        """
        return self._data["Branch 82 Name"]

    @branch_82_name.setter
    def branch_82_name(self, value=None):
        """  Corresponds to IDD Field `branch_82_name`

        Args:
            value (str): value for IDD Field `branch_82_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_82_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_82_name`')

        self._data["Branch 82 Name"] = value

    @property
    def branch_83_name(self):
        """Get branch_83_name

        Returns:
            str: the value of `branch_83_name` or None if not set
        """
        return self._data["Branch 83 Name"]

    @branch_83_name.setter
    def branch_83_name(self, value=None):
        """  Corresponds to IDD Field `branch_83_name`

        Args:
            value (str): value for IDD Field `branch_83_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_83_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_83_name`')

        self._data["Branch 83 Name"] = value

    @property
    def branch_84_name(self):
        """Get branch_84_name

        Returns:
            str: the value of `branch_84_name` or None if not set
        """
        return self._data["Branch 84 Name"]

    @branch_84_name.setter
    def branch_84_name(self, value=None):
        """  Corresponds to IDD Field `branch_84_name`

        Args:
            value (str): value for IDD Field `branch_84_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_84_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_84_name`')

        self._data["Branch 84 Name"] = value

    @property
    def branch_85_name(self):
        """Get branch_85_name

        Returns:
            str: the value of `branch_85_name` or None if not set
        """
        return self._data["Branch 85 Name"]

    @branch_85_name.setter
    def branch_85_name(self, value=None):
        """  Corresponds to IDD Field `branch_85_name`

        Args:
            value (str): value for IDD Field `branch_85_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_85_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_85_name`')

        self._data["Branch 85 Name"] = value

    @property
    def branch_86_name(self):
        """Get branch_86_name

        Returns:
            str: the value of `branch_86_name` or None if not set
        """
        return self._data["Branch 86 Name"]

    @branch_86_name.setter
    def branch_86_name(self, value=None):
        """  Corresponds to IDD Field `branch_86_name`

        Args:
            value (str): value for IDD Field `branch_86_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_86_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_86_name`')

        self._data["Branch 86 Name"] = value

    @property
    def branch_87_name(self):
        """Get branch_87_name

        Returns:
            str: the value of `branch_87_name` or None if not set
        """
        return self._data["Branch 87 Name"]

    @branch_87_name.setter
    def branch_87_name(self, value=None):
        """  Corresponds to IDD Field `branch_87_name`

        Args:
            value (str): value for IDD Field `branch_87_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_87_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_87_name`')

        self._data["Branch 87 Name"] = value

    @property
    def branch_88_name(self):
        """Get branch_88_name

        Returns:
            str: the value of `branch_88_name` or None if not set
        """
        return self._data["Branch 88 Name"]

    @branch_88_name.setter
    def branch_88_name(self, value=None):
        """  Corresponds to IDD Field `branch_88_name`

        Args:
            value (str): value for IDD Field `branch_88_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_88_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_88_name`')

        self._data["Branch 88 Name"] = value

    @property
    def branch_89_name(self):
        """Get branch_89_name

        Returns:
            str: the value of `branch_89_name` or None if not set
        """
        return self._data["Branch 89 Name"]

    @branch_89_name.setter
    def branch_89_name(self, value=None):
        """  Corresponds to IDD Field `branch_89_name`

        Args:
            value (str): value for IDD Field `branch_89_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_89_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_89_name`')

        self._data["Branch 89 Name"] = value

    @property
    def branch_90_name(self):
        """Get branch_90_name

        Returns:
            str: the value of `branch_90_name` or None if not set
        """
        return self._data["Branch 90 Name"]

    @branch_90_name.setter
    def branch_90_name(self, value=None):
        """  Corresponds to IDD Field `branch_90_name`

        Args:
            value (str): value for IDD Field `branch_90_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_90_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_90_name`')

        self._data["Branch 90 Name"] = value

    @property
    def branch_91_name(self):
        """Get branch_91_name

        Returns:
            str: the value of `branch_91_name` or None if not set
        """
        return self._data["Branch 91 Name"]

    @branch_91_name.setter
    def branch_91_name(self, value=None):
        """  Corresponds to IDD Field `branch_91_name`

        Args:
            value (str): value for IDD Field `branch_91_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_91_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_91_name`')

        self._data["Branch 91 Name"] = value

    @property
    def branch_92_name(self):
        """Get branch_92_name

        Returns:
            str: the value of `branch_92_name` or None if not set
        """
        return self._data["Branch 92 Name"]

    @branch_92_name.setter
    def branch_92_name(self, value=None):
        """  Corresponds to IDD Field `branch_92_name`

        Args:
            value (str): value for IDD Field `branch_92_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_92_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_92_name`')

        self._data["Branch 92 Name"] = value

    @property
    def branch_93_name(self):
        """Get branch_93_name

        Returns:
            str: the value of `branch_93_name` or None if not set
        """
        return self._data["Branch 93 Name"]

    @branch_93_name.setter
    def branch_93_name(self, value=None):
        """  Corresponds to IDD Field `branch_93_name`

        Args:
            value (str): value for IDD Field `branch_93_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_93_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_93_name`')

        self._data["Branch 93 Name"] = value

    @property
    def branch_94_name(self):
        """Get branch_94_name

        Returns:
            str: the value of `branch_94_name` or None if not set
        """
        return self._data["Branch 94 Name"]

    @branch_94_name.setter
    def branch_94_name(self, value=None):
        """  Corresponds to IDD Field `branch_94_name`

        Args:
            value (str): value for IDD Field `branch_94_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_94_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_94_name`')

        self._data["Branch 94 Name"] = value

    @property
    def branch_95_name(self):
        """Get branch_95_name

        Returns:
            str: the value of `branch_95_name` or None if not set
        """
        return self._data["Branch 95 Name"]

    @branch_95_name.setter
    def branch_95_name(self, value=None):
        """  Corresponds to IDD Field `branch_95_name`

        Args:
            value (str): value for IDD Field `branch_95_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_95_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_95_name`')

        self._data["Branch 95 Name"] = value

    @property
    def branch_96_name(self):
        """Get branch_96_name

        Returns:
            str: the value of `branch_96_name` or None if not set
        """
        return self._data["Branch 96 Name"]

    @branch_96_name.setter
    def branch_96_name(self, value=None):
        """  Corresponds to IDD Field `branch_96_name`

        Args:
            value (str): value for IDD Field `branch_96_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_96_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_96_name`')

        self._data["Branch 96 Name"] = value

    @property
    def branch_97_name(self):
        """Get branch_97_name

        Returns:
            str: the value of `branch_97_name` or None if not set
        """
        return self._data["Branch 97 Name"]

    @branch_97_name.setter
    def branch_97_name(self, value=None):
        """  Corresponds to IDD Field `branch_97_name`

        Args:
            value (str): value for IDD Field `branch_97_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_97_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_97_name`')

        self._data["Branch 97 Name"] = value

    @property
    def branch_98_name(self):
        """Get branch_98_name

        Returns:
            str: the value of `branch_98_name` or None if not set
        """
        return self._data["Branch 98 Name"]

    @branch_98_name.setter
    def branch_98_name(self, value=None):
        """  Corresponds to IDD Field `branch_98_name`

        Args:
            value (str): value for IDD Field `branch_98_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_98_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_98_name`')

        self._data["Branch 98 Name"] = value

    @property
    def branch_99_name(self):
        """Get branch_99_name

        Returns:
            str: the value of `branch_99_name` or None if not set
        """
        return self._data["Branch 99 Name"]

    @branch_99_name.setter
    def branch_99_name(self, value=None):
        """  Corresponds to IDD Field `branch_99_name`

        Args:
            value (str): value for IDD Field `branch_99_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_99_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_99_name`')

        self._data["Branch 99 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

    @property
    def branch_100_name(self):
        """Get branch_100_name

        Returns:
            str: the value of `branch_100_name` or None if not set
        """
        return self._data["Branch 100 Name"]

    @branch_100_name.setter
    def branch_100_name(self, value=None):
        """  Corresponds to IDD Field `branch_100_name`

        Args:
            value (str): value for IDD Field `branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `branch_100_name`')

        self._data["Branch 100 Name"] = value

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
        out.append(self._to_str(self.branch_1_name))
        out.append(self._to_str(self.branch_2_name))
        out.append(self._to_str(self.branch_3_name))
        out.append(self._to_str(self.branch_4_name))
        out.append(self._to_str(self.branch_5_name))
        out.append(self._to_str(self.branch_6_name))
        out.append(self._to_str(self.branch_7_name))
        out.append(self._to_str(self.branch_8_name))
        out.append(self._to_str(self.branch_9_name))
        out.append(self._to_str(self.branch_10_name))
        out.append(self._to_str(self.branch_11_name))
        out.append(self._to_str(self.branch_12_name))
        out.append(self._to_str(self.branch_13_name))
        out.append(self._to_str(self.branch_14_name))
        out.append(self._to_str(self.branch_15_name))
        out.append(self._to_str(self.branch_16_name))
        out.append(self._to_str(self.branch_17_name))
        out.append(self._to_str(self.branch_18_name))
        out.append(self._to_str(self.branch_19_name))
        out.append(self._to_str(self.branch_20_name))
        out.append(self._to_str(self.branch_21_name))
        out.append(self._to_str(self.branch_22_name))
        out.append(self._to_str(self.branch_23_name))
        out.append(self._to_str(self.branch_24_name))
        out.append(self._to_str(self.branch_25_name))
        out.append(self._to_str(self.branch_26_name))
        out.append(self._to_str(self.branch_27_name))
        out.append(self._to_str(self.branch_28_name))
        out.append(self._to_str(self.branch_29_name))
        out.append(self._to_str(self.branch_30_name))
        out.append(self._to_str(self.branch_31_name))
        out.append(self._to_str(self.branch_32_name))
        out.append(self._to_str(self.branch_33_name))
        out.append(self._to_str(self.branch_34_name))
        out.append(self._to_str(self.branch_35_name))
        out.append(self._to_str(self.branch_36_name))
        out.append(self._to_str(self.branch_37_name))
        out.append(self._to_str(self.branch_38_name))
        out.append(self._to_str(self.branch_39_name))
        out.append(self._to_str(self.branch_40_name))
        out.append(self._to_str(self.branch_41_name))
        out.append(self._to_str(self.branch_42_name))
        out.append(self._to_str(self.branch_43_name))
        out.append(self._to_str(self.branch_44_name))
        out.append(self._to_str(self.branch_45_name))
        out.append(self._to_str(self.branch_46_name))
        out.append(self._to_str(self.branch_47_name))
        out.append(self._to_str(self.branch_48_name))
        out.append(self._to_str(self.branch_49_name))
        out.append(self._to_str(self.branch_50_name))
        out.append(self._to_str(self.branch_51_name))
        out.append(self._to_str(self.branch_52_name))
        out.append(self._to_str(self.branch_53_name))
        out.append(self._to_str(self.branch_54_name))
        out.append(self._to_str(self.branch_55_name))
        out.append(self._to_str(self.branch_56_name))
        out.append(self._to_str(self.branch_57_name))
        out.append(self._to_str(self.branch_58_name))
        out.append(self._to_str(self.branch_59_name))
        out.append(self._to_str(self.branch_60_name))
        out.append(self._to_str(self.branch_61_name))
        out.append(self._to_str(self.branch_62_name))
        out.append(self._to_str(self.branch_63_name))
        out.append(self._to_str(self.branch_64_name))
        out.append(self._to_str(self.branch_65_name))
        out.append(self._to_str(self.branch_66_name))
        out.append(self._to_str(self.branch_67_name))
        out.append(self._to_str(self.branch_68_name))
        out.append(self._to_str(self.branch_69_name))
        out.append(self._to_str(self.branch_70_name))
        out.append(self._to_str(self.branch_71_name))
        out.append(self._to_str(self.branch_72_name))
        out.append(self._to_str(self.branch_73_name))
        out.append(self._to_str(self.branch_74_name))
        out.append(self._to_str(self.branch_75_name))
        out.append(self._to_str(self.branch_76_name))
        out.append(self._to_str(self.branch_77_name))
        out.append(self._to_str(self.branch_78_name))
        out.append(self._to_str(self.branch_79_name))
        out.append(self._to_str(self.branch_80_name))
        out.append(self._to_str(self.branch_81_name))
        out.append(self._to_str(self.branch_82_name))
        out.append(self._to_str(self.branch_83_name))
        out.append(self._to_str(self.branch_84_name))
        out.append(self._to_str(self.branch_85_name))
        out.append(self._to_str(self.branch_86_name))
        out.append(self._to_str(self.branch_87_name))
        out.append(self._to_str(self.branch_88_name))
        out.append(self._to_str(self.branch_89_name))
        out.append(self._to_str(self.branch_90_name))
        out.append(self._to_str(self.branch_91_name))
        out.append(self._to_str(self.branch_92_name))
        out.append(self._to_str(self.branch_93_name))
        out.append(self._to_str(self.branch_94_name))
        out.append(self._to_str(self.branch_95_name))
        out.append(self._to_str(self.branch_96_name))
        out.append(self._to_str(self.branch_97_name))
        out.append(self._to_str(self.branch_98_name))
        out.append(self._to_str(self.branch_99_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        out.append(self._to_str(self.branch_100_name))
        return ",".join(out)