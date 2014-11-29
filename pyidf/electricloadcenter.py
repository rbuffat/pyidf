from collections import OrderedDict

class ElectricLoadCenterGenerators(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Generators`
        List of electric power generators to include in the simulation including the name and
        type of each generators along with availability schedule, rated power output,
        and thermal-to-electrical power ratio.
    """
    internal_name = "ElectricLoadCenter:Generators"
    field_count = 151

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Generators`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Generator 1 Name"] = None
        self._data["Generator 1 Object Type"] = None
        self._data["Generator 1 Rated Electric Power Output"] = None
        self._data["Generator 1 Availability Schedule Name"] = None
        self._data["Generator 1 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 2 Name"] = None
        self._data["Generator 2 Object Type"] = None
        self._data["Generator 2 Rated Electric Power Output"] = None
        self._data["Generator 2 Availability Schedule Name"] = None
        self._data["Generator 2 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 3 Name"] = None
        self._data["Generator 3 Object Type"] = None
        self._data["Generator 3 Rated Electric Power Output"] = None
        self._data["Generator 3 Availability Schedule Name"] = None
        self._data["Generator 3 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 4 Name"] = None
        self._data["Generator 4 Object Type"] = None
        self._data["Generator 4 Rated Electric Power Output"] = None
        self._data["Generator 4 Availability Schedule Name"] = None
        self._data["Generator 4 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 5 Name"] = None
        self._data["Generator 5 Object Type"] = None
        self._data["Generator 5 Rated Electric Power Output"] = None
        self._data["Generator 5 Availability Schedule Name"] = None
        self._data["Generator 5 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 6 Name"] = None
        self._data["Generator 6 Object Type"] = None
        self._data["Generator 6 Rated Electric Power Output"] = None
        self._data["Generator 6 Availability Schedule Name"] = None
        self._data["Generator 6 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 7 Name"] = None
        self._data["Generator 7 Object Type"] = None
        self._data["Generator 7 Rated Electric Power Output"] = None
        self._data["Generator 7 Availability Schedule Name"] = None
        self._data["Generator 7 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 8 Name"] = None
        self._data["Generator 8 Object Type"] = None
        self._data["Generator 8 Rated Electric Power Output"] = None
        self._data["Generator 8 Availability Schedule Name"] = None
        self._data["Generator 8 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 9 Name"] = None
        self._data["Generator 9 Object Type"] = None
        self._data["Generator 9 Rated Electric Power Output"] = None
        self._data["Generator 9 Availability Schedule Name"] = None
        self._data["Generator 9 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 10 Name"] = None
        self._data["Generator 10 Object Type"] = None
        self._data["Generator 10 Rated Electric Power Output"] = None
        self._data["Generator 10 Availability Schedule Name"] = None
        self._data["Generator 10 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 11 Name"] = None
        self._data["Generator 11 Object Type"] = None
        self._data["Generator 11 Rated Electric Power Output"] = None
        self._data["Generator 11 Availability Schedule Name"] = None
        self._data["Generator 11 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 12 Name"] = None
        self._data["Generator 12 Object Type"] = None
        self._data["Generator 12 Rated Electric Power Output"] = None
        self._data["Generator 12 Availability Schedule Name"] = None
        self._data["Generator 12 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 13 Name"] = None
        self._data["Generator 13 Object Type"] = None
        self._data["Generator 13 Rated Electric Power Output"] = None
        self._data["Generator 13 Availability Schedule Name"] = None
        self._data["Generator 13 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 14 Name"] = None
        self._data["Generator 14 Object Type"] = None
        self._data["Generator 14 Rated Electric Power Output"] = None
        self._data["Generator 14 Availability Schedule Name"] = None
        self._data["Generator 14 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 15 Name"] = None
        self._data["Generator 15 Object Type"] = None
        self._data["Generator 15 Rated Electric Power Output"] = None
        self._data["Generator 15 Availability Schedule Name"] = None
        self._data["Generator 15 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 16 Name"] = None
        self._data["Generator 16 Object Type"] = None
        self._data["Generator 16 Rated Electric Power Output"] = None
        self._data["Generator 16 Availability Schedule Name"] = None
        self._data["Generator 16 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 17 Name"] = None
        self._data["Generator 17 Object Type"] = None
        self._data["Generator 17 Rated Electric Power Output"] = None
        self._data["Generator 17 Availability Schedule Name"] = None
        self._data["Generator 17 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 18 Name"] = None
        self._data["Generator 18 Object Type"] = None
        self._data["Generator 18 Rated Electric Power Output"] = None
        self._data["Generator 18 Availability Schedule Name"] = None
        self._data["Generator 18 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 19 Name"] = None
        self._data["Generator 19 Object Type"] = None
        self._data["Generator 19 Rated Electric Power Output"] = None
        self._data["Generator 19 Availability Schedule Name"] = None
        self._data["Generator 19 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 20 Name"] = None
        self._data["Generator 20 Object Type"] = None
        self._data["Generator 20 Rated Electric Power Output"] = None
        self._data["Generator 20 Availability Schedule Name"] = None
        self._data["Generator 20 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 21 Name"] = None
        self._data["Generator 21 Object Type"] = None
        self._data["Generator 21 Rated Electric Power Output"] = None
        self._data["Generator 21 Availability Schedule Name"] = None
        self._data["Generator 21 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 22 Name"] = None
        self._data["Generator 22 Object Type"] = None
        self._data["Generator 22 Rated Electric Power Output"] = None
        self._data["Generator 22 Availability Schedule Name"] = None
        self._data["Generator 22 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 23 Name"] = None
        self._data["Generator 23 Object Type"] = None
        self._data["Generator 23 Rated Electric Power Output"] = None
        self._data["Generator 23 Availability Schedule Name"] = None
        self._data["Generator 23 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 24 Name"] = None
        self._data["Generator 24 Object Type"] = None
        self._data["Generator 24 Rated Electric Power Output"] = None
        self._data["Generator 24 Availability Schedule Name"] = None
        self._data["Generator 24 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 25 Name"] = None
        self._data["Generator 25 Object Type"] = None
        self._data["Generator 25 Rated Electric Power Output"] = None
        self._data["Generator 25 Availability Schedule Name"] = None
        self._data["Generator 25 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 26 Name"] = None
        self._data["Generator 26 Object Type"] = None
        self._data["Generator 26 Rated Electric Power Output"] = None
        self._data["Generator 26 Availability Schedule Name"] = None
        self._data["Generator 26 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 27 Name"] = None
        self._data["Generator 27 Object Type"] = None
        self._data["Generator 27 Rated Electric Power Output"] = None
        self._data["Generator 27 Availability Schedule Name"] = None
        self._data["Generator 27 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 28 Name"] = None
        self._data["Generator 28 Object Type"] = None
        self._data["Generator 28 Rated Electric Power Output"] = None
        self._data["Generator 28 Availability Schedule Name"] = None
        self._data["Generator 28 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 29 Name"] = None
        self._data["Generator 29 Object Type"] = None
        self._data["Generator 29 Rated Electric Power Output"] = None
        self._data["Generator 29 Availability Schedule Name"] = None
        self._data["Generator 29 Rated Thermal to Electrical Power Ratio"] = None
        self._data["Generator 30 Name"] = None
        self._data["Generator 30 Object Type"] = None
        self._data["Generator 30 Rated Electric Power Output"] = None
        self._data["Generator 30 Availability Schedule Name"] = None
        self._data["Generator 30 Rated Thermal to Electrical Power Ratio"] = None

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
            self.generator_1_name = None
        else:
            self.generator_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_1_object_type = None
        else:
            self.generator_1_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_1_rated_electric_power_output = None
        else:
            self.generator_1_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_1_availability_schedule_name = None
        else:
            self.generator_1_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_1_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_1_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_2_name = None
        else:
            self.generator_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_2_object_type = None
        else:
            self.generator_2_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_2_rated_electric_power_output = None
        else:
            self.generator_2_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_2_availability_schedule_name = None
        else:
            self.generator_2_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_2_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_2_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_3_name = None
        else:
            self.generator_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_3_object_type = None
        else:
            self.generator_3_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_3_rated_electric_power_output = None
        else:
            self.generator_3_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_3_availability_schedule_name = None
        else:
            self.generator_3_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_3_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_3_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_4_name = None
        else:
            self.generator_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_4_object_type = None
        else:
            self.generator_4_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_4_rated_electric_power_output = None
        else:
            self.generator_4_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_4_availability_schedule_name = None
        else:
            self.generator_4_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_4_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_4_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_5_name = None
        else:
            self.generator_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_5_object_type = None
        else:
            self.generator_5_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_5_rated_electric_power_output = None
        else:
            self.generator_5_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_5_availability_schedule_name = None
        else:
            self.generator_5_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_5_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_5_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_6_name = None
        else:
            self.generator_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_6_object_type = None
        else:
            self.generator_6_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_6_rated_electric_power_output = None
        else:
            self.generator_6_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_6_availability_schedule_name = None
        else:
            self.generator_6_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_6_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_6_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_7_name = None
        else:
            self.generator_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_7_object_type = None
        else:
            self.generator_7_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_7_rated_electric_power_output = None
        else:
            self.generator_7_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_7_availability_schedule_name = None
        else:
            self.generator_7_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_7_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_7_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_8_name = None
        else:
            self.generator_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_8_object_type = None
        else:
            self.generator_8_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_8_rated_electric_power_output = None
        else:
            self.generator_8_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_8_availability_schedule_name = None
        else:
            self.generator_8_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_8_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_8_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_9_name = None
        else:
            self.generator_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_9_object_type = None
        else:
            self.generator_9_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_9_rated_electric_power_output = None
        else:
            self.generator_9_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_9_availability_schedule_name = None
        else:
            self.generator_9_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_9_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_9_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_10_name = None
        else:
            self.generator_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_10_object_type = None
        else:
            self.generator_10_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_10_rated_electric_power_output = None
        else:
            self.generator_10_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_10_availability_schedule_name = None
        else:
            self.generator_10_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_10_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_10_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_11_name = None
        else:
            self.generator_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_11_object_type = None
        else:
            self.generator_11_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_11_rated_electric_power_output = None
        else:
            self.generator_11_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_11_availability_schedule_name = None
        else:
            self.generator_11_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_11_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_11_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_12_name = None
        else:
            self.generator_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_12_object_type = None
        else:
            self.generator_12_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_12_rated_electric_power_output = None
        else:
            self.generator_12_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_12_availability_schedule_name = None
        else:
            self.generator_12_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_12_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_12_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_13_name = None
        else:
            self.generator_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_13_object_type = None
        else:
            self.generator_13_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_13_rated_electric_power_output = None
        else:
            self.generator_13_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_13_availability_schedule_name = None
        else:
            self.generator_13_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_13_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_13_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_14_name = None
        else:
            self.generator_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_14_object_type = None
        else:
            self.generator_14_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_14_rated_electric_power_output = None
        else:
            self.generator_14_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_14_availability_schedule_name = None
        else:
            self.generator_14_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_14_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_14_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_15_name = None
        else:
            self.generator_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_15_object_type = None
        else:
            self.generator_15_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_15_rated_electric_power_output = None
        else:
            self.generator_15_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_15_availability_schedule_name = None
        else:
            self.generator_15_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_15_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_15_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_16_name = None
        else:
            self.generator_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_16_object_type = None
        else:
            self.generator_16_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_16_rated_electric_power_output = None
        else:
            self.generator_16_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_16_availability_schedule_name = None
        else:
            self.generator_16_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_16_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_16_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_17_name = None
        else:
            self.generator_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_17_object_type = None
        else:
            self.generator_17_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_17_rated_electric_power_output = None
        else:
            self.generator_17_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_17_availability_schedule_name = None
        else:
            self.generator_17_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_17_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_17_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_18_name = None
        else:
            self.generator_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_18_object_type = None
        else:
            self.generator_18_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_18_rated_electric_power_output = None
        else:
            self.generator_18_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_18_availability_schedule_name = None
        else:
            self.generator_18_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_18_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_18_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_19_name = None
        else:
            self.generator_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_19_object_type = None
        else:
            self.generator_19_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_19_rated_electric_power_output = None
        else:
            self.generator_19_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_19_availability_schedule_name = None
        else:
            self.generator_19_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_19_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_19_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_20_name = None
        else:
            self.generator_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_20_object_type = None
        else:
            self.generator_20_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_20_rated_electric_power_output = None
        else:
            self.generator_20_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_20_availability_schedule_name = None
        else:
            self.generator_20_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_20_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_20_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_21_name = None
        else:
            self.generator_21_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_21_object_type = None
        else:
            self.generator_21_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_21_rated_electric_power_output = None
        else:
            self.generator_21_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_21_availability_schedule_name = None
        else:
            self.generator_21_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_21_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_21_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_22_name = None
        else:
            self.generator_22_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_22_object_type = None
        else:
            self.generator_22_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_22_rated_electric_power_output = None
        else:
            self.generator_22_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_22_availability_schedule_name = None
        else:
            self.generator_22_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_22_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_22_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_23_name = None
        else:
            self.generator_23_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_23_object_type = None
        else:
            self.generator_23_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_23_rated_electric_power_output = None
        else:
            self.generator_23_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_23_availability_schedule_name = None
        else:
            self.generator_23_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_23_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_23_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_24_name = None
        else:
            self.generator_24_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_24_object_type = None
        else:
            self.generator_24_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_24_rated_electric_power_output = None
        else:
            self.generator_24_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_24_availability_schedule_name = None
        else:
            self.generator_24_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_24_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_24_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_25_name = None
        else:
            self.generator_25_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_25_object_type = None
        else:
            self.generator_25_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_25_rated_electric_power_output = None
        else:
            self.generator_25_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_25_availability_schedule_name = None
        else:
            self.generator_25_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_25_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_25_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_26_name = None
        else:
            self.generator_26_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_26_object_type = None
        else:
            self.generator_26_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_26_rated_electric_power_output = None
        else:
            self.generator_26_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_26_availability_schedule_name = None
        else:
            self.generator_26_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_26_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_26_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_27_name = None
        else:
            self.generator_27_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_27_object_type = None
        else:
            self.generator_27_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_27_rated_electric_power_output = None
        else:
            self.generator_27_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_27_availability_schedule_name = None
        else:
            self.generator_27_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_27_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_27_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_28_name = None
        else:
            self.generator_28_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_28_object_type = None
        else:
            self.generator_28_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_28_rated_electric_power_output = None
        else:
            self.generator_28_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_28_availability_schedule_name = None
        else:
            self.generator_28_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_28_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_28_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_29_name = None
        else:
            self.generator_29_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_29_object_type = None
        else:
            self.generator_29_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_29_rated_electric_power_output = None
        else:
            self.generator_29_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_29_availability_schedule_name = None
        else:
            self.generator_29_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_29_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_29_rated_thermal_to_electrical_power_ratio = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_30_name = None
        else:
            self.generator_30_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_30_object_type = None
        else:
            self.generator_30_object_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_30_rated_electric_power_output = None
        else:
            self.generator_30_rated_electric_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_30_availability_schedule_name = None
        else:
            self.generator_30_availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_30_rated_thermal_to_electrical_power_ratio = None
        else:
            self.generator_30_rated_thermal_to_electrical_power_ratio = vals[i]
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
    def generator_1_name(self):
        """Get generator_1_name

        Returns:
            str: the value of `generator_1_name` or None if not set
        """
        return self._data["Generator 1 Name"]

    @generator_1_name.setter
    def generator_1_name(self, value=None):
        """  Corresponds to IDD Field `generator_1_name`

        Args:
            value (str): value for IDD Field `generator_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_1_name`')

        self._data["Generator 1 Name"] = value

    @property
    def generator_1_object_type(self):
        """Get generator_1_object_type

        Returns:
            str: the value of `generator_1_object_type` or None if not set
        """
        return self._data["Generator 1 Object Type"]

    @generator_1_object_type.setter
    def generator_1_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_1_object_type`

        Args:
            value (str): value for IDD Field `generator_1_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_1_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_1_object_type`'.format(value))

        self._data["Generator 1 Object Type"] = value

    @property
    def generator_1_rated_electric_power_output(self):
        """Get generator_1_rated_electric_power_output

        Returns:
            float: the value of `generator_1_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 1 Rated Electric Power Output"]

    @generator_1_rated_electric_power_output.setter
    def generator_1_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_1_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_1_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_1_rated_electric_power_output`'.format(value))

        self._data["Generator 1 Rated Electric Power Output"] = value

    @property
    def generator_1_availability_schedule_name(self):
        """Get generator_1_availability_schedule_name

        Returns:
            str: the value of `generator_1_availability_schedule_name` or None if not set
        """
        return self._data["Generator 1 Availability Schedule Name"]

    @generator_1_availability_schedule_name.setter
    def generator_1_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_1_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_1_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_1_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_1_availability_schedule_name`')

        self._data["Generator 1 Availability Schedule Name"] = value

    @property
    def generator_1_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_1_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_1_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 1 Rated Thermal to Electrical Power Ratio"]

    @generator_1_rated_thermal_to_electrical_power_ratio.setter
    def generator_1_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_1_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_1_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_1_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 1 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_2_name(self):
        """Get generator_2_name

        Returns:
            str: the value of `generator_2_name` or None if not set
        """
        return self._data["Generator 2 Name"]

    @generator_2_name.setter
    def generator_2_name(self, value=None):
        """  Corresponds to IDD Field `generator_2_name`

        Args:
            value (str): value for IDD Field `generator_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_2_name`')

        self._data["Generator 2 Name"] = value

    @property
    def generator_2_object_type(self):
        """Get generator_2_object_type

        Returns:
            str: the value of `generator_2_object_type` or None if not set
        """
        return self._data["Generator 2 Object Type"]

    @generator_2_object_type.setter
    def generator_2_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_2_object_type`

        Args:
            value (str): value for IDD Field `generator_2_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_2_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_2_object_type`'.format(value))

        self._data["Generator 2 Object Type"] = value

    @property
    def generator_2_rated_electric_power_output(self):
        """Get generator_2_rated_electric_power_output

        Returns:
            float: the value of `generator_2_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 2 Rated Electric Power Output"]

    @generator_2_rated_electric_power_output.setter
    def generator_2_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_2_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_2_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_2_rated_electric_power_output`'.format(value))

        self._data["Generator 2 Rated Electric Power Output"] = value

    @property
    def generator_2_availability_schedule_name(self):
        """Get generator_2_availability_schedule_name

        Returns:
            str: the value of `generator_2_availability_schedule_name` or None if not set
        """
        return self._data["Generator 2 Availability Schedule Name"]

    @generator_2_availability_schedule_name.setter
    def generator_2_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_2_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_2_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_2_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_2_availability_schedule_name`')

        self._data["Generator 2 Availability Schedule Name"] = value

    @property
    def generator_2_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_2_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_2_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 2 Rated Thermal to Electrical Power Ratio"]

    @generator_2_rated_thermal_to_electrical_power_ratio.setter
    def generator_2_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_2_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_2_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_2_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 2 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_3_name(self):
        """Get generator_3_name

        Returns:
            str: the value of `generator_3_name` or None if not set
        """
        return self._data["Generator 3 Name"]

    @generator_3_name.setter
    def generator_3_name(self, value=None):
        """  Corresponds to IDD Field `generator_3_name`

        Args:
            value (str): value for IDD Field `generator_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_3_name`')

        self._data["Generator 3 Name"] = value

    @property
    def generator_3_object_type(self):
        """Get generator_3_object_type

        Returns:
            str: the value of `generator_3_object_type` or None if not set
        """
        return self._data["Generator 3 Object Type"]

    @generator_3_object_type.setter
    def generator_3_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_3_object_type`

        Args:
            value (str): value for IDD Field `generator_3_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_3_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_3_object_type`'.format(value))

        self._data["Generator 3 Object Type"] = value

    @property
    def generator_3_rated_electric_power_output(self):
        """Get generator_3_rated_electric_power_output

        Returns:
            float: the value of `generator_3_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 3 Rated Electric Power Output"]

    @generator_3_rated_electric_power_output.setter
    def generator_3_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_3_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_3_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_3_rated_electric_power_output`'.format(value))

        self._data["Generator 3 Rated Electric Power Output"] = value

    @property
    def generator_3_availability_schedule_name(self):
        """Get generator_3_availability_schedule_name

        Returns:
            str: the value of `generator_3_availability_schedule_name` or None if not set
        """
        return self._data["Generator 3 Availability Schedule Name"]

    @generator_3_availability_schedule_name.setter
    def generator_3_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_3_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_3_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_3_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_3_availability_schedule_name`')

        self._data["Generator 3 Availability Schedule Name"] = value

    @property
    def generator_3_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_3_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_3_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 3 Rated Thermal to Electrical Power Ratio"]

    @generator_3_rated_thermal_to_electrical_power_ratio.setter
    def generator_3_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_3_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_3_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_3_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 3 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_4_name(self):
        """Get generator_4_name

        Returns:
            str: the value of `generator_4_name` or None if not set
        """
        return self._data["Generator 4 Name"]

    @generator_4_name.setter
    def generator_4_name(self, value=None):
        """  Corresponds to IDD Field `generator_4_name`

        Args:
            value (str): value for IDD Field `generator_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_4_name`')

        self._data["Generator 4 Name"] = value

    @property
    def generator_4_object_type(self):
        """Get generator_4_object_type

        Returns:
            str: the value of `generator_4_object_type` or None if not set
        """
        return self._data["Generator 4 Object Type"]

    @generator_4_object_type.setter
    def generator_4_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_4_object_type`

        Args:
            value (str): value for IDD Field `generator_4_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_4_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_4_object_type`'.format(value))

        self._data["Generator 4 Object Type"] = value

    @property
    def generator_4_rated_electric_power_output(self):
        """Get generator_4_rated_electric_power_output

        Returns:
            float: the value of `generator_4_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 4 Rated Electric Power Output"]

    @generator_4_rated_electric_power_output.setter
    def generator_4_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_4_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_4_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_4_rated_electric_power_output`'.format(value))

        self._data["Generator 4 Rated Electric Power Output"] = value

    @property
    def generator_4_availability_schedule_name(self):
        """Get generator_4_availability_schedule_name

        Returns:
            str: the value of `generator_4_availability_schedule_name` or None if not set
        """
        return self._data["Generator 4 Availability Schedule Name"]

    @generator_4_availability_schedule_name.setter
    def generator_4_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_4_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_4_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_4_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_4_availability_schedule_name`')

        self._data["Generator 4 Availability Schedule Name"] = value

    @property
    def generator_4_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_4_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_4_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 4 Rated Thermal to Electrical Power Ratio"]

    @generator_4_rated_thermal_to_electrical_power_ratio.setter
    def generator_4_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_4_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_4_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_4_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 4 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_5_name(self):
        """Get generator_5_name

        Returns:
            str: the value of `generator_5_name` or None if not set
        """
        return self._data["Generator 5 Name"]

    @generator_5_name.setter
    def generator_5_name(self, value=None):
        """  Corresponds to IDD Field `generator_5_name`

        Args:
            value (str): value for IDD Field `generator_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_5_name`')

        self._data["Generator 5 Name"] = value

    @property
    def generator_5_object_type(self):
        """Get generator_5_object_type

        Returns:
            str: the value of `generator_5_object_type` or None if not set
        """
        return self._data["Generator 5 Object Type"]

    @generator_5_object_type.setter
    def generator_5_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_5_object_type`

        Args:
            value (str): value for IDD Field `generator_5_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_5_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_5_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_5_object_type`'.format(value))

        self._data["Generator 5 Object Type"] = value

    @property
    def generator_5_rated_electric_power_output(self):
        """Get generator_5_rated_electric_power_output

        Returns:
            float: the value of `generator_5_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 5 Rated Electric Power Output"]

    @generator_5_rated_electric_power_output.setter
    def generator_5_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_5_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_5_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_5_rated_electric_power_output`'.format(value))

        self._data["Generator 5 Rated Electric Power Output"] = value

    @property
    def generator_5_availability_schedule_name(self):
        """Get generator_5_availability_schedule_name

        Returns:
            str: the value of `generator_5_availability_schedule_name` or None if not set
        """
        return self._data["Generator 5 Availability Schedule Name"]

    @generator_5_availability_schedule_name.setter
    def generator_5_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_5_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_5_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_5_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_5_availability_schedule_name`')

        self._data["Generator 5 Availability Schedule Name"] = value

    @property
    def generator_5_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_5_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_5_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 5 Rated Thermal to Electrical Power Ratio"]

    @generator_5_rated_thermal_to_electrical_power_ratio.setter
    def generator_5_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_5_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_5_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_5_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 5 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_6_name(self):
        """Get generator_6_name

        Returns:
            str: the value of `generator_6_name` or None if not set
        """
        return self._data["Generator 6 Name"]

    @generator_6_name.setter
    def generator_6_name(self, value=None):
        """  Corresponds to IDD Field `generator_6_name`

        Args:
            value (str): value for IDD Field `generator_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_6_name`')

        self._data["Generator 6 Name"] = value

    @property
    def generator_6_object_type(self):
        """Get generator_6_object_type

        Returns:
            str: the value of `generator_6_object_type` or None if not set
        """
        return self._data["Generator 6 Object Type"]

    @generator_6_object_type.setter
    def generator_6_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_6_object_type`

        Args:
            value (str): value for IDD Field `generator_6_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_6_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_6_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_6_object_type`'.format(value))

        self._data["Generator 6 Object Type"] = value

    @property
    def generator_6_rated_electric_power_output(self):
        """Get generator_6_rated_electric_power_output

        Returns:
            float: the value of `generator_6_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 6 Rated Electric Power Output"]

    @generator_6_rated_electric_power_output.setter
    def generator_6_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_6_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_6_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_6_rated_electric_power_output`'.format(value))

        self._data["Generator 6 Rated Electric Power Output"] = value

    @property
    def generator_6_availability_schedule_name(self):
        """Get generator_6_availability_schedule_name

        Returns:
            str: the value of `generator_6_availability_schedule_name` or None if not set
        """
        return self._data["Generator 6 Availability Schedule Name"]

    @generator_6_availability_schedule_name.setter
    def generator_6_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_6_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_6_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_6_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_6_availability_schedule_name`')

        self._data["Generator 6 Availability Schedule Name"] = value

    @property
    def generator_6_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_6_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_6_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 6 Rated Thermal to Electrical Power Ratio"]

    @generator_6_rated_thermal_to_electrical_power_ratio.setter
    def generator_6_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_6_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_6_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_6_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 6 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_7_name(self):
        """Get generator_7_name

        Returns:
            str: the value of `generator_7_name` or None if not set
        """
        return self._data["Generator 7 Name"]

    @generator_7_name.setter
    def generator_7_name(self, value=None):
        """  Corresponds to IDD Field `generator_7_name`

        Args:
            value (str): value for IDD Field `generator_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_7_name`')

        self._data["Generator 7 Name"] = value

    @property
    def generator_7_object_type(self):
        """Get generator_7_object_type

        Returns:
            str: the value of `generator_7_object_type` or None if not set
        """
        return self._data["Generator 7 Object Type"]

    @generator_7_object_type.setter
    def generator_7_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_7_object_type`

        Args:
            value (str): value for IDD Field `generator_7_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_7_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_7_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_7_object_type`'.format(value))

        self._data["Generator 7 Object Type"] = value

    @property
    def generator_7_rated_electric_power_output(self):
        """Get generator_7_rated_electric_power_output

        Returns:
            float: the value of `generator_7_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 7 Rated Electric Power Output"]

    @generator_7_rated_electric_power_output.setter
    def generator_7_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_7_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_7_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_7_rated_electric_power_output`'.format(value))

        self._data["Generator 7 Rated Electric Power Output"] = value

    @property
    def generator_7_availability_schedule_name(self):
        """Get generator_7_availability_schedule_name

        Returns:
            str: the value of `generator_7_availability_schedule_name` or None if not set
        """
        return self._data["Generator 7 Availability Schedule Name"]

    @generator_7_availability_schedule_name.setter
    def generator_7_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_7_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_7_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_7_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_7_availability_schedule_name`')

        self._data["Generator 7 Availability Schedule Name"] = value

    @property
    def generator_7_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_7_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_7_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 7 Rated Thermal to Electrical Power Ratio"]

    @generator_7_rated_thermal_to_electrical_power_ratio.setter
    def generator_7_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_7_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_7_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_7_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 7 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_8_name(self):
        """Get generator_8_name

        Returns:
            str: the value of `generator_8_name` or None if not set
        """
        return self._data["Generator 8 Name"]

    @generator_8_name.setter
    def generator_8_name(self, value=None):
        """  Corresponds to IDD Field `generator_8_name`

        Args:
            value (str): value for IDD Field `generator_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_8_name`')

        self._data["Generator 8 Name"] = value

    @property
    def generator_8_object_type(self):
        """Get generator_8_object_type

        Returns:
            str: the value of `generator_8_object_type` or None if not set
        """
        return self._data["Generator 8 Object Type"]

    @generator_8_object_type.setter
    def generator_8_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_8_object_type`

        Args:
            value (str): value for IDD Field `generator_8_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_8_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_8_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_8_object_type`'.format(value))

        self._data["Generator 8 Object Type"] = value

    @property
    def generator_8_rated_electric_power_output(self):
        """Get generator_8_rated_electric_power_output

        Returns:
            float: the value of `generator_8_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 8 Rated Electric Power Output"]

    @generator_8_rated_electric_power_output.setter
    def generator_8_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_8_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_8_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_8_rated_electric_power_output`'.format(value))

        self._data["Generator 8 Rated Electric Power Output"] = value

    @property
    def generator_8_availability_schedule_name(self):
        """Get generator_8_availability_schedule_name

        Returns:
            str: the value of `generator_8_availability_schedule_name` or None if not set
        """
        return self._data["Generator 8 Availability Schedule Name"]

    @generator_8_availability_schedule_name.setter
    def generator_8_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_8_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_8_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_8_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_8_availability_schedule_name`')

        self._data["Generator 8 Availability Schedule Name"] = value

    @property
    def generator_8_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_8_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_8_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 8 Rated Thermal to Electrical Power Ratio"]

    @generator_8_rated_thermal_to_electrical_power_ratio.setter
    def generator_8_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_8_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_8_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_8_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 8 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_9_name(self):
        """Get generator_9_name

        Returns:
            str: the value of `generator_9_name` or None if not set
        """
        return self._data["Generator 9 Name"]

    @generator_9_name.setter
    def generator_9_name(self, value=None):
        """  Corresponds to IDD Field `generator_9_name`

        Args:
            value (str): value for IDD Field `generator_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_9_name`')

        self._data["Generator 9 Name"] = value

    @property
    def generator_9_object_type(self):
        """Get generator_9_object_type

        Returns:
            str: the value of `generator_9_object_type` or None if not set
        """
        return self._data["Generator 9 Object Type"]

    @generator_9_object_type.setter
    def generator_9_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_9_object_type`

        Args:
            value (str): value for IDD Field `generator_9_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_9_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_9_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_9_object_type`'.format(value))

        self._data["Generator 9 Object Type"] = value

    @property
    def generator_9_rated_electric_power_output(self):
        """Get generator_9_rated_electric_power_output

        Returns:
            float: the value of `generator_9_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 9 Rated Electric Power Output"]

    @generator_9_rated_electric_power_output.setter
    def generator_9_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_9_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_9_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_9_rated_electric_power_output`'.format(value))

        self._data["Generator 9 Rated Electric Power Output"] = value

    @property
    def generator_9_availability_schedule_name(self):
        """Get generator_9_availability_schedule_name

        Returns:
            str: the value of `generator_9_availability_schedule_name` or None if not set
        """
        return self._data["Generator 9 Availability Schedule Name"]

    @generator_9_availability_schedule_name.setter
    def generator_9_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_9_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_9_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_9_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_9_availability_schedule_name`')

        self._data["Generator 9 Availability Schedule Name"] = value

    @property
    def generator_9_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_9_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_9_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 9 Rated Thermal to Electrical Power Ratio"]

    @generator_9_rated_thermal_to_electrical_power_ratio.setter
    def generator_9_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_9_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_9_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_9_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 9 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_10_name(self):
        """Get generator_10_name

        Returns:
            str: the value of `generator_10_name` or None if not set
        """
        return self._data["Generator 10 Name"]

    @generator_10_name.setter
    def generator_10_name(self, value=None):
        """  Corresponds to IDD Field `generator_10_name`

        Args:
            value (str): value for IDD Field `generator_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_10_name`')

        self._data["Generator 10 Name"] = value

    @property
    def generator_10_object_type(self):
        """Get generator_10_object_type

        Returns:
            str: the value of `generator_10_object_type` or None if not set
        """
        return self._data["Generator 10 Object Type"]

    @generator_10_object_type.setter
    def generator_10_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_10_object_type`

        Args:
            value (str): value for IDD Field `generator_10_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_10_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_10_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_10_object_type`'.format(value))

        self._data["Generator 10 Object Type"] = value

    @property
    def generator_10_rated_electric_power_output(self):
        """Get generator_10_rated_electric_power_output

        Returns:
            float: the value of `generator_10_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 10 Rated Electric Power Output"]

    @generator_10_rated_electric_power_output.setter
    def generator_10_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_10_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_10_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_10_rated_electric_power_output`'.format(value))

        self._data["Generator 10 Rated Electric Power Output"] = value

    @property
    def generator_10_availability_schedule_name(self):
        """Get generator_10_availability_schedule_name

        Returns:
            str: the value of `generator_10_availability_schedule_name` or None if not set
        """
        return self._data["Generator 10 Availability Schedule Name"]

    @generator_10_availability_schedule_name.setter
    def generator_10_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_10_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_10_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_10_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_10_availability_schedule_name`')

        self._data["Generator 10 Availability Schedule Name"] = value

    @property
    def generator_10_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_10_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_10_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 10 Rated Thermal to Electrical Power Ratio"]

    @generator_10_rated_thermal_to_electrical_power_ratio.setter
    def generator_10_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_10_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_10_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_10_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 10 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_11_name(self):
        """Get generator_11_name

        Returns:
            str: the value of `generator_11_name` or None if not set
        """
        return self._data["Generator 11 Name"]

    @generator_11_name.setter
    def generator_11_name(self, value=None):
        """  Corresponds to IDD Field `generator_11_name`

        Args:
            value (str): value for IDD Field `generator_11_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_11_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_11_name`')

        self._data["Generator 11 Name"] = value

    @property
    def generator_11_object_type(self):
        """Get generator_11_object_type

        Returns:
            str: the value of `generator_11_object_type` or None if not set
        """
        return self._data["Generator 11 Object Type"]

    @generator_11_object_type.setter
    def generator_11_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_11_object_type`

        Args:
            value (str): value for IDD Field `generator_11_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_11_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_11_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_11_object_type`'.format(value))

        self._data["Generator 11 Object Type"] = value

    @property
    def generator_11_rated_electric_power_output(self):
        """Get generator_11_rated_electric_power_output

        Returns:
            float: the value of `generator_11_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 11 Rated Electric Power Output"]

    @generator_11_rated_electric_power_output.setter
    def generator_11_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_11_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_11_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_11_rated_electric_power_output`'.format(value))

        self._data["Generator 11 Rated Electric Power Output"] = value

    @property
    def generator_11_availability_schedule_name(self):
        """Get generator_11_availability_schedule_name

        Returns:
            str: the value of `generator_11_availability_schedule_name` or None if not set
        """
        return self._data["Generator 11 Availability Schedule Name"]

    @generator_11_availability_schedule_name.setter
    def generator_11_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_11_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_11_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_11_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_11_availability_schedule_name`')

        self._data["Generator 11 Availability Schedule Name"] = value

    @property
    def generator_11_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_11_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_11_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 11 Rated Thermal to Electrical Power Ratio"]

    @generator_11_rated_thermal_to_electrical_power_ratio.setter
    def generator_11_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_11_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_11_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_11_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 11 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_12_name(self):
        """Get generator_12_name

        Returns:
            str: the value of `generator_12_name` or None if not set
        """
        return self._data["Generator 12 Name"]

    @generator_12_name.setter
    def generator_12_name(self, value=None):
        """  Corresponds to IDD Field `generator_12_name`

        Args:
            value (str): value for IDD Field `generator_12_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_12_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_12_name`')

        self._data["Generator 12 Name"] = value

    @property
    def generator_12_object_type(self):
        """Get generator_12_object_type

        Returns:
            str: the value of `generator_12_object_type` or None if not set
        """
        return self._data["Generator 12 Object Type"]

    @generator_12_object_type.setter
    def generator_12_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_12_object_type`

        Args:
            value (str): value for IDD Field `generator_12_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_12_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_12_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_12_object_type`'.format(value))

        self._data["Generator 12 Object Type"] = value

    @property
    def generator_12_rated_electric_power_output(self):
        """Get generator_12_rated_electric_power_output

        Returns:
            float: the value of `generator_12_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 12 Rated Electric Power Output"]

    @generator_12_rated_electric_power_output.setter
    def generator_12_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_12_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_12_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_12_rated_electric_power_output`'.format(value))

        self._data["Generator 12 Rated Electric Power Output"] = value

    @property
    def generator_12_availability_schedule_name(self):
        """Get generator_12_availability_schedule_name

        Returns:
            str: the value of `generator_12_availability_schedule_name` or None if not set
        """
        return self._data["Generator 12 Availability Schedule Name"]

    @generator_12_availability_schedule_name.setter
    def generator_12_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_12_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_12_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_12_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_12_availability_schedule_name`')

        self._data["Generator 12 Availability Schedule Name"] = value

    @property
    def generator_12_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_12_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_12_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 12 Rated Thermal to Electrical Power Ratio"]

    @generator_12_rated_thermal_to_electrical_power_ratio.setter
    def generator_12_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_12_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_12_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_12_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 12 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_13_name(self):
        """Get generator_13_name

        Returns:
            str: the value of `generator_13_name` or None if not set
        """
        return self._data["Generator 13 Name"]

    @generator_13_name.setter
    def generator_13_name(self, value=None):
        """  Corresponds to IDD Field `generator_13_name`

        Args:
            value (str): value for IDD Field `generator_13_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_13_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_13_name`')

        self._data["Generator 13 Name"] = value

    @property
    def generator_13_object_type(self):
        """Get generator_13_object_type

        Returns:
            str: the value of `generator_13_object_type` or None if not set
        """
        return self._data["Generator 13 Object Type"]

    @generator_13_object_type.setter
    def generator_13_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_13_object_type`

        Args:
            value (str): value for IDD Field `generator_13_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_13_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_13_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_13_object_type`'.format(value))

        self._data["Generator 13 Object Type"] = value

    @property
    def generator_13_rated_electric_power_output(self):
        """Get generator_13_rated_electric_power_output

        Returns:
            float: the value of `generator_13_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 13 Rated Electric Power Output"]

    @generator_13_rated_electric_power_output.setter
    def generator_13_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_13_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_13_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_13_rated_electric_power_output`'.format(value))

        self._data["Generator 13 Rated Electric Power Output"] = value

    @property
    def generator_13_availability_schedule_name(self):
        """Get generator_13_availability_schedule_name

        Returns:
            str: the value of `generator_13_availability_schedule_name` or None if not set
        """
        return self._data["Generator 13 Availability Schedule Name"]

    @generator_13_availability_schedule_name.setter
    def generator_13_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_13_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_13_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_13_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_13_availability_schedule_name`')

        self._data["Generator 13 Availability Schedule Name"] = value

    @property
    def generator_13_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_13_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_13_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 13 Rated Thermal to Electrical Power Ratio"]

    @generator_13_rated_thermal_to_electrical_power_ratio.setter
    def generator_13_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_13_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_13_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_13_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 13 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_14_name(self):
        """Get generator_14_name

        Returns:
            str: the value of `generator_14_name` or None if not set
        """
        return self._data["Generator 14 Name"]

    @generator_14_name.setter
    def generator_14_name(self, value=None):
        """  Corresponds to IDD Field `generator_14_name`

        Args:
            value (str): value for IDD Field `generator_14_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_14_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_14_name`')

        self._data["Generator 14 Name"] = value

    @property
    def generator_14_object_type(self):
        """Get generator_14_object_type

        Returns:
            str: the value of `generator_14_object_type` or None if not set
        """
        return self._data["Generator 14 Object Type"]

    @generator_14_object_type.setter
    def generator_14_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_14_object_type`

        Args:
            value (str): value for IDD Field `generator_14_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_14_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_14_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_14_object_type`'.format(value))

        self._data["Generator 14 Object Type"] = value

    @property
    def generator_14_rated_electric_power_output(self):
        """Get generator_14_rated_electric_power_output

        Returns:
            float: the value of `generator_14_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 14 Rated Electric Power Output"]

    @generator_14_rated_electric_power_output.setter
    def generator_14_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_14_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_14_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_14_rated_electric_power_output`'.format(value))

        self._data["Generator 14 Rated Electric Power Output"] = value

    @property
    def generator_14_availability_schedule_name(self):
        """Get generator_14_availability_schedule_name

        Returns:
            str: the value of `generator_14_availability_schedule_name` or None if not set
        """
        return self._data["Generator 14 Availability Schedule Name"]

    @generator_14_availability_schedule_name.setter
    def generator_14_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_14_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_14_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_14_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_14_availability_schedule_name`')

        self._data["Generator 14 Availability Schedule Name"] = value

    @property
    def generator_14_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_14_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_14_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 14 Rated Thermal to Electrical Power Ratio"]

    @generator_14_rated_thermal_to_electrical_power_ratio.setter
    def generator_14_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_14_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_14_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_14_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 14 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_15_name(self):
        """Get generator_15_name

        Returns:
            str: the value of `generator_15_name` or None if not set
        """
        return self._data["Generator 15 Name"]

    @generator_15_name.setter
    def generator_15_name(self, value=None):
        """  Corresponds to IDD Field `generator_15_name`

        Args:
            value (str): value for IDD Field `generator_15_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_15_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_15_name`')

        self._data["Generator 15 Name"] = value

    @property
    def generator_15_object_type(self):
        """Get generator_15_object_type

        Returns:
            str: the value of `generator_15_object_type` or None if not set
        """
        return self._data["Generator 15 Object Type"]

    @generator_15_object_type.setter
    def generator_15_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_15_object_type`

        Args:
            value (str): value for IDD Field `generator_15_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_15_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_15_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_15_object_type`'.format(value))

        self._data["Generator 15 Object Type"] = value

    @property
    def generator_15_rated_electric_power_output(self):
        """Get generator_15_rated_electric_power_output

        Returns:
            float: the value of `generator_15_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 15 Rated Electric Power Output"]

    @generator_15_rated_electric_power_output.setter
    def generator_15_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_15_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_15_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_15_rated_electric_power_output`'.format(value))

        self._data["Generator 15 Rated Electric Power Output"] = value

    @property
    def generator_15_availability_schedule_name(self):
        """Get generator_15_availability_schedule_name

        Returns:
            str: the value of `generator_15_availability_schedule_name` or None if not set
        """
        return self._data["Generator 15 Availability Schedule Name"]

    @generator_15_availability_schedule_name.setter
    def generator_15_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_15_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_15_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_15_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_15_availability_schedule_name`')

        self._data["Generator 15 Availability Schedule Name"] = value

    @property
    def generator_15_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_15_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_15_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 15 Rated Thermal to Electrical Power Ratio"]

    @generator_15_rated_thermal_to_electrical_power_ratio.setter
    def generator_15_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_15_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_15_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_15_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 15 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_16_name(self):
        """Get generator_16_name

        Returns:
            str: the value of `generator_16_name` or None if not set
        """
        return self._data["Generator 16 Name"]

    @generator_16_name.setter
    def generator_16_name(self, value=None):
        """  Corresponds to IDD Field `generator_16_name`

        Args:
            value (str): value for IDD Field `generator_16_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_16_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_16_name`')

        self._data["Generator 16 Name"] = value

    @property
    def generator_16_object_type(self):
        """Get generator_16_object_type

        Returns:
            str: the value of `generator_16_object_type` or None if not set
        """
        return self._data["Generator 16 Object Type"]

    @generator_16_object_type.setter
    def generator_16_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_16_object_type`

        Args:
            value (str): value for IDD Field `generator_16_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_16_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_16_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_16_object_type`'.format(value))

        self._data["Generator 16 Object Type"] = value

    @property
    def generator_16_rated_electric_power_output(self):
        """Get generator_16_rated_electric_power_output

        Returns:
            float: the value of `generator_16_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 16 Rated Electric Power Output"]

    @generator_16_rated_electric_power_output.setter
    def generator_16_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_16_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_16_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_16_rated_electric_power_output`'.format(value))

        self._data["Generator 16 Rated Electric Power Output"] = value

    @property
    def generator_16_availability_schedule_name(self):
        """Get generator_16_availability_schedule_name

        Returns:
            str: the value of `generator_16_availability_schedule_name` or None if not set
        """
        return self._data["Generator 16 Availability Schedule Name"]

    @generator_16_availability_schedule_name.setter
    def generator_16_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_16_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_16_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_16_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_16_availability_schedule_name`')

        self._data["Generator 16 Availability Schedule Name"] = value

    @property
    def generator_16_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_16_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_16_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 16 Rated Thermal to Electrical Power Ratio"]

    @generator_16_rated_thermal_to_electrical_power_ratio.setter
    def generator_16_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_16_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_16_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_16_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 16 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_17_name(self):
        """Get generator_17_name

        Returns:
            str: the value of `generator_17_name` or None if not set
        """
        return self._data["Generator 17 Name"]

    @generator_17_name.setter
    def generator_17_name(self, value=None):
        """  Corresponds to IDD Field `generator_17_name`

        Args:
            value (str): value for IDD Field `generator_17_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_17_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_17_name`')

        self._data["Generator 17 Name"] = value

    @property
    def generator_17_object_type(self):
        """Get generator_17_object_type

        Returns:
            str: the value of `generator_17_object_type` or None if not set
        """
        return self._data["Generator 17 Object Type"]

    @generator_17_object_type.setter
    def generator_17_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_17_object_type`

        Args:
            value (str): value for IDD Field `generator_17_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_17_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_17_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_17_object_type`'.format(value))

        self._data["Generator 17 Object Type"] = value

    @property
    def generator_17_rated_electric_power_output(self):
        """Get generator_17_rated_electric_power_output

        Returns:
            float: the value of `generator_17_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 17 Rated Electric Power Output"]

    @generator_17_rated_electric_power_output.setter
    def generator_17_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_17_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_17_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_17_rated_electric_power_output`'.format(value))

        self._data["Generator 17 Rated Electric Power Output"] = value

    @property
    def generator_17_availability_schedule_name(self):
        """Get generator_17_availability_schedule_name

        Returns:
            str: the value of `generator_17_availability_schedule_name` or None if not set
        """
        return self._data["Generator 17 Availability Schedule Name"]

    @generator_17_availability_schedule_name.setter
    def generator_17_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_17_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_17_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_17_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_17_availability_schedule_name`')

        self._data["Generator 17 Availability Schedule Name"] = value

    @property
    def generator_17_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_17_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_17_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 17 Rated Thermal to Electrical Power Ratio"]

    @generator_17_rated_thermal_to_electrical_power_ratio.setter
    def generator_17_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_17_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_17_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_17_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 17 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_18_name(self):
        """Get generator_18_name

        Returns:
            str: the value of `generator_18_name` or None if not set
        """
        return self._data["Generator 18 Name"]

    @generator_18_name.setter
    def generator_18_name(self, value=None):
        """  Corresponds to IDD Field `generator_18_name`

        Args:
            value (str): value for IDD Field `generator_18_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_18_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_18_name`')

        self._data["Generator 18 Name"] = value

    @property
    def generator_18_object_type(self):
        """Get generator_18_object_type

        Returns:
            str: the value of `generator_18_object_type` or None if not set
        """
        return self._data["Generator 18 Object Type"]

    @generator_18_object_type.setter
    def generator_18_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_18_object_type`

        Args:
            value (str): value for IDD Field `generator_18_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_18_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_18_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_18_object_type`'.format(value))

        self._data["Generator 18 Object Type"] = value

    @property
    def generator_18_rated_electric_power_output(self):
        """Get generator_18_rated_electric_power_output

        Returns:
            float: the value of `generator_18_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 18 Rated Electric Power Output"]

    @generator_18_rated_electric_power_output.setter
    def generator_18_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_18_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_18_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_18_rated_electric_power_output`'.format(value))

        self._data["Generator 18 Rated Electric Power Output"] = value

    @property
    def generator_18_availability_schedule_name(self):
        """Get generator_18_availability_schedule_name

        Returns:
            str: the value of `generator_18_availability_schedule_name` or None if not set
        """
        return self._data["Generator 18 Availability Schedule Name"]

    @generator_18_availability_schedule_name.setter
    def generator_18_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_18_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_18_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_18_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_18_availability_schedule_name`')

        self._data["Generator 18 Availability Schedule Name"] = value

    @property
    def generator_18_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_18_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_18_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 18 Rated Thermal to Electrical Power Ratio"]

    @generator_18_rated_thermal_to_electrical_power_ratio.setter
    def generator_18_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_18_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_18_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_18_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 18 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_19_name(self):
        """Get generator_19_name

        Returns:
            str: the value of `generator_19_name` or None if not set
        """
        return self._data["Generator 19 Name"]

    @generator_19_name.setter
    def generator_19_name(self, value=None):
        """  Corresponds to IDD Field `generator_19_name`

        Args:
            value (str): value for IDD Field `generator_19_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_19_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_19_name`')

        self._data["Generator 19 Name"] = value

    @property
    def generator_19_object_type(self):
        """Get generator_19_object_type

        Returns:
            str: the value of `generator_19_object_type` or None if not set
        """
        return self._data["Generator 19 Object Type"]

    @generator_19_object_type.setter
    def generator_19_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_19_object_type`

        Args:
            value (str): value for IDD Field `generator_19_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_19_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_19_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_19_object_type`'.format(value))

        self._data["Generator 19 Object Type"] = value

    @property
    def generator_19_rated_electric_power_output(self):
        """Get generator_19_rated_electric_power_output

        Returns:
            float: the value of `generator_19_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 19 Rated Electric Power Output"]

    @generator_19_rated_electric_power_output.setter
    def generator_19_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_19_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_19_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_19_rated_electric_power_output`'.format(value))

        self._data["Generator 19 Rated Electric Power Output"] = value

    @property
    def generator_19_availability_schedule_name(self):
        """Get generator_19_availability_schedule_name

        Returns:
            str: the value of `generator_19_availability_schedule_name` or None if not set
        """
        return self._data["Generator 19 Availability Schedule Name"]

    @generator_19_availability_schedule_name.setter
    def generator_19_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_19_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_19_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_19_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_19_availability_schedule_name`')

        self._data["Generator 19 Availability Schedule Name"] = value

    @property
    def generator_19_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_19_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_19_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 19 Rated Thermal to Electrical Power Ratio"]

    @generator_19_rated_thermal_to_electrical_power_ratio.setter
    def generator_19_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_19_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_19_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_19_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 19 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_20_name(self):
        """Get generator_20_name

        Returns:
            str: the value of `generator_20_name` or None if not set
        """
        return self._data["Generator 20 Name"]

    @generator_20_name.setter
    def generator_20_name(self, value=None):
        """  Corresponds to IDD Field `generator_20_name`

        Args:
            value (str): value for IDD Field `generator_20_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_20_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_20_name`')

        self._data["Generator 20 Name"] = value

    @property
    def generator_20_object_type(self):
        """Get generator_20_object_type

        Returns:
            str: the value of `generator_20_object_type` or None if not set
        """
        return self._data["Generator 20 Object Type"]

    @generator_20_object_type.setter
    def generator_20_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_20_object_type`

        Args:
            value (str): value for IDD Field `generator_20_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_20_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_20_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_20_object_type`'.format(value))

        self._data["Generator 20 Object Type"] = value

    @property
    def generator_20_rated_electric_power_output(self):
        """Get generator_20_rated_electric_power_output

        Returns:
            float: the value of `generator_20_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 20 Rated Electric Power Output"]

    @generator_20_rated_electric_power_output.setter
    def generator_20_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_20_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_20_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_20_rated_electric_power_output`'.format(value))

        self._data["Generator 20 Rated Electric Power Output"] = value

    @property
    def generator_20_availability_schedule_name(self):
        """Get generator_20_availability_schedule_name

        Returns:
            str: the value of `generator_20_availability_schedule_name` or None if not set
        """
        return self._data["Generator 20 Availability Schedule Name"]

    @generator_20_availability_schedule_name.setter
    def generator_20_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_20_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_20_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_20_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_20_availability_schedule_name`')

        self._data["Generator 20 Availability Schedule Name"] = value

    @property
    def generator_20_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_20_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_20_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 20 Rated Thermal to Electrical Power Ratio"]

    @generator_20_rated_thermal_to_electrical_power_ratio.setter
    def generator_20_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_20_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_20_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_20_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 20 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_21_name(self):
        """Get generator_21_name

        Returns:
            str: the value of `generator_21_name` or None if not set
        """
        return self._data["Generator 21 Name"]

    @generator_21_name.setter
    def generator_21_name(self, value=None):
        """  Corresponds to IDD Field `generator_21_name`

        Args:
            value (str): value for IDD Field `generator_21_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_21_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_21_name`')

        self._data["Generator 21 Name"] = value

    @property
    def generator_21_object_type(self):
        """Get generator_21_object_type

        Returns:
            str: the value of `generator_21_object_type` or None if not set
        """
        return self._data["Generator 21 Object Type"]

    @generator_21_object_type.setter
    def generator_21_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_21_object_type`

        Args:
            value (str): value for IDD Field `generator_21_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_21_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_21_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_21_object_type`'.format(value))

        self._data["Generator 21 Object Type"] = value

    @property
    def generator_21_rated_electric_power_output(self):
        """Get generator_21_rated_electric_power_output

        Returns:
            float: the value of `generator_21_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 21 Rated Electric Power Output"]

    @generator_21_rated_electric_power_output.setter
    def generator_21_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_21_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_21_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_21_rated_electric_power_output`'.format(value))

        self._data["Generator 21 Rated Electric Power Output"] = value

    @property
    def generator_21_availability_schedule_name(self):
        """Get generator_21_availability_schedule_name

        Returns:
            str: the value of `generator_21_availability_schedule_name` or None if not set
        """
        return self._data["Generator 21 Availability Schedule Name"]

    @generator_21_availability_schedule_name.setter
    def generator_21_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_21_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_21_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_21_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_21_availability_schedule_name`')

        self._data["Generator 21 Availability Schedule Name"] = value

    @property
    def generator_21_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_21_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_21_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 21 Rated Thermal to Electrical Power Ratio"]

    @generator_21_rated_thermal_to_electrical_power_ratio.setter
    def generator_21_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_21_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_21_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_21_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 21 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_22_name(self):
        """Get generator_22_name

        Returns:
            str: the value of `generator_22_name` or None if not set
        """
        return self._data["Generator 22 Name"]

    @generator_22_name.setter
    def generator_22_name(self, value=None):
        """  Corresponds to IDD Field `generator_22_name`

        Args:
            value (str): value for IDD Field `generator_22_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_22_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_22_name`')

        self._data["Generator 22 Name"] = value

    @property
    def generator_22_object_type(self):
        """Get generator_22_object_type

        Returns:
            str: the value of `generator_22_object_type` or None if not set
        """
        return self._data["Generator 22 Object Type"]

    @generator_22_object_type.setter
    def generator_22_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_22_object_type`

        Args:
            value (str): value for IDD Field `generator_22_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_22_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_22_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_22_object_type`'.format(value))

        self._data["Generator 22 Object Type"] = value

    @property
    def generator_22_rated_electric_power_output(self):
        """Get generator_22_rated_electric_power_output

        Returns:
            float: the value of `generator_22_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 22 Rated Electric Power Output"]

    @generator_22_rated_electric_power_output.setter
    def generator_22_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_22_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_22_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_22_rated_electric_power_output`'.format(value))

        self._data["Generator 22 Rated Electric Power Output"] = value

    @property
    def generator_22_availability_schedule_name(self):
        """Get generator_22_availability_schedule_name

        Returns:
            str: the value of `generator_22_availability_schedule_name` or None if not set
        """
        return self._data["Generator 22 Availability Schedule Name"]

    @generator_22_availability_schedule_name.setter
    def generator_22_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_22_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_22_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_22_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_22_availability_schedule_name`')

        self._data["Generator 22 Availability Schedule Name"] = value

    @property
    def generator_22_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_22_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_22_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 22 Rated Thermal to Electrical Power Ratio"]

    @generator_22_rated_thermal_to_electrical_power_ratio.setter
    def generator_22_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_22_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_22_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_22_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 22 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_23_name(self):
        """Get generator_23_name

        Returns:
            str: the value of `generator_23_name` or None if not set
        """
        return self._data["Generator 23 Name"]

    @generator_23_name.setter
    def generator_23_name(self, value=None):
        """  Corresponds to IDD Field `generator_23_name`

        Args:
            value (str): value for IDD Field `generator_23_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_23_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_23_name`')

        self._data["Generator 23 Name"] = value

    @property
    def generator_23_object_type(self):
        """Get generator_23_object_type

        Returns:
            str: the value of `generator_23_object_type` or None if not set
        """
        return self._data["Generator 23 Object Type"]

    @generator_23_object_type.setter
    def generator_23_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_23_object_type`

        Args:
            value (str): value for IDD Field `generator_23_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_23_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_23_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_23_object_type`'.format(value))

        self._data["Generator 23 Object Type"] = value

    @property
    def generator_23_rated_electric_power_output(self):
        """Get generator_23_rated_electric_power_output

        Returns:
            float: the value of `generator_23_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 23 Rated Electric Power Output"]

    @generator_23_rated_electric_power_output.setter
    def generator_23_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_23_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_23_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_23_rated_electric_power_output`'.format(value))

        self._data["Generator 23 Rated Electric Power Output"] = value

    @property
    def generator_23_availability_schedule_name(self):
        """Get generator_23_availability_schedule_name

        Returns:
            str: the value of `generator_23_availability_schedule_name` or None if not set
        """
        return self._data["Generator 23 Availability Schedule Name"]

    @generator_23_availability_schedule_name.setter
    def generator_23_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_23_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_23_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_23_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_23_availability_schedule_name`')

        self._data["Generator 23 Availability Schedule Name"] = value

    @property
    def generator_23_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_23_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_23_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 23 Rated Thermal to Electrical Power Ratio"]

    @generator_23_rated_thermal_to_electrical_power_ratio.setter
    def generator_23_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_23_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_23_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_23_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 23 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_24_name(self):
        """Get generator_24_name

        Returns:
            str: the value of `generator_24_name` or None if not set
        """
        return self._data["Generator 24 Name"]

    @generator_24_name.setter
    def generator_24_name(self, value=None):
        """  Corresponds to IDD Field `generator_24_name`

        Args:
            value (str): value for IDD Field `generator_24_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_24_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_24_name`')

        self._data["Generator 24 Name"] = value

    @property
    def generator_24_object_type(self):
        """Get generator_24_object_type

        Returns:
            str: the value of `generator_24_object_type` or None if not set
        """
        return self._data["Generator 24 Object Type"]

    @generator_24_object_type.setter
    def generator_24_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_24_object_type`

        Args:
            value (str): value for IDD Field `generator_24_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_24_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_24_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_24_object_type`'.format(value))

        self._data["Generator 24 Object Type"] = value

    @property
    def generator_24_rated_electric_power_output(self):
        """Get generator_24_rated_electric_power_output

        Returns:
            float: the value of `generator_24_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 24 Rated Electric Power Output"]

    @generator_24_rated_electric_power_output.setter
    def generator_24_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_24_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_24_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_24_rated_electric_power_output`'.format(value))

        self._data["Generator 24 Rated Electric Power Output"] = value

    @property
    def generator_24_availability_schedule_name(self):
        """Get generator_24_availability_schedule_name

        Returns:
            str: the value of `generator_24_availability_schedule_name` or None if not set
        """
        return self._data["Generator 24 Availability Schedule Name"]

    @generator_24_availability_schedule_name.setter
    def generator_24_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_24_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_24_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_24_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_24_availability_schedule_name`')

        self._data["Generator 24 Availability Schedule Name"] = value

    @property
    def generator_24_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_24_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_24_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 24 Rated Thermal to Electrical Power Ratio"]

    @generator_24_rated_thermal_to_electrical_power_ratio.setter
    def generator_24_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_24_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_24_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_24_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 24 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_25_name(self):
        """Get generator_25_name

        Returns:
            str: the value of `generator_25_name` or None if not set
        """
        return self._data["Generator 25 Name"]

    @generator_25_name.setter
    def generator_25_name(self, value=None):
        """  Corresponds to IDD Field `generator_25_name`

        Args:
            value (str): value for IDD Field `generator_25_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_25_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_25_name`')

        self._data["Generator 25 Name"] = value

    @property
    def generator_25_object_type(self):
        """Get generator_25_object_type

        Returns:
            str: the value of `generator_25_object_type` or None if not set
        """
        return self._data["Generator 25 Object Type"]

    @generator_25_object_type.setter
    def generator_25_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_25_object_type`

        Args:
            value (str): value for IDD Field `generator_25_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_25_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_25_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_25_object_type`'.format(value))

        self._data["Generator 25 Object Type"] = value

    @property
    def generator_25_rated_electric_power_output(self):
        """Get generator_25_rated_electric_power_output

        Returns:
            float: the value of `generator_25_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 25 Rated Electric Power Output"]

    @generator_25_rated_electric_power_output.setter
    def generator_25_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_25_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_25_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_25_rated_electric_power_output`'.format(value))

        self._data["Generator 25 Rated Electric Power Output"] = value

    @property
    def generator_25_availability_schedule_name(self):
        """Get generator_25_availability_schedule_name

        Returns:
            str: the value of `generator_25_availability_schedule_name` or None if not set
        """
        return self._data["Generator 25 Availability Schedule Name"]

    @generator_25_availability_schedule_name.setter
    def generator_25_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_25_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_25_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_25_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_25_availability_schedule_name`')

        self._data["Generator 25 Availability Schedule Name"] = value

    @property
    def generator_25_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_25_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_25_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 25 Rated Thermal to Electrical Power Ratio"]

    @generator_25_rated_thermal_to_electrical_power_ratio.setter
    def generator_25_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_25_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_25_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_25_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 25 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_26_name(self):
        """Get generator_26_name

        Returns:
            str: the value of `generator_26_name` or None if not set
        """
        return self._data["Generator 26 Name"]

    @generator_26_name.setter
    def generator_26_name(self, value=None):
        """  Corresponds to IDD Field `generator_26_name`

        Args:
            value (str): value for IDD Field `generator_26_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_26_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_26_name`')

        self._data["Generator 26 Name"] = value

    @property
    def generator_26_object_type(self):
        """Get generator_26_object_type

        Returns:
            str: the value of `generator_26_object_type` or None if not set
        """
        return self._data["Generator 26 Object Type"]

    @generator_26_object_type.setter
    def generator_26_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_26_object_type`

        Args:
            value (str): value for IDD Field `generator_26_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_26_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_26_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_26_object_type`'.format(value))

        self._data["Generator 26 Object Type"] = value

    @property
    def generator_26_rated_electric_power_output(self):
        """Get generator_26_rated_electric_power_output

        Returns:
            float: the value of `generator_26_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 26 Rated Electric Power Output"]

    @generator_26_rated_electric_power_output.setter
    def generator_26_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_26_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_26_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_26_rated_electric_power_output`'.format(value))

        self._data["Generator 26 Rated Electric Power Output"] = value

    @property
    def generator_26_availability_schedule_name(self):
        """Get generator_26_availability_schedule_name

        Returns:
            str: the value of `generator_26_availability_schedule_name` or None if not set
        """
        return self._data["Generator 26 Availability Schedule Name"]

    @generator_26_availability_schedule_name.setter
    def generator_26_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_26_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_26_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_26_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_26_availability_schedule_name`')

        self._data["Generator 26 Availability Schedule Name"] = value

    @property
    def generator_26_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_26_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_26_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 26 Rated Thermal to Electrical Power Ratio"]

    @generator_26_rated_thermal_to_electrical_power_ratio.setter
    def generator_26_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_26_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_26_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_26_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 26 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_27_name(self):
        """Get generator_27_name

        Returns:
            str: the value of `generator_27_name` or None if not set
        """
        return self._data["Generator 27 Name"]

    @generator_27_name.setter
    def generator_27_name(self, value=None):
        """  Corresponds to IDD Field `generator_27_name`

        Args:
            value (str): value for IDD Field `generator_27_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_27_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_27_name`')

        self._data["Generator 27 Name"] = value

    @property
    def generator_27_object_type(self):
        """Get generator_27_object_type

        Returns:
            str: the value of `generator_27_object_type` or None if not set
        """
        return self._data["Generator 27 Object Type"]

    @generator_27_object_type.setter
    def generator_27_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_27_object_type`

        Args:
            value (str): value for IDD Field `generator_27_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_27_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_27_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_27_object_type`'.format(value))

        self._data["Generator 27 Object Type"] = value

    @property
    def generator_27_rated_electric_power_output(self):
        """Get generator_27_rated_electric_power_output

        Returns:
            float: the value of `generator_27_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 27 Rated Electric Power Output"]

    @generator_27_rated_electric_power_output.setter
    def generator_27_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_27_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_27_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_27_rated_electric_power_output`'.format(value))

        self._data["Generator 27 Rated Electric Power Output"] = value

    @property
    def generator_27_availability_schedule_name(self):
        """Get generator_27_availability_schedule_name

        Returns:
            str: the value of `generator_27_availability_schedule_name` or None if not set
        """
        return self._data["Generator 27 Availability Schedule Name"]

    @generator_27_availability_schedule_name.setter
    def generator_27_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_27_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_27_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_27_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_27_availability_schedule_name`')

        self._data["Generator 27 Availability Schedule Name"] = value

    @property
    def generator_27_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_27_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_27_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 27 Rated Thermal to Electrical Power Ratio"]

    @generator_27_rated_thermal_to_electrical_power_ratio.setter
    def generator_27_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_27_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_27_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_27_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 27 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_28_name(self):
        """Get generator_28_name

        Returns:
            str: the value of `generator_28_name` or None if not set
        """
        return self._data["Generator 28 Name"]

    @generator_28_name.setter
    def generator_28_name(self, value=None):
        """  Corresponds to IDD Field `generator_28_name`

        Args:
            value (str): value for IDD Field `generator_28_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_28_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_28_name`')

        self._data["Generator 28 Name"] = value

    @property
    def generator_28_object_type(self):
        """Get generator_28_object_type

        Returns:
            str: the value of `generator_28_object_type` or None if not set
        """
        return self._data["Generator 28 Object Type"]

    @generator_28_object_type.setter
    def generator_28_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_28_object_type`

        Args:
            value (str): value for IDD Field `generator_28_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_28_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_28_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_28_object_type`'.format(value))

        self._data["Generator 28 Object Type"] = value

    @property
    def generator_28_rated_electric_power_output(self):
        """Get generator_28_rated_electric_power_output

        Returns:
            float: the value of `generator_28_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 28 Rated Electric Power Output"]

    @generator_28_rated_electric_power_output.setter
    def generator_28_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_28_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_28_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_28_rated_electric_power_output`'.format(value))

        self._data["Generator 28 Rated Electric Power Output"] = value

    @property
    def generator_28_availability_schedule_name(self):
        """Get generator_28_availability_schedule_name

        Returns:
            str: the value of `generator_28_availability_schedule_name` or None if not set
        """
        return self._data["Generator 28 Availability Schedule Name"]

    @generator_28_availability_schedule_name.setter
    def generator_28_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_28_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_28_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_28_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_28_availability_schedule_name`')

        self._data["Generator 28 Availability Schedule Name"] = value

    @property
    def generator_28_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_28_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_28_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 28 Rated Thermal to Electrical Power Ratio"]

    @generator_28_rated_thermal_to_electrical_power_ratio.setter
    def generator_28_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_28_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_28_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_28_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 28 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_29_name(self):
        """Get generator_29_name

        Returns:
            str: the value of `generator_29_name` or None if not set
        """
        return self._data["Generator 29 Name"]

    @generator_29_name.setter
    def generator_29_name(self, value=None):
        """  Corresponds to IDD Field `generator_29_name`

        Args:
            value (str): value for IDD Field `generator_29_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_29_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_29_name`')

        self._data["Generator 29 Name"] = value

    @property
    def generator_29_object_type(self):
        """Get generator_29_object_type

        Returns:
            str: the value of `generator_29_object_type` or None if not set
        """
        return self._data["Generator 29 Object Type"]

    @generator_29_object_type.setter
    def generator_29_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_29_object_type`

        Args:
            value (str): value for IDD Field `generator_29_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_29_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_29_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_29_object_type`'.format(value))

        self._data["Generator 29 Object Type"] = value

    @property
    def generator_29_rated_electric_power_output(self):
        """Get generator_29_rated_electric_power_output

        Returns:
            float: the value of `generator_29_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 29 Rated Electric Power Output"]

    @generator_29_rated_electric_power_output.setter
    def generator_29_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_29_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_29_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_29_rated_electric_power_output`'.format(value))

        self._data["Generator 29 Rated Electric Power Output"] = value

    @property
    def generator_29_availability_schedule_name(self):
        """Get generator_29_availability_schedule_name

        Returns:
            str: the value of `generator_29_availability_schedule_name` or None if not set
        """
        return self._data["Generator 29 Availability Schedule Name"]

    @generator_29_availability_schedule_name.setter
    def generator_29_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_29_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_29_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_29_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_29_availability_schedule_name`')

        self._data["Generator 29 Availability Schedule Name"] = value

    @property
    def generator_29_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_29_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_29_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 29 Rated Thermal to Electrical Power Ratio"]

    @generator_29_rated_thermal_to_electrical_power_ratio.setter
    def generator_29_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_29_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_29_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_29_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 29 Rated Thermal to Electrical Power Ratio"] = value

    @property
    def generator_30_name(self):
        """Get generator_30_name

        Returns:
            str: the value of `generator_30_name` or None if not set
        """
        return self._data["Generator 30 Name"]

    @generator_30_name.setter
    def generator_30_name(self, value=None):
        """  Corresponds to IDD Field `generator_30_name`

        Args:
            value (str): value for IDD Field `generator_30_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_30_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_30_name`')

        self._data["Generator 30 Name"] = value

    @property
    def generator_30_object_type(self):
        """Get generator_30_object_type

        Returns:
            str: the value of `generator_30_object_type` or None if not set
        """
        return self._data["Generator 30 Object Type"]

    @generator_30_object_type.setter
    def generator_30_object_type(self, value=None):
        """  Corresponds to IDD Field `generator_30_object_type`

        Args:
            value (str): value for IDD Field `generator_30_object_type`
                Accepted values are:
                      - Generator:InternalCombustionEngine
                      - Generator:CombustionTurbine
                      - Generator:Photovoltaic
                      - Generator:FuelCell
                      - Generator:MicroCHP
                      - Generator:MicroTurbine
                      - Generator:WindTurbine
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_30_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_30_object_type`')
            vals = set()
            vals.add("Generator:InternalCombustionEngine")
            vals.add("Generator:CombustionTurbine")
            vals.add("Generator:Photovoltaic")
            vals.add("Generator:FuelCell")
            vals.add("Generator:MicroCHP")
            vals.add("Generator:MicroTurbine")
            vals.add("Generator:WindTurbine")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_30_object_type`'.format(value))

        self._data["Generator 30 Object Type"] = value

    @property
    def generator_30_rated_electric_power_output(self):
        """Get generator_30_rated_electric_power_output

        Returns:
            float: the value of `generator_30_rated_electric_power_output` or None if not set
        """
        return self._data["Generator 30 Rated Electric Power Output"]

    @generator_30_rated_electric_power_output.setter
    def generator_30_rated_electric_power_output(self, value=None):
        """  Corresponds to IDD Field `generator_30_rated_electric_power_output`

        Args:
            value (float): value for IDD Field `generator_30_rated_electric_power_output`
                Unit: W
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
                                 'for field `generator_30_rated_electric_power_output`'.format(value))

        self._data["Generator 30 Rated Electric Power Output"] = value

    @property
    def generator_30_availability_schedule_name(self):
        """Get generator_30_availability_schedule_name

        Returns:
            str: the value of `generator_30_availability_schedule_name` or None if not set
        """
        return self._data["Generator 30 Availability Schedule Name"]

    @generator_30_availability_schedule_name.setter
    def generator_30_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generator_30_availability_schedule_name`
        Availability schedule name for this generator. Schedule value > 0 means the generator is available.
        If this field is blank, the generator is always available.

        Args:
            value (str): value for IDD Field `generator_30_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_30_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_30_availability_schedule_name`')

        self._data["Generator 30 Availability Schedule Name"] = value

    @property
    def generator_30_rated_thermal_to_electrical_power_ratio(self):
        """Get generator_30_rated_thermal_to_electrical_power_ratio

        Returns:
            float: the value of `generator_30_rated_thermal_to_electrical_power_ratio` or None if not set
        """
        return self._data["Generator 30 Rated Thermal to Electrical Power Ratio"]

    @generator_30_rated_thermal_to_electrical_power_ratio.setter
    def generator_30_rated_thermal_to_electrical_power_ratio(self, value=None):
        """  Corresponds to IDD Field `generator_30_rated_thermal_to_electrical_power_ratio`

        Args:
            value (float): value for IDD Field `generator_30_rated_thermal_to_electrical_power_ratio`
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
                                 'for field `generator_30_rated_thermal_to_electrical_power_ratio`'.format(value))

        self._data["Generator 30 Rated Thermal to Electrical Power Ratio"] = value

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
        out.append(self._to_str(self.generator_1_name))
        out.append(self._to_str(self.generator_1_object_type))
        out.append(self._to_str(self.generator_1_rated_electric_power_output))
        out.append(self._to_str(self.generator_1_availability_schedule_name))
        out.append(self._to_str(self.generator_1_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_2_name))
        out.append(self._to_str(self.generator_2_object_type))
        out.append(self._to_str(self.generator_2_rated_electric_power_output))
        out.append(self._to_str(self.generator_2_availability_schedule_name))
        out.append(self._to_str(self.generator_2_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_3_name))
        out.append(self._to_str(self.generator_3_object_type))
        out.append(self._to_str(self.generator_3_rated_electric_power_output))
        out.append(self._to_str(self.generator_3_availability_schedule_name))
        out.append(self._to_str(self.generator_3_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_4_name))
        out.append(self._to_str(self.generator_4_object_type))
        out.append(self._to_str(self.generator_4_rated_electric_power_output))
        out.append(self._to_str(self.generator_4_availability_schedule_name))
        out.append(self._to_str(self.generator_4_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_5_name))
        out.append(self._to_str(self.generator_5_object_type))
        out.append(self._to_str(self.generator_5_rated_electric_power_output))
        out.append(self._to_str(self.generator_5_availability_schedule_name))
        out.append(self._to_str(self.generator_5_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_6_name))
        out.append(self._to_str(self.generator_6_object_type))
        out.append(self._to_str(self.generator_6_rated_electric_power_output))
        out.append(self._to_str(self.generator_6_availability_schedule_name))
        out.append(self._to_str(self.generator_6_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_7_name))
        out.append(self._to_str(self.generator_7_object_type))
        out.append(self._to_str(self.generator_7_rated_electric_power_output))
        out.append(self._to_str(self.generator_7_availability_schedule_name))
        out.append(self._to_str(self.generator_7_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_8_name))
        out.append(self._to_str(self.generator_8_object_type))
        out.append(self._to_str(self.generator_8_rated_electric_power_output))
        out.append(self._to_str(self.generator_8_availability_schedule_name))
        out.append(self._to_str(self.generator_8_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_9_name))
        out.append(self._to_str(self.generator_9_object_type))
        out.append(self._to_str(self.generator_9_rated_electric_power_output))
        out.append(self._to_str(self.generator_9_availability_schedule_name))
        out.append(self._to_str(self.generator_9_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_10_name))
        out.append(self._to_str(self.generator_10_object_type))
        out.append(self._to_str(self.generator_10_rated_electric_power_output))
        out.append(self._to_str(self.generator_10_availability_schedule_name))
        out.append(self._to_str(self.generator_10_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_11_name))
        out.append(self._to_str(self.generator_11_object_type))
        out.append(self._to_str(self.generator_11_rated_electric_power_output))
        out.append(self._to_str(self.generator_11_availability_schedule_name))
        out.append(self._to_str(self.generator_11_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_12_name))
        out.append(self._to_str(self.generator_12_object_type))
        out.append(self._to_str(self.generator_12_rated_electric_power_output))
        out.append(self._to_str(self.generator_12_availability_schedule_name))
        out.append(self._to_str(self.generator_12_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_13_name))
        out.append(self._to_str(self.generator_13_object_type))
        out.append(self._to_str(self.generator_13_rated_electric_power_output))
        out.append(self._to_str(self.generator_13_availability_schedule_name))
        out.append(self._to_str(self.generator_13_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_14_name))
        out.append(self._to_str(self.generator_14_object_type))
        out.append(self._to_str(self.generator_14_rated_electric_power_output))
        out.append(self._to_str(self.generator_14_availability_schedule_name))
        out.append(self._to_str(self.generator_14_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_15_name))
        out.append(self._to_str(self.generator_15_object_type))
        out.append(self._to_str(self.generator_15_rated_electric_power_output))
        out.append(self._to_str(self.generator_15_availability_schedule_name))
        out.append(self._to_str(self.generator_15_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_16_name))
        out.append(self._to_str(self.generator_16_object_type))
        out.append(self._to_str(self.generator_16_rated_electric_power_output))
        out.append(self._to_str(self.generator_16_availability_schedule_name))
        out.append(self._to_str(self.generator_16_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_17_name))
        out.append(self._to_str(self.generator_17_object_type))
        out.append(self._to_str(self.generator_17_rated_electric_power_output))
        out.append(self._to_str(self.generator_17_availability_schedule_name))
        out.append(self._to_str(self.generator_17_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_18_name))
        out.append(self._to_str(self.generator_18_object_type))
        out.append(self._to_str(self.generator_18_rated_electric_power_output))
        out.append(self._to_str(self.generator_18_availability_schedule_name))
        out.append(self._to_str(self.generator_18_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_19_name))
        out.append(self._to_str(self.generator_19_object_type))
        out.append(self._to_str(self.generator_19_rated_electric_power_output))
        out.append(self._to_str(self.generator_19_availability_schedule_name))
        out.append(self._to_str(self.generator_19_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_20_name))
        out.append(self._to_str(self.generator_20_object_type))
        out.append(self._to_str(self.generator_20_rated_electric_power_output))
        out.append(self._to_str(self.generator_20_availability_schedule_name))
        out.append(self._to_str(self.generator_20_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_21_name))
        out.append(self._to_str(self.generator_21_object_type))
        out.append(self._to_str(self.generator_21_rated_electric_power_output))
        out.append(self._to_str(self.generator_21_availability_schedule_name))
        out.append(self._to_str(self.generator_21_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_22_name))
        out.append(self._to_str(self.generator_22_object_type))
        out.append(self._to_str(self.generator_22_rated_electric_power_output))
        out.append(self._to_str(self.generator_22_availability_schedule_name))
        out.append(self._to_str(self.generator_22_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_23_name))
        out.append(self._to_str(self.generator_23_object_type))
        out.append(self._to_str(self.generator_23_rated_electric_power_output))
        out.append(self._to_str(self.generator_23_availability_schedule_name))
        out.append(self._to_str(self.generator_23_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_24_name))
        out.append(self._to_str(self.generator_24_object_type))
        out.append(self._to_str(self.generator_24_rated_electric_power_output))
        out.append(self._to_str(self.generator_24_availability_schedule_name))
        out.append(self._to_str(self.generator_24_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_25_name))
        out.append(self._to_str(self.generator_25_object_type))
        out.append(self._to_str(self.generator_25_rated_electric_power_output))
        out.append(self._to_str(self.generator_25_availability_schedule_name))
        out.append(self._to_str(self.generator_25_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_26_name))
        out.append(self._to_str(self.generator_26_object_type))
        out.append(self._to_str(self.generator_26_rated_electric_power_output))
        out.append(self._to_str(self.generator_26_availability_schedule_name))
        out.append(self._to_str(self.generator_26_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_27_name))
        out.append(self._to_str(self.generator_27_object_type))
        out.append(self._to_str(self.generator_27_rated_electric_power_output))
        out.append(self._to_str(self.generator_27_availability_schedule_name))
        out.append(self._to_str(self.generator_27_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_28_name))
        out.append(self._to_str(self.generator_28_object_type))
        out.append(self._to_str(self.generator_28_rated_electric_power_output))
        out.append(self._to_str(self.generator_28_availability_schedule_name))
        out.append(self._to_str(self.generator_28_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_29_name))
        out.append(self._to_str(self.generator_29_object_type))
        out.append(self._to_str(self.generator_29_rated_electric_power_output))
        out.append(self._to_str(self.generator_29_availability_schedule_name))
        out.append(self._to_str(self.generator_29_rated_thermal_to_electrical_power_ratio))
        out.append(self._to_str(self.generator_30_name))
        out.append(self._to_str(self.generator_30_object_type))
        out.append(self._to_str(self.generator_30_rated_electric_power_output))
        out.append(self._to_str(self.generator_30_availability_schedule_name))
        out.append(self._to_str(self.generator_30_rated_thermal_to_electrical_power_ratio))
        return ",".join(out)

class ElectricLoadCenterInverterSimple(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Inverter:Simple`
        Electric power inverter to convert from direct current (DC) to alternating current
        (AC) in an electric load center that contains photovoltaic modules. This input
        object is for the simplest inverter model and uses a fixed efficiency.
    """
    internal_name = "ElectricLoadCenter:Inverter:Simple"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Inverter:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Radiative Fraction"] = None
        self._data["Inverter Efficiency"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radiative_fraction = None
        else:
            self.radiative_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inverter_efficiency = None
        else:
            self.inverter_efficiency = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        enter name of zone to receive inverter losses as heat
        if blank then inverter is assumed to be outdoors

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def radiative_fraction(self):
        """Get radiative_fraction

        Returns:
            float: the value of `radiative_fraction` or None if not set
        """
        return self._data["Radiative Fraction"]

    @radiative_fraction.setter
    def radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `radiative_fraction`

        Args:
            value (float): value for IDD Field `radiative_fraction`
                value >= 0.0
                value <= 1.0
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
                                 'for field `radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `radiative_fraction`')

        self._data["Radiative Fraction"] = value

    @property
    def inverter_efficiency(self):
        """Get inverter_efficiency

        Returns:
            float: the value of `inverter_efficiency` or None if not set
        """
        return self._data["Inverter Efficiency"]

    @inverter_efficiency.setter
    def inverter_efficiency(self, value=None):
        """  Corresponds to IDD Field `inverter_efficiency`

        Args:
            value (float): value for IDD Field `inverter_efficiency`
                value >= 0.0
                value <= 1.0
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
                                 'for field `inverter_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `inverter_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `inverter_efficiency`')

        self._data["Inverter Efficiency"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.radiative_fraction))
        out.append(self._to_str(self.inverter_efficiency))
        return ",".join(out)

