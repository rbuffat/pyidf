from collections import OrderedDict

class ZoneThermalChimney(object):
    """ Corresponds to IDD object `ZoneThermalChimney`
        A thermal chimney is a vertical shaft utilizing solar radiation to enhance natural
        ventilation. It consists of an absorber wall, air gap and glass cover with high solar
        transmissivity.
    """
    internal_name = "ZoneThermalChimney"
    field_count = 86

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `ZoneThermalChimney`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Availability Schedule Name"] = None
        self._data["Width of the Absorber Wall"] = None
        self._data["Cross Sectional Area of Air Channel Outlet"] = None
        self._data["Discharge Coefficient"] = None
        self._data["Zone 1 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 1"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 1"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 1"] = None
        self._data["Zone 2 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 2"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 2"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 2"] = None
        self._data["Zone 3 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 3"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 3"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 3"] = None
        self._data["Zone 4 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 4"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 4"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 4"] = None
        self._data["Zone 5 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 5"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 5"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 5"] = None
        self._data["Zone 6 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 6"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 6"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 6"] = None
        self._data["Zone 7 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 7"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 7"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 7"] = None
        self._data["Zone 8 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 8"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 8"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 8"] = None
        self._data["Zone 9 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 9"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 9"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 9"] = None
        self._data["Zone 10 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 10"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 10"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 10"] = None
        self._data["Zone 11 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 11"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 11"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 11"] = None
        self._data["Zone 12 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 12"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 12"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 12"] = None
        self._data["Zone 13 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 13"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 13"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 13"] = None
        self._data["Zone 14 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 14"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 14"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 14"] = None
        self._data["Zone 15 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 15"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 15"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 15"] = None
        self._data["Zone 16 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 16"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 16"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 16"] = None
        self._data["Zone 17 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 17"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 17"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 17"] = None
        self._data["Zone 18 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 18"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 18"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 18"] = None
        self._data["Zone 19 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 19"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 19"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 19"] = None
        self._data["Zone 20 Name"] = None
        self._data["Distance from Top of Thermal Chimney to Inlet 20"] = None
        self._data["Relative Ratios of Air Flow Rates Passing through Zone 20"] = None
        self._data["Cross Sectional Areas of Air Channel Inlet 20"] = None

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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.availability_schedule_name = None
        else:
            self.availability_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.width_of_the_absorber_wall = None
        else:
            self.width_of_the_absorber_wall = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_area_of_air_channel_outlet = None
        else:
            self.cross_sectional_area_of_air_channel_outlet = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.discharge_coefficient = None
        else:
            self.discharge_coefficient = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_1_name = None
        else:
            self.zone_1_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_1 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_1 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_1 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_1 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_2_name = None
        else:
            self.zone_2_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_2 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_2 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_2 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_2 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_3_name = None
        else:
            self.zone_3_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_3 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_3 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_3 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_3 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_4_name = None
        else:
            self.zone_4_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_4 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_4 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_4 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_4 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_5_name = None
        else:
            self.zone_5_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_5 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_5 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_5 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_5 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_6_name = None
        else:
            self.zone_6_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_6 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_6 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_6 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_6 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_7_name = None
        else:
            self.zone_7_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_7 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_7 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_7 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_7 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_8_name = None
        else:
            self.zone_8_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_8 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_8 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_8 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_8 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_9_name = None
        else:
            self.zone_9_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_9 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_9 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_9 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_9 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_10_name = None
        else:
            self.zone_10_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_10 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_10 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_10 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_10 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_11_name = None
        else:
            self.zone_11_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_11 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_11 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_11 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_11 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_12_name = None
        else:
            self.zone_12_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_12 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_12 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_12 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_12 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_13_name = None
        else:
            self.zone_13_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_13 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_13 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_13 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_13 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_14_name = None
        else:
            self.zone_14_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_14 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_14 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_14 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_14 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_15_name = None
        else:
            self.zone_15_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_15 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_15 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_15 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_15 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_16_name = None
        else:
            self.zone_16_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_16 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_16 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_16 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_16 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_17_name = None
        else:
            self.zone_17_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_17 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_17 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_17 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_17 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_18_name = None
        else:
            self.zone_18_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_18 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_18 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_18 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_18 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_19_name = None
        else:
            self.zone_19_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_19 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_19 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_19 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_19 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_20_name = None
        else:
            self.zone_20_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.distance_from_top_of_thermal_chimney_to_inlet_20 = None
        else:
            self.distance_from_top_of_thermal_chimney_to_inlet_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_20 = None
        else:
            self.relative_ratios_of_air_flow_rates_passing_through_zone_20 = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cross_sectional_areas_of_air_channel_inlet_20 = None
        else:
            self.cross_sectional_areas_of_air_channel_inlet_20 = vals[i]
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
    def zone_name(self):
        """Get zone_name

        Returns:
            str: the value of `zone_name` or None if not set
        """
        return self._data["Zone Name"]

    @zone_name.setter
    def zone_name(self, value=None):
        """  Corresponds to IDD Field `zone_name`
        Name of zone that is the thermal chimney

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
    def width_of_the_absorber_wall(self):
        """Get width_of_the_absorber_wall

        Returns:
            float: the value of `width_of_the_absorber_wall` or None if not set
        """
        return self._data["Width of the Absorber Wall"]

    @width_of_the_absorber_wall.setter
    def width_of_the_absorber_wall(self, value=None):
        """  Corresponds to IDD Field `width_of_the_absorber_wall`

        Args:
            value (float): value for IDD Field `width_of_the_absorber_wall`
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
                                 'for field `width_of_the_absorber_wall`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `width_of_the_absorber_wall`')

        self._data["Width of the Absorber Wall"] = value

    @property
    def cross_sectional_area_of_air_channel_outlet(self):
        """Get cross_sectional_area_of_air_channel_outlet

        Returns:
            float: the value of `cross_sectional_area_of_air_channel_outlet` or None if not set
        """
        return self._data["Cross Sectional Area of Air Channel Outlet"]

    @cross_sectional_area_of_air_channel_outlet.setter
    def cross_sectional_area_of_air_channel_outlet(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_area_of_air_channel_outlet`

        Args:
            value (float): value for IDD Field `cross_sectional_area_of_air_channel_outlet`
                Unit: m2
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
                                 'for field `cross_sectional_area_of_air_channel_outlet`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_area_of_air_channel_outlet`')

        self._data["Cross Sectional Area of Air Channel Outlet"] = value

    @property
    def discharge_coefficient(self):
        """Get discharge_coefficient

        Returns:
            float: the value of `discharge_coefficient` or None if not set
        """
        return self._data["Discharge Coefficient"]

    @discharge_coefficient.setter
    def discharge_coefficient(self, value=0.8 ):
        """  Corresponds to IDD Field `discharge_coefficient`

        Args:
            value (float): value for IDD Field `discharge_coefficient`
                Default value: 0.8
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
                                 'for field `discharge_coefficient`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `discharge_coefficient`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `discharge_coefficient`')

        self._data["Discharge Coefficient"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_1(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_1

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_1` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 1"]

    @distance_from_top_of_thermal_chimney_to_inlet_1.setter
    def distance_from_top_of_thermal_chimney_to_inlet_1(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_1`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_1`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_1`')

        self._data["Distance from Top of Thermal Chimney to Inlet 1"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_1(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_1

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_1` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 1"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_1.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_1(self, value=1.0 ):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_1`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_1`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_1`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_1`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 1"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_1(self):
        """Get cross_sectional_areas_of_air_channel_inlet_1

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_1` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 1"]

    @cross_sectional_areas_of_air_channel_inlet_1.setter
    def cross_sectional_areas_of_air_channel_inlet_1(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_1`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_1`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_1`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_1`')

        self._data["Cross Sectional Areas of Air Channel Inlet 1"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_2(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_2

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_2` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 2"]

    @distance_from_top_of_thermal_chimney_to_inlet_2.setter
    def distance_from_top_of_thermal_chimney_to_inlet_2(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_2`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_2`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_2`')

        self._data["Distance from Top of Thermal Chimney to Inlet 2"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_2(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_2

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_2` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 2"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_2.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_2(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_2`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_2`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_2`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_2`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 2"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_2(self):
        """Get cross_sectional_areas_of_air_channel_inlet_2

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_2` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 2"]

    @cross_sectional_areas_of_air_channel_inlet_2.setter
    def cross_sectional_areas_of_air_channel_inlet_2(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_2`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_2`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_2`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_2`')

        self._data["Cross Sectional Areas of Air Channel Inlet 2"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_3(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_3

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_3` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 3"]

    @distance_from_top_of_thermal_chimney_to_inlet_3.setter
    def distance_from_top_of_thermal_chimney_to_inlet_3(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_3`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_3`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_3`')

        self._data["Distance from Top of Thermal Chimney to Inlet 3"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_3(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_3

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_3` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 3"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_3.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_3(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_3`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_3`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_3`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_3`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 3"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_3(self):
        """Get cross_sectional_areas_of_air_channel_inlet_3

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_3` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 3"]

    @cross_sectional_areas_of_air_channel_inlet_3.setter
    def cross_sectional_areas_of_air_channel_inlet_3(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_3`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_3`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_3`')

        self._data["Cross Sectional Areas of Air Channel Inlet 3"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_4(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_4

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_4` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 4"]

    @distance_from_top_of_thermal_chimney_to_inlet_4.setter
    def distance_from_top_of_thermal_chimney_to_inlet_4(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_4`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_4`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_4`')

        self._data["Distance from Top of Thermal Chimney to Inlet 4"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_4(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_4

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_4` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 4"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_4.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_4(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_4`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_4`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_4`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_4`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 4"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_4(self):
        """Get cross_sectional_areas_of_air_channel_inlet_4

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_4` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 4"]

    @cross_sectional_areas_of_air_channel_inlet_4.setter
    def cross_sectional_areas_of_air_channel_inlet_4(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_4`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_4`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_4`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_4`')

        self._data["Cross Sectional Areas of Air Channel Inlet 4"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_5(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_5

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_5` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 5"]

    @distance_from_top_of_thermal_chimney_to_inlet_5.setter
    def distance_from_top_of_thermal_chimney_to_inlet_5(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_5`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_5`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_5`')

        self._data["Distance from Top of Thermal Chimney to Inlet 5"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_5(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_5

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_5` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 5"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_5.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_5(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_5`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_5`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_5`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_5`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 5"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_5(self):
        """Get cross_sectional_areas_of_air_channel_inlet_5

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_5` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 5"]

    @cross_sectional_areas_of_air_channel_inlet_5.setter
    def cross_sectional_areas_of_air_channel_inlet_5(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_5`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_5`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_5`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_5`')

        self._data["Cross Sectional Areas of Air Channel Inlet 5"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_6(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_6

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_6` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 6"]

    @distance_from_top_of_thermal_chimney_to_inlet_6.setter
    def distance_from_top_of_thermal_chimney_to_inlet_6(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_6`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_6`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_6`')

        self._data["Distance from Top of Thermal Chimney to Inlet 6"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_6(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_6

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_6` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 6"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_6.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_6(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_6`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_6`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_6`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_6`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 6"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_6(self):
        """Get cross_sectional_areas_of_air_channel_inlet_6

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_6` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 6"]

    @cross_sectional_areas_of_air_channel_inlet_6.setter
    def cross_sectional_areas_of_air_channel_inlet_6(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_6`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_6`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_6`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_6`')

        self._data["Cross Sectional Areas of Air Channel Inlet 6"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_7(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_7

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_7` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 7"]

    @distance_from_top_of_thermal_chimney_to_inlet_7.setter
    def distance_from_top_of_thermal_chimney_to_inlet_7(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_7`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_7`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_7`')

        self._data["Distance from Top of Thermal Chimney to Inlet 7"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_7(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_7

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_7` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 7"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_7.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_7(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_7`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_7`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_7`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_7`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 7"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_7(self):
        """Get cross_sectional_areas_of_air_channel_inlet_7

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_7` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 7"]

    @cross_sectional_areas_of_air_channel_inlet_7.setter
    def cross_sectional_areas_of_air_channel_inlet_7(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_7`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_7`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_7`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_7`')

        self._data["Cross Sectional Areas of Air Channel Inlet 7"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_8(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_8

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_8` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 8"]

    @distance_from_top_of_thermal_chimney_to_inlet_8.setter
    def distance_from_top_of_thermal_chimney_to_inlet_8(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_8`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_8`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_8`')

        self._data["Distance from Top of Thermal Chimney to Inlet 8"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_8(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_8

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_8` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 8"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_8.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_8(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_8`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_8`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_8`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_8`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 8"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_8(self):
        """Get cross_sectional_areas_of_air_channel_inlet_8

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_8` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 8"]

    @cross_sectional_areas_of_air_channel_inlet_8.setter
    def cross_sectional_areas_of_air_channel_inlet_8(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_8`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_8`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_8`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_8`')

        self._data["Cross Sectional Areas of Air Channel Inlet 8"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_9(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_9

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_9` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 9"]

    @distance_from_top_of_thermal_chimney_to_inlet_9.setter
    def distance_from_top_of_thermal_chimney_to_inlet_9(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_9`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_9`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_9`')

        self._data["Distance from Top of Thermal Chimney to Inlet 9"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_9(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_9

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_9` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 9"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_9.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_9(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_9`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_9`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_9`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_9`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 9"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_9(self):
        """Get cross_sectional_areas_of_air_channel_inlet_9

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_9` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 9"]

    @cross_sectional_areas_of_air_channel_inlet_9.setter
    def cross_sectional_areas_of_air_channel_inlet_9(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_9`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_9`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_9`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_9`')

        self._data["Cross Sectional Areas of Air Channel Inlet 9"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_10(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_10

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_10` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 10"]

    @distance_from_top_of_thermal_chimney_to_inlet_10.setter
    def distance_from_top_of_thermal_chimney_to_inlet_10(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_10`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_10`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_10`')

        self._data["Distance from Top of Thermal Chimney to Inlet 10"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_10(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_10

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_10` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 10"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_10.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_10(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_10`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_10`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_10`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_10`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 10"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_10(self):
        """Get cross_sectional_areas_of_air_channel_inlet_10

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_10` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 10"]

    @cross_sectional_areas_of_air_channel_inlet_10.setter
    def cross_sectional_areas_of_air_channel_inlet_10(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_10`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_10`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_10`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_10`')

        self._data["Cross Sectional Areas of Air Channel Inlet 10"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_11(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_11

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_11` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 11"]

    @distance_from_top_of_thermal_chimney_to_inlet_11.setter
    def distance_from_top_of_thermal_chimney_to_inlet_11(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_11`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_11`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_11`')

        self._data["Distance from Top of Thermal Chimney to Inlet 11"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_11(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_11

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_11` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 11"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_11.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_11(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_11`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_11`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_11`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_11`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 11"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_11(self):
        """Get cross_sectional_areas_of_air_channel_inlet_11

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_11` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 11"]

    @cross_sectional_areas_of_air_channel_inlet_11.setter
    def cross_sectional_areas_of_air_channel_inlet_11(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_11`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_11`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_11`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_11`')

        self._data["Cross Sectional Areas of Air Channel Inlet 11"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_12(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_12

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_12` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 12"]

    @distance_from_top_of_thermal_chimney_to_inlet_12.setter
    def distance_from_top_of_thermal_chimney_to_inlet_12(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_12`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_12`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_12`')

        self._data["Distance from Top of Thermal Chimney to Inlet 12"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_12(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_12

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_12` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 12"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_12.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_12(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_12`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_12`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_12`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_12`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 12"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_12(self):
        """Get cross_sectional_areas_of_air_channel_inlet_12

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_12` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 12"]

    @cross_sectional_areas_of_air_channel_inlet_12.setter
    def cross_sectional_areas_of_air_channel_inlet_12(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_12`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_12`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_12`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_12`')

        self._data["Cross Sectional Areas of Air Channel Inlet 12"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_13(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_13

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_13` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 13"]

    @distance_from_top_of_thermal_chimney_to_inlet_13.setter
    def distance_from_top_of_thermal_chimney_to_inlet_13(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_13`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_13`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_13`')

        self._data["Distance from Top of Thermal Chimney to Inlet 13"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_13(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_13

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_13` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 13"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_13.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_13(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_13`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_13`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_13`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_13`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 13"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_13(self):
        """Get cross_sectional_areas_of_air_channel_inlet_13

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_13` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 13"]

    @cross_sectional_areas_of_air_channel_inlet_13.setter
    def cross_sectional_areas_of_air_channel_inlet_13(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_13`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_13`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_13`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_13`')

        self._data["Cross Sectional Areas of Air Channel Inlet 13"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_14(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_14

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_14` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 14"]

    @distance_from_top_of_thermal_chimney_to_inlet_14.setter
    def distance_from_top_of_thermal_chimney_to_inlet_14(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_14`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_14`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_14`')

        self._data["Distance from Top of Thermal Chimney to Inlet 14"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_14(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_14

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_14` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 14"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_14.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_14(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_14`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_14`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_14`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_14`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 14"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_14(self):
        """Get cross_sectional_areas_of_air_channel_inlet_14

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_14` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 14"]

    @cross_sectional_areas_of_air_channel_inlet_14.setter
    def cross_sectional_areas_of_air_channel_inlet_14(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_14`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_14`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_14`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_14`')

        self._data["Cross Sectional Areas of Air Channel Inlet 14"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_15(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_15

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_15` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 15"]

    @distance_from_top_of_thermal_chimney_to_inlet_15.setter
    def distance_from_top_of_thermal_chimney_to_inlet_15(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_15`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_15`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_15`')

        self._data["Distance from Top of Thermal Chimney to Inlet 15"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_15(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_15

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_15` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 15"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_15.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_15(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_15`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_15`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_15`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_15`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 15"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_15(self):
        """Get cross_sectional_areas_of_air_channel_inlet_15

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_15` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 15"]

    @cross_sectional_areas_of_air_channel_inlet_15.setter
    def cross_sectional_areas_of_air_channel_inlet_15(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_15`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_15`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_15`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_15`')

        self._data["Cross Sectional Areas of Air Channel Inlet 15"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_16(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_16

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_16` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 16"]

    @distance_from_top_of_thermal_chimney_to_inlet_16.setter
    def distance_from_top_of_thermal_chimney_to_inlet_16(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_16`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_16`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_16`')

        self._data["Distance from Top of Thermal Chimney to Inlet 16"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_16(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_16

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_16` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 16"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_16.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_16(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_16`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_16`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_16`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_16`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 16"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_16(self):
        """Get cross_sectional_areas_of_air_channel_inlet_16

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_16` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 16"]

    @cross_sectional_areas_of_air_channel_inlet_16.setter
    def cross_sectional_areas_of_air_channel_inlet_16(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_16`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_16`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_16`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_16`')

        self._data["Cross Sectional Areas of Air Channel Inlet 16"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_17(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_17

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_17` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 17"]

    @distance_from_top_of_thermal_chimney_to_inlet_17.setter
    def distance_from_top_of_thermal_chimney_to_inlet_17(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_17`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_17`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_17`')

        self._data["Distance from Top of Thermal Chimney to Inlet 17"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_17(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_17

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_17` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 17"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_17.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_17(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_17`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_17`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_17`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_17`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 17"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_17(self):
        """Get cross_sectional_areas_of_air_channel_inlet_17

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_17` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 17"]

    @cross_sectional_areas_of_air_channel_inlet_17.setter
    def cross_sectional_areas_of_air_channel_inlet_17(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_17`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_17`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_17`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_17`')

        self._data["Cross Sectional Areas of Air Channel Inlet 17"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_18(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_18

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_18` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 18"]

    @distance_from_top_of_thermal_chimney_to_inlet_18.setter
    def distance_from_top_of_thermal_chimney_to_inlet_18(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_18`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_18`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_18`')

        self._data["Distance from Top of Thermal Chimney to Inlet 18"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_18(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_18

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_18` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 18"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_18.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_18(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_18`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_18`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_18`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_18`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 18"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_18(self):
        """Get cross_sectional_areas_of_air_channel_inlet_18

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_18` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 18"]

    @cross_sectional_areas_of_air_channel_inlet_18.setter
    def cross_sectional_areas_of_air_channel_inlet_18(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_18`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_18`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_18`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_18`')

        self._data["Cross Sectional Areas of Air Channel Inlet 18"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_19(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_19

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_19` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 19"]

    @distance_from_top_of_thermal_chimney_to_inlet_19.setter
    def distance_from_top_of_thermal_chimney_to_inlet_19(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_19`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_19`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_19`')

        self._data["Distance from Top of Thermal Chimney to Inlet 19"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_19(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_19

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_19` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 19"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_19.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_19(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_19`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_19`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_19`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_19`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 19"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_19(self):
        """Get cross_sectional_areas_of_air_channel_inlet_19

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_19` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 19"]

    @cross_sectional_areas_of_air_channel_inlet_19.setter
    def cross_sectional_areas_of_air_channel_inlet_19(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_19`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_19`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_19`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_19`')

        self._data["Cross Sectional Areas of Air Channel Inlet 19"] = value

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
    def distance_from_top_of_thermal_chimney_to_inlet_20(self):
        """Get distance_from_top_of_thermal_chimney_to_inlet_20

        Returns:
            float: the value of `distance_from_top_of_thermal_chimney_to_inlet_20` or None if not set
        """
        return self._data["Distance from Top of Thermal Chimney to Inlet 20"]

    @distance_from_top_of_thermal_chimney_to_inlet_20.setter
    def distance_from_top_of_thermal_chimney_to_inlet_20(self, value=None):
        """  Corresponds to IDD Field `distance_from_top_of_thermal_chimney_to_inlet_20`

        Args:
            value (float): value for IDD Field `distance_from_top_of_thermal_chimney_to_inlet_20`
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
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `distance_from_top_of_thermal_chimney_to_inlet_20`')

        self._data["Distance from Top of Thermal Chimney to Inlet 20"] = value

    @property
    def relative_ratios_of_air_flow_rates_passing_through_zone_20(self):
        """Get relative_ratios_of_air_flow_rates_passing_through_zone_20

        Returns:
            float: the value of `relative_ratios_of_air_flow_rates_passing_through_zone_20` or None if not set
        """
        return self._data["Relative Ratios of Air Flow Rates Passing through Zone 20"]

    @relative_ratios_of_air_flow_rates_passing_through_zone_20.setter
    def relative_ratios_of_air_flow_rates_passing_through_zone_20(self, value=None):
        """  Corresponds to IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_20`

        Args:
            value (float): value for IDD Field `relative_ratios_of_air_flow_rates_passing_through_zone_20`
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
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_20`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `relative_ratios_of_air_flow_rates_passing_through_zone_20`')

        self._data["Relative Ratios of Air Flow Rates Passing through Zone 20"] = value

    @property
    def cross_sectional_areas_of_air_channel_inlet_20(self):
        """Get cross_sectional_areas_of_air_channel_inlet_20

        Returns:
            float: the value of `cross_sectional_areas_of_air_channel_inlet_20` or None if not set
        """
        return self._data["Cross Sectional Areas of Air Channel Inlet 20"]

    @cross_sectional_areas_of_air_channel_inlet_20.setter
    def cross_sectional_areas_of_air_channel_inlet_20(self, value=None):
        """  Corresponds to IDD Field `cross_sectional_areas_of_air_channel_inlet_20`

        Args:
            value (float): value for IDD Field `cross_sectional_areas_of_air_channel_inlet_20`
                Unit: m2
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
                                 'for field `cross_sectional_areas_of_air_channel_inlet_20`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cross_sectional_areas_of_air_channel_inlet_20`')

        self._data["Cross Sectional Areas of Air Channel Inlet 20"] = value

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
        out.append(self._to_str(self.zone_name))
        out.append(self._to_str(self.availability_schedule_name))
        out.append(self._to_str(self.width_of_the_absorber_wall))
        out.append(self._to_str(self.cross_sectional_area_of_air_channel_outlet))
        out.append(self._to_str(self.discharge_coefficient))
        out.append(self._to_str(self.zone_1_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_1))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_1))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_1))
        out.append(self._to_str(self.zone_2_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_2))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_2))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_2))
        out.append(self._to_str(self.zone_3_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_3))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_3))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_3))
        out.append(self._to_str(self.zone_4_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_4))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_4))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_4))
        out.append(self._to_str(self.zone_5_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_5))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_5))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_5))
        out.append(self._to_str(self.zone_6_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_6))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_6))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_6))
        out.append(self._to_str(self.zone_7_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_7))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_7))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_7))
        out.append(self._to_str(self.zone_8_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_8))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_8))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_8))
        out.append(self._to_str(self.zone_9_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_9))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_9))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_9))
        out.append(self._to_str(self.zone_10_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_10))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_10))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_10))
        out.append(self._to_str(self.zone_11_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_11))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_11))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_11))
        out.append(self._to_str(self.zone_12_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_12))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_12))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_12))
        out.append(self._to_str(self.zone_13_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_13))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_13))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_13))
        out.append(self._to_str(self.zone_14_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_14))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_14))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_14))
        out.append(self._to_str(self.zone_15_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_15))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_15))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_15))
        out.append(self._to_str(self.zone_16_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_16))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_16))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_16))
        out.append(self._to_str(self.zone_17_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_17))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_17))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_17))
        out.append(self._to_str(self.zone_18_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_18))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_18))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_18))
        out.append(self._to_str(self.zone_19_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_19))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_19))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_19))
        out.append(self._to_str(self.zone_20_name))
        out.append(self._to_str(self.distance_from_top_of_thermal_chimney_to_inlet_20))
        out.append(self._to_str(self.relative_ratios_of_air_flow_rates_passing_through_zone_20))
        out.append(self._to_str(self.cross_sectional_areas_of_air_channel_inlet_20))
        return ",".join(out)