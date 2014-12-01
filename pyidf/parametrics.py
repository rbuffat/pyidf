from collections import OrderedDict

class ParametricSetValueForRun(object):
    """ Corresponds to IDD object `Parametric:SetValueForRun`
        Parametric objects allow a set of multiple simulations to be defined in a single idf
        file. The parametric preprocessor scans the idf for Parametric:* objects then creates
        and runs multiple idf files, one for each defined simulation.
        The core parametric object is Parametric:SetValueForRun which defines the name
        of a parameters and sets the parameter to different values depending on which
        run is being simulated.
    
    """
    internal_name = "Parametric:SetValueForRun"
    field_count = 101
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:SetValueForRun`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Value for Run 1"] = None
        self._data["Value for Run 2"] = None
        self._data["Value for Run 3"] = None
        self._data["Value for Run 4"] = None
        self._data["Value for Run 5"] = None
        self._data["Value for Run 6"] = None
        self._data["Value for Run 7"] = None
        self._data["Value for Run 8"] = None
        self._data["Value for Run 9"] = None
        self._data["Value for Run 10"] = None
        self._data["Value for Run 11"] = None
        self._data["Value for Run 12"] = None
        self._data["Value for Run 13"] = None
        self._data["Value for Run 14"] = None
        self._data["Value for Run 15"] = None
        self._data["Value for Run 16"] = None
        self._data["Value for Run 17"] = None
        self._data["Value for Run 18"] = None
        self._data["Value for Run 19"] = None
        self._data["Value for Run 20"] = None
        self._data["Value for Run 21"] = None
        self._data["Value for Run 22"] = None
        self._data["Value for Run 23"] = None
        self._data["Value for Run 24"] = None
        self._data["Value for Run 25"] = None
        self._data["Value for Run 26"] = None
        self._data["Value for Run 27"] = None
        self._data["Value for Run 28"] = None
        self._data["Value for Run 29"] = None
        self._data["Value for Run 30"] = None
        self._data["Value for Run 31"] = None
        self._data["Value for Run 32"] = None
        self._data["Value for Run 33"] = None
        self._data["Value for Run 34"] = None
        self._data["Value for Run 35"] = None
        self._data["Value for Run 36"] = None
        self._data["Value for Run 37"] = None
        self._data["Value for Run 38"] = None
        self._data["Value for Run 39"] = None
        self._data["Value for Run 40"] = None
        self._data["Value for Run 41"] = None
        self._data["Value for Run 42"] = None
        self._data["Value for Run 43"] = None
        self._data["Value for Run 44"] = None
        self._data["Value for Run 45"] = None
        self._data["Value for Run 46"] = None
        self._data["Value for Run 47"] = None
        self._data["Value for Run 48"] = None
        self._data["Value for Run 49"] = None
        self._data["Value for Run 50"] = None
        self._data["Value for Run 51"] = None
        self._data["Value for Run 52"] = None
        self._data["Value for Run 53"] = None
        self._data["Value for Run 54"] = None
        self._data["Value for Run 55"] = None
        self._data["Value for Run 56"] = None
        self._data["Value for Run 57"] = None
        self._data["Value for Run 58"] = None
        self._data["Value for Run 59"] = None
        self._data["Value for Run 60"] = None
        self._data["Value for Run 61"] = None
        self._data["Value for Run 62"] = None
        self._data["Value for Run 63"] = None
        self._data["Value for Run 64"] = None
        self._data["Value for Run 65"] = None
        self._data["Value for Run 66"] = None
        self._data["Value for Run 67"] = None
        self._data["Value for Run 68"] = None
        self._data["Value for Run 69"] = None
        self._data["Value for Run 70"] = None
        self._data["Value for Run 71"] = None
        self._data["Value for Run 72"] = None
        self._data["Value for Run 73"] = None
        self._data["Value for Run 74"] = None
        self._data["Value for Run 75"] = None
        self._data["Value for Run 76"] = None
        self._data["Value for Run 77"] = None
        self._data["Value for Run 78"] = None
        self._data["Value for Run 79"] = None
        self._data["Value for Run 80"] = None
        self._data["Value for Run 81"] = None
        self._data["Value for Run 82"] = None
        self._data["Value for Run 83"] = None
        self._data["Value for Run 84"] = None
        self._data["Value for Run 85"] = None
        self._data["Value for Run 86"] = None
        self._data["Value for Run 87"] = None
        self._data["Value for Run 88"] = None
        self._data["Value for Run 89"] = None
        self._data["Value for Run 90"] = None
        self._data["Value for Run 91"] = None
        self._data["Value for Run 92"] = None
        self._data["Value for Run 93"] = None
        self._data["Value for Run 94"] = None
        self._data["Value for Run 95"] = None
        self._data["Value for Run 96"] = None
        self._data["Value for Run 97"] = None
        self._data["Value for Run 98"] = None
        self._data["Value for Run 99"] = None
        self._data["Value for Run 100"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_1 = None
        else:
            self.value_for_run_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_2 = None
        else:
            self.value_for_run_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_3 = None
        else:
            self.value_for_run_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_4 = None
        else:
            self.value_for_run_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_5 = None
        else:
            self.value_for_run_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_6 = None
        else:
            self.value_for_run_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_7 = None
        else:
            self.value_for_run_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_8 = None
        else:
            self.value_for_run_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_9 = None
        else:
            self.value_for_run_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_10 = None
        else:
            self.value_for_run_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_11 = None
        else:
            self.value_for_run_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_12 = None
        else:
            self.value_for_run_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_13 = None
        else:
            self.value_for_run_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_14 = None
        else:
            self.value_for_run_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_15 = None
        else:
            self.value_for_run_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_16 = None
        else:
            self.value_for_run_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_17 = None
        else:
            self.value_for_run_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_18 = None
        else:
            self.value_for_run_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_19 = None
        else:
            self.value_for_run_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_20 = None
        else:
            self.value_for_run_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_21 = None
        else:
            self.value_for_run_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_22 = None
        else:
            self.value_for_run_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_23 = None
        else:
            self.value_for_run_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_24 = None
        else:
            self.value_for_run_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_25 = None
        else:
            self.value_for_run_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_26 = None
        else:
            self.value_for_run_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_27 = None
        else:
            self.value_for_run_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_28 = None
        else:
            self.value_for_run_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_29 = None
        else:
            self.value_for_run_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_30 = None
        else:
            self.value_for_run_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_31 = None
        else:
            self.value_for_run_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_32 = None
        else:
            self.value_for_run_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_33 = None
        else:
            self.value_for_run_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_34 = None
        else:
            self.value_for_run_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_35 = None
        else:
            self.value_for_run_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_36 = None
        else:
            self.value_for_run_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_37 = None
        else:
            self.value_for_run_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_38 = None
        else:
            self.value_for_run_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_39 = None
        else:
            self.value_for_run_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_40 = None
        else:
            self.value_for_run_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_41 = None
        else:
            self.value_for_run_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_42 = None
        else:
            self.value_for_run_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_43 = None
        else:
            self.value_for_run_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_44 = None
        else:
            self.value_for_run_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_45 = None
        else:
            self.value_for_run_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_46 = None
        else:
            self.value_for_run_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_47 = None
        else:
            self.value_for_run_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_48 = None
        else:
            self.value_for_run_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_49 = None
        else:
            self.value_for_run_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_50 = None
        else:
            self.value_for_run_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_51 = None
        else:
            self.value_for_run_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_52 = None
        else:
            self.value_for_run_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_53 = None
        else:
            self.value_for_run_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_54 = None
        else:
            self.value_for_run_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_55 = None
        else:
            self.value_for_run_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_56 = None
        else:
            self.value_for_run_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_57 = None
        else:
            self.value_for_run_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_58 = None
        else:
            self.value_for_run_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_59 = None
        else:
            self.value_for_run_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_60 = None
        else:
            self.value_for_run_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_61 = None
        else:
            self.value_for_run_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_62 = None
        else:
            self.value_for_run_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_63 = None
        else:
            self.value_for_run_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_64 = None
        else:
            self.value_for_run_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_65 = None
        else:
            self.value_for_run_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_66 = None
        else:
            self.value_for_run_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_67 = None
        else:
            self.value_for_run_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_68 = None
        else:
            self.value_for_run_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_69 = None
        else:
            self.value_for_run_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_70 = None
        else:
            self.value_for_run_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_71 = None
        else:
            self.value_for_run_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_72 = None
        else:
            self.value_for_run_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_73 = None
        else:
            self.value_for_run_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_74 = None
        else:
            self.value_for_run_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_75 = None
        else:
            self.value_for_run_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_76 = None
        else:
            self.value_for_run_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_77 = None
        else:
            self.value_for_run_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_78 = None
        else:
            self.value_for_run_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_79 = None
        else:
            self.value_for_run_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_80 = None
        else:
            self.value_for_run_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_81 = None
        else:
            self.value_for_run_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_82 = None
        else:
            self.value_for_run_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_83 = None
        else:
            self.value_for_run_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_84 = None
        else:
            self.value_for_run_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_85 = None
        else:
            self.value_for_run_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_86 = None
        else:
            self.value_for_run_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_87 = None
        else:
            self.value_for_run_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_88 = None
        else:
            self.value_for_run_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_89 = None
        else:
            self.value_for_run_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_90 = None
        else:
            self.value_for_run_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_91 = None
        else:
            self.value_for_run_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_92 = None
        else:
            self.value_for_run_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_93 = None
        else:
            self.value_for_run_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_94 = None
        else:
            self.value_for_run_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_95 = None
        else:
            self.value_for_run_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_96 = None
        else:
            self.value_for_run_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_97 = None
        else:
            self.value_for_run_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_98 = None
        else:
            self.value_for_run_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_99 = None
        else:
            self.value_for_run_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.value_for_run_100 = None
        else:
            self.value_for_run_100 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`
        Parameter Name
        Must begin with the dollar sign character. The second character must be a letter.
        Remaining characters may only be letters or numbers. No spaces allowed.

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def value_for_run_1(self):
        """Get value_for_run_1

        Returns:
            str: the value of `value_for_run_1` or None if not set
        """
        return self._data["Value for Run 1"]

    @value_for_run_1.setter
    def value_for_run_1(self, value=None):
        """  Corresponds to IDD Field `Value for Run 1`

        Args:
            value (str): value for IDD Field `Value for Run 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_1`')
        self._data["Value for Run 1"] = value

    @property
    def value_for_run_2(self):
        """Get value_for_run_2

        Returns:
            str: the value of `value_for_run_2` or None if not set
        """
        return self._data["Value for Run 2"]

    @value_for_run_2.setter
    def value_for_run_2(self, value=None):
        """  Corresponds to IDD Field `Value for Run 2`

        Args:
            value (str): value for IDD Field `Value for Run 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_2`')
        self._data["Value for Run 2"] = value

    @property
    def value_for_run_3(self):
        """Get value_for_run_3

        Returns:
            str: the value of `value_for_run_3` or None if not set
        """
        return self._data["Value for Run 3"]

    @value_for_run_3.setter
    def value_for_run_3(self, value=None):
        """  Corresponds to IDD Field `Value for Run 3`

        Args:
            value (str): value for IDD Field `Value for Run 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_3`')
        self._data["Value for Run 3"] = value

    @property
    def value_for_run_4(self):
        """Get value_for_run_4

        Returns:
            str: the value of `value_for_run_4` or None if not set
        """
        return self._data["Value for Run 4"]

    @value_for_run_4.setter
    def value_for_run_4(self, value=None):
        """  Corresponds to IDD Field `Value for Run 4`

        Args:
            value (str): value for IDD Field `Value for Run 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_4`')
        self._data["Value for Run 4"] = value

    @property
    def value_for_run_5(self):
        """Get value_for_run_5

        Returns:
            str: the value of `value_for_run_5` or None if not set
        """
        return self._data["Value for Run 5"]

    @value_for_run_5.setter
    def value_for_run_5(self, value=None):
        """  Corresponds to IDD Field `Value for Run 5`

        Args:
            value (str): value for IDD Field `Value for Run 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_5`')
        self._data["Value for Run 5"] = value

    @property
    def value_for_run_6(self):
        """Get value_for_run_6

        Returns:
            str: the value of `value_for_run_6` or None if not set
        """
        return self._data["Value for Run 6"]

    @value_for_run_6.setter
    def value_for_run_6(self, value=None):
        """  Corresponds to IDD Field `Value for Run 6`

        Args:
            value (str): value for IDD Field `Value for Run 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_6`')
        self._data["Value for Run 6"] = value

    @property
    def value_for_run_7(self):
        """Get value_for_run_7

        Returns:
            str: the value of `value_for_run_7` or None if not set
        """
        return self._data["Value for Run 7"]

    @value_for_run_7.setter
    def value_for_run_7(self, value=None):
        """  Corresponds to IDD Field `Value for Run 7`

        Args:
            value (str): value for IDD Field `Value for Run 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_7`')
        self._data["Value for Run 7"] = value

    @property
    def value_for_run_8(self):
        """Get value_for_run_8

        Returns:
            str: the value of `value_for_run_8` or None if not set
        """
        return self._data["Value for Run 8"]

    @value_for_run_8.setter
    def value_for_run_8(self, value=None):
        """  Corresponds to IDD Field `Value for Run 8`

        Args:
            value (str): value for IDD Field `Value for Run 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_8`')
        self._data["Value for Run 8"] = value

    @property
    def value_for_run_9(self):
        """Get value_for_run_9

        Returns:
            str: the value of `value_for_run_9` or None if not set
        """
        return self._data["Value for Run 9"]

    @value_for_run_9.setter
    def value_for_run_9(self, value=None):
        """  Corresponds to IDD Field `Value for Run 9`

        Args:
            value (str): value for IDD Field `Value for Run 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_9`')
        self._data["Value for Run 9"] = value

    @property
    def value_for_run_10(self):
        """Get value_for_run_10

        Returns:
            str: the value of `value_for_run_10` or None if not set
        """
        return self._data["Value for Run 10"]

    @value_for_run_10.setter
    def value_for_run_10(self, value=None):
        """  Corresponds to IDD Field `Value for Run 10`

        Args:
            value (str): value for IDD Field `Value for Run 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_10`')
        self._data["Value for Run 10"] = value

    @property
    def value_for_run_11(self):
        """Get value_for_run_11

        Returns:
            str: the value of `value_for_run_11` or None if not set
        """
        return self._data["Value for Run 11"]

    @value_for_run_11.setter
    def value_for_run_11(self, value=None):
        """  Corresponds to IDD Field `Value for Run 11`

        Args:
            value (str): value for IDD Field `Value for Run 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_11`')
        self._data["Value for Run 11"] = value

    @property
    def value_for_run_12(self):
        """Get value_for_run_12

        Returns:
            str: the value of `value_for_run_12` or None if not set
        """
        return self._data["Value for Run 12"]

    @value_for_run_12.setter
    def value_for_run_12(self, value=None):
        """  Corresponds to IDD Field `Value for Run 12`

        Args:
            value (str): value for IDD Field `Value for Run 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_12`')
        self._data["Value for Run 12"] = value

    @property
    def value_for_run_13(self):
        """Get value_for_run_13

        Returns:
            str: the value of `value_for_run_13` or None if not set
        """
        return self._data["Value for Run 13"]

    @value_for_run_13.setter
    def value_for_run_13(self, value=None):
        """  Corresponds to IDD Field `Value for Run 13`

        Args:
            value (str): value for IDD Field `Value for Run 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_13`')
        self._data["Value for Run 13"] = value

    @property
    def value_for_run_14(self):
        """Get value_for_run_14

        Returns:
            str: the value of `value_for_run_14` or None if not set
        """
        return self._data["Value for Run 14"]

    @value_for_run_14.setter
    def value_for_run_14(self, value=None):
        """  Corresponds to IDD Field `Value for Run 14`

        Args:
            value (str): value for IDD Field `Value for Run 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_14`')
        self._data["Value for Run 14"] = value

    @property
    def value_for_run_15(self):
        """Get value_for_run_15

        Returns:
            str: the value of `value_for_run_15` or None if not set
        """
        return self._data["Value for Run 15"]

    @value_for_run_15.setter
    def value_for_run_15(self, value=None):
        """  Corresponds to IDD Field `Value for Run 15`

        Args:
            value (str): value for IDD Field `Value for Run 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_15`')
        self._data["Value for Run 15"] = value

    @property
    def value_for_run_16(self):
        """Get value_for_run_16

        Returns:
            str: the value of `value_for_run_16` or None if not set
        """
        return self._data["Value for Run 16"]

    @value_for_run_16.setter
    def value_for_run_16(self, value=None):
        """  Corresponds to IDD Field `Value for Run 16`

        Args:
            value (str): value for IDD Field `Value for Run 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_16`')
        self._data["Value for Run 16"] = value

    @property
    def value_for_run_17(self):
        """Get value_for_run_17

        Returns:
            str: the value of `value_for_run_17` or None if not set
        """
        return self._data["Value for Run 17"]

    @value_for_run_17.setter
    def value_for_run_17(self, value=None):
        """  Corresponds to IDD Field `Value for Run 17`

        Args:
            value (str): value for IDD Field `Value for Run 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_17`')
        self._data["Value for Run 17"] = value

    @property
    def value_for_run_18(self):
        """Get value_for_run_18

        Returns:
            str: the value of `value_for_run_18` or None if not set
        """
        return self._data["Value for Run 18"]

    @value_for_run_18.setter
    def value_for_run_18(self, value=None):
        """  Corresponds to IDD Field `Value for Run 18`

        Args:
            value (str): value for IDD Field `Value for Run 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_18`')
        self._data["Value for Run 18"] = value

    @property
    def value_for_run_19(self):
        """Get value_for_run_19

        Returns:
            str: the value of `value_for_run_19` or None if not set
        """
        return self._data["Value for Run 19"]

    @value_for_run_19.setter
    def value_for_run_19(self, value=None):
        """  Corresponds to IDD Field `Value for Run 19`

        Args:
            value (str): value for IDD Field `Value for Run 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_19`')
        self._data["Value for Run 19"] = value

    @property
    def value_for_run_20(self):
        """Get value_for_run_20

        Returns:
            str: the value of `value_for_run_20` or None if not set
        """
        return self._data["Value for Run 20"]

    @value_for_run_20.setter
    def value_for_run_20(self, value=None):
        """  Corresponds to IDD Field `Value for Run 20`

        Args:
            value (str): value for IDD Field `Value for Run 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_20`')
        self._data["Value for Run 20"] = value

    @property
    def value_for_run_21(self):
        """Get value_for_run_21

        Returns:
            str: the value of `value_for_run_21` or None if not set
        """
        return self._data["Value for Run 21"]

    @value_for_run_21.setter
    def value_for_run_21(self, value=None):
        """  Corresponds to IDD Field `Value for Run 21`

        Args:
            value (str): value for IDD Field `Value for Run 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_21`')
        self._data["Value for Run 21"] = value

    @property
    def value_for_run_22(self):
        """Get value_for_run_22

        Returns:
            str: the value of `value_for_run_22` or None if not set
        """
        return self._data["Value for Run 22"]

    @value_for_run_22.setter
    def value_for_run_22(self, value=None):
        """  Corresponds to IDD Field `Value for Run 22`

        Args:
            value (str): value for IDD Field `Value for Run 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_22`')
        self._data["Value for Run 22"] = value

    @property
    def value_for_run_23(self):
        """Get value_for_run_23

        Returns:
            str: the value of `value_for_run_23` or None if not set
        """
        return self._data["Value for Run 23"]

    @value_for_run_23.setter
    def value_for_run_23(self, value=None):
        """  Corresponds to IDD Field `Value for Run 23`

        Args:
            value (str): value for IDD Field `Value for Run 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_23`')
        self._data["Value for Run 23"] = value

    @property
    def value_for_run_24(self):
        """Get value_for_run_24

        Returns:
            str: the value of `value_for_run_24` or None if not set
        """
        return self._data["Value for Run 24"]

    @value_for_run_24.setter
    def value_for_run_24(self, value=None):
        """  Corresponds to IDD Field `Value for Run 24`

        Args:
            value (str): value for IDD Field `Value for Run 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_24`')
        self._data["Value for Run 24"] = value

    @property
    def value_for_run_25(self):
        """Get value_for_run_25

        Returns:
            str: the value of `value_for_run_25` or None if not set
        """
        return self._data["Value for Run 25"]

    @value_for_run_25.setter
    def value_for_run_25(self, value=None):
        """  Corresponds to IDD Field `Value for Run 25`

        Args:
            value (str): value for IDD Field `Value for Run 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_25`')
        self._data["Value for Run 25"] = value

    @property
    def value_for_run_26(self):
        """Get value_for_run_26

        Returns:
            str: the value of `value_for_run_26` or None if not set
        """
        return self._data["Value for Run 26"]

    @value_for_run_26.setter
    def value_for_run_26(self, value=None):
        """  Corresponds to IDD Field `Value for Run 26`

        Args:
            value (str): value for IDD Field `Value for Run 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_26`')
        self._data["Value for Run 26"] = value

    @property
    def value_for_run_27(self):
        """Get value_for_run_27

        Returns:
            str: the value of `value_for_run_27` or None if not set
        """
        return self._data["Value for Run 27"]

    @value_for_run_27.setter
    def value_for_run_27(self, value=None):
        """  Corresponds to IDD Field `Value for Run 27`

        Args:
            value (str): value for IDD Field `Value for Run 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_27`')
        self._data["Value for Run 27"] = value

    @property
    def value_for_run_28(self):
        """Get value_for_run_28

        Returns:
            str: the value of `value_for_run_28` or None if not set
        """
        return self._data["Value for Run 28"]

    @value_for_run_28.setter
    def value_for_run_28(self, value=None):
        """  Corresponds to IDD Field `Value for Run 28`

        Args:
            value (str): value for IDD Field `Value for Run 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_28`')
        self._data["Value for Run 28"] = value

    @property
    def value_for_run_29(self):
        """Get value_for_run_29

        Returns:
            str: the value of `value_for_run_29` or None if not set
        """
        return self._data["Value for Run 29"]

    @value_for_run_29.setter
    def value_for_run_29(self, value=None):
        """  Corresponds to IDD Field `Value for Run 29`

        Args:
            value (str): value for IDD Field `Value for Run 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_29`')
        self._data["Value for Run 29"] = value

    @property
    def value_for_run_30(self):
        """Get value_for_run_30

        Returns:
            str: the value of `value_for_run_30` or None if not set
        """
        return self._data["Value for Run 30"]

    @value_for_run_30.setter
    def value_for_run_30(self, value=None):
        """  Corresponds to IDD Field `Value for Run 30`

        Args:
            value (str): value for IDD Field `Value for Run 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_30`')
        self._data["Value for Run 30"] = value

    @property
    def value_for_run_31(self):
        """Get value_for_run_31

        Returns:
            str: the value of `value_for_run_31` or None if not set
        """
        return self._data["Value for Run 31"]

    @value_for_run_31.setter
    def value_for_run_31(self, value=None):
        """  Corresponds to IDD Field `Value for Run 31`

        Args:
            value (str): value for IDD Field `Value for Run 31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_31`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_31`')
        self._data["Value for Run 31"] = value

    @property
    def value_for_run_32(self):
        """Get value_for_run_32

        Returns:
            str: the value of `value_for_run_32` or None if not set
        """
        return self._data["Value for Run 32"]

    @value_for_run_32.setter
    def value_for_run_32(self, value=None):
        """  Corresponds to IDD Field `Value for Run 32`

        Args:
            value (str): value for IDD Field `Value for Run 32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_32`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_32`')
        self._data["Value for Run 32"] = value

    @property
    def value_for_run_33(self):
        """Get value_for_run_33

        Returns:
            str: the value of `value_for_run_33` or None if not set
        """
        return self._data["Value for Run 33"]

    @value_for_run_33.setter
    def value_for_run_33(self, value=None):
        """  Corresponds to IDD Field `Value for Run 33`

        Args:
            value (str): value for IDD Field `Value for Run 33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_33`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_33`')
        self._data["Value for Run 33"] = value

    @property
    def value_for_run_34(self):
        """Get value_for_run_34

        Returns:
            str: the value of `value_for_run_34` or None if not set
        """
        return self._data["Value for Run 34"]

    @value_for_run_34.setter
    def value_for_run_34(self, value=None):
        """  Corresponds to IDD Field `Value for Run 34`

        Args:
            value (str): value for IDD Field `Value for Run 34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_34`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_34`')
        self._data["Value for Run 34"] = value

    @property
    def value_for_run_35(self):
        """Get value_for_run_35

        Returns:
            str: the value of `value_for_run_35` or None if not set
        """
        return self._data["Value for Run 35"]

    @value_for_run_35.setter
    def value_for_run_35(self, value=None):
        """  Corresponds to IDD Field `Value for Run 35`

        Args:
            value (str): value for IDD Field `Value for Run 35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_35`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_35`')
        self._data["Value for Run 35"] = value

    @property
    def value_for_run_36(self):
        """Get value_for_run_36

        Returns:
            str: the value of `value_for_run_36` or None if not set
        """
        return self._data["Value for Run 36"]

    @value_for_run_36.setter
    def value_for_run_36(self, value=None):
        """  Corresponds to IDD Field `Value for Run 36`

        Args:
            value (str): value for IDD Field `Value for Run 36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_36`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_36`')
        self._data["Value for Run 36"] = value

    @property
    def value_for_run_37(self):
        """Get value_for_run_37

        Returns:
            str: the value of `value_for_run_37` or None if not set
        """
        return self._data["Value for Run 37"]

    @value_for_run_37.setter
    def value_for_run_37(self, value=None):
        """  Corresponds to IDD Field `Value for Run 37`

        Args:
            value (str): value for IDD Field `Value for Run 37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_37`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_37`')
        self._data["Value for Run 37"] = value

    @property
    def value_for_run_38(self):
        """Get value_for_run_38

        Returns:
            str: the value of `value_for_run_38` or None if not set
        """
        return self._data["Value for Run 38"]

    @value_for_run_38.setter
    def value_for_run_38(self, value=None):
        """  Corresponds to IDD Field `Value for Run 38`

        Args:
            value (str): value for IDD Field `Value for Run 38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_38`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_38`')
        self._data["Value for Run 38"] = value

    @property
    def value_for_run_39(self):
        """Get value_for_run_39

        Returns:
            str: the value of `value_for_run_39` or None if not set
        """
        return self._data["Value for Run 39"]

    @value_for_run_39.setter
    def value_for_run_39(self, value=None):
        """  Corresponds to IDD Field `Value for Run 39`

        Args:
            value (str): value for IDD Field `Value for Run 39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_39`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_39`')
        self._data["Value for Run 39"] = value

    @property
    def value_for_run_40(self):
        """Get value_for_run_40

        Returns:
            str: the value of `value_for_run_40` or None if not set
        """
        return self._data["Value for Run 40"]

    @value_for_run_40.setter
    def value_for_run_40(self, value=None):
        """  Corresponds to IDD Field `Value for Run 40`

        Args:
            value (str): value for IDD Field `Value for Run 40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_40`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_40`')
        self._data["Value for Run 40"] = value

    @property
    def value_for_run_41(self):
        """Get value_for_run_41

        Returns:
            str: the value of `value_for_run_41` or None if not set
        """
        return self._data["Value for Run 41"]

    @value_for_run_41.setter
    def value_for_run_41(self, value=None):
        """  Corresponds to IDD Field `Value for Run 41`

        Args:
            value (str): value for IDD Field `Value for Run 41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_41`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_41`')
        self._data["Value for Run 41"] = value

    @property
    def value_for_run_42(self):
        """Get value_for_run_42

        Returns:
            str: the value of `value_for_run_42` or None if not set
        """
        return self._data["Value for Run 42"]

    @value_for_run_42.setter
    def value_for_run_42(self, value=None):
        """  Corresponds to IDD Field `Value for Run 42`

        Args:
            value (str): value for IDD Field `Value for Run 42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_42`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_42`')
        self._data["Value for Run 42"] = value

    @property
    def value_for_run_43(self):
        """Get value_for_run_43

        Returns:
            str: the value of `value_for_run_43` or None if not set
        """
        return self._data["Value for Run 43"]

    @value_for_run_43.setter
    def value_for_run_43(self, value=None):
        """  Corresponds to IDD Field `Value for Run 43`

        Args:
            value (str): value for IDD Field `Value for Run 43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_43`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_43`')
        self._data["Value for Run 43"] = value

    @property
    def value_for_run_44(self):
        """Get value_for_run_44

        Returns:
            str: the value of `value_for_run_44` or None if not set
        """
        return self._data["Value for Run 44"]

    @value_for_run_44.setter
    def value_for_run_44(self, value=None):
        """  Corresponds to IDD Field `Value for Run 44`

        Args:
            value (str): value for IDD Field `Value for Run 44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_44`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_44`')
        self._data["Value for Run 44"] = value

    @property
    def value_for_run_45(self):
        """Get value_for_run_45

        Returns:
            str: the value of `value_for_run_45` or None if not set
        """
        return self._data["Value for Run 45"]

    @value_for_run_45.setter
    def value_for_run_45(self, value=None):
        """  Corresponds to IDD Field `Value for Run 45`

        Args:
            value (str): value for IDD Field `Value for Run 45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_45`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_45`')
        self._data["Value for Run 45"] = value

    @property
    def value_for_run_46(self):
        """Get value_for_run_46

        Returns:
            str: the value of `value_for_run_46` or None if not set
        """
        return self._data["Value for Run 46"]

    @value_for_run_46.setter
    def value_for_run_46(self, value=None):
        """  Corresponds to IDD Field `Value for Run 46`

        Args:
            value (str): value for IDD Field `Value for Run 46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_46`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_46`')
        self._data["Value for Run 46"] = value

    @property
    def value_for_run_47(self):
        """Get value_for_run_47

        Returns:
            str: the value of `value_for_run_47` or None if not set
        """
        return self._data["Value for Run 47"]

    @value_for_run_47.setter
    def value_for_run_47(self, value=None):
        """  Corresponds to IDD Field `Value for Run 47`

        Args:
            value (str): value for IDD Field `Value for Run 47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_47`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_47`')
        self._data["Value for Run 47"] = value

    @property
    def value_for_run_48(self):
        """Get value_for_run_48

        Returns:
            str: the value of `value_for_run_48` or None if not set
        """
        return self._data["Value for Run 48"]

    @value_for_run_48.setter
    def value_for_run_48(self, value=None):
        """  Corresponds to IDD Field `Value for Run 48`

        Args:
            value (str): value for IDD Field `Value for Run 48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_48`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_48`')
        self._data["Value for Run 48"] = value

    @property
    def value_for_run_49(self):
        """Get value_for_run_49

        Returns:
            str: the value of `value_for_run_49` or None if not set
        """
        return self._data["Value for Run 49"]

    @value_for_run_49.setter
    def value_for_run_49(self, value=None):
        """  Corresponds to IDD Field `Value for Run 49`

        Args:
            value (str): value for IDD Field `Value for Run 49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_49`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_49`')
        self._data["Value for Run 49"] = value

    @property
    def value_for_run_50(self):
        """Get value_for_run_50

        Returns:
            str: the value of `value_for_run_50` or None if not set
        """
        return self._data["Value for Run 50"]

    @value_for_run_50.setter
    def value_for_run_50(self, value=None):
        """  Corresponds to IDD Field `Value for Run 50`

        Args:
            value (str): value for IDD Field `Value for Run 50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_50`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_50`')
        self._data["Value for Run 50"] = value

    @property
    def value_for_run_51(self):
        """Get value_for_run_51

        Returns:
            str: the value of `value_for_run_51` or None if not set
        """
        return self._data["Value for Run 51"]

    @value_for_run_51.setter
    def value_for_run_51(self, value=None):
        """  Corresponds to IDD Field `Value for Run 51`

        Args:
            value (str): value for IDD Field `Value for Run 51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_51`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_51`')
        self._data["Value for Run 51"] = value

    @property
    def value_for_run_52(self):
        """Get value_for_run_52

        Returns:
            str: the value of `value_for_run_52` or None if not set
        """
        return self._data["Value for Run 52"]

    @value_for_run_52.setter
    def value_for_run_52(self, value=None):
        """  Corresponds to IDD Field `Value for Run 52`

        Args:
            value (str): value for IDD Field `Value for Run 52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_52`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_52`')
        self._data["Value for Run 52"] = value

    @property
    def value_for_run_53(self):
        """Get value_for_run_53

        Returns:
            str: the value of `value_for_run_53` or None if not set
        """
        return self._data["Value for Run 53"]

    @value_for_run_53.setter
    def value_for_run_53(self, value=None):
        """  Corresponds to IDD Field `Value for Run 53`

        Args:
            value (str): value for IDD Field `Value for Run 53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_53`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_53`')
        self._data["Value for Run 53"] = value

    @property
    def value_for_run_54(self):
        """Get value_for_run_54

        Returns:
            str: the value of `value_for_run_54` or None if not set
        """
        return self._data["Value for Run 54"]

    @value_for_run_54.setter
    def value_for_run_54(self, value=None):
        """  Corresponds to IDD Field `Value for Run 54`

        Args:
            value (str): value for IDD Field `Value for Run 54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_54`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_54`')
        self._data["Value for Run 54"] = value

    @property
    def value_for_run_55(self):
        """Get value_for_run_55

        Returns:
            str: the value of `value_for_run_55` or None if not set
        """
        return self._data["Value for Run 55"]

    @value_for_run_55.setter
    def value_for_run_55(self, value=None):
        """  Corresponds to IDD Field `Value for Run 55`

        Args:
            value (str): value for IDD Field `Value for Run 55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_55`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_55`')
        self._data["Value for Run 55"] = value

    @property
    def value_for_run_56(self):
        """Get value_for_run_56

        Returns:
            str: the value of `value_for_run_56` or None if not set
        """
        return self._data["Value for Run 56"]

    @value_for_run_56.setter
    def value_for_run_56(self, value=None):
        """  Corresponds to IDD Field `Value for Run 56`

        Args:
            value (str): value for IDD Field `Value for Run 56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_56`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_56`')
        self._data["Value for Run 56"] = value

    @property
    def value_for_run_57(self):
        """Get value_for_run_57

        Returns:
            str: the value of `value_for_run_57` or None if not set
        """
        return self._data["Value for Run 57"]

    @value_for_run_57.setter
    def value_for_run_57(self, value=None):
        """  Corresponds to IDD Field `Value for Run 57`

        Args:
            value (str): value for IDD Field `Value for Run 57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_57`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_57`')
        self._data["Value for Run 57"] = value

    @property
    def value_for_run_58(self):
        """Get value_for_run_58

        Returns:
            str: the value of `value_for_run_58` or None if not set
        """
        return self._data["Value for Run 58"]

    @value_for_run_58.setter
    def value_for_run_58(self, value=None):
        """  Corresponds to IDD Field `Value for Run 58`

        Args:
            value (str): value for IDD Field `Value for Run 58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_58`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_58`')
        self._data["Value for Run 58"] = value

    @property
    def value_for_run_59(self):
        """Get value_for_run_59

        Returns:
            str: the value of `value_for_run_59` or None if not set
        """
        return self._data["Value for Run 59"]

    @value_for_run_59.setter
    def value_for_run_59(self, value=None):
        """  Corresponds to IDD Field `Value for Run 59`

        Args:
            value (str): value for IDD Field `Value for Run 59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_59`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_59`')
        self._data["Value for Run 59"] = value

    @property
    def value_for_run_60(self):
        """Get value_for_run_60

        Returns:
            str: the value of `value_for_run_60` or None if not set
        """
        return self._data["Value for Run 60"]

    @value_for_run_60.setter
    def value_for_run_60(self, value=None):
        """  Corresponds to IDD Field `Value for Run 60`

        Args:
            value (str): value for IDD Field `Value for Run 60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_60`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_60`')
        self._data["Value for Run 60"] = value

    @property
    def value_for_run_61(self):
        """Get value_for_run_61

        Returns:
            str: the value of `value_for_run_61` or None if not set
        """
        return self._data["Value for Run 61"]

    @value_for_run_61.setter
    def value_for_run_61(self, value=None):
        """  Corresponds to IDD Field `Value for Run 61`

        Args:
            value (str): value for IDD Field `Value for Run 61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_61`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_61`')
        self._data["Value for Run 61"] = value

    @property
    def value_for_run_62(self):
        """Get value_for_run_62

        Returns:
            str: the value of `value_for_run_62` or None if not set
        """
        return self._data["Value for Run 62"]

    @value_for_run_62.setter
    def value_for_run_62(self, value=None):
        """  Corresponds to IDD Field `Value for Run 62`

        Args:
            value (str): value for IDD Field `Value for Run 62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_62`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_62`')
        self._data["Value for Run 62"] = value

    @property
    def value_for_run_63(self):
        """Get value_for_run_63

        Returns:
            str: the value of `value_for_run_63` or None if not set
        """
        return self._data["Value for Run 63"]

    @value_for_run_63.setter
    def value_for_run_63(self, value=None):
        """  Corresponds to IDD Field `Value for Run 63`

        Args:
            value (str): value for IDD Field `Value for Run 63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_63`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_63`')
        self._data["Value for Run 63"] = value

    @property
    def value_for_run_64(self):
        """Get value_for_run_64

        Returns:
            str: the value of `value_for_run_64` or None if not set
        """
        return self._data["Value for Run 64"]

    @value_for_run_64.setter
    def value_for_run_64(self, value=None):
        """  Corresponds to IDD Field `Value for Run 64`

        Args:
            value (str): value for IDD Field `Value for Run 64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_64`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_64`')
        self._data["Value for Run 64"] = value

    @property
    def value_for_run_65(self):
        """Get value_for_run_65

        Returns:
            str: the value of `value_for_run_65` or None if not set
        """
        return self._data["Value for Run 65"]

    @value_for_run_65.setter
    def value_for_run_65(self, value=None):
        """  Corresponds to IDD Field `Value for Run 65`

        Args:
            value (str): value for IDD Field `Value for Run 65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_65`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_65`')
        self._data["Value for Run 65"] = value

    @property
    def value_for_run_66(self):
        """Get value_for_run_66

        Returns:
            str: the value of `value_for_run_66` or None if not set
        """
        return self._data["Value for Run 66"]

    @value_for_run_66.setter
    def value_for_run_66(self, value=None):
        """  Corresponds to IDD Field `Value for Run 66`

        Args:
            value (str): value for IDD Field `Value for Run 66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_66`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_66`')
        self._data["Value for Run 66"] = value

    @property
    def value_for_run_67(self):
        """Get value_for_run_67

        Returns:
            str: the value of `value_for_run_67` or None if not set
        """
        return self._data["Value for Run 67"]

    @value_for_run_67.setter
    def value_for_run_67(self, value=None):
        """  Corresponds to IDD Field `Value for Run 67`

        Args:
            value (str): value for IDD Field `Value for Run 67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_67`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_67`')
        self._data["Value for Run 67"] = value

    @property
    def value_for_run_68(self):
        """Get value_for_run_68

        Returns:
            str: the value of `value_for_run_68` or None if not set
        """
        return self._data["Value for Run 68"]

    @value_for_run_68.setter
    def value_for_run_68(self, value=None):
        """  Corresponds to IDD Field `Value for Run 68`

        Args:
            value (str): value for IDD Field `Value for Run 68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_68`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_68`')
        self._data["Value for Run 68"] = value

    @property
    def value_for_run_69(self):
        """Get value_for_run_69

        Returns:
            str: the value of `value_for_run_69` or None if not set
        """
        return self._data["Value for Run 69"]

    @value_for_run_69.setter
    def value_for_run_69(self, value=None):
        """  Corresponds to IDD Field `Value for Run 69`

        Args:
            value (str): value for IDD Field `Value for Run 69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_69`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_69`')
        self._data["Value for Run 69"] = value

    @property
    def value_for_run_70(self):
        """Get value_for_run_70

        Returns:
            str: the value of `value_for_run_70` or None if not set
        """
        return self._data["Value for Run 70"]

    @value_for_run_70.setter
    def value_for_run_70(self, value=None):
        """  Corresponds to IDD Field `Value for Run 70`

        Args:
            value (str): value for IDD Field `Value for Run 70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_70`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_70`')
        self._data["Value for Run 70"] = value

    @property
    def value_for_run_71(self):
        """Get value_for_run_71

        Returns:
            str: the value of `value_for_run_71` or None if not set
        """
        return self._data["Value for Run 71"]

    @value_for_run_71.setter
    def value_for_run_71(self, value=None):
        """  Corresponds to IDD Field `Value for Run 71`

        Args:
            value (str): value for IDD Field `Value for Run 71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_71`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_71`')
        self._data["Value for Run 71"] = value

    @property
    def value_for_run_72(self):
        """Get value_for_run_72

        Returns:
            str: the value of `value_for_run_72` or None if not set
        """
        return self._data["Value for Run 72"]

    @value_for_run_72.setter
    def value_for_run_72(self, value=None):
        """  Corresponds to IDD Field `Value for Run 72`

        Args:
            value (str): value for IDD Field `Value for Run 72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_72`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_72`')
        self._data["Value for Run 72"] = value

    @property
    def value_for_run_73(self):
        """Get value_for_run_73

        Returns:
            str: the value of `value_for_run_73` or None if not set
        """
        return self._data["Value for Run 73"]

    @value_for_run_73.setter
    def value_for_run_73(self, value=None):
        """  Corresponds to IDD Field `Value for Run 73`

        Args:
            value (str): value for IDD Field `Value for Run 73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_73`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_73`')
        self._data["Value for Run 73"] = value

    @property
    def value_for_run_74(self):
        """Get value_for_run_74

        Returns:
            str: the value of `value_for_run_74` or None if not set
        """
        return self._data["Value for Run 74"]

    @value_for_run_74.setter
    def value_for_run_74(self, value=None):
        """  Corresponds to IDD Field `Value for Run 74`

        Args:
            value (str): value for IDD Field `Value for Run 74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_74`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_74`')
        self._data["Value for Run 74"] = value

    @property
    def value_for_run_75(self):
        """Get value_for_run_75

        Returns:
            str: the value of `value_for_run_75` or None if not set
        """
        return self._data["Value for Run 75"]

    @value_for_run_75.setter
    def value_for_run_75(self, value=None):
        """  Corresponds to IDD Field `Value for Run 75`

        Args:
            value (str): value for IDD Field `Value for Run 75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_75`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_75`')
        self._data["Value for Run 75"] = value

    @property
    def value_for_run_76(self):
        """Get value_for_run_76

        Returns:
            str: the value of `value_for_run_76` or None if not set
        """
        return self._data["Value for Run 76"]

    @value_for_run_76.setter
    def value_for_run_76(self, value=None):
        """  Corresponds to IDD Field `Value for Run 76`

        Args:
            value (str): value for IDD Field `Value for Run 76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_76`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_76`')
        self._data["Value for Run 76"] = value

    @property
    def value_for_run_77(self):
        """Get value_for_run_77

        Returns:
            str: the value of `value_for_run_77` or None if not set
        """
        return self._data["Value for Run 77"]

    @value_for_run_77.setter
    def value_for_run_77(self, value=None):
        """  Corresponds to IDD Field `Value for Run 77`

        Args:
            value (str): value for IDD Field `Value for Run 77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_77`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_77`')
        self._data["Value for Run 77"] = value

    @property
    def value_for_run_78(self):
        """Get value_for_run_78

        Returns:
            str: the value of `value_for_run_78` or None if not set
        """
        return self._data["Value for Run 78"]

    @value_for_run_78.setter
    def value_for_run_78(self, value=None):
        """  Corresponds to IDD Field `Value for Run 78`

        Args:
            value (str): value for IDD Field `Value for Run 78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_78`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_78`')
        self._data["Value for Run 78"] = value

    @property
    def value_for_run_79(self):
        """Get value_for_run_79

        Returns:
            str: the value of `value_for_run_79` or None if not set
        """
        return self._data["Value for Run 79"]

    @value_for_run_79.setter
    def value_for_run_79(self, value=None):
        """  Corresponds to IDD Field `Value for Run 79`

        Args:
            value (str): value for IDD Field `Value for Run 79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_79`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_79`')
        self._data["Value for Run 79"] = value

    @property
    def value_for_run_80(self):
        """Get value_for_run_80

        Returns:
            str: the value of `value_for_run_80` or None if not set
        """
        return self._data["Value for Run 80"]

    @value_for_run_80.setter
    def value_for_run_80(self, value=None):
        """  Corresponds to IDD Field `Value for Run 80`

        Args:
            value (str): value for IDD Field `Value for Run 80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_80`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_80`')
        self._data["Value for Run 80"] = value

    @property
    def value_for_run_81(self):
        """Get value_for_run_81

        Returns:
            str: the value of `value_for_run_81` or None if not set
        """
        return self._data["Value for Run 81"]

    @value_for_run_81.setter
    def value_for_run_81(self, value=None):
        """  Corresponds to IDD Field `Value for Run 81`

        Args:
            value (str): value for IDD Field `Value for Run 81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_81`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_81`')
        self._data["Value for Run 81"] = value

    @property
    def value_for_run_82(self):
        """Get value_for_run_82

        Returns:
            str: the value of `value_for_run_82` or None if not set
        """
        return self._data["Value for Run 82"]

    @value_for_run_82.setter
    def value_for_run_82(self, value=None):
        """  Corresponds to IDD Field `Value for Run 82`

        Args:
            value (str): value for IDD Field `Value for Run 82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_82`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_82`')
        self._data["Value for Run 82"] = value

    @property
    def value_for_run_83(self):
        """Get value_for_run_83

        Returns:
            str: the value of `value_for_run_83` or None if not set
        """
        return self._data["Value for Run 83"]

    @value_for_run_83.setter
    def value_for_run_83(self, value=None):
        """  Corresponds to IDD Field `Value for Run 83`

        Args:
            value (str): value for IDD Field `Value for Run 83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_83`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_83`')
        self._data["Value for Run 83"] = value

    @property
    def value_for_run_84(self):
        """Get value_for_run_84

        Returns:
            str: the value of `value_for_run_84` or None if not set
        """
        return self._data["Value for Run 84"]

    @value_for_run_84.setter
    def value_for_run_84(self, value=None):
        """  Corresponds to IDD Field `Value for Run 84`

        Args:
            value (str): value for IDD Field `Value for Run 84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_84`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_84`')
        self._data["Value for Run 84"] = value

    @property
    def value_for_run_85(self):
        """Get value_for_run_85

        Returns:
            str: the value of `value_for_run_85` or None if not set
        """
        return self._data["Value for Run 85"]

    @value_for_run_85.setter
    def value_for_run_85(self, value=None):
        """  Corresponds to IDD Field `Value for Run 85`

        Args:
            value (str): value for IDD Field `Value for Run 85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_85`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_85`')
        self._data["Value for Run 85"] = value

    @property
    def value_for_run_86(self):
        """Get value_for_run_86

        Returns:
            str: the value of `value_for_run_86` or None if not set
        """
        return self._data["Value for Run 86"]

    @value_for_run_86.setter
    def value_for_run_86(self, value=None):
        """  Corresponds to IDD Field `Value for Run 86`

        Args:
            value (str): value for IDD Field `Value for Run 86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_86`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_86`')
        self._data["Value for Run 86"] = value

    @property
    def value_for_run_87(self):
        """Get value_for_run_87

        Returns:
            str: the value of `value_for_run_87` or None if not set
        """
        return self._data["Value for Run 87"]

    @value_for_run_87.setter
    def value_for_run_87(self, value=None):
        """  Corresponds to IDD Field `Value for Run 87`

        Args:
            value (str): value for IDD Field `Value for Run 87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_87`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_87`')
        self._data["Value for Run 87"] = value

    @property
    def value_for_run_88(self):
        """Get value_for_run_88

        Returns:
            str: the value of `value_for_run_88` or None if not set
        """
        return self._data["Value for Run 88"]

    @value_for_run_88.setter
    def value_for_run_88(self, value=None):
        """  Corresponds to IDD Field `Value for Run 88`

        Args:
            value (str): value for IDD Field `Value for Run 88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_88`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_88`')
        self._data["Value for Run 88"] = value

    @property
    def value_for_run_89(self):
        """Get value_for_run_89

        Returns:
            str: the value of `value_for_run_89` or None if not set
        """
        return self._data["Value for Run 89"]

    @value_for_run_89.setter
    def value_for_run_89(self, value=None):
        """  Corresponds to IDD Field `Value for Run 89`

        Args:
            value (str): value for IDD Field `Value for Run 89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_89`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_89`')
        self._data["Value for Run 89"] = value

    @property
    def value_for_run_90(self):
        """Get value_for_run_90

        Returns:
            str: the value of `value_for_run_90` or None if not set
        """
        return self._data["Value for Run 90"]

    @value_for_run_90.setter
    def value_for_run_90(self, value=None):
        """  Corresponds to IDD Field `Value for Run 90`

        Args:
            value (str): value for IDD Field `Value for Run 90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_90`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_90`')
        self._data["Value for Run 90"] = value

    @property
    def value_for_run_91(self):
        """Get value_for_run_91

        Returns:
            str: the value of `value_for_run_91` or None if not set
        """
        return self._data["Value for Run 91"]

    @value_for_run_91.setter
    def value_for_run_91(self, value=None):
        """  Corresponds to IDD Field `Value for Run 91`

        Args:
            value (str): value for IDD Field `Value for Run 91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_91`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_91`')
        self._data["Value for Run 91"] = value

    @property
    def value_for_run_92(self):
        """Get value_for_run_92

        Returns:
            str: the value of `value_for_run_92` or None if not set
        """
        return self._data["Value for Run 92"]

    @value_for_run_92.setter
    def value_for_run_92(self, value=None):
        """  Corresponds to IDD Field `Value for Run 92`

        Args:
            value (str): value for IDD Field `Value for Run 92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_92`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_92`')
        self._data["Value for Run 92"] = value

    @property
    def value_for_run_93(self):
        """Get value_for_run_93

        Returns:
            str: the value of `value_for_run_93` or None if not set
        """
        return self._data["Value for Run 93"]

    @value_for_run_93.setter
    def value_for_run_93(self, value=None):
        """  Corresponds to IDD Field `Value for Run 93`

        Args:
            value (str): value for IDD Field `Value for Run 93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_93`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_93`')
        self._data["Value for Run 93"] = value

    @property
    def value_for_run_94(self):
        """Get value_for_run_94

        Returns:
            str: the value of `value_for_run_94` or None if not set
        """
        return self._data["Value for Run 94"]

    @value_for_run_94.setter
    def value_for_run_94(self, value=None):
        """  Corresponds to IDD Field `Value for Run 94`

        Args:
            value (str): value for IDD Field `Value for Run 94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_94`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_94`')
        self._data["Value for Run 94"] = value

    @property
    def value_for_run_95(self):
        """Get value_for_run_95

        Returns:
            str: the value of `value_for_run_95` or None if not set
        """
        return self._data["Value for Run 95"]

    @value_for_run_95.setter
    def value_for_run_95(self, value=None):
        """  Corresponds to IDD Field `Value for Run 95`

        Args:
            value (str): value for IDD Field `Value for Run 95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_95`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_95`')
        self._data["Value for Run 95"] = value

    @property
    def value_for_run_96(self):
        """Get value_for_run_96

        Returns:
            str: the value of `value_for_run_96` or None if not set
        """
        return self._data["Value for Run 96"]

    @value_for_run_96.setter
    def value_for_run_96(self, value=None):
        """  Corresponds to IDD Field `Value for Run 96`

        Args:
            value (str): value for IDD Field `Value for Run 96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_96`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_96`')
        self._data["Value for Run 96"] = value

    @property
    def value_for_run_97(self):
        """Get value_for_run_97

        Returns:
            str: the value of `value_for_run_97` or None if not set
        """
        return self._data["Value for Run 97"]

    @value_for_run_97.setter
    def value_for_run_97(self, value=None):
        """  Corresponds to IDD Field `Value for Run 97`

        Args:
            value (str): value for IDD Field `Value for Run 97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_97`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_97`')
        self._data["Value for Run 97"] = value

    @property
    def value_for_run_98(self):
        """Get value_for_run_98

        Returns:
            str: the value of `value_for_run_98` or None if not set
        """
        return self._data["Value for Run 98"]

    @value_for_run_98.setter
    def value_for_run_98(self, value=None):
        """  Corresponds to IDD Field `Value for Run 98`

        Args:
            value (str): value for IDD Field `Value for Run 98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_98`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_98`')
        self._data["Value for Run 98"] = value

    @property
    def value_for_run_99(self):
        """Get value_for_run_99

        Returns:
            str: the value of `value_for_run_99` or None if not set
        """
        return self._data["Value for Run 99"]

    @value_for_run_99.setter
    def value_for_run_99(self, value=None):
        """  Corresponds to IDD Field `Value for Run 99`

        Args:
            value (str): value for IDD Field `Value for Run 99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_99`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_99`')
        self._data["Value for Run 99"] = value

    @property
    def value_for_run_100(self):
        """Get value_for_run_100

        Returns:
            str: the value of `value_for_run_100` or None if not set
        """
        return self._data["Value for Run 100"]

    @value_for_run_100.setter
    def value_for_run_100(self, value=None):
        """  Corresponds to IDD Field `Value for Run 100`

        Args:
            value (str): value for IDD Field `Value for Run 100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `value_for_run_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `value_for_run_100`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `value_for_run_100`')
        self._data["Value for Run 100"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ParametricLogic(object):
    """ Corresponds to IDD object `Parametric:Logic`
        This object allows some types of objects to be included for some parametric cases and
        not for others. For example, you might want an overhang on a window in some
        parametric runs and not others. A single Parametric:Logic object is allowed per file.
        Consult the Input Output Reference for available commands and syntax.
    
    """
    internal_name = "Parametric:Logic"
    field_count = 101
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:Logic`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Parametric Logic Line 1"] = None
        self._data["Parametric Logic Line 2"] = None
        self._data["Parametric Logic Line 3"] = None
        self._data["Parametric Logic Line 4"] = None
        self._data["Parametric Logic Line 5"] = None
        self._data["Parametric Logic Line 6"] = None
        self._data["Parametric Logic Line 7"] = None
        self._data["Parametric Logic Line 8"] = None
        self._data["Parametric Logic Line 9"] = None
        self._data["Parametric Logic Line 10"] = None
        self._data["Parametric Logic Line 11"] = None
        self._data["Parametric Logic Line 12"] = None
        self._data["Parametric Logic Line 13"] = None
        self._data["Parametric Logic Line 14"] = None
        self._data["Parametric Logic Line 15"] = None
        self._data["Parametric Logic Line 16"] = None
        self._data["Parametric Logic Line 17"] = None
        self._data["Parametric Logic Line 18"] = None
        self._data["Parametric Logic Line 19"] = None
        self._data["Parametric Logic Line 20"] = None
        self._data["Parametric Logic Line 21"] = None
        self._data["Parametric Logic Line 22"] = None
        self._data["Parametric Logic Line 23"] = None
        self._data["Parametric Logic Line 24"] = None
        self._data["Parametric Logic Line 25"] = None
        self._data["Parametric Logic Line 26"] = None
        self._data["Parametric Logic Line 27"] = None
        self._data["Parametric Logic Line 28"] = None
        self._data["Parametric Logic Line 29"] = None
        self._data["Parametric Logic Line 30"] = None
        self._data["Parametric Logic Line 31"] = None
        self._data["Parametric Logic Line 32"] = None
        self._data["Parametric Logic Line 33"] = None
        self._data["Parametric Logic Line 34"] = None
        self._data["Parametric Logic Line 35"] = None
        self._data["Parametric Logic Line 36"] = None
        self._data["Parametric Logic Line 37"] = None
        self._data["Parametric Logic Line 38"] = None
        self._data["Parametric Logic Line 39"] = None
        self._data["Parametric Logic Line 40"] = None
        self._data["Parametric Logic Line 41"] = None
        self._data["Parametric Logic Line 42"] = None
        self._data["Parametric Logic Line 43"] = None
        self._data["Parametric Logic Line 44"] = None
        self._data["Parametric Logic Line 45"] = None
        self._data["Parametric Logic Line 46"] = None
        self._data["Parametric Logic Line 47"] = None
        self._data["Parametric Logic Line 48"] = None
        self._data["Parametric Logic Line 49"] = None
        self._data["Parametric Logic Line 50"] = None
        self._data["Parametric Logic Line 51"] = None
        self._data["Parametric Logic Line 52"] = None
        self._data["Parametric Logic Line 53"] = None
        self._data["Parametric Logic Line 54"] = None
        self._data["Parametric Logic Line 55"] = None
        self._data["Parametric Logic Line 56"] = None
        self._data["Parametric Logic Line 57"] = None
        self._data["Parametric Logic Line 58"] = None
        self._data["Parametric Logic Line 59"] = None
        self._data["Parametric Logic Line 60"] = None
        self._data["Parametric Logic Line 61"] = None
        self._data["Parametric Logic Line 62"] = None
        self._data["Parametric Logic Line 63"] = None
        self._data["Parametric Logic Line 64"] = None
        self._data["Parametric Logic Line 65"] = None
        self._data["Parametric Logic Line 66"] = None
        self._data["Parametric Logic Line 67"] = None
        self._data["Parametric Logic Line 68"] = None
        self._data["Parametric Logic Line 69"] = None
        self._data["Parametric Logic Line 70"] = None
        self._data["Parametric Logic Line 71"] = None
        self._data["Parametric Logic Line 72"] = None
        self._data["Parametric Logic Line 73"] = None
        self._data["Parametric Logic Line 74"] = None
        self._data["Parametric Logic Line 75"] = None
        self._data["Parametric Logic Line 76"] = None
        self._data["Parametric Logic Line 77"] = None
        self._data["Parametric Logic Line 78"] = None
        self._data["Parametric Logic Line 79"] = None
        self._data["Parametric Logic Line 80"] = None
        self._data["Parametric Logic Line 81"] = None
        self._data["Parametric Logic Line 82"] = None
        self._data["Parametric Logic Line 83"] = None
        self._data["Parametric Logic Line 84"] = None
        self._data["Parametric Logic Line 85"] = None
        self._data["Parametric Logic Line 86"] = None
        self._data["Parametric Logic Line 87"] = None
        self._data["Parametric Logic Line 88"] = None
        self._data["Parametric Logic Line 89"] = None
        self._data["Parametric Logic Line 90"] = None
        self._data["Parametric Logic Line 91"] = None
        self._data["Parametric Logic Line 92"] = None
        self._data["Parametric Logic Line 93"] = None
        self._data["Parametric Logic Line 94"] = None
        self._data["Parametric Logic Line 95"] = None
        self._data["Parametric Logic Line 96"] = None
        self._data["Parametric Logic Line 97"] = None
        self._data["Parametric Logic Line 98"] = None
        self._data["Parametric Logic Line 99"] = None
        self._data["Parametric Logic Line 100"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_1 = None
        else:
            self.parametric_logic_line_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_2 = None
        else:
            self.parametric_logic_line_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_3 = None
        else:
            self.parametric_logic_line_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_4 = None
        else:
            self.parametric_logic_line_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_5 = None
        else:
            self.parametric_logic_line_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_6 = None
        else:
            self.parametric_logic_line_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_7 = None
        else:
            self.parametric_logic_line_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_8 = None
        else:
            self.parametric_logic_line_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_9 = None
        else:
            self.parametric_logic_line_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_10 = None
        else:
            self.parametric_logic_line_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_11 = None
        else:
            self.parametric_logic_line_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_12 = None
        else:
            self.parametric_logic_line_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_13 = None
        else:
            self.parametric_logic_line_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_14 = None
        else:
            self.parametric_logic_line_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_15 = None
        else:
            self.parametric_logic_line_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_16 = None
        else:
            self.parametric_logic_line_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_17 = None
        else:
            self.parametric_logic_line_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_18 = None
        else:
            self.parametric_logic_line_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_19 = None
        else:
            self.parametric_logic_line_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_20 = None
        else:
            self.parametric_logic_line_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_21 = None
        else:
            self.parametric_logic_line_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_22 = None
        else:
            self.parametric_logic_line_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_23 = None
        else:
            self.parametric_logic_line_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_24 = None
        else:
            self.parametric_logic_line_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_25 = None
        else:
            self.parametric_logic_line_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_26 = None
        else:
            self.parametric_logic_line_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_27 = None
        else:
            self.parametric_logic_line_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_28 = None
        else:
            self.parametric_logic_line_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_29 = None
        else:
            self.parametric_logic_line_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_30 = None
        else:
            self.parametric_logic_line_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_31 = None
        else:
            self.parametric_logic_line_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_32 = None
        else:
            self.parametric_logic_line_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_33 = None
        else:
            self.parametric_logic_line_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_34 = None
        else:
            self.parametric_logic_line_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_35 = None
        else:
            self.parametric_logic_line_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_36 = None
        else:
            self.parametric_logic_line_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_37 = None
        else:
            self.parametric_logic_line_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_38 = None
        else:
            self.parametric_logic_line_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_39 = None
        else:
            self.parametric_logic_line_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_40 = None
        else:
            self.parametric_logic_line_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_41 = None
        else:
            self.parametric_logic_line_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_42 = None
        else:
            self.parametric_logic_line_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_43 = None
        else:
            self.parametric_logic_line_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_44 = None
        else:
            self.parametric_logic_line_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_45 = None
        else:
            self.parametric_logic_line_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_46 = None
        else:
            self.parametric_logic_line_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_47 = None
        else:
            self.parametric_logic_line_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_48 = None
        else:
            self.parametric_logic_line_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_49 = None
        else:
            self.parametric_logic_line_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_50 = None
        else:
            self.parametric_logic_line_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_51 = None
        else:
            self.parametric_logic_line_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_52 = None
        else:
            self.parametric_logic_line_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_53 = None
        else:
            self.parametric_logic_line_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_54 = None
        else:
            self.parametric_logic_line_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_55 = None
        else:
            self.parametric_logic_line_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_56 = None
        else:
            self.parametric_logic_line_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_57 = None
        else:
            self.parametric_logic_line_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_58 = None
        else:
            self.parametric_logic_line_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_59 = None
        else:
            self.parametric_logic_line_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_60 = None
        else:
            self.parametric_logic_line_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_61 = None
        else:
            self.parametric_logic_line_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_62 = None
        else:
            self.parametric_logic_line_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_63 = None
        else:
            self.parametric_logic_line_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_64 = None
        else:
            self.parametric_logic_line_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_65 = None
        else:
            self.parametric_logic_line_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_66 = None
        else:
            self.parametric_logic_line_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_67 = None
        else:
            self.parametric_logic_line_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_68 = None
        else:
            self.parametric_logic_line_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_69 = None
        else:
            self.parametric_logic_line_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_70 = None
        else:
            self.parametric_logic_line_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_71 = None
        else:
            self.parametric_logic_line_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_72 = None
        else:
            self.parametric_logic_line_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_73 = None
        else:
            self.parametric_logic_line_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_74 = None
        else:
            self.parametric_logic_line_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_75 = None
        else:
            self.parametric_logic_line_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_76 = None
        else:
            self.parametric_logic_line_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_77 = None
        else:
            self.parametric_logic_line_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_78 = None
        else:
            self.parametric_logic_line_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_79 = None
        else:
            self.parametric_logic_line_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_80 = None
        else:
            self.parametric_logic_line_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_81 = None
        else:
            self.parametric_logic_line_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_82 = None
        else:
            self.parametric_logic_line_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_83 = None
        else:
            self.parametric_logic_line_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_84 = None
        else:
            self.parametric_logic_line_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_85 = None
        else:
            self.parametric_logic_line_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_86 = None
        else:
            self.parametric_logic_line_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_87 = None
        else:
            self.parametric_logic_line_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_88 = None
        else:
            self.parametric_logic_line_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_89 = None
        else:
            self.parametric_logic_line_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_90 = None
        else:
            self.parametric_logic_line_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_91 = None
        else:
            self.parametric_logic_line_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_92 = None
        else:
            self.parametric_logic_line_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_93 = None
        else:
            self.parametric_logic_line_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_94 = None
        else:
            self.parametric_logic_line_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_95 = None
        else:
            self.parametric_logic_line_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_96 = None
        else:
            self.parametric_logic_line_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_97 = None
        else:
            self.parametric_logic_line_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_98 = None
        else:
            self.parametric_logic_line_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_99 = None
        else:
            self.parametric_logic_line_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.parametric_logic_line_100 = None
        else:
            self.parametric_logic_line_100 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def parametric_logic_line_1(self):
        """Get parametric_logic_line_1

        Returns:
            str: the value of `parametric_logic_line_1` or None if not set
        """
        return self._data["Parametric Logic Line 1"]

    @parametric_logic_line_1.setter
    def parametric_logic_line_1(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 1`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_1`')
        self._data["Parametric Logic Line 1"] = value

    @property
    def parametric_logic_line_2(self):
        """Get parametric_logic_line_2

        Returns:
            str: the value of `parametric_logic_line_2` or None if not set
        """
        return self._data["Parametric Logic Line 2"]

    @parametric_logic_line_2.setter
    def parametric_logic_line_2(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 2`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_2`')
        self._data["Parametric Logic Line 2"] = value

    @property
    def parametric_logic_line_3(self):
        """Get parametric_logic_line_3

        Returns:
            str: the value of `parametric_logic_line_3` or None if not set
        """
        return self._data["Parametric Logic Line 3"]

    @parametric_logic_line_3.setter
    def parametric_logic_line_3(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 3`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_3`')
        self._data["Parametric Logic Line 3"] = value

    @property
    def parametric_logic_line_4(self):
        """Get parametric_logic_line_4

        Returns:
            str: the value of `parametric_logic_line_4` or None if not set
        """
        return self._data["Parametric Logic Line 4"]

    @parametric_logic_line_4.setter
    def parametric_logic_line_4(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 4`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_4`')
        self._data["Parametric Logic Line 4"] = value

    @property
    def parametric_logic_line_5(self):
        """Get parametric_logic_line_5

        Returns:
            str: the value of `parametric_logic_line_5` or None if not set
        """
        return self._data["Parametric Logic Line 5"]

    @parametric_logic_line_5.setter
    def parametric_logic_line_5(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 5`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_5`')
        self._data["Parametric Logic Line 5"] = value

    @property
    def parametric_logic_line_6(self):
        """Get parametric_logic_line_6

        Returns:
            str: the value of `parametric_logic_line_6` or None if not set
        """
        return self._data["Parametric Logic Line 6"]

    @parametric_logic_line_6.setter
    def parametric_logic_line_6(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 6`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_6`')
        self._data["Parametric Logic Line 6"] = value

    @property
    def parametric_logic_line_7(self):
        """Get parametric_logic_line_7

        Returns:
            str: the value of `parametric_logic_line_7` or None if not set
        """
        return self._data["Parametric Logic Line 7"]

    @parametric_logic_line_7.setter
    def parametric_logic_line_7(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 7`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_7`')
        self._data["Parametric Logic Line 7"] = value

    @property
    def parametric_logic_line_8(self):
        """Get parametric_logic_line_8

        Returns:
            str: the value of `parametric_logic_line_8` or None if not set
        """
        return self._data["Parametric Logic Line 8"]

    @parametric_logic_line_8.setter
    def parametric_logic_line_8(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 8`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_8`')
        self._data["Parametric Logic Line 8"] = value

    @property
    def parametric_logic_line_9(self):
        """Get parametric_logic_line_9

        Returns:
            str: the value of `parametric_logic_line_9` or None if not set
        """
        return self._data["Parametric Logic Line 9"]

    @parametric_logic_line_9.setter
    def parametric_logic_line_9(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 9`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_9`')
        self._data["Parametric Logic Line 9"] = value

    @property
    def parametric_logic_line_10(self):
        """Get parametric_logic_line_10

        Returns:
            str: the value of `parametric_logic_line_10` or None if not set
        """
        return self._data["Parametric Logic Line 10"]

    @parametric_logic_line_10.setter
    def parametric_logic_line_10(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 10`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_10`')
        self._data["Parametric Logic Line 10"] = value

    @property
    def parametric_logic_line_11(self):
        """Get parametric_logic_line_11

        Returns:
            str: the value of `parametric_logic_line_11` or None if not set
        """
        return self._data["Parametric Logic Line 11"]

    @parametric_logic_line_11.setter
    def parametric_logic_line_11(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 11`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_11`')
        self._data["Parametric Logic Line 11"] = value

    @property
    def parametric_logic_line_12(self):
        """Get parametric_logic_line_12

        Returns:
            str: the value of `parametric_logic_line_12` or None if not set
        """
        return self._data["Parametric Logic Line 12"]

    @parametric_logic_line_12.setter
    def parametric_logic_line_12(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 12`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_12`')
        self._data["Parametric Logic Line 12"] = value

    @property
    def parametric_logic_line_13(self):
        """Get parametric_logic_line_13

        Returns:
            str: the value of `parametric_logic_line_13` or None if not set
        """
        return self._data["Parametric Logic Line 13"]

    @parametric_logic_line_13.setter
    def parametric_logic_line_13(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 13`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_13`')
        self._data["Parametric Logic Line 13"] = value

    @property
    def parametric_logic_line_14(self):
        """Get parametric_logic_line_14

        Returns:
            str: the value of `parametric_logic_line_14` or None if not set
        """
        return self._data["Parametric Logic Line 14"]

    @parametric_logic_line_14.setter
    def parametric_logic_line_14(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 14`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_14`')
        self._data["Parametric Logic Line 14"] = value

    @property
    def parametric_logic_line_15(self):
        """Get parametric_logic_line_15

        Returns:
            str: the value of `parametric_logic_line_15` or None if not set
        """
        return self._data["Parametric Logic Line 15"]

    @parametric_logic_line_15.setter
    def parametric_logic_line_15(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 15`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_15`')
        self._data["Parametric Logic Line 15"] = value

    @property
    def parametric_logic_line_16(self):
        """Get parametric_logic_line_16

        Returns:
            str: the value of `parametric_logic_line_16` or None if not set
        """
        return self._data["Parametric Logic Line 16"]

    @parametric_logic_line_16.setter
    def parametric_logic_line_16(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 16`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_16`')
        self._data["Parametric Logic Line 16"] = value

    @property
    def parametric_logic_line_17(self):
        """Get parametric_logic_line_17

        Returns:
            str: the value of `parametric_logic_line_17` or None if not set
        """
        return self._data["Parametric Logic Line 17"]

    @parametric_logic_line_17.setter
    def parametric_logic_line_17(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 17`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_17`')
        self._data["Parametric Logic Line 17"] = value

    @property
    def parametric_logic_line_18(self):
        """Get parametric_logic_line_18

        Returns:
            str: the value of `parametric_logic_line_18` or None if not set
        """
        return self._data["Parametric Logic Line 18"]

    @parametric_logic_line_18.setter
    def parametric_logic_line_18(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 18`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_18`')
        self._data["Parametric Logic Line 18"] = value

    @property
    def parametric_logic_line_19(self):
        """Get parametric_logic_line_19

        Returns:
            str: the value of `parametric_logic_line_19` or None if not set
        """
        return self._data["Parametric Logic Line 19"]

    @parametric_logic_line_19.setter
    def parametric_logic_line_19(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 19`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_19`')
        self._data["Parametric Logic Line 19"] = value

    @property
    def parametric_logic_line_20(self):
        """Get parametric_logic_line_20

        Returns:
            str: the value of `parametric_logic_line_20` or None if not set
        """
        return self._data["Parametric Logic Line 20"]

    @parametric_logic_line_20.setter
    def parametric_logic_line_20(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 20`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_20`')
        self._data["Parametric Logic Line 20"] = value

    @property
    def parametric_logic_line_21(self):
        """Get parametric_logic_line_21

        Returns:
            str: the value of `parametric_logic_line_21` or None if not set
        """
        return self._data["Parametric Logic Line 21"]

    @parametric_logic_line_21.setter
    def parametric_logic_line_21(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 21`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_21`')
        self._data["Parametric Logic Line 21"] = value

    @property
    def parametric_logic_line_22(self):
        """Get parametric_logic_line_22

        Returns:
            str: the value of `parametric_logic_line_22` or None if not set
        """
        return self._data["Parametric Logic Line 22"]

    @parametric_logic_line_22.setter
    def parametric_logic_line_22(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 22`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_22`')
        self._data["Parametric Logic Line 22"] = value

    @property
    def parametric_logic_line_23(self):
        """Get parametric_logic_line_23

        Returns:
            str: the value of `parametric_logic_line_23` or None if not set
        """
        return self._data["Parametric Logic Line 23"]

    @parametric_logic_line_23.setter
    def parametric_logic_line_23(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 23`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_23`')
        self._data["Parametric Logic Line 23"] = value

    @property
    def parametric_logic_line_24(self):
        """Get parametric_logic_line_24

        Returns:
            str: the value of `parametric_logic_line_24` or None if not set
        """
        return self._data["Parametric Logic Line 24"]

    @parametric_logic_line_24.setter
    def parametric_logic_line_24(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 24`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_24`')
        self._data["Parametric Logic Line 24"] = value

    @property
    def parametric_logic_line_25(self):
        """Get parametric_logic_line_25

        Returns:
            str: the value of `parametric_logic_line_25` or None if not set
        """
        return self._data["Parametric Logic Line 25"]

    @parametric_logic_line_25.setter
    def parametric_logic_line_25(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 25`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_25`')
        self._data["Parametric Logic Line 25"] = value

    @property
    def parametric_logic_line_26(self):
        """Get parametric_logic_line_26

        Returns:
            str: the value of `parametric_logic_line_26` or None if not set
        """
        return self._data["Parametric Logic Line 26"]

    @parametric_logic_line_26.setter
    def parametric_logic_line_26(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 26`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_26`')
        self._data["Parametric Logic Line 26"] = value

    @property
    def parametric_logic_line_27(self):
        """Get parametric_logic_line_27

        Returns:
            str: the value of `parametric_logic_line_27` or None if not set
        """
        return self._data["Parametric Logic Line 27"]

    @parametric_logic_line_27.setter
    def parametric_logic_line_27(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 27`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_27`')
        self._data["Parametric Logic Line 27"] = value

    @property
    def parametric_logic_line_28(self):
        """Get parametric_logic_line_28

        Returns:
            str: the value of `parametric_logic_line_28` or None if not set
        """
        return self._data["Parametric Logic Line 28"]

    @parametric_logic_line_28.setter
    def parametric_logic_line_28(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 28`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_28`')
        self._data["Parametric Logic Line 28"] = value

    @property
    def parametric_logic_line_29(self):
        """Get parametric_logic_line_29

        Returns:
            str: the value of `parametric_logic_line_29` or None if not set
        """
        return self._data["Parametric Logic Line 29"]

    @parametric_logic_line_29.setter
    def parametric_logic_line_29(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 29`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_29`')
        self._data["Parametric Logic Line 29"] = value

    @property
    def parametric_logic_line_30(self):
        """Get parametric_logic_line_30

        Returns:
            str: the value of `parametric_logic_line_30` or None if not set
        """
        return self._data["Parametric Logic Line 30"]

    @parametric_logic_line_30.setter
    def parametric_logic_line_30(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 30`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_30`')
        self._data["Parametric Logic Line 30"] = value

    @property
    def parametric_logic_line_31(self):
        """Get parametric_logic_line_31

        Returns:
            str: the value of `parametric_logic_line_31` or None if not set
        """
        return self._data["Parametric Logic Line 31"]

    @parametric_logic_line_31.setter
    def parametric_logic_line_31(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 31`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_31`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_31`')
        self._data["Parametric Logic Line 31"] = value

    @property
    def parametric_logic_line_32(self):
        """Get parametric_logic_line_32

        Returns:
            str: the value of `parametric_logic_line_32` or None if not set
        """
        return self._data["Parametric Logic Line 32"]

    @parametric_logic_line_32.setter
    def parametric_logic_line_32(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 32`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_32`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_32`')
        self._data["Parametric Logic Line 32"] = value

    @property
    def parametric_logic_line_33(self):
        """Get parametric_logic_line_33

        Returns:
            str: the value of `parametric_logic_line_33` or None if not set
        """
        return self._data["Parametric Logic Line 33"]

    @parametric_logic_line_33.setter
    def parametric_logic_line_33(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 33`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_33`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_33`')
        self._data["Parametric Logic Line 33"] = value

    @property
    def parametric_logic_line_34(self):
        """Get parametric_logic_line_34

        Returns:
            str: the value of `parametric_logic_line_34` or None if not set
        """
        return self._data["Parametric Logic Line 34"]

    @parametric_logic_line_34.setter
    def parametric_logic_line_34(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 34`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_34`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_34`')
        self._data["Parametric Logic Line 34"] = value

    @property
    def parametric_logic_line_35(self):
        """Get parametric_logic_line_35

        Returns:
            str: the value of `parametric_logic_line_35` or None if not set
        """
        return self._data["Parametric Logic Line 35"]

    @parametric_logic_line_35.setter
    def parametric_logic_line_35(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 35`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_35`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_35`')
        self._data["Parametric Logic Line 35"] = value

    @property
    def parametric_logic_line_36(self):
        """Get parametric_logic_line_36

        Returns:
            str: the value of `parametric_logic_line_36` or None if not set
        """
        return self._data["Parametric Logic Line 36"]

    @parametric_logic_line_36.setter
    def parametric_logic_line_36(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 36`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_36`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_36`')
        self._data["Parametric Logic Line 36"] = value

    @property
    def parametric_logic_line_37(self):
        """Get parametric_logic_line_37

        Returns:
            str: the value of `parametric_logic_line_37` or None if not set
        """
        return self._data["Parametric Logic Line 37"]

    @parametric_logic_line_37.setter
    def parametric_logic_line_37(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 37`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_37`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_37`')
        self._data["Parametric Logic Line 37"] = value

    @property
    def parametric_logic_line_38(self):
        """Get parametric_logic_line_38

        Returns:
            str: the value of `parametric_logic_line_38` or None if not set
        """
        return self._data["Parametric Logic Line 38"]

    @parametric_logic_line_38.setter
    def parametric_logic_line_38(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 38`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_38`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_38`')
        self._data["Parametric Logic Line 38"] = value

    @property
    def parametric_logic_line_39(self):
        """Get parametric_logic_line_39

        Returns:
            str: the value of `parametric_logic_line_39` or None if not set
        """
        return self._data["Parametric Logic Line 39"]

    @parametric_logic_line_39.setter
    def parametric_logic_line_39(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 39`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_39`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_39`')
        self._data["Parametric Logic Line 39"] = value

    @property
    def parametric_logic_line_40(self):
        """Get parametric_logic_line_40

        Returns:
            str: the value of `parametric_logic_line_40` or None if not set
        """
        return self._data["Parametric Logic Line 40"]

    @parametric_logic_line_40.setter
    def parametric_logic_line_40(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 40`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_40`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_40`')
        self._data["Parametric Logic Line 40"] = value

    @property
    def parametric_logic_line_41(self):
        """Get parametric_logic_line_41

        Returns:
            str: the value of `parametric_logic_line_41` or None if not set
        """
        return self._data["Parametric Logic Line 41"]

    @parametric_logic_line_41.setter
    def parametric_logic_line_41(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 41`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_41`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_41`')
        self._data["Parametric Logic Line 41"] = value

    @property
    def parametric_logic_line_42(self):
        """Get parametric_logic_line_42

        Returns:
            str: the value of `parametric_logic_line_42` or None if not set
        """
        return self._data["Parametric Logic Line 42"]

    @parametric_logic_line_42.setter
    def parametric_logic_line_42(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 42`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_42`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_42`')
        self._data["Parametric Logic Line 42"] = value

    @property
    def parametric_logic_line_43(self):
        """Get parametric_logic_line_43

        Returns:
            str: the value of `parametric_logic_line_43` or None if not set
        """
        return self._data["Parametric Logic Line 43"]

    @parametric_logic_line_43.setter
    def parametric_logic_line_43(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 43`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_43`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_43`')
        self._data["Parametric Logic Line 43"] = value

    @property
    def parametric_logic_line_44(self):
        """Get parametric_logic_line_44

        Returns:
            str: the value of `parametric_logic_line_44` or None if not set
        """
        return self._data["Parametric Logic Line 44"]

    @parametric_logic_line_44.setter
    def parametric_logic_line_44(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 44`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_44`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_44`')
        self._data["Parametric Logic Line 44"] = value

    @property
    def parametric_logic_line_45(self):
        """Get parametric_logic_line_45

        Returns:
            str: the value of `parametric_logic_line_45` or None if not set
        """
        return self._data["Parametric Logic Line 45"]

    @parametric_logic_line_45.setter
    def parametric_logic_line_45(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 45`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_45`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_45`')
        self._data["Parametric Logic Line 45"] = value

    @property
    def parametric_logic_line_46(self):
        """Get parametric_logic_line_46

        Returns:
            str: the value of `parametric_logic_line_46` or None if not set
        """
        return self._data["Parametric Logic Line 46"]

    @parametric_logic_line_46.setter
    def parametric_logic_line_46(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 46`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_46`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_46`')
        self._data["Parametric Logic Line 46"] = value

    @property
    def parametric_logic_line_47(self):
        """Get parametric_logic_line_47

        Returns:
            str: the value of `parametric_logic_line_47` or None if not set
        """
        return self._data["Parametric Logic Line 47"]

    @parametric_logic_line_47.setter
    def parametric_logic_line_47(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 47`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_47`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_47`')
        self._data["Parametric Logic Line 47"] = value

    @property
    def parametric_logic_line_48(self):
        """Get parametric_logic_line_48

        Returns:
            str: the value of `parametric_logic_line_48` or None if not set
        """
        return self._data["Parametric Logic Line 48"]

    @parametric_logic_line_48.setter
    def parametric_logic_line_48(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 48`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_48`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_48`')
        self._data["Parametric Logic Line 48"] = value

    @property
    def parametric_logic_line_49(self):
        """Get parametric_logic_line_49

        Returns:
            str: the value of `parametric_logic_line_49` or None if not set
        """
        return self._data["Parametric Logic Line 49"]

    @parametric_logic_line_49.setter
    def parametric_logic_line_49(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 49`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_49`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_49`')
        self._data["Parametric Logic Line 49"] = value

    @property
    def parametric_logic_line_50(self):
        """Get parametric_logic_line_50

        Returns:
            str: the value of `parametric_logic_line_50` or None if not set
        """
        return self._data["Parametric Logic Line 50"]

    @parametric_logic_line_50.setter
    def parametric_logic_line_50(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 50`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_50`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_50`')
        self._data["Parametric Logic Line 50"] = value

    @property
    def parametric_logic_line_51(self):
        """Get parametric_logic_line_51

        Returns:
            str: the value of `parametric_logic_line_51` or None if not set
        """
        return self._data["Parametric Logic Line 51"]

    @parametric_logic_line_51.setter
    def parametric_logic_line_51(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 51`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_51`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_51`')
        self._data["Parametric Logic Line 51"] = value

    @property
    def parametric_logic_line_52(self):
        """Get parametric_logic_line_52

        Returns:
            str: the value of `parametric_logic_line_52` or None if not set
        """
        return self._data["Parametric Logic Line 52"]

    @parametric_logic_line_52.setter
    def parametric_logic_line_52(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 52`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_52`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_52`')
        self._data["Parametric Logic Line 52"] = value

    @property
    def parametric_logic_line_53(self):
        """Get parametric_logic_line_53

        Returns:
            str: the value of `parametric_logic_line_53` or None if not set
        """
        return self._data["Parametric Logic Line 53"]

    @parametric_logic_line_53.setter
    def parametric_logic_line_53(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 53`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_53`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_53`')
        self._data["Parametric Logic Line 53"] = value

    @property
    def parametric_logic_line_54(self):
        """Get parametric_logic_line_54

        Returns:
            str: the value of `parametric_logic_line_54` or None if not set
        """
        return self._data["Parametric Logic Line 54"]

    @parametric_logic_line_54.setter
    def parametric_logic_line_54(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 54`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_54`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_54`')
        self._data["Parametric Logic Line 54"] = value

    @property
    def parametric_logic_line_55(self):
        """Get parametric_logic_line_55

        Returns:
            str: the value of `parametric_logic_line_55` or None if not set
        """
        return self._data["Parametric Logic Line 55"]

    @parametric_logic_line_55.setter
    def parametric_logic_line_55(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 55`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_55`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_55`')
        self._data["Parametric Logic Line 55"] = value

    @property
    def parametric_logic_line_56(self):
        """Get parametric_logic_line_56

        Returns:
            str: the value of `parametric_logic_line_56` or None if not set
        """
        return self._data["Parametric Logic Line 56"]

    @parametric_logic_line_56.setter
    def parametric_logic_line_56(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 56`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_56`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_56`')
        self._data["Parametric Logic Line 56"] = value

    @property
    def parametric_logic_line_57(self):
        """Get parametric_logic_line_57

        Returns:
            str: the value of `parametric_logic_line_57` or None if not set
        """
        return self._data["Parametric Logic Line 57"]

    @parametric_logic_line_57.setter
    def parametric_logic_line_57(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 57`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_57`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_57`')
        self._data["Parametric Logic Line 57"] = value

    @property
    def parametric_logic_line_58(self):
        """Get parametric_logic_line_58

        Returns:
            str: the value of `parametric_logic_line_58` or None if not set
        """
        return self._data["Parametric Logic Line 58"]

    @parametric_logic_line_58.setter
    def parametric_logic_line_58(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 58`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_58`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_58`')
        self._data["Parametric Logic Line 58"] = value

    @property
    def parametric_logic_line_59(self):
        """Get parametric_logic_line_59

        Returns:
            str: the value of `parametric_logic_line_59` or None if not set
        """
        return self._data["Parametric Logic Line 59"]

    @parametric_logic_line_59.setter
    def parametric_logic_line_59(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 59`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_59`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_59`')
        self._data["Parametric Logic Line 59"] = value

    @property
    def parametric_logic_line_60(self):
        """Get parametric_logic_line_60

        Returns:
            str: the value of `parametric_logic_line_60` or None if not set
        """
        return self._data["Parametric Logic Line 60"]

    @parametric_logic_line_60.setter
    def parametric_logic_line_60(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 60`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_60`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_60`')
        self._data["Parametric Logic Line 60"] = value

    @property
    def parametric_logic_line_61(self):
        """Get parametric_logic_line_61

        Returns:
            str: the value of `parametric_logic_line_61` or None if not set
        """
        return self._data["Parametric Logic Line 61"]

    @parametric_logic_line_61.setter
    def parametric_logic_line_61(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 61`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_61`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_61`')
        self._data["Parametric Logic Line 61"] = value

    @property
    def parametric_logic_line_62(self):
        """Get parametric_logic_line_62

        Returns:
            str: the value of `parametric_logic_line_62` or None if not set
        """
        return self._data["Parametric Logic Line 62"]

    @parametric_logic_line_62.setter
    def parametric_logic_line_62(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 62`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_62`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_62`')
        self._data["Parametric Logic Line 62"] = value

    @property
    def parametric_logic_line_63(self):
        """Get parametric_logic_line_63

        Returns:
            str: the value of `parametric_logic_line_63` or None if not set
        """
        return self._data["Parametric Logic Line 63"]

    @parametric_logic_line_63.setter
    def parametric_logic_line_63(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 63`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_63`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_63`')
        self._data["Parametric Logic Line 63"] = value

    @property
    def parametric_logic_line_64(self):
        """Get parametric_logic_line_64

        Returns:
            str: the value of `parametric_logic_line_64` or None if not set
        """
        return self._data["Parametric Logic Line 64"]

    @parametric_logic_line_64.setter
    def parametric_logic_line_64(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 64`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_64`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_64`')
        self._data["Parametric Logic Line 64"] = value

    @property
    def parametric_logic_line_65(self):
        """Get parametric_logic_line_65

        Returns:
            str: the value of `parametric_logic_line_65` or None if not set
        """
        return self._data["Parametric Logic Line 65"]

    @parametric_logic_line_65.setter
    def parametric_logic_line_65(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 65`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_65`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_65`')
        self._data["Parametric Logic Line 65"] = value

    @property
    def parametric_logic_line_66(self):
        """Get parametric_logic_line_66

        Returns:
            str: the value of `parametric_logic_line_66` or None if not set
        """
        return self._data["Parametric Logic Line 66"]

    @parametric_logic_line_66.setter
    def parametric_logic_line_66(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 66`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_66`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_66`')
        self._data["Parametric Logic Line 66"] = value

    @property
    def parametric_logic_line_67(self):
        """Get parametric_logic_line_67

        Returns:
            str: the value of `parametric_logic_line_67` or None if not set
        """
        return self._data["Parametric Logic Line 67"]

    @parametric_logic_line_67.setter
    def parametric_logic_line_67(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 67`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_67`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_67`')
        self._data["Parametric Logic Line 67"] = value

    @property
    def parametric_logic_line_68(self):
        """Get parametric_logic_line_68

        Returns:
            str: the value of `parametric_logic_line_68` or None if not set
        """
        return self._data["Parametric Logic Line 68"]

    @parametric_logic_line_68.setter
    def parametric_logic_line_68(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 68`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_68`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_68`')
        self._data["Parametric Logic Line 68"] = value

    @property
    def parametric_logic_line_69(self):
        """Get parametric_logic_line_69

        Returns:
            str: the value of `parametric_logic_line_69` or None if not set
        """
        return self._data["Parametric Logic Line 69"]

    @parametric_logic_line_69.setter
    def parametric_logic_line_69(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 69`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_69`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_69`')
        self._data["Parametric Logic Line 69"] = value

    @property
    def parametric_logic_line_70(self):
        """Get parametric_logic_line_70

        Returns:
            str: the value of `parametric_logic_line_70` or None if not set
        """
        return self._data["Parametric Logic Line 70"]

    @parametric_logic_line_70.setter
    def parametric_logic_line_70(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 70`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_70`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_70`')
        self._data["Parametric Logic Line 70"] = value

    @property
    def parametric_logic_line_71(self):
        """Get parametric_logic_line_71

        Returns:
            str: the value of `parametric_logic_line_71` or None if not set
        """
        return self._data["Parametric Logic Line 71"]

    @parametric_logic_line_71.setter
    def parametric_logic_line_71(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 71`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_71`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_71`')
        self._data["Parametric Logic Line 71"] = value

    @property
    def parametric_logic_line_72(self):
        """Get parametric_logic_line_72

        Returns:
            str: the value of `parametric_logic_line_72` or None if not set
        """
        return self._data["Parametric Logic Line 72"]

    @parametric_logic_line_72.setter
    def parametric_logic_line_72(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 72`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_72`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_72`')
        self._data["Parametric Logic Line 72"] = value

    @property
    def parametric_logic_line_73(self):
        """Get parametric_logic_line_73

        Returns:
            str: the value of `parametric_logic_line_73` or None if not set
        """
        return self._data["Parametric Logic Line 73"]

    @parametric_logic_line_73.setter
    def parametric_logic_line_73(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 73`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_73`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_73`')
        self._data["Parametric Logic Line 73"] = value

    @property
    def parametric_logic_line_74(self):
        """Get parametric_logic_line_74

        Returns:
            str: the value of `parametric_logic_line_74` or None if not set
        """
        return self._data["Parametric Logic Line 74"]

    @parametric_logic_line_74.setter
    def parametric_logic_line_74(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 74`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_74`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_74`')
        self._data["Parametric Logic Line 74"] = value

    @property
    def parametric_logic_line_75(self):
        """Get parametric_logic_line_75

        Returns:
            str: the value of `parametric_logic_line_75` or None if not set
        """
        return self._data["Parametric Logic Line 75"]

    @parametric_logic_line_75.setter
    def parametric_logic_line_75(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 75`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_75`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_75`')
        self._data["Parametric Logic Line 75"] = value

    @property
    def parametric_logic_line_76(self):
        """Get parametric_logic_line_76

        Returns:
            str: the value of `parametric_logic_line_76` or None if not set
        """
        return self._data["Parametric Logic Line 76"]

    @parametric_logic_line_76.setter
    def parametric_logic_line_76(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 76`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_76`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_76`')
        self._data["Parametric Logic Line 76"] = value

    @property
    def parametric_logic_line_77(self):
        """Get parametric_logic_line_77

        Returns:
            str: the value of `parametric_logic_line_77` or None if not set
        """
        return self._data["Parametric Logic Line 77"]

    @parametric_logic_line_77.setter
    def parametric_logic_line_77(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 77`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_77`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_77`')
        self._data["Parametric Logic Line 77"] = value

    @property
    def parametric_logic_line_78(self):
        """Get parametric_logic_line_78

        Returns:
            str: the value of `parametric_logic_line_78` or None if not set
        """
        return self._data["Parametric Logic Line 78"]

    @parametric_logic_line_78.setter
    def parametric_logic_line_78(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 78`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_78`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_78`')
        self._data["Parametric Logic Line 78"] = value

    @property
    def parametric_logic_line_79(self):
        """Get parametric_logic_line_79

        Returns:
            str: the value of `parametric_logic_line_79` or None if not set
        """
        return self._data["Parametric Logic Line 79"]

    @parametric_logic_line_79.setter
    def parametric_logic_line_79(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 79`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_79`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_79`')
        self._data["Parametric Logic Line 79"] = value

    @property
    def parametric_logic_line_80(self):
        """Get parametric_logic_line_80

        Returns:
            str: the value of `parametric_logic_line_80` or None if not set
        """
        return self._data["Parametric Logic Line 80"]

    @parametric_logic_line_80.setter
    def parametric_logic_line_80(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 80`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_80`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_80`')
        self._data["Parametric Logic Line 80"] = value

    @property
    def parametric_logic_line_81(self):
        """Get parametric_logic_line_81

        Returns:
            str: the value of `parametric_logic_line_81` or None if not set
        """
        return self._data["Parametric Logic Line 81"]

    @parametric_logic_line_81.setter
    def parametric_logic_line_81(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 81`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_81`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_81`')
        self._data["Parametric Logic Line 81"] = value

    @property
    def parametric_logic_line_82(self):
        """Get parametric_logic_line_82

        Returns:
            str: the value of `parametric_logic_line_82` or None if not set
        """
        return self._data["Parametric Logic Line 82"]

    @parametric_logic_line_82.setter
    def parametric_logic_line_82(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 82`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_82`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_82`')
        self._data["Parametric Logic Line 82"] = value

    @property
    def parametric_logic_line_83(self):
        """Get parametric_logic_line_83

        Returns:
            str: the value of `parametric_logic_line_83` or None if not set
        """
        return self._data["Parametric Logic Line 83"]

    @parametric_logic_line_83.setter
    def parametric_logic_line_83(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 83`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_83`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_83`')
        self._data["Parametric Logic Line 83"] = value

    @property
    def parametric_logic_line_84(self):
        """Get parametric_logic_line_84

        Returns:
            str: the value of `parametric_logic_line_84` or None if not set
        """
        return self._data["Parametric Logic Line 84"]

    @parametric_logic_line_84.setter
    def parametric_logic_line_84(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 84`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_84`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_84`')
        self._data["Parametric Logic Line 84"] = value

    @property
    def parametric_logic_line_85(self):
        """Get parametric_logic_line_85

        Returns:
            str: the value of `parametric_logic_line_85` or None if not set
        """
        return self._data["Parametric Logic Line 85"]

    @parametric_logic_line_85.setter
    def parametric_logic_line_85(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 85`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_85`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_85`')
        self._data["Parametric Logic Line 85"] = value

    @property
    def parametric_logic_line_86(self):
        """Get parametric_logic_line_86

        Returns:
            str: the value of `parametric_logic_line_86` or None if not set
        """
        return self._data["Parametric Logic Line 86"]

    @parametric_logic_line_86.setter
    def parametric_logic_line_86(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 86`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_86`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_86`')
        self._data["Parametric Logic Line 86"] = value

    @property
    def parametric_logic_line_87(self):
        """Get parametric_logic_line_87

        Returns:
            str: the value of `parametric_logic_line_87` or None if not set
        """
        return self._data["Parametric Logic Line 87"]

    @parametric_logic_line_87.setter
    def parametric_logic_line_87(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 87`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_87`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_87`')
        self._data["Parametric Logic Line 87"] = value

    @property
    def parametric_logic_line_88(self):
        """Get parametric_logic_line_88

        Returns:
            str: the value of `parametric_logic_line_88` or None if not set
        """
        return self._data["Parametric Logic Line 88"]

    @parametric_logic_line_88.setter
    def parametric_logic_line_88(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 88`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_88`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_88`')
        self._data["Parametric Logic Line 88"] = value

    @property
    def parametric_logic_line_89(self):
        """Get parametric_logic_line_89

        Returns:
            str: the value of `parametric_logic_line_89` or None if not set
        """
        return self._data["Parametric Logic Line 89"]

    @parametric_logic_line_89.setter
    def parametric_logic_line_89(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 89`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_89`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_89`')
        self._data["Parametric Logic Line 89"] = value

    @property
    def parametric_logic_line_90(self):
        """Get parametric_logic_line_90

        Returns:
            str: the value of `parametric_logic_line_90` or None if not set
        """
        return self._data["Parametric Logic Line 90"]

    @parametric_logic_line_90.setter
    def parametric_logic_line_90(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 90`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_90`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_90`')
        self._data["Parametric Logic Line 90"] = value

    @property
    def parametric_logic_line_91(self):
        """Get parametric_logic_line_91

        Returns:
            str: the value of `parametric_logic_line_91` or None if not set
        """
        return self._data["Parametric Logic Line 91"]

    @parametric_logic_line_91.setter
    def parametric_logic_line_91(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 91`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_91`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_91`')
        self._data["Parametric Logic Line 91"] = value

    @property
    def parametric_logic_line_92(self):
        """Get parametric_logic_line_92

        Returns:
            str: the value of `parametric_logic_line_92` or None if not set
        """
        return self._data["Parametric Logic Line 92"]

    @parametric_logic_line_92.setter
    def parametric_logic_line_92(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 92`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_92`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_92`')
        self._data["Parametric Logic Line 92"] = value

    @property
    def parametric_logic_line_93(self):
        """Get parametric_logic_line_93

        Returns:
            str: the value of `parametric_logic_line_93` or None if not set
        """
        return self._data["Parametric Logic Line 93"]

    @parametric_logic_line_93.setter
    def parametric_logic_line_93(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 93`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_93`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_93`')
        self._data["Parametric Logic Line 93"] = value

    @property
    def parametric_logic_line_94(self):
        """Get parametric_logic_line_94

        Returns:
            str: the value of `parametric_logic_line_94` or None if not set
        """
        return self._data["Parametric Logic Line 94"]

    @parametric_logic_line_94.setter
    def parametric_logic_line_94(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 94`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_94`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_94`')
        self._data["Parametric Logic Line 94"] = value

    @property
    def parametric_logic_line_95(self):
        """Get parametric_logic_line_95

        Returns:
            str: the value of `parametric_logic_line_95` or None if not set
        """
        return self._data["Parametric Logic Line 95"]

    @parametric_logic_line_95.setter
    def parametric_logic_line_95(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 95`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_95`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_95`')
        self._data["Parametric Logic Line 95"] = value

    @property
    def parametric_logic_line_96(self):
        """Get parametric_logic_line_96

        Returns:
            str: the value of `parametric_logic_line_96` or None if not set
        """
        return self._data["Parametric Logic Line 96"]

    @parametric_logic_line_96.setter
    def parametric_logic_line_96(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 96`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_96`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_96`')
        self._data["Parametric Logic Line 96"] = value

    @property
    def parametric_logic_line_97(self):
        """Get parametric_logic_line_97

        Returns:
            str: the value of `parametric_logic_line_97` or None if not set
        """
        return self._data["Parametric Logic Line 97"]

    @parametric_logic_line_97.setter
    def parametric_logic_line_97(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 97`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_97`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_97`')
        self._data["Parametric Logic Line 97"] = value

    @property
    def parametric_logic_line_98(self):
        """Get parametric_logic_line_98

        Returns:
            str: the value of `parametric_logic_line_98` or None if not set
        """
        return self._data["Parametric Logic Line 98"]

    @parametric_logic_line_98.setter
    def parametric_logic_line_98(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 98`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_98`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_98`')
        self._data["Parametric Logic Line 98"] = value

    @property
    def parametric_logic_line_99(self):
        """Get parametric_logic_line_99

        Returns:
            str: the value of `parametric_logic_line_99` or None if not set
        """
        return self._data["Parametric Logic Line 99"]

    @parametric_logic_line_99.setter
    def parametric_logic_line_99(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 99`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_99`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_99`')
        self._data["Parametric Logic Line 99"] = value

    @property
    def parametric_logic_line_100(self):
        """Get parametric_logic_line_100

        Returns:
            str: the value of `parametric_logic_line_100` or None if not set
        """
        return self._data["Parametric Logic Line 100"]

    @parametric_logic_line_100.setter
    def parametric_logic_line_100(self, value=None):
        """  Corresponds to IDD Field `Parametric Logic Line 100`

        Args:
            value (str): value for IDD Field `Parametric Logic Line 100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `parametric_logic_line_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `parametric_logic_line_100`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `parametric_logic_line_100`')
        self._data["Parametric Logic Line 100"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ParametricRunControl(object):
    """ Corresponds to IDD object `Parametric:RunControl`
        Controls which parametric runs are simulated. This object is optional. If it is not
        included, then all parametric runs are performed.
    
    """
    internal_name = "Parametric:RunControl"
    field_count = 101
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:RunControl`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Perform Run 1"] = None
        self._data["Perform Run 2"] = None
        self._data["Perform Run 3"] = None
        self._data["Perform Run 4"] = None
        self._data["Perform Run 5"] = None
        self._data["Perform Run 6"] = None
        self._data["Perform Run 7"] = None
        self._data["Perform Run 8"] = None
        self._data["Perform Run 9"] = None
        self._data["Perform Run 10"] = None
        self._data["Perform Run 11"] = None
        self._data["Perform Run 12"] = None
        self._data["Perform Run 13"] = None
        self._data["Perform Run 14"] = None
        self._data["Perform Run 15"] = None
        self._data["Perform Run 16"] = None
        self._data["Perform Run 17"] = None
        self._data["Perform Run 18"] = None
        self._data["Perform Run 19"] = None
        self._data["Perform Run 20"] = None
        self._data["Perform Run 21"] = None
        self._data["Perform Run 22"] = None
        self._data["Perform Run 23"] = None
        self._data["Perform Run 24"] = None
        self._data["Perform Run 25"] = None
        self._data["Perform Run 26"] = None
        self._data["Perform Run 27"] = None
        self._data["Perform Run 28"] = None
        self._data["Perform Run 29"] = None
        self._data["Perform Run 30"] = None
        self._data["Perform Run 31"] = None
        self._data["Perform Run 32"] = None
        self._data["Perform Run 33"] = None
        self._data["Perform Run 34"] = None
        self._data["Perform Run 35"] = None
        self._data["Perform Run 36"] = None
        self._data["Perform Run 37"] = None
        self._data["Perform Run 38"] = None
        self._data["Perform Run 39"] = None
        self._data["Perform Run 40"] = None
        self._data["Perform Run 41"] = None
        self._data["Perform Run 42"] = None
        self._data["Perform Run 43"] = None
        self._data["Perform Run 44"] = None
        self._data["Perform Run 45"] = None
        self._data["Perform Run 46"] = None
        self._data["Perform Run 47"] = None
        self._data["Perform Run 48"] = None
        self._data["Perform Run 49"] = None
        self._data["Perform Run 50"] = None
        self._data["Perform Run 51"] = None
        self._data["Perform Run 52"] = None
        self._data["Perform Run 53"] = None
        self._data["Perform Run 54"] = None
        self._data["Perform Run 55"] = None
        self._data["Perform Run 56"] = None
        self._data["Perform Run 57"] = None
        self._data["Perform Run 58"] = None
        self._data["Perform Run 59"] = None
        self._data["Perform Run 60"] = None
        self._data["Perform Run 61"] = None
        self._data["Perform Run 62"] = None
        self._data["Perform Run 63"] = None
        self._data["Perform Run 64"] = None
        self._data["Perform Run 65"] = None
        self._data["Perform Run 66"] = None
        self._data["Perform Run 67"] = None
        self._data["Perform Run 68"] = None
        self._data["Perform Run 69"] = None
        self._data["Perform Run 70"] = None
        self._data["Perform Run 71"] = None
        self._data["Perform Run 72"] = None
        self._data["Perform Run 73"] = None
        self._data["Perform Run 74"] = None
        self._data["Perform Run 75"] = None
        self._data["Perform Run 76"] = None
        self._data["Perform Run 77"] = None
        self._data["Perform Run 78"] = None
        self._data["Perform Run 79"] = None
        self._data["Perform Run 80"] = None
        self._data["Perform Run 81"] = None
        self._data["Perform Run 82"] = None
        self._data["Perform Run 83"] = None
        self._data["Perform Run 84"] = None
        self._data["Perform Run 85"] = None
        self._data["Perform Run 86"] = None
        self._data["Perform Run 87"] = None
        self._data["Perform Run 88"] = None
        self._data["Perform Run 89"] = None
        self._data["Perform Run 90"] = None
        self._data["Perform Run 91"] = None
        self._data["Perform Run 92"] = None
        self._data["Perform Run 93"] = None
        self._data["Perform Run 94"] = None
        self._data["Perform Run 95"] = None
        self._data["Perform Run 96"] = None
        self._data["Perform Run 97"] = None
        self._data["Perform Run 98"] = None
        self._data["Perform Run 99"] = None
        self._data["Perform Run 100"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_1 = None
        else:
            self.perform_run_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_2 = None
        else:
            self.perform_run_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_3 = None
        else:
            self.perform_run_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_4 = None
        else:
            self.perform_run_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_5 = None
        else:
            self.perform_run_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_6 = None
        else:
            self.perform_run_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_7 = None
        else:
            self.perform_run_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_8 = None
        else:
            self.perform_run_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_9 = None
        else:
            self.perform_run_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_10 = None
        else:
            self.perform_run_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_11 = None
        else:
            self.perform_run_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_12 = None
        else:
            self.perform_run_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_13 = None
        else:
            self.perform_run_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_14 = None
        else:
            self.perform_run_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_15 = None
        else:
            self.perform_run_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_16 = None
        else:
            self.perform_run_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_17 = None
        else:
            self.perform_run_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_18 = None
        else:
            self.perform_run_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_19 = None
        else:
            self.perform_run_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_20 = None
        else:
            self.perform_run_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_21 = None
        else:
            self.perform_run_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_22 = None
        else:
            self.perform_run_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_23 = None
        else:
            self.perform_run_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_24 = None
        else:
            self.perform_run_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_25 = None
        else:
            self.perform_run_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_26 = None
        else:
            self.perform_run_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_27 = None
        else:
            self.perform_run_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_28 = None
        else:
            self.perform_run_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_29 = None
        else:
            self.perform_run_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_30 = None
        else:
            self.perform_run_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_31 = None
        else:
            self.perform_run_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_32 = None
        else:
            self.perform_run_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_33 = None
        else:
            self.perform_run_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_34 = None
        else:
            self.perform_run_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_35 = None
        else:
            self.perform_run_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_36 = None
        else:
            self.perform_run_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_37 = None
        else:
            self.perform_run_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_38 = None
        else:
            self.perform_run_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_39 = None
        else:
            self.perform_run_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_40 = None
        else:
            self.perform_run_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_41 = None
        else:
            self.perform_run_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_42 = None
        else:
            self.perform_run_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_43 = None
        else:
            self.perform_run_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_44 = None
        else:
            self.perform_run_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_45 = None
        else:
            self.perform_run_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_46 = None
        else:
            self.perform_run_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_47 = None
        else:
            self.perform_run_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_48 = None
        else:
            self.perform_run_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_49 = None
        else:
            self.perform_run_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_50 = None
        else:
            self.perform_run_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_51 = None
        else:
            self.perform_run_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_52 = None
        else:
            self.perform_run_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_53 = None
        else:
            self.perform_run_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_54 = None
        else:
            self.perform_run_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_55 = None
        else:
            self.perform_run_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_56 = None
        else:
            self.perform_run_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_57 = None
        else:
            self.perform_run_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_58 = None
        else:
            self.perform_run_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_59 = None
        else:
            self.perform_run_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_60 = None
        else:
            self.perform_run_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_61 = None
        else:
            self.perform_run_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_62 = None
        else:
            self.perform_run_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_63 = None
        else:
            self.perform_run_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_64 = None
        else:
            self.perform_run_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_65 = None
        else:
            self.perform_run_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_66 = None
        else:
            self.perform_run_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_67 = None
        else:
            self.perform_run_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_68 = None
        else:
            self.perform_run_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_69 = None
        else:
            self.perform_run_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_70 = None
        else:
            self.perform_run_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_71 = None
        else:
            self.perform_run_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_72 = None
        else:
            self.perform_run_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_73 = None
        else:
            self.perform_run_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_74 = None
        else:
            self.perform_run_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_75 = None
        else:
            self.perform_run_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_76 = None
        else:
            self.perform_run_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_77 = None
        else:
            self.perform_run_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_78 = None
        else:
            self.perform_run_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_79 = None
        else:
            self.perform_run_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_80 = None
        else:
            self.perform_run_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_81 = None
        else:
            self.perform_run_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_82 = None
        else:
            self.perform_run_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_83 = None
        else:
            self.perform_run_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_84 = None
        else:
            self.perform_run_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_85 = None
        else:
            self.perform_run_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_86 = None
        else:
            self.perform_run_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_87 = None
        else:
            self.perform_run_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_88 = None
        else:
            self.perform_run_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_89 = None
        else:
            self.perform_run_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_90 = None
        else:
            self.perform_run_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_91 = None
        else:
            self.perform_run_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_92 = None
        else:
            self.perform_run_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_93 = None
        else:
            self.perform_run_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_94 = None
        else:
            self.perform_run_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_95 = None
        else:
            self.perform_run_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_96 = None
        else:
            self.perform_run_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_97 = None
        else:
            self.perform_run_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_98 = None
        else:
            self.perform_run_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_99 = None
        else:
            self.perform_run_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.perform_run_100 = None
        else:
            self.perform_run_100 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def perform_run_1(self):
        """Get perform_run_1

        Returns:
            str: the value of `perform_run_1` or None if not set
        """
        return self._data["Perform Run 1"]

    @perform_run_1.setter
    def perform_run_1(self, value="Yes"):
        """  Corresponds to IDD Field `Perform Run 1`

        Args:
            value (str): value for IDD Field `Perform Run 1`
                Accepted values are:
                      - Yes
                      - No
                Default value: Yes
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_1`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_1`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 1"] = value

    @property
    def perform_run_2(self):
        """Get perform_run_2

        Returns:
            str: the value of `perform_run_2` or None if not set
        """
        return self._data["Perform Run 2"]

    @perform_run_2.setter
    def perform_run_2(self, value=None):
        """  Corresponds to IDD Field `Perform Run 2`

        Args:
            value (str): value for IDD Field `Perform Run 2`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_2`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_2`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 2"] = value

    @property
    def perform_run_3(self):
        """Get perform_run_3

        Returns:
            str: the value of `perform_run_3` or None if not set
        """
        return self._data["Perform Run 3"]

    @perform_run_3.setter
    def perform_run_3(self, value=None):
        """  Corresponds to IDD Field `Perform Run 3`

        Args:
            value (str): value for IDD Field `Perform Run 3`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_3`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_3`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 3"] = value

    @property
    def perform_run_4(self):
        """Get perform_run_4

        Returns:
            str: the value of `perform_run_4` or None if not set
        """
        return self._data["Perform Run 4"]

    @perform_run_4.setter
    def perform_run_4(self, value=None):
        """  Corresponds to IDD Field `Perform Run 4`

        Args:
            value (str): value for IDD Field `Perform Run 4`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_4`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_4`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 4"] = value

    @property
    def perform_run_5(self):
        """Get perform_run_5

        Returns:
            str: the value of `perform_run_5` or None if not set
        """
        return self._data["Perform Run 5"]

    @perform_run_5.setter
    def perform_run_5(self, value=None):
        """  Corresponds to IDD Field `Perform Run 5`

        Args:
            value (str): value for IDD Field `Perform Run 5`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_5`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_5`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 5"] = value

    @property
    def perform_run_6(self):
        """Get perform_run_6

        Returns:
            str: the value of `perform_run_6` or None if not set
        """
        return self._data["Perform Run 6"]

    @perform_run_6.setter
    def perform_run_6(self, value=None):
        """  Corresponds to IDD Field `Perform Run 6`

        Args:
            value (str): value for IDD Field `Perform Run 6`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_6`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_6`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 6"] = value

    @property
    def perform_run_7(self):
        """Get perform_run_7

        Returns:
            str: the value of `perform_run_7` or None if not set
        """
        return self._data["Perform Run 7"]

    @perform_run_7.setter
    def perform_run_7(self, value=None):
        """  Corresponds to IDD Field `Perform Run 7`

        Args:
            value (str): value for IDD Field `Perform Run 7`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_7`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_7`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 7"] = value

    @property
    def perform_run_8(self):
        """Get perform_run_8

        Returns:
            str: the value of `perform_run_8` or None if not set
        """
        return self._data["Perform Run 8"]

    @perform_run_8.setter
    def perform_run_8(self, value=None):
        """  Corresponds to IDD Field `Perform Run 8`

        Args:
            value (str): value for IDD Field `Perform Run 8`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_8`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_8`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 8"] = value

    @property
    def perform_run_9(self):
        """Get perform_run_9

        Returns:
            str: the value of `perform_run_9` or None if not set
        """
        return self._data["Perform Run 9"]

    @perform_run_9.setter
    def perform_run_9(self, value=None):
        """  Corresponds to IDD Field `Perform Run 9`

        Args:
            value (str): value for IDD Field `Perform Run 9`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_9`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_9`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 9"] = value

    @property
    def perform_run_10(self):
        """Get perform_run_10

        Returns:
            str: the value of `perform_run_10` or None if not set
        """
        return self._data["Perform Run 10"]

    @perform_run_10.setter
    def perform_run_10(self, value=None):
        """  Corresponds to IDD Field `Perform Run 10`

        Args:
            value (str): value for IDD Field `Perform Run 10`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_10`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_10`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 10"] = value

    @property
    def perform_run_11(self):
        """Get perform_run_11

        Returns:
            str: the value of `perform_run_11` or None if not set
        """
        return self._data["Perform Run 11"]

    @perform_run_11.setter
    def perform_run_11(self, value=None):
        """  Corresponds to IDD Field `Perform Run 11`

        Args:
            value (str): value for IDD Field `Perform Run 11`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_11`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_11`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 11"] = value

    @property
    def perform_run_12(self):
        """Get perform_run_12

        Returns:
            str: the value of `perform_run_12` or None if not set
        """
        return self._data["Perform Run 12"]

    @perform_run_12.setter
    def perform_run_12(self, value=None):
        """  Corresponds to IDD Field `Perform Run 12`

        Args:
            value (str): value for IDD Field `Perform Run 12`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_12`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_12`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 12"] = value

    @property
    def perform_run_13(self):
        """Get perform_run_13

        Returns:
            str: the value of `perform_run_13` or None if not set
        """
        return self._data["Perform Run 13"]

    @perform_run_13.setter
    def perform_run_13(self, value=None):
        """  Corresponds to IDD Field `Perform Run 13`

        Args:
            value (str): value for IDD Field `Perform Run 13`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_13`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_13`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 13"] = value

    @property
    def perform_run_14(self):
        """Get perform_run_14

        Returns:
            str: the value of `perform_run_14` or None if not set
        """
        return self._data["Perform Run 14"]

    @perform_run_14.setter
    def perform_run_14(self, value=None):
        """  Corresponds to IDD Field `Perform Run 14`

        Args:
            value (str): value for IDD Field `Perform Run 14`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_14`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_14`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 14"] = value

    @property
    def perform_run_15(self):
        """Get perform_run_15

        Returns:
            str: the value of `perform_run_15` or None if not set
        """
        return self._data["Perform Run 15"]

    @perform_run_15.setter
    def perform_run_15(self, value=None):
        """  Corresponds to IDD Field `Perform Run 15`

        Args:
            value (str): value for IDD Field `Perform Run 15`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_15`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_15`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 15"] = value

    @property
    def perform_run_16(self):
        """Get perform_run_16

        Returns:
            str: the value of `perform_run_16` or None if not set
        """
        return self._data["Perform Run 16"]

    @perform_run_16.setter
    def perform_run_16(self, value=None):
        """  Corresponds to IDD Field `Perform Run 16`

        Args:
            value (str): value for IDD Field `Perform Run 16`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_16`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_16`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 16"] = value

    @property
    def perform_run_17(self):
        """Get perform_run_17

        Returns:
            str: the value of `perform_run_17` or None if not set
        """
        return self._data["Perform Run 17"]

    @perform_run_17.setter
    def perform_run_17(self, value=None):
        """  Corresponds to IDD Field `Perform Run 17`

        Args:
            value (str): value for IDD Field `Perform Run 17`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_17`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_17`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 17"] = value

    @property
    def perform_run_18(self):
        """Get perform_run_18

        Returns:
            str: the value of `perform_run_18` or None if not set
        """
        return self._data["Perform Run 18"]

    @perform_run_18.setter
    def perform_run_18(self, value=None):
        """  Corresponds to IDD Field `Perform Run 18`

        Args:
            value (str): value for IDD Field `Perform Run 18`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_18`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_18`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 18"] = value

    @property
    def perform_run_19(self):
        """Get perform_run_19

        Returns:
            str: the value of `perform_run_19` or None if not set
        """
        return self._data["Perform Run 19"]

    @perform_run_19.setter
    def perform_run_19(self, value=None):
        """  Corresponds to IDD Field `Perform Run 19`

        Args:
            value (str): value for IDD Field `Perform Run 19`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_19`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_19`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 19"] = value

    @property
    def perform_run_20(self):
        """Get perform_run_20

        Returns:
            str: the value of `perform_run_20` or None if not set
        """
        return self._data["Perform Run 20"]

    @perform_run_20.setter
    def perform_run_20(self, value=None):
        """  Corresponds to IDD Field `Perform Run 20`

        Args:
            value (str): value for IDD Field `Perform Run 20`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_20`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_20`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 20"] = value

    @property
    def perform_run_21(self):
        """Get perform_run_21

        Returns:
            str: the value of `perform_run_21` or None if not set
        """
        return self._data["Perform Run 21"]

    @perform_run_21.setter
    def perform_run_21(self, value=None):
        """  Corresponds to IDD Field `Perform Run 21`

        Args:
            value (str): value for IDD Field `Perform Run 21`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_21`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_21`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 21"] = value

    @property
    def perform_run_22(self):
        """Get perform_run_22

        Returns:
            str: the value of `perform_run_22` or None if not set
        """
        return self._data["Perform Run 22"]

    @perform_run_22.setter
    def perform_run_22(self, value=None):
        """  Corresponds to IDD Field `Perform Run 22`

        Args:
            value (str): value for IDD Field `Perform Run 22`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_22`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_22`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 22"] = value

    @property
    def perform_run_23(self):
        """Get perform_run_23

        Returns:
            str: the value of `perform_run_23` or None if not set
        """
        return self._data["Perform Run 23"]

    @perform_run_23.setter
    def perform_run_23(self, value=None):
        """  Corresponds to IDD Field `Perform Run 23`

        Args:
            value (str): value for IDD Field `Perform Run 23`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_23`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_23`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 23"] = value

    @property
    def perform_run_24(self):
        """Get perform_run_24

        Returns:
            str: the value of `perform_run_24` or None if not set
        """
        return self._data["Perform Run 24"]

    @perform_run_24.setter
    def perform_run_24(self, value=None):
        """  Corresponds to IDD Field `Perform Run 24`

        Args:
            value (str): value for IDD Field `Perform Run 24`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_24`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_24`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 24"] = value

    @property
    def perform_run_25(self):
        """Get perform_run_25

        Returns:
            str: the value of `perform_run_25` or None if not set
        """
        return self._data["Perform Run 25"]

    @perform_run_25.setter
    def perform_run_25(self, value=None):
        """  Corresponds to IDD Field `Perform Run 25`

        Args:
            value (str): value for IDD Field `Perform Run 25`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_25`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_25`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 25"] = value

    @property
    def perform_run_26(self):
        """Get perform_run_26

        Returns:
            str: the value of `perform_run_26` or None if not set
        """
        return self._data["Perform Run 26"]

    @perform_run_26.setter
    def perform_run_26(self, value=None):
        """  Corresponds to IDD Field `Perform Run 26`

        Args:
            value (str): value for IDD Field `Perform Run 26`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_26`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_26`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 26"] = value

    @property
    def perform_run_27(self):
        """Get perform_run_27

        Returns:
            str: the value of `perform_run_27` or None if not set
        """
        return self._data["Perform Run 27"]

    @perform_run_27.setter
    def perform_run_27(self, value=None):
        """  Corresponds to IDD Field `Perform Run 27`

        Args:
            value (str): value for IDD Field `Perform Run 27`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_27`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_27`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 27"] = value

    @property
    def perform_run_28(self):
        """Get perform_run_28

        Returns:
            str: the value of `perform_run_28` or None if not set
        """
        return self._data["Perform Run 28"]

    @perform_run_28.setter
    def perform_run_28(self, value=None):
        """  Corresponds to IDD Field `Perform Run 28`

        Args:
            value (str): value for IDD Field `Perform Run 28`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_28`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_28`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 28"] = value

    @property
    def perform_run_29(self):
        """Get perform_run_29

        Returns:
            str: the value of `perform_run_29` or None if not set
        """
        return self._data["Perform Run 29"]

    @perform_run_29.setter
    def perform_run_29(self, value=None):
        """  Corresponds to IDD Field `Perform Run 29`

        Args:
            value (str): value for IDD Field `Perform Run 29`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_29`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_29`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 29"] = value

    @property
    def perform_run_30(self):
        """Get perform_run_30

        Returns:
            str: the value of `perform_run_30` or None if not set
        """
        return self._data["Perform Run 30"]

    @perform_run_30.setter
    def perform_run_30(self, value=None):
        """  Corresponds to IDD Field `Perform Run 30`

        Args:
            value (str): value for IDD Field `Perform Run 30`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_30`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_30`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 30"] = value

    @property
    def perform_run_31(self):
        """Get perform_run_31

        Returns:
            str: the value of `perform_run_31` or None if not set
        """
        return self._data["Perform Run 31"]

    @perform_run_31.setter
    def perform_run_31(self, value=None):
        """  Corresponds to IDD Field `Perform Run 31`

        Args:
            value (str): value for IDD Field `Perform Run 31`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_31`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_31`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_31`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 31"] = value

    @property
    def perform_run_32(self):
        """Get perform_run_32

        Returns:
            str: the value of `perform_run_32` or None if not set
        """
        return self._data["Perform Run 32"]

    @perform_run_32.setter
    def perform_run_32(self, value=None):
        """  Corresponds to IDD Field `Perform Run 32`

        Args:
            value (str): value for IDD Field `Perform Run 32`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_32`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_32`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_32`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 32"] = value

    @property
    def perform_run_33(self):
        """Get perform_run_33

        Returns:
            str: the value of `perform_run_33` or None if not set
        """
        return self._data["Perform Run 33"]

    @perform_run_33.setter
    def perform_run_33(self, value=None):
        """  Corresponds to IDD Field `Perform Run 33`

        Args:
            value (str): value for IDD Field `Perform Run 33`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_33`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_33`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_33`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 33"] = value

    @property
    def perform_run_34(self):
        """Get perform_run_34

        Returns:
            str: the value of `perform_run_34` or None if not set
        """
        return self._data["Perform Run 34"]

    @perform_run_34.setter
    def perform_run_34(self, value=None):
        """  Corresponds to IDD Field `Perform Run 34`

        Args:
            value (str): value for IDD Field `Perform Run 34`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_34`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_34`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_34`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 34"] = value

    @property
    def perform_run_35(self):
        """Get perform_run_35

        Returns:
            str: the value of `perform_run_35` or None if not set
        """
        return self._data["Perform Run 35"]

    @perform_run_35.setter
    def perform_run_35(self, value=None):
        """  Corresponds to IDD Field `Perform Run 35`

        Args:
            value (str): value for IDD Field `Perform Run 35`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_35`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_35`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_35`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 35"] = value

    @property
    def perform_run_36(self):
        """Get perform_run_36

        Returns:
            str: the value of `perform_run_36` or None if not set
        """
        return self._data["Perform Run 36"]

    @perform_run_36.setter
    def perform_run_36(self, value=None):
        """  Corresponds to IDD Field `Perform Run 36`

        Args:
            value (str): value for IDD Field `Perform Run 36`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_36`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_36`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_36`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 36"] = value

    @property
    def perform_run_37(self):
        """Get perform_run_37

        Returns:
            str: the value of `perform_run_37` or None if not set
        """
        return self._data["Perform Run 37"]

    @perform_run_37.setter
    def perform_run_37(self, value=None):
        """  Corresponds to IDD Field `Perform Run 37`

        Args:
            value (str): value for IDD Field `Perform Run 37`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_37`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_37`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_37`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 37"] = value

    @property
    def perform_run_38(self):
        """Get perform_run_38

        Returns:
            str: the value of `perform_run_38` or None if not set
        """
        return self._data["Perform Run 38"]

    @perform_run_38.setter
    def perform_run_38(self, value=None):
        """  Corresponds to IDD Field `Perform Run 38`

        Args:
            value (str): value for IDD Field `Perform Run 38`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_38`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_38`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_38`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 38"] = value

    @property
    def perform_run_39(self):
        """Get perform_run_39

        Returns:
            str: the value of `perform_run_39` or None if not set
        """
        return self._data["Perform Run 39"]

    @perform_run_39.setter
    def perform_run_39(self, value=None):
        """  Corresponds to IDD Field `Perform Run 39`

        Args:
            value (str): value for IDD Field `Perform Run 39`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_39`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_39`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_39`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 39"] = value

    @property
    def perform_run_40(self):
        """Get perform_run_40

        Returns:
            str: the value of `perform_run_40` or None if not set
        """
        return self._data["Perform Run 40"]

    @perform_run_40.setter
    def perform_run_40(self, value=None):
        """  Corresponds to IDD Field `Perform Run 40`

        Args:
            value (str): value for IDD Field `Perform Run 40`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_40`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_40`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_40`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 40"] = value

    @property
    def perform_run_41(self):
        """Get perform_run_41

        Returns:
            str: the value of `perform_run_41` or None if not set
        """
        return self._data["Perform Run 41"]

    @perform_run_41.setter
    def perform_run_41(self, value=None):
        """  Corresponds to IDD Field `Perform Run 41`

        Args:
            value (str): value for IDD Field `Perform Run 41`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_41`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_41`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_41`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 41"] = value

    @property
    def perform_run_42(self):
        """Get perform_run_42

        Returns:
            str: the value of `perform_run_42` or None if not set
        """
        return self._data["Perform Run 42"]

    @perform_run_42.setter
    def perform_run_42(self, value=None):
        """  Corresponds to IDD Field `Perform Run 42`

        Args:
            value (str): value for IDD Field `Perform Run 42`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_42`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_42`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_42`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 42"] = value

    @property
    def perform_run_43(self):
        """Get perform_run_43

        Returns:
            str: the value of `perform_run_43` or None if not set
        """
        return self._data["Perform Run 43"]

    @perform_run_43.setter
    def perform_run_43(self, value=None):
        """  Corresponds to IDD Field `Perform Run 43`

        Args:
            value (str): value for IDD Field `Perform Run 43`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_43`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_43`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_43`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 43"] = value

    @property
    def perform_run_44(self):
        """Get perform_run_44

        Returns:
            str: the value of `perform_run_44` or None if not set
        """
        return self._data["Perform Run 44"]

    @perform_run_44.setter
    def perform_run_44(self, value=None):
        """  Corresponds to IDD Field `Perform Run 44`

        Args:
            value (str): value for IDD Field `Perform Run 44`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_44`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_44`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_44`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 44"] = value

    @property
    def perform_run_45(self):
        """Get perform_run_45

        Returns:
            str: the value of `perform_run_45` or None if not set
        """
        return self._data["Perform Run 45"]

    @perform_run_45.setter
    def perform_run_45(self, value=None):
        """  Corresponds to IDD Field `Perform Run 45`

        Args:
            value (str): value for IDD Field `Perform Run 45`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_45`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_45`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_45`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 45"] = value

    @property
    def perform_run_46(self):
        """Get perform_run_46

        Returns:
            str: the value of `perform_run_46` or None if not set
        """
        return self._data["Perform Run 46"]

    @perform_run_46.setter
    def perform_run_46(self, value=None):
        """  Corresponds to IDD Field `Perform Run 46`

        Args:
            value (str): value for IDD Field `Perform Run 46`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_46`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_46`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_46`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 46"] = value

    @property
    def perform_run_47(self):
        """Get perform_run_47

        Returns:
            str: the value of `perform_run_47` or None if not set
        """
        return self._data["Perform Run 47"]

    @perform_run_47.setter
    def perform_run_47(self, value=None):
        """  Corresponds to IDD Field `Perform Run 47`

        Args:
            value (str): value for IDD Field `Perform Run 47`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_47`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_47`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_47`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 47"] = value

    @property
    def perform_run_48(self):
        """Get perform_run_48

        Returns:
            str: the value of `perform_run_48` or None if not set
        """
        return self._data["Perform Run 48"]

    @perform_run_48.setter
    def perform_run_48(self, value=None):
        """  Corresponds to IDD Field `Perform Run 48`

        Args:
            value (str): value for IDD Field `Perform Run 48`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_48`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_48`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_48`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 48"] = value

    @property
    def perform_run_49(self):
        """Get perform_run_49

        Returns:
            str: the value of `perform_run_49` or None if not set
        """
        return self._data["Perform Run 49"]

    @perform_run_49.setter
    def perform_run_49(self, value=None):
        """  Corresponds to IDD Field `Perform Run 49`

        Args:
            value (str): value for IDD Field `Perform Run 49`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_49`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_49`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_49`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 49"] = value

    @property
    def perform_run_50(self):
        """Get perform_run_50

        Returns:
            str: the value of `perform_run_50` or None if not set
        """
        return self._data["Perform Run 50"]

    @perform_run_50.setter
    def perform_run_50(self, value=None):
        """  Corresponds to IDD Field `Perform Run 50`

        Args:
            value (str): value for IDD Field `Perform Run 50`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_50`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_50`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_50`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 50"] = value

    @property
    def perform_run_51(self):
        """Get perform_run_51

        Returns:
            str: the value of `perform_run_51` or None if not set
        """
        return self._data["Perform Run 51"]

    @perform_run_51.setter
    def perform_run_51(self, value=None):
        """  Corresponds to IDD Field `Perform Run 51`

        Args:
            value (str): value for IDD Field `Perform Run 51`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_51`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_51`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_51`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 51"] = value

    @property
    def perform_run_52(self):
        """Get perform_run_52

        Returns:
            str: the value of `perform_run_52` or None if not set
        """
        return self._data["Perform Run 52"]

    @perform_run_52.setter
    def perform_run_52(self, value=None):
        """  Corresponds to IDD Field `Perform Run 52`

        Args:
            value (str): value for IDD Field `Perform Run 52`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_52`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_52`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_52`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 52"] = value

    @property
    def perform_run_53(self):
        """Get perform_run_53

        Returns:
            str: the value of `perform_run_53` or None if not set
        """
        return self._data["Perform Run 53"]

    @perform_run_53.setter
    def perform_run_53(self, value=None):
        """  Corresponds to IDD Field `Perform Run 53`

        Args:
            value (str): value for IDD Field `Perform Run 53`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_53`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_53`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_53`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 53"] = value

    @property
    def perform_run_54(self):
        """Get perform_run_54

        Returns:
            str: the value of `perform_run_54` or None if not set
        """
        return self._data["Perform Run 54"]

    @perform_run_54.setter
    def perform_run_54(self, value=None):
        """  Corresponds to IDD Field `Perform Run 54`

        Args:
            value (str): value for IDD Field `Perform Run 54`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_54`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_54`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_54`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 54"] = value

    @property
    def perform_run_55(self):
        """Get perform_run_55

        Returns:
            str: the value of `perform_run_55` or None if not set
        """
        return self._data["Perform Run 55"]

    @perform_run_55.setter
    def perform_run_55(self, value=None):
        """  Corresponds to IDD Field `Perform Run 55`

        Args:
            value (str): value for IDD Field `Perform Run 55`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_55`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_55`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_55`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 55"] = value

    @property
    def perform_run_56(self):
        """Get perform_run_56

        Returns:
            str: the value of `perform_run_56` or None if not set
        """
        return self._data["Perform Run 56"]

    @perform_run_56.setter
    def perform_run_56(self, value=None):
        """  Corresponds to IDD Field `Perform Run 56`

        Args:
            value (str): value for IDD Field `Perform Run 56`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_56`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_56`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_56`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 56"] = value

    @property
    def perform_run_57(self):
        """Get perform_run_57

        Returns:
            str: the value of `perform_run_57` or None if not set
        """
        return self._data["Perform Run 57"]

    @perform_run_57.setter
    def perform_run_57(self, value=None):
        """  Corresponds to IDD Field `Perform Run 57`

        Args:
            value (str): value for IDD Field `Perform Run 57`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_57`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_57`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_57`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 57"] = value

    @property
    def perform_run_58(self):
        """Get perform_run_58

        Returns:
            str: the value of `perform_run_58` or None if not set
        """
        return self._data["Perform Run 58"]

    @perform_run_58.setter
    def perform_run_58(self, value=None):
        """  Corresponds to IDD Field `Perform Run 58`

        Args:
            value (str): value for IDD Field `Perform Run 58`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_58`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_58`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_58`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 58"] = value

    @property
    def perform_run_59(self):
        """Get perform_run_59

        Returns:
            str: the value of `perform_run_59` or None if not set
        """
        return self._data["Perform Run 59"]

    @perform_run_59.setter
    def perform_run_59(self, value=None):
        """  Corresponds to IDD Field `Perform Run 59`

        Args:
            value (str): value for IDD Field `Perform Run 59`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_59`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_59`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_59`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 59"] = value

    @property
    def perform_run_60(self):
        """Get perform_run_60

        Returns:
            str: the value of `perform_run_60` or None if not set
        """
        return self._data["Perform Run 60"]

    @perform_run_60.setter
    def perform_run_60(self, value=None):
        """  Corresponds to IDD Field `Perform Run 60`

        Args:
            value (str): value for IDD Field `Perform Run 60`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_60`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_60`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_60`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 60"] = value

    @property
    def perform_run_61(self):
        """Get perform_run_61

        Returns:
            str: the value of `perform_run_61` or None if not set
        """
        return self._data["Perform Run 61"]

    @perform_run_61.setter
    def perform_run_61(self, value=None):
        """  Corresponds to IDD Field `Perform Run 61`

        Args:
            value (str): value for IDD Field `Perform Run 61`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_61`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_61`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_61`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 61"] = value

    @property
    def perform_run_62(self):
        """Get perform_run_62

        Returns:
            str: the value of `perform_run_62` or None if not set
        """
        return self._data["Perform Run 62"]

    @perform_run_62.setter
    def perform_run_62(self, value=None):
        """  Corresponds to IDD Field `Perform Run 62`

        Args:
            value (str): value for IDD Field `Perform Run 62`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_62`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_62`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_62`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 62"] = value

    @property
    def perform_run_63(self):
        """Get perform_run_63

        Returns:
            str: the value of `perform_run_63` or None if not set
        """
        return self._data["Perform Run 63"]

    @perform_run_63.setter
    def perform_run_63(self, value=None):
        """  Corresponds to IDD Field `Perform Run 63`

        Args:
            value (str): value for IDD Field `Perform Run 63`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_63`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_63`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_63`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 63"] = value

    @property
    def perform_run_64(self):
        """Get perform_run_64

        Returns:
            str: the value of `perform_run_64` or None if not set
        """
        return self._data["Perform Run 64"]

    @perform_run_64.setter
    def perform_run_64(self, value=None):
        """  Corresponds to IDD Field `Perform Run 64`

        Args:
            value (str): value for IDD Field `Perform Run 64`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_64`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_64`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_64`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 64"] = value

    @property
    def perform_run_65(self):
        """Get perform_run_65

        Returns:
            str: the value of `perform_run_65` or None if not set
        """
        return self._data["Perform Run 65"]

    @perform_run_65.setter
    def perform_run_65(self, value=None):
        """  Corresponds to IDD Field `Perform Run 65`

        Args:
            value (str): value for IDD Field `Perform Run 65`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_65`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_65`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_65`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 65"] = value

    @property
    def perform_run_66(self):
        """Get perform_run_66

        Returns:
            str: the value of `perform_run_66` or None if not set
        """
        return self._data["Perform Run 66"]

    @perform_run_66.setter
    def perform_run_66(self, value=None):
        """  Corresponds to IDD Field `Perform Run 66`

        Args:
            value (str): value for IDD Field `Perform Run 66`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_66`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_66`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_66`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 66"] = value

    @property
    def perform_run_67(self):
        """Get perform_run_67

        Returns:
            str: the value of `perform_run_67` or None if not set
        """
        return self._data["Perform Run 67"]

    @perform_run_67.setter
    def perform_run_67(self, value=None):
        """  Corresponds to IDD Field `Perform Run 67`

        Args:
            value (str): value for IDD Field `Perform Run 67`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_67`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_67`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_67`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 67"] = value

    @property
    def perform_run_68(self):
        """Get perform_run_68

        Returns:
            str: the value of `perform_run_68` or None if not set
        """
        return self._data["Perform Run 68"]

    @perform_run_68.setter
    def perform_run_68(self, value=None):
        """  Corresponds to IDD Field `Perform Run 68`

        Args:
            value (str): value for IDD Field `Perform Run 68`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_68`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_68`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_68`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 68"] = value

    @property
    def perform_run_69(self):
        """Get perform_run_69

        Returns:
            str: the value of `perform_run_69` or None if not set
        """
        return self._data["Perform Run 69"]

    @perform_run_69.setter
    def perform_run_69(self, value=None):
        """  Corresponds to IDD Field `Perform Run 69`

        Args:
            value (str): value for IDD Field `Perform Run 69`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_69`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_69`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_69`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 69"] = value

    @property
    def perform_run_70(self):
        """Get perform_run_70

        Returns:
            str: the value of `perform_run_70` or None if not set
        """
        return self._data["Perform Run 70"]

    @perform_run_70.setter
    def perform_run_70(self, value=None):
        """  Corresponds to IDD Field `Perform Run 70`

        Args:
            value (str): value for IDD Field `Perform Run 70`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_70`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_70`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_70`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 70"] = value

    @property
    def perform_run_71(self):
        """Get perform_run_71

        Returns:
            str: the value of `perform_run_71` or None if not set
        """
        return self._data["Perform Run 71"]

    @perform_run_71.setter
    def perform_run_71(self, value=None):
        """  Corresponds to IDD Field `Perform Run 71`

        Args:
            value (str): value for IDD Field `Perform Run 71`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_71`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_71`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_71`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 71"] = value

    @property
    def perform_run_72(self):
        """Get perform_run_72

        Returns:
            str: the value of `perform_run_72` or None if not set
        """
        return self._data["Perform Run 72"]

    @perform_run_72.setter
    def perform_run_72(self, value=None):
        """  Corresponds to IDD Field `Perform Run 72`

        Args:
            value (str): value for IDD Field `Perform Run 72`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_72`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_72`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_72`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 72"] = value

    @property
    def perform_run_73(self):
        """Get perform_run_73

        Returns:
            str: the value of `perform_run_73` or None if not set
        """
        return self._data["Perform Run 73"]

    @perform_run_73.setter
    def perform_run_73(self, value=None):
        """  Corresponds to IDD Field `Perform Run 73`

        Args:
            value (str): value for IDD Field `Perform Run 73`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_73`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_73`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_73`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 73"] = value

    @property
    def perform_run_74(self):
        """Get perform_run_74

        Returns:
            str: the value of `perform_run_74` or None if not set
        """
        return self._data["Perform Run 74"]

    @perform_run_74.setter
    def perform_run_74(self, value=None):
        """  Corresponds to IDD Field `Perform Run 74`

        Args:
            value (str): value for IDD Field `Perform Run 74`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_74`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_74`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_74`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 74"] = value

    @property
    def perform_run_75(self):
        """Get perform_run_75

        Returns:
            str: the value of `perform_run_75` or None if not set
        """
        return self._data["Perform Run 75"]

    @perform_run_75.setter
    def perform_run_75(self, value=None):
        """  Corresponds to IDD Field `Perform Run 75`

        Args:
            value (str): value for IDD Field `Perform Run 75`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_75`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_75`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_75`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 75"] = value

    @property
    def perform_run_76(self):
        """Get perform_run_76

        Returns:
            str: the value of `perform_run_76` or None if not set
        """
        return self._data["Perform Run 76"]

    @perform_run_76.setter
    def perform_run_76(self, value=None):
        """  Corresponds to IDD Field `Perform Run 76`

        Args:
            value (str): value for IDD Field `Perform Run 76`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_76`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_76`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_76`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 76"] = value

    @property
    def perform_run_77(self):
        """Get perform_run_77

        Returns:
            str: the value of `perform_run_77` or None if not set
        """
        return self._data["Perform Run 77"]

    @perform_run_77.setter
    def perform_run_77(self, value=None):
        """  Corresponds to IDD Field `Perform Run 77`

        Args:
            value (str): value for IDD Field `Perform Run 77`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_77`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_77`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_77`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 77"] = value

    @property
    def perform_run_78(self):
        """Get perform_run_78

        Returns:
            str: the value of `perform_run_78` or None if not set
        """
        return self._data["Perform Run 78"]

    @perform_run_78.setter
    def perform_run_78(self, value=None):
        """  Corresponds to IDD Field `Perform Run 78`

        Args:
            value (str): value for IDD Field `Perform Run 78`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_78`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_78`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_78`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 78"] = value

    @property
    def perform_run_79(self):
        """Get perform_run_79

        Returns:
            str: the value of `perform_run_79` or None if not set
        """
        return self._data["Perform Run 79"]

    @perform_run_79.setter
    def perform_run_79(self, value=None):
        """  Corresponds to IDD Field `Perform Run 79`

        Args:
            value (str): value for IDD Field `Perform Run 79`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_79`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_79`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_79`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 79"] = value

    @property
    def perform_run_80(self):
        """Get perform_run_80

        Returns:
            str: the value of `perform_run_80` or None if not set
        """
        return self._data["Perform Run 80"]

    @perform_run_80.setter
    def perform_run_80(self, value=None):
        """  Corresponds to IDD Field `Perform Run 80`

        Args:
            value (str): value for IDD Field `Perform Run 80`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_80`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_80`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_80`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 80"] = value

    @property
    def perform_run_81(self):
        """Get perform_run_81

        Returns:
            str: the value of `perform_run_81` or None if not set
        """
        return self._data["Perform Run 81"]

    @perform_run_81.setter
    def perform_run_81(self, value=None):
        """  Corresponds to IDD Field `Perform Run 81`

        Args:
            value (str): value for IDD Field `Perform Run 81`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_81`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_81`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_81`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 81"] = value

    @property
    def perform_run_82(self):
        """Get perform_run_82

        Returns:
            str: the value of `perform_run_82` or None if not set
        """
        return self._data["Perform Run 82"]

    @perform_run_82.setter
    def perform_run_82(self, value=None):
        """  Corresponds to IDD Field `Perform Run 82`

        Args:
            value (str): value for IDD Field `Perform Run 82`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_82`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_82`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_82`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 82"] = value

    @property
    def perform_run_83(self):
        """Get perform_run_83

        Returns:
            str: the value of `perform_run_83` or None if not set
        """
        return self._data["Perform Run 83"]

    @perform_run_83.setter
    def perform_run_83(self, value=None):
        """  Corresponds to IDD Field `Perform Run 83`

        Args:
            value (str): value for IDD Field `Perform Run 83`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_83`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_83`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_83`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 83"] = value

    @property
    def perform_run_84(self):
        """Get perform_run_84

        Returns:
            str: the value of `perform_run_84` or None if not set
        """
        return self._data["Perform Run 84"]

    @perform_run_84.setter
    def perform_run_84(self, value=None):
        """  Corresponds to IDD Field `Perform Run 84`

        Args:
            value (str): value for IDD Field `Perform Run 84`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_84`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_84`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_84`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 84"] = value

    @property
    def perform_run_85(self):
        """Get perform_run_85

        Returns:
            str: the value of `perform_run_85` or None if not set
        """
        return self._data["Perform Run 85"]

    @perform_run_85.setter
    def perform_run_85(self, value=None):
        """  Corresponds to IDD Field `Perform Run 85`

        Args:
            value (str): value for IDD Field `Perform Run 85`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_85`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_85`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_85`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 85"] = value

    @property
    def perform_run_86(self):
        """Get perform_run_86

        Returns:
            str: the value of `perform_run_86` or None if not set
        """
        return self._data["Perform Run 86"]

    @perform_run_86.setter
    def perform_run_86(self, value=None):
        """  Corresponds to IDD Field `Perform Run 86`

        Args:
            value (str): value for IDD Field `Perform Run 86`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_86`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_86`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_86`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 86"] = value

    @property
    def perform_run_87(self):
        """Get perform_run_87

        Returns:
            str: the value of `perform_run_87` or None if not set
        """
        return self._data["Perform Run 87"]

    @perform_run_87.setter
    def perform_run_87(self, value=None):
        """  Corresponds to IDD Field `Perform Run 87`

        Args:
            value (str): value for IDD Field `Perform Run 87`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_87`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_87`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_87`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 87"] = value

    @property
    def perform_run_88(self):
        """Get perform_run_88

        Returns:
            str: the value of `perform_run_88` or None if not set
        """
        return self._data["Perform Run 88"]

    @perform_run_88.setter
    def perform_run_88(self, value=None):
        """  Corresponds to IDD Field `Perform Run 88`

        Args:
            value (str): value for IDD Field `Perform Run 88`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_88`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_88`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_88`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 88"] = value

    @property
    def perform_run_89(self):
        """Get perform_run_89

        Returns:
            str: the value of `perform_run_89` or None if not set
        """
        return self._data["Perform Run 89"]

    @perform_run_89.setter
    def perform_run_89(self, value=None):
        """  Corresponds to IDD Field `Perform Run 89`

        Args:
            value (str): value for IDD Field `Perform Run 89`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_89`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_89`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_89`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 89"] = value

    @property
    def perform_run_90(self):
        """Get perform_run_90

        Returns:
            str: the value of `perform_run_90` or None if not set
        """
        return self._data["Perform Run 90"]

    @perform_run_90.setter
    def perform_run_90(self, value=None):
        """  Corresponds to IDD Field `Perform Run 90`

        Args:
            value (str): value for IDD Field `Perform Run 90`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_90`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_90`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_90`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 90"] = value

    @property
    def perform_run_91(self):
        """Get perform_run_91

        Returns:
            str: the value of `perform_run_91` or None if not set
        """
        return self._data["Perform Run 91"]

    @perform_run_91.setter
    def perform_run_91(self, value=None):
        """  Corresponds to IDD Field `Perform Run 91`

        Args:
            value (str): value for IDD Field `Perform Run 91`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_91`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_91`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_91`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 91"] = value

    @property
    def perform_run_92(self):
        """Get perform_run_92

        Returns:
            str: the value of `perform_run_92` or None if not set
        """
        return self._data["Perform Run 92"]

    @perform_run_92.setter
    def perform_run_92(self, value=None):
        """  Corresponds to IDD Field `Perform Run 92`

        Args:
            value (str): value for IDD Field `Perform Run 92`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_92`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_92`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_92`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 92"] = value

    @property
    def perform_run_93(self):
        """Get perform_run_93

        Returns:
            str: the value of `perform_run_93` or None if not set
        """
        return self._data["Perform Run 93"]

    @perform_run_93.setter
    def perform_run_93(self, value=None):
        """  Corresponds to IDD Field `Perform Run 93`

        Args:
            value (str): value for IDD Field `Perform Run 93`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_93`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_93`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_93`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 93"] = value

    @property
    def perform_run_94(self):
        """Get perform_run_94

        Returns:
            str: the value of `perform_run_94` or None if not set
        """
        return self._data["Perform Run 94"]

    @perform_run_94.setter
    def perform_run_94(self, value=None):
        """  Corresponds to IDD Field `Perform Run 94`

        Args:
            value (str): value for IDD Field `Perform Run 94`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_94`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_94`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_94`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 94"] = value

    @property
    def perform_run_95(self):
        """Get perform_run_95

        Returns:
            str: the value of `perform_run_95` or None if not set
        """
        return self._data["Perform Run 95"]

    @perform_run_95.setter
    def perform_run_95(self, value=None):
        """  Corresponds to IDD Field `Perform Run 95`

        Args:
            value (str): value for IDD Field `Perform Run 95`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_95`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_95`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_95`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 95"] = value

    @property
    def perform_run_96(self):
        """Get perform_run_96

        Returns:
            str: the value of `perform_run_96` or None if not set
        """
        return self._data["Perform Run 96"]

    @perform_run_96.setter
    def perform_run_96(self, value=None):
        """  Corresponds to IDD Field `Perform Run 96`

        Args:
            value (str): value for IDD Field `Perform Run 96`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_96`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_96`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_96`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 96"] = value

    @property
    def perform_run_97(self):
        """Get perform_run_97

        Returns:
            str: the value of `perform_run_97` or None if not set
        """
        return self._data["Perform Run 97"]

    @perform_run_97.setter
    def perform_run_97(self, value=None):
        """  Corresponds to IDD Field `Perform Run 97`

        Args:
            value (str): value for IDD Field `Perform Run 97`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_97`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_97`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_97`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 97"] = value

    @property
    def perform_run_98(self):
        """Get perform_run_98

        Returns:
            str: the value of `perform_run_98` or None if not set
        """
        return self._data["Perform Run 98"]

    @perform_run_98.setter
    def perform_run_98(self, value=None):
        """  Corresponds to IDD Field `Perform Run 98`

        Args:
            value (str): value for IDD Field `Perform Run 98`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_98`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_98`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_98`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 98"] = value

    @property
    def perform_run_99(self):
        """Get perform_run_99

        Returns:
            str: the value of `perform_run_99` or None if not set
        """
        return self._data["Perform Run 99"]

    @perform_run_99.setter
    def perform_run_99(self, value=None):
        """  Corresponds to IDD Field `Perform Run 99`

        Args:
            value (str): value for IDD Field `Perform Run 99`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_99`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_99`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_99`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 99"] = value

    @property
    def perform_run_100(self):
        """Get perform_run_100

        Returns:
            str: the value of `perform_run_100` or None if not set
        """
        return self._data["Perform Run 100"]

    @perform_run_100.setter
    def perform_run_100(self, value=None):
        """  Corresponds to IDD Field `Perform Run 100`

        Args:
            value (str): value for IDD Field `Perform Run 100`
                Accepted values are:
                      - Yes
                      - No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `perform_run_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `perform_run_100`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `perform_run_100`')
            vals = {}
            vals["yes"] = "Yes"
            vals["no"] = "No"
            value_lower = value.lower()
            if value_lower not in vals:
                found = False
                if self.accept_substring:
                    for key in vals:
                        if key in value_lower:
                            value_lower = key
                            found = True
                            break

                if not found:
                    raise ValueError('value {} is not an accepted value for '
                                     'field `perform_run_100`'.format(value))
            value = vals[value_lower]
        self._data["Perform Run 100"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])

