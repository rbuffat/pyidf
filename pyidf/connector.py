from collections import OrderedDict

class ConnectorSplitter(object):
    """ Corresponds to IDD object `Connector:Splitter`
        Split one air/water stream into N outlet streams.  Branch names cannot be duplicated
        within a single Splitter list.
    """
    internal_name = "Connector:Splitter"
    field_count = 142

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Connector:Splitter`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Branch Name"] = None
        self._data["Outlet Branch 1 Name"] = None
        self._data["Outlet Branch 2 Name"] = None
        self._data["Outlet Branch 3 Name"] = None
        self._data["Outlet Branch 4 Name"] = None
        self._data["Outlet Branch 5 Name"] = None
        self._data["Outlet Branch 6 Name"] = None
        self._data["Outlet Branch 7 Name"] = None
        self._data["Outlet Branch 8 Name"] = None
        self._data["Outlet Branch 9 Name"] = None
        self._data["Outlet Branch 10 Name"] = None
        self._data["Outlet Branch 11 Name"] = None
        self._data["Outlet Branch 12 Name"] = None
        self._data["Outlet Branch 13 Name"] = None
        self._data["Outlet Branch 14 Name"] = None
        self._data["Outlet Branch 15 Name"] = None
        self._data["Outlet Branch 16 Name"] = None
        self._data["Outlet Branch 17 Name"] = None
        self._data["Outlet Branch 18 Name"] = None
        self._data["Outlet Branch 19 Name"] = None
        self._data["Outlet Branch 20 Name"] = None
        self._data["Outlet Branch 21 Name"] = None
        self._data["Outlet Branch 22 Name"] = None
        self._data["Outlet Branch 23 Name"] = None
        self._data["Outlet Branch 24 Name"] = None
        self._data["Outlet Branch 25 Name"] = None
        self._data["Outlet Branch 26 Name"] = None
        self._data["Outlet Branch 27 Name"] = None
        self._data["Outlet Branch 28 Name"] = None
        self._data["Outlet Branch 29 Name"] = None
        self._data["Outlet Branch 30 Name"] = None
        self._data["Outlet Branch 31 Name"] = None
        self._data["Outlet Branch 32 Name"] = None
        self._data["Outlet Branch 33 Name"] = None
        self._data["Outlet Branch 34 Name"] = None
        self._data["Outlet Branch 35 Name"] = None
        self._data["Outlet Branch 36 Name"] = None
        self._data["Outlet Branch 37 Name"] = None
        self._data["Outlet Branch 38 Name"] = None
        self._data["Outlet Branch 39 Name"] = None
        self._data["Outlet Branch 40 Name"] = None
        self._data["Outlet Branch 41 Name"] = None
        self._data["Outlet Branch 42 Name"] = None
        self._data["Outlet Branch 43 Name"] = None
        self._data["Outlet Branch 44 Name"] = None
        self._data["Outlet Branch 45 Name"] = None
        self._data["Outlet Branch 46 Name"] = None
        self._data["Outlet Branch 47 Name"] = None
        self._data["Outlet Branch 48 Name"] = None
        self._data["Outlet Branch 49 Name"] = None
        self._data["Outlet Branch 50 Name"] = None
        self._data["Outlet Branch 51 Name"] = None
        self._data["Outlet Branch 52 Name"] = None
        self._data["Outlet Branch 53 Name"] = None
        self._data["Outlet Branch 54 Name"] = None
        self._data["Outlet Branch 55 Name"] = None
        self._data["Outlet Branch 56 Name"] = None
        self._data["Outlet Branch 57 Name"] = None
        self._data["Outlet Branch 58 Name"] = None
        self._data["Outlet Branch 59 Name"] = None
        self._data["Outlet Branch 60 Name"] = None
        self._data["Outlet Branch 61 Name"] = None
        self._data["Outlet Branch 62 Name"] = None
        self._data["Outlet Branch 63 Name"] = None
        self._data["Outlet Branch 64 Name"] = None
        self._data["Outlet Branch 65 Name"] = None
        self._data["Outlet Branch 66 Name"] = None
        self._data["Outlet Branch 67 Name"] = None
        self._data["Outlet Branch 68 Name"] = None
        self._data["Outlet Branch 69 Name"] = None
        self._data["Outlet Branch 70 Name"] = None
        self._data["Outlet Branch 71 Name"] = None
        self._data["Outlet Branch 72 Name"] = None
        self._data["Outlet Branch 73 Name"] = None
        self._data["Outlet Branch 74 Name"] = None
        self._data["Outlet Branch 75 Name"] = None
        self._data["Outlet Branch 76 Name"] = None
        self._data["Outlet Branch 77 Name"] = None
        self._data["Outlet Branch 78 Name"] = None
        self._data["Outlet Branch 79 Name"] = None
        self._data["Outlet Branch 80 Name"] = None
        self._data["Outlet Branch 81 Name"] = None
        self._data["Outlet Branch 82 Name"] = None
        self._data["Outlet Branch 83 Name"] = None
        self._data["Outlet Branch 84 Name"] = None
        self._data["Outlet Branch 85 Name"] = None
        self._data["Outlet Branch 86 Name"] = None
        self._data["Outlet Branch 87 Name"] = None
        self._data["Outlet Branch 88 Name"] = None
        self._data["Outlet Branch 89 Name"] = None
        self._data["Outlet Branch 90 Name"] = None
        self._data["Outlet Branch 91 Name"] = None
        self._data["Outlet Branch 92 Name"] = None
        self._data["Outlet Branch 93 Name"] = None
        self._data["Outlet Branch 94 Name"] = None
        self._data["Outlet Branch 95 Name"] = None
        self._data["Outlet Branch 96 Name"] = None
        self._data["Outlet Branch 97 Name"] = None
        self._data["Outlet Branch 98 Name"] = None
        self._data["Outlet Branch 99 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None
        self._data["Outlet Branch 100 Name"] = None

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
            self.inlet_branch_name = None
        else:
            self.inlet_branch_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_1_name = None
        else:
            self.outlet_branch_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_2_name = None
        else:
            self.outlet_branch_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_3_name = None
        else:
            self.outlet_branch_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_4_name = None
        else:
            self.outlet_branch_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_5_name = None
        else:
            self.outlet_branch_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_6_name = None
        else:
            self.outlet_branch_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_7_name = None
        else:
            self.outlet_branch_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_8_name = None
        else:
            self.outlet_branch_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_9_name = None
        else:
            self.outlet_branch_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_10_name = None
        else:
            self.outlet_branch_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_11_name = None
        else:
            self.outlet_branch_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_12_name = None
        else:
            self.outlet_branch_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_13_name = None
        else:
            self.outlet_branch_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_14_name = None
        else:
            self.outlet_branch_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_15_name = None
        else:
            self.outlet_branch_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_16_name = None
        else:
            self.outlet_branch_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_17_name = None
        else:
            self.outlet_branch_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_18_name = None
        else:
            self.outlet_branch_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_19_name = None
        else:
            self.outlet_branch_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_20_name = None
        else:
            self.outlet_branch_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_21_name = None
        else:
            self.outlet_branch_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_22_name = None
        else:
            self.outlet_branch_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_23_name = None
        else:
            self.outlet_branch_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_24_name = None
        else:
            self.outlet_branch_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_25_name = None
        else:
            self.outlet_branch_25_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_26_name = None
        else:
            self.outlet_branch_26_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_27_name = None
        else:
            self.outlet_branch_27_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_28_name = None
        else:
            self.outlet_branch_28_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_29_name = None
        else:
            self.outlet_branch_29_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_30_name = None
        else:
            self.outlet_branch_30_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_31_name = None
        else:
            self.outlet_branch_31_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_32_name = None
        else:
            self.outlet_branch_32_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_33_name = None
        else:
            self.outlet_branch_33_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_34_name = None
        else:
            self.outlet_branch_34_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_35_name = None
        else:
            self.outlet_branch_35_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_36_name = None
        else:
            self.outlet_branch_36_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_37_name = None
        else:
            self.outlet_branch_37_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_38_name = None
        else:
            self.outlet_branch_38_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_39_name = None
        else:
            self.outlet_branch_39_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_40_name = None
        else:
            self.outlet_branch_40_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_41_name = None
        else:
            self.outlet_branch_41_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_42_name = None
        else:
            self.outlet_branch_42_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_43_name = None
        else:
            self.outlet_branch_43_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_44_name = None
        else:
            self.outlet_branch_44_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_45_name = None
        else:
            self.outlet_branch_45_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_46_name = None
        else:
            self.outlet_branch_46_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_47_name = None
        else:
            self.outlet_branch_47_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_48_name = None
        else:
            self.outlet_branch_48_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_49_name = None
        else:
            self.outlet_branch_49_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_50_name = None
        else:
            self.outlet_branch_50_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_51_name = None
        else:
            self.outlet_branch_51_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_52_name = None
        else:
            self.outlet_branch_52_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_53_name = None
        else:
            self.outlet_branch_53_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_54_name = None
        else:
            self.outlet_branch_54_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_55_name = None
        else:
            self.outlet_branch_55_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_56_name = None
        else:
            self.outlet_branch_56_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_57_name = None
        else:
            self.outlet_branch_57_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_58_name = None
        else:
            self.outlet_branch_58_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_59_name = None
        else:
            self.outlet_branch_59_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_60_name = None
        else:
            self.outlet_branch_60_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_61_name = None
        else:
            self.outlet_branch_61_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_62_name = None
        else:
            self.outlet_branch_62_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_63_name = None
        else:
            self.outlet_branch_63_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_64_name = None
        else:
            self.outlet_branch_64_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_65_name = None
        else:
            self.outlet_branch_65_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_66_name = None
        else:
            self.outlet_branch_66_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_67_name = None
        else:
            self.outlet_branch_67_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_68_name = None
        else:
            self.outlet_branch_68_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_69_name = None
        else:
            self.outlet_branch_69_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_70_name = None
        else:
            self.outlet_branch_70_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_71_name = None
        else:
            self.outlet_branch_71_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_72_name = None
        else:
            self.outlet_branch_72_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_73_name = None
        else:
            self.outlet_branch_73_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_74_name = None
        else:
            self.outlet_branch_74_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_75_name = None
        else:
            self.outlet_branch_75_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_76_name = None
        else:
            self.outlet_branch_76_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_77_name = None
        else:
            self.outlet_branch_77_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_78_name = None
        else:
            self.outlet_branch_78_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_79_name = None
        else:
            self.outlet_branch_79_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_80_name = None
        else:
            self.outlet_branch_80_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_81_name = None
        else:
            self.outlet_branch_81_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_82_name = None
        else:
            self.outlet_branch_82_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_83_name = None
        else:
            self.outlet_branch_83_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_84_name = None
        else:
            self.outlet_branch_84_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_85_name = None
        else:
            self.outlet_branch_85_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_86_name = None
        else:
            self.outlet_branch_86_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_87_name = None
        else:
            self.outlet_branch_87_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_88_name = None
        else:
            self.outlet_branch_88_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_89_name = None
        else:
            self.outlet_branch_89_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_90_name = None
        else:
            self.outlet_branch_90_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_91_name = None
        else:
            self.outlet_branch_91_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_92_name = None
        else:
            self.outlet_branch_92_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_93_name = None
        else:
            self.outlet_branch_93_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_94_name = None
        else:
            self.outlet_branch_94_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_95_name = None
        else:
            self.outlet_branch_95_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_96_name = None
        else:
            self.outlet_branch_96_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_97_name = None
        else:
            self.outlet_branch_97_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_98_name = None
        else:
            self.outlet_branch_98_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_99_name = None
        else:
            self.outlet_branch_99_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_branch_100_name = None
        else:
            self.outlet_branch_100_name = vals[i]
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
    def inlet_branch_name(self):
        """Get inlet_branch_name

        Returns:
            str: the value of `inlet_branch_name` or None if not set
        """
        return self._data["Inlet Branch Name"]

    @inlet_branch_name.setter
    def inlet_branch_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_name`

        Args:
            value (str): value for IDD Field `inlet_branch_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_name`')

        self._data["Inlet Branch Name"] = value

    @property
    def outlet_branch_1_name(self):
        """Get outlet_branch_1_name

        Returns:
            str: the value of `outlet_branch_1_name` or None if not set
        """
        return self._data["Outlet Branch 1 Name"]

    @outlet_branch_1_name.setter
    def outlet_branch_1_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_1_name`

        Args:
            value (str): value for IDD Field `outlet_branch_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_1_name`')

        self._data["Outlet Branch 1 Name"] = value

    @property
    def outlet_branch_2_name(self):
        """Get outlet_branch_2_name

        Returns:
            str: the value of `outlet_branch_2_name` or None if not set
        """
        return self._data["Outlet Branch 2 Name"]

    @outlet_branch_2_name.setter
    def outlet_branch_2_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_2_name`

        Args:
            value (str): value for IDD Field `outlet_branch_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_2_name`')

        self._data["Outlet Branch 2 Name"] = value

    @property
    def outlet_branch_3_name(self):
        """Get outlet_branch_3_name

        Returns:
            str: the value of `outlet_branch_3_name` or None if not set
        """
        return self._data["Outlet Branch 3 Name"]

    @outlet_branch_3_name.setter
    def outlet_branch_3_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_3_name`

        Args:
            value (str): value for IDD Field `outlet_branch_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_3_name`')

        self._data["Outlet Branch 3 Name"] = value

    @property
    def outlet_branch_4_name(self):
        """Get outlet_branch_4_name

        Returns:
            str: the value of `outlet_branch_4_name` or None if not set
        """
        return self._data["Outlet Branch 4 Name"]

    @outlet_branch_4_name.setter
    def outlet_branch_4_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_4_name`

        Args:
            value (str): value for IDD Field `outlet_branch_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_4_name`')

        self._data["Outlet Branch 4 Name"] = value

    @property
    def outlet_branch_5_name(self):
        """Get outlet_branch_5_name

        Returns:
            str: the value of `outlet_branch_5_name` or None if not set
        """
        return self._data["Outlet Branch 5 Name"]

    @outlet_branch_5_name.setter
    def outlet_branch_5_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_5_name`

        Args:
            value (str): value for IDD Field `outlet_branch_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_5_name`')

        self._data["Outlet Branch 5 Name"] = value

    @property
    def outlet_branch_6_name(self):
        """Get outlet_branch_6_name

        Returns:
            str: the value of `outlet_branch_6_name` or None if not set
        """
        return self._data["Outlet Branch 6 Name"]

    @outlet_branch_6_name.setter
    def outlet_branch_6_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_6_name`

        Args:
            value (str): value for IDD Field `outlet_branch_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_6_name`')

        self._data["Outlet Branch 6 Name"] = value

    @property
    def outlet_branch_7_name(self):
        """Get outlet_branch_7_name

        Returns:
            str: the value of `outlet_branch_7_name` or None if not set
        """
        return self._data["Outlet Branch 7 Name"]

    @outlet_branch_7_name.setter
    def outlet_branch_7_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_7_name`

        Args:
            value (str): value for IDD Field `outlet_branch_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_7_name`')

        self._data["Outlet Branch 7 Name"] = value

    @property
    def outlet_branch_8_name(self):
        """Get outlet_branch_8_name

        Returns:
            str: the value of `outlet_branch_8_name` or None if not set
        """
        return self._data["Outlet Branch 8 Name"]

    @outlet_branch_8_name.setter
    def outlet_branch_8_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_8_name`

        Args:
            value (str): value for IDD Field `outlet_branch_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_8_name`')

        self._data["Outlet Branch 8 Name"] = value

    @property
    def outlet_branch_9_name(self):
        """Get outlet_branch_9_name

        Returns:
            str: the value of `outlet_branch_9_name` or None if not set
        """
        return self._data["Outlet Branch 9 Name"]

    @outlet_branch_9_name.setter
    def outlet_branch_9_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_9_name`

        Args:
            value (str): value for IDD Field `outlet_branch_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_9_name`')

        self._data["Outlet Branch 9 Name"] = value

    @property
    def outlet_branch_10_name(self):
        """Get outlet_branch_10_name

        Returns:
            str: the value of `outlet_branch_10_name` or None if not set
        """
        return self._data["Outlet Branch 10 Name"]

    @outlet_branch_10_name.setter
    def outlet_branch_10_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_10_name`

        Args:
            value (str): value for IDD Field `outlet_branch_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_10_name`')

        self._data["Outlet Branch 10 Name"] = value

    @property
    def outlet_branch_11_name(self):
        """Get outlet_branch_11_name

        Returns:
            str: the value of `outlet_branch_11_name` or None if not set
        """
        return self._data["Outlet Branch 11 Name"]

    @outlet_branch_11_name.setter
    def outlet_branch_11_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_11_name`

        Args:
            value (str): value for IDD Field `outlet_branch_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_11_name`')

        self._data["Outlet Branch 11 Name"] = value

    @property
    def outlet_branch_12_name(self):
        """Get outlet_branch_12_name

        Returns:
            str: the value of `outlet_branch_12_name` or None if not set
        """
        return self._data["Outlet Branch 12 Name"]

    @outlet_branch_12_name.setter
    def outlet_branch_12_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_12_name`

        Args:
            value (str): value for IDD Field `outlet_branch_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_12_name`')

        self._data["Outlet Branch 12 Name"] = value

    @property
    def outlet_branch_13_name(self):
        """Get outlet_branch_13_name

        Returns:
            str: the value of `outlet_branch_13_name` or None if not set
        """
        return self._data["Outlet Branch 13 Name"]

    @outlet_branch_13_name.setter
    def outlet_branch_13_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_13_name`

        Args:
            value (str): value for IDD Field `outlet_branch_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_13_name`')

        self._data["Outlet Branch 13 Name"] = value

    @property
    def outlet_branch_14_name(self):
        """Get outlet_branch_14_name

        Returns:
            str: the value of `outlet_branch_14_name` or None if not set
        """
        return self._data["Outlet Branch 14 Name"]

    @outlet_branch_14_name.setter
    def outlet_branch_14_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_14_name`

        Args:
            value (str): value for IDD Field `outlet_branch_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_14_name`')

        self._data["Outlet Branch 14 Name"] = value

    @property
    def outlet_branch_15_name(self):
        """Get outlet_branch_15_name

        Returns:
            str: the value of `outlet_branch_15_name` or None if not set
        """
        return self._data["Outlet Branch 15 Name"]

    @outlet_branch_15_name.setter
    def outlet_branch_15_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_15_name`

        Args:
            value (str): value for IDD Field `outlet_branch_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_15_name`')

        self._data["Outlet Branch 15 Name"] = value

    @property
    def outlet_branch_16_name(self):
        """Get outlet_branch_16_name

        Returns:
            str: the value of `outlet_branch_16_name` or None if not set
        """
        return self._data["Outlet Branch 16 Name"]

    @outlet_branch_16_name.setter
    def outlet_branch_16_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_16_name`

        Args:
            value (str): value for IDD Field `outlet_branch_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_16_name`')

        self._data["Outlet Branch 16 Name"] = value

    @property
    def outlet_branch_17_name(self):
        """Get outlet_branch_17_name

        Returns:
            str: the value of `outlet_branch_17_name` or None if not set
        """
        return self._data["Outlet Branch 17 Name"]

    @outlet_branch_17_name.setter
    def outlet_branch_17_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_17_name`

        Args:
            value (str): value for IDD Field `outlet_branch_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_17_name`')

        self._data["Outlet Branch 17 Name"] = value

    @property
    def outlet_branch_18_name(self):
        """Get outlet_branch_18_name

        Returns:
            str: the value of `outlet_branch_18_name` or None if not set
        """
        return self._data["Outlet Branch 18 Name"]

    @outlet_branch_18_name.setter
    def outlet_branch_18_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_18_name`

        Args:
            value (str): value for IDD Field `outlet_branch_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_18_name`')

        self._data["Outlet Branch 18 Name"] = value

    @property
    def outlet_branch_19_name(self):
        """Get outlet_branch_19_name

        Returns:
            str: the value of `outlet_branch_19_name` or None if not set
        """
        return self._data["Outlet Branch 19 Name"]

    @outlet_branch_19_name.setter
    def outlet_branch_19_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_19_name`

        Args:
            value (str): value for IDD Field `outlet_branch_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_19_name`')

        self._data["Outlet Branch 19 Name"] = value

    @property
    def outlet_branch_20_name(self):
        """Get outlet_branch_20_name

        Returns:
            str: the value of `outlet_branch_20_name` or None if not set
        """
        return self._data["Outlet Branch 20 Name"]

    @outlet_branch_20_name.setter
    def outlet_branch_20_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_20_name`

        Args:
            value (str): value for IDD Field `outlet_branch_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_20_name`')

        self._data["Outlet Branch 20 Name"] = value

    @property
    def outlet_branch_21_name(self):
        """Get outlet_branch_21_name

        Returns:
            str: the value of `outlet_branch_21_name` or None if not set
        """
        return self._data["Outlet Branch 21 Name"]

    @outlet_branch_21_name.setter
    def outlet_branch_21_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_21_name`

        Args:
            value (str): value for IDD Field `outlet_branch_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_21_name`')

        self._data["Outlet Branch 21 Name"] = value

    @property
    def outlet_branch_22_name(self):
        """Get outlet_branch_22_name

        Returns:
            str: the value of `outlet_branch_22_name` or None if not set
        """
        return self._data["Outlet Branch 22 Name"]

    @outlet_branch_22_name.setter
    def outlet_branch_22_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_22_name`

        Args:
            value (str): value for IDD Field `outlet_branch_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_22_name`')

        self._data["Outlet Branch 22 Name"] = value

    @property
    def outlet_branch_23_name(self):
        """Get outlet_branch_23_name

        Returns:
            str: the value of `outlet_branch_23_name` or None if not set
        """
        return self._data["Outlet Branch 23 Name"]

    @outlet_branch_23_name.setter
    def outlet_branch_23_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_23_name`

        Args:
            value (str): value for IDD Field `outlet_branch_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_23_name`')

        self._data["Outlet Branch 23 Name"] = value

    @property
    def outlet_branch_24_name(self):
        """Get outlet_branch_24_name

        Returns:
            str: the value of `outlet_branch_24_name` or None if not set
        """
        return self._data["Outlet Branch 24 Name"]

    @outlet_branch_24_name.setter
    def outlet_branch_24_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_24_name`

        Args:
            value (str): value for IDD Field `outlet_branch_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_24_name`')

        self._data["Outlet Branch 24 Name"] = value

    @property
    def outlet_branch_25_name(self):
        """Get outlet_branch_25_name

        Returns:
            str: the value of `outlet_branch_25_name` or None if not set
        """
        return self._data["Outlet Branch 25 Name"]

    @outlet_branch_25_name.setter
    def outlet_branch_25_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_25_name`

        Args:
            value (str): value for IDD Field `outlet_branch_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_25_name`')

        self._data["Outlet Branch 25 Name"] = value

    @property
    def outlet_branch_26_name(self):
        """Get outlet_branch_26_name

        Returns:
            str: the value of `outlet_branch_26_name` or None if not set
        """
        return self._data["Outlet Branch 26 Name"]

    @outlet_branch_26_name.setter
    def outlet_branch_26_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_26_name`

        Args:
            value (str): value for IDD Field `outlet_branch_26_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_26_name`')

        self._data["Outlet Branch 26 Name"] = value

    @property
    def outlet_branch_27_name(self):
        """Get outlet_branch_27_name

        Returns:
            str: the value of `outlet_branch_27_name` or None if not set
        """
        return self._data["Outlet Branch 27 Name"]

    @outlet_branch_27_name.setter
    def outlet_branch_27_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_27_name`

        Args:
            value (str): value for IDD Field `outlet_branch_27_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_27_name`')

        self._data["Outlet Branch 27 Name"] = value

    @property
    def outlet_branch_28_name(self):
        """Get outlet_branch_28_name

        Returns:
            str: the value of `outlet_branch_28_name` or None if not set
        """
        return self._data["Outlet Branch 28 Name"]

    @outlet_branch_28_name.setter
    def outlet_branch_28_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_28_name`

        Args:
            value (str): value for IDD Field `outlet_branch_28_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_28_name`')

        self._data["Outlet Branch 28 Name"] = value

    @property
    def outlet_branch_29_name(self):
        """Get outlet_branch_29_name

        Returns:
            str: the value of `outlet_branch_29_name` or None if not set
        """
        return self._data["Outlet Branch 29 Name"]

    @outlet_branch_29_name.setter
    def outlet_branch_29_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_29_name`

        Args:
            value (str): value for IDD Field `outlet_branch_29_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_29_name`')

        self._data["Outlet Branch 29 Name"] = value

    @property
    def outlet_branch_30_name(self):
        """Get outlet_branch_30_name

        Returns:
            str: the value of `outlet_branch_30_name` or None if not set
        """
        return self._data["Outlet Branch 30 Name"]

    @outlet_branch_30_name.setter
    def outlet_branch_30_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_30_name`

        Args:
            value (str): value for IDD Field `outlet_branch_30_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_30_name`')

        self._data["Outlet Branch 30 Name"] = value

    @property
    def outlet_branch_31_name(self):
        """Get outlet_branch_31_name

        Returns:
            str: the value of `outlet_branch_31_name` or None if not set
        """
        return self._data["Outlet Branch 31 Name"]

    @outlet_branch_31_name.setter
    def outlet_branch_31_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_31_name`

        Args:
            value (str): value for IDD Field `outlet_branch_31_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_31_name`')

        self._data["Outlet Branch 31 Name"] = value

    @property
    def outlet_branch_32_name(self):
        """Get outlet_branch_32_name

        Returns:
            str: the value of `outlet_branch_32_name` or None if not set
        """
        return self._data["Outlet Branch 32 Name"]

    @outlet_branch_32_name.setter
    def outlet_branch_32_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_32_name`

        Args:
            value (str): value for IDD Field `outlet_branch_32_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_32_name`')

        self._data["Outlet Branch 32 Name"] = value

    @property
    def outlet_branch_33_name(self):
        """Get outlet_branch_33_name

        Returns:
            str: the value of `outlet_branch_33_name` or None if not set
        """
        return self._data["Outlet Branch 33 Name"]

    @outlet_branch_33_name.setter
    def outlet_branch_33_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_33_name`

        Args:
            value (str): value for IDD Field `outlet_branch_33_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_33_name`')

        self._data["Outlet Branch 33 Name"] = value

    @property
    def outlet_branch_34_name(self):
        """Get outlet_branch_34_name

        Returns:
            str: the value of `outlet_branch_34_name` or None if not set
        """
        return self._data["Outlet Branch 34 Name"]

    @outlet_branch_34_name.setter
    def outlet_branch_34_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_34_name`

        Args:
            value (str): value for IDD Field `outlet_branch_34_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_34_name`')

        self._data["Outlet Branch 34 Name"] = value

    @property
    def outlet_branch_35_name(self):
        """Get outlet_branch_35_name

        Returns:
            str: the value of `outlet_branch_35_name` or None if not set
        """
        return self._data["Outlet Branch 35 Name"]

    @outlet_branch_35_name.setter
    def outlet_branch_35_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_35_name`

        Args:
            value (str): value for IDD Field `outlet_branch_35_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_35_name`')

        self._data["Outlet Branch 35 Name"] = value

    @property
    def outlet_branch_36_name(self):
        """Get outlet_branch_36_name

        Returns:
            str: the value of `outlet_branch_36_name` or None if not set
        """
        return self._data["Outlet Branch 36 Name"]

    @outlet_branch_36_name.setter
    def outlet_branch_36_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_36_name`

        Args:
            value (str): value for IDD Field `outlet_branch_36_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_36_name`')

        self._data["Outlet Branch 36 Name"] = value

    @property
    def outlet_branch_37_name(self):
        """Get outlet_branch_37_name

        Returns:
            str: the value of `outlet_branch_37_name` or None if not set
        """
        return self._data["Outlet Branch 37 Name"]

    @outlet_branch_37_name.setter
    def outlet_branch_37_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_37_name`

        Args:
            value (str): value for IDD Field `outlet_branch_37_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_37_name`')

        self._data["Outlet Branch 37 Name"] = value

    @property
    def outlet_branch_38_name(self):
        """Get outlet_branch_38_name

        Returns:
            str: the value of `outlet_branch_38_name` or None if not set
        """
        return self._data["Outlet Branch 38 Name"]

    @outlet_branch_38_name.setter
    def outlet_branch_38_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_38_name`

        Args:
            value (str): value for IDD Field `outlet_branch_38_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_38_name`')

        self._data["Outlet Branch 38 Name"] = value

    @property
    def outlet_branch_39_name(self):
        """Get outlet_branch_39_name

        Returns:
            str: the value of `outlet_branch_39_name` or None if not set
        """
        return self._data["Outlet Branch 39 Name"]

    @outlet_branch_39_name.setter
    def outlet_branch_39_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_39_name`

        Args:
            value (str): value for IDD Field `outlet_branch_39_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_39_name`')

        self._data["Outlet Branch 39 Name"] = value

    @property
    def outlet_branch_40_name(self):
        """Get outlet_branch_40_name

        Returns:
            str: the value of `outlet_branch_40_name` or None if not set
        """
        return self._data["Outlet Branch 40 Name"]

    @outlet_branch_40_name.setter
    def outlet_branch_40_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_40_name`

        Args:
            value (str): value for IDD Field `outlet_branch_40_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_40_name`')

        self._data["Outlet Branch 40 Name"] = value

    @property
    def outlet_branch_41_name(self):
        """Get outlet_branch_41_name

        Returns:
            str: the value of `outlet_branch_41_name` or None if not set
        """
        return self._data["Outlet Branch 41 Name"]

    @outlet_branch_41_name.setter
    def outlet_branch_41_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_41_name`

        Args:
            value (str): value for IDD Field `outlet_branch_41_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_41_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_41_name`')

        self._data["Outlet Branch 41 Name"] = value

    @property
    def outlet_branch_42_name(self):
        """Get outlet_branch_42_name

        Returns:
            str: the value of `outlet_branch_42_name` or None if not set
        """
        return self._data["Outlet Branch 42 Name"]

    @outlet_branch_42_name.setter
    def outlet_branch_42_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_42_name`

        Args:
            value (str): value for IDD Field `outlet_branch_42_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_42_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_42_name`')

        self._data["Outlet Branch 42 Name"] = value

    @property
    def outlet_branch_43_name(self):
        """Get outlet_branch_43_name

        Returns:
            str: the value of `outlet_branch_43_name` or None if not set
        """
        return self._data["Outlet Branch 43 Name"]

    @outlet_branch_43_name.setter
    def outlet_branch_43_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_43_name`

        Args:
            value (str): value for IDD Field `outlet_branch_43_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_43_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_43_name`')

        self._data["Outlet Branch 43 Name"] = value

    @property
    def outlet_branch_44_name(self):
        """Get outlet_branch_44_name

        Returns:
            str: the value of `outlet_branch_44_name` or None if not set
        """
        return self._data["Outlet Branch 44 Name"]

    @outlet_branch_44_name.setter
    def outlet_branch_44_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_44_name`

        Args:
            value (str): value for IDD Field `outlet_branch_44_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_44_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_44_name`')

        self._data["Outlet Branch 44 Name"] = value

    @property
    def outlet_branch_45_name(self):
        """Get outlet_branch_45_name

        Returns:
            str: the value of `outlet_branch_45_name` or None if not set
        """
        return self._data["Outlet Branch 45 Name"]

    @outlet_branch_45_name.setter
    def outlet_branch_45_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_45_name`

        Args:
            value (str): value for IDD Field `outlet_branch_45_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_45_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_45_name`')

        self._data["Outlet Branch 45 Name"] = value

    @property
    def outlet_branch_46_name(self):
        """Get outlet_branch_46_name

        Returns:
            str: the value of `outlet_branch_46_name` or None if not set
        """
        return self._data["Outlet Branch 46 Name"]

    @outlet_branch_46_name.setter
    def outlet_branch_46_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_46_name`

        Args:
            value (str): value for IDD Field `outlet_branch_46_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_46_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_46_name`')

        self._data["Outlet Branch 46 Name"] = value

    @property
    def outlet_branch_47_name(self):
        """Get outlet_branch_47_name

        Returns:
            str: the value of `outlet_branch_47_name` or None if not set
        """
        return self._data["Outlet Branch 47 Name"]

    @outlet_branch_47_name.setter
    def outlet_branch_47_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_47_name`

        Args:
            value (str): value for IDD Field `outlet_branch_47_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_47_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_47_name`')

        self._data["Outlet Branch 47 Name"] = value

    @property
    def outlet_branch_48_name(self):
        """Get outlet_branch_48_name

        Returns:
            str: the value of `outlet_branch_48_name` or None if not set
        """
        return self._data["Outlet Branch 48 Name"]

    @outlet_branch_48_name.setter
    def outlet_branch_48_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_48_name`

        Args:
            value (str): value for IDD Field `outlet_branch_48_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_48_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_48_name`')

        self._data["Outlet Branch 48 Name"] = value

    @property
    def outlet_branch_49_name(self):
        """Get outlet_branch_49_name

        Returns:
            str: the value of `outlet_branch_49_name` or None if not set
        """
        return self._data["Outlet Branch 49 Name"]

    @outlet_branch_49_name.setter
    def outlet_branch_49_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_49_name`

        Args:
            value (str): value for IDD Field `outlet_branch_49_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_49_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_49_name`')

        self._data["Outlet Branch 49 Name"] = value

    @property
    def outlet_branch_50_name(self):
        """Get outlet_branch_50_name

        Returns:
            str: the value of `outlet_branch_50_name` or None if not set
        """
        return self._data["Outlet Branch 50 Name"]

    @outlet_branch_50_name.setter
    def outlet_branch_50_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_50_name`

        Args:
            value (str): value for IDD Field `outlet_branch_50_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_50_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_50_name`')

        self._data["Outlet Branch 50 Name"] = value

    @property
    def outlet_branch_51_name(self):
        """Get outlet_branch_51_name

        Returns:
            str: the value of `outlet_branch_51_name` or None if not set
        """
        return self._data["Outlet Branch 51 Name"]

    @outlet_branch_51_name.setter
    def outlet_branch_51_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_51_name`

        Args:
            value (str): value for IDD Field `outlet_branch_51_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_51_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_51_name`')

        self._data["Outlet Branch 51 Name"] = value

    @property
    def outlet_branch_52_name(self):
        """Get outlet_branch_52_name

        Returns:
            str: the value of `outlet_branch_52_name` or None if not set
        """
        return self._data["Outlet Branch 52 Name"]

    @outlet_branch_52_name.setter
    def outlet_branch_52_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_52_name`

        Args:
            value (str): value for IDD Field `outlet_branch_52_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_52_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_52_name`')

        self._data["Outlet Branch 52 Name"] = value

    @property
    def outlet_branch_53_name(self):
        """Get outlet_branch_53_name

        Returns:
            str: the value of `outlet_branch_53_name` or None if not set
        """
        return self._data["Outlet Branch 53 Name"]

    @outlet_branch_53_name.setter
    def outlet_branch_53_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_53_name`

        Args:
            value (str): value for IDD Field `outlet_branch_53_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_53_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_53_name`')

        self._data["Outlet Branch 53 Name"] = value

    @property
    def outlet_branch_54_name(self):
        """Get outlet_branch_54_name

        Returns:
            str: the value of `outlet_branch_54_name` or None if not set
        """
        return self._data["Outlet Branch 54 Name"]

    @outlet_branch_54_name.setter
    def outlet_branch_54_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_54_name`

        Args:
            value (str): value for IDD Field `outlet_branch_54_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_54_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_54_name`')

        self._data["Outlet Branch 54 Name"] = value

    @property
    def outlet_branch_55_name(self):
        """Get outlet_branch_55_name

        Returns:
            str: the value of `outlet_branch_55_name` or None if not set
        """
        return self._data["Outlet Branch 55 Name"]

    @outlet_branch_55_name.setter
    def outlet_branch_55_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_55_name`

        Args:
            value (str): value for IDD Field `outlet_branch_55_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_55_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_55_name`')

        self._data["Outlet Branch 55 Name"] = value

    @property
    def outlet_branch_56_name(self):
        """Get outlet_branch_56_name

        Returns:
            str: the value of `outlet_branch_56_name` or None if not set
        """
        return self._data["Outlet Branch 56 Name"]

    @outlet_branch_56_name.setter
    def outlet_branch_56_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_56_name`

        Args:
            value (str): value for IDD Field `outlet_branch_56_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_56_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_56_name`')

        self._data["Outlet Branch 56 Name"] = value

    @property
    def outlet_branch_57_name(self):
        """Get outlet_branch_57_name

        Returns:
            str: the value of `outlet_branch_57_name` or None if not set
        """
        return self._data["Outlet Branch 57 Name"]

    @outlet_branch_57_name.setter
    def outlet_branch_57_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_57_name`

        Args:
            value (str): value for IDD Field `outlet_branch_57_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_57_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_57_name`')

        self._data["Outlet Branch 57 Name"] = value

    @property
    def outlet_branch_58_name(self):
        """Get outlet_branch_58_name

        Returns:
            str: the value of `outlet_branch_58_name` or None if not set
        """
        return self._data["Outlet Branch 58 Name"]

    @outlet_branch_58_name.setter
    def outlet_branch_58_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_58_name`

        Args:
            value (str): value for IDD Field `outlet_branch_58_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_58_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_58_name`')

        self._data["Outlet Branch 58 Name"] = value

    @property
    def outlet_branch_59_name(self):
        """Get outlet_branch_59_name

        Returns:
            str: the value of `outlet_branch_59_name` or None if not set
        """
        return self._data["Outlet Branch 59 Name"]

    @outlet_branch_59_name.setter
    def outlet_branch_59_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_59_name`

        Args:
            value (str): value for IDD Field `outlet_branch_59_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_59_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_59_name`')

        self._data["Outlet Branch 59 Name"] = value

    @property
    def outlet_branch_60_name(self):
        """Get outlet_branch_60_name

        Returns:
            str: the value of `outlet_branch_60_name` or None if not set
        """
        return self._data["Outlet Branch 60 Name"]

    @outlet_branch_60_name.setter
    def outlet_branch_60_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_60_name`

        Args:
            value (str): value for IDD Field `outlet_branch_60_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_60_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_60_name`')

        self._data["Outlet Branch 60 Name"] = value

    @property
    def outlet_branch_61_name(self):
        """Get outlet_branch_61_name

        Returns:
            str: the value of `outlet_branch_61_name` or None if not set
        """
        return self._data["Outlet Branch 61 Name"]

    @outlet_branch_61_name.setter
    def outlet_branch_61_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_61_name`

        Args:
            value (str): value for IDD Field `outlet_branch_61_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_61_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_61_name`')

        self._data["Outlet Branch 61 Name"] = value

    @property
    def outlet_branch_62_name(self):
        """Get outlet_branch_62_name

        Returns:
            str: the value of `outlet_branch_62_name` or None if not set
        """
        return self._data["Outlet Branch 62 Name"]

    @outlet_branch_62_name.setter
    def outlet_branch_62_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_62_name`

        Args:
            value (str): value for IDD Field `outlet_branch_62_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_62_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_62_name`')

        self._data["Outlet Branch 62 Name"] = value

    @property
    def outlet_branch_63_name(self):
        """Get outlet_branch_63_name

        Returns:
            str: the value of `outlet_branch_63_name` or None if not set
        """
        return self._data["Outlet Branch 63 Name"]

    @outlet_branch_63_name.setter
    def outlet_branch_63_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_63_name`

        Args:
            value (str): value for IDD Field `outlet_branch_63_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_63_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_63_name`')

        self._data["Outlet Branch 63 Name"] = value

    @property
    def outlet_branch_64_name(self):
        """Get outlet_branch_64_name

        Returns:
            str: the value of `outlet_branch_64_name` or None if not set
        """
        return self._data["Outlet Branch 64 Name"]

    @outlet_branch_64_name.setter
    def outlet_branch_64_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_64_name`

        Args:
            value (str): value for IDD Field `outlet_branch_64_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_64_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_64_name`')

        self._data["Outlet Branch 64 Name"] = value

    @property
    def outlet_branch_65_name(self):
        """Get outlet_branch_65_name

        Returns:
            str: the value of `outlet_branch_65_name` or None if not set
        """
        return self._data["Outlet Branch 65 Name"]

    @outlet_branch_65_name.setter
    def outlet_branch_65_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_65_name`

        Args:
            value (str): value for IDD Field `outlet_branch_65_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_65_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_65_name`')

        self._data["Outlet Branch 65 Name"] = value

    @property
    def outlet_branch_66_name(self):
        """Get outlet_branch_66_name

        Returns:
            str: the value of `outlet_branch_66_name` or None if not set
        """
        return self._data["Outlet Branch 66 Name"]

    @outlet_branch_66_name.setter
    def outlet_branch_66_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_66_name`

        Args:
            value (str): value for IDD Field `outlet_branch_66_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_66_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_66_name`')

        self._data["Outlet Branch 66 Name"] = value

    @property
    def outlet_branch_67_name(self):
        """Get outlet_branch_67_name

        Returns:
            str: the value of `outlet_branch_67_name` or None if not set
        """
        return self._data["Outlet Branch 67 Name"]

    @outlet_branch_67_name.setter
    def outlet_branch_67_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_67_name`

        Args:
            value (str): value for IDD Field `outlet_branch_67_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_67_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_67_name`')

        self._data["Outlet Branch 67 Name"] = value

    @property
    def outlet_branch_68_name(self):
        """Get outlet_branch_68_name

        Returns:
            str: the value of `outlet_branch_68_name` or None if not set
        """
        return self._data["Outlet Branch 68 Name"]

    @outlet_branch_68_name.setter
    def outlet_branch_68_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_68_name`

        Args:
            value (str): value for IDD Field `outlet_branch_68_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_68_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_68_name`')

        self._data["Outlet Branch 68 Name"] = value

    @property
    def outlet_branch_69_name(self):
        """Get outlet_branch_69_name

        Returns:
            str: the value of `outlet_branch_69_name` or None if not set
        """
        return self._data["Outlet Branch 69 Name"]

    @outlet_branch_69_name.setter
    def outlet_branch_69_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_69_name`

        Args:
            value (str): value for IDD Field `outlet_branch_69_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_69_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_69_name`')

        self._data["Outlet Branch 69 Name"] = value

    @property
    def outlet_branch_70_name(self):
        """Get outlet_branch_70_name

        Returns:
            str: the value of `outlet_branch_70_name` or None if not set
        """
        return self._data["Outlet Branch 70 Name"]

    @outlet_branch_70_name.setter
    def outlet_branch_70_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_70_name`

        Args:
            value (str): value for IDD Field `outlet_branch_70_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_70_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_70_name`')

        self._data["Outlet Branch 70 Name"] = value

    @property
    def outlet_branch_71_name(self):
        """Get outlet_branch_71_name

        Returns:
            str: the value of `outlet_branch_71_name` or None if not set
        """
        return self._data["Outlet Branch 71 Name"]

    @outlet_branch_71_name.setter
    def outlet_branch_71_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_71_name`

        Args:
            value (str): value for IDD Field `outlet_branch_71_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_71_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_71_name`')

        self._data["Outlet Branch 71 Name"] = value

    @property
    def outlet_branch_72_name(self):
        """Get outlet_branch_72_name

        Returns:
            str: the value of `outlet_branch_72_name` or None if not set
        """
        return self._data["Outlet Branch 72 Name"]

    @outlet_branch_72_name.setter
    def outlet_branch_72_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_72_name`

        Args:
            value (str): value for IDD Field `outlet_branch_72_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_72_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_72_name`')

        self._data["Outlet Branch 72 Name"] = value

    @property
    def outlet_branch_73_name(self):
        """Get outlet_branch_73_name

        Returns:
            str: the value of `outlet_branch_73_name` or None if not set
        """
        return self._data["Outlet Branch 73 Name"]

    @outlet_branch_73_name.setter
    def outlet_branch_73_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_73_name`

        Args:
            value (str): value for IDD Field `outlet_branch_73_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_73_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_73_name`')

        self._data["Outlet Branch 73 Name"] = value

    @property
    def outlet_branch_74_name(self):
        """Get outlet_branch_74_name

        Returns:
            str: the value of `outlet_branch_74_name` or None if not set
        """
        return self._data["Outlet Branch 74 Name"]

    @outlet_branch_74_name.setter
    def outlet_branch_74_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_74_name`

        Args:
            value (str): value for IDD Field `outlet_branch_74_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_74_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_74_name`')

        self._data["Outlet Branch 74 Name"] = value

    @property
    def outlet_branch_75_name(self):
        """Get outlet_branch_75_name

        Returns:
            str: the value of `outlet_branch_75_name` or None if not set
        """
        return self._data["Outlet Branch 75 Name"]

    @outlet_branch_75_name.setter
    def outlet_branch_75_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_75_name`

        Args:
            value (str): value for IDD Field `outlet_branch_75_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_75_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_75_name`')

        self._data["Outlet Branch 75 Name"] = value

    @property
    def outlet_branch_76_name(self):
        """Get outlet_branch_76_name

        Returns:
            str: the value of `outlet_branch_76_name` or None if not set
        """
        return self._data["Outlet Branch 76 Name"]

    @outlet_branch_76_name.setter
    def outlet_branch_76_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_76_name`

        Args:
            value (str): value for IDD Field `outlet_branch_76_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_76_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_76_name`')

        self._data["Outlet Branch 76 Name"] = value

    @property
    def outlet_branch_77_name(self):
        """Get outlet_branch_77_name

        Returns:
            str: the value of `outlet_branch_77_name` or None if not set
        """
        return self._data["Outlet Branch 77 Name"]

    @outlet_branch_77_name.setter
    def outlet_branch_77_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_77_name`

        Args:
            value (str): value for IDD Field `outlet_branch_77_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_77_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_77_name`')

        self._data["Outlet Branch 77 Name"] = value

    @property
    def outlet_branch_78_name(self):
        """Get outlet_branch_78_name

        Returns:
            str: the value of `outlet_branch_78_name` or None if not set
        """
        return self._data["Outlet Branch 78 Name"]

    @outlet_branch_78_name.setter
    def outlet_branch_78_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_78_name`

        Args:
            value (str): value for IDD Field `outlet_branch_78_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_78_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_78_name`')

        self._data["Outlet Branch 78 Name"] = value

    @property
    def outlet_branch_79_name(self):
        """Get outlet_branch_79_name

        Returns:
            str: the value of `outlet_branch_79_name` or None if not set
        """
        return self._data["Outlet Branch 79 Name"]

    @outlet_branch_79_name.setter
    def outlet_branch_79_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_79_name`

        Args:
            value (str): value for IDD Field `outlet_branch_79_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_79_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_79_name`')

        self._data["Outlet Branch 79 Name"] = value

    @property
    def outlet_branch_80_name(self):
        """Get outlet_branch_80_name

        Returns:
            str: the value of `outlet_branch_80_name` or None if not set
        """
        return self._data["Outlet Branch 80 Name"]

    @outlet_branch_80_name.setter
    def outlet_branch_80_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_80_name`

        Args:
            value (str): value for IDD Field `outlet_branch_80_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_80_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_80_name`')

        self._data["Outlet Branch 80 Name"] = value

    @property
    def outlet_branch_81_name(self):
        """Get outlet_branch_81_name

        Returns:
            str: the value of `outlet_branch_81_name` or None if not set
        """
        return self._data["Outlet Branch 81 Name"]

    @outlet_branch_81_name.setter
    def outlet_branch_81_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_81_name`

        Args:
            value (str): value for IDD Field `outlet_branch_81_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_81_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_81_name`')

        self._data["Outlet Branch 81 Name"] = value

    @property
    def outlet_branch_82_name(self):
        """Get outlet_branch_82_name

        Returns:
            str: the value of `outlet_branch_82_name` or None if not set
        """
        return self._data["Outlet Branch 82 Name"]

    @outlet_branch_82_name.setter
    def outlet_branch_82_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_82_name`

        Args:
            value (str): value for IDD Field `outlet_branch_82_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_82_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_82_name`')

        self._data["Outlet Branch 82 Name"] = value

    @property
    def outlet_branch_83_name(self):
        """Get outlet_branch_83_name

        Returns:
            str: the value of `outlet_branch_83_name` or None if not set
        """
        return self._data["Outlet Branch 83 Name"]

    @outlet_branch_83_name.setter
    def outlet_branch_83_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_83_name`

        Args:
            value (str): value for IDD Field `outlet_branch_83_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_83_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_83_name`')

        self._data["Outlet Branch 83 Name"] = value

    @property
    def outlet_branch_84_name(self):
        """Get outlet_branch_84_name

        Returns:
            str: the value of `outlet_branch_84_name` or None if not set
        """
        return self._data["Outlet Branch 84 Name"]

    @outlet_branch_84_name.setter
    def outlet_branch_84_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_84_name`

        Args:
            value (str): value for IDD Field `outlet_branch_84_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_84_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_84_name`')

        self._data["Outlet Branch 84 Name"] = value

    @property
    def outlet_branch_85_name(self):
        """Get outlet_branch_85_name

        Returns:
            str: the value of `outlet_branch_85_name` or None if not set
        """
        return self._data["Outlet Branch 85 Name"]

    @outlet_branch_85_name.setter
    def outlet_branch_85_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_85_name`

        Args:
            value (str): value for IDD Field `outlet_branch_85_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_85_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_85_name`')

        self._data["Outlet Branch 85 Name"] = value

    @property
    def outlet_branch_86_name(self):
        """Get outlet_branch_86_name

        Returns:
            str: the value of `outlet_branch_86_name` or None if not set
        """
        return self._data["Outlet Branch 86 Name"]

    @outlet_branch_86_name.setter
    def outlet_branch_86_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_86_name`

        Args:
            value (str): value for IDD Field `outlet_branch_86_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_86_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_86_name`')

        self._data["Outlet Branch 86 Name"] = value

    @property
    def outlet_branch_87_name(self):
        """Get outlet_branch_87_name

        Returns:
            str: the value of `outlet_branch_87_name` or None if not set
        """
        return self._data["Outlet Branch 87 Name"]

    @outlet_branch_87_name.setter
    def outlet_branch_87_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_87_name`

        Args:
            value (str): value for IDD Field `outlet_branch_87_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_87_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_87_name`')

        self._data["Outlet Branch 87 Name"] = value

    @property
    def outlet_branch_88_name(self):
        """Get outlet_branch_88_name

        Returns:
            str: the value of `outlet_branch_88_name` or None if not set
        """
        return self._data["Outlet Branch 88 Name"]

    @outlet_branch_88_name.setter
    def outlet_branch_88_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_88_name`

        Args:
            value (str): value for IDD Field `outlet_branch_88_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_88_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_88_name`')

        self._data["Outlet Branch 88 Name"] = value

    @property
    def outlet_branch_89_name(self):
        """Get outlet_branch_89_name

        Returns:
            str: the value of `outlet_branch_89_name` or None if not set
        """
        return self._data["Outlet Branch 89 Name"]

    @outlet_branch_89_name.setter
    def outlet_branch_89_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_89_name`

        Args:
            value (str): value for IDD Field `outlet_branch_89_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_89_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_89_name`')

        self._data["Outlet Branch 89 Name"] = value

    @property
    def outlet_branch_90_name(self):
        """Get outlet_branch_90_name

        Returns:
            str: the value of `outlet_branch_90_name` or None if not set
        """
        return self._data["Outlet Branch 90 Name"]

    @outlet_branch_90_name.setter
    def outlet_branch_90_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_90_name`

        Args:
            value (str): value for IDD Field `outlet_branch_90_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_90_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_90_name`')

        self._data["Outlet Branch 90 Name"] = value

    @property
    def outlet_branch_91_name(self):
        """Get outlet_branch_91_name

        Returns:
            str: the value of `outlet_branch_91_name` or None if not set
        """
        return self._data["Outlet Branch 91 Name"]

    @outlet_branch_91_name.setter
    def outlet_branch_91_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_91_name`

        Args:
            value (str): value for IDD Field `outlet_branch_91_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_91_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_91_name`')

        self._data["Outlet Branch 91 Name"] = value

    @property
    def outlet_branch_92_name(self):
        """Get outlet_branch_92_name

        Returns:
            str: the value of `outlet_branch_92_name` or None if not set
        """
        return self._data["Outlet Branch 92 Name"]

    @outlet_branch_92_name.setter
    def outlet_branch_92_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_92_name`

        Args:
            value (str): value for IDD Field `outlet_branch_92_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_92_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_92_name`')

        self._data["Outlet Branch 92 Name"] = value

    @property
    def outlet_branch_93_name(self):
        """Get outlet_branch_93_name

        Returns:
            str: the value of `outlet_branch_93_name` or None if not set
        """
        return self._data["Outlet Branch 93 Name"]

    @outlet_branch_93_name.setter
    def outlet_branch_93_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_93_name`

        Args:
            value (str): value for IDD Field `outlet_branch_93_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_93_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_93_name`')

        self._data["Outlet Branch 93 Name"] = value

    @property
    def outlet_branch_94_name(self):
        """Get outlet_branch_94_name

        Returns:
            str: the value of `outlet_branch_94_name` or None if not set
        """
        return self._data["Outlet Branch 94 Name"]

    @outlet_branch_94_name.setter
    def outlet_branch_94_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_94_name`

        Args:
            value (str): value for IDD Field `outlet_branch_94_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_94_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_94_name`')

        self._data["Outlet Branch 94 Name"] = value

    @property
    def outlet_branch_95_name(self):
        """Get outlet_branch_95_name

        Returns:
            str: the value of `outlet_branch_95_name` or None if not set
        """
        return self._data["Outlet Branch 95 Name"]

    @outlet_branch_95_name.setter
    def outlet_branch_95_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_95_name`

        Args:
            value (str): value for IDD Field `outlet_branch_95_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_95_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_95_name`')

        self._data["Outlet Branch 95 Name"] = value

    @property
    def outlet_branch_96_name(self):
        """Get outlet_branch_96_name

        Returns:
            str: the value of `outlet_branch_96_name` or None if not set
        """
        return self._data["Outlet Branch 96 Name"]

    @outlet_branch_96_name.setter
    def outlet_branch_96_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_96_name`

        Args:
            value (str): value for IDD Field `outlet_branch_96_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_96_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_96_name`')

        self._data["Outlet Branch 96 Name"] = value

    @property
    def outlet_branch_97_name(self):
        """Get outlet_branch_97_name

        Returns:
            str: the value of `outlet_branch_97_name` or None if not set
        """
        return self._data["Outlet Branch 97 Name"]

    @outlet_branch_97_name.setter
    def outlet_branch_97_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_97_name`

        Args:
            value (str): value for IDD Field `outlet_branch_97_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_97_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_97_name`')

        self._data["Outlet Branch 97 Name"] = value

    @property
    def outlet_branch_98_name(self):
        """Get outlet_branch_98_name

        Returns:
            str: the value of `outlet_branch_98_name` or None if not set
        """
        return self._data["Outlet Branch 98 Name"]

    @outlet_branch_98_name.setter
    def outlet_branch_98_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_98_name`

        Args:
            value (str): value for IDD Field `outlet_branch_98_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_98_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_98_name`')

        self._data["Outlet Branch 98 Name"] = value

    @property
    def outlet_branch_99_name(self):
        """Get outlet_branch_99_name

        Returns:
            str: the value of `outlet_branch_99_name` or None if not set
        """
        return self._data["Outlet Branch 99 Name"]

    @outlet_branch_99_name.setter
    def outlet_branch_99_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_99_name`

        Args:
            value (str): value for IDD Field `outlet_branch_99_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_99_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_99_name`')

        self._data["Outlet Branch 99 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

    @property
    def outlet_branch_100_name(self):
        """Get outlet_branch_100_name

        Returns:
            str: the value of `outlet_branch_100_name` or None if not set
        """
        return self._data["Outlet Branch 100 Name"]

    @outlet_branch_100_name.setter
    def outlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_100_name`

        Args:
            value (str): value for IDD Field `outlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_100_name`')

        self._data["Outlet Branch 100 Name"] = value

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
        out.append(self._to_str(self.inlet_branch_name))
        out.append(self._to_str(self.outlet_branch_1_name))
        out.append(self._to_str(self.outlet_branch_2_name))
        out.append(self._to_str(self.outlet_branch_3_name))
        out.append(self._to_str(self.outlet_branch_4_name))
        out.append(self._to_str(self.outlet_branch_5_name))
        out.append(self._to_str(self.outlet_branch_6_name))
        out.append(self._to_str(self.outlet_branch_7_name))
        out.append(self._to_str(self.outlet_branch_8_name))
        out.append(self._to_str(self.outlet_branch_9_name))
        out.append(self._to_str(self.outlet_branch_10_name))
        out.append(self._to_str(self.outlet_branch_11_name))
        out.append(self._to_str(self.outlet_branch_12_name))
        out.append(self._to_str(self.outlet_branch_13_name))
        out.append(self._to_str(self.outlet_branch_14_name))
        out.append(self._to_str(self.outlet_branch_15_name))
        out.append(self._to_str(self.outlet_branch_16_name))
        out.append(self._to_str(self.outlet_branch_17_name))
        out.append(self._to_str(self.outlet_branch_18_name))
        out.append(self._to_str(self.outlet_branch_19_name))
        out.append(self._to_str(self.outlet_branch_20_name))
        out.append(self._to_str(self.outlet_branch_21_name))
        out.append(self._to_str(self.outlet_branch_22_name))
        out.append(self._to_str(self.outlet_branch_23_name))
        out.append(self._to_str(self.outlet_branch_24_name))
        out.append(self._to_str(self.outlet_branch_25_name))
        out.append(self._to_str(self.outlet_branch_26_name))
        out.append(self._to_str(self.outlet_branch_27_name))
        out.append(self._to_str(self.outlet_branch_28_name))
        out.append(self._to_str(self.outlet_branch_29_name))
        out.append(self._to_str(self.outlet_branch_30_name))
        out.append(self._to_str(self.outlet_branch_31_name))
        out.append(self._to_str(self.outlet_branch_32_name))
        out.append(self._to_str(self.outlet_branch_33_name))
        out.append(self._to_str(self.outlet_branch_34_name))
        out.append(self._to_str(self.outlet_branch_35_name))
        out.append(self._to_str(self.outlet_branch_36_name))
        out.append(self._to_str(self.outlet_branch_37_name))
        out.append(self._to_str(self.outlet_branch_38_name))
        out.append(self._to_str(self.outlet_branch_39_name))
        out.append(self._to_str(self.outlet_branch_40_name))
        out.append(self._to_str(self.outlet_branch_41_name))
        out.append(self._to_str(self.outlet_branch_42_name))
        out.append(self._to_str(self.outlet_branch_43_name))
        out.append(self._to_str(self.outlet_branch_44_name))
        out.append(self._to_str(self.outlet_branch_45_name))
        out.append(self._to_str(self.outlet_branch_46_name))
        out.append(self._to_str(self.outlet_branch_47_name))
        out.append(self._to_str(self.outlet_branch_48_name))
        out.append(self._to_str(self.outlet_branch_49_name))
        out.append(self._to_str(self.outlet_branch_50_name))
        out.append(self._to_str(self.outlet_branch_51_name))
        out.append(self._to_str(self.outlet_branch_52_name))
        out.append(self._to_str(self.outlet_branch_53_name))
        out.append(self._to_str(self.outlet_branch_54_name))
        out.append(self._to_str(self.outlet_branch_55_name))
        out.append(self._to_str(self.outlet_branch_56_name))
        out.append(self._to_str(self.outlet_branch_57_name))
        out.append(self._to_str(self.outlet_branch_58_name))
        out.append(self._to_str(self.outlet_branch_59_name))
        out.append(self._to_str(self.outlet_branch_60_name))
        out.append(self._to_str(self.outlet_branch_61_name))
        out.append(self._to_str(self.outlet_branch_62_name))
        out.append(self._to_str(self.outlet_branch_63_name))
        out.append(self._to_str(self.outlet_branch_64_name))
        out.append(self._to_str(self.outlet_branch_65_name))
        out.append(self._to_str(self.outlet_branch_66_name))
        out.append(self._to_str(self.outlet_branch_67_name))
        out.append(self._to_str(self.outlet_branch_68_name))
        out.append(self._to_str(self.outlet_branch_69_name))
        out.append(self._to_str(self.outlet_branch_70_name))
        out.append(self._to_str(self.outlet_branch_71_name))
        out.append(self._to_str(self.outlet_branch_72_name))
        out.append(self._to_str(self.outlet_branch_73_name))
        out.append(self._to_str(self.outlet_branch_74_name))
        out.append(self._to_str(self.outlet_branch_75_name))
        out.append(self._to_str(self.outlet_branch_76_name))
        out.append(self._to_str(self.outlet_branch_77_name))
        out.append(self._to_str(self.outlet_branch_78_name))
        out.append(self._to_str(self.outlet_branch_79_name))
        out.append(self._to_str(self.outlet_branch_80_name))
        out.append(self._to_str(self.outlet_branch_81_name))
        out.append(self._to_str(self.outlet_branch_82_name))
        out.append(self._to_str(self.outlet_branch_83_name))
        out.append(self._to_str(self.outlet_branch_84_name))
        out.append(self._to_str(self.outlet_branch_85_name))
        out.append(self._to_str(self.outlet_branch_86_name))
        out.append(self._to_str(self.outlet_branch_87_name))
        out.append(self._to_str(self.outlet_branch_88_name))
        out.append(self._to_str(self.outlet_branch_89_name))
        out.append(self._to_str(self.outlet_branch_90_name))
        out.append(self._to_str(self.outlet_branch_91_name))
        out.append(self._to_str(self.outlet_branch_92_name))
        out.append(self._to_str(self.outlet_branch_93_name))
        out.append(self._to_str(self.outlet_branch_94_name))
        out.append(self._to_str(self.outlet_branch_95_name))
        out.append(self._to_str(self.outlet_branch_96_name))
        out.append(self._to_str(self.outlet_branch_97_name))
        out.append(self._to_str(self.outlet_branch_98_name))
        out.append(self._to_str(self.outlet_branch_99_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        out.append(self._to_str(self.outlet_branch_100_name))
        return ",".join(out)

class ConnectorMixer(object):
    """ Corresponds to IDD object `Connector:Mixer`
        Mix N inlet air/water streams into one.  Branch names cannot be duplicated within
        a single mixer list.
    """
    internal_name = "Connector:Mixer"
    field_count = 142

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `Connector:Mixer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outlet Branch Name"] = None
        self._data["Inlet Branch 1 Name"] = None
        self._data["Inlet Branch 2 Name"] = None
        self._data["Inlet Branch 3 Name"] = None
        self._data["Inlet Branch 4 Name"] = None
        self._data["Inlet Branch 5 Name"] = None
        self._data["Inlet Branch 6 Name"] = None
        self._data["Inlet Branch 7 Name"] = None
        self._data["Inlet Branch 8 Name"] = None
        self._data["Inlet Branch 9 Name"] = None
        self._data["Inlet Branch 10 Name"] = None
        self._data["Inlet Branch 11 Name"] = None
        self._data["Inlet Branch 12 Name"] = None
        self._data["Inlet Branch 13 Name"] = None
        self._data["Inlet Branch 14 Name"] = None
        self._data["Inlet Branch 15 Name"] = None
        self._data["Inlet Branch 16 Name"] = None
        self._data["Inlet Branch 17 Name"] = None
        self._data["Inlet Branch 18 Name"] = None
        self._data["Inlet Branch 19 Name"] = None
        self._data["Inlet Branch 20 Name"] = None
        self._data["Inlet Branch 21 Name"] = None
        self._data["Inlet Branch 22 Name"] = None
        self._data["Inlet Branch 23 Name"] = None
        self._data["Inlet Branch 24 Name"] = None
        self._data["Inlet Branch 25 Name"] = None
        self._data["Inlet Branch 26 Name"] = None
        self._data["Inlet Branch 27 Name"] = None
        self._data["Inlet Branch 28 Name"] = None
        self._data["Inlet Branch 29 Name"] = None
        self._data["Inlet Branch 30 Name"] = None
        self._data["Inlet Branch 31 Name"] = None
        self._data["Inlet Branch 32 Name"] = None
        self._data["Inlet Branch 33 Name"] = None
        self._data["Inlet Branch 34 Name"] = None
        self._data["Inlet Branch 35 Name"] = None
        self._data["Inlet Branch 36 Name"] = None
        self._data["Inlet Branch 37 Name"] = None
        self._data["Inlet Branch 38 Name"] = None
        self._data["Inlet Branch 39 Name"] = None
        self._data["Inlet Branch 40 Name"] = None
        self._data["Inlet Branch 41 Name"] = None
        self._data["Inlet Branch 42 Name"] = None
        self._data["Inlet Branch 43 Name"] = None
        self._data["Inlet Branch 44 Name"] = None
        self._data["Inlet Branch 45 Name"] = None
        self._data["Inlet Branch 46 Name"] = None
        self._data["Inlet Branch 47 Name"] = None
        self._data["Inlet Branch 48 Name"] = None
        self._data["Inlet Branch 49 Name"] = None
        self._data["Inlet Branch 50 Name"] = None
        self._data["Inlet Branch 51 Name"] = None
        self._data["Inlet Branch 52 Name"] = None
        self._data["Inlet Branch 53 Name"] = None
        self._data["Inlet Branch 54 Name"] = None
        self._data["Inlet Branch 55 Name"] = None
        self._data["Inlet Branch 56 Name"] = None
        self._data["Inlet Branch 57 Name"] = None
        self._data["Inlet Branch 58 Name"] = None
        self._data["Inlet Branch 59 Name"] = None
        self._data["Inlet Branch 60 Name"] = None
        self._data["Inlet Branch 61 Name"] = None
        self._data["Inlet Branch 62 Name"] = None
        self._data["Inlet Branch 63 Name"] = None
        self._data["Inlet Branch 64 Name"] = None
        self._data["Inlet Branch 65 Name"] = None
        self._data["Inlet Branch 66 Name"] = None
        self._data["Inlet Branch 67 Name"] = None
        self._data["Inlet Branch 68 Name"] = None
        self._data["Inlet Branch 69 Name"] = None
        self._data["Inlet Branch 70 Name"] = None
        self._data["Inlet Branch 71 Name"] = None
        self._data["Inlet Branch 72 Name"] = None
        self._data["Inlet Branch 73 Name"] = None
        self._data["Inlet Branch 74 Name"] = None
        self._data["Inlet Branch 75 Name"] = None
        self._data["Inlet Branch 76 Name"] = None
        self._data["Inlet Branch 77 Name"] = None
        self._data["Inlet Branch 78 Name"] = None
        self._data["Inlet Branch 79 Name"] = None
        self._data["Inlet Branch 80 Name"] = None
        self._data["Inlet Branch 81 Name"] = None
        self._data["Inlet Branch 82 Name"] = None
        self._data["Inlet Branch 83 Name"] = None
        self._data["Inlet Branch 84 Name"] = None
        self._data["Inlet Branch 85 Name"] = None
        self._data["Inlet Branch 86 Name"] = None
        self._data["Inlet Branch 87 Name"] = None
        self._data["Inlet Branch 88 Name"] = None
        self._data["Inlet Branch 89 Name"] = None
        self._data["Inlet Branch 90 Name"] = None
        self._data["Inlet Branch 91 Name"] = None
        self._data["Inlet Branch 92 Name"] = None
        self._data["Inlet Branch 93 Name"] = None
        self._data["Inlet Branch 94 Name"] = None
        self._data["Inlet Branch 95 Name"] = None
        self._data["Inlet Branch 96 Name"] = None
        self._data["Inlet Branch 97 Name"] = None
        self._data["Inlet Branch 98 Name"] = None
        self._data["Inlet Branch 99 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None
        self._data["Inlet Branch 100 Name"] = None

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
            self.outlet_branch_name = None
        else:
            self.outlet_branch_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_1_name = None
        else:
            self.inlet_branch_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_2_name = None
        else:
            self.inlet_branch_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_3_name = None
        else:
            self.inlet_branch_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_4_name = None
        else:
            self.inlet_branch_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_5_name = None
        else:
            self.inlet_branch_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_6_name = None
        else:
            self.inlet_branch_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_7_name = None
        else:
            self.inlet_branch_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_8_name = None
        else:
            self.inlet_branch_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_9_name = None
        else:
            self.inlet_branch_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_10_name = None
        else:
            self.inlet_branch_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_11_name = None
        else:
            self.inlet_branch_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_12_name = None
        else:
            self.inlet_branch_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_13_name = None
        else:
            self.inlet_branch_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_14_name = None
        else:
            self.inlet_branch_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_15_name = None
        else:
            self.inlet_branch_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_16_name = None
        else:
            self.inlet_branch_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_17_name = None
        else:
            self.inlet_branch_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_18_name = None
        else:
            self.inlet_branch_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_19_name = None
        else:
            self.inlet_branch_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_20_name = None
        else:
            self.inlet_branch_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_21_name = None
        else:
            self.inlet_branch_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_22_name = None
        else:
            self.inlet_branch_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_23_name = None
        else:
            self.inlet_branch_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_24_name = None
        else:
            self.inlet_branch_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_25_name = None
        else:
            self.inlet_branch_25_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_26_name = None
        else:
            self.inlet_branch_26_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_27_name = None
        else:
            self.inlet_branch_27_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_28_name = None
        else:
            self.inlet_branch_28_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_29_name = None
        else:
            self.inlet_branch_29_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_30_name = None
        else:
            self.inlet_branch_30_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_31_name = None
        else:
            self.inlet_branch_31_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_32_name = None
        else:
            self.inlet_branch_32_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_33_name = None
        else:
            self.inlet_branch_33_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_34_name = None
        else:
            self.inlet_branch_34_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_35_name = None
        else:
            self.inlet_branch_35_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_36_name = None
        else:
            self.inlet_branch_36_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_37_name = None
        else:
            self.inlet_branch_37_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_38_name = None
        else:
            self.inlet_branch_38_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_39_name = None
        else:
            self.inlet_branch_39_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_40_name = None
        else:
            self.inlet_branch_40_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_41_name = None
        else:
            self.inlet_branch_41_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_42_name = None
        else:
            self.inlet_branch_42_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_43_name = None
        else:
            self.inlet_branch_43_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_44_name = None
        else:
            self.inlet_branch_44_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_45_name = None
        else:
            self.inlet_branch_45_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_46_name = None
        else:
            self.inlet_branch_46_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_47_name = None
        else:
            self.inlet_branch_47_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_48_name = None
        else:
            self.inlet_branch_48_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_49_name = None
        else:
            self.inlet_branch_49_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_50_name = None
        else:
            self.inlet_branch_50_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_51_name = None
        else:
            self.inlet_branch_51_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_52_name = None
        else:
            self.inlet_branch_52_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_53_name = None
        else:
            self.inlet_branch_53_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_54_name = None
        else:
            self.inlet_branch_54_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_55_name = None
        else:
            self.inlet_branch_55_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_56_name = None
        else:
            self.inlet_branch_56_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_57_name = None
        else:
            self.inlet_branch_57_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_58_name = None
        else:
            self.inlet_branch_58_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_59_name = None
        else:
            self.inlet_branch_59_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_60_name = None
        else:
            self.inlet_branch_60_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_61_name = None
        else:
            self.inlet_branch_61_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_62_name = None
        else:
            self.inlet_branch_62_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_63_name = None
        else:
            self.inlet_branch_63_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_64_name = None
        else:
            self.inlet_branch_64_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_65_name = None
        else:
            self.inlet_branch_65_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_66_name = None
        else:
            self.inlet_branch_66_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_67_name = None
        else:
            self.inlet_branch_67_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_68_name = None
        else:
            self.inlet_branch_68_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_69_name = None
        else:
            self.inlet_branch_69_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_70_name = None
        else:
            self.inlet_branch_70_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_71_name = None
        else:
            self.inlet_branch_71_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_72_name = None
        else:
            self.inlet_branch_72_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_73_name = None
        else:
            self.inlet_branch_73_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_74_name = None
        else:
            self.inlet_branch_74_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_75_name = None
        else:
            self.inlet_branch_75_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_76_name = None
        else:
            self.inlet_branch_76_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_77_name = None
        else:
            self.inlet_branch_77_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_78_name = None
        else:
            self.inlet_branch_78_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_79_name = None
        else:
            self.inlet_branch_79_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_80_name = None
        else:
            self.inlet_branch_80_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_81_name = None
        else:
            self.inlet_branch_81_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_82_name = None
        else:
            self.inlet_branch_82_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_83_name = None
        else:
            self.inlet_branch_83_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_84_name = None
        else:
            self.inlet_branch_84_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_85_name = None
        else:
            self.inlet_branch_85_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_86_name = None
        else:
            self.inlet_branch_86_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_87_name = None
        else:
            self.inlet_branch_87_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_88_name = None
        else:
            self.inlet_branch_88_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_89_name = None
        else:
            self.inlet_branch_89_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_90_name = None
        else:
            self.inlet_branch_90_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_91_name = None
        else:
            self.inlet_branch_91_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_92_name = None
        else:
            self.inlet_branch_92_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_93_name = None
        else:
            self.inlet_branch_93_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_94_name = None
        else:
            self.inlet_branch_94_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_95_name = None
        else:
            self.inlet_branch_95_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_96_name = None
        else:
            self.inlet_branch_96_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_97_name = None
        else:
            self.inlet_branch_97_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_98_name = None
        else:
            self.inlet_branch_98_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_99_name = None
        else:
            self.inlet_branch_99_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inlet_branch_100_name = None
        else:
            self.inlet_branch_100_name = vals[i]
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
    def outlet_branch_name(self):
        """Get outlet_branch_name

        Returns:
            str: the value of `outlet_branch_name` or None if not set
        """
        return self._data["Outlet Branch Name"]

    @outlet_branch_name.setter
    def outlet_branch_name(self, value=None):
        """  Corresponds to IDD Field `outlet_branch_name`

        Args:
            value (str): value for IDD Field `outlet_branch_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_branch_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_branch_name`')

        self._data["Outlet Branch Name"] = value

    @property
    def inlet_branch_1_name(self):
        """Get inlet_branch_1_name

        Returns:
            str: the value of `inlet_branch_1_name` or None if not set
        """
        return self._data["Inlet Branch 1 Name"]

    @inlet_branch_1_name.setter
    def inlet_branch_1_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_1_name`

        Args:
            value (str): value for IDD Field `inlet_branch_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_1_name`')

        self._data["Inlet Branch 1 Name"] = value

    @property
    def inlet_branch_2_name(self):
        """Get inlet_branch_2_name

        Returns:
            str: the value of `inlet_branch_2_name` or None if not set
        """
        return self._data["Inlet Branch 2 Name"]

    @inlet_branch_2_name.setter
    def inlet_branch_2_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_2_name`

        Args:
            value (str): value for IDD Field `inlet_branch_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_2_name`')

        self._data["Inlet Branch 2 Name"] = value

    @property
    def inlet_branch_3_name(self):
        """Get inlet_branch_3_name

        Returns:
            str: the value of `inlet_branch_3_name` or None if not set
        """
        return self._data["Inlet Branch 3 Name"]

    @inlet_branch_3_name.setter
    def inlet_branch_3_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_3_name`

        Args:
            value (str): value for IDD Field `inlet_branch_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_3_name`')

        self._data["Inlet Branch 3 Name"] = value

    @property
    def inlet_branch_4_name(self):
        """Get inlet_branch_4_name

        Returns:
            str: the value of `inlet_branch_4_name` or None if not set
        """
        return self._data["Inlet Branch 4 Name"]

    @inlet_branch_4_name.setter
    def inlet_branch_4_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_4_name`

        Args:
            value (str): value for IDD Field `inlet_branch_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_4_name`')

        self._data["Inlet Branch 4 Name"] = value

    @property
    def inlet_branch_5_name(self):
        """Get inlet_branch_5_name

        Returns:
            str: the value of `inlet_branch_5_name` or None if not set
        """
        return self._data["Inlet Branch 5 Name"]

    @inlet_branch_5_name.setter
    def inlet_branch_5_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_5_name`

        Args:
            value (str): value for IDD Field `inlet_branch_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_5_name`')

        self._data["Inlet Branch 5 Name"] = value

    @property
    def inlet_branch_6_name(self):
        """Get inlet_branch_6_name

        Returns:
            str: the value of `inlet_branch_6_name` or None if not set
        """
        return self._data["Inlet Branch 6 Name"]

    @inlet_branch_6_name.setter
    def inlet_branch_6_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_6_name`

        Args:
            value (str): value for IDD Field `inlet_branch_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_6_name`')

        self._data["Inlet Branch 6 Name"] = value

    @property
    def inlet_branch_7_name(self):
        """Get inlet_branch_7_name

        Returns:
            str: the value of `inlet_branch_7_name` or None if not set
        """
        return self._data["Inlet Branch 7 Name"]

    @inlet_branch_7_name.setter
    def inlet_branch_7_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_7_name`

        Args:
            value (str): value for IDD Field `inlet_branch_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_7_name`')

        self._data["Inlet Branch 7 Name"] = value

    @property
    def inlet_branch_8_name(self):
        """Get inlet_branch_8_name

        Returns:
            str: the value of `inlet_branch_8_name` or None if not set
        """
        return self._data["Inlet Branch 8 Name"]

    @inlet_branch_8_name.setter
    def inlet_branch_8_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_8_name`

        Args:
            value (str): value for IDD Field `inlet_branch_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_8_name`')

        self._data["Inlet Branch 8 Name"] = value

    @property
    def inlet_branch_9_name(self):
        """Get inlet_branch_9_name

        Returns:
            str: the value of `inlet_branch_9_name` or None if not set
        """
        return self._data["Inlet Branch 9 Name"]

    @inlet_branch_9_name.setter
    def inlet_branch_9_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_9_name`

        Args:
            value (str): value for IDD Field `inlet_branch_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_9_name`')

        self._data["Inlet Branch 9 Name"] = value

    @property
    def inlet_branch_10_name(self):
        """Get inlet_branch_10_name

        Returns:
            str: the value of `inlet_branch_10_name` or None if not set
        """
        return self._data["Inlet Branch 10 Name"]

    @inlet_branch_10_name.setter
    def inlet_branch_10_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_10_name`

        Args:
            value (str): value for IDD Field `inlet_branch_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_10_name`')

        self._data["Inlet Branch 10 Name"] = value

    @property
    def inlet_branch_11_name(self):
        """Get inlet_branch_11_name

        Returns:
            str: the value of `inlet_branch_11_name` or None if not set
        """
        return self._data["Inlet Branch 11 Name"]

    @inlet_branch_11_name.setter
    def inlet_branch_11_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_11_name`

        Args:
            value (str): value for IDD Field `inlet_branch_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_11_name`')

        self._data["Inlet Branch 11 Name"] = value

    @property
    def inlet_branch_12_name(self):
        """Get inlet_branch_12_name

        Returns:
            str: the value of `inlet_branch_12_name` or None if not set
        """
        return self._data["Inlet Branch 12 Name"]

    @inlet_branch_12_name.setter
    def inlet_branch_12_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_12_name`

        Args:
            value (str): value for IDD Field `inlet_branch_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_12_name`')

        self._data["Inlet Branch 12 Name"] = value

    @property
    def inlet_branch_13_name(self):
        """Get inlet_branch_13_name

        Returns:
            str: the value of `inlet_branch_13_name` or None if not set
        """
        return self._data["Inlet Branch 13 Name"]

    @inlet_branch_13_name.setter
    def inlet_branch_13_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_13_name`

        Args:
            value (str): value for IDD Field `inlet_branch_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_13_name`')

        self._data["Inlet Branch 13 Name"] = value

    @property
    def inlet_branch_14_name(self):
        """Get inlet_branch_14_name

        Returns:
            str: the value of `inlet_branch_14_name` or None if not set
        """
        return self._data["Inlet Branch 14 Name"]

    @inlet_branch_14_name.setter
    def inlet_branch_14_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_14_name`

        Args:
            value (str): value for IDD Field `inlet_branch_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_14_name`')

        self._data["Inlet Branch 14 Name"] = value

    @property
    def inlet_branch_15_name(self):
        """Get inlet_branch_15_name

        Returns:
            str: the value of `inlet_branch_15_name` or None if not set
        """
        return self._data["Inlet Branch 15 Name"]

    @inlet_branch_15_name.setter
    def inlet_branch_15_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_15_name`

        Args:
            value (str): value for IDD Field `inlet_branch_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_15_name`')

        self._data["Inlet Branch 15 Name"] = value

    @property
    def inlet_branch_16_name(self):
        """Get inlet_branch_16_name

        Returns:
            str: the value of `inlet_branch_16_name` or None if not set
        """
        return self._data["Inlet Branch 16 Name"]

    @inlet_branch_16_name.setter
    def inlet_branch_16_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_16_name`

        Args:
            value (str): value for IDD Field `inlet_branch_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_16_name`')

        self._data["Inlet Branch 16 Name"] = value

    @property
    def inlet_branch_17_name(self):
        """Get inlet_branch_17_name

        Returns:
            str: the value of `inlet_branch_17_name` or None if not set
        """
        return self._data["Inlet Branch 17 Name"]

    @inlet_branch_17_name.setter
    def inlet_branch_17_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_17_name`

        Args:
            value (str): value for IDD Field `inlet_branch_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_17_name`')

        self._data["Inlet Branch 17 Name"] = value

    @property
    def inlet_branch_18_name(self):
        """Get inlet_branch_18_name

        Returns:
            str: the value of `inlet_branch_18_name` or None if not set
        """
        return self._data["Inlet Branch 18 Name"]

    @inlet_branch_18_name.setter
    def inlet_branch_18_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_18_name`

        Args:
            value (str): value for IDD Field `inlet_branch_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_18_name`')

        self._data["Inlet Branch 18 Name"] = value

    @property
    def inlet_branch_19_name(self):
        """Get inlet_branch_19_name

        Returns:
            str: the value of `inlet_branch_19_name` or None if not set
        """
        return self._data["Inlet Branch 19 Name"]

    @inlet_branch_19_name.setter
    def inlet_branch_19_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_19_name`

        Args:
            value (str): value for IDD Field `inlet_branch_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_19_name`')

        self._data["Inlet Branch 19 Name"] = value

    @property
    def inlet_branch_20_name(self):
        """Get inlet_branch_20_name

        Returns:
            str: the value of `inlet_branch_20_name` or None if not set
        """
        return self._data["Inlet Branch 20 Name"]

    @inlet_branch_20_name.setter
    def inlet_branch_20_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_20_name`

        Args:
            value (str): value for IDD Field `inlet_branch_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_20_name`')

        self._data["Inlet Branch 20 Name"] = value

    @property
    def inlet_branch_21_name(self):
        """Get inlet_branch_21_name

        Returns:
            str: the value of `inlet_branch_21_name` or None if not set
        """
        return self._data["Inlet Branch 21 Name"]

    @inlet_branch_21_name.setter
    def inlet_branch_21_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_21_name`

        Args:
            value (str): value for IDD Field `inlet_branch_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_21_name`')

        self._data["Inlet Branch 21 Name"] = value

    @property
    def inlet_branch_22_name(self):
        """Get inlet_branch_22_name

        Returns:
            str: the value of `inlet_branch_22_name` or None if not set
        """
        return self._data["Inlet Branch 22 Name"]

    @inlet_branch_22_name.setter
    def inlet_branch_22_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_22_name`

        Args:
            value (str): value for IDD Field `inlet_branch_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_22_name`')

        self._data["Inlet Branch 22 Name"] = value

    @property
    def inlet_branch_23_name(self):
        """Get inlet_branch_23_name

        Returns:
            str: the value of `inlet_branch_23_name` or None if not set
        """
        return self._data["Inlet Branch 23 Name"]

    @inlet_branch_23_name.setter
    def inlet_branch_23_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_23_name`

        Args:
            value (str): value for IDD Field `inlet_branch_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_23_name`')

        self._data["Inlet Branch 23 Name"] = value

    @property
    def inlet_branch_24_name(self):
        """Get inlet_branch_24_name

        Returns:
            str: the value of `inlet_branch_24_name` or None if not set
        """
        return self._data["Inlet Branch 24 Name"]

    @inlet_branch_24_name.setter
    def inlet_branch_24_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_24_name`

        Args:
            value (str): value for IDD Field `inlet_branch_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_24_name`')

        self._data["Inlet Branch 24 Name"] = value

    @property
    def inlet_branch_25_name(self):
        """Get inlet_branch_25_name

        Returns:
            str: the value of `inlet_branch_25_name` or None if not set
        """
        return self._data["Inlet Branch 25 Name"]

    @inlet_branch_25_name.setter
    def inlet_branch_25_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_25_name`

        Args:
            value (str): value for IDD Field `inlet_branch_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_25_name`')

        self._data["Inlet Branch 25 Name"] = value

    @property
    def inlet_branch_26_name(self):
        """Get inlet_branch_26_name

        Returns:
            str: the value of `inlet_branch_26_name` or None if not set
        """
        return self._data["Inlet Branch 26 Name"]

    @inlet_branch_26_name.setter
    def inlet_branch_26_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_26_name`

        Args:
            value (str): value for IDD Field `inlet_branch_26_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_26_name`')

        self._data["Inlet Branch 26 Name"] = value

    @property
    def inlet_branch_27_name(self):
        """Get inlet_branch_27_name

        Returns:
            str: the value of `inlet_branch_27_name` or None if not set
        """
        return self._data["Inlet Branch 27 Name"]

    @inlet_branch_27_name.setter
    def inlet_branch_27_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_27_name`

        Args:
            value (str): value for IDD Field `inlet_branch_27_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_27_name`')

        self._data["Inlet Branch 27 Name"] = value

    @property
    def inlet_branch_28_name(self):
        """Get inlet_branch_28_name

        Returns:
            str: the value of `inlet_branch_28_name` or None if not set
        """
        return self._data["Inlet Branch 28 Name"]

    @inlet_branch_28_name.setter
    def inlet_branch_28_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_28_name`

        Args:
            value (str): value for IDD Field `inlet_branch_28_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_28_name`')

        self._data["Inlet Branch 28 Name"] = value

    @property
    def inlet_branch_29_name(self):
        """Get inlet_branch_29_name

        Returns:
            str: the value of `inlet_branch_29_name` or None if not set
        """
        return self._data["Inlet Branch 29 Name"]

    @inlet_branch_29_name.setter
    def inlet_branch_29_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_29_name`

        Args:
            value (str): value for IDD Field `inlet_branch_29_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_29_name`')

        self._data["Inlet Branch 29 Name"] = value

    @property
    def inlet_branch_30_name(self):
        """Get inlet_branch_30_name

        Returns:
            str: the value of `inlet_branch_30_name` or None if not set
        """
        return self._data["Inlet Branch 30 Name"]

    @inlet_branch_30_name.setter
    def inlet_branch_30_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_30_name`

        Args:
            value (str): value for IDD Field `inlet_branch_30_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_30_name`')

        self._data["Inlet Branch 30 Name"] = value

    @property
    def inlet_branch_31_name(self):
        """Get inlet_branch_31_name

        Returns:
            str: the value of `inlet_branch_31_name` or None if not set
        """
        return self._data["Inlet Branch 31 Name"]

    @inlet_branch_31_name.setter
    def inlet_branch_31_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_31_name`

        Args:
            value (str): value for IDD Field `inlet_branch_31_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_31_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_31_name`')

        self._data["Inlet Branch 31 Name"] = value

    @property
    def inlet_branch_32_name(self):
        """Get inlet_branch_32_name

        Returns:
            str: the value of `inlet_branch_32_name` or None if not set
        """
        return self._data["Inlet Branch 32 Name"]

    @inlet_branch_32_name.setter
    def inlet_branch_32_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_32_name`

        Args:
            value (str): value for IDD Field `inlet_branch_32_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_32_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_32_name`')

        self._data["Inlet Branch 32 Name"] = value

    @property
    def inlet_branch_33_name(self):
        """Get inlet_branch_33_name

        Returns:
            str: the value of `inlet_branch_33_name` or None if not set
        """
        return self._data["Inlet Branch 33 Name"]

    @inlet_branch_33_name.setter
    def inlet_branch_33_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_33_name`

        Args:
            value (str): value for IDD Field `inlet_branch_33_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_33_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_33_name`')

        self._data["Inlet Branch 33 Name"] = value

    @property
    def inlet_branch_34_name(self):
        """Get inlet_branch_34_name

        Returns:
            str: the value of `inlet_branch_34_name` or None if not set
        """
        return self._data["Inlet Branch 34 Name"]

    @inlet_branch_34_name.setter
    def inlet_branch_34_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_34_name`

        Args:
            value (str): value for IDD Field `inlet_branch_34_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_34_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_34_name`')

        self._data["Inlet Branch 34 Name"] = value

    @property
    def inlet_branch_35_name(self):
        """Get inlet_branch_35_name

        Returns:
            str: the value of `inlet_branch_35_name` or None if not set
        """
        return self._data["Inlet Branch 35 Name"]

    @inlet_branch_35_name.setter
    def inlet_branch_35_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_35_name`

        Args:
            value (str): value for IDD Field `inlet_branch_35_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_35_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_35_name`')

        self._data["Inlet Branch 35 Name"] = value

    @property
    def inlet_branch_36_name(self):
        """Get inlet_branch_36_name

        Returns:
            str: the value of `inlet_branch_36_name` or None if not set
        """
        return self._data["Inlet Branch 36 Name"]

    @inlet_branch_36_name.setter
    def inlet_branch_36_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_36_name`

        Args:
            value (str): value for IDD Field `inlet_branch_36_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_36_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_36_name`')

        self._data["Inlet Branch 36 Name"] = value

    @property
    def inlet_branch_37_name(self):
        """Get inlet_branch_37_name

        Returns:
            str: the value of `inlet_branch_37_name` or None if not set
        """
        return self._data["Inlet Branch 37 Name"]

    @inlet_branch_37_name.setter
    def inlet_branch_37_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_37_name`

        Args:
            value (str): value for IDD Field `inlet_branch_37_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_37_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_37_name`')

        self._data["Inlet Branch 37 Name"] = value

    @property
    def inlet_branch_38_name(self):
        """Get inlet_branch_38_name

        Returns:
            str: the value of `inlet_branch_38_name` or None if not set
        """
        return self._data["Inlet Branch 38 Name"]

    @inlet_branch_38_name.setter
    def inlet_branch_38_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_38_name`

        Args:
            value (str): value for IDD Field `inlet_branch_38_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_38_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_38_name`')

        self._data["Inlet Branch 38 Name"] = value

    @property
    def inlet_branch_39_name(self):
        """Get inlet_branch_39_name

        Returns:
            str: the value of `inlet_branch_39_name` or None if not set
        """
        return self._data["Inlet Branch 39 Name"]

    @inlet_branch_39_name.setter
    def inlet_branch_39_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_39_name`

        Args:
            value (str): value for IDD Field `inlet_branch_39_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_39_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_39_name`')

        self._data["Inlet Branch 39 Name"] = value

    @property
    def inlet_branch_40_name(self):
        """Get inlet_branch_40_name

        Returns:
            str: the value of `inlet_branch_40_name` or None if not set
        """
        return self._data["Inlet Branch 40 Name"]

    @inlet_branch_40_name.setter
    def inlet_branch_40_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_40_name`

        Args:
            value (str): value for IDD Field `inlet_branch_40_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_40_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_40_name`')

        self._data["Inlet Branch 40 Name"] = value

    @property
    def inlet_branch_41_name(self):
        """Get inlet_branch_41_name

        Returns:
            str: the value of `inlet_branch_41_name` or None if not set
        """
        return self._data["Inlet Branch 41 Name"]

    @inlet_branch_41_name.setter
    def inlet_branch_41_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_41_name`

        Args:
            value (str): value for IDD Field `inlet_branch_41_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_41_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_41_name`')

        self._data["Inlet Branch 41 Name"] = value

    @property
    def inlet_branch_42_name(self):
        """Get inlet_branch_42_name

        Returns:
            str: the value of `inlet_branch_42_name` or None if not set
        """
        return self._data["Inlet Branch 42 Name"]

    @inlet_branch_42_name.setter
    def inlet_branch_42_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_42_name`

        Args:
            value (str): value for IDD Field `inlet_branch_42_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_42_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_42_name`')

        self._data["Inlet Branch 42 Name"] = value

    @property
    def inlet_branch_43_name(self):
        """Get inlet_branch_43_name

        Returns:
            str: the value of `inlet_branch_43_name` or None if not set
        """
        return self._data["Inlet Branch 43 Name"]

    @inlet_branch_43_name.setter
    def inlet_branch_43_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_43_name`

        Args:
            value (str): value for IDD Field `inlet_branch_43_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_43_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_43_name`')

        self._data["Inlet Branch 43 Name"] = value

    @property
    def inlet_branch_44_name(self):
        """Get inlet_branch_44_name

        Returns:
            str: the value of `inlet_branch_44_name` or None if not set
        """
        return self._data["Inlet Branch 44 Name"]

    @inlet_branch_44_name.setter
    def inlet_branch_44_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_44_name`

        Args:
            value (str): value for IDD Field `inlet_branch_44_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_44_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_44_name`')

        self._data["Inlet Branch 44 Name"] = value

    @property
    def inlet_branch_45_name(self):
        """Get inlet_branch_45_name

        Returns:
            str: the value of `inlet_branch_45_name` or None if not set
        """
        return self._data["Inlet Branch 45 Name"]

    @inlet_branch_45_name.setter
    def inlet_branch_45_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_45_name`

        Args:
            value (str): value for IDD Field `inlet_branch_45_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_45_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_45_name`')

        self._data["Inlet Branch 45 Name"] = value

    @property
    def inlet_branch_46_name(self):
        """Get inlet_branch_46_name

        Returns:
            str: the value of `inlet_branch_46_name` or None if not set
        """
        return self._data["Inlet Branch 46 Name"]

    @inlet_branch_46_name.setter
    def inlet_branch_46_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_46_name`

        Args:
            value (str): value for IDD Field `inlet_branch_46_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_46_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_46_name`')

        self._data["Inlet Branch 46 Name"] = value

    @property
    def inlet_branch_47_name(self):
        """Get inlet_branch_47_name

        Returns:
            str: the value of `inlet_branch_47_name` or None if not set
        """
        return self._data["Inlet Branch 47 Name"]

    @inlet_branch_47_name.setter
    def inlet_branch_47_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_47_name`

        Args:
            value (str): value for IDD Field `inlet_branch_47_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_47_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_47_name`')

        self._data["Inlet Branch 47 Name"] = value

    @property
    def inlet_branch_48_name(self):
        """Get inlet_branch_48_name

        Returns:
            str: the value of `inlet_branch_48_name` or None if not set
        """
        return self._data["Inlet Branch 48 Name"]

    @inlet_branch_48_name.setter
    def inlet_branch_48_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_48_name`

        Args:
            value (str): value for IDD Field `inlet_branch_48_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_48_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_48_name`')

        self._data["Inlet Branch 48 Name"] = value

    @property
    def inlet_branch_49_name(self):
        """Get inlet_branch_49_name

        Returns:
            str: the value of `inlet_branch_49_name` or None if not set
        """
        return self._data["Inlet Branch 49 Name"]

    @inlet_branch_49_name.setter
    def inlet_branch_49_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_49_name`

        Args:
            value (str): value for IDD Field `inlet_branch_49_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_49_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_49_name`')

        self._data["Inlet Branch 49 Name"] = value

    @property
    def inlet_branch_50_name(self):
        """Get inlet_branch_50_name

        Returns:
            str: the value of `inlet_branch_50_name` or None if not set
        """
        return self._data["Inlet Branch 50 Name"]

    @inlet_branch_50_name.setter
    def inlet_branch_50_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_50_name`

        Args:
            value (str): value for IDD Field `inlet_branch_50_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_50_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_50_name`')

        self._data["Inlet Branch 50 Name"] = value

    @property
    def inlet_branch_51_name(self):
        """Get inlet_branch_51_name

        Returns:
            str: the value of `inlet_branch_51_name` or None if not set
        """
        return self._data["Inlet Branch 51 Name"]

    @inlet_branch_51_name.setter
    def inlet_branch_51_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_51_name`

        Args:
            value (str): value for IDD Field `inlet_branch_51_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_51_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_51_name`')

        self._data["Inlet Branch 51 Name"] = value

    @property
    def inlet_branch_52_name(self):
        """Get inlet_branch_52_name

        Returns:
            str: the value of `inlet_branch_52_name` or None if not set
        """
        return self._data["Inlet Branch 52 Name"]

    @inlet_branch_52_name.setter
    def inlet_branch_52_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_52_name`

        Args:
            value (str): value for IDD Field `inlet_branch_52_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_52_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_52_name`')

        self._data["Inlet Branch 52 Name"] = value

    @property
    def inlet_branch_53_name(self):
        """Get inlet_branch_53_name

        Returns:
            str: the value of `inlet_branch_53_name` or None if not set
        """
        return self._data["Inlet Branch 53 Name"]

    @inlet_branch_53_name.setter
    def inlet_branch_53_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_53_name`

        Args:
            value (str): value for IDD Field `inlet_branch_53_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_53_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_53_name`')

        self._data["Inlet Branch 53 Name"] = value

    @property
    def inlet_branch_54_name(self):
        """Get inlet_branch_54_name

        Returns:
            str: the value of `inlet_branch_54_name` or None if not set
        """
        return self._data["Inlet Branch 54 Name"]

    @inlet_branch_54_name.setter
    def inlet_branch_54_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_54_name`

        Args:
            value (str): value for IDD Field `inlet_branch_54_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_54_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_54_name`')

        self._data["Inlet Branch 54 Name"] = value

    @property
    def inlet_branch_55_name(self):
        """Get inlet_branch_55_name

        Returns:
            str: the value of `inlet_branch_55_name` or None if not set
        """
        return self._data["Inlet Branch 55 Name"]

    @inlet_branch_55_name.setter
    def inlet_branch_55_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_55_name`

        Args:
            value (str): value for IDD Field `inlet_branch_55_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_55_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_55_name`')

        self._data["Inlet Branch 55 Name"] = value

    @property
    def inlet_branch_56_name(self):
        """Get inlet_branch_56_name

        Returns:
            str: the value of `inlet_branch_56_name` or None if not set
        """
        return self._data["Inlet Branch 56 Name"]

    @inlet_branch_56_name.setter
    def inlet_branch_56_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_56_name`

        Args:
            value (str): value for IDD Field `inlet_branch_56_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_56_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_56_name`')

        self._data["Inlet Branch 56 Name"] = value

    @property
    def inlet_branch_57_name(self):
        """Get inlet_branch_57_name

        Returns:
            str: the value of `inlet_branch_57_name` or None if not set
        """
        return self._data["Inlet Branch 57 Name"]

    @inlet_branch_57_name.setter
    def inlet_branch_57_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_57_name`

        Args:
            value (str): value for IDD Field `inlet_branch_57_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_57_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_57_name`')

        self._data["Inlet Branch 57 Name"] = value

    @property
    def inlet_branch_58_name(self):
        """Get inlet_branch_58_name

        Returns:
            str: the value of `inlet_branch_58_name` or None if not set
        """
        return self._data["Inlet Branch 58 Name"]

    @inlet_branch_58_name.setter
    def inlet_branch_58_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_58_name`

        Args:
            value (str): value for IDD Field `inlet_branch_58_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_58_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_58_name`')

        self._data["Inlet Branch 58 Name"] = value

    @property
    def inlet_branch_59_name(self):
        """Get inlet_branch_59_name

        Returns:
            str: the value of `inlet_branch_59_name` or None if not set
        """
        return self._data["Inlet Branch 59 Name"]

    @inlet_branch_59_name.setter
    def inlet_branch_59_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_59_name`

        Args:
            value (str): value for IDD Field `inlet_branch_59_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_59_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_59_name`')

        self._data["Inlet Branch 59 Name"] = value

    @property
    def inlet_branch_60_name(self):
        """Get inlet_branch_60_name

        Returns:
            str: the value of `inlet_branch_60_name` or None if not set
        """
        return self._data["Inlet Branch 60 Name"]

    @inlet_branch_60_name.setter
    def inlet_branch_60_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_60_name`

        Args:
            value (str): value for IDD Field `inlet_branch_60_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_60_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_60_name`')

        self._data["Inlet Branch 60 Name"] = value

    @property
    def inlet_branch_61_name(self):
        """Get inlet_branch_61_name

        Returns:
            str: the value of `inlet_branch_61_name` or None if not set
        """
        return self._data["Inlet Branch 61 Name"]

    @inlet_branch_61_name.setter
    def inlet_branch_61_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_61_name`

        Args:
            value (str): value for IDD Field `inlet_branch_61_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_61_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_61_name`')

        self._data["Inlet Branch 61 Name"] = value

    @property
    def inlet_branch_62_name(self):
        """Get inlet_branch_62_name

        Returns:
            str: the value of `inlet_branch_62_name` or None if not set
        """
        return self._data["Inlet Branch 62 Name"]

    @inlet_branch_62_name.setter
    def inlet_branch_62_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_62_name`

        Args:
            value (str): value for IDD Field `inlet_branch_62_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_62_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_62_name`')

        self._data["Inlet Branch 62 Name"] = value

    @property
    def inlet_branch_63_name(self):
        """Get inlet_branch_63_name

        Returns:
            str: the value of `inlet_branch_63_name` or None if not set
        """
        return self._data["Inlet Branch 63 Name"]

    @inlet_branch_63_name.setter
    def inlet_branch_63_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_63_name`

        Args:
            value (str): value for IDD Field `inlet_branch_63_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_63_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_63_name`')

        self._data["Inlet Branch 63 Name"] = value

    @property
    def inlet_branch_64_name(self):
        """Get inlet_branch_64_name

        Returns:
            str: the value of `inlet_branch_64_name` or None if not set
        """
        return self._data["Inlet Branch 64 Name"]

    @inlet_branch_64_name.setter
    def inlet_branch_64_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_64_name`

        Args:
            value (str): value for IDD Field `inlet_branch_64_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_64_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_64_name`')

        self._data["Inlet Branch 64 Name"] = value

    @property
    def inlet_branch_65_name(self):
        """Get inlet_branch_65_name

        Returns:
            str: the value of `inlet_branch_65_name` or None if not set
        """
        return self._data["Inlet Branch 65 Name"]

    @inlet_branch_65_name.setter
    def inlet_branch_65_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_65_name`

        Args:
            value (str): value for IDD Field `inlet_branch_65_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_65_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_65_name`')

        self._data["Inlet Branch 65 Name"] = value

    @property
    def inlet_branch_66_name(self):
        """Get inlet_branch_66_name

        Returns:
            str: the value of `inlet_branch_66_name` or None if not set
        """
        return self._data["Inlet Branch 66 Name"]

    @inlet_branch_66_name.setter
    def inlet_branch_66_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_66_name`

        Args:
            value (str): value for IDD Field `inlet_branch_66_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_66_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_66_name`')

        self._data["Inlet Branch 66 Name"] = value

    @property
    def inlet_branch_67_name(self):
        """Get inlet_branch_67_name

        Returns:
            str: the value of `inlet_branch_67_name` or None if not set
        """
        return self._data["Inlet Branch 67 Name"]

    @inlet_branch_67_name.setter
    def inlet_branch_67_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_67_name`

        Args:
            value (str): value for IDD Field `inlet_branch_67_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_67_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_67_name`')

        self._data["Inlet Branch 67 Name"] = value

    @property
    def inlet_branch_68_name(self):
        """Get inlet_branch_68_name

        Returns:
            str: the value of `inlet_branch_68_name` or None if not set
        """
        return self._data["Inlet Branch 68 Name"]

    @inlet_branch_68_name.setter
    def inlet_branch_68_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_68_name`

        Args:
            value (str): value for IDD Field `inlet_branch_68_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_68_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_68_name`')

        self._data["Inlet Branch 68 Name"] = value

    @property
    def inlet_branch_69_name(self):
        """Get inlet_branch_69_name

        Returns:
            str: the value of `inlet_branch_69_name` or None if not set
        """
        return self._data["Inlet Branch 69 Name"]

    @inlet_branch_69_name.setter
    def inlet_branch_69_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_69_name`

        Args:
            value (str): value for IDD Field `inlet_branch_69_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_69_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_69_name`')

        self._data["Inlet Branch 69 Name"] = value

    @property
    def inlet_branch_70_name(self):
        """Get inlet_branch_70_name

        Returns:
            str: the value of `inlet_branch_70_name` or None if not set
        """
        return self._data["Inlet Branch 70 Name"]

    @inlet_branch_70_name.setter
    def inlet_branch_70_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_70_name`

        Args:
            value (str): value for IDD Field `inlet_branch_70_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_70_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_70_name`')

        self._data["Inlet Branch 70 Name"] = value

    @property
    def inlet_branch_71_name(self):
        """Get inlet_branch_71_name

        Returns:
            str: the value of `inlet_branch_71_name` or None if not set
        """
        return self._data["Inlet Branch 71 Name"]

    @inlet_branch_71_name.setter
    def inlet_branch_71_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_71_name`

        Args:
            value (str): value for IDD Field `inlet_branch_71_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_71_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_71_name`')

        self._data["Inlet Branch 71 Name"] = value

    @property
    def inlet_branch_72_name(self):
        """Get inlet_branch_72_name

        Returns:
            str: the value of `inlet_branch_72_name` or None if not set
        """
        return self._data["Inlet Branch 72 Name"]

    @inlet_branch_72_name.setter
    def inlet_branch_72_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_72_name`

        Args:
            value (str): value for IDD Field `inlet_branch_72_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_72_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_72_name`')

        self._data["Inlet Branch 72 Name"] = value

    @property
    def inlet_branch_73_name(self):
        """Get inlet_branch_73_name

        Returns:
            str: the value of `inlet_branch_73_name` or None if not set
        """
        return self._data["Inlet Branch 73 Name"]

    @inlet_branch_73_name.setter
    def inlet_branch_73_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_73_name`

        Args:
            value (str): value for IDD Field `inlet_branch_73_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_73_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_73_name`')

        self._data["Inlet Branch 73 Name"] = value

    @property
    def inlet_branch_74_name(self):
        """Get inlet_branch_74_name

        Returns:
            str: the value of `inlet_branch_74_name` or None if not set
        """
        return self._data["Inlet Branch 74 Name"]

    @inlet_branch_74_name.setter
    def inlet_branch_74_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_74_name`

        Args:
            value (str): value for IDD Field `inlet_branch_74_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_74_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_74_name`')

        self._data["Inlet Branch 74 Name"] = value

    @property
    def inlet_branch_75_name(self):
        """Get inlet_branch_75_name

        Returns:
            str: the value of `inlet_branch_75_name` or None if not set
        """
        return self._data["Inlet Branch 75 Name"]

    @inlet_branch_75_name.setter
    def inlet_branch_75_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_75_name`

        Args:
            value (str): value for IDD Field `inlet_branch_75_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_75_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_75_name`')

        self._data["Inlet Branch 75 Name"] = value

    @property
    def inlet_branch_76_name(self):
        """Get inlet_branch_76_name

        Returns:
            str: the value of `inlet_branch_76_name` or None if not set
        """
        return self._data["Inlet Branch 76 Name"]

    @inlet_branch_76_name.setter
    def inlet_branch_76_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_76_name`

        Args:
            value (str): value for IDD Field `inlet_branch_76_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_76_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_76_name`')

        self._data["Inlet Branch 76 Name"] = value

    @property
    def inlet_branch_77_name(self):
        """Get inlet_branch_77_name

        Returns:
            str: the value of `inlet_branch_77_name` or None if not set
        """
        return self._data["Inlet Branch 77 Name"]

    @inlet_branch_77_name.setter
    def inlet_branch_77_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_77_name`

        Args:
            value (str): value for IDD Field `inlet_branch_77_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_77_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_77_name`')

        self._data["Inlet Branch 77 Name"] = value

    @property
    def inlet_branch_78_name(self):
        """Get inlet_branch_78_name

        Returns:
            str: the value of `inlet_branch_78_name` or None if not set
        """
        return self._data["Inlet Branch 78 Name"]

    @inlet_branch_78_name.setter
    def inlet_branch_78_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_78_name`

        Args:
            value (str): value for IDD Field `inlet_branch_78_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_78_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_78_name`')

        self._data["Inlet Branch 78 Name"] = value

    @property
    def inlet_branch_79_name(self):
        """Get inlet_branch_79_name

        Returns:
            str: the value of `inlet_branch_79_name` or None if not set
        """
        return self._data["Inlet Branch 79 Name"]

    @inlet_branch_79_name.setter
    def inlet_branch_79_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_79_name`

        Args:
            value (str): value for IDD Field `inlet_branch_79_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_79_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_79_name`')

        self._data["Inlet Branch 79 Name"] = value

    @property
    def inlet_branch_80_name(self):
        """Get inlet_branch_80_name

        Returns:
            str: the value of `inlet_branch_80_name` or None if not set
        """
        return self._data["Inlet Branch 80 Name"]

    @inlet_branch_80_name.setter
    def inlet_branch_80_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_80_name`

        Args:
            value (str): value for IDD Field `inlet_branch_80_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_80_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_80_name`')

        self._data["Inlet Branch 80 Name"] = value

    @property
    def inlet_branch_81_name(self):
        """Get inlet_branch_81_name

        Returns:
            str: the value of `inlet_branch_81_name` or None if not set
        """
        return self._data["Inlet Branch 81 Name"]

    @inlet_branch_81_name.setter
    def inlet_branch_81_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_81_name`

        Args:
            value (str): value for IDD Field `inlet_branch_81_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_81_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_81_name`')

        self._data["Inlet Branch 81 Name"] = value

    @property
    def inlet_branch_82_name(self):
        """Get inlet_branch_82_name

        Returns:
            str: the value of `inlet_branch_82_name` or None if not set
        """
        return self._data["Inlet Branch 82 Name"]

    @inlet_branch_82_name.setter
    def inlet_branch_82_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_82_name`

        Args:
            value (str): value for IDD Field `inlet_branch_82_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_82_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_82_name`')

        self._data["Inlet Branch 82 Name"] = value

    @property
    def inlet_branch_83_name(self):
        """Get inlet_branch_83_name

        Returns:
            str: the value of `inlet_branch_83_name` or None if not set
        """
        return self._data["Inlet Branch 83 Name"]

    @inlet_branch_83_name.setter
    def inlet_branch_83_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_83_name`

        Args:
            value (str): value for IDD Field `inlet_branch_83_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_83_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_83_name`')

        self._data["Inlet Branch 83 Name"] = value

    @property
    def inlet_branch_84_name(self):
        """Get inlet_branch_84_name

        Returns:
            str: the value of `inlet_branch_84_name` or None if not set
        """
        return self._data["Inlet Branch 84 Name"]

    @inlet_branch_84_name.setter
    def inlet_branch_84_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_84_name`

        Args:
            value (str): value for IDD Field `inlet_branch_84_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_84_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_84_name`')

        self._data["Inlet Branch 84 Name"] = value

    @property
    def inlet_branch_85_name(self):
        """Get inlet_branch_85_name

        Returns:
            str: the value of `inlet_branch_85_name` or None if not set
        """
        return self._data["Inlet Branch 85 Name"]

    @inlet_branch_85_name.setter
    def inlet_branch_85_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_85_name`

        Args:
            value (str): value for IDD Field `inlet_branch_85_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_85_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_85_name`')

        self._data["Inlet Branch 85 Name"] = value

    @property
    def inlet_branch_86_name(self):
        """Get inlet_branch_86_name

        Returns:
            str: the value of `inlet_branch_86_name` or None if not set
        """
        return self._data["Inlet Branch 86 Name"]

    @inlet_branch_86_name.setter
    def inlet_branch_86_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_86_name`

        Args:
            value (str): value for IDD Field `inlet_branch_86_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_86_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_86_name`')

        self._data["Inlet Branch 86 Name"] = value

    @property
    def inlet_branch_87_name(self):
        """Get inlet_branch_87_name

        Returns:
            str: the value of `inlet_branch_87_name` or None if not set
        """
        return self._data["Inlet Branch 87 Name"]

    @inlet_branch_87_name.setter
    def inlet_branch_87_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_87_name`

        Args:
            value (str): value for IDD Field `inlet_branch_87_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_87_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_87_name`')

        self._data["Inlet Branch 87 Name"] = value

    @property
    def inlet_branch_88_name(self):
        """Get inlet_branch_88_name

        Returns:
            str: the value of `inlet_branch_88_name` or None if not set
        """
        return self._data["Inlet Branch 88 Name"]

    @inlet_branch_88_name.setter
    def inlet_branch_88_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_88_name`

        Args:
            value (str): value for IDD Field `inlet_branch_88_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_88_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_88_name`')

        self._data["Inlet Branch 88 Name"] = value

    @property
    def inlet_branch_89_name(self):
        """Get inlet_branch_89_name

        Returns:
            str: the value of `inlet_branch_89_name` or None if not set
        """
        return self._data["Inlet Branch 89 Name"]

    @inlet_branch_89_name.setter
    def inlet_branch_89_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_89_name`

        Args:
            value (str): value for IDD Field `inlet_branch_89_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_89_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_89_name`')

        self._data["Inlet Branch 89 Name"] = value

    @property
    def inlet_branch_90_name(self):
        """Get inlet_branch_90_name

        Returns:
            str: the value of `inlet_branch_90_name` or None if not set
        """
        return self._data["Inlet Branch 90 Name"]

    @inlet_branch_90_name.setter
    def inlet_branch_90_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_90_name`

        Args:
            value (str): value for IDD Field `inlet_branch_90_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_90_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_90_name`')

        self._data["Inlet Branch 90 Name"] = value

    @property
    def inlet_branch_91_name(self):
        """Get inlet_branch_91_name

        Returns:
            str: the value of `inlet_branch_91_name` or None if not set
        """
        return self._data["Inlet Branch 91 Name"]

    @inlet_branch_91_name.setter
    def inlet_branch_91_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_91_name`

        Args:
            value (str): value for IDD Field `inlet_branch_91_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_91_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_91_name`')

        self._data["Inlet Branch 91 Name"] = value

    @property
    def inlet_branch_92_name(self):
        """Get inlet_branch_92_name

        Returns:
            str: the value of `inlet_branch_92_name` or None if not set
        """
        return self._data["Inlet Branch 92 Name"]

    @inlet_branch_92_name.setter
    def inlet_branch_92_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_92_name`

        Args:
            value (str): value for IDD Field `inlet_branch_92_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_92_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_92_name`')

        self._data["Inlet Branch 92 Name"] = value

    @property
    def inlet_branch_93_name(self):
        """Get inlet_branch_93_name

        Returns:
            str: the value of `inlet_branch_93_name` or None if not set
        """
        return self._data["Inlet Branch 93 Name"]

    @inlet_branch_93_name.setter
    def inlet_branch_93_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_93_name`

        Args:
            value (str): value for IDD Field `inlet_branch_93_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_93_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_93_name`')

        self._data["Inlet Branch 93 Name"] = value

    @property
    def inlet_branch_94_name(self):
        """Get inlet_branch_94_name

        Returns:
            str: the value of `inlet_branch_94_name` or None if not set
        """
        return self._data["Inlet Branch 94 Name"]

    @inlet_branch_94_name.setter
    def inlet_branch_94_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_94_name`

        Args:
            value (str): value for IDD Field `inlet_branch_94_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_94_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_94_name`')

        self._data["Inlet Branch 94 Name"] = value

    @property
    def inlet_branch_95_name(self):
        """Get inlet_branch_95_name

        Returns:
            str: the value of `inlet_branch_95_name` or None if not set
        """
        return self._data["Inlet Branch 95 Name"]

    @inlet_branch_95_name.setter
    def inlet_branch_95_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_95_name`

        Args:
            value (str): value for IDD Field `inlet_branch_95_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_95_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_95_name`')

        self._data["Inlet Branch 95 Name"] = value

    @property
    def inlet_branch_96_name(self):
        """Get inlet_branch_96_name

        Returns:
            str: the value of `inlet_branch_96_name` or None if not set
        """
        return self._data["Inlet Branch 96 Name"]

    @inlet_branch_96_name.setter
    def inlet_branch_96_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_96_name`

        Args:
            value (str): value for IDD Field `inlet_branch_96_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_96_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_96_name`')

        self._data["Inlet Branch 96 Name"] = value

    @property
    def inlet_branch_97_name(self):
        """Get inlet_branch_97_name

        Returns:
            str: the value of `inlet_branch_97_name` or None if not set
        """
        return self._data["Inlet Branch 97 Name"]

    @inlet_branch_97_name.setter
    def inlet_branch_97_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_97_name`

        Args:
            value (str): value for IDD Field `inlet_branch_97_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_97_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_97_name`')

        self._data["Inlet Branch 97 Name"] = value

    @property
    def inlet_branch_98_name(self):
        """Get inlet_branch_98_name

        Returns:
            str: the value of `inlet_branch_98_name` or None if not set
        """
        return self._data["Inlet Branch 98 Name"]

    @inlet_branch_98_name.setter
    def inlet_branch_98_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_98_name`

        Args:
            value (str): value for IDD Field `inlet_branch_98_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_98_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_98_name`')

        self._data["Inlet Branch 98 Name"] = value

    @property
    def inlet_branch_99_name(self):
        """Get inlet_branch_99_name

        Returns:
            str: the value of `inlet_branch_99_name` or None if not set
        """
        return self._data["Inlet Branch 99 Name"]

    @inlet_branch_99_name.setter
    def inlet_branch_99_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_99_name`

        Args:
            value (str): value for IDD Field `inlet_branch_99_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_99_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_99_name`')

        self._data["Inlet Branch 99 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

    @property
    def inlet_branch_100_name(self):
        """Get inlet_branch_100_name

        Returns:
            str: the value of `inlet_branch_100_name` or None if not set
        """
        return self._data["Inlet Branch 100 Name"]

    @inlet_branch_100_name.setter
    def inlet_branch_100_name(self, value=None):
        """  Corresponds to IDD Field `inlet_branch_100_name`

        Args:
            value (str): value for IDD Field `inlet_branch_100_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_branch_100_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_branch_100_name`')

        self._data["Inlet Branch 100 Name"] = value

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
        out.append(self._to_str(self.outlet_branch_name))
        out.append(self._to_str(self.inlet_branch_1_name))
        out.append(self._to_str(self.inlet_branch_2_name))
        out.append(self._to_str(self.inlet_branch_3_name))
        out.append(self._to_str(self.inlet_branch_4_name))
        out.append(self._to_str(self.inlet_branch_5_name))
        out.append(self._to_str(self.inlet_branch_6_name))
        out.append(self._to_str(self.inlet_branch_7_name))
        out.append(self._to_str(self.inlet_branch_8_name))
        out.append(self._to_str(self.inlet_branch_9_name))
        out.append(self._to_str(self.inlet_branch_10_name))
        out.append(self._to_str(self.inlet_branch_11_name))
        out.append(self._to_str(self.inlet_branch_12_name))
        out.append(self._to_str(self.inlet_branch_13_name))
        out.append(self._to_str(self.inlet_branch_14_name))
        out.append(self._to_str(self.inlet_branch_15_name))
        out.append(self._to_str(self.inlet_branch_16_name))
        out.append(self._to_str(self.inlet_branch_17_name))
        out.append(self._to_str(self.inlet_branch_18_name))
        out.append(self._to_str(self.inlet_branch_19_name))
        out.append(self._to_str(self.inlet_branch_20_name))
        out.append(self._to_str(self.inlet_branch_21_name))
        out.append(self._to_str(self.inlet_branch_22_name))
        out.append(self._to_str(self.inlet_branch_23_name))
        out.append(self._to_str(self.inlet_branch_24_name))
        out.append(self._to_str(self.inlet_branch_25_name))
        out.append(self._to_str(self.inlet_branch_26_name))
        out.append(self._to_str(self.inlet_branch_27_name))
        out.append(self._to_str(self.inlet_branch_28_name))
        out.append(self._to_str(self.inlet_branch_29_name))
        out.append(self._to_str(self.inlet_branch_30_name))
        out.append(self._to_str(self.inlet_branch_31_name))
        out.append(self._to_str(self.inlet_branch_32_name))
        out.append(self._to_str(self.inlet_branch_33_name))
        out.append(self._to_str(self.inlet_branch_34_name))
        out.append(self._to_str(self.inlet_branch_35_name))
        out.append(self._to_str(self.inlet_branch_36_name))
        out.append(self._to_str(self.inlet_branch_37_name))
        out.append(self._to_str(self.inlet_branch_38_name))
        out.append(self._to_str(self.inlet_branch_39_name))
        out.append(self._to_str(self.inlet_branch_40_name))
        out.append(self._to_str(self.inlet_branch_41_name))
        out.append(self._to_str(self.inlet_branch_42_name))
        out.append(self._to_str(self.inlet_branch_43_name))
        out.append(self._to_str(self.inlet_branch_44_name))
        out.append(self._to_str(self.inlet_branch_45_name))
        out.append(self._to_str(self.inlet_branch_46_name))
        out.append(self._to_str(self.inlet_branch_47_name))
        out.append(self._to_str(self.inlet_branch_48_name))
        out.append(self._to_str(self.inlet_branch_49_name))
        out.append(self._to_str(self.inlet_branch_50_name))
        out.append(self._to_str(self.inlet_branch_51_name))
        out.append(self._to_str(self.inlet_branch_52_name))
        out.append(self._to_str(self.inlet_branch_53_name))
        out.append(self._to_str(self.inlet_branch_54_name))
        out.append(self._to_str(self.inlet_branch_55_name))
        out.append(self._to_str(self.inlet_branch_56_name))
        out.append(self._to_str(self.inlet_branch_57_name))
        out.append(self._to_str(self.inlet_branch_58_name))
        out.append(self._to_str(self.inlet_branch_59_name))
        out.append(self._to_str(self.inlet_branch_60_name))
        out.append(self._to_str(self.inlet_branch_61_name))
        out.append(self._to_str(self.inlet_branch_62_name))
        out.append(self._to_str(self.inlet_branch_63_name))
        out.append(self._to_str(self.inlet_branch_64_name))
        out.append(self._to_str(self.inlet_branch_65_name))
        out.append(self._to_str(self.inlet_branch_66_name))
        out.append(self._to_str(self.inlet_branch_67_name))
        out.append(self._to_str(self.inlet_branch_68_name))
        out.append(self._to_str(self.inlet_branch_69_name))
        out.append(self._to_str(self.inlet_branch_70_name))
        out.append(self._to_str(self.inlet_branch_71_name))
        out.append(self._to_str(self.inlet_branch_72_name))
        out.append(self._to_str(self.inlet_branch_73_name))
        out.append(self._to_str(self.inlet_branch_74_name))
        out.append(self._to_str(self.inlet_branch_75_name))
        out.append(self._to_str(self.inlet_branch_76_name))
        out.append(self._to_str(self.inlet_branch_77_name))
        out.append(self._to_str(self.inlet_branch_78_name))
        out.append(self._to_str(self.inlet_branch_79_name))
        out.append(self._to_str(self.inlet_branch_80_name))
        out.append(self._to_str(self.inlet_branch_81_name))
        out.append(self._to_str(self.inlet_branch_82_name))
        out.append(self._to_str(self.inlet_branch_83_name))
        out.append(self._to_str(self.inlet_branch_84_name))
        out.append(self._to_str(self.inlet_branch_85_name))
        out.append(self._to_str(self.inlet_branch_86_name))
        out.append(self._to_str(self.inlet_branch_87_name))
        out.append(self._to_str(self.inlet_branch_88_name))
        out.append(self._to_str(self.inlet_branch_89_name))
        out.append(self._to_str(self.inlet_branch_90_name))
        out.append(self._to_str(self.inlet_branch_91_name))
        out.append(self._to_str(self.inlet_branch_92_name))
        out.append(self._to_str(self.inlet_branch_93_name))
        out.append(self._to_str(self.inlet_branch_94_name))
        out.append(self._to_str(self.inlet_branch_95_name))
        out.append(self._to_str(self.inlet_branch_96_name))
        out.append(self._to_str(self.inlet_branch_97_name))
        out.append(self._to_str(self.inlet_branch_98_name))
        out.append(self._to_str(self.inlet_branch_99_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        out.append(self._to_str(self.inlet_branch_100_name))
        return ",".join(out)