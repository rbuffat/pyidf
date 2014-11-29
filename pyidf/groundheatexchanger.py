from collections import OrderedDict

class GroundHeatExchangerVertical(object):
    """ Corresponds to IDD object `GroundHeatExchanger:Vertical`
        Variable short time step vertical ground heat exchanger model based on
        Yavuztruk, C., J.D.Spitler. 1999. A Short Time Step response Factor Model for
        Vertical Ground Loop Heat Exchangers
        The Fluid Type in the associated condenser loop must be same for which the
        g-functions below are calculated.
    """
    internal_name = "GroundHeatExchanger:Vertical"
    field_count = 219

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `GroundHeatExchanger:Vertical`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Maximum Flow Rate"] = None
        self._data["Number of Bore Holes"] = None
        self._data["Bore Hole Length"] = None
        self._data["Bore Hole Radius"] = None
        self._data["Ground Thermal Conductivity"] = None
        self._data["Ground Thermal Heat Capacity"] = None
        self._data["Ground Temperature"] = None
        self._data["Design Flow Rate"] = None
        self._data["Grout Thermal Conductivity"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Out Diameter"] = None
        self._data["U-Tube Distance"] = None
        self._data["Pipe Thickness"] = None
        self._data["Maximum Length of Simulation"] = None
        self._data["G-Function Reference Ratio"] = None
        self._data["Number of Data Pairs of the G Function"] = None
        self._data["G-Function Ln(T/Ts) Value 1"] = None
        self._data["G-Function G Value 1"] = None
        self._data["G-Function Ln(T/Ts) Value 2"] = None
        self._data["G-Function G Value 2"] = None
        self._data["G-Function Ln(T/Ts) Value 3"] = None
        self._data["G-Function G Value 3"] = None
        self._data["G-Function Ln(T/Ts) Value 4"] = None
        self._data["G-Function G Value 4"] = None
        self._data["G-Function Ln(T/Ts) Value 5"] = None
        self._data["G-Function G Value 5"] = None
        self._data["G-Function Ln(T/Ts) Value 6"] = None
        self._data["G-Function G Value 6"] = None
        self._data["G-Function Ln(T/Ts) Value 7"] = None
        self._data["G-Function G Value 7"] = None
        self._data["G-Function Ln(T/Ts) Value 8"] = None
        self._data["G-Function G Value 8"] = None
        self._data["G-Function Ln(T/Ts) Value 9"] = None
        self._data["G-Function G Value 9"] = None
        self._data["G-Function Ln(T/Ts) Value 10"] = None
        self._data["G-Function G Value 10"] = None
        self._data["G-Function Ln(T/Ts) Value 11"] = None
        self._data["G-Function G Value 11"] = None
        self._data["G-Function Ln(T/Ts) Value 12"] = None
        self._data["G-Function G Value 12"] = None
        self._data["G-Function Ln(T/Ts) Value 13"] = None
        self._data["G-Function G Value 13"] = None
        self._data["G-Function Ln(T/Ts) Value 14"] = None
        self._data["G-Function G Value 14"] = None
        self._data["G-Function Ln(T/Ts) Value 15"] = None
        self._data["G-Function G Value 15"] = None
        self._data["G-Function Ln(T/Ts) Value 16"] = None
        self._data["G-Function G Value 16"] = None
        self._data["G-Function Ln(T/Ts) Value 17"] = None
        self._data["G-Function G Value 17"] = None
        self._data["G-Function Ln(T/Ts) Value 18"] = None
        self._data["G-Function G Value 18"] = None
        self._data["G-Function Ln(T/Ts) Value 19"] = None
        self._data["G-Function G Value 19"] = None
        self._data["G-Function Ln(T/Ts) Value 20"] = None
        self._data["G-Function G Value 20"] = None
        self._data["G-Function Ln(T/Ts) Value 21"] = None
        self._data["G-Function G Value 21"] = None
        self._data["G-Function Ln(T/Ts) Value 22"] = None
        self._data["G-Function G Value 22"] = None
        self._data["G-Function Ln(T/Ts) Value 23"] = None
        self._data["G-Function G Value 23"] = None
        self._data["G-Function Ln(T/Ts) Value 24"] = None
        self._data["G-Function G Value 24"] = None
        self._data["G-Function Ln(T/Ts) Value 25"] = None
        self._data["G-Function G Value 25"] = None
        self._data["G-Function Ln(T/Ts) Value 26"] = None
        self._data["G-Function G Value 26"] = None
        self._data["G-Function Ln(T/Ts) Value 27"] = None
        self._data["G-Function G Value 27"] = None
        self._data["G-Function Ln(T/Ts) Value 28"] = None
        self._data["G-Function G Value 28"] = None
        self._data["G-Function Ln(T/Ts) Value 29"] = None
        self._data["G-Function G Value 29"] = None
        self._data["G-Function Ln(T/Ts) Value 30"] = None
        self._data["G-Function G Value 30"] = None
        self._data["G-Function Ln(T/Ts) Value 31"] = None
        self._data["G-Function G Value 31"] = None
        self._data["G-Function Ln(T/Ts) Value 32"] = None
        self._data["G-Function G Value 32"] = None
        self._data["G-Function Ln(T/Ts) Value 33"] = None
        self._data["G-Function G Value 33"] = None
        self._data["G-Function Ln(T/Ts) Value 34"] = None
        self._data["G-Function G Value 34"] = None
        self._data["G-Function Ln(T/Ts) Value 35"] = None
        self._data["G-Function G Value 35"] = None
        self._data["G-Function Ln(T/Ts) Value 36"] = None
        self._data["G-Function G Value 36"] = None
        self._data["G-Function Ln(T/Ts) Value 37"] = None
        self._data["G-Function G Value 37"] = None
        self._data["G-Function Ln(T/Ts) Value 38"] = None
        self._data["G-Function G Value 38"] = None
        self._data["G-Function Ln(T/Ts) Value 39"] = None
        self._data["G-Function G Value 39"] = None
        self._data["G-Function Ln(T/Ts) Value 40"] = None
        self._data["G-Function G Value 40"] = None
        self._data["G-Function Ln(T/Ts) Value 41"] = None
        self._data["G-Function G Value 41"] = None
        self._data["G-Function Ln(T/Ts) Value 42"] = None
        self._data["G-Function G Value 42"] = None
        self._data["G-Function Ln(T/Ts) Value 43"] = None
        self._data["G-Function G Value 43"] = None
        self._data["G-Function Ln(T/Ts) Value 44"] = None
        self._data["G-Function G Value 44"] = None
        self._data["G-Function Ln(T/Ts) Value 45"] = None
        self._data["G-Function G Value 45"] = None
        self._data["G-Function Ln(T/Ts) Value 46"] = None
        self._data["G-Function G Value 46"] = None
        self._data["G-Function Ln(T/Ts) Value 47"] = None
        self._data["G-Function G Value 47"] = None
        self._data["G-Function Ln(T/Ts) Value 48"] = None
        self._data["G-Function G Value 48"] = None
        self._data["G-Function Ln(T/Ts) Value 49"] = None
        self._data["G-Function G Value 49"] = None
        self._data["G-Function Ln(T/Ts) Value 50"] = None
        self._data["G-Function G Value 50"] = None
        self._data["G-Function Ln(T/Ts) Value 51"] = None
        self._data["G-Function G Value 51"] = None
        self._data["G-Function Ln(T/Ts) Value 52"] = None
        self._data["G-Function G Value 52"] = None
        self._data["G-Function Ln(T/Ts) Value 53"] = None
        self._data["G-Function G Value 53"] = None
        self._data["G-Function Ln(T/Ts) Value 54"] = None
        self._data["G-Function G Value 54"] = None
        self._data["G-Function Ln(T/Ts) Value 55"] = None
        self._data["G-Function G Value 55"] = None
        self._data["G-Function Ln(T/Ts) Value 56"] = None
        self._data["G-Function G Value 56"] = None
        self._data["G-Function Ln(T/Ts) Value 57"] = None
        self._data["G-Function G Value 57"] = None
        self._data["G-Function Ln(T/Ts) Value 58"] = None
        self._data["G-Function G Value 58"] = None
        self._data["G-Function Ln(T/Ts) Value 59"] = None
        self._data["G-Function G Value 59"] = None
        self._data["G-Function Ln(T/Ts) Value 60"] = None
        self._data["G-Function G Value 60"] = None
        self._data["G-Function Ln(T/Ts) Value 61"] = None
        self._data["G-Function G Value 61"] = None
        self._data["G-Function Ln(T/Ts) Value 62"] = None
        self._data["G-Function G Value 62"] = None
        self._data["G-Function Ln(T/Ts) Value 63"] = None
        self._data["G-Function G Value 63"] = None
        self._data["G-Function Ln(T/Ts) Value 64"] = None
        self._data["G-Function G Value 64"] = None
        self._data["G-Function Ln(T/Ts) Value 65"] = None
        self._data["G-Function G Value 65"] = None
        self._data["G-Function Ln(T/Ts) Value 66"] = None
        self._data["G-Function G Value 66"] = None
        self._data["G-Function Ln(T/Ts) Value 67"] = None
        self._data["G-Function G Value 67"] = None
        self._data["G-Function Ln(T/Ts) Value 68"] = None
        self._data["G-Function G Value 68"] = None
        self._data["G-Function Ln(T/Ts) Value 69"] = None
        self._data["G-Function G Value 69"] = None
        self._data["G-Function Ln(T/Ts) Value 70"] = None
        self._data["G-Function G Value 70"] = None
        self._data["G-Function Ln(T/Ts) Value 71"] = None
        self._data["G-Function G Value 71"] = None
        self._data["G-Function Ln(T/Ts) Value 72"] = None
        self._data["G-Function G Value 72"] = None
        self._data["G-Function Ln(T/Ts) Value 73"] = None
        self._data["G-Function G Value 73"] = None
        self._data["G-Function Ln(T/Ts) Value 74"] = None
        self._data["G-Function G Value 74"] = None
        self._data["G-Function Ln(T/Ts) Value 75"] = None
        self._data["G-Function G Value 75"] = None
        self._data["G-Function Ln(T/Ts) Value 76"] = None
        self._data["G-Function G Value 76"] = None
        self._data["G-Function Ln(T/Ts) Value 77"] = None
        self._data["G-Function G Value 77"] = None
        self._data["G-Function Ln(T/Ts) Value 78"] = None
        self._data["G-Function G Value 78"] = None
        self._data["G-Function Ln(T/Ts) Value 79"] = None
        self._data["G-Function G Value 79"] = None
        self._data["G-Function Ln(T/Ts) Value 80"] = None
        self._data["G-Function G Value 80"] = None
        self._data["G-Function Ln(T/Ts) Value 81"] = None
        self._data["G-Function G Value 81"] = None
        self._data["G-Function Ln(T/Ts) Value 82"] = None
        self._data["G-Function G Value 82"] = None
        self._data["G-Function Ln(T/Ts) Value 83"] = None
        self._data["G-Function G Value 83"] = None
        self._data["G-Function Ln(T/Ts) Value 84"] = None
        self._data["G-Function G Value 84"] = None
        self._data["G-Function Ln(T/Ts) Value 85"] = None
        self._data["G-Function G Value 85"] = None
        self._data["G-Function Ln(T/Ts) Value 86"] = None
        self._data["G-Function G Value 86"] = None
        self._data["G-Function Ln(T/Ts) Value 87"] = None
        self._data["G-Function G Value 87"] = None
        self._data["G-Function Ln(T/Ts) Value 88"] = None
        self._data["G-Function G Value 88"] = None
        self._data["G-Function Ln(T/Ts) Value 89"] = None
        self._data["G-Function G Value 89"] = None
        self._data["G-Function Ln(T/Ts) Value 90"] = None
        self._data["G-Function G Value 90"] = None
        self._data["G-Function Ln(T/Ts) Value 91"] = None
        self._data["G-Function G Value 91"] = None
        self._data["G-Function Ln(T/Ts) Value 92"] = None
        self._data["G-Function G Value 92"] = None
        self._data["G-Function Ln(T/Ts) Value 93"] = None
        self._data["G-Function G Value 93"] = None
        self._data["G-Function Ln(T/Ts) Value 94"] = None
        self._data["G-Function G Value 94"] = None
        self._data["G-Function Ln(T/Ts) Value 95"] = None
        self._data["G-Function G Value 95"] = None
        self._data["G-Function Ln(T/Ts) Value 96"] = None
        self._data["G-Function G Value 96"] = None
        self._data["G-Function Ln(T/Ts) Value 97"] = None
        self._data["G-Function G Value 97"] = None
        self._data["G-Function Ln(T/Ts) Value 98"] = None
        self._data["G-Function G Value 98"] = None
        self._data["G-Function Ln(T/Ts) Value 99"] = None
        self._data["G-Function G Value 99"] = None
        self._data["G-Function Ln(T/Ts) Value 100"] = None
        self._data["G-Function G Value 100"] = None

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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_flow_rate = None
        else:
            self.maximum_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_bore_holes = None
        else:
            self.number_of_bore_holes = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bore_hole_length = None
        else:
            self.bore_hole_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.bore_hole_radius = None
        else:
            self.bore_hole_radius = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ground_thermal_conductivity = None
        else:
            self.ground_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ground_thermal_heat_capacity = None
        else:
            self.ground_thermal_heat_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ground_temperature = None
        else:
            self.ground_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.grout_thermal_conductivity = None
        else:
            self.grout_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_out_diameter = None
        else:
            self.pipe_out_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.utube_distance = None
        else:
            self.utube_distance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_thickness = None
        else:
            self.pipe_thickness = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_length_of_simulation = None
        else:
            self.maximum_length_of_simulation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_reference_ratio = None
        else:
            self.gfunction_reference_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_data_pairs_of_the_g_function = None
        else:
            self.number_of_data_pairs_of_the_g_function = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_1 = None
        else:
            self.gfunction_lnt_or_ts_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_1 = None
        else:
            self.gfunction_g_value_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_2 = None
        else:
            self.gfunction_lnt_or_ts_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_2 = None
        else:
            self.gfunction_g_value_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_3 = None
        else:
            self.gfunction_lnt_or_ts_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_3 = None
        else:
            self.gfunction_g_value_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_4 = None
        else:
            self.gfunction_lnt_or_ts_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_4 = None
        else:
            self.gfunction_g_value_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_5 = None
        else:
            self.gfunction_lnt_or_ts_value_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_5 = None
        else:
            self.gfunction_g_value_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_6 = None
        else:
            self.gfunction_lnt_or_ts_value_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_6 = None
        else:
            self.gfunction_g_value_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_7 = None
        else:
            self.gfunction_lnt_or_ts_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_7 = None
        else:
            self.gfunction_g_value_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_8 = None
        else:
            self.gfunction_lnt_or_ts_value_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_8 = None
        else:
            self.gfunction_g_value_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_9 = None
        else:
            self.gfunction_lnt_or_ts_value_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_9 = None
        else:
            self.gfunction_g_value_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_10 = None
        else:
            self.gfunction_lnt_or_ts_value_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_10 = None
        else:
            self.gfunction_g_value_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_11 = None
        else:
            self.gfunction_lnt_or_ts_value_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_11 = None
        else:
            self.gfunction_g_value_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_12 = None
        else:
            self.gfunction_lnt_or_ts_value_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_12 = None
        else:
            self.gfunction_g_value_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_13 = None
        else:
            self.gfunction_lnt_or_ts_value_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_13 = None
        else:
            self.gfunction_g_value_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_14 = None
        else:
            self.gfunction_lnt_or_ts_value_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_14 = None
        else:
            self.gfunction_g_value_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_15 = None
        else:
            self.gfunction_lnt_or_ts_value_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_15 = None
        else:
            self.gfunction_g_value_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_16 = None
        else:
            self.gfunction_lnt_or_ts_value_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_16 = None
        else:
            self.gfunction_g_value_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_17 = None
        else:
            self.gfunction_lnt_or_ts_value_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_17 = None
        else:
            self.gfunction_g_value_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_18 = None
        else:
            self.gfunction_lnt_or_ts_value_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_18 = None
        else:
            self.gfunction_g_value_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_19 = None
        else:
            self.gfunction_lnt_or_ts_value_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_19 = None
        else:
            self.gfunction_g_value_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_20 = None
        else:
            self.gfunction_lnt_or_ts_value_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_20 = None
        else:
            self.gfunction_g_value_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_21 = None
        else:
            self.gfunction_lnt_or_ts_value_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_21 = None
        else:
            self.gfunction_g_value_21 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_22 = None
        else:
            self.gfunction_lnt_or_ts_value_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_22 = None
        else:
            self.gfunction_g_value_22 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_23 = None
        else:
            self.gfunction_lnt_or_ts_value_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_23 = None
        else:
            self.gfunction_g_value_23 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_24 = None
        else:
            self.gfunction_lnt_or_ts_value_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_24 = None
        else:
            self.gfunction_g_value_24 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_25 = None
        else:
            self.gfunction_lnt_or_ts_value_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_25 = None
        else:
            self.gfunction_g_value_25 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_26 = None
        else:
            self.gfunction_lnt_or_ts_value_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_26 = None
        else:
            self.gfunction_g_value_26 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_27 = None
        else:
            self.gfunction_lnt_or_ts_value_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_27 = None
        else:
            self.gfunction_g_value_27 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_28 = None
        else:
            self.gfunction_lnt_or_ts_value_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_28 = None
        else:
            self.gfunction_g_value_28 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_29 = None
        else:
            self.gfunction_lnt_or_ts_value_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_29 = None
        else:
            self.gfunction_g_value_29 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_30 = None
        else:
            self.gfunction_lnt_or_ts_value_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_30 = None
        else:
            self.gfunction_g_value_30 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_31 = None
        else:
            self.gfunction_lnt_or_ts_value_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_31 = None
        else:
            self.gfunction_g_value_31 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_32 = None
        else:
            self.gfunction_lnt_or_ts_value_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_32 = None
        else:
            self.gfunction_g_value_32 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_33 = None
        else:
            self.gfunction_lnt_or_ts_value_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_33 = None
        else:
            self.gfunction_g_value_33 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_34 = None
        else:
            self.gfunction_lnt_or_ts_value_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_34 = None
        else:
            self.gfunction_g_value_34 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_35 = None
        else:
            self.gfunction_lnt_or_ts_value_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_35 = None
        else:
            self.gfunction_g_value_35 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_36 = None
        else:
            self.gfunction_lnt_or_ts_value_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_36 = None
        else:
            self.gfunction_g_value_36 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_37 = None
        else:
            self.gfunction_lnt_or_ts_value_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_37 = None
        else:
            self.gfunction_g_value_37 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_38 = None
        else:
            self.gfunction_lnt_or_ts_value_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_38 = None
        else:
            self.gfunction_g_value_38 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_39 = None
        else:
            self.gfunction_lnt_or_ts_value_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_39 = None
        else:
            self.gfunction_g_value_39 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_40 = None
        else:
            self.gfunction_lnt_or_ts_value_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_40 = None
        else:
            self.gfunction_g_value_40 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_41 = None
        else:
            self.gfunction_lnt_or_ts_value_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_41 = None
        else:
            self.gfunction_g_value_41 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_42 = None
        else:
            self.gfunction_lnt_or_ts_value_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_42 = None
        else:
            self.gfunction_g_value_42 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_43 = None
        else:
            self.gfunction_lnt_or_ts_value_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_43 = None
        else:
            self.gfunction_g_value_43 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_44 = None
        else:
            self.gfunction_lnt_or_ts_value_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_44 = None
        else:
            self.gfunction_g_value_44 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_45 = None
        else:
            self.gfunction_lnt_or_ts_value_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_45 = None
        else:
            self.gfunction_g_value_45 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_46 = None
        else:
            self.gfunction_lnt_or_ts_value_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_46 = None
        else:
            self.gfunction_g_value_46 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_47 = None
        else:
            self.gfunction_lnt_or_ts_value_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_47 = None
        else:
            self.gfunction_g_value_47 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_48 = None
        else:
            self.gfunction_lnt_or_ts_value_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_48 = None
        else:
            self.gfunction_g_value_48 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_49 = None
        else:
            self.gfunction_lnt_or_ts_value_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_49 = None
        else:
            self.gfunction_g_value_49 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_50 = None
        else:
            self.gfunction_lnt_or_ts_value_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_50 = None
        else:
            self.gfunction_g_value_50 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_51 = None
        else:
            self.gfunction_lnt_or_ts_value_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_51 = None
        else:
            self.gfunction_g_value_51 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_52 = None
        else:
            self.gfunction_lnt_or_ts_value_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_52 = None
        else:
            self.gfunction_g_value_52 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_53 = None
        else:
            self.gfunction_lnt_or_ts_value_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_53 = None
        else:
            self.gfunction_g_value_53 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_54 = None
        else:
            self.gfunction_lnt_or_ts_value_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_54 = None
        else:
            self.gfunction_g_value_54 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_55 = None
        else:
            self.gfunction_lnt_or_ts_value_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_55 = None
        else:
            self.gfunction_g_value_55 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_56 = None
        else:
            self.gfunction_lnt_or_ts_value_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_56 = None
        else:
            self.gfunction_g_value_56 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_57 = None
        else:
            self.gfunction_lnt_or_ts_value_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_57 = None
        else:
            self.gfunction_g_value_57 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_58 = None
        else:
            self.gfunction_lnt_or_ts_value_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_58 = None
        else:
            self.gfunction_g_value_58 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_59 = None
        else:
            self.gfunction_lnt_or_ts_value_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_59 = None
        else:
            self.gfunction_g_value_59 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_60 = None
        else:
            self.gfunction_lnt_or_ts_value_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_60 = None
        else:
            self.gfunction_g_value_60 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_61 = None
        else:
            self.gfunction_lnt_or_ts_value_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_61 = None
        else:
            self.gfunction_g_value_61 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_62 = None
        else:
            self.gfunction_lnt_or_ts_value_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_62 = None
        else:
            self.gfunction_g_value_62 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_63 = None
        else:
            self.gfunction_lnt_or_ts_value_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_63 = None
        else:
            self.gfunction_g_value_63 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_64 = None
        else:
            self.gfunction_lnt_or_ts_value_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_64 = None
        else:
            self.gfunction_g_value_64 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_65 = None
        else:
            self.gfunction_lnt_or_ts_value_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_65 = None
        else:
            self.gfunction_g_value_65 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_66 = None
        else:
            self.gfunction_lnt_or_ts_value_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_66 = None
        else:
            self.gfunction_g_value_66 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_67 = None
        else:
            self.gfunction_lnt_or_ts_value_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_67 = None
        else:
            self.gfunction_g_value_67 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_68 = None
        else:
            self.gfunction_lnt_or_ts_value_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_68 = None
        else:
            self.gfunction_g_value_68 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_69 = None
        else:
            self.gfunction_lnt_or_ts_value_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_69 = None
        else:
            self.gfunction_g_value_69 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_70 = None
        else:
            self.gfunction_lnt_or_ts_value_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_70 = None
        else:
            self.gfunction_g_value_70 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_71 = None
        else:
            self.gfunction_lnt_or_ts_value_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_71 = None
        else:
            self.gfunction_g_value_71 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_72 = None
        else:
            self.gfunction_lnt_or_ts_value_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_72 = None
        else:
            self.gfunction_g_value_72 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_73 = None
        else:
            self.gfunction_lnt_or_ts_value_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_73 = None
        else:
            self.gfunction_g_value_73 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_74 = None
        else:
            self.gfunction_lnt_or_ts_value_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_74 = None
        else:
            self.gfunction_g_value_74 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_75 = None
        else:
            self.gfunction_lnt_or_ts_value_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_75 = None
        else:
            self.gfunction_g_value_75 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_76 = None
        else:
            self.gfunction_lnt_or_ts_value_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_76 = None
        else:
            self.gfunction_g_value_76 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_77 = None
        else:
            self.gfunction_lnt_or_ts_value_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_77 = None
        else:
            self.gfunction_g_value_77 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_78 = None
        else:
            self.gfunction_lnt_or_ts_value_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_78 = None
        else:
            self.gfunction_g_value_78 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_79 = None
        else:
            self.gfunction_lnt_or_ts_value_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_79 = None
        else:
            self.gfunction_g_value_79 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_80 = None
        else:
            self.gfunction_lnt_or_ts_value_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_80 = None
        else:
            self.gfunction_g_value_80 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_81 = None
        else:
            self.gfunction_lnt_or_ts_value_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_81 = None
        else:
            self.gfunction_g_value_81 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_82 = None
        else:
            self.gfunction_lnt_or_ts_value_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_82 = None
        else:
            self.gfunction_g_value_82 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_83 = None
        else:
            self.gfunction_lnt_or_ts_value_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_83 = None
        else:
            self.gfunction_g_value_83 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_84 = None
        else:
            self.gfunction_lnt_or_ts_value_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_84 = None
        else:
            self.gfunction_g_value_84 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_85 = None
        else:
            self.gfunction_lnt_or_ts_value_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_85 = None
        else:
            self.gfunction_g_value_85 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_86 = None
        else:
            self.gfunction_lnt_or_ts_value_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_86 = None
        else:
            self.gfunction_g_value_86 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_87 = None
        else:
            self.gfunction_lnt_or_ts_value_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_87 = None
        else:
            self.gfunction_g_value_87 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_88 = None
        else:
            self.gfunction_lnt_or_ts_value_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_88 = None
        else:
            self.gfunction_g_value_88 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_89 = None
        else:
            self.gfunction_lnt_or_ts_value_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_89 = None
        else:
            self.gfunction_g_value_89 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_90 = None
        else:
            self.gfunction_lnt_or_ts_value_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_90 = None
        else:
            self.gfunction_g_value_90 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_91 = None
        else:
            self.gfunction_lnt_or_ts_value_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_91 = None
        else:
            self.gfunction_g_value_91 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_92 = None
        else:
            self.gfunction_lnt_or_ts_value_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_92 = None
        else:
            self.gfunction_g_value_92 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_93 = None
        else:
            self.gfunction_lnt_or_ts_value_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_93 = None
        else:
            self.gfunction_g_value_93 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_94 = None
        else:
            self.gfunction_lnt_or_ts_value_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_94 = None
        else:
            self.gfunction_g_value_94 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_95 = None
        else:
            self.gfunction_lnt_or_ts_value_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_95 = None
        else:
            self.gfunction_g_value_95 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_96 = None
        else:
            self.gfunction_lnt_or_ts_value_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_96 = None
        else:
            self.gfunction_g_value_96 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_97 = None
        else:
            self.gfunction_lnt_or_ts_value_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_97 = None
        else:
            self.gfunction_g_value_97 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_98 = None
        else:
            self.gfunction_lnt_or_ts_value_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_98 = None
        else:
            self.gfunction_g_value_98 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_99 = None
        else:
            self.gfunction_lnt_or_ts_value_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_99 = None
        else:
            self.gfunction_g_value_99 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_lnt_or_ts_value_100 = None
        else:
            self.gfunction_lnt_or_ts_value_100 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.gfunction_g_value_100 = None
        else:
            self.gfunction_g_value_100 = vals[i]
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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def maximum_flow_rate(self):
        """Get maximum_flow_rate

        Returns:
            float: the value of `maximum_flow_rate` or None if not set
        """
        return self._data["Maximum Flow Rate"]

    @maximum_flow_rate.setter
    def maximum_flow_rate(self, value=None):
        """  Corresponds to IDD Field `maximum_flow_rate`

        Args:
            value (float): value for IDD Field `maximum_flow_rate`
                Unit: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_flow_rate`')

        self._data["Maximum Flow Rate"] = value

    @property
    def number_of_bore_holes(self):
        """Get number_of_bore_holes

        Returns:
            float: the value of `number_of_bore_holes` or None if not set
        """
        return self._data["Number of Bore Holes"]

    @number_of_bore_holes.setter
    def number_of_bore_holes(self, value=None):
        """  Corresponds to IDD Field `number_of_bore_holes`

        Args:
            value (float): value for IDD Field `number_of_bore_holes`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_bore_holes`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_bore_holes`')

        self._data["Number of Bore Holes"] = value

    @property
    def bore_hole_length(self):
        """Get bore_hole_length

        Returns:
            float: the value of `bore_hole_length` or None if not set
        """
        return self._data["Bore Hole Length"]

    @bore_hole_length.setter
    def bore_hole_length(self, value=None):
        """  Corresponds to IDD Field `bore_hole_length`

        Args:
            value (float): value for IDD Field `bore_hole_length`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `bore_hole_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `bore_hole_length`')

        self._data["Bore Hole Length"] = value

    @property
    def bore_hole_radius(self):
        """Get bore_hole_radius

        Returns:
            float: the value of `bore_hole_radius` or None if not set
        """
        return self._data["Bore Hole Radius"]

    @bore_hole_radius.setter
    def bore_hole_radius(self, value=None):
        """  Corresponds to IDD Field `bore_hole_radius`

        Args:
            value (float): value for IDD Field `bore_hole_radius`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `bore_hole_radius`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `bore_hole_radius`')

        self._data["Bore Hole Radius"] = value

    @property
    def ground_thermal_conductivity(self):
        """Get ground_thermal_conductivity

        Returns:
            float: the value of `ground_thermal_conductivity` or None if not set
        """
        return self._data["Ground Thermal Conductivity"]

    @ground_thermal_conductivity.setter
    def ground_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `ground_thermal_conductivity`

        Args:
            value (float): value for IDD Field `ground_thermal_conductivity`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_thermal_conductivity`')

        self._data["Ground Thermal Conductivity"] = value

    @property
    def ground_thermal_heat_capacity(self):
        """Get ground_thermal_heat_capacity

        Returns:
            float: the value of `ground_thermal_heat_capacity` or None if not set
        """
        return self._data["Ground Thermal Heat Capacity"]

    @ground_thermal_heat_capacity.setter
    def ground_thermal_heat_capacity(self, value=None):
        """  Corresponds to IDD Field `ground_thermal_heat_capacity`

        Args:
            value (float): value for IDD Field `ground_thermal_heat_capacity`
                Unit: J/m3-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_thermal_heat_capacity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_thermal_heat_capacity`')

        self._data["Ground Thermal Heat Capacity"] = value

    @property
    def ground_temperature(self):
        """Get ground_temperature

        Returns:
            float: the value of `ground_temperature` or None if not set
        """
        return self._data["Ground Temperature"]

    @ground_temperature.setter
    def ground_temperature(self, value=None):
        """  Corresponds to IDD Field `ground_temperature`

        Args:
            value (float): value for IDD Field `ground_temperature`
                Unit: C
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_temperature`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_temperature`')

        self._data["Ground Temperature"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`

        Args:
            value (float): value for IDD Field `design_flow_rate`
                Unit: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_flow_rate`')

        self._data["Design Flow Rate"] = value

    @property
    def grout_thermal_conductivity(self):
        """Get grout_thermal_conductivity

        Returns:
            float: the value of `grout_thermal_conductivity` or None if not set
        """
        return self._data["Grout Thermal Conductivity"]

    @grout_thermal_conductivity.setter
    def grout_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `grout_thermal_conductivity`

        Args:
            value (float): value for IDD Field `grout_thermal_conductivity`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `grout_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `grout_thermal_conductivity`')

        self._data["Grout Thermal Conductivity"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `pipe_thermal_conductivity`

        Args:
            value (float): value for IDD Field `pipe_thermal_conductivity`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')

        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_out_diameter(self):
        """Get pipe_out_diameter

        Returns:
            float: the value of `pipe_out_diameter` or None if not set
        """
        return self._data["Pipe Out Diameter"]

    @pipe_out_diameter.setter
    def pipe_out_diameter(self, value=None):
        """  Corresponds to IDD Field `pipe_out_diameter`

        Args:
            value (float): value for IDD Field `pipe_out_diameter`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_out_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_out_diameter`')

        self._data["Pipe Out Diameter"] = value

    @property
    def utube_distance(self):
        """Get utube_distance

        Returns:
            float: the value of `utube_distance` or None if not set
        """
        return self._data["U-Tube Distance"]

    @utube_distance.setter
    def utube_distance(self, value=None):
        """  Corresponds to IDD Field `utube_distance`

        Args:
            value (float): value for IDD Field `utube_distance`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `utube_distance`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `utube_distance`')

        self._data["U-Tube Distance"] = value

    @property
    def pipe_thickness(self):
        """Get pipe_thickness

        Returns:
            float: the value of `pipe_thickness` or None if not set
        """
        return self._data["Pipe Thickness"]

    @pipe_thickness.setter
    def pipe_thickness(self, value=None):
        """  Corresponds to IDD Field `pipe_thickness`

        Args:
            value (float): value for IDD Field `pipe_thickness`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thickness`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thickness`')

        self._data["Pipe Thickness"] = value

    @property
    def maximum_length_of_simulation(self):
        """Get maximum_length_of_simulation

        Returns:
            float: the value of `maximum_length_of_simulation` or None if not set
        """
        return self._data["Maximum Length of Simulation"]

    @maximum_length_of_simulation.setter
    def maximum_length_of_simulation(self, value=None):
        """  Corresponds to IDD Field `maximum_length_of_simulation`

        Args:
            value (float): value for IDD Field `maximum_length_of_simulation`
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_length_of_simulation`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `maximum_length_of_simulation`')

        self._data["Maximum Length of Simulation"] = value

    @property
    def gfunction_reference_ratio(self):
        """Get gfunction_reference_ratio

        Returns:
            float: the value of `gfunction_reference_ratio` or None if not set
        """
        return self._data["G-Function Reference Ratio"]

    @gfunction_reference_ratio.setter
    def gfunction_reference_ratio(self, value=0.0005 ):
        """  Corresponds to IDD Field `gfunction_reference_ratio`

        Args:
            value (float): value for IDD Field `gfunction_reference_ratio`
                Unit: dimensionless
                Default value: 0.0005
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_reference_ratio`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `gfunction_reference_ratio`')

        self._data["G-Function Reference Ratio"] = value

    @property
    def number_of_data_pairs_of_the_g_function(self):
        """Get number_of_data_pairs_of_the_g_function

        Returns:
            float: the value of `number_of_data_pairs_of_the_g_function` or None if not set
        """
        return self._data["Number of Data Pairs of the G Function"]

    @number_of_data_pairs_of_the_g_function.setter
    def number_of_data_pairs_of_the_g_function(self, value=None):
        """  Corresponds to IDD Field `number_of_data_pairs_of_the_g_function`

        Args:
            value (float): value for IDD Field `number_of_data_pairs_of_the_g_function`
                value > 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `number_of_data_pairs_of_the_g_function`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `number_of_data_pairs_of_the_g_function`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `number_of_data_pairs_of_the_g_function`')

        self._data["Number of Data Pairs of the G Function"] = value

    @property
    def gfunction_lnt_or_ts_value_1(self):
        """Get gfunction_lnt_or_ts_value_1

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_1` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 1"]

    @gfunction_lnt_or_ts_value_1.setter
    def gfunction_lnt_or_ts_value_1(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_1`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_1`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 1"] = value

    @property
    def gfunction_g_value_1(self):
        """Get gfunction_g_value_1

        Returns:
            float: the value of `gfunction_g_value_1` or None if not set
        """
        return self._data["G-Function G Value 1"]

    @gfunction_g_value_1.setter
    def gfunction_g_value_1(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_1`

        Args:
            value (float): value for IDD Field `gfunction_g_value_1`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_1`'.format(value))

        self._data["G-Function G Value 1"] = value

    @property
    def gfunction_lnt_or_ts_value_2(self):
        """Get gfunction_lnt_or_ts_value_2

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_2` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 2"]

    @gfunction_lnt_or_ts_value_2.setter
    def gfunction_lnt_or_ts_value_2(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_2`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_2`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 2"] = value

    @property
    def gfunction_g_value_2(self):
        """Get gfunction_g_value_2

        Returns:
            float: the value of `gfunction_g_value_2` or None if not set
        """
        return self._data["G-Function G Value 2"]

    @gfunction_g_value_2.setter
    def gfunction_g_value_2(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_2`

        Args:
            value (float): value for IDD Field `gfunction_g_value_2`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_2`'.format(value))

        self._data["G-Function G Value 2"] = value

    @property
    def gfunction_lnt_or_ts_value_3(self):
        """Get gfunction_lnt_or_ts_value_3

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_3` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 3"]

    @gfunction_lnt_or_ts_value_3.setter
    def gfunction_lnt_or_ts_value_3(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_3`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_3`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 3"] = value

    @property
    def gfunction_g_value_3(self):
        """Get gfunction_g_value_3

        Returns:
            float: the value of `gfunction_g_value_3` or None if not set
        """
        return self._data["G-Function G Value 3"]

    @gfunction_g_value_3.setter
    def gfunction_g_value_3(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_3`

        Args:
            value (float): value for IDD Field `gfunction_g_value_3`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_3`'.format(value))

        self._data["G-Function G Value 3"] = value

    @property
    def gfunction_lnt_or_ts_value_4(self):
        """Get gfunction_lnt_or_ts_value_4

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_4` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 4"]

    @gfunction_lnt_or_ts_value_4.setter
    def gfunction_lnt_or_ts_value_4(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_4`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_4`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 4"] = value

    @property
    def gfunction_g_value_4(self):
        """Get gfunction_g_value_4

        Returns:
            float: the value of `gfunction_g_value_4` or None if not set
        """
        return self._data["G-Function G Value 4"]

    @gfunction_g_value_4.setter
    def gfunction_g_value_4(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_4`

        Args:
            value (float): value for IDD Field `gfunction_g_value_4`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_4`'.format(value))

        self._data["G-Function G Value 4"] = value

    @property
    def gfunction_lnt_or_ts_value_5(self):
        """Get gfunction_lnt_or_ts_value_5

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_5` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 5"]

    @gfunction_lnt_or_ts_value_5.setter
    def gfunction_lnt_or_ts_value_5(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_5`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_5`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 5"] = value

    @property
    def gfunction_g_value_5(self):
        """Get gfunction_g_value_5

        Returns:
            float: the value of `gfunction_g_value_5` or None if not set
        """
        return self._data["G-Function G Value 5"]

    @gfunction_g_value_5.setter
    def gfunction_g_value_5(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_5`

        Args:
            value (float): value for IDD Field `gfunction_g_value_5`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_5`'.format(value))

        self._data["G-Function G Value 5"] = value

    @property
    def gfunction_lnt_or_ts_value_6(self):
        """Get gfunction_lnt_or_ts_value_6

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_6` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 6"]

    @gfunction_lnt_or_ts_value_6.setter
    def gfunction_lnt_or_ts_value_6(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_6`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_6`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 6"] = value

    @property
    def gfunction_g_value_6(self):
        """Get gfunction_g_value_6

        Returns:
            float: the value of `gfunction_g_value_6` or None if not set
        """
        return self._data["G-Function G Value 6"]

    @gfunction_g_value_6.setter
    def gfunction_g_value_6(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_6`

        Args:
            value (float): value for IDD Field `gfunction_g_value_6`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_6`'.format(value))

        self._data["G-Function G Value 6"] = value

    @property
    def gfunction_lnt_or_ts_value_7(self):
        """Get gfunction_lnt_or_ts_value_7

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_7` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 7"]

    @gfunction_lnt_or_ts_value_7.setter
    def gfunction_lnt_or_ts_value_7(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_7`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_7`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 7"] = value

    @property
    def gfunction_g_value_7(self):
        """Get gfunction_g_value_7

        Returns:
            float: the value of `gfunction_g_value_7` or None if not set
        """
        return self._data["G-Function G Value 7"]

    @gfunction_g_value_7.setter
    def gfunction_g_value_7(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_7`

        Args:
            value (float): value for IDD Field `gfunction_g_value_7`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_7`'.format(value))

        self._data["G-Function G Value 7"] = value

    @property
    def gfunction_lnt_or_ts_value_8(self):
        """Get gfunction_lnt_or_ts_value_8

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_8` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 8"]

    @gfunction_lnt_or_ts_value_8.setter
    def gfunction_lnt_or_ts_value_8(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_8`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_8`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 8"] = value

    @property
    def gfunction_g_value_8(self):
        """Get gfunction_g_value_8

        Returns:
            float: the value of `gfunction_g_value_8` or None if not set
        """
        return self._data["G-Function G Value 8"]

    @gfunction_g_value_8.setter
    def gfunction_g_value_8(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_8`

        Args:
            value (float): value for IDD Field `gfunction_g_value_8`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_8`'.format(value))

        self._data["G-Function G Value 8"] = value

    @property
    def gfunction_lnt_or_ts_value_9(self):
        """Get gfunction_lnt_or_ts_value_9

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_9` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 9"]

    @gfunction_lnt_or_ts_value_9.setter
    def gfunction_lnt_or_ts_value_9(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_9`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_9`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 9"] = value

    @property
    def gfunction_g_value_9(self):
        """Get gfunction_g_value_9

        Returns:
            float: the value of `gfunction_g_value_9` or None if not set
        """
        return self._data["G-Function G Value 9"]

    @gfunction_g_value_9.setter
    def gfunction_g_value_9(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_9`

        Args:
            value (float): value for IDD Field `gfunction_g_value_9`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_9`'.format(value))

        self._data["G-Function G Value 9"] = value

    @property
    def gfunction_lnt_or_ts_value_10(self):
        """Get gfunction_lnt_or_ts_value_10

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_10` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 10"]

    @gfunction_lnt_or_ts_value_10.setter
    def gfunction_lnt_or_ts_value_10(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_10`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_10`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 10"] = value

    @property
    def gfunction_g_value_10(self):
        """Get gfunction_g_value_10

        Returns:
            float: the value of `gfunction_g_value_10` or None if not set
        """
        return self._data["G-Function G Value 10"]

    @gfunction_g_value_10.setter
    def gfunction_g_value_10(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_10`

        Args:
            value (float): value for IDD Field `gfunction_g_value_10`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_10`'.format(value))

        self._data["G-Function G Value 10"] = value

    @property
    def gfunction_lnt_or_ts_value_11(self):
        """Get gfunction_lnt_or_ts_value_11

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_11` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 11"]

    @gfunction_lnt_or_ts_value_11.setter
    def gfunction_lnt_or_ts_value_11(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_11`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_11`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 11"] = value

    @property
    def gfunction_g_value_11(self):
        """Get gfunction_g_value_11

        Returns:
            float: the value of `gfunction_g_value_11` or None if not set
        """
        return self._data["G-Function G Value 11"]

    @gfunction_g_value_11.setter
    def gfunction_g_value_11(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_11`

        Args:
            value (float): value for IDD Field `gfunction_g_value_11`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_11`'.format(value))

        self._data["G-Function G Value 11"] = value

    @property
    def gfunction_lnt_or_ts_value_12(self):
        """Get gfunction_lnt_or_ts_value_12

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_12` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 12"]

    @gfunction_lnt_or_ts_value_12.setter
    def gfunction_lnt_or_ts_value_12(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_12`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_12`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 12"] = value

    @property
    def gfunction_g_value_12(self):
        """Get gfunction_g_value_12

        Returns:
            float: the value of `gfunction_g_value_12` or None if not set
        """
        return self._data["G-Function G Value 12"]

    @gfunction_g_value_12.setter
    def gfunction_g_value_12(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_12`

        Args:
            value (float): value for IDD Field `gfunction_g_value_12`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_12`'.format(value))

        self._data["G-Function G Value 12"] = value

    @property
    def gfunction_lnt_or_ts_value_13(self):
        """Get gfunction_lnt_or_ts_value_13

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_13` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 13"]

    @gfunction_lnt_or_ts_value_13.setter
    def gfunction_lnt_or_ts_value_13(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_13`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_13`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 13"] = value

    @property
    def gfunction_g_value_13(self):
        """Get gfunction_g_value_13

        Returns:
            float: the value of `gfunction_g_value_13` or None if not set
        """
        return self._data["G-Function G Value 13"]

    @gfunction_g_value_13.setter
    def gfunction_g_value_13(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_13`

        Args:
            value (float): value for IDD Field `gfunction_g_value_13`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_13`'.format(value))

        self._data["G-Function G Value 13"] = value

    @property
    def gfunction_lnt_or_ts_value_14(self):
        """Get gfunction_lnt_or_ts_value_14

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_14` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 14"]

    @gfunction_lnt_or_ts_value_14.setter
    def gfunction_lnt_or_ts_value_14(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_14`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_14`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 14"] = value

    @property
    def gfunction_g_value_14(self):
        """Get gfunction_g_value_14

        Returns:
            float: the value of `gfunction_g_value_14` or None if not set
        """
        return self._data["G-Function G Value 14"]

    @gfunction_g_value_14.setter
    def gfunction_g_value_14(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_14`

        Args:
            value (float): value for IDD Field `gfunction_g_value_14`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_14`'.format(value))

        self._data["G-Function G Value 14"] = value

    @property
    def gfunction_lnt_or_ts_value_15(self):
        """Get gfunction_lnt_or_ts_value_15

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_15` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 15"]

    @gfunction_lnt_or_ts_value_15.setter
    def gfunction_lnt_or_ts_value_15(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_15`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_15`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 15"] = value

    @property
    def gfunction_g_value_15(self):
        """Get gfunction_g_value_15

        Returns:
            float: the value of `gfunction_g_value_15` or None if not set
        """
        return self._data["G-Function G Value 15"]

    @gfunction_g_value_15.setter
    def gfunction_g_value_15(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_15`

        Args:
            value (float): value for IDD Field `gfunction_g_value_15`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_15`'.format(value))

        self._data["G-Function G Value 15"] = value

    @property
    def gfunction_lnt_or_ts_value_16(self):
        """Get gfunction_lnt_or_ts_value_16

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_16` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 16"]

    @gfunction_lnt_or_ts_value_16.setter
    def gfunction_lnt_or_ts_value_16(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_16`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_16`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 16"] = value

    @property
    def gfunction_g_value_16(self):
        """Get gfunction_g_value_16

        Returns:
            float: the value of `gfunction_g_value_16` or None if not set
        """
        return self._data["G-Function G Value 16"]

    @gfunction_g_value_16.setter
    def gfunction_g_value_16(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_16`

        Args:
            value (float): value for IDD Field `gfunction_g_value_16`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_16`'.format(value))

        self._data["G-Function G Value 16"] = value

    @property
    def gfunction_lnt_or_ts_value_17(self):
        """Get gfunction_lnt_or_ts_value_17

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_17` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 17"]

    @gfunction_lnt_or_ts_value_17.setter
    def gfunction_lnt_or_ts_value_17(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_17`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_17`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 17"] = value

    @property
    def gfunction_g_value_17(self):
        """Get gfunction_g_value_17

        Returns:
            float: the value of `gfunction_g_value_17` or None if not set
        """
        return self._data["G-Function G Value 17"]

    @gfunction_g_value_17.setter
    def gfunction_g_value_17(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_17`

        Args:
            value (float): value for IDD Field `gfunction_g_value_17`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_17`'.format(value))

        self._data["G-Function G Value 17"] = value

    @property
    def gfunction_lnt_or_ts_value_18(self):
        """Get gfunction_lnt_or_ts_value_18

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_18` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 18"]

    @gfunction_lnt_or_ts_value_18.setter
    def gfunction_lnt_or_ts_value_18(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_18`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_18`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 18"] = value

    @property
    def gfunction_g_value_18(self):
        """Get gfunction_g_value_18

        Returns:
            float: the value of `gfunction_g_value_18` or None if not set
        """
        return self._data["G-Function G Value 18"]

    @gfunction_g_value_18.setter
    def gfunction_g_value_18(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_18`

        Args:
            value (float): value for IDD Field `gfunction_g_value_18`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_18`'.format(value))

        self._data["G-Function G Value 18"] = value

    @property
    def gfunction_lnt_or_ts_value_19(self):
        """Get gfunction_lnt_or_ts_value_19

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_19` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 19"]

    @gfunction_lnt_or_ts_value_19.setter
    def gfunction_lnt_or_ts_value_19(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_19`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_19`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 19"] = value

    @property
    def gfunction_g_value_19(self):
        """Get gfunction_g_value_19

        Returns:
            float: the value of `gfunction_g_value_19` or None if not set
        """
        return self._data["G-Function G Value 19"]

    @gfunction_g_value_19.setter
    def gfunction_g_value_19(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_19`

        Args:
            value (float): value for IDD Field `gfunction_g_value_19`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_19`'.format(value))

        self._data["G-Function G Value 19"] = value

    @property
    def gfunction_lnt_or_ts_value_20(self):
        """Get gfunction_lnt_or_ts_value_20

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_20` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 20"]

    @gfunction_lnt_or_ts_value_20.setter
    def gfunction_lnt_or_ts_value_20(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_20`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_20`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 20"] = value

    @property
    def gfunction_g_value_20(self):
        """Get gfunction_g_value_20

        Returns:
            float: the value of `gfunction_g_value_20` or None if not set
        """
        return self._data["G-Function G Value 20"]

    @gfunction_g_value_20.setter
    def gfunction_g_value_20(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_20`

        Args:
            value (float): value for IDD Field `gfunction_g_value_20`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_20`'.format(value))

        self._data["G-Function G Value 20"] = value

    @property
    def gfunction_lnt_or_ts_value_21(self):
        """Get gfunction_lnt_or_ts_value_21

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_21` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 21"]

    @gfunction_lnt_or_ts_value_21.setter
    def gfunction_lnt_or_ts_value_21(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_21`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_21`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 21"] = value

    @property
    def gfunction_g_value_21(self):
        """Get gfunction_g_value_21

        Returns:
            float: the value of `gfunction_g_value_21` or None if not set
        """
        return self._data["G-Function G Value 21"]

    @gfunction_g_value_21.setter
    def gfunction_g_value_21(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_21`

        Args:
            value (float): value for IDD Field `gfunction_g_value_21`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_21`'.format(value))

        self._data["G-Function G Value 21"] = value

    @property
    def gfunction_lnt_or_ts_value_22(self):
        """Get gfunction_lnt_or_ts_value_22

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_22` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 22"]

    @gfunction_lnt_or_ts_value_22.setter
    def gfunction_lnt_or_ts_value_22(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_22`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_22`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 22"] = value

    @property
    def gfunction_g_value_22(self):
        """Get gfunction_g_value_22

        Returns:
            float: the value of `gfunction_g_value_22` or None if not set
        """
        return self._data["G-Function G Value 22"]

    @gfunction_g_value_22.setter
    def gfunction_g_value_22(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_22`

        Args:
            value (float): value for IDD Field `gfunction_g_value_22`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_22`'.format(value))

        self._data["G-Function G Value 22"] = value

    @property
    def gfunction_lnt_or_ts_value_23(self):
        """Get gfunction_lnt_or_ts_value_23

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_23` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 23"]

    @gfunction_lnt_or_ts_value_23.setter
    def gfunction_lnt_or_ts_value_23(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_23`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_23`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 23"] = value

    @property
    def gfunction_g_value_23(self):
        """Get gfunction_g_value_23

        Returns:
            float: the value of `gfunction_g_value_23` or None if not set
        """
        return self._data["G-Function G Value 23"]

    @gfunction_g_value_23.setter
    def gfunction_g_value_23(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_23`

        Args:
            value (float): value for IDD Field `gfunction_g_value_23`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_23`'.format(value))

        self._data["G-Function G Value 23"] = value

    @property
    def gfunction_lnt_or_ts_value_24(self):
        """Get gfunction_lnt_or_ts_value_24

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_24` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 24"]

    @gfunction_lnt_or_ts_value_24.setter
    def gfunction_lnt_or_ts_value_24(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_24`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_24`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 24"] = value

    @property
    def gfunction_g_value_24(self):
        """Get gfunction_g_value_24

        Returns:
            float: the value of `gfunction_g_value_24` or None if not set
        """
        return self._data["G-Function G Value 24"]

    @gfunction_g_value_24.setter
    def gfunction_g_value_24(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_24`

        Args:
            value (float): value for IDD Field `gfunction_g_value_24`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_24`'.format(value))

        self._data["G-Function G Value 24"] = value

    @property
    def gfunction_lnt_or_ts_value_25(self):
        """Get gfunction_lnt_or_ts_value_25

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_25` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 25"]

    @gfunction_lnt_or_ts_value_25.setter
    def gfunction_lnt_or_ts_value_25(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_25`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_25`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 25"] = value

    @property
    def gfunction_g_value_25(self):
        """Get gfunction_g_value_25

        Returns:
            float: the value of `gfunction_g_value_25` or None if not set
        """
        return self._data["G-Function G Value 25"]

    @gfunction_g_value_25.setter
    def gfunction_g_value_25(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_25`

        Args:
            value (float): value for IDD Field `gfunction_g_value_25`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_25`'.format(value))

        self._data["G-Function G Value 25"] = value

    @property
    def gfunction_lnt_or_ts_value_26(self):
        """Get gfunction_lnt_or_ts_value_26

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_26` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 26"]

    @gfunction_lnt_or_ts_value_26.setter
    def gfunction_lnt_or_ts_value_26(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_26`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_26`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 26"] = value

    @property
    def gfunction_g_value_26(self):
        """Get gfunction_g_value_26

        Returns:
            float: the value of `gfunction_g_value_26` or None if not set
        """
        return self._data["G-Function G Value 26"]

    @gfunction_g_value_26.setter
    def gfunction_g_value_26(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_26`

        Args:
            value (float): value for IDD Field `gfunction_g_value_26`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_26`'.format(value))

        self._data["G-Function G Value 26"] = value

    @property
    def gfunction_lnt_or_ts_value_27(self):
        """Get gfunction_lnt_or_ts_value_27

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_27` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 27"]

    @gfunction_lnt_or_ts_value_27.setter
    def gfunction_lnt_or_ts_value_27(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_27`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_27`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 27"] = value

    @property
    def gfunction_g_value_27(self):
        """Get gfunction_g_value_27

        Returns:
            float: the value of `gfunction_g_value_27` or None if not set
        """
        return self._data["G-Function G Value 27"]

    @gfunction_g_value_27.setter
    def gfunction_g_value_27(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_27`

        Args:
            value (float): value for IDD Field `gfunction_g_value_27`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_27`'.format(value))

        self._data["G-Function G Value 27"] = value

    @property
    def gfunction_lnt_or_ts_value_28(self):
        """Get gfunction_lnt_or_ts_value_28

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_28` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 28"]

    @gfunction_lnt_or_ts_value_28.setter
    def gfunction_lnt_or_ts_value_28(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_28`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_28`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 28"] = value

    @property
    def gfunction_g_value_28(self):
        """Get gfunction_g_value_28

        Returns:
            float: the value of `gfunction_g_value_28` or None if not set
        """
        return self._data["G-Function G Value 28"]

    @gfunction_g_value_28.setter
    def gfunction_g_value_28(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_28`

        Args:
            value (float): value for IDD Field `gfunction_g_value_28`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_28`'.format(value))

        self._data["G-Function G Value 28"] = value

    @property
    def gfunction_lnt_or_ts_value_29(self):
        """Get gfunction_lnt_or_ts_value_29

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_29` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 29"]

    @gfunction_lnt_or_ts_value_29.setter
    def gfunction_lnt_or_ts_value_29(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_29`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_29`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 29"] = value

    @property
    def gfunction_g_value_29(self):
        """Get gfunction_g_value_29

        Returns:
            float: the value of `gfunction_g_value_29` or None if not set
        """
        return self._data["G-Function G Value 29"]

    @gfunction_g_value_29.setter
    def gfunction_g_value_29(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_29`

        Args:
            value (float): value for IDD Field `gfunction_g_value_29`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_29`'.format(value))

        self._data["G-Function G Value 29"] = value

    @property
    def gfunction_lnt_or_ts_value_30(self):
        """Get gfunction_lnt_or_ts_value_30

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_30` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 30"]

    @gfunction_lnt_or_ts_value_30.setter
    def gfunction_lnt_or_ts_value_30(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_30`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_30`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 30"] = value

    @property
    def gfunction_g_value_30(self):
        """Get gfunction_g_value_30

        Returns:
            float: the value of `gfunction_g_value_30` or None if not set
        """
        return self._data["G-Function G Value 30"]

    @gfunction_g_value_30.setter
    def gfunction_g_value_30(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_30`

        Args:
            value (float): value for IDD Field `gfunction_g_value_30`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_30`'.format(value))

        self._data["G-Function G Value 30"] = value

    @property
    def gfunction_lnt_or_ts_value_31(self):
        """Get gfunction_lnt_or_ts_value_31

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_31` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 31"]

    @gfunction_lnt_or_ts_value_31.setter
    def gfunction_lnt_or_ts_value_31(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_31`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_31`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 31"] = value

    @property
    def gfunction_g_value_31(self):
        """Get gfunction_g_value_31

        Returns:
            float: the value of `gfunction_g_value_31` or None if not set
        """
        return self._data["G-Function G Value 31"]

    @gfunction_g_value_31.setter
    def gfunction_g_value_31(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_31`

        Args:
            value (float): value for IDD Field `gfunction_g_value_31`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_31`'.format(value))

        self._data["G-Function G Value 31"] = value

    @property
    def gfunction_lnt_or_ts_value_32(self):
        """Get gfunction_lnt_or_ts_value_32

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_32` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 32"]

    @gfunction_lnt_or_ts_value_32.setter
    def gfunction_lnt_or_ts_value_32(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_32`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_32`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 32"] = value

    @property
    def gfunction_g_value_32(self):
        """Get gfunction_g_value_32

        Returns:
            float: the value of `gfunction_g_value_32` or None if not set
        """
        return self._data["G-Function G Value 32"]

    @gfunction_g_value_32.setter
    def gfunction_g_value_32(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_32`

        Args:
            value (float): value for IDD Field `gfunction_g_value_32`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_32`'.format(value))

        self._data["G-Function G Value 32"] = value

    @property
    def gfunction_lnt_or_ts_value_33(self):
        """Get gfunction_lnt_or_ts_value_33

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_33` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 33"]

    @gfunction_lnt_or_ts_value_33.setter
    def gfunction_lnt_or_ts_value_33(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_33`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_33`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 33"] = value

    @property
    def gfunction_g_value_33(self):
        """Get gfunction_g_value_33

        Returns:
            float: the value of `gfunction_g_value_33` or None if not set
        """
        return self._data["G-Function G Value 33"]

    @gfunction_g_value_33.setter
    def gfunction_g_value_33(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_33`

        Args:
            value (float): value for IDD Field `gfunction_g_value_33`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_33`'.format(value))

        self._data["G-Function G Value 33"] = value

    @property
    def gfunction_lnt_or_ts_value_34(self):
        """Get gfunction_lnt_or_ts_value_34

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_34` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 34"]

    @gfunction_lnt_or_ts_value_34.setter
    def gfunction_lnt_or_ts_value_34(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_34`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_34`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 34"] = value

    @property
    def gfunction_g_value_34(self):
        """Get gfunction_g_value_34

        Returns:
            float: the value of `gfunction_g_value_34` or None if not set
        """
        return self._data["G-Function G Value 34"]

    @gfunction_g_value_34.setter
    def gfunction_g_value_34(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_34`

        Args:
            value (float): value for IDD Field `gfunction_g_value_34`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_34`'.format(value))

        self._data["G-Function G Value 34"] = value

    @property
    def gfunction_lnt_or_ts_value_35(self):
        """Get gfunction_lnt_or_ts_value_35

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_35` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 35"]

    @gfunction_lnt_or_ts_value_35.setter
    def gfunction_lnt_or_ts_value_35(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_35`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_35`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 35"] = value

    @property
    def gfunction_g_value_35(self):
        """Get gfunction_g_value_35

        Returns:
            float: the value of `gfunction_g_value_35` or None if not set
        """
        return self._data["G-Function G Value 35"]

    @gfunction_g_value_35.setter
    def gfunction_g_value_35(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_35`

        Args:
            value (float): value for IDD Field `gfunction_g_value_35`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_35`'.format(value))

        self._data["G-Function G Value 35"] = value

    @property
    def gfunction_lnt_or_ts_value_36(self):
        """Get gfunction_lnt_or_ts_value_36

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_36` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 36"]

    @gfunction_lnt_or_ts_value_36.setter
    def gfunction_lnt_or_ts_value_36(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_36`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_36`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 36"] = value

    @property
    def gfunction_g_value_36(self):
        """Get gfunction_g_value_36

        Returns:
            float: the value of `gfunction_g_value_36` or None if not set
        """
        return self._data["G-Function G Value 36"]

    @gfunction_g_value_36.setter
    def gfunction_g_value_36(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_36`

        Args:
            value (float): value for IDD Field `gfunction_g_value_36`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_36`'.format(value))

        self._data["G-Function G Value 36"] = value

    @property
    def gfunction_lnt_or_ts_value_37(self):
        """Get gfunction_lnt_or_ts_value_37

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_37` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 37"]

    @gfunction_lnt_or_ts_value_37.setter
    def gfunction_lnt_or_ts_value_37(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_37`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_37`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 37"] = value

    @property
    def gfunction_g_value_37(self):
        """Get gfunction_g_value_37

        Returns:
            float: the value of `gfunction_g_value_37` or None if not set
        """
        return self._data["G-Function G Value 37"]

    @gfunction_g_value_37.setter
    def gfunction_g_value_37(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_37`

        Args:
            value (float): value for IDD Field `gfunction_g_value_37`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_37`'.format(value))

        self._data["G-Function G Value 37"] = value

    @property
    def gfunction_lnt_or_ts_value_38(self):
        """Get gfunction_lnt_or_ts_value_38

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_38` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 38"]

    @gfunction_lnt_or_ts_value_38.setter
    def gfunction_lnt_or_ts_value_38(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_38`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_38`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 38"] = value

    @property
    def gfunction_g_value_38(self):
        """Get gfunction_g_value_38

        Returns:
            float: the value of `gfunction_g_value_38` or None if not set
        """
        return self._data["G-Function G Value 38"]

    @gfunction_g_value_38.setter
    def gfunction_g_value_38(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_38`

        Args:
            value (float): value for IDD Field `gfunction_g_value_38`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_38`'.format(value))

        self._data["G-Function G Value 38"] = value

    @property
    def gfunction_lnt_or_ts_value_39(self):
        """Get gfunction_lnt_or_ts_value_39

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_39` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 39"]

    @gfunction_lnt_or_ts_value_39.setter
    def gfunction_lnt_or_ts_value_39(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_39`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_39`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 39"] = value

    @property
    def gfunction_g_value_39(self):
        """Get gfunction_g_value_39

        Returns:
            float: the value of `gfunction_g_value_39` or None if not set
        """
        return self._data["G-Function G Value 39"]

    @gfunction_g_value_39.setter
    def gfunction_g_value_39(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_39`

        Args:
            value (float): value for IDD Field `gfunction_g_value_39`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_39`'.format(value))

        self._data["G-Function G Value 39"] = value

    @property
    def gfunction_lnt_or_ts_value_40(self):
        """Get gfunction_lnt_or_ts_value_40

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_40` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 40"]

    @gfunction_lnt_or_ts_value_40.setter
    def gfunction_lnt_or_ts_value_40(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_40`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_40`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 40"] = value

    @property
    def gfunction_g_value_40(self):
        """Get gfunction_g_value_40

        Returns:
            float: the value of `gfunction_g_value_40` or None if not set
        """
        return self._data["G-Function G Value 40"]

    @gfunction_g_value_40.setter
    def gfunction_g_value_40(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_40`

        Args:
            value (float): value for IDD Field `gfunction_g_value_40`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_40`'.format(value))

        self._data["G-Function G Value 40"] = value

    @property
    def gfunction_lnt_or_ts_value_41(self):
        """Get gfunction_lnt_or_ts_value_41

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_41` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 41"]

    @gfunction_lnt_or_ts_value_41.setter
    def gfunction_lnt_or_ts_value_41(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_41`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_41`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 41"] = value

    @property
    def gfunction_g_value_41(self):
        """Get gfunction_g_value_41

        Returns:
            float: the value of `gfunction_g_value_41` or None if not set
        """
        return self._data["G-Function G Value 41"]

    @gfunction_g_value_41.setter
    def gfunction_g_value_41(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_41`

        Args:
            value (float): value for IDD Field `gfunction_g_value_41`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_41`'.format(value))

        self._data["G-Function G Value 41"] = value

    @property
    def gfunction_lnt_or_ts_value_42(self):
        """Get gfunction_lnt_or_ts_value_42

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_42` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 42"]

    @gfunction_lnt_or_ts_value_42.setter
    def gfunction_lnt_or_ts_value_42(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_42`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_42`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 42"] = value

    @property
    def gfunction_g_value_42(self):
        """Get gfunction_g_value_42

        Returns:
            float: the value of `gfunction_g_value_42` or None if not set
        """
        return self._data["G-Function G Value 42"]

    @gfunction_g_value_42.setter
    def gfunction_g_value_42(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_42`

        Args:
            value (float): value for IDD Field `gfunction_g_value_42`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_42`'.format(value))

        self._data["G-Function G Value 42"] = value

    @property
    def gfunction_lnt_or_ts_value_43(self):
        """Get gfunction_lnt_or_ts_value_43

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_43` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 43"]

    @gfunction_lnt_or_ts_value_43.setter
    def gfunction_lnt_or_ts_value_43(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_43`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_43`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 43"] = value

    @property
    def gfunction_g_value_43(self):
        """Get gfunction_g_value_43

        Returns:
            float: the value of `gfunction_g_value_43` or None if not set
        """
        return self._data["G-Function G Value 43"]

    @gfunction_g_value_43.setter
    def gfunction_g_value_43(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_43`

        Args:
            value (float): value for IDD Field `gfunction_g_value_43`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_43`'.format(value))

        self._data["G-Function G Value 43"] = value

    @property
    def gfunction_lnt_or_ts_value_44(self):
        """Get gfunction_lnt_or_ts_value_44

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_44` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 44"]

    @gfunction_lnt_or_ts_value_44.setter
    def gfunction_lnt_or_ts_value_44(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_44`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_44`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 44"] = value

    @property
    def gfunction_g_value_44(self):
        """Get gfunction_g_value_44

        Returns:
            float: the value of `gfunction_g_value_44` or None if not set
        """
        return self._data["G-Function G Value 44"]

    @gfunction_g_value_44.setter
    def gfunction_g_value_44(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_44`

        Args:
            value (float): value for IDD Field `gfunction_g_value_44`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_44`'.format(value))

        self._data["G-Function G Value 44"] = value

    @property
    def gfunction_lnt_or_ts_value_45(self):
        """Get gfunction_lnt_or_ts_value_45

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_45` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 45"]

    @gfunction_lnt_or_ts_value_45.setter
    def gfunction_lnt_or_ts_value_45(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_45`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_45`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 45"] = value

    @property
    def gfunction_g_value_45(self):
        """Get gfunction_g_value_45

        Returns:
            float: the value of `gfunction_g_value_45` or None if not set
        """
        return self._data["G-Function G Value 45"]

    @gfunction_g_value_45.setter
    def gfunction_g_value_45(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_45`

        Args:
            value (float): value for IDD Field `gfunction_g_value_45`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_45`'.format(value))

        self._data["G-Function G Value 45"] = value

    @property
    def gfunction_lnt_or_ts_value_46(self):
        """Get gfunction_lnt_or_ts_value_46

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_46` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 46"]

    @gfunction_lnt_or_ts_value_46.setter
    def gfunction_lnt_or_ts_value_46(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_46`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_46`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 46"] = value

    @property
    def gfunction_g_value_46(self):
        """Get gfunction_g_value_46

        Returns:
            float: the value of `gfunction_g_value_46` or None if not set
        """
        return self._data["G-Function G Value 46"]

    @gfunction_g_value_46.setter
    def gfunction_g_value_46(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_46`

        Args:
            value (float): value for IDD Field `gfunction_g_value_46`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_46`'.format(value))

        self._data["G-Function G Value 46"] = value

    @property
    def gfunction_lnt_or_ts_value_47(self):
        """Get gfunction_lnt_or_ts_value_47

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_47` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 47"]

    @gfunction_lnt_or_ts_value_47.setter
    def gfunction_lnt_or_ts_value_47(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_47`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_47`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 47"] = value

    @property
    def gfunction_g_value_47(self):
        """Get gfunction_g_value_47

        Returns:
            float: the value of `gfunction_g_value_47` or None if not set
        """
        return self._data["G-Function G Value 47"]

    @gfunction_g_value_47.setter
    def gfunction_g_value_47(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_47`

        Args:
            value (float): value for IDD Field `gfunction_g_value_47`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_47`'.format(value))

        self._data["G-Function G Value 47"] = value

    @property
    def gfunction_lnt_or_ts_value_48(self):
        """Get gfunction_lnt_or_ts_value_48

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_48` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 48"]

    @gfunction_lnt_or_ts_value_48.setter
    def gfunction_lnt_or_ts_value_48(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_48`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_48`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 48"] = value

    @property
    def gfunction_g_value_48(self):
        """Get gfunction_g_value_48

        Returns:
            float: the value of `gfunction_g_value_48` or None if not set
        """
        return self._data["G-Function G Value 48"]

    @gfunction_g_value_48.setter
    def gfunction_g_value_48(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_48`

        Args:
            value (float): value for IDD Field `gfunction_g_value_48`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_48`'.format(value))

        self._data["G-Function G Value 48"] = value

    @property
    def gfunction_lnt_or_ts_value_49(self):
        """Get gfunction_lnt_or_ts_value_49

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_49` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 49"]

    @gfunction_lnt_or_ts_value_49.setter
    def gfunction_lnt_or_ts_value_49(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_49`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_49`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 49"] = value

    @property
    def gfunction_g_value_49(self):
        """Get gfunction_g_value_49

        Returns:
            float: the value of `gfunction_g_value_49` or None if not set
        """
        return self._data["G-Function G Value 49"]

    @gfunction_g_value_49.setter
    def gfunction_g_value_49(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_49`

        Args:
            value (float): value for IDD Field `gfunction_g_value_49`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_49`'.format(value))

        self._data["G-Function G Value 49"] = value

    @property
    def gfunction_lnt_or_ts_value_50(self):
        """Get gfunction_lnt_or_ts_value_50

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_50` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 50"]

    @gfunction_lnt_or_ts_value_50.setter
    def gfunction_lnt_or_ts_value_50(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_50`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_50`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 50"] = value

    @property
    def gfunction_g_value_50(self):
        """Get gfunction_g_value_50

        Returns:
            float: the value of `gfunction_g_value_50` or None if not set
        """
        return self._data["G-Function G Value 50"]

    @gfunction_g_value_50.setter
    def gfunction_g_value_50(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_50`

        Args:
            value (float): value for IDD Field `gfunction_g_value_50`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_50`'.format(value))

        self._data["G-Function G Value 50"] = value

    @property
    def gfunction_lnt_or_ts_value_51(self):
        """Get gfunction_lnt_or_ts_value_51

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_51` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 51"]

    @gfunction_lnt_or_ts_value_51.setter
    def gfunction_lnt_or_ts_value_51(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_51`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_51`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 51"] = value

    @property
    def gfunction_g_value_51(self):
        """Get gfunction_g_value_51

        Returns:
            float: the value of `gfunction_g_value_51` or None if not set
        """
        return self._data["G-Function G Value 51"]

    @gfunction_g_value_51.setter
    def gfunction_g_value_51(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_51`

        Args:
            value (float): value for IDD Field `gfunction_g_value_51`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_51`'.format(value))

        self._data["G-Function G Value 51"] = value

    @property
    def gfunction_lnt_or_ts_value_52(self):
        """Get gfunction_lnt_or_ts_value_52

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_52` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 52"]

    @gfunction_lnt_or_ts_value_52.setter
    def gfunction_lnt_or_ts_value_52(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_52`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_52`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 52"] = value

    @property
    def gfunction_g_value_52(self):
        """Get gfunction_g_value_52

        Returns:
            float: the value of `gfunction_g_value_52` or None if not set
        """
        return self._data["G-Function G Value 52"]

    @gfunction_g_value_52.setter
    def gfunction_g_value_52(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_52`

        Args:
            value (float): value for IDD Field `gfunction_g_value_52`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_52`'.format(value))

        self._data["G-Function G Value 52"] = value

    @property
    def gfunction_lnt_or_ts_value_53(self):
        """Get gfunction_lnt_or_ts_value_53

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_53` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 53"]

    @gfunction_lnt_or_ts_value_53.setter
    def gfunction_lnt_or_ts_value_53(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_53`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_53`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 53"] = value

    @property
    def gfunction_g_value_53(self):
        """Get gfunction_g_value_53

        Returns:
            float: the value of `gfunction_g_value_53` or None if not set
        """
        return self._data["G-Function G Value 53"]

    @gfunction_g_value_53.setter
    def gfunction_g_value_53(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_53`

        Args:
            value (float): value for IDD Field `gfunction_g_value_53`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_53`'.format(value))

        self._data["G-Function G Value 53"] = value

    @property
    def gfunction_lnt_or_ts_value_54(self):
        """Get gfunction_lnt_or_ts_value_54

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_54` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 54"]

    @gfunction_lnt_or_ts_value_54.setter
    def gfunction_lnt_or_ts_value_54(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_54`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_54`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 54"] = value

    @property
    def gfunction_g_value_54(self):
        """Get gfunction_g_value_54

        Returns:
            float: the value of `gfunction_g_value_54` or None if not set
        """
        return self._data["G-Function G Value 54"]

    @gfunction_g_value_54.setter
    def gfunction_g_value_54(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_54`

        Args:
            value (float): value for IDD Field `gfunction_g_value_54`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_54`'.format(value))

        self._data["G-Function G Value 54"] = value

    @property
    def gfunction_lnt_or_ts_value_55(self):
        """Get gfunction_lnt_or_ts_value_55

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_55` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 55"]

    @gfunction_lnt_or_ts_value_55.setter
    def gfunction_lnt_or_ts_value_55(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_55`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_55`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 55"] = value

    @property
    def gfunction_g_value_55(self):
        """Get gfunction_g_value_55

        Returns:
            float: the value of `gfunction_g_value_55` or None if not set
        """
        return self._data["G-Function G Value 55"]

    @gfunction_g_value_55.setter
    def gfunction_g_value_55(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_55`

        Args:
            value (float): value for IDD Field `gfunction_g_value_55`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_55`'.format(value))

        self._data["G-Function G Value 55"] = value

    @property
    def gfunction_lnt_or_ts_value_56(self):
        """Get gfunction_lnt_or_ts_value_56

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_56` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 56"]

    @gfunction_lnt_or_ts_value_56.setter
    def gfunction_lnt_or_ts_value_56(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_56`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_56`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 56"] = value

    @property
    def gfunction_g_value_56(self):
        """Get gfunction_g_value_56

        Returns:
            float: the value of `gfunction_g_value_56` or None if not set
        """
        return self._data["G-Function G Value 56"]

    @gfunction_g_value_56.setter
    def gfunction_g_value_56(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_56`

        Args:
            value (float): value for IDD Field `gfunction_g_value_56`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_56`'.format(value))

        self._data["G-Function G Value 56"] = value

    @property
    def gfunction_lnt_or_ts_value_57(self):
        """Get gfunction_lnt_or_ts_value_57

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_57` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 57"]

    @gfunction_lnt_or_ts_value_57.setter
    def gfunction_lnt_or_ts_value_57(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_57`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_57`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 57"] = value

    @property
    def gfunction_g_value_57(self):
        """Get gfunction_g_value_57

        Returns:
            float: the value of `gfunction_g_value_57` or None if not set
        """
        return self._data["G-Function G Value 57"]

    @gfunction_g_value_57.setter
    def gfunction_g_value_57(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_57`

        Args:
            value (float): value for IDD Field `gfunction_g_value_57`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_57`'.format(value))

        self._data["G-Function G Value 57"] = value

    @property
    def gfunction_lnt_or_ts_value_58(self):
        """Get gfunction_lnt_or_ts_value_58

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_58` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 58"]

    @gfunction_lnt_or_ts_value_58.setter
    def gfunction_lnt_or_ts_value_58(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_58`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_58`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 58"] = value

    @property
    def gfunction_g_value_58(self):
        """Get gfunction_g_value_58

        Returns:
            float: the value of `gfunction_g_value_58` or None if not set
        """
        return self._data["G-Function G Value 58"]

    @gfunction_g_value_58.setter
    def gfunction_g_value_58(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_58`

        Args:
            value (float): value for IDD Field `gfunction_g_value_58`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_58`'.format(value))

        self._data["G-Function G Value 58"] = value

    @property
    def gfunction_lnt_or_ts_value_59(self):
        """Get gfunction_lnt_or_ts_value_59

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_59` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 59"]

    @gfunction_lnt_or_ts_value_59.setter
    def gfunction_lnt_or_ts_value_59(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_59`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_59`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 59"] = value

    @property
    def gfunction_g_value_59(self):
        """Get gfunction_g_value_59

        Returns:
            float: the value of `gfunction_g_value_59` or None if not set
        """
        return self._data["G-Function G Value 59"]

    @gfunction_g_value_59.setter
    def gfunction_g_value_59(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_59`

        Args:
            value (float): value for IDD Field `gfunction_g_value_59`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_59`'.format(value))

        self._data["G-Function G Value 59"] = value

    @property
    def gfunction_lnt_or_ts_value_60(self):
        """Get gfunction_lnt_or_ts_value_60

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_60` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 60"]

    @gfunction_lnt_or_ts_value_60.setter
    def gfunction_lnt_or_ts_value_60(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_60`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_60`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 60"] = value

    @property
    def gfunction_g_value_60(self):
        """Get gfunction_g_value_60

        Returns:
            float: the value of `gfunction_g_value_60` or None if not set
        """
        return self._data["G-Function G Value 60"]

    @gfunction_g_value_60.setter
    def gfunction_g_value_60(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_60`

        Args:
            value (float): value for IDD Field `gfunction_g_value_60`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_60`'.format(value))

        self._data["G-Function G Value 60"] = value

    @property
    def gfunction_lnt_or_ts_value_61(self):
        """Get gfunction_lnt_or_ts_value_61

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_61` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 61"]

    @gfunction_lnt_or_ts_value_61.setter
    def gfunction_lnt_or_ts_value_61(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_61`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_61`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 61"] = value

    @property
    def gfunction_g_value_61(self):
        """Get gfunction_g_value_61

        Returns:
            float: the value of `gfunction_g_value_61` or None if not set
        """
        return self._data["G-Function G Value 61"]

    @gfunction_g_value_61.setter
    def gfunction_g_value_61(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_61`

        Args:
            value (float): value for IDD Field `gfunction_g_value_61`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_61`'.format(value))

        self._data["G-Function G Value 61"] = value

    @property
    def gfunction_lnt_or_ts_value_62(self):
        """Get gfunction_lnt_or_ts_value_62

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_62` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 62"]

    @gfunction_lnt_or_ts_value_62.setter
    def gfunction_lnt_or_ts_value_62(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_62`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_62`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 62"] = value

    @property
    def gfunction_g_value_62(self):
        """Get gfunction_g_value_62

        Returns:
            float: the value of `gfunction_g_value_62` or None if not set
        """
        return self._data["G-Function G Value 62"]

    @gfunction_g_value_62.setter
    def gfunction_g_value_62(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_62`

        Args:
            value (float): value for IDD Field `gfunction_g_value_62`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_62`'.format(value))

        self._data["G-Function G Value 62"] = value

    @property
    def gfunction_lnt_or_ts_value_63(self):
        """Get gfunction_lnt_or_ts_value_63

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_63` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 63"]

    @gfunction_lnt_or_ts_value_63.setter
    def gfunction_lnt_or_ts_value_63(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_63`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_63`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 63"] = value

    @property
    def gfunction_g_value_63(self):
        """Get gfunction_g_value_63

        Returns:
            float: the value of `gfunction_g_value_63` or None if not set
        """
        return self._data["G-Function G Value 63"]

    @gfunction_g_value_63.setter
    def gfunction_g_value_63(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_63`

        Args:
            value (float): value for IDD Field `gfunction_g_value_63`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_63`'.format(value))

        self._data["G-Function G Value 63"] = value

    @property
    def gfunction_lnt_or_ts_value_64(self):
        """Get gfunction_lnt_or_ts_value_64

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_64` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 64"]

    @gfunction_lnt_or_ts_value_64.setter
    def gfunction_lnt_or_ts_value_64(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_64`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_64`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 64"] = value

    @property
    def gfunction_g_value_64(self):
        """Get gfunction_g_value_64

        Returns:
            float: the value of `gfunction_g_value_64` or None if not set
        """
        return self._data["G-Function G Value 64"]

    @gfunction_g_value_64.setter
    def gfunction_g_value_64(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_64`

        Args:
            value (float): value for IDD Field `gfunction_g_value_64`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_64`'.format(value))

        self._data["G-Function G Value 64"] = value

    @property
    def gfunction_lnt_or_ts_value_65(self):
        """Get gfunction_lnt_or_ts_value_65

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_65` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 65"]

    @gfunction_lnt_or_ts_value_65.setter
    def gfunction_lnt_or_ts_value_65(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_65`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_65`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 65"] = value

    @property
    def gfunction_g_value_65(self):
        """Get gfunction_g_value_65

        Returns:
            float: the value of `gfunction_g_value_65` or None if not set
        """
        return self._data["G-Function G Value 65"]

    @gfunction_g_value_65.setter
    def gfunction_g_value_65(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_65`

        Args:
            value (float): value for IDD Field `gfunction_g_value_65`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_65`'.format(value))

        self._data["G-Function G Value 65"] = value

    @property
    def gfunction_lnt_or_ts_value_66(self):
        """Get gfunction_lnt_or_ts_value_66

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_66` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 66"]

    @gfunction_lnt_or_ts_value_66.setter
    def gfunction_lnt_or_ts_value_66(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_66`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_66`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 66"] = value

    @property
    def gfunction_g_value_66(self):
        """Get gfunction_g_value_66

        Returns:
            float: the value of `gfunction_g_value_66` or None if not set
        """
        return self._data["G-Function G Value 66"]

    @gfunction_g_value_66.setter
    def gfunction_g_value_66(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_66`

        Args:
            value (float): value for IDD Field `gfunction_g_value_66`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_66`'.format(value))

        self._data["G-Function G Value 66"] = value

    @property
    def gfunction_lnt_or_ts_value_67(self):
        """Get gfunction_lnt_or_ts_value_67

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_67` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 67"]

    @gfunction_lnt_or_ts_value_67.setter
    def gfunction_lnt_or_ts_value_67(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_67`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_67`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 67"] = value

    @property
    def gfunction_g_value_67(self):
        """Get gfunction_g_value_67

        Returns:
            float: the value of `gfunction_g_value_67` or None if not set
        """
        return self._data["G-Function G Value 67"]

    @gfunction_g_value_67.setter
    def gfunction_g_value_67(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_67`

        Args:
            value (float): value for IDD Field `gfunction_g_value_67`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_67`'.format(value))

        self._data["G-Function G Value 67"] = value

    @property
    def gfunction_lnt_or_ts_value_68(self):
        """Get gfunction_lnt_or_ts_value_68

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_68` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 68"]

    @gfunction_lnt_or_ts_value_68.setter
    def gfunction_lnt_or_ts_value_68(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_68`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_68`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 68"] = value

    @property
    def gfunction_g_value_68(self):
        """Get gfunction_g_value_68

        Returns:
            float: the value of `gfunction_g_value_68` or None if not set
        """
        return self._data["G-Function G Value 68"]

    @gfunction_g_value_68.setter
    def gfunction_g_value_68(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_68`

        Args:
            value (float): value for IDD Field `gfunction_g_value_68`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_68`'.format(value))

        self._data["G-Function G Value 68"] = value

    @property
    def gfunction_lnt_or_ts_value_69(self):
        """Get gfunction_lnt_or_ts_value_69

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_69` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 69"]

    @gfunction_lnt_or_ts_value_69.setter
    def gfunction_lnt_or_ts_value_69(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_69`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_69`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 69"] = value

    @property
    def gfunction_g_value_69(self):
        """Get gfunction_g_value_69

        Returns:
            float: the value of `gfunction_g_value_69` or None if not set
        """
        return self._data["G-Function G Value 69"]

    @gfunction_g_value_69.setter
    def gfunction_g_value_69(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_69`

        Args:
            value (float): value for IDD Field `gfunction_g_value_69`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_69`'.format(value))

        self._data["G-Function G Value 69"] = value

    @property
    def gfunction_lnt_or_ts_value_70(self):
        """Get gfunction_lnt_or_ts_value_70

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_70` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 70"]

    @gfunction_lnt_or_ts_value_70.setter
    def gfunction_lnt_or_ts_value_70(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_70`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_70`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 70"] = value

    @property
    def gfunction_g_value_70(self):
        """Get gfunction_g_value_70

        Returns:
            float: the value of `gfunction_g_value_70` or None if not set
        """
        return self._data["G-Function G Value 70"]

    @gfunction_g_value_70.setter
    def gfunction_g_value_70(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_70`

        Args:
            value (float): value for IDD Field `gfunction_g_value_70`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_70`'.format(value))

        self._data["G-Function G Value 70"] = value

    @property
    def gfunction_lnt_or_ts_value_71(self):
        """Get gfunction_lnt_or_ts_value_71

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_71` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 71"]

    @gfunction_lnt_or_ts_value_71.setter
    def gfunction_lnt_or_ts_value_71(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_71`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_71`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 71"] = value

    @property
    def gfunction_g_value_71(self):
        """Get gfunction_g_value_71

        Returns:
            float: the value of `gfunction_g_value_71` or None if not set
        """
        return self._data["G-Function G Value 71"]

    @gfunction_g_value_71.setter
    def gfunction_g_value_71(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_71`

        Args:
            value (float): value for IDD Field `gfunction_g_value_71`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_71`'.format(value))

        self._data["G-Function G Value 71"] = value

    @property
    def gfunction_lnt_or_ts_value_72(self):
        """Get gfunction_lnt_or_ts_value_72

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_72` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 72"]

    @gfunction_lnt_or_ts_value_72.setter
    def gfunction_lnt_or_ts_value_72(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_72`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_72`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 72"] = value

    @property
    def gfunction_g_value_72(self):
        """Get gfunction_g_value_72

        Returns:
            float: the value of `gfunction_g_value_72` or None if not set
        """
        return self._data["G-Function G Value 72"]

    @gfunction_g_value_72.setter
    def gfunction_g_value_72(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_72`

        Args:
            value (float): value for IDD Field `gfunction_g_value_72`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_72`'.format(value))

        self._data["G-Function G Value 72"] = value

    @property
    def gfunction_lnt_or_ts_value_73(self):
        """Get gfunction_lnt_or_ts_value_73

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_73` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 73"]

    @gfunction_lnt_or_ts_value_73.setter
    def gfunction_lnt_or_ts_value_73(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_73`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_73`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 73"] = value

    @property
    def gfunction_g_value_73(self):
        """Get gfunction_g_value_73

        Returns:
            float: the value of `gfunction_g_value_73` or None if not set
        """
        return self._data["G-Function G Value 73"]

    @gfunction_g_value_73.setter
    def gfunction_g_value_73(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_73`

        Args:
            value (float): value for IDD Field `gfunction_g_value_73`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_73`'.format(value))

        self._data["G-Function G Value 73"] = value

    @property
    def gfunction_lnt_or_ts_value_74(self):
        """Get gfunction_lnt_or_ts_value_74

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_74` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 74"]

    @gfunction_lnt_or_ts_value_74.setter
    def gfunction_lnt_or_ts_value_74(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_74`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_74`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 74"] = value

    @property
    def gfunction_g_value_74(self):
        """Get gfunction_g_value_74

        Returns:
            float: the value of `gfunction_g_value_74` or None if not set
        """
        return self._data["G-Function G Value 74"]

    @gfunction_g_value_74.setter
    def gfunction_g_value_74(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_74`

        Args:
            value (float): value for IDD Field `gfunction_g_value_74`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_74`'.format(value))

        self._data["G-Function G Value 74"] = value

    @property
    def gfunction_lnt_or_ts_value_75(self):
        """Get gfunction_lnt_or_ts_value_75

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_75` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 75"]

    @gfunction_lnt_or_ts_value_75.setter
    def gfunction_lnt_or_ts_value_75(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_75`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_75`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 75"] = value

    @property
    def gfunction_g_value_75(self):
        """Get gfunction_g_value_75

        Returns:
            float: the value of `gfunction_g_value_75` or None if not set
        """
        return self._data["G-Function G Value 75"]

    @gfunction_g_value_75.setter
    def gfunction_g_value_75(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_75`

        Args:
            value (float): value for IDD Field `gfunction_g_value_75`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_75`'.format(value))

        self._data["G-Function G Value 75"] = value

    @property
    def gfunction_lnt_or_ts_value_76(self):
        """Get gfunction_lnt_or_ts_value_76

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_76` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 76"]

    @gfunction_lnt_or_ts_value_76.setter
    def gfunction_lnt_or_ts_value_76(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_76`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_76`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 76"] = value

    @property
    def gfunction_g_value_76(self):
        """Get gfunction_g_value_76

        Returns:
            float: the value of `gfunction_g_value_76` or None if not set
        """
        return self._data["G-Function G Value 76"]

    @gfunction_g_value_76.setter
    def gfunction_g_value_76(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_76`

        Args:
            value (float): value for IDD Field `gfunction_g_value_76`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_76`'.format(value))

        self._data["G-Function G Value 76"] = value

    @property
    def gfunction_lnt_or_ts_value_77(self):
        """Get gfunction_lnt_or_ts_value_77

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_77` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 77"]

    @gfunction_lnt_or_ts_value_77.setter
    def gfunction_lnt_or_ts_value_77(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_77`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_77`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 77"] = value

    @property
    def gfunction_g_value_77(self):
        """Get gfunction_g_value_77

        Returns:
            float: the value of `gfunction_g_value_77` or None if not set
        """
        return self._data["G-Function G Value 77"]

    @gfunction_g_value_77.setter
    def gfunction_g_value_77(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_77`

        Args:
            value (float): value for IDD Field `gfunction_g_value_77`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_77`'.format(value))

        self._data["G-Function G Value 77"] = value

    @property
    def gfunction_lnt_or_ts_value_78(self):
        """Get gfunction_lnt_or_ts_value_78

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_78` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 78"]

    @gfunction_lnt_or_ts_value_78.setter
    def gfunction_lnt_or_ts_value_78(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_78`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_78`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 78"] = value

    @property
    def gfunction_g_value_78(self):
        """Get gfunction_g_value_78

        Returns:
            float: the value of `gfunction_g_value_78` or None if not set
        """
        return self._data["G-Function G Value 78"]

    @gfunction_g_value_78.setter
    def gfunction_g_value_78(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_78`

        Args:
            value (float): value for IDD Field `gfunction_g_value_78`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_78`'.format(value))

        self._data["G-Function G Value 78"] = value

    @property
    def gfunction_lnt_or_ts_value_79(self):
        """Get gfunction_lnt_or_ts_value_79

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_79` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 79"]

    @gfunction_lnt_or_ts_value_79.setter
    def gfunction_lnt_or_ts_value_79(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_79`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_79`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 79"] = value

    @property
    def gfunction_g_value_79(self):
        """Get gfunction_g_value_79

        Returns:
            float: the value of `gfunction_g_value_79` or None if not set
        """
        return self._data["G-Function G Value 79"]

    @gfunction_g_value_79.setter
    def gfunction_g_value_79(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_79`

        Args:
            value (float): value for IDD Field `gfunction_g_value_79`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_79`'.format(value))

        self._data["G-Function G Value 79"] = value

    @property
    def gfunction_lnt_or_ts_value_80(self):
        """Get gfunction_lnt_or_ts_value_80

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_80` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 80"]

    @gfunction_lnt_or_ts_value_80.setter
    def gfunction_lnt_or_ts_value_80(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_80`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_80`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 80"] = value

    @property
    def gfunction_g_value_80(self):
        """Get gfunction_g_value_80

        Returns:
            float: the value of `gfunction_g_value_80` or None if not set
        """
        return self._data["G-Function G Value 80"]

    @gfunction_g_value_80.setter
    def gfunction_g_value_80(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_80`

        Args:
            value (float): value for IDD Field `gfunction_g_value_80`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_80`'.format(value))

        self._data["G-Function G Value 80"] = value

    @property
    def gfunction_lnt_or_ts_value_81(self):
        """Get gfunction_lnt_or_ts_value_81

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_81` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 81"]

    @gfunction_lnt_or_ts_value_81.setter
    def gfunction_lnt_or_ts_value_81(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_81`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_81`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 81"] = value

    @property
    def gfunction_g_value_81(self):
        """Get gfunction_g_value_81

        Returns:
            float: the value of `gfunction_g_value_81` or None if not set
        """
        return self._data["G-Function G Value 81"]

    @gfunction_g_value_81.setter
    def gfunction_g_value_81(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_81`

        Args:
            value (float): value for IDD Field `gfunction_g_value_81`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_81`'.format(value))

        self._data["G-Function G Value 81"] = value

    @property
    def gfunction_lnt_or_ts_value_82(self):
        """Get gfunction_lnt_or_ts_value_82

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_82` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 82"]

    @gfunction_lnt_or_ts_value_82.setter
    def gfunction_lnt_or_ts_value_82(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_82`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_82`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 82"] = value

    @property
    def gfunction_g_value_82(self):
        """Get gfunction_g_value_82

        Returns:
            float: the value of `gfunction_g_value_82` or None if not set
        """
        return self._data["G-Function G Value 82"]

    @gfunction_g_value_82.setter
    def gfunction_g_value_82(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_82`

        Args:
            value (float): value for IDD Field `gfunction_g_value_82`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_82`'.format(value))

        self._data["G-Function G Value 82"] = value

    @property
    def gfunction_lnt_or_ts_value_83(self):
        """Get gfunction_lnt_or_ts_value_83

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_83` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 83"]

    @gfunction_lnt_or_ts_value_83.setter
    def gfunction_lnt_or_ts_value_83(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_83`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_83`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 83"] = value

    @property
    def gfunction_g_value_83(self):
        """Get gfunction_g_value_83

        Returns:
            float: the value of `gfunction_g_value_83` or None if not set
        """
        return self._data["G-Function G Value 83"]

    @gfunction_g_value_83.setter
    def gfunction_g_value_83(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_83`

        Args:
            value (float): value for IDD Field `gfunction_g_value_83`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_83`'.format(value))

        self._data["G-Function G Value 83"] = value

    @property
    def gfunction_lnt_or_ts_value_84(self):
        """Get gfunction_lnt_or_ts_value_84

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_84` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 84"]

    @gfunction_lnt_or_ts_value_84.setter
    def gfunction_lnt_or_ts_value_84(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_84`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_84`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 84"] = value

    @property
    def gfunction_g_value_84(self):
        """Get gfunction_g_value_84

        Returns:
            float: the value of `gfunction_g_value_84` or None if not set
        """
        return self._data["G-Function G Value 84"]

    @gfunction_g_value_84.setter
    def gfunction_g_value_84(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_84`

        Args:
            value (float): value for IDD Field `gfunction_g_value_84`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_84`'.format(value))

        self._data["G-Function G Value 84"] = value

    @property
    def gfunction_lnt_or_ts_value_85(self):
        """Get gfunction_lnt_or_ts_value_85

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_85` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 85"]

    @gfunction_lnt_or_ts_value_85.setter
    def gfunction_lnt_or_ts_value_85(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_85`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_85`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 85"] = value

    @property
    def gfunction_g_value_85(self):
        """Get gfunction_g_value_85

        Returns:
            float: the value of `gfunction_g_value_85` or None if not set
        """
        return self._data["G-Function G Value 85"]

    @gfunction_g_value_85.setter
    def gfunction_g_value_85(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_85`

        Args:
            value (float): value for IDD Field `gfunction_g_value_85`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_85`'.format(value))

        self._data["G-Function G Value 85"] = value

    @property
    def gfunction_lnt_or_ts_value_86(self):
        """Get gfunction_lnt_or_ts_value_86

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_86` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 86"]

    @gfunction_lnt_or_ts_value_86.setter
    def gfunction_lnt_or_ts_value_86(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_86`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_86`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 86"] = value

    @property
    def gfunction_g_value_86(self):
        """Get gfunction_g_value_86

        Returns:
            float: the value of `gfunction_g_value_86` or None if not set
        """
        return self._data["G-Function G Value 86"]

    @gfunction_g_value_86.setter
    def gfunction_g_value_86(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_86`

        Args:
            value (float): value for IDD Field `gfunction_g_value_86`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_86`'.format(value))

        self._data["G-Function G Value 86"] = value

    @property
    def gfunction_lnt_or_ts_value_87(self):
        """Get gfunction_lnt_or_ts_value_87

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_87` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 87"]

    @gfunction_lnt_or_ts_value_87.setter
    def gfunction_lnt_or_ts_value_87(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_87`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_87`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 87"] = value

    @property
    def gfunction_g_value_87(self):
        """Get gfunction_g_value_87

        Returns:
            float: the value of `gfunction_g_value_87` or None if not set
        """
        return self._data["G-Function G Value 87"]

    @gfunction_g_value_87.setter
    def gfunction_g_value_87(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_87`

        Args:
            value (float): value for IDD Field `gfunction_g_value_87`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_87`'.format(value))

        self._data["G-Function G Value 87"] = value

    @property
    def gfunction_lnt_or_ts_value_88(self):
        """Get gfunction_lnt_or_ts_value_88

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_88` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 88"]

    @gfunction_lnt_or_ts_value_88.setter
    def gfunction_lnt_or_ts_value_88(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_88`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_88`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 88"] = value

    @property
    def gfunction_g_value_88(self):
        """Get gfunction_g_value_88

        Returns:
            float: the value of `gfunction_g_value_88` or None if not set
        """
        return self._data["G-Function G Value 88"]

    @gfunction_g_value_88.setter
    def gfunction_g_value_88(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_88`

        Args:
            value (float): value for IDD Field `gfunction_g_value_88`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_88`'.format(value))

        self._data["G-Function G Value 88"] = value

    @property
    def gfunction_lnt_or_ts_value_89(self):
        """Get gfunction_lnt_or_ts_value_89

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_89` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 89"]

    @gfunction_lnt_or_ts_value_89.setter
    def gfunction_lnt_or_ts_value_89(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_89`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_89`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 89"] = value

    @property
    def gfunction_g_value_89(self):
        """Get gfunction_g_value_89

        Returns:
            float: the value of `gfunction_g_value_89` or None if not set
        """
        return self._data["G-Function G Value 89"]

    @gfunction_g_value_89.setter
    def gfunction_g_value_89(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_89`

        Args:
            value (float): value for IDD Field `gfunction_g_value_89`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_89`'.format(value))

        self._data["G-Function G Value 89"] = value

    @property
    def gfunction_lnt_or_ts_value_90(self):
        """Get gfunction_lnt_or_ts_value_90

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_90` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 90"]

    @gfunction_lnt_or_ts_value_90.setter
    def gfunction_lnt_or_ts_value_90(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_90`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_90`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 90"] = value

    @property
    def gfunction_g_value_90(self):
        """Get gfunction_g_value_90

        Returns:
            float: the value of `gfunction_g_value_90` or None if not set
        """
        return self._data["G-Function G Value 90"]

    @gfunction_g_value_90.setter
    def gfunction_g_value_90(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_90`

        Args:
            value (float): value for IDD Field `gfunction_g_value_90`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_90`'.format(value))

        self._data["G-Function G Value 90"] = value

    @property
    def gfunction_lnt_or_ts_value_91(self):
        """Get gfunction_lnt_or_ts_value_91

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_91` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 91"]

    @gfunction_lnt_or_ts_value_91.setter
    def gfunction_lnt_or_ts_value_91(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_91`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_91`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 91"] = value

    @property
    def gfunction_g_value_91(self):
        """Get gfunction_g_value_91

        Returns:
            float: the value of `gfunction_g_value_91` or None if not set
        """
        return self._data["G-Function G Value 91"]

    @gfunction_g_value_91.setter
    def gfunction_g_value_91(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_91`

        Args:
            value (float): value for IDD Field `gfunction_g_value_91`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_91`'.format(value))

        self._data["G-Function G Value 91"] = value

    @property
    def gfunction_lnt_or_ts_value_92(self):
        """Get gfunction_lnt_or_ts_value_92

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_92` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 92"]

    @gfunction_lnt_or_ts_value_92.setter
    def gfunction_lnt_or_ts_value_92(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_92`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_92`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 92"] = value

    @property
    def gfunction_g_value_92(self):
        """Get gfunction_g_value_92

        Returns:
            float: the value of `gfunction_g_value_92` or None if not set
        """
        return self._data["G-Function G Value 92"]

    @gfunction_g_value_92.setter
    def gfunction_g_value_92(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_92`

        Args:
            value (float): value for IDD Field `gfunction_g_value_92`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_92`'.format(value))

        self._data["G-Function G Value 92"] = value

    @property
    def gfunction_lnt_or_ts_value_93(self):
        """Get gfunction_lnt_or_ts_value_93

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_93` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 93"]

    @gfunction_lnt_or_ts_value_93.setter
    def gfunction_lnt_or_ts_value_93(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_93`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_93`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 93"] = value

    @property
    def gfunction_g_value_93(self):
        """Get gfunction_g_value_93

        Returns:
            float: the value of `gfunction_g_value_93` or None if not set
        """
        return self._data["G-Function G Value 93"]

    @gfunction_g_value_93.setter
    def gfunction_g_value_93(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_93`

        Args:
            value (float): value for IDD Field `gfunction_g_value_93`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_93`'.format(value))

        self._data["G-Function G Value 93"] = value

    @property
    def gfunction_lnt_or_ts_value_94(self):
        """Get gfunction_lnt_or_ts_value_94

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_94` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 94"]

    @gfunction_lnt_or_ts_value_94.setter
    def gfunction_lnt_or_ts_value_94(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_94`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_94`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 94"] = value

    @property
    def gfunction_g_value_94(self):
        """Get gfunction_g_value_94

        Returns:
            float: the value of `gfunction_g_value_94` or None if not set
        """
        return self._data["G-Function G Value 94"]

    @gfunction_g_value_94.setter
    def gfunction_g_value_94(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_94`

        Args:
            value (float): value for IDD Field `gfunction_g_value_94`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_94`'.format(value))

        self._data["G-Function G Value 94"] = value

    @property
    def gfunction_lnt_or_ts_value_95(self):
        """Get gfunction_lnt_or_ts_value_95

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_95` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 95"]

    @gfunction_lnt_or_ts_value_95.setter
    def gfunction_lnt_or_ts_value_95(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_95`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_95`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 95"] = value

    @property
    def gfunction_g_value_95(self):
        """Get gfunction_g_value_95

        Returns:
            float: the value of `gfunction_g_value_95` or None if not set
        """
        return self._data["G-Function G Value 95"]

    @gfunction_g_value_95.setter
    def gfunction_g_value_95(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_95`

        Args:
            value (float): value for IDD Field `gfunction_g_value_95`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_95`'.format(value))

        self._data["G-Function G Value 95"] = value

    @property
    def gfunction_lnt_or_ts_value_96(self):
        """Get gfunction_lnt_or_ts_value_96

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_96` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 96"]

    @gfunction_lnt_or_ts_value_96.setter
    def gfunction_lnt_or_ts_value_96(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_96`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_96`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 96"] = value

    @property
    def gfunction_g_value_96(self):
        """Get gfunction_g_value_96

        Returns:
            float: the value of `gfunction_g_value_96` or None if not set
        """
        return self._data["G-Function G Value 96"]

    @gfunction_g_value_96.setter
    def gfunction_g_value_96(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_96`

        Args:
            value (float): value for IDD Field `gfunction_g_value_96`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_96`'.format(value))

        self._data["G-Function G Value 96"] = value

    @property
    def gfunction_lnt_or_ts_value_97(self):
        """Get gfunction_lnt_or_ts_value_97

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_97` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 97"]

    @gfunction_lnt_or_ts_value_97.setter
    def gfunction_lnt_or_ts_value_97(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_97`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_97`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 97"] = value

    @property
    def gfunction_g_value_97(self):
        """Get gfunction_g_value_97

        Returns:
            float: the value of `gfunction_g_value_97` or None if not set
        """
        return self._data["G-Function G Value 97"]

    @gfunction_g_value_97.setter
    def gfunction_g_value_97(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_97`

        Args:
            value (float): value for IDD Field `gfunction_g_value_97`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_97`'.format(value))

        self._data["G-Function G Value 97"] = value

    @property
    def gfunction_lnt_or_ts_value_98(self):
        """Get gfunction_lnt_or_ts_value_98

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_98` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 98"]

    @gfunction_lnt_or_ts_value_98.setter
    def gfunction_lnt_or_ts_value_98(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_98`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_98`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 98"] = value

    @property
    def gfunction_g_value_98(self):
        """Get gfunction_g_value_98

        Returns:
            float: the value of `gfunction_g_value_98` or None if not set
        """
        return self._data["G-Function G Value 98"]

    @gfunction_g_value_98.setter
    def gfunction_g_value_98(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_98`

        Args:
            value (float): value for IDD Field `gfunction_g_value_98`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_98`'.format(value))

        self._data["G-Function G Value 98"] = value

    @property
    def gfunction_lnt_or_ts_value_99(self):
        """Get gfunction_lnt_or_ts_value_99

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_99` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 99"]

    @gfunction_lnt_or_ts_value_99.setter
    def gfunction_lnt_or_ts_value_99(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_99`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_99`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 99"] = value

    @property
    def gfunction_g_value_99(self):
        """Get gfunction_g_value_99

        Returns:
            float: the value of `gfunction_g_value_99` or None if not set
        """
        return self._data["G-Function G Value 99"]

    @gfunction_g_value_99.setter
    def gfunction_g_value_99(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_99`

        Args:
            value (float): value for IDD Field `gfunction_g_value_99`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_99`'.format(value))

        self._data["G-Function G Value 99"] = value

    @property
    def gfunction_lnt_or_ts_value_100(self):
        """Get gfunction_lnt_or_ts_value_100

        Returns:
            float: the value of `gfunction_lnt_or_ts_value_100` or None if not set
        """
        return self._data["G-Function Ln(T/Ts) Value 100"]

    @gfunction_lnt_or_ts_value_100.setter
    def gfunction_lnt_or_ts_value_100(self, value=None):
        """  Corresponds to IDD Field `gfunction_lnt_or_ts_value_100`

        Args:
            value (float): value for IDD Field `gfunction_lnt_or_ts_value_100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_lnt_or_ts_value_100`'.format(value))

        self._data["G-Function Ln(T/Ts) Value 100"] = value

    @property
    def gfunction_g_value_100(self):
        """Get gfunction_g_value_100

        Returns:
            float: the value of `gfunction_g_value_100` or None if not set
        """
        return self._data["G-Function G Value 100"]

    @gfunction_g_value_100.setter
    def gfunction_g_value_100(self, value=None):
        """  Corresponds to IDD Field `gfunction_g_value_100`

        Args:
            value (float): value for IDD Field `gfunction_g_value_100`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `gfunction_g_value_100`'.format(value))

        self._data["G-Function G Value 100"] = value

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
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.maximum_flow_rate))
        out.append(self._to_str(self.number_of_bore_holes))
        out.append(self._to_str(self.bore_hole_length))
        out.append(self._to_str(self.bore_hole_radius))
        out.append(self._to_str(self.ground_thermal_conductivity))
        out.append(self._to_str(self.ground_thermal_heat_capacity))
        out.append(self._to_str(self.ground_temperature))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.grout_thermal_conductivity))
        out.append(self._to_str(self.pipe_thermal_conductivity))
        out.append(self._to_str(self.pipe_out_diameter))
        out.append(self._to_str(self.utube_distance))
        out.append(self._to_str(self.pipe_thickness))
        out.append(self._to_str(self.maximum_length_of_simulation))
        out.append(self._to_str(self.gfunction_reference_ratio))
        out.append(self._to_str(self.number_of_data_pairs_of_the_g_function))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_1))
        out.append(self._to_str(self.gfunction_g_value_1))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_2))
        out.append(self._to_str(self.gfunction_g_value_2))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_3))
        out.append(self._to_str(self.gfunction_g_value_3))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_4))
        out.append(self._to_str(self.gfunction_g_value_4))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_5))
        out.append(self._to_str(self.gfunction_g_value_5))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_6))
        out.append(self._to_str(self.gfunction_g_value_6))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_7))
        out.append(self._to_str(self.gfunction_g_value_7))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_8))
        out.append(self._to_str(self.gfunction_g_value_8))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_9))
        out.append(self._to_str(self.gfunction_g_value_9))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_10))
        out.append(self._to_str(self.gfunction_g_value_10))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_11))
        out.append(self._to_str(self.gfunction_g_value_11))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_12))
        out.append(self._to_str(self.gfunction_g_value_12))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_13))
        out.append(self._to_str(self.gfunction_g_value_13))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_14))
        out.append(self._to_str(self.gfunction_g_value_14))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_15))
        out.append(self._to_str(self.gfunction_g_value_15))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_16))
        out.append(self._to_str(self.gfunction_g_value_16))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_17))
        out.append(self._to_str(self.gfunction_g_value_17))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_18))
        out.append(self._to_str(self.gfunction_g_value_18))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_19))
        out.append(self._to_str(self.gfunction_g_value_19))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_20))
        out.append(self._to_str(self.gfunction_g_value_20))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_21))
        out.append(self._to_str(self.gfunction_g_value_21))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_22))
        out.append(self._to_str(self.gfunction_g_value_22))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_23))
        out.append(self._to_str(self.gfunction_g_value_23))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_24))
        out.append(self._to_str(self.gfunction_g_value_24))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_25))
        out.append(self._to_str(self.gfunction_g_value_25))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_26))
        out.append(self._to_str(self.gfunction_g_value_26))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_27))
        out.append(self._to_str(self.gfunction_g_value_27))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_28))
        out.append(self._to_str(self.gfunction_g_value_28))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_29))
        out.append(self._to_str(self.gfunction_g_value_29))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_30))
        out.append(self._to_str(self.gfunction_g_value_30))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_31))
        out.append(self._to_str(self.gfunction_g_value_31))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_32))
        out.append(self._to_str(self.gfunction_g_value_32))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_33))
        out.append(self._to_str(self.gfunction_g_value_33))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_34))
        out.append(self._to_str(self.gfunction_g_value_34))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_35))
        out.append(self._to_str(self.gfunction_g_value_35))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_36))
        out.append(self._to_str(self.gfunction_g_value_36))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_37))
        out.append(self._to_str(self.gfunction_g_value_37))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_38))
        out.append(self._to_str(self.gfunction_g_value_38))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_39))
        out.append(self._to_str(self.gfunction_g_value_39))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_40))
        out.append(self._to_str(self.gfunction_g_value_40))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_41))
        out.append(self._to_str(self.gfunction_g_value_41))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_42))
        out.append(self._to_str(self.gfunction_g_value_42))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_43))
        out.append(self._to_str(self.gfunction_g_value_43))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_44))
        out.append(self._to_str(self.gfunction_g_value_44))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_45))
        out.append(self._to_str(self.gfunction_g_value_45))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_46))
        out.append(self._to_str(self.gfunction_g_value_46))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_47))
        out.append(self._to_str(self.gfunction_g_value_47))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_48))
        out.append(self._to_str(self.gfunction_g_value_48))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_49))
        out.append(self._to_str(self.gfunction_g_value_49))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_50))
        out.append(self._to_str(self.gfunction_g_value_50))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_51))
        out.append(self._to_str(self.gfunction_g_value_51))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_52))
        out.append(self._to_str(self.gfunction_g_value_52))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_53))
        out.append(self._to_str(self.gfunction_g_value_53))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_54))
        out.append(self._to_str(self.gfunction_g_value_54))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_55))
        out.append(self._to_str(self.gfunction_g_value_55))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_56))
        out.append(self._to_str(self.gfunction_g_value_56))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_57))
        out.append(self._to_str(self.gfunction_g_value_57))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_58))
        out.append(self._to_str(self.gfunction_g_value_58))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_59))
        out.append(self._to_str(self.gfunction_g_value_59))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_60))
        out.append(self._to_str(self.gfunction_g_value_60))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_61))
        out.append(self._to_str(self.gfunction_g_value_61))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_62))
        out.append(self._to_str(self.gfunction_g_value_62))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_63))
        out.append(self._to_str(self.gfunction_g_value_63))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_64))
        out.append(self._to_str(self.gfunction_g_value_64))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_65))
        out.append(self._to_str(self.gfunction_g_value_65))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_66))
        out.append(self._to_str(self.gfunction_g_value_66))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_67))
        out.append(self._to_str(self.gfunction_g_value_67))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_68))
        out.append(self._to_str(self.gfunction_g_value_68))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_69))
        out.append(self._to_str(self.gfunction_g_value_69))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_70))
        out.append(self._to_str(self.gfunction_g_value_70))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_71))
        out.append(self._to_str(self.gfunction_g_value_71))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_72))
        out.append(self._to_str(self.gfunction_g_value_72))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_73))
        out.append(self._to_str(self.gfunction_g_value_73))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_74))
        out.append(self._to_str(self.gfunction_g_value_74))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_75))
        out.append(self._to_str(self.gfunction_g_value_75))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_76))
        out.append(self._to_str(self.gfunction_g_value_76))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_77))
        out.append(self._to_str(self.gfunction_g_value_77))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_78))
        out.append(self._to_str(self.gfunction_g_value_78))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_79))
        out.append(self._to_str(self.gfunction_g_value_79))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_80))
        out.append(self._to_str(self.gfunction_g_value_80))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_81))
        out.append(self._to_str(self.gfunction_g_value_81))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_82))
        out.append(self._to_str(self.gfunction_g_value_82))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_83))
        out.append(self._to_str(self.gfunction_g_value_83))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_84))
        out.append(self._to_str(self.gfunction_g_value_84))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_85))
        out.append(self._to_str(self.gfunction_g_value_85))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_86))
        out.append(self._to_str(self.gfunction_g_value_86))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_87))
        out.append(self._to_str(self.gfunction_g_value_87))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_88))
        out.append(self._to_str(self.gfunction_g_value_88))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_89))
        out.append(self._to_str(self.gfunction_g_value_89))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_90))
        out.append(self._to_str(self.gfunction_g_value_90))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_91))
        out.append(self._to_str(self.gfunction_g_value_91))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_92))
        out.append(self._to_str(self.gfunction_g_value_92))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_93))
        out.append(self._to_str(self.gfunction_g_value_93))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_94))
        out.append(self._to_str(self.gfunction_g_value_94))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_95))
        out.append(self._to_str(self.gfunction_g_value_95))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_96))
        out.append(self._to_str(self.gfunction_g_value_96))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_97))
        out.append(self._to_str(self.gfunction_g_value_97))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_98))
        out.append(self._to_str(self.gfunction_g_value_98))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_99))
        out.append(self._to_str(self.gfunction_g_value_99))
        out.append(self._to_str(self.gfunction_lnt_or_ts_value_100))
        out.append(self._to_str(self.gfunction_g_value_100))
        return ",".join(out)