class ParametricFileNameSuffix(object):
    """ Corresponds to IDD object `Parametric:FileNameSuffix`
        Defines the suffixes to be appended to the idf and output file names for each
        parametric run. If this object is omitted, the suffix will default to the run number.
    
    """
    internal_name = "Parametric:FileNameSuffix"
    field_count = 101
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Parametric:FileNameSuffix`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Suffix for File Name in Run 1"] = None
        self._data["Suffix for File Name in Run 2"] = None
        self._data["Suffix for File Name in Run 3"] = None
        self._data["Suffix for File Name in Run 4"] = None
        self._data["Suffix for File Name in Run 5"] = None
        self._data["Suffix for File Name in Run 6"] = None
        self._data["Suffix for File Name in Run 7"] = None
        self._data["Suffix for File Name in Run 8"] = None
        self._data["Suffix for File Name in Run 9"] = None
        self._data["Suffix for File Name in Run 10"] = None
        self._data["Suffix for File Name in Run 11"] = None
        self._data["Suffix for File Name in Run 12"] = None
        self._data["Suffix for File Name in Run 13"] = None
        self._data["Suffix for File Name in Run 14"] = None
        self._data["Suffix for File Name in Run 15"] = None
        self._data["Suffix for File Name in Run 16"] = None
        self._data["Suffix for File Name in Run 17"] = None
        self._data["Suffix for File Name in Run 18"] = None
        self._data["Suffix for File Name in Run 19"] = None
        self._data["Suffix for File Name in Run 20"] = None
        self._data["Suffix for File Name in Run 21"] = None
        self._data["Suffix for File Name in Run 22"] = None
        self._data["Suffix for File Name in Run 23"] = None
        self._data["Suffix for File Name in Run 24"] = None
        self._data["Suffix for File Name in Run 25"] = None
        self._data["Suffix for File Name in Run 26"] = None
        self._data["Suffix for File Name in Run 27"] = None
        self._data["Suffix for File Name in Run 28"] = None
        self._data["Suffix for File Name in Run 29"] = None
        self._data["Suffix for File Name in Run 30"] = None
        self._data["Suffix for File Name in Run 31"] = None
        self._data["Suffix for File Name in Run 32"] = None
        self._data["Suffix for File Name in Run 33"] = None
        self._data["Suffix for File Name in Run 34"] = None
        self._data["Suffix for File Name in Run 35"] = None
        self._data["Suffix for File Name in Run 36"] = None
        self._data["Suffix for File Name in Run 37"] = None
        self._data["Suffix for File Name in Run 38"] = None
        self._data["Suffix for File Name in Run 39"] = None
        self._data["Suffix for File Name in Run 40"] = None
        self._data["Suffix for File Name in Run 41"] = None
        self._data["Suffix for File Name in Run 42"] = None
        self._data["Suffix for File Name in Run 43"] = None
        self._data["Suffix for File Name in Run 44"] = None
        self._data["Suffix for File Name in Run 45"] = None
        self._data["Suffix for File Name in Run 46"] = None
        self._data["Suffix for File Name in Run 47"] = None
        self._data["Suffix for File Name in Run 48"] = None
        self._data["Suffix for File Name in Run 49"] = None
        self._data["Suffix for File Name in Run 50"] = None
        self._data["Suffix for File Name in Run 51"] = None
        self._data["Suffix for File Name in Run 52"] = None
        self._data["Suffix for File Name in Run 53"] = None
        self._data["Suffix for File Name in Run 54"] = None
        self._data["Suffix for File Name in Run 55"] = None
        self._data["Suffix for File Name in Run 56"] = None
        self._data["Suffix for File Name in Run 57"] = None
        self._data["Suffix for File Name in Run 58"] = None
        self._data["Suffix for File Name in Run 59"] = None
        self._data["Suffix for File Name in Run 60"] = None
        self._data["Suffix for File Name in Run 61"] = None
        self._data["Suffix for File Name in Run 62"] = None
        self._data["Suffix for File Name in Run 63"] = None
        self._data["Suffix for File Name in Run 64"] = None
        self._data["Suffix for File Name in Run 65"] = None
        self._data["Suffix for File Name in Run 66"] = None
        self._data["Suffix for File Name in Run 67"] = None
        self._data["Suffix for File Name in Run 68"] = None
        self._data["Suffix for File Name in Run 69"] = None
        self._data["Suffix for File Name in Run 70"] = None
        self._data["Suffix for File Name in Run 71"] = None
        self._data["Suffix for File Name in Run 72"] = None
        self._data["Suffix for File Name in Run 73"] = None
        self._data["Suffix for File Name in Run 74"] = None
        self._data["Suffix for File Name in Run 75"] = None
        self._data["Suffix for File Name in Run 76"] = None
        self._data["Suffix for File Name in Run 77"] = None
        self._data["Suffix for File Name in Run 78"] = None
        self._data["Suffix for File Name in Run 79"] = None
        self._data["Suffix for File Name in Run 80"] = None
        self._data["Suffix for File Name in Run 81"] = None
        self._data["Suffix for File Name in Run 82"] = None
        self._data["Suffix for File Name in Run 83"] = None
        self._data["Suffix for File Name in Run 84"] = None
        self._data["Suffix for File Name in Run 85"] = None
        self._data["Suffix for File Name in Run 86"] = None
        self._data["Suffix for File Name in Run 87"] = None
        self._data["Suffix for File Name in Run 88"] = None
        self._data["Suffix for File Name in Run 89"] = None
        self._data["Suffix for File Name in Run 90"] = None
        self._data["Suffix for File Name in Run 91"] = None
        self._data["Suffix for File Name in Run 92"] = None
        self._data["Suffix for File Name in Run 93"] = None
        self._data["Suffix for File Name in Run 94"] = None
        self._data["Suffix for File Name in Run 95"] = None
        self._data["Suffix for File Name in Run 96"] = None
        self._data["Suffix for File Name in Run 97"] = None
        self._data["Suffix for File Name in Run 98"] = None
        self._data["Suffix for File Name in Run 99"] = None
        self._data["Suffix for File Name in Run 100"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.name = None
        else:
            self.name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_1 = None
        else:
            self.suffix_for_file_name_in_run_1 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_2 = None
        else:
            self.suffix_for_file_name_in_run_2 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_3 = None
        else:
            self.suffix_for_file_name_in_run_3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_4 = None
        else:
            self.suffix_for_file_name_in_run_4 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_5 = None
        else:
            self.suffix_for_file_name_in_run_5 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_6 = None
        else:
            self.suffix_for_file_name_in_run_6 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_7 = None
        else:
            self.suffix_for_file_name_in_run_7 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_8 = None
        else:
            self.suffix_for_file_name_in_run_8 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_9 = None
        else:
            self.suffix_for_file_name_in_run_9 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_10 = None
        else:
            self.suffix_for_file_name_in_run_10 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_11 = None
        else:
            self.suffix_for_file_name_in_run_11 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_12 = None
        else:
            self.suffix_for_file_name_in_run_12 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_13 = None
        else:
            self.suffix_for_file_name_in_run_13 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_14 = None
        else:
            self.suffix_for_file_name_in_run_14 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_15 = None
        else:
            self.suffix_for_file_name_in_run_15 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_16 = None
        else:
            self.suffix_for_file_name_in_run_16 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_17 = None
        else:
            self.suffix_for_file_name_in_run_17 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_18 = None
        else:
            self.suffix_for_file_name_in_run_18 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_19 = None
        else:
            self.suffix_for_file_name_in_run_19 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_20 = None
        else:
            self.suffix_for_file_name_in_run_20 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_21 = None
        else:
            self.suffix_for_file_name_in_run_21 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_22 = None
        else:
            self.suffix_for_file_name_in_run_22 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_23 = None
        else:
            self.suffix_for_file_name_in_run_23 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_24 = None
        else:
            self.suffix_for_file_name_in_run_24 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_25 = None
        else:
            self.suffix_for_file_name_in_run_25 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_26 = None
        else:
            self.suffix_for_file_name_in_run_26 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_27 = None
        else:
            self.suffix_for_file_name_in_run_27 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_28 = None
        else:
            self.suffix_for_file_name_in_run_28 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_29 = None
        else:
            self.suffix_for_file_name_in_run_29 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_30 = None
        else:
            self.suffix_for_file_name_in_run_30 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_31 = None
        else:
            self.suffix_for_file_name_in_run_31 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_32 = None
        else:
            self.suffix_for_file_name_in_run_32 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_33 = None
        else:
            self.suffix_for_file_name_in_run_33 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_34 = None
        else:
            self.suffix_for_file_name_in_run_34 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_35 = None
        else:
            self.suffix_for_file_name_in_run_35 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_36 = None
        else:
            self.suffix_for_file_name_in_run_36 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_37 = None
        else:
            self.suffix_for_file_name_in_run_37 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_38 = None
        else:
            self.suffix_for_file_name_in_run_38 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_39 = None
        else:
            self.suffix_for_file_name_in_run_39 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_40 = None
        else:
            self.suffix_for_file_name_in_run_40 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_41 = None
        else:
            self.suffix_for_file_name_in_run_41 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_42 = None
        else:
            self.suffix_for_file_name_in_run_42 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_43 = None
        else:
            self.suffix_for_file_name_in_run_43 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_44 = None
        else:
            self.suffix_for_file_name_in_run_44 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_45 = None
        else:
            self.suffix_for_file_name_in_run_45 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_46 = None
        else:
            self.suffix_for_file_name_in_run_46 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_47 = None
        else:
            self.suffix_for_file_name_in_run_47 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_48 = None
        else:
            self.suffix_for_file_name_in_run_48 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_49 = None
        else:
            self.suffix_for_file_name_in_run_49 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_50 = None
        else:
            self.suffix_for_file_name_in_run_50 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_51 = None
        else:
            self.suffix_for_file_name_in_run_51 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_52 = None
        else:
            self.suffix_for_file_name_in_run_52 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_53 = None
        else:
            self.suffix_for_file_name_in_run_53 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_54 = None
        else:
            self.suffix_for_file_name_in_run_54 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_55 = None
        else:
            self.suffix_for_file_name_in_run_55 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_56 = None
        else:
            self.suffix_for_file_name_in_run_56 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_57 = None
        else:
            self.suffix_for_file_name_in_run_57 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_58 = None
        else:
            self.suffix_for_file_name_in_run_58 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_59 = None
        else:
            self.suffix_for_file_name_in_run_59 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_60 = None
        else:
            self.suffix_for_file_name_in_run_60 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_61 = None
        else:
            self.suffix_for_file_name_in_run_61 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_62 = None
        else:
            self.suffix_for_file_name_in_run_62 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_63 = None
        else:
            self.suffix_for_file_name_in_run_63 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_64 = None
        else:
            self.suffix_for_file_name_in_run_64 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_65 = None
        else:
            self.suffix_for_file_name_in_run_65 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_66 = None
        else:
            self.suffix_for_file_name_in_run_66 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_67 = None
        else:
            self.suffix_for_file_name_in_run_67 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_68 = None
        else:
            self.suffix_for_file_name_in_run_68 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_69 = None
        else:
            self.suffix_for_file_name_in_run_69 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_70 = None
        else:
            self.suffix_for_file_name_in_run_70 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_71 = None
        else:
            self.suffix_for_file_name_in_run_71 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_72 = None
        else:
            self.suffix_for_file_name_in_run_72 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_73 = None
        else:
            self.suffix_for_file_name_in_run_73 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_74 = None
        else:
            self.suffix_for_file_name_in_run_74 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_75 = None
        else:
            self.suffix_for_file_name_in_run_75 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_76 = None
        else:
            self.suffix_for_file_name_in_run_76 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_77 = None
        else:
            self.suffix_for_file_name_in_run_77 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_78 = None
        else:
            self.suffix_for_file_name_in_run_78 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_79 = None
        else:
            self.suffix_for_file_name_in_run_79 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_80 = None
        else:
            self.suffix_for_file_name_in_run_80 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_81 = None
        else:
            self.suffix_for_file_name_in_run_81 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_82 = None
        else:
            self.suffix_for_file_name_in_run_82 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_83 = None
        else:
            self.suffix_for_file_name_in_run_83 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_84 = None
        else:
            self.suffix_for_file_name_in_run_84 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_85 = None
        else:
            self.suffix_for_file_name_in_run_85 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_86 = None
        else:
            self.suffix_for_file_name_in_run_86 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_87 = None
        else:
            self.suffix_for_file_name_in_run_87 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_88 = None
        else:
            self.suffix_for_file_name_in_run_88 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_89 = None
        else:
            self.suffix_for_file_name_in_run_89 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_90 = None
        else:
            self.suffix_for_file_name_in_run_90 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_91 = None
        else:
            self.suffix_for_file_name_in_run_91 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_92 = None
        else:
            self.suffix_for_file_name_in_run_92 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_93 = None
        else:
            self.suffix_for_file_name_in_run_93 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_94 = None
        else:
            self.suffix_for_file_name_in_run_94 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_95 = None
        else:
            self.suffix_for_file_name_in_run_95 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_96 = None
        else:
            self.suffix_for_file_name_in_run_96 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_97 = None
        else:
            self.suffix_for_file_name_in_run_97 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_98 = None
        else:
            self.suffix_for_file_name_in_run_98 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_99 = None
        else:
            self.suffix_for_file_name_in_run_99 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.suffix_for_file_name_in_run_100 = None
        else:
            self.suffix_for_file_name_in_run_100 = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def name(self):
        """Get name

        Returns:
            str: the value of `name` or None if not set
        """
        return self._data["Name"]

    @name.setter
    def name(self, value=None):
        """  Corresponds to IDD Field `Name`

        Args:
            value (str): value for IDD Field `Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')
        self._data["Name"] = value

    @property
    def suffix_for_file_name_in_run_1(self):
        """Get suffix_for_file_name_in_run_1

        Returns:
            str: the value of `suffix_for_file_name_in_run_1` or None if not set
        """
        return self._data["Suffix for File Name in Run 1"]

    @suffix_for_file_name_in_run_1.setter
    def suffix_for_file_name_in_run_1(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 1`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_1`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_1`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_1`')
        self._data["Suffix for File Name in Run 1"] = value

    @property
    def suffix_for_file_name_in_run_2(self):
        """Get suffix_for_file_name_in_run_2

        Returns:
            str: the value of `suffix_for_file_name_in_run_2` or None if not set
        """
        return self._data["Suffix for File Name in Run 2"]

    @suffix_for_file_name_in_run_2.setter
    def suffix_for_file_name_in_run_2(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 2`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_2`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_2`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_2`')
        self._data["Suffix for File Name in Run 2"] = value

    @property
    def suffix_for_file_name_in_run_3(self):
        """Get suffix_for_file_name_in_run_3

        Returns:
            str: the value of `suffix_for_file_name_in_run_3` or None if not set
        """
        return self._data["Suffix for File Name in Run 3"]

    @suffix_for_file_name_in_run_3.setter
    def suffix_for_file_name_in_run_3(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 3`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_3`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_3`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_3`')
        self._data["Suffix for File Name in Run 3"] = value

    @property
    def suffix_for_file_name_in_run_4(self):
        """Get suffix_for_file_name_in_run_4

        Returns:
            str: the value of `suffix_for_file_name_in_run_4` or None if not set
        """
        return self._data["Suffix for File Name in Run 4"]

    @suffix_for_file_name_in_run_4.setter
    def suffix_for_file_name_in_run_4(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 4`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_4`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_4`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_4`')
        self._data["Suffix for File Name in Run 4"] = value

    @property
    def suffix_for_file_name_in_run_5(self):
        """Get suffix_for_file_name_in_run_5

        Returns:
            str: the value of `suffix_for_file_name_in_run_5` or None if not set
        """
        return self._data["Suffix for File Name in Run 5"]

    @suffix_for_file_name_in_run_5.setter
    def suffix_for_file_name_in_run_5(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 5`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_5`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_5`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_5`')
        self._data["Suffix for File Name in Run 5"] = value

    @property
    def suffix_for_file_name_in_run_6(self):
        """Get suffix_for_file_name_in_run_6

        Returns:
            str: the value of `suffix_for_file_name_in_run_6` or None if not set
        """
        return self._data["Suffix for File Name in Run 6"]

    @suffix_for_file_name_in_run_6.setter
    def suffix_for_file_name_in_run_6(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 6`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_6`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_6`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_6`')
        self._data["Suffix for File Name in Run 6"] = value

    @property
    def suffix_for_file_name_in_run_7(self):
        """Get suffix_for_file_name_in_run_7

        Returns:
            str: the value of `suffix_for_file_name_in_run_7` or None if not set
        """
        return self._data["Suffix for File Name in Run 7"]

    @suffix_for_file_name_in_run_7.setter
    def suffix_for_file_name_in_run_7(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 7`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_7`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_7`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_7`')
        self._data["Suffix for File Name in Run 7"] = value

    @property
    def suffix_for_file_name_in_run_8(self):
        """Get suffix_for_file_name_in_run_8

        Returns:
            str: the value of `suffix_for_file_name_in_run_8` or None if not set
        """
        return self._data["Suffix for File Name in Run 8"]

    @suffix_for_file_name_in_run_8.setter
    def suffix_for_file_name_in_run_8(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 8`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_8`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_8`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_8`')
        self._data["Suffix for File Name in Run 8"] = value

    @property
    def suffix_for_file_name_in_run_9(self):
        """Get suffix_for_file_name_in_run_9

        Returns:
            str: the value of `suffix_for_file_name_in_run_9` or None if not set
        """
        return self._data["Suffix for File Name in Run 9"]

    @suffix_for_file_name_in_run_9.setter
    def suffix_for_file_name_in_run_9(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 9`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_9`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_9`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_9`')
        self._data["Suffix for File Name in Run 9"] = value

    @property
    def suffix_for_file_name_in_run_10(self):
        """Get suffix_for_file_name_in_run_10

        Returns:
            str: the value of `suffix_for_file_name_in_run_10` or None if not set
        """
        return self._data["Suffix for File Name in Run 10"]

    @suffix_for_file_name_in_run_10.setter
    def suffix_for_file_name_in_run_10(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 10`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_10`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_10`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_10`')
        self._data["Suffix for File Name in Run 10"] = value

    @property
    def suffix_for_file_name_in_run_11(self):
        """Get suffix_for_file_name_in_run_11

        Returns:
            str: the value of `suffix_for_file_name_in_run_11` or None if not set
        """
        return self._data["Suffix for File Name in Run 11"]

    @suffix_for_file_name_in_run_11.setter
    def suffix_for_file_name_in_run_11(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 11`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_11`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_11`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_11`')
        self._data["Suffix for File Name in Run 11"] = value

    @property
    def suffix_for_file_name_in_run_12(self):
        """Get suffix_for_file_name_in_run_12

        Returns:
            str: the value of `suffix_for_file_name_in_run_12` or None if not set
        """
        return self._data["Suffix for File Name in Run 12"]

    @suffix_for_file_name_in_run_12.setter
    def suffix_for_file_name_in_run_12(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 12`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_12`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_12`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_12`')
        self._data["Suffix for File Name in Run 12"] = value

    @property
    def suffix_for_file_name_in_run_13(self):
        """Get suffix_for_file_name_in_run_13

        Returns:
            str: the value of `suffix_for_file_name_in_run_13` or None if not set
        """
        return self._data["Suffix for File Name in Run 13"]

    @suffix_for_file_name_in_run_13.setter
    def suffix_for_file_name_in_run_13(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 13`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_13`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_13`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_13`')
        self._data["Suffix for File Name in Run 13"] = value

    @property
    def suffix_for_file_name_in_run_14(self):
        """Get suffix_for_file_name_in_run_14

        Returns:
            str: the value of `suffix_for_file_name_in_run_14` or None if not set
        """
        return self._data["Suffix for File Name in Run 14"]

    @suffix_for_file_name_in_run_14.setter
    def suffix_for_file_name_in_run_14(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 14`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_14`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_14`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_14`')
        self._data["Suffix for File Name in Run 14"] = value

    @property
    def suffix_for_file_name_in_run_15(self):
        """Get suffix_for_file_name_in_run_15

        Returns:
            str: the value of `suffix_for_file_name_in_run_15` or None if not set
        """
        return self._data["Suffix for File Name in Run 15"]

    @suffix_for_file_name_in_run_15.setter
    def suffix_for_file_name_in_run_15(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 15`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_15`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_15`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_15`')
        self._data["Suffix for File Name in Run 15"] = value

    @property
    def suffix_for_file_name_in_run_16(self):
        """Get suffix_for_file_name_in_run_16

        Returns:
            str: the value of `suffix_for_file_name_in_run_16` or None if not set
        """
        return self._data["Suffix for File Name in Run 16"]

    @suffix_for_file_name_in_run_16.setter
    def suffix_for_file_name_in_run_16(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 16`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_16`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_16`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_16`')
        self._data["Suffix for File Name in Run 16"] = value

    @property
    def suffix_for_file_name_in_run_17(self):
        """Get suffix_for_file_name_in_run_17

        Returns:
            str: the value of `suffix_for_file_name_in_run_17` or None if not set
        """
        return self._data["Suffix for File Name in Run 17"]

    @suffix_for_file_name_in_run_17.setter
    def suffix_for_file_name_in_run_17(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 17`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_17`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_17`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_17`')
        self._data["Suffix for File Name in Run 17"] = value

    @property
    def suffix_for_file_name_in_run_18(self):
        """Get suffix_for_file_name_in_run_18

        Returns:
            str: the value of `suffix_for_file_name_in_run_18` or None if not set
        """
        return self._data["Suffix for File Name in Run 18"]

    @suffix_for_file_name_in_run_18.setter
    def suffix_for_file_name_in_run_18(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 18`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_18`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_18`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_18`')
        self._data["Suffix for File Name in Run 18"] = value

    @property
    def suffix_for_file_name_in_run_19(self):
        """Get suffix_for_file_name_in_run_19

        Returns:
            str: the value of `suffix_for_file_name_in_run_19` or None if not set
        """
        return self._data["Suffix for File Name in Run 19"]

    @suffix_for_file_name_in_run_19.setter
    def suffix_for_file_name_in_run_19(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 19`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_19`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_19`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_19`')
        self._data["Suffix for File Name in Run 19"] = value

    @property
    def suffix_for_file_name_in_run_20(self):
        """Get suffix_for_file_name_in_run_20

        Returns:
            str: the value of `suffix_for_file_name_in_run_20` or None if not set
        """
        return self._data["Suffix for File Name in Run 20"]

    @suffix_for_file_name_in_run_20.setter
    def suffix_for_file_name_in_run_20(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 20`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_20`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_20`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_20`')
        self._data["Suffix for File Name in Run 20"] = value

    @property
    def suffix_for_file_name_in_run_21(self):
        """Get suffix_for_file_name_in_run_21

        Returns:
            str: the value of `suffix_for_file_name_in_run_21` or None if not set
        """
        return self._data["Suffix for File Name in Run 21"]

    @suffix_for_file_name_in_run_21.setter
    def suffix_for_file_name_in_run_21(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 21`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_21`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_21`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_21`')
        self._data["Suffix for File Name in Run 21"] = value

    @property
    def suffix_for_file_name_in_run_22(self):
        """Get suffix_for_file_name_in_run_22

        Returns:
            str: the value of `suffix_for_file_name_in_run_22` or None if not set
        """
        return self._data["Suffix for File Name in Run 22"]

    @suffix_for_file_name_in_run_22.setter
    def suffix_for_file_name_in_run_22(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 22`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_22`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_22`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_22`')
        self._data["Suffix for File Name in Run 22"] = value

    @property
    def suffix_for_file_name_in_run_23(self):
        """Get suffix_for_file_name_in_run_23

        Returns:
            str: the value of `suffix_for_file_name_in_run_23` or None if not set
        """
        return self._data["Suffix for File Name in Run 23"]

    @suffix_for_file_name_in_run_23.setter
    def suffix_for_file_name_in_run_23(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 23`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_23`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_23`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_23`')
        self._data["Suffix for File Name in Run 23"] = value

    @property
    def suffix_for_file_name_in_run_24(self):
        """Get suffix_for_file_name_in_run_24

        Returns:
            str: the value of `suffix_for_file_name_in_run_24` or None if not set
        """
        return self._data["Suffix for File Name in Run 24"]

    @suffix_for_file_name_in_run_24.setter
    def suffix_for_file_name_in_run_24(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 24`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_24`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_24`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_24`')
        self._data["Suffix for File Name in Run 24"] = value

    @property
    def suffix_for_file_name_in_run_25(self):
        """Get suffix_for_file_name_in_run_25

        Returns:
            str: the value of `suffix_for_file_name_in_run_25` or None if not set
        """
        return self._data["Suffix for File Name in Run 25"]

    @suffix_for_file_name_in_run_25.setter
    def suffix_for_file_name_in_run_25(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 25`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_25`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_25`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_25`')
        self._data["Suffix for File Name in Run 25"] = value

    @property
    def suffix_for_file_name_in_run_26(self):
        """Get suffix_for_file_name_in_run_26

        Returns:
            str: the value of `suffix_for_file_name_in_run_26` or None if not set
        """
        return self._data["Suffix for File Name in Run 26"]

    @suffix_for_file_name_in_run_26.setter
    def suffix_for_file_name_in_run_26(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 26`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_26`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_26`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_26`')
        self._data["Suffix for File Name in Run 26"] = value

    @property
    def suffix_for_file_name_in_run_27(self):
        """Get suffix_for_file_name_in_run_27

        Returns:
            str: the value of `suffix_for_file_name_in_run_27` or None if not set
        """
        return self._data["Suffix for File Name in Run 27"]

    @suffix_for_file_name_in_run_27.setter
    def suffix_for_file_name_in_run_27(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 27`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_27`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_27`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_27`')
        self._data["Suffix for File Name in Run 27"] = value

    @property
    def suffix_for_file_name_in_run_28(self):
        """Get suffix_for_file_name_in_run_28

        Returns:
            str: the value of `suffix_for_file_name_in_run_28` or None if not set
        """
        return self._data["Suffix for File Name in Run 28"]

    @suffix_for_file_name_in_run_28.setter
    def suffix_for_file_name_in_run_28(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 28`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_28`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_28`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_28`')
        self._data["Suffix for File Name in Run 28"] = value

    @property
    def suffix_for_file_name_in_run_29(self):
        """Get suffix_for_file_name_in_run_29

        Returns:
            str: the value of `suffix_for_file_name_in_run_29` or None if not set
        """
        return self._data["Suffix for File Name in Run 29"]

    @suffix_for_file_name_in_run_29.setter
    def suffix_for_file_name_in_run_29(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 29`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_29`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_29`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_29`')
        self._data["Suffix for File Name in Run 29"] = value

    @property
    def suffix_for_file_name_in_run_30(self):
        """Get suffix_for_file_name_in_run_30

        Returns:
            str: the value of `suffix_for_file_name_in_run_30` or None if not set
        """
        return self._data["Suffix for File Name in Run 30"]

    @suffix_for_file_name_in_run_30.setter
    def suffix_for_file_name_in_run_30(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 30`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_30`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_30`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_30`')
        self._data["Suffix for File Name in Run 30"] = value

    @property
    def suffix_for_file_name_in_run_31(self):
        """Get suffix_for_file_name_in_run_31

        Returns:
            str: the value of `suffix_for_file_name_in_run_31` or None if not set
        """
        return self._data["Suffix for File Name in Run 31"]

    @suffix_for_file_name_in_run_31.setter
    def suffix_for_file_name_in_run_31(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 31`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_31`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_31`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_31`')
        self._data["Suffix for File Name in Run 31"] = value

    @property
    def suffix_for_file_name_in_run_32(self):
        """Get suffix_for_file_name_in_run_32

        Returns:
            str: the value of `suffix_for_file_name_in_run_32` or None if not set
        """
        return self._data["Suffix for File Name in Run 32"]

    @suffix_for_file_name_in_run_32.setter
    def suffix_for_file_name_in_run_32(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 32`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_32`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_32`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_32`')
        self._data["Suffix for File Name in Run 32"] = value

    @property
    def suffix_for_file_name_in_run_33(self):
        """Get suffix_for_file_name_in_run_33

        Returns:
            str: the value of `suffix_for_file_name_in_run_33` or None if not set
        """
        return self._data["Suffix for File Name in Run 33"]

    @suffix_for_file_name_in_run_33.setter
    def suffix_for_file_name_in_run_33(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 33`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_33`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_33`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_33`')
        self._data["Suffix for File Name in Run 33"] = value

    @property
    def suffix_for_file_name_in_run_34(self):
        """Get suffix_for_file_name_in_run_34

        Returns:
            str: the value of `suffix_for_file_name_in_run_34` or None if not set
        """
        return self._data["Suffix for File Name in Run 34"]

    @suffix_for_file_name_in_run_34.setter
    def suffix_for_file_name_in_run_34(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 34`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_34`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_34`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_34`')
        self._data["Suffix for File Name in Run 34"] = value

    @property
    def suffix_for_file_name_in_run_35(self):
        """Get suffix_for_file_name_in_run_35

        Returns:
            str: the value of `suffix_for_file_name_in_run_35` or None if not set
        """
        return self._data["Suffix for File Name in Run 35"]

    @suffix_for_file_name_in_run_35.setter
    def suffix_for_file_name_in_run_35(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 35`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_35`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_35`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_35`')
        self._data["Suffix for File Name in Run 35"] = value

    @property
    def suffix_for_file_name_in_run_36(self):
        """Get suffix_for_file_name_in_run_36

        Returns:
            str: the value of `suffix_for_file_name_in_run_36` or None if not set
        """
        return self._data["Suffix for File Name in Run 36"]

    @suffix_for_file_name_in_run_36.setter
    def suffix_for_file_name_in_run_36(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 36`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_36`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_36`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_36`')
        self._data["Suffix for File Name in Run 36"] = value

    @property
    def suffix_for_file_name_in_run_37(self):
        """Get suffix_for_file_name_in_run_37

        Returns:
            str: the value of `suffix_for_file_name_in_run_37` or None if not set
        """
        return self._data["Suffix for File Name in Run 37"]

    @suffix_for_file_name_in_run_37.setter
    def suffix_for_file_name_in_run_37(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 37`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_37`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_37`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_37`')
        self._data["Suffix for File Name in Run 37"] = value

    @property
    def suffix_for_file_name_in_run_38(self):
        """Get suffix_for_file_name_in_run_38

        Returns:
            str: the value of `suffix_for_file_name_in_run_38` or None if not set
        """
        return self._data["Suffix for File Name in Run 38"]

    @suffix_for_file_name_in_run_38.setter
    def suffix_for_file_name_in_run_38(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 38`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_38`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_38`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_38`')
        self._data["Suffix for File Name in Run 38"] = value

    @property
    def suffix_for_file_name_in_run_39(self):
        """Get suffix_for_file_name_in_run_39

        Returns:
            str: the value of `suffix_for_file_name_in_run_39` or None if not set
        """
        return self._data["Suffix for File Name in Run 39"]

    @suffix_for_file_name_in_run_39.setter
    def suffix_for_file_name_in_run_39(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 39`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_39`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_39`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_39`')
        self._data["Suffix for File Name in Run 39"] = value

    @property
    def suffix_for_file_name_in_run_40(self):
        """Get suffix_for_file_name_in_run_40

        Returns:
            str: the value of `suffix_for_file_name_in_run_40` or None if not set
        """
        return self._data["Suffix for File Name in Run 40"]

    @suffix_for_file_name_in_run_40.setter
    def suffix_for_file_name_in_run_40(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 40`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_40`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_40`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_40`')
        self._data["Suffix for File Name in Run 40"] = value

    @property
    def suffix_for_file_name_in_run_41(self):
        """Get suffix_for_file_name_in_run_41

        Returns:
            str: the value of `suffix_for_file_name_in_run_41` or None if not set
        """
        return self._data["Suffix for File Name in Run 41"]

    @suffix_for_file_name_in_run_41.setter
    def suffix_for_file_name_in_run_41(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 41`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_41`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_41`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_41`')
        self._data["Suffix for File Name in Run 41"] = value

    @property
    def suffix_for_file_name_in_run_42(self):
        """Get suffix_for_file_name_in_run_42

        Returns:
            str: the value of `suffix_for_file_name_in_run_42` or None if not set
        """
        return self._data["Suffix for File Name in Run 42"]

    @suffix_for_file_name_in_run_42.setter
    def suffix_for_file_name_in_run_42(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 42`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_42`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_42`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_42`')
        self._data["Suffix for File Name in Run 42"] = value

    @property
    def suffix_for_file_name_in_run_43(self):
        """Get suffix_for_file_name_in_run_43

        Returns:
            str: the value of `suffix_for_file_name_in_run_43` or None if not set
        """
        return self._data["Suffix for File Name in Run 43"]

    @suffix_for_file_name_in_run_43.setter
    def suffix_for_file_name_in_run_43(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 43`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_43`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_43`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_43`')
        self._data["Suffix for File Name in Run 43"] = value

    @property
    def suffix_for_file_name_in_run_44(self):
        """Get suffix_for_file_name_in_run_44

        Returns:
            str: the value of `suffix_for_file_name_in_run_44` or None if not set
        """
        return self._data["Suffix for File Name in Run 44"]

    @suffix_for_file_name_in_run_44.setter
    def suffix_for_file_name_in_run_44(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 44`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_44`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_44`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_44`')
        self._data["Suffix for File Name in Run 44"] = value

    @property
    def suffix_for_file_name_in_run_45(self):
        """Get suffix_for_file_name_in_run_45

        Returns:
            str: the value of `suffix_for_file_name_in_run_45` or None if not set
        """
        return self._data["Suffix for File Name in Run 45"]

    @suffix_for_file_name_in_run_45.setter
    def suffix_for_file_name_in_run_45(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 45`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_45`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_45`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_45`')
        self._data["Suffix for File Name in Run 45"] = value

    @property
    def suffix_for_file_name_in_run_46(self):
        """Get suffix_for_file_name_in_run_46

        Returns:
            str: the value of `suffix_for_file_name_in_run_46` or None if not set
        """
        return self._data["Suffix for File Name in Run 46"]

    @suffix_for_file_name_in_run_46.setter
    def suffix_for_file_name_in_run_46(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 46`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_46`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_46`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_46`')
        self._data["Suffix for File Name in Run 46"] = value

    @property
    def suffix_for_file_name_in_run_47(self):
        """Get suffix_for_file_name_in_run_47

        Returns:
            str: the value of `suffix_for_file_name_in_run_47` or None if not set
        """
        return self._data["Suffix for File Name in Run 47"]

    @suffix_for_file_name_in_run_47.setter
    def suffix_for_file_name_in_run_47(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 47`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_47`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_47`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_47`')
        self._data["Suffix for File Name in Run 47"] = value

    @property
    def suffix_for_file_name_in_run_48(self):
        """Get suffix_for_file_name_in_run_48

        Returns:
            str: the value of `suffix_for_file_name_in_run_48` or None if not set
        """
        return self._data["Suffix for File Name in Run 48"]

    @suffix_for_file_name_in_run_48.setter
    def suffix_for_file_name_in_run_48(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 48`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_48`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_48`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_48`')
        self._data["Suffix for File Name in Run 48"] = value

    @property
    def suffix_for_file_name_in_run_49(self):
        """Get suffix_for_file_name_in_run_49

        Returns:
            str: the value of `suffix_for_file_name_in_run_49` or None if not set
        """
        return self._data["Suffix for File Name in Run 49"]

    @suffix_for_file_name_in_run_49.setter
    def suffix_for_file_name_in_run_49(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 49`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_49`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_49`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_49`')
        self._data["Suffix for File Name in Run 49"] = value

    @property
    def suffix_for_file_name_in_run_50(self):
        """Get suffix_for_file_name_in_run_50

        Returns:
            str: the value of `suffix_for_file_name_in_run_50` or None if not set
        """
        return self._data["Suffix for File Name in Run 50"]

    @suffix_for_file_name_in_run_50.setter
    def suffix_for_file_name_in_run_50(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 50`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_50`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_50`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_50`')
        self._data["Suffix for File Name in Run 50"] = value

    @property
    def suffix_for_file_name_in_run_51(self):
        """Get suffix_for_file_name_in_run_51

        Returns:
            str: the value of `suffix_for_file_name_in_run_51` or None if not set
        """
        return self._data["Suffix for File Name in Run 51"]

    @suffix_for_file_name_in_run_51.setter
    def suffix_for_file_name_in_run_51(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 51`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_51`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_51`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_51`')
        self._data["Suffix for File Name in Run 51"] = value

    @property
    def suffix_for_file_name_in_run_52(self):
        """Get suffix_for_file_name_in_run_52

        Returns:
            str: the value of `suffix_for_file_name_in_run_52` or None if not set
        """
        return self._data["Suffix for File Name in Run 52"]

    @suffix_for_file_name_in_run_52.setter
    def suffix_for_file_name_in_run_52(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 52`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_52`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_52`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_52`')
        self._data["Suffix for File Name in Run 52"] = value

    @property
    def suffix_for_file_name_in_run_53(self):
        """Get suffix_for_file_name_in_run_53

        Returns:
            str: the value of `suffix_for_file_name_in_run_53` or None if not set
        """
        return self._data["Suffix for File Name in Run 53"]

    @suffix_for_file_name_in_run_53.setter
    def suffix_for_file_name_in_run_53(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 53`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_53`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_53`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_53`')
        self._data["Suffix for File Name in Run 53"] = value

    @property
    def suffix_for_file_name_in_run_54(self):
        """Get suffix_for_file_name_in_run_54

        Returns:
            str: the value of `suffix_for_file_name_in_run_54` or None if not set
        """
        return self._data["Suffix for File Name in Run 54"]

    @suffix_for_file_name_in_run_54.setter
    def suffix_for_file_name_in_run_54(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 54`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_54`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_54`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_54`')
        self._data["Suffix for File Name in Run 54"] = value

    @property
    def suffix_for_file_name_in_run_55(self):
        """Get suffix_for_file_name_in_run_55

        Returns:
            str: the value of `suffix_for_file_name_in_run_55` or None if not set
        """
        return self._data["Suffix for File Name in Run 55"]

    @suffix_for_file_name_in_run_55.setter
    def suffix_for_file_name_in_run_55(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 55`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_55`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_55`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_55`')
        self._data["Suffix for File Name in Run 55"] = value

    @property
    def suffix_for_file_name_in_run_56(self):
        """Get suffix_for_file_name_in_run_56

        Returns:
            str: the value of `suffix_for_file_name_in_run_56` or None if not set
        """
        return self._data["Suffix for File Name in Run 56"]

    @suffix_for_file_name_in_run_56.setter
    def suffix_for_file_name_in_run_56(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 56`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_56`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_56`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_56`')
        self._data["Suffix for File Name in Run 56"] = value

    @property
    def suffix_for_file_name_in_run_57(self):
        """Get suffix_for_file_name_in_run_57

        Returns:
            str: the value of `suffix_for_file_name_in_run_57` or None if not set
        """
        return self._data["Suffix for File Name in Run 57"]

    @suffix_for_file_name_in_run_57.setter
    def suffix_for_file_name_in_run_57(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 57`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_57`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_57`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_57`')
        self._data["Suffix for File Name in Run 57"] = value

    @property
    def suffix_for_file_name_in_run_58(self):
        """Get suffix_for_file_name_in_run_58

        Returns:
            str: the value of `suffix_for_file_name_in_run_58` or None if not set
        """
        return self._data["Suffix for File Name in Run 58"]

    @suffix_for_file_name_in_run_58.setter
    def suffix_for_file_name_in_run_58(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 58`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_58`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_58`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_58`')
        self._data["Suffix for File Name in Run 58"] = value

    @property
    def suffix_for_file_name_in_run_59(self):
        """Get suffix_for_file_name_in_run_59

        Returns:
            str: the value of `suffix_for_file_name_in_run_59` or None if not set
        """
        return self._data["Suffix for File Name in Run 59"]

    @suffix_for_file_name_in_run_59.setter
    def suffix_for_file_name_in_run_59(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 59`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_59`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_59`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_59`')
        self._data["Suffix for File Name in Run 59"] = value

    @property
    def suffix_for_file_name_in_run_60(self):
        """Get suffix_for_file_name_in_run_60

        Returns:
            str: the value of `suffix_for_file_name_in_run_60` or None if not set
        """
        return self._data["Suffix for File Name in Run 60"]

    @suffix_for_file_name_in_run_60.setter
    def suffix_for_file_name_in_run_60(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 60`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_60`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_60`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_60`')
        self._data["Suffix for File Name in Run 60"] = value

    @property
    def suffix_for_file_name_in_run_61(self):
        """Get suffix_for_file_name_in_run_61

        Returns:
            str: the value of `suffix_for_file_name_in_run_61` or None if not set
        """
        return self._data["Suffix for File Name in Run 61"]

    @suffix_for_file_name_in_run_61.setter
    def suffix_for_file_name_in_run_61(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 61`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_61`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_61`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_61`')
        self._data["Suffix for File Name in Run 61"] = value

    @property
    def suffix_for_file_name_in_run_62(self):
        """Get suffix_for_file_name_in_run_62

        Returns:
            str: the value of `suffix_for_file_name_in_run_62` or None if not set
        """
        return self._data["Suffix for File Name in Run 62"]

    @suffix_for_file_name_in_run_62.setter
    def suffix_for_file_name_in_run_62(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 62`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_62`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_62`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_62`')
        self._data["Suffix for File Name in Run 62"] = value

    @property
    def suffix_for_file_name_in_run_63(self):
        """Get suffix_for_file_name_in_run_63

        Returns:
            str: the value of `suffix_for_file_name_in_run_63` or None if not set
        """
        return self._data["Suffix for File Name in Run 63"]

    @suffix_for_file_name_in_run_63.setter
    def suffix_for_file_name_in_run_63(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 63`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_63`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_63`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_63`')
        self._data["Suffix for File Name in Run 63"] = value

    @property
    def suffix_for_file_name_in_run_64(self):
        """Get suffix_for_file_name_in_run_64

        Returns:
            str: the value of `suffix_for_file_name_in_run_64` or None if not set
        """
        return self._data["Suffix for File Name in Run 64"]

    @suffix_for_file_name_in_run_64.setter
    def suffix_for_file_name_in_run_64(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 64`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_64`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_64`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_64`')
        self._data["Suffix for File Name in Run 64"] = value

    @property
    def suffix_for_file_name_in_run_65(self):
        """Get suffix_for_file_name_in_run_65

        Returns:
            str: the value of `suffix_for_file_name_in_run_65` or None if not set
        """
        return self._data["Suffix for File Name in Run 65"]

    @suffix_for_file_name_in_run_65.setter
    def suffix_for_file_name_in_run_65(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 65`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_65`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_65`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_65`')
        self._data["Suffix for File Name in Run 65"] = value

    @property
    def suffix_for_file_name_in_run_66(self):
        """Get suffix_for_file_name_in_run_66

        Returns:
            str: the value of `suffix_for_file_name_in_run_66` or None if not set
        """
        return self._data["Suffix for File Name in Run 66"]

    @suffix_for_file_name_in_run_66.setter
    def suffix_for_file_name_in_run_66(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 66`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_66`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_66`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_66`')
        self._data["Suffix for File Name in Run 66"] = value

    @property
    def suffix_for_file_name_in_run_67(self):
        """Get suffix_for_file_name_in_run_67

        Returns:
            str: the value of `suffix_for_file_name_in_run_67` or None if not set
        """
        return self._data["Suffix for File Name in Run 67"]

    @suffix_for_file_name_in_run_67.setter
    def suffix_for_file_name_in_run_67(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 67`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_67`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_67`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_67`')
        self._data["Suffix for File Name in Run 67"] = value

    @property
    def suffix_for_file_name_in_run_68(self):
        """Get suffix_for_file_name_in_run_68

        Returns:
            str: the value of `suffix_for_file_name_in_run_68` or None if not set
        """
        return self._data["Suffix for File Name in Run 68"]

    @suffix_for_file_name_in_run_68.setter
    def suffix_for_file_name_in_run_68(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 68`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_68`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_68`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_68`')
        self._data["Suffix for File Name in Run 68"] = value

    @property
    def suffix_for_file_name_in_run_69(self):
        """Get suffix_for_file_name_in_run_69

        Returns:
            str: the value of `suffix_for_file_name_in_run_69` or None if not set
        """
        return self._data["Suffix for File Name in Run 69"]

    @suffix_for_file_name_in_run_69.setter
    def suffix_for_file_name_in_run_69(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 69`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_69`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_69`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_69`')
        self._data["Suffix for File Name in Run 69"] = value

    @property
    def suffix_for_file_name_in_run_70(self):
        """Get suffix_for_file_name_in_run_70

        Returns:
            str: the value of `suffix_for_file_name_in_run_70` or None if not set
        """
        return self._data["Suffix for File Name in Run 70"]

    @suffix_for_file_name_in_run_70.setter
    def suffix_for_file_name_in_run_70(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 70`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_70`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_70`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_70`')
        self._data["Suffix for File Name in Run 70"] = value

    @property
    def suffix_for_file_name_in_run_71(self):
        """Get suffix_for_file_name_in_run_71

        Returns:
            str: the value of `suffix_for_file_name_in_run_71` or None if not set
        """
        return self._data["Suffix for File Name in Run 71"]

    @suffix_for_file_name_in_run_71.setter
    def suffix_for_file_name_in_run_71(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 71`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_71`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_71`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_71`')
        self._data["Suffix for File Name in Run 71"] = value

    @property
    def suffix_for_file_name_in_run_72(self):
        """Get suffix_for_file_name_in_run_72

        Returns:
            str: the value of `suffix_for_file_name_in_run_72` or None if not set
        """
        return self._data["Suffix for File Name in Run 72"]

    @suffix_for_file_name_in_run_72.setter
    def suffix_for_file_name_in_run_72(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 72`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_72`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_72`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_72`')
        self._data["Suffix for File Name in Run 72"] = value

    @property
    def suffix_for_file_name_in_run_73(self):
        """Get suffix_for_file_name_in_run_73

        Returns:
            str: the value of `suffix_for_file_name_in_run_73` or None if not set
        """
        return self._data["Suffix for File Name in Run 73"]

    @suffix_for_file_name_in_run_73.setter
    def suffix_for_file_name_in_run_73(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 73`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_73`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_73`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_73`')
        self._data["Suffix for File Name in Run 73"] = value

    @property
    def suffix_for_file_name_in_run_74(self):
        """Get suffix_for_file_name_in_run_74

        Returns:
            str: the value of `suffix_for_file_name_in_run_74` or None if not set
        """
        return self._data["Suffix for File Name in Run 74"]

    @suffix_for_file_name_in_run_74.setter
    def suffix_for_file_name_in_run_74(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 74`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_74`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_74`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_74`')
        self._data["Suffix for File Name in Run 74"] = value

    @property
    def suffix_for_file_name_in_run_75(self):
        """Get suffix_for_file_name_in_run_75

        Returns:
            str: the value of `suffix_for_file_name_in_run_75` or None if not set
        """
        return self._data["Suffix for File Name in Run 75"]

    @suffix_for_file_name_in_run_75.setter
    def suffix_for_file_name_in_run_75(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 75`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_75`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_75`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_75`')
        self._data["Suffix for File Name in Run 75"] = value

    @property
    def suffix_for_file_name_in_run_76(self):
        """Get suffix_for_file_name_in_run_76

        Returns:
            str: the value of `suffix_for_file_name_in_run_76` or None if not set
        """
        return self._data["Suffix for File Name in Run 76"]

    @suffix_for_file_name_in_run_76.setter
    def suffix_for_file_name_in_run_76(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 76`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_76`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_76`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_76`')
        self._data["Suffix for File Name in Run 76"] = value

    @property
    def suffix_for_file_name_in_run_77(self):
        """Get suffix_for_file_name_in_run_77

        Returns:
            str: the value of `suffix_for_file_name_in_run_77` or None if not set
        """
        return self._data["Suffix for File Name in Run 77"]

    @suffix_for_file_name_in_run_77.setter
    def suffix_for_file_name_in_run_77(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 77`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_77`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_77`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_77`')
        self._data["Suffix for File Name in Run 77"] = value

    @property
    def suffix_for_file_name_in_run_78(self):
        """Get suffix_for_file_name_in_run_78

        Returns:
            str: the value of `suffix_for_file_name_in_run_78` or None if not set
        """
        return self._data["Suffix for File Name in Run 78"]

    @suffix_for_file_name_in_run_78.setter
    def suffix_for_file_name_in_run_78(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 78`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_78`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_78`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_78`')
        self._data["Suffix for File Name in Run 78"] = value

    @property
    def suffix_for_file_name_in_run_79(self):
        """Get suffix_for_file_name_in_run_79

        Returns:
            str: the value of `suffix_for_file_name_in_run_79` or None if not set
        """
        return self._data["Suffix for File Name in Run 79"]

    @suffix_for_file_name_in_run_79.setter
    def suffix_for_file_name_in_run_79(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 79`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_79`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_79`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_79`')
        self._data["Suffix for File Name in Run 79"] = value

    @property
    def suffix_for_file_name_in_run_80(self):
        """Get suffix_for_file_name_in_run_80

        Returns:
            str: the value of `suffix_for_file_name_in_run_80` or None if not set
        """
        return self._data["Suffix for File Name in Run 80"]

    @suffix_for_file_name_in_run_80.setter
    def suffix_for_file_name_in_run_80(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 80`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_80`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_80`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_80`')
        self._data["Suffix for File Name in Run 80"] = value

    @property
    def suffix_for_file_name_in_run_81(self):
        """Get suffix_for_file_name_in_run_81

        Returns:
            str: the value of `suffix_for_file_name_in_run_81` or None if not set
        """
        return self._data["Suffix for File Name in Run 81"]

    @suffix_for_file_name_in_run_81.setter
    def suffix_for_file_name_in_run_81(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 81`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_81`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_81`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_81`')
        self._data["Suffix for File Name in Run 81"] = value

    @property
    def suffix_for_file_name_in_run_82(self):
        """Get suffix_for_file_name_in_run_82

        Returns:
            str: the value of `suffix_for_file_name_in_run_82` or None if not set
        """
        return self._data["Suffix for File Name in Run 82"]

    @suffix_for_file_name_in_run_82.setter
    def suffix_for_file_name_in_run_82(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 82`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_82`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_82`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_82`')
        self._data["Suffix for File Name in Run 82"] = value

    @property
    def suffix_for_file_name_in_run_83(self):
        """Get suffix_for_file_name_in_run_83

        Returns:
            str: the value of `suffix_for_file_name_in_run_83` or None if not set
        """
        return self._data["Suffix for File Name in Run 83"]

    @suffix_for_file_name_in_run_83.setter
    def suffix_for_file_name_in_run_83(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 83`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_83`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_83`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_83`')
        self._data["Suffix for File Name in Run 83"] = value

    @property
    def suffix_for_file_name_in_run_84(self):
        """Get suffix_for_file_name_in_run_84

        Returns:
            str: the value of `suffix_for_file_name_in_run_84` or None if not set
        """
        return self._data["Suffix for File Name in Run 84"]

    @suffix_for_file_name_in_run_84.setter
    def suffix_for_file_name_in_run_84(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 84`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_84`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_84`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_84`')
        self._data["Suffix for File Name in Run 84"] = value

    @property
    def suffix_for_file_name_in_run_85(self):
        """Get suffix_for_file_name_in_run_85

        Returns:
            str: the value of `suffix_for_file_name_in_run_85` or None if not set
        """
        return self._data["Suffix for File Name in Run 85"]

    @suffix_for_file_name_in_run_85.setter
    def suffix_for_file_name_in_run_85(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 85`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_85`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_85`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_85`')
        self._data["Suffix for File Name in Run 85"] = value

    @property
    def suffix_for_file_name_in_run_86(self):
        """Get suffix_for_file_name_in_run_86

        Returns:
            str: the value of `suffix_for_file_name_in_run_86` or None if not set
        """
        return self._data["Suffix for File Name in Run 86"]

    @suffix_for_file_name_in_run_86.setter
    def suffix_for_file_name_in_run_86(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 86`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_86`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_86`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_86`')
        self._data["Suffix for File Name in Run 86"] = value

    @property
    def suffix_for_file_name_in_run_87(self):
        """Get suffix_for_file_name_in_run_87

        Returns:
            str: the value of `suffix_for_file_name_in_run_87` or None if not set
        """
        return self._data["Suffix for File Name in Run 87"]

    @suffix_for_file_name_in_run_87.setter
    def suffix_for_file_name_in_run_87(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 87`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_87`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_87`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_87`')
        self._data["Suffix for File Name in Run 87"] = value

    @property
    def suffix_for_file_name_in_run_88(self):
        """Get suffix_for_file_name_in_run_88

        Returns:
            str: the value of `suffix_for_file_name_in_run_88` or None if not set
        """
        return self._data["Suffix for File Name in Run 88"]

    @suffix_for_file_name_in_run_88.setter
    def suffix_for_file_name_in_run_88(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 88`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_88`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_88`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_88`')
        self._data["Suffix for File Name in Run 88"] = value

    @property
    def suffix_for_file_name_in_run_89(self):
        """Get suffix_for_file_name_in_run_89

        Returns:
            str: the value of `suffix_for_file_name_in_run_89` or None if not set
        """
        return self._data["Suffix for File Name in Run 89"]

    @suffix_for_file_name_in_run_89.setter
    def suffix_for_file_name_in_run_89(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 89`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_89`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_89`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_89`')
        self._data["Suffix for File Name in Run 89"] = value

    @property
    def suffix_for_file_name_in_run_90(self):
        """Get suffix_for_file_name_in_run_90

        Returns:
            str: the value of `suffix_for_file_name_in_run_90` or None if not set
        """
        return self._data["Suffix for File Name in Run 90"]

    @suffix_for_file_name_in_run_90.setter
    def suffix_for_file_name_in_run_90(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 90`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_90`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_90`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_90`')
        self._data["Suffix for File Name in Run 90"] = value

    @property
    def suffix_for_file_name_in_run_91(self):
        """Get suffix_for_file_name_in_run_91

        Returns:
            str: the value of `suffix_for_file_name_in_run_91` or None if not set
        """
        return self._data["Suffix for File Name in Run 91"]

    @suffix_for_file_name_in_run_91.setter
    def suffix_for_file_name_in_run_91(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 91`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_91`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_91`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_91`')
        self._data["Suffix for File Name in Run 91"] = value

    @property
    def suffix_for_file_name_in_run_92(self):
        """Get suffix_for_file_name_in_run_92

        Returns:
            str: the value of `suffix_for_file_name_in_run_92` or None if not set
        """
        return self._data["Suffix for File Name in Run 92"]

    @suffix_for_file_name_in_run_92.setter
    def suffix_for_file_name_in_run_92(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 92`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_92`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_92`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_92`')
        self._data["Suffix for File Name in Run 92"] = value

    @property
    def suffix_for_file_name_in_run_93(self):
        """Get suffix_for_file_name_in_run_93

        Returns:
            str: the value of `suffix_for_file_name_in_run_93` or None if not set
        """
        return self._data["Suffix for File Name in Run 93"]

    @suffix_for_file_name_in_run_93.setter
    def suffix_for_file_name_in_run_93(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 93`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_93`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_93`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_93`')
        self._data["Suffix for File Name in Run 93"] = value

    @property
    def suffix_for_file_name_in_run_94(self):
        """Get suffix_for_file_name_in_run_94

        Returns:
            str: the value of `suffix_for_file_name_in_run_94` or None if not set
        """
        return self._data["Suffix for File Name in Run 94"]

    @suffix_for_file_name_in_run_94.setter
    def suffix_for_file_name_in_run_94(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 94`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_94`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_94`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_94`')
        self._data["Suffix for File Name in Run 94"] = value

    @property
    def suffix_for_file_name_in_run_95(self):
        """Get suffix_for_file_name_in_run_95

        Returns:
            str: the value of `suffix_for_file_name_in_run_95` or None if not set
        """
        return self._data["Suffix for File Name in Run 95"]

    @suffix_for_file_name_in_run_95.setter
    def suffix_for_file_name_in_run_95(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 95`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_95`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_95`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_95`')
        self._data["Suffix for File Name in Run 95"] = value

    @property
    def suffix_for_file_name_in_run_96(self):
        """Get suffix_for_file_name_in_run_96

        Returns:
            str: the value of `suffix_for_file_name_in_run_96` or None if not set
        """
        return self._data["Suffix for File Name in Run 96"]

    @suffix_for_file_name_in_run_96.setter
    def suffix_for_file_name_in_run_96(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 96`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_96`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_96`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_96`')
        self._data["Suffix for File Name in Run 96"] = value

    @property
    def suffix_for_file_name_in_run_97(self):
        """Get suffix_for_file_name_in_run_97

        Returns:
            str: the value of `suffix_for_file_name_in_run_97` or None if not set
        """
        return self._data["Suffix for File Name in Run 97"]

    @suffix_for_file_name_in_run_97.setter
    def suffix_for_file_name_in_run_97(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 97`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_97`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_97`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_97`')
        self._data["Suffix for File Name in Run 97"] = value

    @property
    def suffix_for_file_name_in_run_98(self):
        """Get suffix_for_file_name_in_run_98

        Returns:
            str: the value of `suffix_for_file_name_in_run_98` or None if not set
        """
        return self._data["Suffix for File Name in Run 98"]

    @suffix_for_file_name_in_run_98.setter
    def suffix_for_file_name_in_run_98(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 98`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_98`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_98`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_98`')
        self._data["Suffix for File Name in Run 98"] = value

    @property
    def suffix_for_file_name_in_run_99(self):
        """Get suffix_for_file_name_in_run_99

        Returns:
            str: the value of `suffix_for_file_name_in_run_99` or None if not set
        """
        return self._data["Suffix for File Name in Run 99"]

    @suffix_for_file_name_in_run_99.setter
    def suffix_for_file_name_in_run_99(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 99`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_99`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_99`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_99`')
        self._data["Suffix for File Name in Run 99"] = value

    @property
    def suffix_for_file_name_in_run_100(self):
        """Get suffix_for_file_name_in_run_100

        Returns:
            str: the value of `suffix_for_file_name_in_run_100` or None if not set
        """
        return self._data["Suffix for File Name in Run 100"]

    @suffix_for_file_name_in_run_100.setter
    def suffix_for_file_name_in_run_100(self, value=None):
        """  Corresponds to IDD Field `Suffix for File Name in Run 100`

        Args:
            value (str): value for IDD Field `Suffix for File Name in Run 100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
                raise ValueError('value {} need to be of type str '
                                 'for field `suffix_for_file_name_in_run_100`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `suffix_for_file_name_in_run_100`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `suffix_for_file_name_in_run_100`')
        self._data["Suffix for File Name in Run 100"] = value

    def check(self):
        """ Checks if all required fields are not None
        """
        good = True
        for key in self.required_fields:
            if self._data[key] is None:
                good = False
                break
        return good

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

    def export(self):
        """ Export values of data object as list of strings"""
        out = []
        for key, value in self._data.iteritems():
            out.append(self._to_str(value))
        return out

    def __str__(self):
        out = [self.internal_name]
        out += self.export()
        return ",".join(out[:20])