class ElectricLoadCenterInverterFunctionOfPower(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Inverter:FunctionOfPower`
        Electric power inverter to convert from direct current (DC) to alternating current
        (AC) in an electric load center that contains photovoltaic modules. This input
        object is for an inverter model where efficiency is a function of normalized
        power.
    """
    internal_name = "ElectricLoadCenter:Inverter:FunctionOfPower"
    field_count = 11

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Inverter:FunctionOfPower`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Radiative Fraction"] = None
        self._data["Efficiency Function of Power Curve Name"] = None
        self._data["Rated Maximum Continuous Input Power"] = None
        self._data["Minimum Efficiency"] = None
        self._data["Maximum Efficiency"] = None
        self._data["Minimum Power Output"] = None
        self._data["Maximum Power Output"] = None
        self._data["Ancillary Power Consumed In Standby"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radiative_fraction = None
        else:
            self.radiative_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_function_of_power_curve_name = None
        else:
            self.efficiency_function_of_power_curve_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_maximum_continuous_input_power = None
        else:
            self.rated_maximum_continuous_input_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_efficiency = None
        else:
            self.minimum_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_efficiency = None
        else:
            self.maximum_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.minimum_power_output = None
        else:
            self.minimum_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_power_output = None
        else:
            self.maximum_power_output = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.ancillary_power_consumed_in_standby = None
        else:
            self.ancillary_power_consumed_in_standby = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Enter name of zone to receive inverter losses as heat
        if blank then inverter is assumed to be outdoors

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def radiative_fraction(self):
        """Get radiative_fraction

        Returns:
            float: the value of `radiative_fraction` or None if not set
        """
        return self._data["Radiative Fraction"]

    @radiative_fraction.setter
    def radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `radiative_fraction`

        Args:
            value (float): value for IDD Field `radiative_fraction`
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
                                 'for field `radiative_fraction`'.format(value))

        self._data["Radiative Fraction"] = value

    @property
    def efficiency_function_of_power_curve_name(self):
        """Get efficiency_function_of_power_curve_name

        Returns:
            str: the value of `efficiency_function_of_power_curve_name` or None if not set
        """
        return self._data["Efficiency Function of Power Curve Name"]

    @efficiency_function_of_power_curve_name.setter
    def efficiency_function_of_power_curve_name(self, value=None):
        """  Corresponds to IDD Field `efficiency_function_of_power_curve_name`
        curve describes efficiency as a function of power
        curve is normalized relative to rated power in next field
        Table:OneIndependentVariable object can also be used

        Args:
            value (str): value for IDD Field `efficiency_function_of_power_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `efficiency_function_of_power_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `efficiency_function_of_power_curve_name`')

        self._data["Efficiency Function of Power Curve Name"] = value

    @property
    def rated_maximum_continuous_input_power(self):
        """Get rated_maximum_continuous_input_power

        Returns:
            float: the value of `rated_maximum_continuous_input_power` or None if not set
        """
        return self._data["Rated Maximum Continuous Input Power"]

    @rated_maximum_continuous_input_power.setter
    def rated_maximum_continuous_input_power(self, value=None):
        """  Corresponds to IDD Field `rated_maximum_continuous_input_power`

        Args:
            value (float): value for IDD Field `rated_maximum_continuous_input_power`
                Unit: W
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
                                 'for field `rated_maximum_continuous_input_power`'.format(value))

        self._data["Rated Maximum Continuous Input Power"] = value

    @property
    def minimum_efficiency(self):
        """Get minimum_efficiency

        Returns:
            float: the value of `minimum_efficiency` or None if not set
        """
        return self._data["Minimum Efficiency"]

    @minimum_efficiency.setter
    def minimum_efficiency(self, value=None):
        """  Corresponds to IDD Field `minimum_efficiency`

        Args:
            value (float): value for IDD Field `minimum_efficiency`
                value >= 0.0
                value <= 1.0
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
                                 'for field `minimum_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_efficiency`')

        self._data["Minimum Efficiency"] = value

    @property
    def maximum_efficiency(self):
        """Get maximum_efficiency

        Returns:
            float: the value of `maximum_efficiency` or None if not set
        """
        return self._data["Maximum Efficiency"]

    @maximum_efficiency.setter
    def maximum_efficiency(self, value=None):
        """  Corresponds to IDD Field `maximum_efficiency`

        Args:
            value (float): value for IDD Field `maximum_efficiency`
                value >= 0.0
                value <= 1.0
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
                                 'for field `maximum_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `maximum_efficiency`')

        self._data["Maximum Efficiency"] = value

    @property
    def minimum_power_output(self):
        """Get minimum_power_output

        Returns:
            float: the value of `minimum_power_output` or None if not set
        """
        return self._data["Minimum Power Output"]

    @minimum_power_output.setter
    def minimum_power_output(self, value=None):
        """  Corresponds to IDD Field `minimum_power_output`

        Args:
            value (float): value for IDD Field `minimum_power_output`
                Unit: W
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
                                 'for field `minimum_power_output`'.format(value))

        self._data["Minimum Power Output"] = value

    @property
    def maximum_power_output(self):
        """Get maximum_power_output

        Returns:
            float: the value of `maximum_power_output` or None if not set
        """
        return self._data["Maximum Power Output"]

    @maximum_power_output.setter
    def maximum_power_output(self, value=None):
        """  Corresponds to IDD Field `maximum_power_output`

        Args:
            value (float): value for IDD Field `maximum_power_output`
                Unit: W
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
                                 'for field `maximum_power_output`'.format(value))

        self._data["Maximum Power Output"] = value

    @property
    def ancillary_power_consumed_in_standby(self):
        """Get ancillary_power_consumed_in_standby

        Returns:
            float: the value of `ancillary_power_consumed_in_standby` or None if not set
        """
        return self._data["Ancillary Power Consumed In Standby"]

    @ancillary_power_consumed_in_standby.setter
    def ancillary_power_consumed_in_standby(self, value=None):
        """  Corresponds to IDD Field `ancillary_power_consumed_in_standby`

        Args:
            value (float): value for IDD Field `ancillary_power_consumed_in_standby`
                Unit: W
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
                                 'for field `ancillary_power_consumed_in_standby`'.format(value))

        self._data["Ancillary Power Consumed In Standby"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.radiative_fraction))
        out.append(self._to_str(self.efficiency_function_of_power_curve_name))
        out.append(self._to_str(self.rated_maximum_continuous_input_power))
        out.append(self._to_str(self.minimum_efficiency))
        out.append(self._to_str(self.maximum_efficiency))
        out.append(self._to_str(self.minimum_power_output))
        out.append(self._to_str(self.maximum_power_output))
        out.append(self._to_str(self.ancillary_power_consumed_in_standby))
        return ",".join(out)

class ElectricLoadCenterInverterLookUpTable(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Inverter:LookUpTable`
        California Energy Commission tests and publishs data on inverters
        This inverter model interpolates using CEC test data
        Input data are at http://www.gosolarcalifornia.org/equipment/inverter_tests/summaries
    """
    internal_name = "ElectricLoadCenter:Inverter:LookUpTable"
    field_count = 13

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Inverter:LookUpTable`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Radiative Fraction"] = None
        self._data["Rated Maximum Continuous Output Power"] = None
        self._data["Night Tare Loss Power"] = None
        self._data["Nominal Voltage Input"] = None
        self._data["Efficiency at 10% Power and Nominal Voltage"] = None
        self._data["Efficiency at 20% Power and Nominal Voltage"] = None
        self._data["Efficiency at 30% Power and Nominal Voltage"] = None
        self._data["Efficiency at 50% Power and Nominal Voltage"] = None
        self._data["Efficiency at 75% Power and Nominal Voltage"] = None
        self._data["Efficiency at 100% Power and Nominal Voltage"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radiative_fraction = None
        else:
            self.radiative_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_maximum_continuous_output_power = None
        else:
            self.rated_maximum_continuous_output_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.night_tare_loss_power = None
        else:
            self.night_tare_loss_power = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_voltage_input = None
        else:
            self.nominal_voltage_input = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_at_10_power_and_nominal_voltage = None
        else:
            self.efficiency_at_10_power_and_nominal_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_at_20_power_and_nominal_voltage = None
        else:
            self.efficiency_at_20_power_and_nominal_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_at_30_power_and_nominal_voltage = None
        else:
            self.efficiency_at_30_power_and_nominal_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_at_50_power_and_nominal_voltage = None
        else:
            self.efficiency_at_50_power_and_nominal_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_at_75_power_and_nominal_voltage = None
        else:
            self.efficiency_at_75_power_and_nominal_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.efficiency_at_100_power_and_nominal_voltage = None
        else:
            self.efficiency_at_100_power_and_nominal_voltage = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Enter name of zone to receive inverter losses as heat
        if blank then inverter is assumed to be outdoors

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def radiative_fraction(self):
        """Get radiative_fraction

        Returns:
            float: the value of `radiative_fraction` or None if not set
        """
        return self._data["Radiative Fraction"]

    @radiative_fraction.setter
    def radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `radiative_fraction`

        Args:
            value (float): value for IDD Field `radiative_fraction`
                value >= 0.0
                value <= 1.0
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
                                 'for field `radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `radiative_fraction`')

        self._data["Radiative Fraction"] = value

    @property
    def rated_maximum_continuous_output_power(self):
        """Get rated_maximum_continuous_output_power

        Returns:
            float: the value of `rated_maximum_continuous_output_power` or None if not set
        """
        return self._data["Rated Maximum Continuous Output Power"]

    @rated_maximum_continuous_output_power.setter
    def rated_maximum_continuous_output_power(self, value=None):
        """  Corresponds to IDD Field `rated_maximum_continuous_output_power`

        Args:
            value (float): value for IDD Field `rated_maximum_continuous_output_power`
                Unit: W
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
                                 'for field `rated_maximum_continuous_output_power`'.format(value))

        self._data["Rated Maximum Continuous Output Power"] = value

    @property
    def night_tare_loss_power(self):
        """Get night_tare_loss_power

        Returns:
            float: the value of `night_tare_loss_power` or None if not set
        """
        return self._data["Night Tare Loss Power"]

    @night_tare_loss_power.setter
    def night_tare_loss_power(self, value=None):
        """  Corresponds to IDD Field `night_tare_loss_power`

        Args:
            value (float): value for IDD Field `night_tare_loss_power`
                Unit: W
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
                                 'for field `night_tare_loss_power`'.format(value))

        self._data["Night Tare Loss Power"] = value

    @property
    def nominal_voltage_input(self):
        """Get nominal_voltage_input

        Returns:
            float: the value of `nominal_voltage_input` or None if not set
        """
        return self._data["Nominal Voltage Input"]

    @nominal_voltage_input.setter
    def nominal_voltage_input(self, value=None):
        """  Corresponds to IDD Field `nominal_voltage_input`

        Args:
            value (float): value for IDD Field `nominal_voltage_input`
                Unit: V
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
                                 'for field `nominal_voltage_input`'.format(value))

        self._data["Nominal Voltage Input"] = value

    @property
    def efficiency_at_10_power_and_nominal_voltage(self):
        """Get efficiency_at_10_power_and_nominal_voltage

        Returns:
            float: the value of `efficiency_at_10_power_and_nominal_voltage` or None if not set
        """
        return self._data["Efficiency at 10% Power and Nominal Voltage"]

    @efficiency_at_10_power_and_nominal_voltage.setter
    def efficiency_at_10_power_and_nominal_voltage(self, value=None):
        """  Corresponds to IDD Field `efficiency_at_10_power_and_nominal_voltage`

        Args:
            value (float): value for IDD Field `efficiency_at_10_power_and_nominal_voltage`
                value >= 0.0
                value <= 1.0
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
                                 'for field `efficiency_at_10_power_and_nominal_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `efficiency_at_10_power_and_nominal_voltage`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `efficiency_at_10_power_and_nominal_voltage`')

        self._data["Efficiency at 10% Power and Nominal Voltage"] = value

    @property
    def efficiency_at_20_power_and_nominal_voltage(self):
        """Get efficiency_at_20_power_and_nominal_voltage

        Returns:
            float: the value of `efficiency_at_20_power_and_nominal_voltage` or None if not set
        """
        return self._data["Efficiency at 20% Power and Nominal Voltage"]

    @efficiency_at_20_power_and_nominal_voltage.setter
    def efficiency_at_20_power_and_nominal_voltage(self, value=None):
        """  Corresponds to IDD Field `efficiency_at_20_power_and_nominal_voltage`

        Args:
            value (float): value for IDD Field `efficiency_at_20_power_and_nominal_voltage`
                value >= 0.0
                value <= 1.0
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
                                 'for field `efficiency_at_20_power_and_nominal_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `efficiency_at_20_power_and_nominal_voltage`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `efficiency_at_20_power_and_nominal_voltage`')

        self._data["Efficiency at 20% Power and Nominal Voltage"] = value

    @property
    def efficiency_at_30_power_and_nominal_voltage(self):
        """Get efficiency_at_30_power_and_nominal_voltage

        Returns:
            float: the value of `efficiency_at_30_power_and_nominal_voltage` or None if not set
        """
        return self._data["Efficiency at 30% Power and Nominal Voltage"]

    @efficiency_at_30_power_and_nominal_voltage.setter
    def efficiency_at_30_power_and_nominal_voltage(self, value=None):
        """  Corresponds to IDD Field `efficiency_at_30_power_and_nominal_voltage`

        Args:
            value (float): value for IDD Field `efficiency_at_30_power_and_nominal_voltage`
                value >= 0.0
                value <= 1.0
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
                                 'for field `efficiency_at_30_power_and_nominal_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `efficiency_at_30_power_and_nominal_voltage`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `efficiency_at_30_power_and_nominal_voltage`')

        self._data["Efficiency at 30% Power and Nominal Voltage"] = value

    @property
    def efficiency_at_50_power_and_nominal_voltage(self):
        """Get efficiency_at_50_power_and_nominal_voltage

        Returns:
            float: the value of `efficiency_at_50_power_and_nominal_voltage` or None if not set
        """
        return self._data["Efficiency at 50% Power and Nominal Voltage"]

    @efficiency_at_50_power_and_nominal_voltage.setter
    def efficiency_at_50_power_and_nominal_voltage(self, value=None):
        """  Corresponds to IDD Field `efficiency_at_50_power_and_nominal_voltage`

        Args:
            value (float): value for IDD Field `efficiency_at_50_power_and_nominal_voltage`
                value >= 0.0
                value <= 1.0
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
                                 'for field `efficiency_at_50_power_and_nominal_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `efficiency_at_50_power_and_nominal_voltage`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `efficiency_at_50_power_and_nominal_voltage`')

        self._data["Efficiency at 50% Power and Nominal Voltage"] = value

    @property
    def efficiency_at_75_power_and_nominal_voltage(self):
        """Get efficiency_at_75_power_and_nominal_voltage

        Returns:
            float: the value of `efficiency_at_75_power_and_nominal_voltage` or None if not set
        """
        return self._data["Efficiency at 75% Power and Nominal Voltage"]

    @efficiency_at_75_power_and_nominal_voltage.setter
    def efficiency_at_75_power_and_nominal_voltage(self, value=None):
        """  Corresponds to IDD Field `efficiency_at_75_power_and_nominal_voltage`

        Args:
            value (float): value for IDD Field `efficiency_at_75_power_and_nominal_voltage`
                value >= 0.0
                value <= 1.0
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
                                 'for field `efficiency_at_75_power_and_nominal_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `efficiency_at_75_power_and_nominal_voltage`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `efficiency_at_75_power_and_nominal_voltage`')

        self._data["Efficiency at 75% Power and Nominal Voltage"] = value

    @property
    def efficiency_at_100_power_and_nominal_voltage(self):
        """Get efficiency_at_100_power_and_nominal_voltage

        Returns:
            float: the value of `efficiency_at_100_power_and_nominal_voltage` or None if not set
        """
        return self._data["Efficiency at 100% Power and Nominal Voltage"]

    @efficiency_at_100_power_and_nominal_voltage.setter
    def efficiency_at_100_power_and_nominal_voltage(self, value=None):
        """  Corresponds to IDD Field `efficiency_at_100_power_and_nominal_voltage`

        Args:
            value (float): value for IDD Field `efficiency_at_100_power_and_nominal_voltage`
                value >= 0.0
                value <= 1.0
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
                                 'for field `efficiency_at_100_power_and_nominal_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `efficiency_at_100_power_and_nominal_voltage`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `efficiency_at_100_power_and_nominal_voltage`')

        self._data["Efficiency at 100% Power and Nominal Voltage"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.radiative_fraction))
        out.append(self._to_str(self.rated_maximum_continuous_output_power))
        out.append(self._to_str(self.night_tare_loss_power))
        out.append(self._to_str(self.nominal_voltage_input))
        out.append(self._to_str(self.efficiency_at_10_power_and_nominal_voltage))
        out.append(self._to_str(self.efficiency_at_20_power_and_nominal_voltage))
        out.append(self._to_str(self.efficiency_at_30_power_and_nominal_voltage))
        out.append(self._to_str(self.efficiency_at_50_power_and_nominal_voltage))
        out.append(self._to_str(self.efficiency_at_75_power_and_nominal_voltage))
        out.append(self._to_str(self.efficiency_at_100_power_and_nominal_voltage))
        return ",".join(out)

class ElectricLoadCenterStorageSimple(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Storage:Simple`
        Used to model storage of electricity in an electric load center.  This is a simple
        model that does not attempt to represent any of the characteristics of a real
        storage device such as a battery.  The type of power, AC or DC, depends on
        the configuration chosen as the Electrical Buss Type in the
        ElectricLoadCenter:Distribution object.
    """
    internal_name = "ElectricLoadCenter:Storage:Simple"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Storage:Simple`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Radiative Fraction for Zone Heat Gains"] = None
        self._data["Nominal Energetic Efficiency for Charging"] = None
        self._data["Nominal Discharging Energetic Efficiency"] = None
        self._data["Maximum Storage Capacity"] = None
        self._data["Maximum Power for Discharging"] = None
        self._data["Maximum Power for Charging"] = None
        self._data["Initial State of Charge"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radiative_fraction_for_zone_heat_gains = None
        else:
            self.radiative_fraction_for_zone_heat_gains = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_energetic_efficiency_for_charging = None
        else:
            self.nominal_energetic_efficiency_for_charging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nominal_discharging_energetic_efficiency = None
        else:
            self.nominal_discharging_energetic_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_storage_capacity = None
        else:
            self.maximum_storage_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_power_for_discharging = None
        else:
            self.maximum_power_for_discharging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_power_for_charging = None
        else:
            self.maximum_power_for_charging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_state_of_charge = None
        else:
            self.initial_state_of_charge = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Enter name of zone to receive storage losses as heat
        if blank then storage is assumed to be outdoors

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def radiative_fraction_for_zone_heat_gains(self):
        """Get radiative_fraction_for_zone_heat_gains

        Returns:
            float: the value of `radiative_fraction_for_zone_heat_gains` or None if not set
        """
        return self._data["Radiative Fraction for Zone Heat Gains"]

    @radiative_fraction_for_zone_heat_gains.setter
    def radiative_fraction_for_zone_heat_gains(self, value=None):
        """  Corresponds to IDD Field `radiative_fraction_for_zone_heat_gains`

        Args:
            value (float): value for IDD Field `radiative_fraction_for_zone_heat_gains`
                value >= 0.0
                value <= 1.0
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
                                 'for field `radiative_fraction_for_zone_heat_gains`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `radiative_fraction_for_zone_heat_gains`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `radiative_fraction_for_zone_heat_gains`')

        self._data["Radiative Fraction for Zone Heat Gains"] = value

    @property
    def nominal_energetic_efficiency_for_charging(self):
        """Get nominal_energetic_efficiency_for_charging

        Returns:
            float: the value of `nominal_energetic_efficiency_for_charging` or None if not set
        """
        return self._data["Nominal Energetic Efficiency for Charging"]

    @nominal_energetic_efficiency_for_charging.setter
    def nominal_energetic_efficiency_for_charging(self, value=None):
        """  Corresponds to IDD Field `nominal_energetic_efficiency_for_charging`

        Args:
            value (float): value for IDD Field `nominal_energetic_efficiency_for_charging`
                value >= 0.0
                value <= 1.0
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
                                 'for field `nominal_energetic_efficiency_for_charging`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_energetic_efficiency_for_charging`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `nominal_energetic_efficiency_for_charging`')

        self._data["Nominal Energetic Efficiency for Charging"] = value

    @property
    def nominal_discharging_energetic_efficiency(self):
        """Get nominal_discharging_energetic_efficiency

        Returns:
            float: the value of `nominal_discharging_energetic_efficiency` or None if not set
        """
        return self._data["Nominal Discharging Energetic Efficiency"]

    @nominal_discharging_energetic_efficiency.setter
    def nominal_discharging_energetic_efficiency(self, value=None):
        """  Corresponds to IDD Field `nominal_discharging_energetic_efficiency`

        Args:
            value (float): value for IDD Field `nominal_discharging_energetic_efficiency`
                value >= 0.0
                value <= 1.0
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
                                 'for field `nominal_discharging_energetic_efficiency`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `nominal_discharging_energetic_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `nominal_discharging_energetic_efficiency`')

        self._data["Nominal Discharging Energetic Efficiency"] = value

    @property
    def maximum_storage_capacity(self):
        """Get maximum_storage_capacity

        Returns:
            float: the value of `maximum_storage_capacity` or None if not set
        """
        return self._data["Maximum Storage Capacity"]

    @maximum_storage_capacity.setter
    def maximum_storage_capacity(self, value=None):
        """  Corresponds to IDD Field `maximum_storage_capacity`

        Args:
            value (float): value for IDD Field `maximum_storage_capacity`
                Unit: J
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
                                 'for field `maximum_storage_capacity`'.format(value))

        self._data["Maximum Storage Capacity"] = value

    @property
    def maximum_power_for_discharging(self):
        """Get maximum_power_for_discharging

        Returns:
            float: the value of `maximum_power_for_discharging` or None if not set
        """
        return self._data["Maximum Power for Discharging"]

    @maximum_power_for_discharging.setter
    def maximum_power_for_discharging(self, value=None):
        """  Corresponds to IDD Field `maximum_power_for_discharging`

        Args:
            value (float): value for IDD Field `maximum_power_for_discharging`
                Unit: W
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
                                 'for field `maximum_power_for_discharging`'.format(value))

        self._data["Maximum Power for Discharging"] = value

    @property
    def maximum_power_for_charging(self):
        """Get maximum_power_for_charging

        Returns:
            float: the value of `maximum_power_for_charging` or None if not set
        """
        return self._data["Maximum Power for Charging"]

    @maximum_power_for_charging.setter
    def maximum_power_for_charging(self, value=None):
        """  Corresponds to IDD Field `maximum_power_for_charging`

        Args:
            value (float): value for IDD Field `maximum_power_for_charging`
                Unit: W
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
                                 'for field `maximum_power_for_charging`'.format(value))

        self._data["Maximum Power for Charging"] = value

    @property
    def initial_state_of_charge(self):
        """Get initial_state_of_charge

        Returns:
            float: the value of `initial_state_of_charge` or None if not set
        """
        return self._data["Initial State of Charge"]

    @initial_state_of_charge.setter
    def initial_state_of_charge(self, value=None):
        """  Corresponds to IDD Field `initial_state_of_charge`

        Args:
            value (float): value for IDD Field `initial_state_of_charge`
                Unit: J
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
                                 'for field `initial_state_of_charge`'.format(value))

        self._data["Initial State of Charge"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.radiative_fraction_for_zone_heat_gains))
        out.append(self._to_str(self.nominal_energetic_efficiency_for_charging))
        out.append(self._to_str(self.nominal_discharging_energetic_efficiency))
        out.append(self._to_str(self.maximum_storage_capacity))
        out.append(self._to_str(self.maximum_power_for_discharging))
        out.append(self._to_str(self.maximum_power_for_charging))
        out.append(self._to_str(self.initial_state_of_charge))
        return ",".join(out)

class ElectricLoadCenterStorageBattery(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Storage:Battery`
        Uses the kinetic battery model (KiBaM) to simulate rechargeable battery banks in an
        electrical load center. The battery bank is a collection of one or more individual
        battery modules. Given the surplus or deficit power from the electrical system and
        the state of charge from the previous time step, this object can model the voltage,
        current, and energy losses with charging and discharging during each time step.
        The cumulative battery damage can be also modeled and reported at the end of
        each simulation run.
    """
    internal_name = "ElectricLoadCenter:Storage:Battery"
    field_count = 21

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Storage:Battery`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Zone Name"] = None
        self._data["Radiative Fraction"] = None
        self._data["Number of Battery Modules in Parallel"] = None
        self._data["Number of Battery Modules in Series"] = None
        self._data["Maximum Module Capacity"] = None
        self._data["Initial Fractional State of Charge"] = None
        self._data["Fraction of Available Charge Capacity"] = None
        self._data["Change Rate from Bound Charge to Available Charge"] = None
        self._data["Fully Charged Module Open Circuit Voltage"] = None
        self._data["Fully Discharged Module Open Circuit Voltage"] = None
        self._data["Voltage Change Curve Name for Charging"] = None
        self._data["Voltage Change Curve Name for Discharging"] = None
        self._data["Module Internal Electrical Resistance"] = None
        self._data["Maximum Module Discharging Current"] = None
        self._data["Module Cut-off Voltage"] = None
        self._data["Module Charge Rate Limit"] = None
        self._data["Battery Life Calculation"] = None
        self._data["Number of Cycle Bins"] = None
        self._data["Battery Life Curve Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radiative_fraction = None
        else:
            self.radiative_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_battery_modules_in_parallel = None
        else:
            self.number_of_battery_modules_in_parallel = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_battery_modules_in_series = None
        else:
            self.number_of_battery_modules_in_series = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_module_capacity = None
        else:
            self.maximum_module_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.initial_fractional_state_of_charge = None
        else:
            self.initial_fractional_state_of_charge = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_available_charge_capacity = None
        else:
            self.fraction_of_available_charge_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.change_rate_from_bound_charge_to_available_charge = None
        else:
            self.change_rate_from_bound_charge_to_available_charge = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fully_charged_module_open_circuit_voltage = None
        else:
            self.fully_charged_module_open_circuit_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fully_discharged_module_open_circuit_voltage = None
        else:
            self.fully_discharged_module_open_circuit_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.voltage_change_curve_name_for_charging = None
        else:
            self.voltage_change_curve_name_for_charging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.voltage_change_curve_name_for_discharging = None
        else:
            self.voltage_change_curve_name_for_discharging = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.module_internal_electrical_resistance = None
        else:
            self.module_internal_electrical_resistance = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.maximum_module_discharging_current = None
        else:
            self.maximum_module_discharging_current = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.module_cutoff_voltage = None
        else:
            self.module_cutoff_voltage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.module_charge_rate_limit = None
        else:
            self.module_charge_rate_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.battery_life_calculation = None
        else:
            self.battery_life_calculation = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.number_of_cycle_bins = None
        else:
            self.number_of_cycle_bins = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.battery_life_curve_name = None
        else:
            self.battery_life_curve_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Enter name of zone to receive electrical storage losses as heat
        if blank then electrical storage losses are dissipated to outdoors

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def radiative_fraction(self):
        """Get radiative_fraction

        Returns:
            float: the value of `radiative_fraction` or None if not set
        """
        return self._data["Radiative Fraction"]

    @radiative_fraction.setter
    def radiative_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `radiative_fraction`

        Args:
            value (float): value for IDD Field `radiative_fraction`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `radiative_fraction`')

        self._data["Radiative Fraction"] = value

    @property
    def number_of_battery_modules_in_parallel(self):
        """Get number_of_battery_modules_in_parallel

        Returns:
            int: the value of `number_of_battery_modules_in_parallel` or None if not set
        """
        return self._data["Number of Battery Modules in Parallel"]

    @number_of_battery_modules_in_parallel.setter
    def number_of_battery_modules_in_parallel(self, value=1 ):
        """  Corresponds to IDD Field `number_of_battery_modules_in_parallel`
        A module usually consists of several cells.
        The total number of modules in the battery bank
        is equal to number of modules in parallel times
        number of modules in series.

        Args:
            value (int): value for IDD Field `number_of_battery_modules_in_parallel`
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
                                 'for field `number_of_battery_modules_in_parallel`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_battery_modules_in_parallel`')

        self._data["Number of Battery Modules in Parallel"] = value

    @property
    def number_of_battery_modules_in_series(self):
        """Get number_of_battery_modules_in_series

        Returns:
            int: the value of `number_of_battery_modules_in_series` or None if not set
        """
        return self._data["Number of Battery Modules in Series"]

    @number_of_battery_modules_in_series.setter
    def number_of_battery_modules_in_series(self, value=1 ):
        """  Corresponds to IDD Field `number_of_battery_modules_in_series`
        A module usually consists of several cells.
        The total number of modules in the battery bank
        is equal to number of modules in parallel times
        number of modules in series.

        Args:
            value (int): value for IDD Field `number_of_battery_modules_in_series`
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
                                 'for field `number_of_battery_modules_in_series`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_battery_modules_in_series`')

        self._data["Number of Battery Modules in Series"] = value

    @property
    def maximum_module_capacity(self):
        """Get maximum_module_capacity

        Returns:
            float: the value of `maximum_module_capacity` or None if not set
        """
        return self._data["Maximum Module Capacity"]

    @maximum_module_capacity.setter
    def maximum_module_capacity(self, value=None):
        """  Corresponds to IDD Field `maximum_module_capacity`
        The capacity is for each module.
        A model parameter from manufactures data or test data.

        Args:
            value (float): value for IDD Field `maximum_module_capacity`
                Unit: Ah
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
                                 'for field `maximum_module_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_module_capacity`')

        self._data["Maximum Module Capacity"] = value

    @property
    def initial_fractional_state_of_charge(self):
        """Get initial_fractional_state_of_charge

        Returns:
            float: the value of `initial_fractional_state_of_charge` or None if not set
        """
        return self._data["Initial Fractional State of Charge"]

    @initial_fractional_state_of_charge.setter
    def initial_fractional_state_of_charge(self, value=1.0 ):
        """  Corresponds to IDD Field `initial_fractional_state_of_charge`
        The state of charge is evaluated based on the
        maximum capacity defined in the next field.

        Args:
            value (float): value for IDD Field `initial_fractional_state_of_charge`
                Default value: 1.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `initial_fractional_state_of_charge`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `initial_fractional_state_of_charge`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `initial_fractional_state_of_charge`')

        self._data["Initial Fractional State of Charge"] = value

    @property
    def fraction_of_available_charge_capacity(self):
        """Get fraction_of_available_charge_capacity

        Returns:
            float: the value of `fraction_of_available_charge_capacity` or None if not set
        """
        return self._data["Fraction of Available Charge Capacity"]

    @fraction_of_available_charge_capacity.setter
    def fraction_of_available_charge_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_available_charge_capacity`
        A model parameter usually derived from test data by curve fitting.

        Args:
            value (float): value for IDD Field `fraction_of_available_charge_capacity`
                value >= 0.0
                value <= 1.0
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
                                 'for field `fraction_of_available_charge_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_available_charge_capacity`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_available_charge_capacity`')

        self._data["Fraction of Available Charge Capacity"] = value

    @property
    def change_rate_from_bound_charge_to_available_charge(self):
        """Get change_rate_from_bound_charge_to_available_charge

        Returns:
            float: the value of `change_rate_from_bound_charge_to_available_charge` or None if not set
        """
        return self._data["Change Rate from Bound Charge to Available Charge"]

    @change_rate_from_bound_charge_to_available_charge.setter
    def change_rate_from_bound_charge_to_available_charge(self, value=None):
        """  Corresponds to IDD Field `change_rate_from_bound_charge_to_available_charge`
        A model parameter usually derived from test data by curve fitting.

        Args:
            value (float): value for IDD Field `change_rate_from_bound_charge_to_available_charge`
                Unit: 1/hr
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
                                 'for field `change_rate_from_bound_charge_to_available_charge`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `change_rate_from_bound_charge_to_available_charge`')

        self._data["Change Rate from Bound Charge to Available Charge"] = value

    @property
    def fully_charged_module_open_circuit_voltage(self):
        """Get fully_charged_module_open_circuit_voltage

        Returns:
            float: the value of `fully_charged_module_open_circuit_voltage` or None if not set
        """
        return self._data["Fully Charged Module Open Circuit Voltage"]

    @fully_charged_module_open_circuit_voltage.setter
    def fully_charged_module_open_circuit_voltage(self, value=None):
        """  Corresponds to IDD Field `fully_charged_module_open_circuit_voltage`
        The voltage is for each battery module.

        Args:
            value (float): value for IDD Field `fully_charged_module_open_circuit_voltage`
                Unit: V
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
                                 'for field `fully_charged_module_open_circuit_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fully_charged_module_open_circuit_voltage`')

        self._data["Fully Charged Module Open Circuit Voltage"] = value

    @property
    def fully_discharged_module_open_circuit_voltage(self):
        """Get fully_discharged_module_open_circuit_voltage

        Returns:
            float: the value of `fully_discharged_module_open_circuit_voltage` or None if not set
        """
        return self._data["Fully Discharged Module Open Circuit Voltage"]

    @fully_discharged_module_open_circuit_voltage.setter
    def fully_discharged_module_open_circuit_voltage(self, value=None):
        """  Corresponds to IDD Field `fully_discharged_module_open_circuit_voltage`
        The voltage is for each battery module.

        Args:
            value (float): value for IDD Field `fully_discharged_module_open_circuit_voltage`
                Unit: V
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
                                 'for field `fully_discharged_module_open_circuit_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fully_discharged_module_open_circuit_voltage`')

        self._data["Fully Discharged Module Open Circuit Voltage"] = value

    @property
    def voltage_change_curve_name_for_charging(self):
        """Get voltage_change_curve_name_for_charging

        Returns:
            str: the value of `voltage_change_curve_name_for_charging` or None if not set
        """
        return self._data["Voltage Change Curve Name for Charging"]

    @voltage_change_curve_name_for_charging.setter
    def voltage_change_curve_name_for_charging(self, value=None):
        """  Corresponds to IDD Field `voltage_change_curve_name_for_charging`
        Table:OneIndependentVariable object can also be used
        Determines how the open circuit voltage change with state of charge relative to the fully discharged state.

        Args:
            value (str): value for IDD Field `voltage_change_curve_name_for_charging`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `voltage_change_curve_name_for_charging`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `voltage_change_curve_name_for_charging`')

        self._data["Voltage Change Curve Name for Charging"] = value

    @property
    def voltage_change_curve_name_for_discharging(self):
        """Get voltage_change_curve_name_for_discharging

        Returns:
            str: the value of `voltage_change_curve_name_for_discharging` or None if not set
        """
        return self._data["Voltage Change Curve Name for Discharging"]

    @voltage_change_curve_name_for_discharging.setter
    def voltage_change_curve_name_for_discharging(self, value=None):
        """  Corresponds to IDD Field `voltage_change_curve_name_for_discharging`
        Table:OneIndependentVariable object can also be used
        Determines how the open circuit voltage change with state of charge relative to the fully charged state.

        Args:
            value (str): value for IDD Field `voltage_change_curve_name_for_discharging`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `voltage_change_curve_name_for_discharging`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `voltage_change_curve_name_for_discharging`')

        self._data["Voltage Change Curve Name for Discharging"] = value

    @property
    def module_internal_electrical_resistance(self):
        """Get module_internal_electrical_resistance

        Returns:
            float: the value of `module_internal_electrical_resistance` or None if not set
        """
        return self._data["Module Internal Electrical Resistance"]

    @module_internal_electrical_resistance.setter
    def module_internal_electrical_resistance(self, value=None):
        """  Corresponds to IDD Field `module_internal_electrical_resistance`
        A model parameter from manufacture or derived from test data.
        Internal resistance is assumed to be constant.
        The internal resistance is for each battery module.

        Args:
            value (float): value for IDD Field `module_internal_electrical_resistance`
                Unit: ohms
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
                                 'for field `module_internal_electrical_resistance`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `module_internal_electrical_resistance`')

        self._data["Module Internal Electrical Resistance"] = value

    @property
    def maximum_module_discharging_current(self):
        """Get maximum_module_discharging_current

        Returns:
            float: the value of `maximum_module_discharging_current` or None if not set
        """
        return self._data["Maximum Module Discharging Current"]

    @maximum_module_discharging_current.setter
    def maximum_module_discharging_current(self, value=None):
        """  Corresponds to IDD Field `maximum_module_discharging_current`
        The constraint on discharging current is for each battery module.

        Args:
            value (float): value for IDD Field `maximum_module_discharging_current`
                Unit: A
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
                                 'for field `maximum_module_discharging_current`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_module_discharging_current`')

        self._data["Maximum Module Discharging Current"] = value

    @property
    def module_cutoff_voltage(self):
        """Get module_cutoff_voltage

        Returns:
            float: the value of `module_cutoff_voltage` or None if not set
        """
        return self._data["Module Cut-off Voltage"]

    @module_cutoff_voltage.setter
    def module_cutoff_voltage(self, value=None):
        """  Corresponds to IDD Field `module_cutoff_voltage`
        The voltage constraint is for each battery module.

        Args:
            value (float): value for IDD Field `module_cutoff_voltage`
                Unit: V
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
                                 'for field `module_cutoff_voltage`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `module_cutoff_voltage`')

        self._data["Module Cut-off Voltage"] = value

    @property
    def module_charge_rate_limit(self):
        """Get module_charge_rate_limit

        Returns:
            float: the value of `module_charge_rate_limit` or None if not set
        """
        return self._data["Module Charge Rate Limit"]

    @module_charge_rate_limit.setter
    def module_charge_rate_limit(self, value=1.0 ):
        """  Corresponds to IDD Field `module_charge_rate_limit`
        units 1/hr
        Charge rate limit is the division between charging current the remaining capacity.
        The constraint on charging current is for each module.

        Args:
            value (float): value for IDD Field `module_charge_rate_limit`
                Default value: 1.0
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
                                 'for field `module_charge_rate_limit`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `module_charge_rate_limit`')

        self._data["Module Charge Rate Limit"] = value

    @property
    def battery_life_calculation(self):
        """Get battery_life_calculation

        Returns:
            str: the value of `battery_life_calculation` or None if not set
        """
        return self._data["Battery Life Calculation"]

    @battery_life_calculation.setter
    def battery_life_calculation(self, value="No"):
        """  Corresponds to IDD Field `battery_life_calculation`

        Args:
            value (str): value for IDD Field `battery_life_calculation`
                Accepted values are:
                      - Yes
                      - No
                Default value: No
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `battery_life_calculation`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `battery_life_calculation`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `battery_life_calculation`'.format(value))

        self._data["Battery Life Calculation"] = value

    @property
    def number_of_cycle_bins(self):
        """Get number_of_cycle_bins

        Returns:
            int: the value of `number_of_cycle_bins` or None if not set
        """
        return self._data["Number of Cycle Bins"]

    @number_of_cycle_bins.setter
    def number_of_cycle_bins(self, value=10 ):
        """  Corresponds to IDD Field `number_of_cycle_bins`
        Only required when battery life calculation is activated

        Args:
            value (int): value for IDD Field `number_of_cycle_bins`
                Default value: 10
                value >= 5
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
                                 'for field `number_of_cycle_bins`'.format(value))
            if value < 5:
                raise ValueError('value need to be greater or equal 5 '
                                 'for field `number_of_cycle_bins`')

        self._data["Number of Cycle Bins"] = value

    @property
    def battery_life_curve_name(self):
        """Get battery_life_curve_name

        Returns:
            str: the value of `battery_life_curve_name` or None if not set
        """
        return self._data["Battery Life Curve Name"]

    @battery_life_curve_name.setter
    def battery_life_curve_name(self, value=None):
        """  Corresponds to IDD Field `battery_life_curve_name`
        Table:OneIndependentVariable object can also be used
        Determines the number of cycles to failure in relation to cycle range.
        Only required when battery life calculation is activated.

        Args:
            value (str): value for IDD Field `battery_life_curve_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `battery_life_curve_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `battery_life_curve_name`')

        self._data["Battery Life Curve Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.radiative_fraction))
        out.append(self._to_str(self.number_of_battery_modules_in_parallel))
        out.append(self._to_str(self.number_of_battery_modules_in_series))
        out.append(self._to_str(self.maximum_module_capacity))
        out.append(self._to_str(self.initial_fractional_state_of_charge))
        out.append(self._to_str(self.fraction_of_available_charge_capacity))
        out.append(self._to_str(self.change_rate_from_bound_charge_to_available_charge))
        out.append(self._to_str(self.fully_charged_module_open_circuit_voltage))
        out.append(self._to_str(self.fully_discharged_module_open_circuit_voltage))
        out.append(self._to_str(self.voltage_change_curve_name_for_charging))
        out.append(self._to_str(self.voltage_change_curve_name_for_discharging))
        out.append(self._to_str(self.module_internal_electrical_resistance))
        out.append(self._to_str(self.maximum_module_discharging_current))
        out.append(self._to_str(self.module_cutoff_voltage))
        out.append(self._to_str(self.module_charge_rate_limit))
        out.append(self._to_str(self.battery_life_calculation))
        out.append(self._to_str(self.number_of_cycle_bins))
        out.append(self._to_str(self.battery_life_curve_name))
        return ",".join(out)

class ElectricLoadCenterTransformer(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Transformer`
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "ElectricLoadCenter:Transformer"
    field_count = 28

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Transformer`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Transformer Usage"] = None
        self._data["Zone Name"] = None
        self._data["Radiative Fraction"] = None
        self._data["Rated Capacity"] = None
        self._data["Phase"] = None
        self._data["Conductor Material"] = None
        self._data["Full Load Temperature Rise"] = None
        self._data["Fraction of Eddy Current Losses"] = None
        self._data["Performance Input Method"] = None
        self._data["Rated No Load Loss"] = None
        self._data["Rated Load Loss"] = None
        self._data["Nameplate Efficiency"] = None
        self._data["Per Unit Load for Nameplate Efficiency"] = None
        self._data["Reference Temperature for Nameplate Efficiency"] = None
        self._data["Per Unit Load for Maximum Efficiency"] = None
        self._data["Consider Transformer Loss for Utility Cost"] = None
        self._data["Meter 1 Name"] = None
        self._data["Meter 2 Name"] = None
        self._data["Meter 3 Name"] = None
        self._data["Meter 4 Name"] = None
        self._data["Meter 5 Name"] = None
        self._data["Meter 6 Name"] = None
        self._data["Meter 7 Name"] = None
        self._data["Meter 8 Name"] = None
        self._data["Meter 9 Name"] = None
        self._data["Meter 10 Name"] = None

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
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transformer_usage = None
        else:
            self.transformer_usage = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.radiative_fraction = None
        else:
            self.radiative_fraction = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_capacity = None
        else:
            self.rated_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.phase = None
        else:
            self.phase = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.conductor_material = None
        else:
            self.conductor_material = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.full_load_temperature_rise = None
        else:
            self.full_load_temperature_rise = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_eddy_current_losses = None
        else:
            self.fraction_of_eddy_current_losses = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.performance_input_method = None
        else:
            self.performance_input_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_no_load_loss = None
        else:
            self.rated_no_load_loss = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.rated_load_loss = None
        else:
            self.rated_load_loss = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.nameplate_efficiency = None
        else:
            self.nameplate_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.per_unit_load_for_nameplate_efficiency = None
        else:
            self.per_unit_load_for_nameplate_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.reference_temperature_for_nameplate_efficiency = None
        else:
            self.reference_temperature_for_nameplate_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.per_unit_load_for_maximum_efficiency = None
        else:
            self.per_unit_load_for_maximum_efficiency = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.consider_transformer_loss_for_utility_cost = None
        else:
            self.consider_transformer_loss_for_utility_cost = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_1_name = None
        else:
            self.meter_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_2_name = None
        else:
            self.meter_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_3_name = None
        else:
            self.meter_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_4_name = None
        else:
            self.meter_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_5_name = None
        else:
            self.meter_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_6_name = None
        else:
            self.meter_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_7_name = None
        else:
            self.meter_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_8_name = None
        else:
            self.meter_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_9_name = None
        else:
            self.meter_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.meter_10_name = None
        else:
            self.meter_10_name = vals[i]
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
    def availability_schedule_name(self):
        """Get availability_schedule_name

        Returns:
            str: the value of `availability_schedule_name` or None if not set
        """
        return self._data["Availability Schedule Name"]

    @availability_schedule_name.setter
    def availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `availability_schedule_name`
        Availability schedule name for this system. Schedule value > 0 means the system is available.
        If this field is blank, the system is always available.

        Args:
            value (str): value for IDD Field `availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `availability_schedule_name`')

        self._data["Availability Schedule Name"] = value

    @property
    def transformer_usage(self):
        """Get transformer_usage

        Returns:
            str: the value of `transformer_usage` or None if not set
        """
        return self._data["Transformer Usage"]

    @transformer_usage.setter
    def transformer_usage(self, value="PowerInFromGrid"):
        """  Corresponds to IDD Field `transformer_usage`
        A transformer can be used to transfer electric energy from utility grid to
        building (PowerInFromGrid)or from building onsite generation to
        the grid (PowerOutFromOnsiteGeneration)

        Args:
            value (str): value for IDD Field `transformer_usage`
                Accepted values are:
                      - PowerInFromGrid
                      - PowerOutFromOnsiteGeneration
                Default value: PowerInFromGrid
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `transformer_usage`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transformer_usage`')
            vals = set()
            vals.add("PowerInFromGrid")
            vals.add("PowerOutFromOnsiteGeneration")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `transformer_usage`'.format(value))

        self._data["Transformer Usage"] = value

    @property
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Enter name of zone to receive transformer losses as heat
        if blank then transformer losses are dissipated to outdoors

        Args:
            value (str): value for IDD Field `zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def radiative_fraction(self):
        """Get radiative_fraction

        Returns:
            float: the value of `radiative_fraction` or None if not set
        """
        return self._data["Radiative Fraction"]

    @radiative_fraction.setter
    def radiative_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `radiative_fraction`

        Args:
            value (float): value for IDD Field `radiative_fraction`
                Default value: 0.0
                value >= 0.0
                value <= 1.0
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
                                 'for field `radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `radiative_fraction`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `radiative_fraction`')

        self._data["Radiative Fraction"] = value

    @property
    def rated_capacity(self):
        """Get rated_capacity

        Returns:
            float: the value of `rated_capacity` or None if not set
        """
        return self._data["Rated Capacity"]

    @rated_capacity.setter
    def rated_capacity(self, value=None):
        """  Corresponds to IDD Field `rated_capacity`
        the unit is VA, instead of kVA as usually shown on transformer nameplates.

        Args:
            value (float): value for IDD Field `rated_capacity`
                Unit: VA
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
                                 'for field `rated_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_capacity`')

        self._data["Rated Capacity"] = value

    @property
    def phase(self):
        """Get phase

        Returns:
            str: the value of `phase` or None if not set
        """
        return self._data["Phase"]

    @phase.setter
    def phase(self, value="3"):
        """  Corresponds to IDD Field `phase`
        Must be single or three phase transformer.
        NOT used in the current model.

        Args:
            value (str): value for IDD Field `phase`
                Accepted values are:
                      - 1
                      - 3
                Default value: 3
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `phase`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `phase`')
            vals = set()
            vals.add("1")
            vals.add("3")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `phase`'.format(value))

        self._data["Phase"] = value

    @property
    def conductor_material(self):
        """Get conductor_material

        Returns:
            str: the value of `conductor_material` or None if not set
        """
        return self._data["Conductor Material"]

    @conductor_material.setter
    def conductor_material(self, value="Aluminum"):
        """  Corresponds to IDD Field `conductor_material`
        Winding material used by the transformer.

        Args:
            value (str): value for IDD Field `conductor_material`
                Accepted values are:
                      - Copper
                      - Aluminum
                Default value: Aluminum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `conductor_material`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `conductor_material`')
            vals = set()
            vals.add("Copper")
            vals.add("Aluminum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `conductor_material`'.format(value))

        self._data["Conductor Material"] = value

    @property
    def full_load_temperature_rise(self):
        """Get full_load_temperature_rise

        Returns:
            float: the value of `full_load_temperature_rise` or None if not set
        """
        return self._data["Full Load Temperature Rise"]

    @full_load_temperature_rise.setter
    def full_load_temperature_rise(self, value=150.0 ):
        """  Corresponds to IDD Field `full_load_temperature_rise`

        Args:
            value (float): value for IDD Field `full_load_temperature_rise`
                Unit: C
                Default value: 150.0
                value >= 50.0
                value <= 180.0
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
                                 'for field `full_load_temperature_rise`'.format(value))
            if value < 50.0:
                raise ValueError('value need to be greater or equal 50.0 '
                                 'for field `full_load_temperature_rise`')
            if value > 180.0:
                raise ValueError('value need to be smaller 180.0 '
                                 'for field `full_load_temperature_rise`')

        self._data["Full Load Temperature Rise"] = value

    @property
    def fraction_of_eddy_current_losses(self):
        """Get fraction_of_eddy_current_losses

        Returns:
            float: the value of `fraction_of_eddy_current_losses` or None if not set
        """
        return self._data["Fraction of Eddy Current Losses"]

    @fraction_of_eddy_current_losses.setter
    def fraction_of_eddy_current_losses(self, value=0.1 ):
        """  Corresponds to IDD Field `fraction_of_eddy_current_losses`

        Args:
            value (float): value for IDD Field `fraction_of_eddy_current_losses`
                Default value: 0.1
                value >= 0.0
                value <= 1.0
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
                                 'for field `fraction_of_eddy_current_losses`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_eddy_current_losses`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `fraction_of_eddy_current_losses`')

        self._data["Fraction of Eddy Current Losses"] = value

    @property
    def performance_input_method(self):
        """Get performance_input_method

        Returns:
            str: the value of `performance_input_method` or None if not set
        """
        return self._data["Performance Input Method"]

    @performance_input_method.setter
    def performance_input_method(self, value="RatedLosses"):
        """  Corresponds to IDD Field `performance_input_method`
        User can define transformer performance by specifying
        load and no load losses at rated conditions or
        nameplate efficiency and maximum efficiency

        Args:
            value (str): value for IDD Field `performance_input_method`
                Accepted values are:
                      - RatedLosses
                      - NominalEfficiency
                Default value: RatedLosses
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `performance_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `performance_input_method`')
            vals = set()
            vals.add("RatedLosses")
            vals.add("NominalEfficiency")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `performance_input_method`'.format(value))

        self._data["Performance Input Method"] = value

    @property
    def rated_no_load_loss(self):
        """Get rated_no_load_loss

        Returns:
            float: the value of `rated_no_load_loss` or None if not set
        """
        return self._data["Rated No Load Loss"]

    @rated_no_load_loss.setter
    def rated_no_load_loss(self, value=None):
        """  Corresponds to IDD Field `rated_no_load_loss`
        Only required when RatedLosses is the performance input method

        Args:
            value (float): value for IDD Field `rated_no_load_loss`
                Unit: W
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
                                 'for field `rated_no_load_loss`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `rated_no_load_loss`')

        self._data["Rated No Load Loss"] = value

    @property
    def rated_load_loss(self):
        """Get rated_load_loss

        Returns:
            float: the value of `rated_load_loss` or None if not set
        """
        return self._data["Rated Load Loss"]

    @rated_load_loss.setter
    def rated_load_loss(self, value=None):
        """  Corresponds to IDD Field `rated_load_loss`
        Only required when RatedLosses is the performance input method

        Args:
            value (float): value for IDD Field `rated_load_loss`
                Unit: W
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
                                 'for field `rated_load_loss`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `rated_load_loss`')

        self._data["Rated Load Loss"] = value

    @property
    def nameplate_efficiency(self):
        """Get nameplate_efficiency

        Returns:
            float: the value of `nameplate_efficiency` or None if not set
        """
        return self._data["Nameplate Efficiency"]

    @nameplate_efficiency.setter
    def nameplate_efficiency(self, value=0.98 ):
        """  Corresponds to IDD Field `nameplate_efficiency`
        Only required when NominalEfficiency is the performance input method

        Args:
            value (float): value for IDD Field `nameplate_efficiency`
                Default value: 0.98
                value > 0.0
                value <= 1.0
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
                                 'for field `nameplate_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `nameplate_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `nameplate_efficiency`')

        self._data["Nameplate Efficiency"] = value

    @property
    def per_unit_load_for_nameplate_efficiency(self):
        """Get per_unit_load_for_nameplate_efficiency

        Returns:
            float: the value of `per_unit_load_for_nameplate_efficiency` or None if not set
        """
        return self._data["Per Unit Load for Nameplate Efficiency"]

    @per_unit_load_for_nameplate_efficiency.setter
    def per_unit_load_for_nameplate_efficiency(self, value=0.35 ):
        """  Corresponds to IDD Field `per_unit_load_for_nameplate_efficiency`
        Percentage of the rated capacity at which the nameplate efficiency is defined
        Only required when NominalEfficiency is the performance input method

        Args:
            value (float): value for IDD Field `per_unit_load_for_nameplate_efficiency`
                Default value: 0.35
                value > 0.0
                value <= 1.0
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
                                 'for field `per_unit_load_for_nameplate_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `per_unit_load_for_nameplate_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `per_unit_load_for_nameplate_efficiency`')

        self._data["Per Unit Load for Nameplate Efficiency"] = value

    @property
    def reference_temperature_for_nameplate_efficiency(self):
        """Get reference_temperature_for_nameplate_efficiency

        Returns:
            float: the value of `reference_temperature_for_nameplate_efficiency` or None if not set
        """
        return self._data["Reference Temperature for Nameplate Efficiency"]

    @reference_temperature_for_nameplate_efficiency.setter
    def reference_temperature_for_nameplate_efficiency(self, value=75.0 ):
        """  Corresponds to IDD Field `reference_temperature_for_nameplate_efficiency`
        Conductor operating temperature at which the nameplate efficiency is defined
        Only required when NominalEfficiency is the performance input method

        Args:
            value (float): value for IDD Field `reference_temperature_for_nameplate_efficiency`
                Unit: C
                Default value: 75.0
                value >= 20.0
                value <= 150.0
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
                                 'for field `reference_temperature_for_nameplate_efficiency`'.format(value))
            if value < 20.0:
                raise ValueError('value need to be greater or equal 20.0 '
                                 'for field `reference_temperature_for_nameplate_efficiency`')
            if value > 150.0:
                raise ValueError('value need to be smaller 150.0 '
                                 'for field `reference_temperature_for_nameplate_efficiency`')

        self._data["Reference Temperature for Nameplate Efficiency"] = value

    @property
    def per_unit_load_for_maximum_efficiency(self):
        """Get per_unit_load_for_maximum_efficiency

        Returns:
            float: the value of `per_unit_load_for_maximum_efficiency` or None if not set
        """
        return self._data["Per Unit Load for Maximum Efficiency"]

    @per_unit_load_for_maximum_efficiency.setter
    def per_unit_load_for_maximum_efficiency(self, value=None):
        """  Corresponds to IDD Field `per_unit_load_for_maximum_efficiency`
        Percentage of the rate capacity at which the maximum efficiency is obtained
        Only required when NominalEfficiency is the performance input method

        Args:
            value (float): value for IDD Field `per_unit_load_for_maximum_efficiency`
                value > 0.0
                value <= 1.0
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
                                 'for field `per_unit_load_for_maximum_efficiency`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `per_unit_load_for_maximum_efficiency`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `per_unit_load_for_maximum_efficiency`')

        self._data["Per Unit Load for Maximum Efficiency"] = value

    @property
    def consider_transformer_loss_for_utility_cost(self):
        """Get consider_transformer_loss_for_utility_cost

        Returns:
            str: the value of `consider_transformer_loss_for_utility_cost` or None if not set
        """
        return self._data["Consider Transformer Loss for Utility Cost"]

    @consider_transformer_loss_for_utility_cost.setter
    def consider_transformer_loss_for_utility_cost(self, value="Yes"):
        """  Corresponds to IDD Field `consider_transformer_loss_for_utility_cost`
        Only required when the transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `consider_transformer_loss_for_utility_cost`
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
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `consider_transformer_loss_for_utility_cost`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `consider_transformer_loss_for_utility_cost`')
            vals = set()
            vals.add("Yes")
            vals.add("No")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `consider_transformer_loss_for_utility_cost`'.format(value))

        self._data["Consider Transformer Loss for Utility Cost"] = value

    @property
    def meter_1_name(self):
        """Get meter_1_name

        Returns:
            str: the value of `meter_1_name` or None if not set
        """
        return self._data["Meter 1 Name"]

    @meter_1_name.setter
    def meter_1_name(self, value=None):
        """  Corresponds to IDD Field `meter_1_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_1_name`')

        self._data["Meter 1 Name"] = value

    @property
    def meter_2_name(self):
        """Get meter_2_name

        Returns:
            str: the value of `meter_2_name` or None if not set
        """
        return self._data["Meter 2 Name"]

    @meter_2_name.setter
    def meter_2_name(self, value=None):
        """  Corresponds to IDD Field `meter_2_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_2_name`')

        self._data["Meter 2 Name"] = value

    @property
    def meter_3_name(self):
        """Get meter_3_name

        Returns:
            str: the value of `meter_3_name` or None if not set
        """
        return self._data["Meter 3 Name"]

    @meter_3_name.setter
    def meter_3_name(self, value=None):
        """  Corresponds to IDD Field `meter_3_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_3_name`')

        self._data["Meter 3 Name"] = value

    @property
    def meter_4_name(self):
        """Get meter_4_name

        Returns:
            str: the value of `meter_4_name` or None if not set
        """
        return self._data["Meter 4 Name"]

    @meter_4_name.setter
    def meter_4_name(self, value=None):
        """  Corresponds to IDD Field `meter_4_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_4_name`')

        self._data["Meter 4 Name"] = value

    @property
    def meter_5_name(self):
        """Get meter_5_name

        Returns:
            str: the value of `meter_5_name` or None if not set
        """
        return self._data["Meter 5 Name"]

    @meter_5_name.setter
    def meter_5_name(self, value=None):
        """  Corresponds to IDD Field `meter_5_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_5_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_5_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_5_name`')

        self._data["Meter 5 Name"] = value

    @property
    def meter_6_name(self):
        """Get meter_6_name

        Returns:
            str: the value of `meter_6_name` or None if not set
        """
        return self._data["Meter 6 Name"]

    @meter_6_name.setter
    def meter_6_name(self, value=None):
        """  Corresponds to IDD Field `meter_6_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_6_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_6_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_6_name`')

        self._data["Meter 6 Name"] = value

    @property
    def meter_7_name(self):
        """Get meter_7_name

        Returns:
            str: the value of `meter_7_name` or None if not set
        """
        return self._data["Meter 7 Name"]

    @meter_7_name.setter
    def meter_7_name(self, value=None):
        """  Corresponds to IDD Field `meter_7_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_7_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_7_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_7_name`')

        self._data["Meter 7 Name"] = value

    @property
    def meter_8_name(self):
        """Get meter_8_name

        Returns:
            str: the value of `meter_8_name` or None if not set
        """
        return self._data["Meter 8 Name"]

    @meter_8_name.setter
    def meter_8_name(self, value=None):
        """  Corresponds to IDD Field `meter_8_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_8_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_8_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_8_name`')

        self._data["Meter 8 Name"] = value

    @property
    def meter_9_name(self):
        """Get meter_9_name

        Returns:
            str: the value of `meter_9_name` or None if not set
        """
        return self._data["Meter 9 Name"]

    @meter_9_name.setter
    def meter_9_name(self, value=None):
        """  Corresponds to IDD Field `meter_9_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_9_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_9_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_9_name`')

        self._data["Meter 9 Name"] = value

    @property
    def meter_10_name(self):
        """Get meter_10_name

        Returns:
            str: the value of `meter_10_name` or None if not set
        """
        return self._data["Meter 10 Name"]

    @meter_10_name.setter
    def meter_10_name(self, value=None):
        """  Corresponds to IDD Field `meter_10_name`
        Must be an electric meter (with electricity as the resource type)
        Only required when transformer is used for power in from the utility grid

        Args:
            value (str): value for IDD Field `meter_10_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `meter_10_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `meter_10_name`')

        self._data["Meter 10 Name"] = value

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
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.transformer_usage))
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.radiative_fraction))
        out.append(self._to_str(self.rated_capacity))
        out.append(self._to_str(self.phase))
        out.append(self._to_str(self.conductor_material))
        out.append(self._to_str(self.full_load_temperature_rise))
        out.append(self._to_str(self.fraction_of_eddy_current_losses))
        out.append(self._to_str(self.performance_input_method))
        out.append(self._to_str(self.rated_no_load_loss))
        out.append(self._to_str(self.rated_load_loss))
        out.append(self._to_str(self.nameplate_efficiency))
        out.append(self._to_str(self.per_unit_load_for_nameplate_efficiency))
        out.append(self._to_str(self.reference_temperature_for_nameplate_efficiency))
        out.append(self._to_str(self.per_unit_load_for_maximum_efficiency))
        out.append(self._to_str(self.consider_transformer_loss_for_utility_cost))
        out.append(self._to_str(self.meter_1_name))
        out.append(self._to_str(self.meter_2_name))
        out.append(self._to_str(self.meter_3_name))
        out.append(self._to_str(self.meter_4_name))
        out.append(self._to_str(self.meter_5_name))
        out.append(self._to_str(self.meter_6_name))
        out.append(self._to_str(self.meter_7_name))
        out.append(self._to_str(self.meter_8_name))
        out.append(self._to_str(self.meter_9_name))
        out.append(self._to_str(self.meter_10_name))
        return ",".join(out)

class ElectricLoadCenterDistribution(object):
    """ Corresponds to IDD object `ElectricLoadCenter:Distribution`
        a list of meters that can be reported are available after a run on
        the meter dictionary file (.mdd) if the Output:VariableDictionary has been requested.
    """
    internal_name = "ElectricLoadCenter:Distribution"
    field_count = 10

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ElectricLoadCenter:Distribution`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Generator List Name"] = None
        self._data["Generator Operation Scheme Type"] = None
        self._data["Demand Limit Scheme Purchased Electric Demand Limit"] = None
        self._data["Track Schedule Name Scheme Schedule Name"] = None
        self._data["Track Meter Scheme Meter Name"] = None
        self._data["Electrical Buss Type"] = None
        self._data["Inverter Object Name"] = None
        self._data["Electrical Storage Object Name"] = None
        self._data["Transformer Object Name"] = None

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
            self.generator_list_name = None
        else:
            self.generator_list_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.generator_operation_scheme_type = None
        else:
            self.generator_operation_scheme_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.demand_limit_scheme_purchased_electric_demand_limit = None
        else:
            self.demand_limit_scheme_purchased_electric_demand_limit = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.track_schedule_name_scheme_schedule_name = None
        else:
            self.track_schedule_name_scheme_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.track_meter_scheme_meter_name = None
        else:
            self.track_meter_scheme_meter_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electrical_buss_type = None
        else:
            self.electrical_buss_type = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.inverter_object_name = None
        else:
            self.inverter_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.electrical_storage_object_name = None
        else:
            self.electrical_storage_object_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.transformer_object_name = None
        else:
            self.transformer_object_name = vals[i]
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
    def generator_list_name(self):
        """Get generator_list_name

        Returns:
            str: the value of `generator_list_name` or None if not set
        """
        return self._data["Generator List Name"]

    @generator_list_name.setter
    def generator_list_name(self, value=None):
        """  Corresponds to IDD Field `generator_list_name`

        Args:
            value (str): value for IDD Field `generator_list_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_list_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_list_name`')

        self._data["Generator List Name"] = value

    @property
    def generator_operation_scheme_type(self):
        """Get generator_operation_scheme_type

        Returns:
            str: the value of `generator_operation_scheme_type` or None if not set
        """
        return self._data["Generator Operation Scheme Type"]

    @generator_operation_scheme_type.setter
    def generator_operation_scheme_type(self, value=None):
        """  Corresponds to IDD Field `generator_operation_scheme_type`
        required if Generator List is entered.

        Args:
            value (str): value for IDD Field `generator_operation_scheme_type`
                Accepted values are:
                      - Baseload
                      - DemandLimit
                      - TrackElectrical
                      - TrackSchedule
                      - TrackMeter
                      - FollowThermal
                      - FollowThermalLimitElectrical
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generator_operation_scheme_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generator_operation_scheme_type`')
            vals = set()
            vals.add("Baseload")
            vals.add("DemandLimit")
            vals.add("TrackElectrical")
            vals.add("TrackSchedule")
            vals.add("TrackMeter")
            vals.add("FollowThermal")
            vals.add("FollowThermalLimitElectrical")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `generator_operation_scheme_type`'.format(value))

        self._data["Generator Operation Scheme Type"] = value

    @property
    def demand_limit_scheme_purchased_electric_demand_limit(self):
        """Get demand_limit_scheme_purchased_electric_demand_limit

        Returns:
            float: the value of `demand_limit_scheme_purchased_electric_demand_limit` or None if not set
        """
        return self._data["Demand Limit Scheme Purchased Electric Demand Limit"]

    @demand_limit_scheme_purchased_electric_demand_limit.setter
    def demand_limit_scheme_purchased_electric_demand_limit(self, value=None):
        """  Corresponds to IDD Field `demand_limit_scheme_purchased_electric_demand_limit`

        Args:
            value (float): value for IDD Field `demand_limit_scheme_purchased_electric_demand_limit`
                Unit: W
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
                                 'for field `demand_limit_scheme_purchased_electric_demand_limit`'.format(value))

        self._data["Demand Limit Scheme Purchased Electric Demand Limit"] = value

    @property
    def track_schedule_name_scheme_schedule_name(self):
        """Get track_schedule_name_scheme_schedule_name

        Returns:
            str: the value of `track_schedule_name_scheme_schedule_name` or None if not set
        """
        return self._data["Track Schedule Name Scheme Schedule Name"]

    @track_schedule_name_scheme_schedule_name.setter
    def track_schedule_name_scheme_schedule_name(self, value=None):
        """  Corresponds to IDD Field `track_schedule_name_scheme_schedule_name`
        required when Generator Operation Scheme Type=TrackSchedule

        Args:
            value (str): value for IDD Field `track_schedule_name_scheme_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `track_schedule_name_scheme_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `track_schedule_name_scheme_schedule_name`')

        self._data["Track Schedule Name Scheme Schedule Name"] = value

    @property
    def track_meter_scheme_meter_name(self):
        """Get track_meter_scheme_meter_name

        Returns:
            str: the value of `track_meter_scheme_meter_name` or None if not set
        """
        return self._data["Track Meter Scheme Meter Name"]

    @track_meter_scheme_meter_name.setter
    def track_meter_scheme_meter_name(self, value=None):
        """  Corresponds to IDD Field `track_meter_scheme_meter_name`
        required when Generator Operation Scheme Type=TrackMeter

        Args:
            value (str): value for IDD Field `track_meter_scheme_meter_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `track_meter_scheme_meter_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `track_meter_scheme_meter_name`')

        self._data["Track Meter Scheme Meter Name"] = value

    @property
    def electrical_buss_type(self):
        """Get electrical_buss_type

        Returns:
            str: the value of `electrical_buss_type` or None if not set
        """
        return self._data["Electrical Buss Type"]

    @electrical_buss_type.setter
    def electrical_buss_type(self, value="AlternatingCurrent"):
        """  Corresponds to IDD Field `electrical_buss_type`

        Args:
            value (str): value for IDD Field `electrical_buss_type`
                Accepted values are:
                      - AlternatingCurrent
                      - AlternatingCurrentWithStorage
                      - DirectCurrentWithInverter
                      - DirectCurrentWithInverterDCStorage
                      - DirectCurrentWithInverterACStorage
                Default value: AlternatingCurrent
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electrical_buss_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electrical_buss_type`')
            vals = set()
            vals.add("AlternatingCurrent")
            vals.add("AlternatingCurrentWithStorage")
            vals.add("DirectCurrentWithInverter")
            vals.add("DirectCurrentWithInverterDCStorage")
            vals.add("DirectCurrentWithInverterACStorage")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `electrical_buss_type`'.format(value))

        self._data["Electrical Buss Type"] = value

    @property
    def inverter_object_name(self):
        """Get inverter_object_name

        Returns:
            str: the value of `inverter_object_name` or None if not set
        """
        return self._data["Inverter Object Name"]

    @inverter_object_name.setter
    def inverter_object_name(self, value=None):
        """  Corresponds to IDD Field `inverter_object_name`
        required when Electrical Buss Type=DirectCurrentWithInverter, DirectCurrentWithInverterDCStorage,
        or DirectCurrentWithInverterACStorage

        Args:
            value (str): value for IDD Field `inverter_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `inverter_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `inverter_object_name`')

        self._data["Inverter Object Name"] = value

    @property
    def electrical_storage_object_name(self):
        """Get electrical_storage_object_name

        Returns:
            str: the value of `electrical_storage_object_name` or None if not set
        """
        return self._data["Electrical Storage Object Name"]

    @electrical_storage_object_name.setter
    def electrical_storage_object_name(self, value=None):
        """  Corresponds to IDD Field `electrical_storage_object_name`
        required when Electrical Buss Type=AlternatingCurrentWithStorage, DirectCurrentWithInverterDCStorage,
        or DirectCurrentWithInverterACStorage

        Args:
            value (str): value for IDD Field `electrical_storage_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `electrical_storage_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `electrical_storage_object_name`')

        self._data["Electrical Storage Object Name"] = value

    @property
    def transformer_object_name(self):
        """Get transformer_object_name

        Returns:
            str: the value of `transformer_object_name` or None if not set
        """
        return self._data["Transformer Object Name"]

    @transformer_object_name.setter
    def transformer_object_name(self, value=None):
        """  Corresponds to IDD Field `transformer_object_name`
        required when power needs to be output from onsite generation to the grid via transformer

        Args:
            value (str): value for IDD Field `transformer_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `transformer_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `transformer_object_name`')

        self._data["Transformer Object Name"] = value

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
        out.append(self._to_str(self.generator_list_name))
        out.append(self._to_str(self.generator_operation_scheme_type))
        out.append(self._to_str(self.demand_limit_scheme_purchased_electric_demand_limit))
        out.append(self._to_str(self.track_schedule_name_scheme_schedule_name))
        out.append(self._to_str(self.track_meter_scheme_meter_name))
        out.append(self._to_str(self.electrical_buss_type))
        out.append(self._to_str(self.inverter_object_name))
        out.append(self._to_str(self.electrical_storage_object_name))
        out.append(self._to_str(self.transformer_object_name))
        return ",".join(out)