class GroundHeatExchangerPond(object):
    """ Corresponds to IDD object `GroundHeatExchanger:Pond`
        A model of a shallow pond with immersed pipe loops.
        Typically used in hybrid geothermal systems and included in the condenser loop.
        This component may also be used as a simple solar collector.
    """
    internal_name = "GroundHeatExchanger:Pond"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `GroundHeatExchanger:Pond`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Pond Depth"] = None
        self._data["Pond Area"] = None
        self._data["Hydronic Tubing Inside Diameter"] = None
        self._data["Hydronic Tubing Outside Diameter"] = None
        self._data["Hydronic Tubing Thermal Conductivity"] = None
        self._data["Ground Thermal Conductivity"] = None
        self._data["Number of Tubing Circuits"] = None
        self._data["Length of Each Tubing Circuit"] = None

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
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pond_depth = None
        else:
            self.pond_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pond_area = None
        else:
            self.pond_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hydronic_tubing_inside_diameter = None
        else:
            self.hydronic_tubing_inside_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hydronic_tubing_outside_diameter = None
        else:
            self.hydronic_tubing_outside_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hydronic_tubing_thermal_conductivity = None
        else:
            self.hydronic_tubing_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ground_thermal_conductivity = None
        else:
            self.ground_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_tubing_circuits = None
        else:
            self.number_of_tubing_circuits = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.length_of_each_tubing_circuit = None
        else:
            self.length_of_each_tubing_circuit = vals[i]
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
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_inlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')

        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_outlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')

        self._data["Fluid Outlet Node Name"] = value

    @property
    def pond_depth(self):
        """Get pond_depth

        Returns:
            float: the value of `pond_depth` or None if not set
        """
        return self._data["Pond Depth"]

    @pond_depth.setter
    def pond_depth(self, value=None):
        """  Corresponds to IDD Field `pond_depth`

        Args:
            value (float): value for IDD Field `pond_depth`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pond_depth`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pond_depth`')

        self._data["Pond Depth"] = value

    @property
    def pond_area(self):
        """Get pond_area

        Returns:
            float: the value of `pond_area` or None if not set
        """
        return self._data["Pond Area"]

    @pond_area.setter
    def pond_area(self, value=None):
        """  Corresponds to IDD Field `pond_area`

        Args:
            value (float): value for IDD Field `pond_area`
                Unit: m2
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pond_area`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pond_area`')

        self._data["Pond Area"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """Get hydronic_tubing_inside_diameter

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `hydronic_tubing_inside_diameter`

        Args:
            value (float): value for IDD Field `hydronic_tubing_inside_diameter`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_inside_diameter`')

        self._data["Hydronic Tubing Inside Diameter"] = value

    @property
    def hydronic_tubing_outside_diameter(self):
        """Get hydronic_tubing_outside_diameter

        Returns:
            float: the value of `hydronic_tubing_outside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Outside Diameter"]

    @hydronic_tubing_outside_diameter.setter
    def hydronic_tubing_outside_diameter(self, value=None):
        """  Corresponds to IDD Field `hydronic_tubing_outside_diameter`

        Args:
            value (float): value for IDD Field `hydronic_tubing_outside_diameter`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_outside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_outside_diameter`')

        self._data["Hydronic Tubing Outside Diameter"] = value

    @property
    def hydronic_tubing_thermal_conductivity(self):
        """Get hydronic_tubing_thermal_conductivity

        Returns:
            float: the value of `hydronic_tubing_thermal_conductivity` or None if not set
        """
        return self._data["Hydronic Tubing Thermal Conductivity"]

    @hydronic_tubing_thermal_conductivity.setter
    def hydronic_tubing_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `hydronic_tubing_thermal_conductivity`

        Args:
            value (float): value for IDD Field `hydronic_tubing_thermal_conductivity`
                Unit: W/m-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_thermal_conductivity`')

        self._data["Hydronic Tubing Thermal Conductivity"] = value

    @property
    def ground_thermal_conductivity(self):
        """Get ground_thermal_conductivity

        Returns:
            float: the value of `ground_thermal_conductivity` or None if not set
        """
        return self._data["Ground Thermal Conductivity"]

    @ground_thermal_conductivity.setter
    def ground_thermal_conductivity(self, value=None):
        """  Corresponds to IDD Field `ground_thermal_conductivity`

        Args:
            value (float): value for IDD Field `ground_thermal_conductivity`
                Unit: W/m2-K
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `ground_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `ground_thermal_conductivity`')

        self._data["Ground Thermal Conductivity"] = value

    @property
    def number_of_tubing_circuits(self):
        """Get number_of_tubing_circuits

        Returns:
            int: the value of `number_of_tubing_circuits` or None if not set
        """
        return self._data["Number of Tubing Circuits"]

    @number_of_tubing_circuits.setter
    def number_of_tubing_circuits(self, value=None):
        """  Corresponds to IDD Field `number_of_tubing_circuits`

        Args:
            value (int): value for IDD Field `number_of_tubing_circuits`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_tubing_circuits`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_tubing_circuits`')

        self._data["Number of Tubing Circuits"] = value

    @property
    def length_of_each_tubing_circuit(self):
        """Get length_of_each_tubing_circuit

        Returns:
            float: the value of `length_of_each_tubing_circuit` or None if not set
        """
        return self._data["Length of Each Tubing Circuit"]

    @length_of_each_tubing_circuit.setter
    def length_of_each_tubing_circuit(self, value=None):
        """  Corresponds to IDD Field `length_of_each_tubing_circuit`

        Args:
            value (float): value for IDD Field `length_of_each_tubing_circuit`
                Unit: m
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `length_of_each_tubing_circuit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `length_of_each_tubing_circuit`')

        self._data["Length of Each Tubing Circuit"] = value

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
        out.append(self._to_str(self.fluid_inlet_node_name))
        out.append(self._to_str(self.fluid_outlet_node_name))
        out.append(self._to_str(self.pond_depth))
        out.append(self._to_str(self.pond_area))
        out.append(self._to_str(self.hydronic_tubing_inside_diameter))
        out.append(self._to_str(self.hydronic_tubing_outside_diameter))
        out.append(self._to_str(self.hydronic_tubing_thermal_conductivity))
        out.append(self._to_str(self.ground_thermal_conductivity))
        out.append(self._to_str(self.number_of_tubing_circuits))
        out.append(self._to_str(self.length_of_each_tubing_circuit))
        return ",".join(out)

class GroundHeatExchangerSurface(object):
    """ Corresponds to IDD object `GroundHeatExchanger:Surface`
        A hydronic surface/panel consisting of a multi-layer construction with embedded rows of tubes.
        Typically used in hybrid geothermal systems and included in the condenser loop.
        This component may also be used as a simple solar collector.
        The bottom surface may be defined as ground-coupled or exposed to wind (eg. bridge deck).
    """
    internal_name = "GroundHeatExchanger:Surface"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `GroundHeatExchanger:Surface`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Construction Name"] = None
        self._data["Fluid Inlet Node Name"] = None
        self._data["Fluid Outlet Node Name"] = None
        self._data["Hydronic Tubing Inside Diameter"] = None
        self._data["Number of Tubing Circuits"] = None
        self._data["Hydronic Tube Spacing"] = None
        self._data["Surface Length"] = None
        self._data["Surface Width"] = None
        self._data["Lower Surface Environment"] = None

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
            self.construction_name = None
        else:
            self.construction_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fluid_inlet_node_name = None
        else:
            self.fluid_inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fluid_outlet_node_name = None
        else:
            self.fluid_outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hydronic_tubing_inside_diameter = None
        else:
            self.hydronic_tubing_inside_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_tubing_circuits = None
        else:
            self.number_of_tubing_circuits = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.hydronic_tube_spacing = None
        else:
            self.hydronic_tube_spacing = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_length = None
        else:
            self.surface_length = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.surface_width = None
        else:
            self.surface_width = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.lower_surface_environment = None
        else:
            self.lower_surface_environment = vals[i]
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
    def construction_name(self):
        """Get construction_name

        Returns:
            str: the value of `construction_name` or None if not set
        """
        return self._data["Construction Name"]

    @construction_name.setter
    def construction_name(self, value=None):
        """  Corresponds to IDD Field `construction_name`

        Args:
            value (str): value for IDD Field `construction_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `construction_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `construction_name`')

        self._data["Construction Name"] = value

    @property
    def fluid_inlet_node_name(self):
        """Get fluid_inlet_node_name

        Returns:
            str: the value of `fluid_inlet_node_name` or None if not set
        """
        return self._data["Fluid Inlet Node Name"]

    @fluid_inlet_node_name.setter
    def fluid_inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_inlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_inlet_node_name`')

        self._data["Fluid Inlet Node Name"] = value

    @property
    def fluid_outlet_node_name(self):
        """Get fluid_outlet_node_name

        Returns:
            str: the value of `fluid_outlet_node_name` or None if not set
        """
        return self._data["Fluid Outlet Node Name"]

    @fluid_outlet_node_name.setter
    def fluid_outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `fluid_outlet_node_name`

        Args:
            value (str): value for IDD Field `fluid_outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fluid_outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fluid_outlet_node_name`')

        self._data["Fluid Outlet Node Name"] = value

    @property
    def hydronic_tubing_inside_diameter(self):
        """Get hydronic_tubing_inside_diameter

        Returns:
            float: the value of `hydronic_tubing_inside_diameter` or None if not set
        """
        return self._data["Hydronic Tubing Inside Diameter"]

    @hydronic_tubing_inside_diameter.setter
    def hydronic_tubing_inside_diameter(self, value=None):
        """  Corresponds to IDD Field `hydronic_tubing_inside_diameter`

        Args:
            value (float): value for IDD Field `hydronic_tubing_inside_diameter`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tubing_inside_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tubing_inside_diameter`')

        self._data["Hydronic Tubing Inside Diameter"] = value

    @property
    def number_of_tubing_circuits(self):
        """Get number_of_tubing_circuits

        Returns:
            int: the value of `number_of_tubing_circuits` or None if not set
        """
        return self._data["Number of Tubing Circuits"]

    @number_of_tubing_circuits.setter
    def number_of_tubing_circuits(self, value=None):
        """  Corresponds to IDD Field `number_of_tubing_circuits`

        Args:
            value (int): value for IDD Field `number_of_tubing_circuits`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_tubing_circuits`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_tubing_circuits`')

        self._data["Number of Tubing Circuits"] = value

    @property
    def hydronic_tube_spacing(self):
        """Get hydronic_tube_spacing

        Returns:
            float: the value of `hydronic_tube_spacing` or None if not set
        """
        return self._data["Hydronic Tube Spacing"]

    @hydronic_tube_spacing.setter
    def hydronic_tube_spacing(self, value=None):
        """  Corresponds to IDD Field `hydronic_tube_spacing`

        Args:
            value (float): value for IDD Field `hydronic_tube_spacing`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `hydronic_tube_spacing`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `hydronic_tube_spacing`')

        self._data["Hydronic Tube Spacing"] = value

    @property
    def surface_length(self):
        """Get surface_length

        Returns:
            float: the value of `surface_length` or None if not set
        """
        return self._data["Surface Length"]

    @surface_length.setter
    def surface_length(self, value=None):
        """  Corresponds to IDD Field `surface_length`

        Args:
            value (float): value for IDD Field `surface_length`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `surface_length`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `surface_length`')

        self._data["Surface Length"] = value

    @property
    def surface_width(self):
        """Get surface_width

        Returns:
            float: the value of `surface_width` or None if not set
        """
        return self._data["Surface Width"]

    @surface_width.setter
    def surface_width(self, value=None):
        """  Corresponds to IDD Field `surface_width`

        Args:
            value (float): value for IDD Field `surface_width`
                Unit: m
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `surface_width`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `surface_width`')

        self._data["Surface Width"] = value

    @property
    def lower_surface_environment(self):
        """Get lower_surface_environment

        Returns:
            str: the value of `lower_surface_environment` or None if not set
        """
        return self._data["Lower Surface Environment"]

    @lower_surface_environment.setter
    def lower_surface_environment(self, value="Ground"):
        """  Corresponds to IDD Field `lower_surface_environment`

        Args:
            value (str): value for IDD Field `lower_surface_environment`
                Accepted values are:
                      - Ground
                      - Exposed
                Default value: Ground
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `lower_surface_environment`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `lower_surface_environment`')
            vals = set()
            vals.add("Ground")
            vals.add("Exposed")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `lower_surface_environment`'.format(value))

        self._data["Lower Surface Environment"] = value

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
        out.append(self._to_str(self.construction_name))
        out.append(self._to_str(self.fluid_inlet_node_name))
        out.append(self._to_str(self.fluid_outlet_node_name))
        out.append(self._to_str(self.hydronic_tubing_inside_diameter))
        out.append(self._to_str(self.number_of_tubing_circuits))
        out.append(self._to_str(self.hydronic_tube_spacing))
        out.append(self._to_str(self.surface_length))
        out.append(self._to_str(self.surface_width))
        out.append(self._to_str(self.lower_surface_environment))
        return ",".join(out)

class GroundHeatExchangerHorizontalTrench(object):
    """ Corresponds to IDD object `GroundHeatExchanger:HorizontalTrench`
        This models a horizontal heat exchanger placed in a series of trenches
        The model uses the PipingSystem:Underground underlying algorithms,
        but provides a more usable input interface.
    """
    internal_name = "GroundHeatExchanger:HorizontalTrench"
    field_count = 22

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `GroundHeatExchanger:HorizontalTrench`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Inlet Node Name"] = None
        self._data["Outlet Node Name"] = None
        self._data["Design Flow Rate"] = None
        self._data["Trench Length in Pipe Axial Direction"] = None
        self._data["Number of Trenches"] = None
        self._data["Horizontal Spacing Between Pipes"] = None
        self._data["Pipe Inner Diameter"] = None
        self._data["Pipe Outer Diameter"] = None
        self._data["Burial Depth"] = None
        self._data["Soil Thermal Conductivity"] = None
        self._data["Soil Density"] = None
        self._data["Soil Specific Heat"] = None
        self._data["Pipe Thermal Conductivity"] = None
        self._data["Pipe Density"] = None
        self._data["Pipe Specific Heat"] = None
        self._data["Soil Moisture Content Percent"] = None
        self._data["Soil Moisture Content Percent at Saturation"] = None
        self._data["Kusuda-Achenbach Average Surface Temperature"] = None
        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = None
        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = None
        self._data["Evapotranspiration Ground Cover Parameter"] = None

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
            self.inlet_node_name = None
        else:
            self.inlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outlet_node_name = None
        else:
            self.outlet_node_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.design_flow_rate = None
        else:
            self.design_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.trench_length_in_pipe_axial_direction = None
        else:
            self.trench_length_in_pipe_axial_direction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_trenches = None
        else:
            self.number_of_trenches = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.horizontal_spacing_between_pipes = None
        else:
            self.horizontal_spacing_between_pipes = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_inner_diameter = None
        else:
            self.pipe_inner_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_outer_diameter = None
        else:
            self.pipe_outer_diameter = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.burial_depth = None
        else:
            self.burial_depth = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_thermal_conductivity = None
        else:
            self.soil_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_density = None
        else:
            self.soil_density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_specific_heat = None
        else:
            self.soil_specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_thermal_conductivity = None
        else:
            self.pipe_thermal_conductivity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_density = None
        else:
            self.pipe_density = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.pipe_specific_heat = None
        else:
            self.pipe_specific_heat = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_moisture_content_percent = None
        else:
            self.soil_moisture_content_percent = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.soil_moisture_content_percent_at_saturation = None
        else:
            self.soil_moisture_content_percent_at_saturation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_surface_temperature = None
        else:
            self.kusudaachenbach_average_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = None
        else:
            self.kusudaachenbach_average_amplitude_of_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = None
        else:
            self.kusudaachenbach_phase_shift_of_minimum_surface_temperature = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.evapotranspiration_ground_cover_parameter = None
        else:
            self.evapotranspiration_ground_cover_parameter = vals[i]
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
    def inlet_node_name(self):
        """Get inlet_node_name

        Returns:
            str: the value of `inlet_node_name` or None if not set
        """
        return self._data["Inlet Node Name"]

    @inlet_node_name.setter
    def inlet_node_name(self, value=None):
        """  Corresponds to IDD Field `inlet_node_name`

        Args:
            value (str): value for IDD Field `inlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inlet_node_name`')

        self._data["Inlet Node Name"] = value

    @property
    def outlet_node_name(self):
        """Get outlet_node_name

        Returns:
            str: the value of `outlet_node_name` or None if not set
        """
        return self._data["Outlet Node Name"]

    @outlet_node_name.setter
    def outlet_node_name(self, value=None):
        """  Corresponds to IDD Field `outlet_node_name`

        Args:
            value (str): value for IDD Field `outlet_node_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outlet_node_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outlet_node_name`')

        self._data["Outlet Node Name"] = value

    @property
    def design_flow_rate(self):
        """Get design_flow_rate

        Returns:
            float: the value of `design_flow_rate` or None if not set
        """
        return self._data["Design Flow Rate"]

    @design_flow_rate.setter
    def design_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_flow_rate`

        Args:
            value (float): value for IDD Field `design_flow_rate`
                Unit: m3/s
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_flow_rate`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `design_flow_rate`')

        self._data["Design Flow Rate"] = value

    @property
    def trench_length_in_pipe_axial_direction(self):
        """Get trench_length_in_pipe_axial_direction

        Returns:
            float: the value of `trench_length_in_pipe_axial_direction` or None if not set
        """
        return self._data["Trench Length in Pipe Axial Direction"]

    @trench_length_in_pipe_axial_direction.setter
    def trench_length_in_pipe_axial_direction(self, value=50.0 ):
        """  Corresponds to IDD Field `trench_length_in_pipe_axial_direction`
        This is the total pipe axial length of the heat exchanger
        If all pipe trenches are parallel, this is the length of a
        single trench.  If a single, long run of pipe is used with one
        trench, this is the full length of the pipe run.

        Args:
            value (float): value for IDD Field `trench_length_in_pipe_axial_direction`
                Unit: m
                Default value: 50.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `trench_length_in_pipe_axial_direction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `trench_length_in_pipe_axial_direction`')

        self._data["Trench Length in Pipe Axial Direction"] = value

    @property
    def number_of_trenches(self):
        """Get number_of_trenches

        Returns:
            int: the value of `number_of_trenches` or None if not set
        """
        return self._data["Number of Trenches"]

    @number_of_trenches.setter
    def number_of_trenches(self, value=1 ):
        """  Corresponds to IDD Field `number_of_trenches`
        This is the number of horizontal legs that will be used
        in the entire heat exchanger, one pipe per trench

        Args:
            value (int): value for IDD Field `number_of_trenches`
                Default value: 1
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except:
                raise ValueError('value {} need to be of type int '
                                 'for field `number_of_trenches`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_trenches`')

        self._data["Number of Trenches"] = value

    @property
    def horizontal_spacing_between_pipes(self):
        """Get horizontal_spacing_between_pipes

        Returns:
            float: the value of `horizontal_spacing_between_pipes` or None if not set
        """
        return self._data["Horizontal Spacing Between Pipes"]

    @horizontal_spacing_between_pipes.setter
    def horizontal_spacing_between_pipes(self, value=1.0 ):
        """  Corresponds to IDD Field `horizontal_spacing_between_pipes`
        This represents the average horizontal spacing between any two
        trenches for heat exchangers that have multiple trenches

        Args:
            value (float): value for IDD Field `horizontal_spacing_between_pipes`
                Unit: m
                Default value: 1.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `horizontal_spacing_between_pipes`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `horizontal_spacing_between_pipes`')

        self._data["Horizontal Spacing Between Pipes"] = value

    @property
    def pipe_inner_diameter(self):
        """Get pipe_inner_diameter

        Returns:
            float: the value of `pipe_inner_diameter` or None if not set
        """
        return self._data["Pipe Inner Diameter"]

    @pipe_inner_diameter.setter
    def pipe_inner_diameter(self, value=0.016 ):
        """  Corresponds to IDD Field `pipe_inner_diameter`

        Args:
            value (float): value for IDD Field `pipe_inner_diameter`
                Unit: m
                Default value: 0.016
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_inner_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_inner_diameter`')

        self._data["Pipe Inner Diameter"] = value

    @property
    def pipe_outer_diameter(self):
        """Get pipe_outer_diameter

        Returns:
            float: the value of `pipe_outer_diameter` or None if not set
        """
        return self._data["Pipe Outer Diameter"]

    @pipe_outer_diameter.setter
    def pipe_outer_diameter(self, value=0.026 ):
        """  Corresponds to IDD Field `pipe_outer_diameter`

        Args:
            value (float): value for IDD Field `pipe_outer_diameter`
                Unit: m
                Default value: 0.026
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_outer_diameter`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_outer_diameter`')

        self._data["Pipe Outer Diameter"] = value

    @property
    def burial_depth(self):
        """Get burial_depth

        Returns:
            float: the value of `burial_depth` or None if not set
        """
        return self._data["Burial Depth"]

    @burial_depth.setter
    def burial_depth(self, value=1.5 ):
        """  Corresponds to IDD Field `burial_depth`
        This is the burial depth of the pipes, or the trenches
        containing the pipes

        Args:
            value (float): value for IDD Field `burial_depth`
                Unit: m
                Default value: 1.5
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `burial_depth`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `burial_depth`')

        self._data["Burial Depth"] = value

    @property
    def soil_thermal_conductivity(self):
        """Get soil_thermal_conductivity

        Returns:
            float: the value of `soil_thermal_conductivity` or None if not set
        """
        return self._data["Soil Thermal Conductivity"]

    @soil_thermal_conductivity.setter
    def soil_thermal_conductivity(self, value=1.08 ):
        """  Corresponds to IDD Field `soil_thermal_conductivity`

        Args:
            value (float): value for IDD Field `soil_thermal_conductivity`
                Unit: W/m-K
                Default value: 1.08
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_thermal_conductivity`')

        self._data["Soil Thermal Conductivity"] = value

    @property
    def soil_density(self):
        """Get soil_density

        Returns:
            float: the value of `soil_density` or None if not set
        """
        return self._data["Soil Density"]

    @soil_density.setter
    def soil_density(self, value=962.0 ):
        """  Corresponds to IDD Field `soil_density`

        Args:
            value (float): value for IDD Field `soil_density`
                Unit: kg/m3
                Default value: 962.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_density`')

        self._data["Soil Density"] = value

    @property
    def soil_specific_heat(self):
        """Get soil_specific_heat

        Returns:
            float: the value of `soil_specific_heat` or None if not set
        """
        return self._data["Soil Specific Heat"]

    @soil_specific_heat.setter
    def soil_specific_heat(self, value=2576.0 ):
        """  Corresponds to IDD Field `soil_specific_heat`

        Args:
            value (float): value for IDD Field `soil_specific_heat`
                Unit: J/kg-K
                Default value: 2576.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `soil_specific_heat`')

        self._data["Soil Specific Heat"] = value

    @property
    def pipe_thermal_conductivity(self):
        """Get pipe_thermal_conductivity

        Returns:
            float: the value of `pipe_thermal_conductivity` or None if not set
        """
        return self._data["Pipe Thermal Conductivity"]

    @pipe_thermal_conductivity.setter
    def pipe_thermal_conductivity(self, value=0.3895 ):
        """  Corresponds to IDD Field `pipe_thermal_conductivity`

        Args:
            value (float): value for IDD Field `pipe_thermal_conductivity`
                Unit: W/m-K
                Default value: 0.3895
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_thermal_conductivity`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_thermal_conductivity`')

        self._data["Pipe Thermal Conductivity"] = value

    @property
    def pipe_density(self):
        """Get pipe_density

        Returns:
            float: the value of `pipe_density` or None if not set
        """
        return self._data["Pipe Density"]

    @pipe_density.setter
    def pipe_density(self, value=641.0 ):
        """  Corresponds to IDD Field `pipe_density`

        Args:
            value (float): value for IDD Field `pipe_density`
                Unit: kg/m3
                Default value: 641.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_density`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_density`')

        self._data["Pipe Density"] = value

    @property
    def pipe_specific_heat(self):
        """Get pipe_specific_heat

        Returns:
            float: the value of `pipe_specific_heat` or None if not set
        """
        return self._data["Pipe Specific Heat"]

    @pipe_specific_heat.setter
    def pipe_specific_heat(self, value=2405.0 ):
        """  Corresponds to IDD Field `pipe_specific_heat`

        Args:
            value (float): value for IDD Field `pipe_specific_heat`
                Unit: J/kg-K
                Default value: 2405.0
                value > 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `pipe_specific_heat`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `pipe_specific_heat`')

        self._data["Pipe Specific Heat"] = value

    @property
    def soil_moisture_content_percent(self):
        """Get soil_moisture_content_percent

        Returns:
            float: the value of `soil_moisture_content_percent` or None if not set
        """
        return self._data["Soil Moisture Content Percent"]

    @soil_moisture_content_percent.setter
    def soil_moisture_content_percent(self, value=30.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_percent`

        Args:
            value (float): value for IDD Field `soil_moisture_content_percent`
                Unit: percent
                Default value: 30.0
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_moisture_content_percent`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_percent`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_percent`')

        self._data["Soil Moisture Content Percent"] = value

    @property
    def soil_moisture_content_percent_at_saturation(self):
        """Get soil_moisture_content_percent_at_saturation

        Returns:
            float: the value of `soil_moisture_content_percent_at_saturation` or None if not set
        """
        return self._data["Soil Moisture Content Percent at Saturation"]

    @soil_moisture_content_percent_at_saturation.setter
    def soil_moisture_content_percent_at_saturation(self, value=50.0 ):
        """  Corresponds to IDD Field `soil_moisture_content_percent_at_saturation`

        Args:
            value (float): value for IDD Field `soil_moisture_content_percent_at_saturation`
                Unit: percent
                Default value: 50.0
                value >= 0.0
                value <= 100.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `soil_moisture_content_percent_at_saturation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `soil_moisture_content_percent_at_saturation`')
            if value > 100.0:
                raise ValueError('value need to be smaller 100.0 '
                                 'for field `soil_moisture_content_percent_at_saturation`')

        self._data["Soil Moisture Content Percent at Saturation"] = value

    @property
    def kusudaachenbach_average_surface_temperature(self):
        """Get kusudaachenbach_average_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Surface Temperature"]

    @kusudaachenbach_average_surface_temperature.setter
    def kusudaachenbach_average_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_surface_temperature`
        This is the parameter for average annual surface temperature
        This is an optional input in that if it is missing, a
        Site:GroundTemperature:Shallow object must be found in the input
        The undisturbed ground temperature will be approximated from this object

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_surface_temperature`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Surface Temperature"] = value

    @property
    def kusudaachenbach_average_amplitude_of_surface_temperature(self):
        """Get kusudaachenbach_average_amplitude_of_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_average_amplitude_of_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"]

    @kusudaachenbach_average_amplitude_of_surface_temperature.setter
    def kusudaachenbach_average_amplitude_of_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`
        This is the parameter for annual average amplitude from average surface temperature
        This is an optional input in that if it is missing, a
        Site:GroundTemperature:Shallow object must be found in the input
        The undisturbed ground temperature will be approximated from this object

        Args:
            value (float): value for IDD Field `kusudaachenbach_average_amplitude_of_surface_temperature`
                Unit: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_average_amplitude_of_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Average Amplitude of Surface Temperature"] = value

    @property
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self):
        """Get kusudaachenbach_phase_shift_of_minimum_surface_temperature

        Returns:
            float: the value of `kusudaachenbach_phase_shift_of_minimum_surface_temperature` or None if not set
        """
        return self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"]

    @kusudaachenbach_phase_shift_of_minimum_surface_temperature.setter
    def kusudaachenbach_phase_shift_of_minimum_surface_temperature(self, value=None):
        """  Corresponds to IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`
        This is the parameter for phase shift from minimum surface temperature
        This is an optional input in that if it is missing, a
        Site:GroundTemperature:Shallow object must be found in the input
        The undisturbed ground temperature will be approximated from this object

        Args:
            value (float): value for IDD Field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`
                Unit: days
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `kusudaachenbach_phase_shift_of_minimum_surface_temperature`'.format(value))

        self._data["Kusuda-Achenbach Phase Shift of Minimum Surface Temperature"] = value

    @property
    def evapotranspiration_ground_cover_parameter(self):
        """Get evapotranspiration_ground_cover_parameter

        Returns:
            float: the value of `evapotranspiration_ground_cover_parameter` or None if not set
        """
        return self._data["Evapotranspiration Ground Cover Parameter"]

    @evapotranspiration_ground_cover_parameter.setter
    def evapotranspiration_ground_cover_parameter(self, value=0.4 ):
        """  Corresponds to IDD Field `evapotranspiration_ground_cover_parameter`
        This specifies the ground cover effects during evapotranspiration
        calculations.  The value roughly represents the following cases:
        = 0   : concrete or other solid, non-permeable ground surface material
        = 0.5 : short grass, much like a manicured lawn
        = 1   : standard reference state (12 cm grass)
        = 1.5 : wild growth

        Args:
            value (float): value for IDD Field `evapotranspiration_ground_cover_parameter`
                Default value: 0.4
                value >= 0.0
                value <= 1.5
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `evapotranspiration_ground_cover_parameter`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `evapotranspiration_ground_cover_parameter`')
            if value > 1.5:
                raise ValueError('value need to be smaller 1.5 '
                                 'for field `evapotranspiration_ground_cover_parameter`')

        self._data["Evapotranspiration Ground Cover Parameter"] = value

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
        out.append(self._to_str(self.inlet_node_name))
        out.append(self._to_str(self.outlet_node_name))
        out.append(self._to_str(self.design_flow_rate))
        out.append(self._to_str(self.trench_length_in_pipe_axial_direction))
        out.append(self._to_str(self.number_of_trenches))
        out.append(self._to_str(self.horizontal_spacing_between_pipes))
        out.append(self._to_str(self.pipe_inner_diameter))
        out.append(self._to_str(self.pipe_outer_diameter))
        out.append(self._to_str(self.burial_depth))
        out.append(self._to_str(self.soil_thermal_conductivity))
        out.append(self._to_str(self.soil_density))
        out.append(self._to_str(self.soil_specific_heat))
        out.append(self._to_str(self.pipe_thermal_conductivity))
        out.append(self._to_str(self.pipe_density))
        out.append(self._to_str(self.pipe_specific_heat))
        out.append(self._to_str(self.soil_moisture_content_percent))
        out.append(self._to_str(self.soil_moisture_content_percent_at_saturation))
        out.append(self._to_str(self.kusudaachenbach_average_surface_temperature))
        out.append(self._to_str(self.kusudaachenbach_average_amplitude_of_surface_temperature))
        out.append(self._to_str(self.kusudaachenbach_phase_shift_of_minimum_surface_temperature))
        out.append(self._to_str(self.evapotranspiration_ground_cover_parameter))
        return ",".join(out)