from collections import OrderedDict

class DesignSpecificationOutdoorAir(object):
    """ Corresponds to IDD object `DesignSpecification:OutdoorAir`
        This object is used to describe general outdoor air requirements which
        are referenced by other objects.
    
    """
    internal_name = "DesignSpecification:OutdoorAir"
    field_count = 7
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DesignSpecification:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outdoor Air Method"] = None
        self._data["Outdoor Air Flow per Person"] = None
        self._data["Outdoor Air Flow per Zone Floor Area"] = None
        self._data["Outdoor Air Flow per Zone"] = None
        self._data["Outdoor Air Flow Air Changes per Hour"] = None
        self._data["Outdoor Air Flow Rate Fraction Schedule Name"] = None
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
            self.outdoor_air_method = None
        else:
            self.outdoor_air_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_per_person = None
        else:
            self.outdoor_air_flow_per_person = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_per_zone_floor_area = None
        else:
            self.outdoor_air_flow_per_zone_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_per_zone = None
        else:
            self.outdoor_air_flow_per_zone = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_air_changes_per_hour = None
        else:
            self.outdoor_air_flow_air_changes_per_hour = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_fraction_schedule_name = None
        else:
            self.outdoor_air_flow_rate_fraction_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def outdoor_air_method(self):
        """Get outdoor_air_method

        Returns:
            str: the value of `outdoor_air_method` or None if not set
        """
        return self._data["Outdoor Air Method"]

    @outdoor_air_method.setter
    def outdoor_air_method(self, value="Flow/Person"):
        """  Corresponds to IDD Field `outdoor_air_method`
        Flow/Person => Outdoor Air Flow per Person * Occupancy = Design Flow Rate,
        Flow/Area => Outdoor Air Flow per Zone Floor Area * Zone Floor Area = Design Flow Rate,
        Flow/Zone => Outdoor Air Flow per Zone = Design Flow Rate,
        AirChanges/Hour => Outdoor Air Flow Air Changes per Hour * Zone Volume adjusted for m3/s = Design Flow Rate

        Args:
            value (str): value for IDD Field `outdoor_air_method`
                Accepted values are:
                      - Flow/Person
                      - Flow/Area
                      - Flow/Zone
                      - AirChanges/Hour
                      - Sum
                      - Maximum
                Default value: Flow/Person
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_method`')
            vals = {}
            vals["flow/person"] = "Flow/Person"
            vals["flow/area"] = "Flow/Area"
            vals["flow/zone"] = "Flow/Zone"
            vals["airchanges/hour"] = "AirChanges/Hour"
            vals["sum"] = "Sum"
            vals["maximum"] = "Maximum"
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
                                     'field `outdoor_air_method`'.format(value))
            value = vals[value_lower]

        self._data["Outdoor Air Method"] = value

    @property
    def outdoor_air_flow_per_person(self):
        """Get outdoor_air_flow_per_person

        Returns:
            float: the value of `outdoor_air_flow_per_person` or None if not set
        """
        return self._data["Outdoor Air Flow per Person"]

    @outdoor_air_flow_per_person.setter
    def outdoor_air_flow_per_person(self, value=0.00944 ):
        """  Corresponds to IDD Field `outdoor_air_flow_per_person`
        0.00944 m3/s is equivalent to 20 cfm per person
        This input should be used if the field Outdoor Air Method is Flow/Person.
        This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum

        Args:
            value (float): value for IDD Field `outdoor_air_flow_per_person`
                Units: m3/s-person
                Default value: 0.00944
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
                                 'for field `outdoor_air_flow_per_person`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_per_person`')

        self._data["Outdoor Air Flow per Person"] = value

    @property
    def outdoor_air_flow_per_zone_floor_area(self):
        """Get outdoor_air_flow_per_zone_floor_area

        Returns:
            float: the value of `outdoor_air_flow_per_zone_floor_area` or None if not set
        """
        return self._data["Outdoor Air Flow per Zone Floor Area"]

    @outdoor_air_flow_per_zone_floor_area.setter
    def outdoor_air_flow_per_zone_floor_area(self, value=0.0 ):
        """  Corresponds to IDD Field `outdoor_air_flow_per_zone_floor_area`
        This input should be used if the field Outdoor Air Method is Flow/Area.
        This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum

        Args:
            value (float): value for IDD Field `outdoor_air_flow_per_zone_floor_area`
                Units: m3/s-m2
                Default value: 0.0
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
                                 'for field `outdoor_air_flow_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_per_zone_floor_area`')

        self._data["Outdoor Air Flow per Zone Floor Area"] = value

    @property
    def outdoor_air_flow_per_zone(self):
        """Get outdoor_air_flow_per_zone

        Returns:
            float: the value of `outdoor_air_flow_per_zone` or None if not set
        """
        return self._data["Outdoor Air Flow per Zone"]

    @outdoor_air_flow_per_zone.setter
    def outdoor_air_flow_per_zone(self, value=0.0 ):
        """  Corresponds to IDD Field `outdoor_air_flow_per_zone`
        This input should be used if the field Outdoor Air Method is Flow/Zone.
        This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum

        Args:
            value (float): value for IDD Field `outdoor_air_flow_per_zone`
                Units: m3/s
                Default value: 0.0
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
                                 'for field `outdoor_air_flow_per_zone`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_per_zone`')

        self._data["Outdoor Air Flow per Zone"] = value

    @property
    def outdoor_air_flow_air_changes_per_hour(self):
        """Get outdoor_air_flow_air_changes_per_hour

        Returns:
            float: the value of `outdoor_air_flow_air_changes_per_hour` or None if not set
        """
        return self._data["Outdoor Air Flow Air Changes per Hour"]

    @outdoor_air_flow_air_changes_per_hour.setter
    def outdoor_air_flow_air_changes_per_hour(self, value=0.0 ):
        """  Corresponds to IDD Field `outdoor_air_flow_air_changes_per_hour`
        This input should be used if the field Outdoor Air Method is AirChanges/Hour.
        This input is used if the field Outdoor Air Method is AirChanges/Hour, Sum, or Maximum

        Args:
            value (float): value for IDD Field `outdoor_air_flow_air_changes_per_hour`
                Units: 1/hr
                Default value: 0.0
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
                                 'for field `outdoor_air_flow_air_changes_per_hour`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `outdoor_air_flow_air_changes_per_hour`')

        self._data["Outdoor Air Flow Air Changes per Hour"] = value

    @property
    def outdoor_air_flow_rate_fraction_schedule_name(self):
        """Get outdoor_air_flow_rate_fraction_schedule_name

        Returns:
            str: the value of `outdoor_air_flow_rate_fraction_schedule_name` or None if not set
        """
        return self._data["Outdoor Air Flow Rate Fraction Schedule Name"]

    @outdoor_air_flow_rate_fraction_schedule_name.setter
    def outdoor_air_flow_rate_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `outdoor_air_flow_rate_fraction_schedule_name`
        Schedule values are multiplied by the Outdoor Air Flow rate calculated using
        the previous four inputs. Schedule values are limited to 0 to 1.

        Args:
            value (str): value for IDD Field `outdoor_air_flow_rate_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `outdoor_air_flow_rate_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `outdoor_air_flow_rate_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `outdoor_air_flow_rate_fraction_schedule_name`')

        self._data["Outdoor Air Flow Rate Fraction Schedule Name"] = value

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

class DesignSpecificationZoneAirDistribution(object):
    """ Corresponds to IDD object `DesignSpecification:ZoneAirDistribution`
        This object is used to describe zone air distribution in terms of air distribution
        effectiveness and secondary recirculation fraction. It is referenced by Sizing:Zone
        and Controller:MechanicalVentilation objects
    
    """
    internal_name = "DesignSpecification:ZoneAirDistribution"
    field_count = 5
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DesignSpecification:ZoneAirDistribution`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Air Distribution Effectiveness in Cooling Mode"] = None
        self._data["Zone Air Distribution Effectiveness in Heating Mode"] = None
        self._data["Zone Air Distribution Effectiveness Schedule Name"] = None
        self._data["Zone Secondary Recirculation Fraction"] = None
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
            self.zone_air_distribution_effectiveness_in_cooling_mode = None
        else:
            self.zone_air_distribution_effectiveness_in_cooling_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_air_distribution_effectiveness_in_heating_mode = None
        else:
            self.zone_air_distribution_effectiveness_in_heating_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_air_distribution_effectiveness_schedule_name = None
        else:
            self.zone_air_distribution_effectiveness_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_secondary_recirculation_fraction = None
        else:
            self.zone_secondary_recirculation_fraction = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_air_distribution_effectiveness_in_cooling_mode(self):
        """Get zone_air_distribution_effectiveness_in_cooling_mode

        Returns:
            float: the value of `zone_air_distribution_effectiveness_in_cooling_mode` or None if not set
        """
        return self._data["Zone Air Distribution Effectiveness in Cooling Mode"]

    @zone_air_distribution_effectiveness_in_cooling_mode.setter
    def zone_air_distribution_effectiveness_in_cooling_mode(self, value=1.0 ):
        """  Corresponds to IDD Field `zone_air_distribution_effectiveness_in_cooling_mode`

        Args:
            value (float): value for IDD Field `zone_air_distribution_effectiveness_in_cooling_mode`
                Units: dimensionless
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
                                 'for field `zone_air_distribution_effectiveness_in_cooling_mode`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zone_air_distribution_effectiveness_in_cooling_mode`')

        self._data["Zone Air Distribution Effectiveness in Cooling Mode"] = value

    @property
    def zone_air_distribution_effectiveness_in_heating_mode(self):
        """Get zone_air_distribution_effectiveness_in_heating_mode

        Returns:
            float: the value of `zone_air_distribution_effectiveness_in_heating_mode` or None if not set
        """
        return self._data["Zone Air Distribution Effectiveness in Heating Mode"]

    @zone_air_distribution_effectiveness_in_heating_mode.setter
    def zone_air_distribution_effectiveness_in_heating_mode(self, value=1.0 ):
        """  Corresponds to IDD Field `zone_air_distribution_effectiveness_in_heating_mode`

        Args:
            value (float): value for IDD Field `zone_air_distribution_effectiveness_in_heating_mode`
                Units: dimensionless
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
                                 'for field `zone_air_distribution_effectiveness_in_heating_mode`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zone_air_distribution_effectiveness_in_heating_mode`')

        self._data["Zone Air Distribution Effectiveness in Heating Mode"] = value

    @property
    def zone_air_distribution_effectiveness_schedule_name(self):
        """Get zone_air_distribution_effectiveness_schedule_name

        Returns:
            str: the value of `zone_air_distribution_effectiveness_schedule_name` or None if not set
        """
        return self._data["Zone Air Distribution Effectiveness Schedule Name"]

    @zone_air_distribution_effectiveness_schedule_name.setter
    def zone_air_distribution_effectiveness_schedule_name(self, value=None):
        """  Corresponds to IDD Field `zone_air_distribution_effectiveness_schedule_name`
        optionally used to replace Zone Air Distribution Effectiveness in Cooling and
        Heating Mode

        Args:
            value (str): value for IDD Field `zone_air_distribution_effectiveness_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_air_distribution_effectiveness_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_air_distribution_effectiveness_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_air_distribution_effectiveness_schedule_name`')

        self._data["Zone Air Distribution Effectiveness Schedule Name"] = value

    @property
    def zone_secondary_recirculation_fraction(self):
        """Get zone_secondary_recirculation_fraction

        Returns:
            float: the value of `zone_secondary_recirculation_fraction` or None if not set
        """
        return self._data["Zone Secondary Recirculation Fraction"]

    @zone_secondary_recirculation_fraction.setter
    def zone_secondary_recirculation_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `zone_secondary_recirculation_fraction`

        Args:
            value (float): value for IDD Field `zone_secondary_recirculation_fraction`
                Units: dimensionless
                Default value: 0.0
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
                                 'for field `zone_secondary_recirculation_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_secondary_recirculation_fraction`')

        self._data["Zone Secondary Recirculation Fraction"] = value

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

class SizingParameters(object):
    """ Corresponds to IDD object `Sizing:Parameters`
        Specifies global heating and cooling sizing factors/ratios.
        These ratios are applied at the zone level to all of the zone heating and cooling loads
        and air flow rates. Then these new loads and air flow rates are used to calculate the
        system level flow rates and capacities and are used in all component sizing calculations.
        Specifies the width (in load timesteps) of a moving average window
        which is used to smooth the peak load across more than one timestep.
    
    """
    internal_name = "Sizing:Parameters"
    field_count = 3
    required_fields = []

    def __init__(self):
        """ Init data dictionary object for IDD  `Sizing:Parameters`
        """
        self._data = OrderedDict()
        self._data["Heating Sizing Factor"] = None
        self._data["Cooling Sizing Factor"] = None
        self._data["Timesteps in Averaging Window"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.heating_sizing_factor = None
        else:
            self.heating_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_sizing_factor = None
        else:
            self.cooling_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.timesteps_in_averaging_window = None
        else:
            self.timesteps_in_averaging_window = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def heating_sizing_factor(self):
        """Get heating_sizing_factor

        Returns:
            float: the value of `heating_sizing_factor` or None if not set
        """
        return self._data["Heating Sizing Factor"]

    @heating_sizing_factor.setter
    def heating_sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `heating_sizing_factor`

        Args:
            value (float): value for IDD Field `heating_sizing_factor`
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
                                 'for field `heating_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `heating_sizing_factor`')

        self._data["Heating Sizing Factor"] = value

    @property
    def cooling_sizing_factor(self):
        """Get cooling_sizing_factor

        Returns:
            float: the value of `cooling_sizing_factor` or None if not set
        """
        return self._data["Cooling Sizing Factor"]

    @cooling_sizing_factor.setter
    def cooling_sizing_factor(self, value=1.0 ):
        """  Corresponds to IDD Field `cooling_sizing_factor`

        Args:
            value (float): value for IDD Field `cooling_sizing_factor`
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
                                 'for field `cooling_sizing_factor`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `cooling_sizing_factor`')

        self._data["Cooling Sizing Factor"] = value

    @property
    def timesteps_in_averaging_window(self):
        """Get timesteps_in_averaging_window

        Returns:
            int: the value of `timesteps_in_averaging_window` or None if not set
        """
        return self._data["Timesteps in Averaging Window"]

    @timesteps_in_averaging_window.setter
    def timesteps_in_averaging_window(self, value=None):
        """  Corresponds to IDD Field `timesteps_in_averaging_window`
        blank => set the timesteps in averaging window to
        Number of Timesteps per Hour resulting in a 1 hour averaging window
        default is number of timesteps for 1 hour averaging window

        Args:
            value (int): value for IDD Field `timesteps_in_averaging_window`
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
                                 'for field `timesteps_in_averaging_window`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `timesteps_in_averaging_window`')

        self._data["Timesteps in Averaging Window"] = value

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

class SizingZone(object):
    """ Corresponds to IDD object `Sizing:Zone`
        Specifies the data needed to perform a zone design air flow calculation.
        The calculation is done for every sizing period included in the input. The maximum
        cooling and heating load and cooling, heating, and ventilation air flows are then saved
        for system level and zone component design calculations.
    
    """
    internal_name = "Sizing:Zone"
    field_count = 23
    required_fields = ["Zone or ZoneList Name", "Zone Cooling Design Supply Air Temperature Input Method", "Zone Heating Design Supply Air Temperature Input Method", "Zone Cooling Design Supply Air Humidity Ratio", "Zone Heating Design Supply Air Humidity Ratio"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Sizing:Zone`
        """
        self._data = OrderedDict()
        self._data["Zone or ZoneList Name"] = None
        self._data["Zone Cooling Design Supply Air Temperature Input Method"] = None
        self._data["Zone Cooling Design Supply Air Temperature"] = None
        self._data["Zone Cooling Design Supply Air Temperature Difference"] = None
        self._data["Zone Heating Design Supply Air Temperature Input Method"] = None
        self._data["Zone Heating Design Supply Air Temperature"] = None
        self._data["Zone Heating Design Supply Air Temperature Difference"] = None
        self._data["Zone Cooling Design Supply Air Humidity Ratio"] = None
        self._data["Zone Heating Design Supply Air Humidity Ratio"] = None
        self._data["Design Specification Outdoor Air Object Name"] = None
        self._data["Zone Heating Sizing Factor"] = None
        self._data["Zone Cooling Sizing Factor"] = None
        self._data["Cooling Design Air Flow Method"] = None
        self._data["Cooling Design Air Flow Rate"] = None
        self._data["Cooling Minimum Air Flow per Zone Floor Area"] = None
        self._data["Cooling Minimum Air Flow"] = None
        self._data["Cooling Minimum Air Flow Fraction"] = None
        self._data["Heating Design Air Flow Method"] = None
        self._data["Heating Design Air Flow Rate"] = None
        self._data["Heating Maximum Air Flow per Zone Floor Area"] = None
        self._data["Heating Maximum Air Flow"] = None
        self._data["Heating Maximum Air Flow Fraction"] = None
        self._data["Design Specification Zone Air Distribution Object Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_temperature_input_method = None
        else:
            self.zone_cooling_design_supply_air_temperature_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_temperature = None
        else:
            self.zone_cooling_design_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_temperature_difference = None
        else:
            self.zone_cooling_design_supply_air_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_temperature_input_method = None
        else:
            self.zone_heating_design_supply_air_temperature_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_temperature = None
        else:
            self.zone_heating_design_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_temperature_difference = None
        else:
            self.zone_heating_design_supply_air_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_cooling_design_supply_air_humidity_ratio = None
        else:
            self.zone_cooling_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_heating_design_supply_air_humidity_ratio = None
        else:
            self.zone_heating_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_outdoor_air_object_name = None
        else:
            self.design_specification_outdoor_air_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_heating_sizing_factor = None
        else:
            self.zone_heating_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_cooling_sizing_factor = None
        else:
            self.zone_cooling_sizing_factor = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_method = None
        else:
            self.cooling_design_air_flow_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_rate = None
        else:
            self.cooling_design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_minimum_air_flow_per_zone_floor_area = None
        else:
            self.cooling_minimum_air_flow_per_zone_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_minimum_air_flow = None
        else:
            self.cooling_minimum_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_minimum_air_flow_fraction = None
        else:
            self.cooling_minimum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_air_flow_method = None
        else:
            self.heating_design_air_flow_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_air_flow_rate = None
        else:
            self.heating_design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_maximum_air_flow_per_zone_floor_area = None
        else:
            self.heating_maximum_air_flow_per_zone_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_maximum_air_flow = None
        else:
            self.heating_maximum_air_flow = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_maximum_air_flow_fraction = None
        else:
            self.heating_maximum_air_flow_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_specification_zone_air_distribution_object_name = None
        else:
            self.design_specification_zone_air_distribution_object_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def zone_cooling_design_supply_air_temperature_input_method(self):
        """Get zone_cooling_design_supply_air_temperature_input_method

        Returns:
            str: the value of `zone_cooling_design_supply_air_temperature_input_method` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Temperature Input Method"]

    @zone_cooling_design_supply_air_temperature_input_method.setter
    def zone_cooling_design_supply_air_temperature_input_method(self, value="SupplyAirTemperature"):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_temperature_input_method`

        Args:
            value (str): value for IDD Field `zone_cooling_design_supply_air_temperature_input_method`
                Accepted values are:
                      - SupplyAirTemperature
                      - TemperatureDifference
                Default value: SupplyAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_cooling_design_supply_air_temperature_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_cooling_design_supply_air_temperature_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_cooling_design_supply_air_temperature_input_method`')
            vals = {}
            vals["supplyairtemperature"] = "SupplyAirTemperature"
            vals["temperaturedifference"] = "TemperatureDifference"
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
                                     'field `zone_cooling_design_supply_air_temperature_input_method`'.format(value))
            value = vals[value_lower]

        self._data["Zone Cooling Design Supply Air Temperature Input Method"] = value

    @property
    def zone_cooling_design_supply_air_temperature(self):
        """Get zone_cooling_design_supply_air_temperature

        Returns:
            float: the value of `zone_cooling_design_supply_air_temperature` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Temperature"]

    @zone_cooling_design_supply_air_temperature.setter
    def zone_cooling_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_temperature`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `zone_cooling_design_supply_air_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_cooling_design_supply_air_temperature`'.format(value))

        self._data["Zone Cooling Design Supply Air Temperature"] = value

    @property
    def zone_cooling_design_supply_air_temperature_difference(self):
        """Get zone_cooling_design_supply_air_temperature_difference

        Returns:
            float: the value of `zone_cooling_design_supply_air_temperature_difference` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Temperature Difference"]

    @zone_cooling_design_supply_air_temperature_difference.setter
    def zone_cooling_design_supply_air_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_temperature_difference`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be subtracted from the zone temperature
        at peak load to calculate the Zone Cooling Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `zone_cooling_design_supply_air_temperature_difference`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_cooling_design_supply_air_temperature_difference`'.format(value))

        self._data["Zone Cooling Design Supply Air Temperature Difference"] = value

    @property
    def zone_heating_design_supply_air_temperature_input_method(self):
        """Get zone_heating_design_supply_air_temperature_input_method

        Returns:
            str: the value of `zone_heating_design_supply_air_temperature_input_method` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Temperature Input Method"]

    @zone_heating_design_supply_air_temperature_input_method.setter
    def zone_heating_design_supply_air_temperature_input_method(self, value="SupplyAirTemperature"):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_temperature_input_method`

        Args:
            value (str): value for IDD Field `zone_heating_design_supply_air_temperature_input_method`
                Accepted values are:
                      - SupplyAirTemperature
                      - TemperatureDifference
                Default value: SupplyAirTemperature
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_heating_design_supply_air_temperature_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_heating_design_supply_air_temperature_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_heating_design_supply_air_temperature_input_method`')
            vals = {}
            vals["supplyairtemperature"] = "SupplyAirTemperature"
            vals["temperaturedifference"] = "TemperatureDifference"
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
                                     'field `zone_heating_design_supply_air_temperature_input_method`'.format(value))
            value = vals[value_lower]

        self._data["Zone Heating Design Supply Air Temperature Input Method"] = value

    @property
    def zone_heating_design_supply_air_temperature(self):
        """Get zone_heating_design_supply_air_temperature

        Returns:
            float: the value of `zone_heating_design_supply_air_temperature` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Temperature"]

    @zone_heating_design_supply_air_temperature.setter
    def zone_heating_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_temperature`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `zone_heating_design_supply_air_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_heating_design_supply_air_temperature`'.format(value))

        self._data["Zone Heating Design Supply Air Temperature"] = value

    @property
    def zone_heating_design_supply_air_temperature_difference(self):
        """Get zone_heating_design_supply_air_temperature_difference

        Returns:
            float: the value of `zone_heating_design_supply_air_temperature_difference` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Temperature Difference"]

    @zone_heating_design_supply_air_temperature_difference.setter
    def zone_heating_design_supply_air_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_temperature_difference`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be added to the zone temperature
        at peak load to calculate the Zone Heating Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `zone_heating_design_supply_air_temperature_difference`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `zone_heating_design_supply_air_temperature_difference`'.format(value))

        self._data["Zone Heating Design Supply Air Temperature Difference"] = value

    @property
    def zone_cooling_design_supply_air_humidity_ratio(self):
        """Get zone_cooling_design_supply_air_humidity_ratio

        Returns:
            float: the value of `zone_cooling_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Zone Cooling Design Supply Air Humidity Ratio"]

    @zone_cooling_design_supply_air_humidity_ratio.setter
    def zone_cooling_design_supply_air_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `zone_cooling_design_supply_air_humidity_ratio`
                Units: kgWater/kgDryAir
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
                                 'for field `zone_cooling_design_supply_air_humidity_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_cooling_design_supply_air_humidity_ratio`')

        self._data["Zone Cooling Design Supply Air Humidity Ratio"] = value

    @property
    def zone_heating_design_supply_air_humidity_ratio(self):
        """Get zone_heating_design_supply_air_humidity_ratio

        Returns:
            float: the value of `zone_heating_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Zone Heating Design Supply Air Humidity Ratio"]

    @zone_heating_design_supply_air_humidity_ratio.setter
    def zone_heating_design_supply_air_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `zone_heating_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `zone_heating_design_supply_air_humidity_ratio`
                Units: kgWater/kgDryAir
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
                                 'for field `zone_heating_design_supply_air_humidity_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_heating_design_supply_air_humidity_ratio`')

        self._data["Zone Heating Design Supply Air Humidity Ratio"] = value

    @property
    def design_specification_outdoor_air_object_name(self):
        """Get design_specification_outdoor_air_object_name

        Returns:
            str: the value of `design_specification_outdoor_air_object_name` or None if not set
        """
        return self._data["Design Specification Outdoor Air Object Name"]

    @design_specification_outdoor_air_object_name.setter
    def design_specification_outdoor_air_object_name(self, value=None):
        """  Corresponds to IDD Field `design_specification_outdoor_air_object_name`

        Args:
            value (str): value for IDD Field `design_specification_outdoor_air_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_outdoor_air_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_outdoor_air_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_outdoor_air_object_name`')

        self._data["Design Specification Outdoor Air Object Name"] = value

    @property
    def zone_heating_sizing_factor(self):
        """Get zone_heating_sizing_factor

        Returns:
            float: the value of `zone_heating_sizing_factor` or None if not set
        """
        return self._data["Zone Heating Sizing Factor"]

    @zone_heating_sizing_factor.setter
    def zone_heating_sizing_factor(self, value=None):
        """  Corresponds to IDD Field `zone_heating_sizing_factor`
        if blank or zero, global heating sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `zone_heating_sizing_factor`
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
                                 'for field `zone_heating_sizing_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_heating_sizing_factor`')

        self._data["Zone Heating Sizing Factor"] = value

    @property
    def zone_cooling_sizing_factor(self):
        """Get zone_cooling_sizing_factor

        Returns:
            float: the value of `zone_cooling_sizing_factor` or None if not set
        """
        return self._data["Zone Cooling Sizing Factor"]

    @zone_cooling_sizing_factor.setter
    def zone_cooling_sizing_factor(self, value=None):
        """  Corresponds to IDD Field `zone_cooling_sizing_factor`
        if blank or zero, global cooling sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `zone_cooling_sizing_factor`
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
                                 'for field `zone_cooling_sizing_factor`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `zone_cooling_sizing_factor`')

        self._data["Zone Cooling Sizing Factor"] = value

    @property
    def cooling_design_air_flow_method(self):
        """Get cooling_design_air_flow_method

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self._data["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `cooling_design_air_flow_method`

        Args:
            value (str): value for IDD Field `cooling_design_air_flow_method`
                Accepted values are:
                      - Flow/Zone
                      - DesignDay
                      - DesignDayWithLimit
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_air_flow_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_design_air_flow_method`')
            vals = {}
            vals["flow/zone"] = "Flow/Zone"
            vals["designday"] = "DesignDay"
            vals["designdaywithlimit"] = "DesignDayWithLimit"
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
                                     'field `cooling_design_air_flow_method`'.format(value))
            value = vals[value_lower]

        self._data["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_air_flow_rate(self):
        """Get cooling_design_air_flow_rate

        Returns:
            float: the value of `cooling_design_air_flow_rate` or None if not set
        """
        return self._data["Cooling Design Air Flow Rate"]

    @cooling_design_air_flow_rate.setter
    def cooling_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_design_air_flow_rate`
        This input is used if Cooling Design Air Flow Method is Flow/Zone
        This value will be multiplied by the global or zone sizing factor and
        by zone multipliers.

        Args:
            value (float): value for IDD Field `cooling_design_air_flow_rate`
                Units: m3/s
                Default value: 0.0
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
                                 'for field `cooling_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_air_flow_rate`')

        self._data["Cooling Design Air Flow Rate"] = value

    @property
    def cooling_minimum_air_flow_per_zone_floor_area(self):
        """Get cooling_minimum_air_flow_per_zone_floor_area

        Returns:
            float: the value of `cooling_minimum_air_flow_per_zone_floor_area` or None if not set
        """
        return self._data["Cooling Minimum Air Flow per Zone Floor Area"]

    @cooling_minimum_air_flow_per_zone_floor_area.setter
    def cooling_minimum_air_flow_per_zone_floor_area(self, value=0.000762 ):
        """  Corresponds to IDD Field `cooling_minimum_air_flow_per_zone_floor_area`
        default is .15 cfm/ft2
        This input is used if Cooling Design Air Flow Method is DesignDayWithLimit

        Args:
            value (float): value for IDD Field `cooling_minimum_air_flow_per_zone_floor_area`
                Units: m3/s-m2
                Default value: 0.000762
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
                                 'for field `cooling_minimum_air_flow_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_minimum_air_flow_per_zone_floor_area`')

        self._data["Cooling Minimum Air Flow per Zone Floor Area"] = value

    @property
    def cooling_minimum_air_flow(self):
        """Get cooling_minimum_air_flow

        Returns:
            float: the value of `cooling_minimum_air_flow` or None if not set
        """
        return self._data["Cooling Minimum Air Flow"]

    @cooling_minimum_air_flow.setter
    def cooling_minimum_air_flow(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_minimum_air_flow`
        This input is used if Cooling Design Air Flow Method is DesignDayWithLimit

        Args:
            value (float): value for IDD Field `cooling_minimum_air_flow`
                Units: m3/s
                Default value: 0.0
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
                                 'for field `cooling_minimum_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_minimum_air_flow`')

        self._data["Cooling Minimum Air Flow"] = value

    @property
    def cooling_minimum_air_flow_fraction(self):
        """Get cooling_minimum_air_flow_fraction

        Returns:
            float: the value of `cooling_minimum_air_flow_fraction` or None if not set
        """
        return self._data["Cooling Minimum Air Flow Fraction"]

    @cooling_minimum_air_flow_fraction.setter
    def cooling_minimum_air_flow_fraction(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_minimum_air_flow_fraction`
        fraction of the Cooling design Air Flow Rate
        This input is currently used in sizing the Fan minimum Flow Rate.
        It does not currently affect other component autosizing.

        Args:
            value (float): value for IDD Field `cooling_minimum_air_flow_fraction`
                Default value: 0.0
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
                                 'for field `cooling_minimum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_minimum_air_flow_fraction`')

        self._data["Cooling Minimum Air Flow Fraction"] = value

    @property
    def heating_design_air_flow_method(self):
        """Get heating_design_air_flow_method

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set
        """
        return self._data["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `heating_design_air_flow_method`

        Args:
            value (str): value for IDD Field `heating_design_air_flow_method`
                Accepted values are:
                      - Flow/Zone
                      - DesignDay
                      - DesignDayWithLimit
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_air_flow_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_design_air_flow_method`')
            vals = {}
            vals["flow/zone"] = "Flow/Zone"
            vals["designday"] = "DesignDay"
            vals["designdaywithlimit"] = "DesignDayWithLimit"
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
                                     'field `heating_design_air_flow_method`'.format(value))
            value = vals[value_lower]

        self._data["Heating Design Air Flow Method"] = value

    @property
    def heating_design_air_flow_rate(self):
        """Get heating_design_air_flow_rate

        Returns:
            float: the value of `heating_design_air_flow_rate` or None if not set
        """
        return self._data["Heating Design Air Flow Rate"]

    @heating_design_air_flow_rate.setter
    def heating_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `heating_design_air_flow_rate`
        This input is used if Heating Design Air Flow Method is Flow/Zone.
        This value will be multiplied by the global or zone sizing factor and
        by zone multipliers.

        Args:
            value (float): value for IDD Field `heating_design_air_flow_rate`
                Units: m3/s
                Default value: 0.0
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
                                 'for field `heating_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_air_flow_rate`')

        self._data["Heating Design Air Flow Rate"] = value

    @property
    def heating_maximum_air_flow_per_zone_floor_area(self):
        """Get heating_maximum_air_flow_per_zone_floor_area

        Returns:
            float: the value of `heating_maximum_air_flow_per_zone_floor_area` or None if not set
        """
        return self._data["Heating Maximum Air Flow per Zone Floor Area"]

    @heating_maximum_air_flow_per_zone_floor_area.setter
    def heating_maximum_air_flow_per_zone_floor_area(self, value=0.002032 ):
        """  Corresponds to IDD Field `heating_maximum_air_flow_per_zone_floor_area`
        default is .40 cfm/ft2
        This field is used to size the heating design flow rate when Heating Design Air Flow Method = Flow/Zone.
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `heating_maximum_air_flow_per_zone_floor_area`
                Units: m3/s-m2
                Default value: 0.002032
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
                                 'for field `heating_maximum_air_flow_per_zone_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_maximum_air_flow_per_zone_floor_area`')

        self._data["Heating Maximum Air Flow per Zone Floor Area"] = value

    @property
    def heating_maximum_air_flow(self):
        """Get heating_maximum_air_flow

        Returns:
            float: the value of `heating_maximum_air_flow` or None if not set
        """
        return self._data["Heating Maximum Air Flow"]

    @heating_maximum_air_flow.setter
    def heating_maximum_air_flow(self, value=0.1415762 ):
        """  Corresponds to IDD Field `heating_maximum_air_flow`
        default is 300 cfm
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `heating_maximum_air_flow`
                Units: m3/s
                Default value: 0.1415762
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
                                 'for field `heating_maximum_air_flow`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_maximum_air_flow`')

        self._data["Heating Maximum Air Flow"] = value

    @property
    def heating_maximum_air_flow_fraction(self):
        """Get heating_maximum_air_flow_fraction

        Returns:
            float: the value of `heating_maximum_air_flow_fraction` or None if not set
        """
        return self._data["Heating Maximum Air Flow Fraction"]

    @heating_maximum_air_flow_fraction.setter
    def heating_maximum_air_flow_fraction(self, value=0.3 ):
        """  Corresponds to IDD Field `heating_maximum_air_flow_fraction`
        fraction of the Heating Design Air Flow Rate
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `heating_maximum_air_flow_fraction`
                Default value: 0.3
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
                                 'for field `heating_maximum_air_flow_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_maximum_air_flow_fraction`')

        self._data["Heating Maximum Air Flow Fraction"] = value

    @property
    def design_specification_zone_air_distribution_object_name(self):
        """Get design_specification_zone_air_distribution_object_name

        Returns:
            str: the value of `design_specification_zone_air_distribution_object_name` or None if not set
        """
        return self._data["Design Specification Zone Air Distribution Object Name"]

    @design_specification_zone_air_distribution_object_name.setter
    def design_specification_zone_air_distribution_object_name(self, value=None):
        """  Corresponds to IDD Field `design_specification_zone_air_distribution_object_name`

        Args:
            value (str): value for IDD Field `design_specification_zone_air_distribution_object_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `design_specification_zone_air_distribution_object_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `design_specification_zone_air_distribution_object_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `design_specification_zone_air_distribution_object_name`')

        self._data["Design Specification Zone Air Distribution Object Name"] = value

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

class DesignSpecificationZoneHvacSizing(object):
    """ Corresponds to IDD object `DesignSpecification:ZoneHVAC:Sizing`
        This object is used to describe general scalable zone HVAC equipment sizing which
        are referenced by other objects.
    
    """
    internal_name = "DesignSpecification:ZoneHVAC:Sizing"
    field_count = 24
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `DesignSpecification:ZoneHVAC:Sizing`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Cooling Design Air Flow Method"] = None
        self._data["Cooling Design Supply Air Flow Rate"] = None
        self._data["Cooling Design Supply Air Flow Rate Per Floor Area"] = None
        self._data["Fraction of Autosized Cooling Design Supply Air Flow Rate"] = None
        self._data["Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity"] = None
        self._data["Supply Air Flow Rate Method When No Cooling or Heating is Required"] = None
        self._data["Supply Air Flow Rate When No Cooling or Heating is Required"] = None
        self._data["Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required"] = None
        self._data["Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required"] = None
        self._data["Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required"] = None
        self._data["Heating Design Air Flow Method"] = None
        self._data["Heating Design Supply Air Flow Rate"] = None
        self._data["Heating Design Supply Air Flow Rate Per Floor Area"] = None
        self._data["Fraction of Heating Design Supply Air Flow Rate"] = None
        self._data["Heating Design Supply Air Flow Rate Per Unit Heating Capacity"] = None
        self._data["Cooling Design Capacity Method"] = None
        self._data["Cooling Design Capacity"] = None
        self._data["Cooling Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Cooling Design Capacity"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
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
            self.cooling_design_air_flow_method = None
        else:
            self.cooling_design_air_flow_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_supply_air_flow_rate = None
        else:
            self.cooling_design_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_supply_air_flow_rate_per_floor_area = None
        else:
            self.cooling_design_supply_air_flow_rate_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_cooling_design_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_supply_air_flow_rate_per_unit_cooling_capacity = None
        else:
            self.cooling_design_supply_air_flow_rate_per_unit_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required = None
        else:
            self.supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required = None
        else:
            self.fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required = None
        else:
            self.fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_air_flow_method = None
        else:
            self.heating_design_air_flow_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_supply_air_flow_rate = None
        else:
            self.heating_design_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_supply_air_flow_rate_per_floor_area = None
        else:
            self.heating_design_supply_air_flow_rate_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_heating_design_supply_air_flow_rate = None
        else:
            self.fraction_of_heating_design_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_supply_air_flow_rate_per_unit_heating_capacity = None
        else:
            self.heating_design_supply_air_flow_rate_per_unit_heating_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity_method = None
        else:
            self.cooling_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity = None
        else:
            self.cooling_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity_per_floor_area = None
        else:
            self.cooling_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_capacity = None
        else:
            self.fraction_of_autosized_cooling_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def cooling_design_air_flow_method(self):
        """Get cooling_design_air_flow_method

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self._data["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="SupplyAirFlowRate"):
        """  Corresponds to IDD Field `cooling_design_air_flow_method`
        Enter the method used to determine the cooling supply air volume flow rate.
        None is used when a cooling coil is not included in the Zone HVAC Equip or this field
        may be blank. SupplyAirFlowRate => selected when the magnitude of the supply air volume
        flow rate is specified. FlowPerFloorArea => selected when the supply air volume flow rate
        is determined from total floor area served by the Zone HVAC unit and Flow Per Floor Area
        value specified. FractionOfAutosizedCoolingAirflow => is selected when the supply air volume
        is determined from a user specified fraction and the autosized cooling supply air flow rate
        value determined by the simulation. FlowPerCoolingCapacity => is selected when the supply
        air volume is determined from user specified flow per Cooling Capacity and Cooling Capacity
        determined by the simulation.

        Args:
            value (str): value for IDD Field `cooling_design_air_flow_method`
                Accepted values are:
                      - None
                      - SupplyAirFlowRate
                      - FlowPerFloorArea
                      - FractionOfAutosizedCoolingAirflow
                      - FlowPerCoolingCapacity
                Default value: SupplyAirFlowRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_air_flow_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_design_air_flow_method`')
            vals = {}
            vals["none"] = "None"
            vals["supplyairflowrate"] = "SupplyAirFlowRate"
            vals["flowperfloorarea"] = "FlowPerFloorArea"
            vals["fractionofautosizedcoolingairflow"] = "FractionOfAutosizedCoolingAirflow"
            vals["flowpercoolingcapacity"] = "FlowPerCoolingCapacity"
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
                                     'field `cooling_design_air_flow_method`'.format(value))
            value = vals[value_lower]

        self._data["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_supply_air_flow_rate(self):
        """Get cooling_design_supply_air_flow_rate

        Returns:
            float: the value of `cooling_design_supply_air_flow_rate` or None if not set
        """
        return self._data["Cooling Design Supply Air Flow Rate"]

    @cooling_design_supply_air_flow_rate.setter
    def cooling_design_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `cooling_design_supply_air_flow_rate`
        Enter the magnitude of supply air volume flow rate during cooling operation.
        Required field when Supply air Flow Rate Method During Cooling Operation is SupplyAirFlowRate.
        This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `cooling_design_supply_air_flow_rate`
                Units: m3/s
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
                                 'for field `cooling_design_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_supply_air_flow_rate`')

        self._data["Cooling Design Supply Air Flow Rate"] = value

    @property
    def cooling_design_supply_air_flow_rate_per_floor_area(self):
        """Get cooling_design_supply_air_flow_rate_per_floor_area

        Returns:
            float: the value of `cooling_design_supply_air_flow_rate_per_floor_area` or None if not set
        """
        return self._data["Cooling Design Supply Air Flow Rate Per Floor Area"]

    @cooling_design_supply_air_flow_rate_per_floor_area.setter
    def cooling_design_supply_air_flow_rate_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `cooling_design_supply_air_flow_rate_per_floor_area`
        Enter the cooling supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method During Cooling Operation is FlowPerFloorArea.
        This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `cooling_design_supply_air_flow_rate_per_floor_area`
                Units: m3/s-m2
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
                                 'for field `cooling_design_supply_air_flow_rate_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_supply_air_flow_rate_per_floor_area`')

        self._data["Cooling Design Supply Air Flow Rate Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_supply_air_flow_rate(self):
        """Get fraction_of_autosized_cooling_design_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Cooling Design Supply Air Flow Rate"]

    @fraction_of_autosized_cooling_design_supply_air_flow_rate.setter
    def fraction_of_autosized_cooling_design_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_cooling_design_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FractionOfAutosizedCoolingAirflow.
        This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_cooling_design_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_cooling_design_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_cooling_design_supply_air_flow_rate`')

        self._data["Fraction of Autosized Cooling Design Supply Air Flow Rate"] = value

    @property
    def cooling_design_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """Get cooling_design_supply_air_flow_rate_per_unit_cooling_capacity

        Returns:
            float: the value of `cooling_design_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set
        """
        return self._data["Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity"]

    @cooling_design_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def cooling_design_supply_air_flow_rate_per_unit_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `cooling_design_supply_air_flow_rate_per_unit_cooling_capacity`
        Enter the cooling supply air volume flow rate unit cooling capacity.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FlowPerCoolingCapacity. This field may be blank if a cooling coil is not
        included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `cooling_design_supply_air_flow_rate_per_unit_cooling_capacity`
                Units: m3/s-W
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
                                 'for field `cooling_design_supply_air_flow_rate_per_unit_cooling_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_supply_air_flow_rate_per_unit_cooling_capacity`')

        self._data["Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(self):
        """Get supply_air_flow_rate_method_when_no_cooling_or_heating_is_required

        Returns:
            str: the value of `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required` or None if not set
        """
        return self._data["Supply Air Flow Rate Method When No Cooling or Heating is Required"]

    @supply_air_flow_rate_method_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_method_when_no_cooling_or_heating_is_required(self, value="SupplyAirFlowRate"):
        """  Corresponds to IDD Field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`
        Enter the method used to determine the supply air volume flow rate When No Cooling or Heating
        is Required. None is used when a cooling or heating coils is not included in the Zone HVAC
        Equipment or this field may be blank. SupplyAirFlowRate => selected when the magnitude of the
        supply air volume flow rate is specified. FlowPerFloorArea => selected when the supply air
        volume flow rate is determined from total floor area served by the Zone HVAC unit and Flow Per
        Floor Area is specified. FractionOfAutosizedCoolingAirflow => is selected when the supply
        air volume is determined from a user specified fraction and the Autosized cooling supply
        air flow rate value determined by the simulation. FractionOfAutosizedHeatingAirflow => is
        selected when the supply air volume is determined from a user specified fraction and the
        Autosized heating supply air flow rate value determined by the simulation.

        Args:
            value (str): value for IDD Field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`
                Accepted values are:
                      - None
                      - SupplyAirFlowRate
                      - FlowPerFloorArea
                      - FractionOfAutosizedCoolingAirflow
                      - FractionOfAutosizedHeatingAirflow
                Default value: SupplyAirFlowRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`')
            vals = {}
            vals["none"] = "None"
            vals["supplyairflowrate"] = "SupplyAirFlowRate"
            vals["flowperfloorarea"] = "FlowPerFloorArea"
            vals["fractionofautosizedcoolingairflow"] = "FractionOfAutosizedCoolingAirflow"
            vals["fractionofautosizedheatingairflow"] = "FractionOfAutosizedHeatingAirflow"
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
                                     'field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`'.format(value))
            value = vals[value_lower]

        self._data["Supply Air Flow Rate Method When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(self):
        """Get supply_air_flow_rate_when_no_cooling_or_heating_is_required

        Returns:
            float: the value of `supply_air_flow_rate_when_no_cooling_or_heating_is_required` or None if not set
        """
        return self._data["Supply Air Flow Rate When No Cooling or Heating is Required"]

    @supply_air_flow_rate_when_no_cooling_or_heating_is_required.setter
    def supply_air_flow_rate_when_no_cooling_or_heating_is_required(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`
        Enter the magnitude of the supply air volume flow rate during when no cooling or heating
        is required. Required field when Supply air Flow Rate Method When No Cooling or Heating
        is Required is SupplyAirFlowRate.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`
                Units: m3/s
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
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_when_no_cooling_or_heating_is_required`')

        self._data["Supply Air Flow Rate When No Cooling or Heating is Required"] = value

    @property
    def supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required(self):
        """Get supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required"]

    @supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required.setter
    def supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required`
        Enter the supply air volume flow rate per total floor area.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required
        is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required`
                Units: m3/s-m2
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
                                 'for field `supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required`')

        self._data["Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required"] = value

    @property
    def fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required(self):
        """Get fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required

        Returns:
            float: the value of `fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required` or None if not set
        """
        return self._data["Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required"]

    @fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required.setter
    def fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required(self, value=None):
        """  Corresponds to IDD Field `fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required
        is FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required`
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
                                 'for field `fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required`')

        self._data["Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required"] = value

    @property
    def fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required(self):
        """Get fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required

        Returns:
            float: the value of `fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required` or None if not set
        """
        return self._data["Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required"]

    @fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required.setter
    def fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required(self, value=None):
        """  Corresponds to IDD Field `fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required
        is FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required`
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
                                 'for field `fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required`')

        self._data["Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required"] = value

    @property
    def heating_design_air_flow_method(self):
        """Get heating_design_air_flow_method

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set
        """
        return self._data["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="SupplyAirFlowRate"):
        """  Corresponds to IDD Field `heating_design_air_flow_method`
        Enter the method used to determine the heating supply air volume flow rate.
        None is used when a heating coil is not included in the Zone HVAC Equipment or this field may
        be blank. SupplyAirFlowRate => selected when the magnitude of the heating supply air volume
        flow rate is specified.  FlowPerFloorArea => selected when the supply air volume flow rate is
        determined from total floor area served by a Zone HVAC unit and user specified value of Flow
        Per Floor Area. FractionOfAutosizedHeatingAirflow => is selected when the supply air volume
        is determined from a user specified fraction and the Autosized heating supply air flow rate
        value determined by the simulation. FlowPerHeatingCapacity => is selected when the supply
        air volume is determined from user specified flow per Heating Capacity and Heating Capacity
        determined by the simulation.

        Args:
            value (str): value for IDD Field `heating_design_air_flow_method`
                Accepted values are:
                      - None
                      - SupplyAirFlowRate
                      - FlowPerFloorArea
                      - FractionOfAutosizedHeatingAirflow
                      - FlowPerHeatingCapacity
                Default value: SupplyAirFlowRate
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_air_flow_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_design_air_flow_method`')
            vals = {}
            vals["none"] = "None"
            vals["supplyairflowrate"] = "SupplyAirFlowRate"
            vals["flowperfloorarea"] = "FlowPerFloorArea"
            vals["fractionofautosizedheatingairflow"] = "FractionOfAutosizedHeatingAirflow"
            vals["flowperheatingcapacity"] = "FlowPerHeatingCapacity"
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
                                     'field `heating_design_air_flow_method`'.format(value))
            value = vals[value_lower]

        self._data["Heating Design Air Flow Method"] = value

    @property
    def heating_design_supply_air_flow_rate(self):
        """Get heating_design_supply_air_flow_rate

        Returns:
            float: the value of `heating_design_supply_air_flow_rate` or None if not set
        """
        return self._data["Heating Design Supply Air Flow Rate"]

    @heating_design_supply_air_flow_rate.setter
    def heating_design_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `heating_design_supply_air_flow_rate`
        Enter the magnitude of the supply air volume flow rate during heating operation.
        Required field when Supply air Flow Rate Method During Heating Operation is SupplyAirFlowRate.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `heating_design_supply_air_flow_rate`
                Units: m3/s
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
                                 'for field `heating_design_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_supply_air_flow_rate`')

        self._data["Heating Design Supply Air Flow Rate"] = value

    @property
    def heating_design_supply_air_flow_rate_per_floor_area(self):
        """Get heating_design_supply_air_flow_rate_per_floor_area

        Returns:
            float: the value of `heating_design_supply_air_flow_rate_per_floor_area` or None if not set
        """
        return self._data["Heating Design Supply Air Flow Rate Per Floor Area"]

    @heating_design_supply_air_flow_rate_per_floor_area.setter
    def heating_design_supply_air_flow_rate_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `heating_design_supply_air_flow_rate_per_floor_area`
        Enter the heating supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method During Heating Operation is FlowPerFloorArea.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `heating_design_supply_air_flow_rate_per_floor_area`
                Units: m3/s-m2
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
                                 'for field `heating_design_supply_air_flow_rate_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_supply_air_flow_rate_per_floor_area`')

        self._data["Heating Design Supply Air Flow Rate Per Floor Area"] = value

    @property
    def fraction_of_heating_design_supply_air_flow_rate(self):
        """Get fraction_of_heating_design_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_heating_design_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Heating Design Supply Air Flow Rate"]

    @fraction_of_heating_design_supply_air_flow_rate.setter
    def fraction_of_heating_design_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_heating_design_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method During Heating Operation is
        FractionOfAutosizedHeatingAirflow.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `fraction_of_heating_design_supply_air_flow_rate`
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
                                 'for field `fraction_of_heating_design_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_heating_design_supply_air_flow_rate`')

        self._data["Fraction of Heating Design Supply Air Flow Rate"] = value

    @property
    def heating_design_supply_air_flow_rate_per_unit_heating_capacity(self):
        """Get heating_design_supply_air_flow_rate_per_unit_heating_capacity

        Returns:
            float: the value of `heating_design_supply_air_flow_rate_per_unit_heating_capacity` or None if not set
        """
        return self._data["Heating Design Supply Air Flow Rate Per Unit Heating Capacity"]

    @heating_design_supply_air_flow_rate_per_unit_heating_capacity.setter
    def heating_design_supply_air_flow_rate_per_unit_heating_capacity(self, value=None):
        """  Corresponds to IDD Field `heating_design_supply_air_flow_rate_per_unit_heating_capacity`
        Enter the supply air volume flow rate per unit heating capacity.
        Required field when Supply air Flow Rate Method During Heating Operation is
        FlowPerHeatingCapacity.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `heating_design_supply_air_flow_rate_per_unit_heating_capacity`
                Units: m3/s-W
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
                                 'for field `heating_design_supply_air_flow_rate_per_unit_heating_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_supply_air_flow_rate_per_unit_heating_capacity`')

        self._data["Heating Design Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def cooling_design_capacity_method(self):
        """Get cooling_design_capacity_method

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set
        """
        return self._data["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="None"):
        """  Corresponds to IDD Field `cooling_design_capacity_method`
        Enter the method used to determine the cooling design capacity for scalable sizing.
        None is used when a cooling coils is not included in the Zone HVAC Equipment or
        this field may be blank. If this input field is left blank, then the design cooling
        capacity is set to zero. CoolingDesignCapacity => selected when the design cooling capacity
        value is specified or auto-sized. CapacityPerFloorArea => selected when the design cooling
        capacity is determine from user specified cooling capacity per floor area and zone floor area.
        FractionOfAutosizedCoolingCapacity => is selected when the design cooling capacity is
        determined from a user specified fraction and the auto-sized design cooling capacity.

        Args:
            value (str): value for IDD Field `cooling_design_capacity_method`
                Accepted values are:
                      - None
                      - CoolingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedCoolingCapacity
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_design_capacity_method`')
            vals = {}
            vals["none"] = "None"
            vals["coolingdesigncapacity"] = "CoolingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedcoolingcapacity"] = "FractionOfAutosizedCoolingCapacity"
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
                                     'field `cooling_design_capacity_method`'.format(value))
            value = vals[value_lower]

        self._data["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """Get cooling_design_capacity

        Returns:
            float: the value of `cooling_design_capacity` or None if not set
        """
        return self._data["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `cooling_design_capacity`
        Enter the design cooling capacity. Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float): value for IDD Field `cooling_design_capacity`
                Units: W
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
                                 'for field `cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_capacity`')

        self._data["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """Get cooling_design_capacity_per_floor_area

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `cooling_design_capacity_per_floor_area`
        Enter the cooling design capacity per zone floor area. Required field when the cooling design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `cooling_design_capacity_per_floor_area`
                Units: W/m2
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
                                 'for field `cooling_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_capacity_per_floor_area`')

        self._data["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """Get fraction_of_autosized_cooling_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_cooling_design_capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_cooling_design_capacity`
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
                                 'for field `fraction_of_autosized_cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_cooling_design_capacity`')

        self._data["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="None"):
        """  Corresponds to IDD Field `heating_design_capacity_method`
        Enter the method used to determine the heating design capacity for scalable sizing.
        None is used when a heating coil is not included in the Zone HVAC Equipment or
        this field may be blank. If this input field is left blank, then the design heating
        capacity is set to zero. HeatingDesignCapacity => selected when the design heating capacity
        value is specified or auto-sized. CapacityPerFloorArea => selected when the design cooling
        capacity is determine from user specified heating capacity per flow area and zone floor area.
        FractionOfAutosizedHeatingCapacity => is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity

        Args:
            value (str): value for IDD Field `heating_design_capacity_method`
                Accepted values are:
                      - None
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: None
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_design_capacity_method`')
            vals = {}
            vals["none"] = "None"
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
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
                                     'field `heating_design_capacity_method`'.format(value))
            value = vals[value_lower]

        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value=None):
        """  Corresponds to IDD Field `heating_design_capacity`
        Enter the design heating capacity. Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float): value for IDD Field `heating_design_capacity`
                Units: W
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
                                 'for field `heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_capacity`')

        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `heating_design_capacity_per_floor_area`
        Enter the heating design capacity per zone floor area. Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `heating_design_capacity_per_floor_area`
                Units: W/m2
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
                                 'for field `heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_capacity_per_floor_area`')

        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_heating_design_capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_heating_design_capacity`
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
                                 'for field `fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_heating_design_capacity`')

        self._data["Fraction of Autosized Heating Design Capacity"] = value

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

class SizingSystem(object):
    """ Corresponds to IDD object `Sizing:System`
        Specifies the input needed to perform sizing calculations for a central forced air
        system design air flow, heating capacity, and cooling capacity.
    
    """
    internal_name = "Sizing:System"
    field_count = 36
    required_fields = ["AirLoop Name", "Type of Load to Size On", "Minimum System Air Flow Ratio", "Preheat Design Temperature", "Preheat Design Humidity Ratio", "Precool Design Temperature", "Precool Design Humidity Ratio", "Central Cooling Design Supply Air Temperature", "Central Heating Design Supply Air Temperature", "Central Cooling Design Supply Air Humidity Ratio", "Central Heating Design Supply Air Humidity Ratio"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Sizing:System`
        """
        self._data = OrderedDict()
        self._data["AirLoop Name"] = None
        self._data["Type of Load to Size On"] = None
        self._data["Design Outdoor Air Flow Rate"] = None
        self._data["Minimum System Air Flow Ratio"] = None
        self._data["Preheat Design Temperature"] = None
        self._data["Preheat Design Humidity Ratio"] = None
        self._data["Precool Design Temperature"] = None
        self._data["Precool Design Humidity Ratio"] = None
        self._data["Central Cooling Design Supply Air Temperature"] = None
        self._data["Central Heating Design Supply Air Temperature"] = None
        self._data["Sizing Option"] = None
        self._data["100% Outdoor Air in Cooling"] = None
        self._data["100% Outdoor Air in Heating"] = None
        self._data["Central Cooling Design Supply Air Humidity Ratio"] = None
        self._data["Central Heating Design Supply Air Humidity Ratio"] = None
        self._data["Cooling Design Air Flow Method"] = None
        self._data["Cooling Design Air Flow Rate"] = None
        self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"] = None
        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = None
        self._data["Design Supply Air Flow Rate Per Unit Cooling Capacity"] = None
        self._data["Heating Design Air Flow Method"] = None
        self._data["Heating Design Air Flow Rate"] = None
        self._data["Supply Air Flow Rate Per Floor Area During Heating Operation"] = None
        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"] = None
        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate v3"] = None
        self._data["Design Supply Air Flow Rate Per Unit Heating Capacity"] = None
        self._data["System Outdoor Air Method"] = None
        self._data["Zone Maximum Outdoor Air Fraction"] = None
        self._data["Cooling Design Capacity Method"] = None
        self._data["Cooling Design Capacity"] = None
        self._data["Cooling Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Cooling Design Capacity"] = None
        self._data["Heating Design Capacity Method"] = None
        self._data["Heating Design Capacity"] = None
        self._data["Heating Design Capacity Per Floor Area"] = None
        self._data["Fraction of Autosized Heating Design Capacity"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.airloop_name = None
        else:
            self.airloop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.type_of_load_to_size_on = None
        else:
            self.type_of_load_to_size_on = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_outdoor_air_flow_rate = None
        else:
            self.design_outdoor_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_system_air_flow_ratio = None
        else:
            self.minimum_system_air_flow_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.preheat_design_temperature = None
        else:
            self.preheat_design_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.preheat_design_humidity_ratio = None
        else:
            self.preheat_design_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.precool_design_temperature = None
        else:
            self.precool_design_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.precool_design_humidity_ratio = None
        else:
            self.precool_design_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_cooling_design_supply_air_temperature = None
        else:
            self.central_cooling_design_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_heating_design_supply_air_temperature = None
        else:
            self.central_heating_design_supply_air_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.sizing_option = None
        else:
            self.sizing_option = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.a_100_outdoor_air_in_cooling = None
        else:
            self.a_100_outdoor_air_in_cooling = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.a_100_outdoor_air_in_heating = None
        else:
            self.a_100_outdoor_air_in_heating = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_cooling_design_supply_air_humidity_ratio = None
        else:
            self.central_cooling_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.central_heating_design_supply_air_humidity_ratio = None
        else:
            self.central_heating_design_supply_air_humidity_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_method = None
        else:
            self.cooling_design_air_flow_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_air_flow_rate = None
        else:
            self.cooling_design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_during_cooling_operation = None
        else:
            self.supply_air_flow_rate_per_floor_area_during_cooling_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_cooling_capacity = None
        else:
            self.design_supply_air_flow_rate_per_unit_cooling_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_air_flow_method = None
        else:
            self.heating_design_air_flow_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_air_flow_rate = None
        else:
            self.heating_design_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_during_heating_operation = None
        else:
            self.supply_air_flow_rate_per_floor_area_during_heating_operation = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_design_heating_supply_air_flow_rate = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate_v3 = None
        else:
            self.fraction_of_autosized_design_cooling_supply_air_flow_rate_v3 = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_supply_air_flow_rate_per_unit_heating_capacity = None
        else:
            self.design_supply_air_flow_rate_per_unit_heating_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.system_outdoor_air_method = None
        else:
            self.system_outdoor_air_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.zone_maximum_outdoor_air_fraction = None
        else:
            self.zone_maximum_outdoor_air_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity_method = None
        else:
            self.cooling_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity = None
        else:
            self.cooling_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_design_capacity_per_floor_area = None
        else:
            self.cooling_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_capacity = None
        else:
            self.fraction_of_autosized_cooling_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def airloop_name(self):
        """Get airloop_name

        Returns:
            str: the value of `airloop_name` or None if not set
        """
        return self._data["AirLoop Name"]

    @airloop_name.setter
    def airloop_name(self, value=None):
        """  Corresponds to IDD Field `airloop_name`

        Args:
            value (str): value for IDD Field `airloop_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `airloop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `airloop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `airloop_name`')

        self._data["AirLoop Name"] = value

    @property
    def type_of_load_to_size_on(self):
        """Get type_of_load_to_size_on

        Returns:
            str: the value of `type_of_load_to_size_on` or None if not set
        """
        return self._data["Type of Load to Size On"]

    @type_of_load_to_size_on.setter
    def type_of_load_to_size_on(self, value="Sensible"):
        """  Corresponds to IDD Field `type_of_load_to_size_on`
        Specifies the basis for sizing the system supply air flow rate
        Sensible and VentilationRequirement are the only available options
        Sensible uses the zone design air flow rates
        VentilationRequirement uses the system ventilation requirement

        Args:
            value (str): value for IDD Field `type_of_load_to_size_on`
                Accepted values are:
                      - Sensible
                      - VentilationRequirement
                Default value: Sensible
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `type_of_load_to_size_on`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `type_of_load_to_size_on`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `type_of_load_to_size_on`')
            vals = {}
            vals["sensible"] = "Sensible"
            vals["ventilationrequirement"] = "VentilationRequirement"
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
                                     'field `type_of_load_to_size_on`'.format(value))
            value = vals[value_lower]

        self._data["Type of Load to Size On"] = value

    @property
    def design_outdoor_air_flow_rate(self):
        """Get design_outdoor_air_flow_rate

        Returns:
            float: the value of `design_outdoor_air_flow_rate` or None if not set
        """
        return self._data["Design Outdoor Air Flow Rate"]

    @design_outdoor_air_flow_rate.setter
    def design_outdoor_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `design_outdoor_air_flow_rate`

        Args:
            value (float): value for IDD Field `design_outdoor_air_flow_rate`
                Units: m3/s
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
                                 'for field `design_outdoor_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_outdoor_air_flow_rate`')

        self._data["Design Outdoor Air Flow Rate"] = value

    @property
    def minimum_system_air_flow_ratio(self):
        """Get minimum_system_air_flow_ratio

        Returns:
            float: the value of `minimum_system_air_flow_ratio` or None if not set
        """
        return self._data["Minimum System Air Flow Ratio"]

    @minimum_system_air_flow_ratio.setter
    def minimum_system_air_flow_ratio(self, value=None):
        """  Corresponds to IDD Field `minimum_system_air_flow_ratio`

        Args:
            value (float): value for IDD Field `minimum_system_air_flow_ratio`
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
                                 'for field `minimum_system_air_flow_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_system_air_flow_ratio`')
            if value > 1.0:
                raise ValueError('value need to be smaller 1.0 '
                                 'for field `minimum_system_air_flow_ratio`')

        self._data["Minimum System Air Flow Ratio"] = value

    @property
    def preheat_design_temperature(self):
        """Get preheat_design_temperature

        Returns:
            float: the value of `preheat_design_temperature` or None if not set
        """
        return self._data["Preheat Design Temperature"]

    @preheat_design_temperature.setter
    def preheat_design_temperature(self, value=None):
        """  Corresponds to IDD Field `preheat_design_temperature`

        Args:
            value (float): value for IDD Field `preheat_design_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `preheat_design_temperature`'.format(value))

        self._data["Preheat Design Temperature"] = value

    @property
    def preheat_design_humidity_ratio(self):
        """Get preheat_design_humidity_ratio

        Returns:
            float: the value of `preheat_design_humidity_ratio` or None if not set
        """
        return self._data["Preheat Design Humidity Ratio"]

    @preheat_design_humidity_ratio.setter
    def preheat_design_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `preheat_design_humidity_ratio`

        Args:
            value (float): value for IDD Field `preheat_design_humidity_ratio`
                Units: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `preheat_design_humidity_ratio`'.format(value))

        self._data["Preheat Design Humidity Ratio"] = value

    @property
    def precool_design_temperature(self):
        """Get precool_design_temperature

        Returns:
            float: the value of `precool_design_temperature` or None if not set
        """
        return self._data["Precool Design Temperature"]

    @precool_design_temperature.setter
    def precool_design_temperature(self, value=None):
        """  Corresponds to IDD Field `precool_design_temperature`

        Args:
            value (float): value for IDD Field `precool_design_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `precool_design_temperature`'.format(value))

        self._data["Precool Design Temperature"] = value

    @property
    def precool_design_humidity_ratio(self):
        """Get precool_design_humidity_ratio

        Returns:
            float: the value of `precool_design_humidity_ratio` or None if not set
        """
        return self._data["Precool Design Humidity Ratio"]

    @precool_design_humidity_ratio.setter
    def precool_design_humidity_ratio(self, value=None):
        """  Corresponds to IDD Field `precool_design_humidity_ratio`

        Args:
            value (float): value for IDD Field `precool_design_humidity_ratio`
                Units: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `precool_design_humidity_ratio`'.format(value))

        self._data["Precool Design Humidity Ratio"] = value

    @property
    def central_cooling_design_supply_air_temperature(self):
        """Get central_cooling_design_supply_air_temperature

        Returns:
            float: the value of `central_cooling_design_supply_air_temperature` or None if not set
        """
        return self._data["Central Cooling Design Supply Air Temperature"]

    @central_cooling_design_supply_air_temperature.setter
    def central_cooling_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `central_cooling_design_supply_air_temperature`

        Args:
            value (float): value for IDD Field `central_cooling_design_supply_air_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `central_cooling_design_supply_air_temperature`'.format(value))

        self._data["Central Cooling Design Supply Air Temperature"] = value

    @property
    def central_heating_design_supply_air_temperature(self):
        """Get central_heating_design_supply_air_temperature

        Returns:
            float: the value of `central_heating_design_supply_air_temperature` or None if not set
        """
        return self._data["Central Heating Design Supply Air Temperature"]

    @central_heating_design_supply_air_temperature.setter
    def central_heating_design_supply_air_temperature(self, value=None):
        """  Corresponds to IDD Field `central_heating_design_supply_air_temperature`

        Args:
            value (float): value for IDD Field `central_heating_design_supply_air_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `central_heating_design_supply_air_temperature`'.format(value))

        self._data["Central Heating Design Supply Air Temperature"] = value

    @property
    def sizing_option(self):
        """Get sizing_option

        Returns:
            str: the value of `sizing_option` or None if not set
        """
        return self._data["Sizing Option"]

    @sizing_option.setter
    def sizing_option(self, value="NonCoincident"):
        """  Corresponds to IDD Field `sizing_option`

        Args:
            value (str): value for IDD Field `sizing_option`
                Accepted values are:
                      - Coincident
                      - NonCoincident
                Default value: NonCoincident
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `sizing_option`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `sizing_option`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `sizing_option`')
            vals = {}
            vals["coincident"] = "Coincident"
            vals["noncoincident"] = "NonCoincident"
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
                                     'field `sizing_option`'.format(value))
            value = vals[value_lower]

        self._data["Sizing Option"] = value

    @property
    def a_100_outdoor_air_in_cooling(self):
        """Get a_100_outdoor_air_in_cooling

        Returns:
            str: the value of `a_100_outdoor_air_in_cooling` or None if not set
        """
        return self._data["100% Outdoor Air in Cooling"]

    @a_100_outdoor_air_in_cooling.setter
    def a_100_outdoor_air_in_cooling(self, value="No"):
        """  Corresponds to IDD Field `a_100_outdoor_air_in_cooling`

        Args:
            value (str): value for IDD Field `a_100_outdoor_air_in_cooling`
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
                                 'for field `a_100_outdoor_air_in_cooling`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `a_100_outdoor_air_in_cooling`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `a_100_outdoor_air_in_cooling`')
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
                                     'field `a_100_outdoor_air_in_cooling`'.format(value))
            value = vals[value_lower]

        self._data["100% Outdoor Air in Cooling"] = value

    @property
    def a_100_outdoor_air_in_heating(self):
        """Get a_100_outdoor_air_in_heating

        Returns:
            str: the value of `a_100_outdoor_air_in_heating` or None if not set
        """
        return self._data["100% Outdoor Air in Heating"]

    @a_100_outdoor_air_in_heating.setter
    def a_100_outdoor_air_in_heating(self, value="No"):
        """  Corresponds to IDD Field `a_100_outdoor_air_in_heating`

        Args:
            value (str): value for IDD Field `a_100_outdoor_air_in_heating`
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
                                 'for field `a_100_outdoor_air_in_heating`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `a_100_outdoor_air_in_heating`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `a_100_outdoor_air_in_heating`')
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
                                     'field `a_100_outdoor_air_in_heating`'.format(value))
            value = vals[value_lower]

        self._data["100% Outdoor Air in Heating"] = value

    @property
    def central_cooling_design_supply_air_humidity_ratio(self):
        """Get central_cooling_design_supply_air_humidity_ratio

        Returns:
            float: the value of `central_cooling_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Central Cooling Design Supply Air Humidity Ratio"]

    @central_cooling_design_supply_air_humidity_ratio.setter
    def central_cooling_design_supply_air_humidity_ratio(self, value=0.008 ):
        """  Corresponds to IDD Field `central_cooling_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `central_cooling_design_supply_air_humidity_ratio`
                Units: kgWater/kgDryAir
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `central_cooling_design_supply_air_humidity_ratio`'.format(value))

        self._data["Central Cooling Design Supply Air Humidity Ratio"] = value

    @property
    def central_heating_design_supply_air_humidity_ratio(self):
        """Get central_heating_design_supply_air_humidity_ratio

        Returns:
            float: the value of `central_heating_design_supply_air_humidity_ratio` or None if not set
        """
        return self._data["Central Heating Design Supply Air Humidity Ratio"]

    @central_heating_design_supply_air_humidity_ratio.setter
    def central_heating_design_supply_air_humidity_ratio(self, value=0.008 ):
        """  Corresponds to IDD Field `central_heating_design_supply_air_humidity_ratio`

        Args:
            value (float): value for IDD Field `central_heating_design_supply_air_humidity_ratio`
                Units: kgWater/kgDryAir
                Default value: 0.008
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `central_heating_design_supply_air_humidity_ratio`'.format(value))

        self._data["Central Heating Design Supply Air Humidity Ratio"] = value

    @property
    def cooling_design_air_flow_method(self):
        """Get cooling_design_air_flow_method

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self._data["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `cooling_design_air_flow_method`

        Args:
            value (str): value for IDD Field `cooling_design_air_flow_method`
                Accepted values are:
                      - Flow/System
                      - DesignDay
                      - FlowPerFloorArea
                      - FractionOfAutosizedCoolingAirflow
                      - FlowPerCoolingCapacity
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_air_flow_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_design_air_flow_method`')
            vals = {}
            vals["flow/system"] = "Flow/System"
            vals["designday"] = "DesignDay"
            vals["flowperfloorarea"] = "FlowPerFloorArea"
            vals["fractionofautosizedcoolingairflow"] = "FractionOfAutosizedCoolingAirflow"
            vals["flowpercoolingcapacity"] = "FlowPerCoolingCapacity"
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
                                     'field `cooling_design_air_flow_method`'.format(value))
            value = vals[value_lower]

        self._data["Cooling Design Air Flow Method"] = value

    @property
    def cooling_design_air_flow_rate(self):
        """Get cooling_design_air_flow_rate

        Returns:
            float: the value of `cooling_design_air_flow_rate` or None if not set
        """
        return self._data["Cooling Design Air Flow Rate"]

    @cooling_design_air_flow_rate.setter
    def cooling_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `cooling_design_air_flow_rate`
        This input is used if Cooling Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `cooling_design_air_flow_rate`
                Units: m3/s
                Default value: 0.0
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
                                 'for field `cooling_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_air_flow_rate`')

        self._data["Cooling Design Air Flow Rate"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self):
        """Get supply_air_flow_rate_per_floor_area_during_cooling_operation

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_cooling_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"]

    @supply_air_flow_rate_per_floor_area_during_cooling_operation.setter
    def supply_air_flow_rate_per_floor_area_during_cooling_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_during_cooling_operation`
        Enter the cooling supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method during cooling operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_during_cooling_operation`
                Units: m3/s-m2
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
                                 'for field `supply_air_flow_rate_per_floor_area_during_cooling_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_during_cooling_operation`')

        self._data["Supply Air Flow Rate Per Floor Area During Cooling Operation"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_cooling_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method during cooling operation is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate"] = value

    @property
    def design_supply_air_flow_rate_per_unit_cooling_capacity(self):
        """Get design_supply_air_flow_rate_per_unit_cooling_capacity

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_cooling_capacity` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit Cooling Capacity"]

    @design_supply_air_flow_rate_per_unit_cooling_capacity.setter
    def design_supply_air_flow_rate_per_unit_cooling_capacity(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_cooling_capacity`
        Enter the supply air volume flow rate per unit cooling capacity.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FlowPerCoolingCapacity.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_cooling_capacity`
                Units: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_cooling_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_cooling_capacity`')

        self._data["Design Supply Air Flow Rate Per Unit Cooling Capacity"] = value

    @property
    def heating_design_air_flow_method(self):
        """Get heating_design_air_flow_method

        Returns:
            str: the value of `heating_design_air_flow_method` or None if not set
        """
        return self._data["Heating Design Air Flow Method"]

    @heating_design_air_flow_method.setter
    def heating_design_air_flow_method(self, value="DesignDay"):
        """  Corresponds to IDD Field `heating_design_air_flow_method`

        Args:
            value (str): value for IDD Field `heating_design_air_flow_method`
                Accepted values are:
                      - Flow/System
                      - DesignDay
                      - FlowPerFloorArea
                      - FractionOfAutosizedHeatingAirflow
                      - FractionOfAutosizedCoolingAirflow
                      - FlowPerCoolingCapacity
                Default value: DesignDay
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_air_flow_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_air_flow_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_design_air_flow_method`')
            vals = {}
            vals["flow/system"] = "Flow/System"
            vals["designday"] = "DesignDay"
            vals["flowperfloorarea"] = "FlowPerFloorArea"
            vals["fractionofautosizedheatingairflow"] = "FractionOfAutosizedHeatingAirflow"
            vals["fractionofautosizedcoolingairflow"] = "FractionOfAutosizedCoolingAirflow"
            vals["flowpercoolingcapacity"] = "FlowPerCoolingCapacity"
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
                                     'field `heating_design_air_flow_method`'.format(value))
            value = vals[value_lower]

        self._data["Heating Design Air Flow Method"] = value

    @property
    def heating_design_air_flow_rate(self):
        """Get heating_design_air_flow_rate

        Returns:
            float: the value of `heating_design_air_flow_rate` or None if not set
        """
        return self._data["Heating Design Air Flow Rate"]

    @heating_design_air_flow_rate.setter
    def heating_design_air_flow_rate(self, value=0.0 ):
        """  Corresponds to IDD Field `heating_design_air_flow_rate`
        This input is used if Heating Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `heating_design_air_flow_rate`
                Units: m3/s
                Default value: 0.0
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
                                 'for field `heating_design_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_air_flow_rate`')

        self._data["Heating Design Air Flow Rate"] = value

    @property
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self):
        """Get supply_air_flow_rate_per_floor_area_during_heating_operation

        Returns:
            float: the value of `supply_air_flow_rate_per_floor_area_during_heating_operation` or None if not set
        """
        return self._data["Supply Air Flow Rate Per Floor Area During Heating Operation"]

    @supply_air_flow_rate_per_floor_area_during_heating_operation.setter
    def supply_air_flow_rate_per_floor_area_during_heating_operation(self, value=None):
        """  Corresponds to IDD Field `supply_air_flow_rate_per_floor_area_during_heating_operation`
        Enter the heating supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method during heating operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `supply_air_flow_rate_per_floor_area_during_heating_operation`
                Units: m3/s-m2
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
                                 'for field `supply_air_flow_rate_per_floor_area_during_heating_operation`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `supply_air_flow_rate_per_floor_area_during_heating_operation`')

        self._data["Supply Air Flow Rate Per Floor Area During Heating Operation"] = value

    @property
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self):
        """Get fraction_of_autosized_design_heating_supply_air_flow_rate

        Returns:
            float: the value of `fraction_of_autosized_design_heating_supply_air_flow_rate` or None if not set
        """
        return self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"]

    @fraction_of_autosized_design_heating_supply_air_flow_rate.setter
    def fraction_of_autosized_design_heating_supply_air_flow_rate(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method during heating operation is
        FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_heating_supply_air_flow_rate`
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
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_heating_supply_air_flow_rate`')

        self._data["Fraction of Autosized Design Heating Supply Air Flow Rate"] = value

    @property
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v3(self):
        """Get fraction_of_autosized_design_cooling_supply_air_flow_rate_v3

        Returns:
            float: the value of `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3` or None if not set
        """
        return self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate v3"]

    @fraction_of_autosized_design_cooling_supply_air_flow_rate_v3.setter
    def fraction_of_autosized_design_cooling_supply_air_flow_rate_v3(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method during heating operation is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3`
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
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_design_cooling_supply_air_flow_rate_v3`')

        self._data["Fraction of Autosized Design Cooling Supply Air Flow Rate v3"] = value

    @property
    def design_supply_air_flow_rate_per_unit_heating_capacity(self):
        """Get design_supply_air_flow_rate_per_unit_heating_capacity

        Returns:
            float: the value of `design_supply_air_flow_rate_per_unit_heating_capacity` or None if not set
        """
        return self._data["Design Supply Air Flow Rate Per Unit Heating Capacity"]

    @design_supply_air_flow_rate_per_unit_heating_capacity.setter
    def design_supply_air_flow_rate_per_unit_heating_capacity(self, value=None):
        """  Corresponds to IDD Field `design_supply_air_flow_rate_per_unit_heating_capacity`
        Enter the heating supply air volume flow rate per unit heating capacity.
        Required field when Supply air Flow Rate Method during heating operation is
        FlowPerHeatingCapacity.

        Args:
            value (float): value for IDD Field `design_supply_air_flow_rate_per_unit_heating_capacity`
                Units: m3/s-W
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
                                 'for field `design_supply_air_flow_rate_per_unit_heating_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `design_supply_air_flow_rate_per_unit_heating_capacity`')

        self._data["Design Supply Air Flow Rate Per Unit Heating Capacity"] = value

    @property
    def system_outdoor_air_method(self):
        """Get system_outdoor_air_method

        Returns:
            str: the value of `system_outdoor_air_method` or None if not set
        """
        return self._data["System Outdoor Air Method"]

    @system_outdoor_air_method.setter
    def system_outdoor_air_method(self, value="ZoneSum"):
        """  Corresponds to IDD Field `system_outdoor_air_method`

        Args:
            value (str): value for IDD Field `system_outdoor_air_method`
                Accepted values are:
                      - ZoneSum
                      - VentilationRateProcedure
                Default value: ZoneSum
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `system_outdoor_air_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `system_outdoor_air_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `system_outdoor_air_method`')
            vals = {}
            vals["zonesum"] = "ZoneSum"
            vals["ventilationrateprocedure"] = "VentilationRateProcedure"
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
                                     'field `system_outdoor_air_method`'.format(value))
            value = vals[value_lower]

        self._data["System Outdoor Air Method"] = value

    @property
    def zone_maximum_outdoor_air_fraction(self):
        """Get zone_maximum_outdoor_air_fraction

        Returns:
            float: the value of `zone_maximum_outdoor_air_fraction` or None if not set
        """
        return self._data["Zone Maximum Outdoor Air Fraction"]

    @zone_maximum_outdoor_air_fraction.setter
    def zone_maximum_outdoor_air_fraction(self, value=1.0 ):
        """  Corresponds to IDD Field `zone_maximum_outdoor_air_fraction`

        Args:
            value (float): value for IDD Field `zone_maximum_outdoor_air_fraction`
                Units: dimensionless
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
                                 'for field `zone_maximum_outdoor_air_fraction`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `zone_maximum_outdoor_air_fraction`')

        self._data["Zone Maximum Outdoor Air Fraction"] = value

    @property
    def cooling_design_capacity_method(self):
        """Get cooling_design_capacity_method

        Returns:
            str: the value of `cooling_design_capacity_method` or None if not set
        """
        return self._data["Cooling Design Capacity Method"]

    @cooling_design_capacity_method.setter
    def cooling_design_capacity_method(self, value="CoolingDesignCapacity"):
        """  Corresponds to IDD Field `cooling_design_capacity_method`
        Enter the method used to determine the system cooling design capacity for scalable sizing.
        None is used when a cooling coils is not included in an airloop or this field may be blank.
        If this input field is left blank, then the design cooling capacity is set to zero.
        CoolingDesignCapacity => selected when the design cooling capacity value is specified or
        auto-sized. CapacityPerFloorArea => selected when the design cooling capacity is determined
        from user specified cooling capacity per floor area and total floor area of cooled zones
        served by an airloop. FractionOfAutosizedCoolingCapacity => is selected when the design
        cooling capacity is determined from a user specified fraction and the auto-sized design
        cooling capacity of the system.

        Args:
            value (str): value for IDD Field `cooling_design_capacity_method`
                Accepted values are:
                      - None
                      - CoolingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedCoolingCapacity
                Default value: CoolingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_design_capacity_method`')
            vals = {}
            vals["none"] = "None"
            vals["coolingdesigncapacity"] = "CoolingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedcoolingcapacity"] = "FractionOfAutosizedCoolingCapacity"
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
                                     'field `cooling_design_capacity_method`'.format(value))
            value = vals[value_lower]

        self._data["Cooling Design Capacity Method"] = value

    @property
    def cooling_design_capacity(self):
        """Get cooling_design_capacity

        Returns:
            float: the value of `cooling_design_capacity` or None if not set
        """
        return self._data["Cooling Design Capacity"]

    @cooling_design_capacity.setter
    def cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `cooling_design_capacity`
        Enter the design cooling capacity. Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float): value for IDD Field `cooling_design_capacity`
                Units: W
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
                                 'for field `cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_capacity`')

        self._data["Cooling Design Capacity"] = value

    @property
    def cooling_design_capacity_per_floor_area(self):
        """Get cooling_design_capacity_per_floor_area

        Returns:
            float: the value of `cooling_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Cooling Design Capacity Per Floor Area"]

    @cooling_design_capacity_per_floor_area.setter
    def cooling_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `cooling_design_capacity_per_floor_area`
        Enter the cooling design capacity per total floor area of cooled zones served by an airloop.
        Required field when the cooling design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `cooling_design_capacity_per_floor_area`
                Units: W/m2
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
                                 'for field `cooling_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_design_capacity_per_floor_area`')

        self._data["Cooling Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_cooling_design_capacity(self):
        """Get fraction_of_autosized_cooling_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_cooling_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Cooling Design Capacity"]

    @fraction_of_autosized_cooling_design_capacity.setter
    def fraction_of_autosized_cooling_design_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_cooling_design_capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_cooling_design_capacity`
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
                                 'for field `fraction_of_autosized_cooling_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_cooling_design_capacity`')

        self._data["Fraction of Autosized Cooling Design Capacity"] = value

    @property
    def heating_design_capacity_method(self):
        """Get heating_design_capacity_method

        Returns:
            str: the value of `heating_design_capacity_method` or None if not set
        """
        return self._data["Heating Design Capacity Method"]

    @heating_design_capacity_method.setter
    def heating_design_capacity_method(self, value="HeatingDesignCapacity"):
        """  Corresponds to IDD Field `heating_design_capacity_method`
        Enter the method used to determine the heating design capacity for scalable sizing.
        None is used when a heating coil not included in an airloop or this field may be blank.
        If this input field is left blank, then the design heating capacity is set to zero.
        HeatingDesignCapacity => selected when the design heating capacity value is specified or
        auto-sized. CapacityPerFloorArea => selected when the design heating capacity is determined
        from user specified heating capacity per flow area and total floor area of heated zones
        served by an airloop. FractionOfAutosizedHeatingCapacity => is selected when the design
        heating capacity is determined from a user specified fraction and the auto-sized design
        heating capacity of the system.

        Args:
            value (str): value for IDD Field `heating_design_capacity_method`
                Accepted values are:
                      - None
                      - HeatingDesignCapacity
                      - CapacityPerFloorArea
                      - FractionOfAutosizedHeatingCapacity
                Default value: HeatingDesignCapacity
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_design_capacity_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_design_capacity_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_design_capacity_method`')
            vals = {}
            vals["none"] = "None"
            vals["heatingdesigncapacity"] = "HeatingDesignCapacity"
            vals["capacityperfloorarea"] = "CapacityPerFloorArea"
            vals["fractionofautosizedheatingcapacity"] = "FractionOfAutosizedHeatingCapacity"
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
                                     'field `heating_design_capacity_method`'.format(value))
            value = vals[value_lower]

        self._data["Heating Design Capacity Method"] = value

    @property
    def heating_design_capacity(self):
        """Get heating_design_capacity

        Returns:
            float: the value of `heating_design_capacity` or None if not set
        """
        return self._data["Heating Design Capacity"]

    @heating_design_capacity.setter
    def heating_design_capacity(self, value=None):
        """  Corresponds to IDD Field `heating_design_capacity`
        Enter the design heating capacity. Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float): value for IDD Field `heating_design_capacity`
                Units: W
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
                                 'for field `heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_capacity`')

        self._data["Heating Design Capacity"] = value

    @property
    def heating_design_capacity_per_floor_area(self):
        """Get heating_design_capacity_per_floor_area

        Returns:
            float: the value of `heating_design_capacity_per_floor_area` or None if not set
        """
        return self._data["Heating Design Capacity Per Floor Area"]

    @heating_design_capacity_per_floor_area.setter
    def heating_design_capacity_per_floor_area(self, value=None):
        """  Corresponds to IDD Field `heating_design_capacity_per_floor_area`
        Enter the heating design capacity per zone floor area. Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `heating_design_capacity_per_floor_area`
                Units: W/m2
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
                                 'for field `heating_design_capacity_per_floor_area`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_design_capacity_per_floor_area`')

        self._data["Heating Design Capacity Per Floor Area"] = value

    @property
    def fraction_of_autosized_heating_design_capacity(self):
        """Get fraction_of_autosized_heating_design_capacity

        Returns:
            float: the value of `fraction_of_autosized_heating_design_capacity` or None if not set
        """
        return self._data["Fraction of Autosized Heating Design Capacity"]

    @fraction_of_autosized_heating_design_capacity.setter
    def fraction_of_autosized_heating_design_capacity(self, value=None):
        """  Corresponds to IDD Field `fraction_of_autosized_heating_design_capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `fraction_of_autosized_heating_design_capacity`
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
                                 'for field `fraction_of_autosized_heating_design_capacity`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fraction_of_autosized_heating_design_capacity`')

        self._data["Fraction of Autosized Heating Design Capacity"] = value

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

class SizingPlant(object):
    """ Corresponds to IDD object `Sizing:Plant`
        Specifies the input needed to autosize plant loop flow rates and equipment capacities.
        This information is initially used by components that use water for heating or cooling
        such as hot or chilled water coils to calculate their maximum water flow rates. These
        flow rates are then summed for use in calculating the Plant Loop flow rates.
    
    """
    internal_name = "Sizing:Plant"
    field_count = 4
    required_fields = ["Plant or Condenser Loop Name", "Loop Type", "Design Loop Exit Temperature", "Loop Design Temperature Difference"]

    def __init__(self):
        """ Init data dictionary object for IDD  `Sizing:Plant`
        """
        self._data = OrderedDict()
        self._data["Plant or Condenser Loop Name"] = None
        self._data["Loop Type"] = None
        self._data["Design Loop Exit Temperature"] = None
        self._data["Loop Design Temperature Difference"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.plant_or_condenser_loop_name = None
        else:
            self.plant_or_condenser_loop_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_type = None
        else:
            self.loop_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.design_loop_exit_temperature = None
        else:
            self.design_loop_exit_temperature = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.loop_design_temperature_difference = None
        else:
            self.loop_design_temperature_difference = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def plant_or_condenser_loop_name(self):
        """Get plant_or_condenser_loop_name

        Returns:
            str: the value of `plant_or_condenser_loop_name` or None if not set
        """
        return self._data["Plant or Condenser Loop Name"]

    @plant_or_condenser_loop_name.setter
    def plant_or_condenser_loop_name(self, value=None):
        """  Corresponds to IDD Field `plant_or_condenser_loop_name`
        Enter the name of a PlantLoop or a CondenserLoop object

        Args:
            value (str): value for IDD Field `plant_or_condenser_loop_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `plant_or_condenser_loop_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `plant_or_condenser_loop_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `plant_or_condenser_loop_name`')

        self._data["Plant or Condenser Loop Name"] = value

    @property
    def loop_type(self):
        """Get loop_type

        Returns:
            str: the value of `loop_type` or None if not set
        """
        return self._data["Loop Type"]

    @loop_type.setter
    def loop_type(self, value=None):
        """  Corresponds to IDD Field `loop_type`

        Args:
            value (str): value for IDD Field `loop_type`
                Accepted values are:
                      - Heating
                      - Cooling
                      - Condenser
                      - Steam
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `loop_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `loop_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `loop_type`')
            vals = {}
            vals["heating"] = "Heating"
            vals["cooling"] = "Cooling"
            vals["condenser"] = "Condenser"
            vals["steam"] = "Steam"
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
                                     'field `loop_type`'.format(value))
            value = vals[value_lower]

        self._data["Loop Type"] = value

    @property
    def design_loop_exit_temperature(self):
        """Get design_loop_exit_temperature

        Returns:
            float: the value of `design_loop_exit_temperature` or None if not set
        """
        return self._data["Design Loop Exit Temperature"]

    @design_loop_exit_temperature.setter
    def design_loop_exit_temperature(self, value=None):
        """  Corresponds to IDD Field `design_loop_exit_temperature`

        Args:
            value (float): value for IDD Field `design_loop_exit_temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `design_loop_exit_temperature`'.format(value))

        self._data["Design Loop Exit Temperature"] = value

    @property
    def loop_design_temperature_difference(self):
        """Get loop_design_temperature_difference

        Returns:
            float: the value of `loop_design_temperature_difference` or None if not set
        """
        return self._data["Loop Design Temperature Difference"]

    @loop_design_temperature_difference.setter
    def loop_design_temperature_difference(self, value=None):
        """  Corresponds to IDD Field `loop_design_temperature_difference`

        Args:
            value (float): value for IDD Field `loop_design_temperature_difference`
                Units: deltaC
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
                                 'for field `loop_design_temperature_difference`'.format(value))
            if value <= 0.0:
                raise ValueError('value need to be greater 0.0 '
                                 'for field `loop_design_temperature_difference`')

        self._data["Loop Design Temperature Difference"] = value

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

class OutputControlSizingStyle(object):
    """ Corresponds to IDD object `OutputControl:Sizing:Style`
        default style for the Sizing output files is comma -- this works well for
        importing into spreadsheet programs such as Excel(tm) but not so well for word
        processing progams -- there tab may be a better choice.  fixed puts spaces between
        the "columns"
    
    """
    internal_name = "OutputControl:Sizing:Style"
    field_count = 1
    required_fields = ["Column Separator"]

    def __init__(self):
        """ Init data dictionary object for IDD  `OutputControl:Sizing:Style`
        """
        self._data = OrderedDict()
        self._data["Column Separator"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.column_separator = None
        else:
            self.column_separator = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def column_separator(self):
        """Get column_separator

        Returns:
            str: the value of `column_separator` or None if not set
        """
        return self._data["Column Separator"]

    @column_separator.setter
    def column_separator(self, value=None):
        """  Corresponds to IDD Field `column_separator`

        Args:
            value (str): value for IDD Field `column_separator`
                Accepted values are:
                      - Comma
                      - Tab
                      - Fixed
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `column_separator`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `column_separator`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `column_separator`')
            vals = {}
            vals["comma"] = "Comma"
            vals["tab"] = "Tab"
            vals["fixed"] = "Fixed"
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
                                     'field `column_separator`'.format(value))
            value = vals[value_lower]

        self._data["Column Separator"] = value

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

class ZoneControlHumidistat(object):
    """ Corresponds to IDD object `ZoneControl:Humidistat`
        Specifies zone relative humidity setpoint schedules for humidifying and dehumidifying.
    
    """
    internal_name = "ZoneControl:Humidistat"
    field_count = 4
    required_fields = ["Name", "Zone Name", "Humidifying Relative Humidity Setpoint Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Humidistat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Name"] = None
        self._data["Humidifying Relative Humidity Setpoint Schedule Name"] = None
        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = None
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
            self.zone_name = None
        else:
            self.zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.humidifying_relative_humidity_setpoint_schedule_name = None
        else:
            self.humidifying_relative_humidity_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = None
        else:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_name`')

        self._data["Zone Name"] = value

    @property
    def humidifying_relative_humidity_setpoint_schedule_name(self):
        """Get humidifying_relative_humidity_setpoint_schedule_name

        Returns:
            str: the value of `humidifying_relative_humidity_setpoint_schedule_name` or None if not set
        """
        return self._data["Humidifying Relative Humidity Setpoint Schedule Name"]

    @humidifying_relative_humidity_setpoint_schedule_name.setter
    def humidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `humidifying_relative_humidity_setpoint_schedule_name`
        hourly schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `humidifying_relative_humidity_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `humidifying_relative_humidity_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `humidifying_relative_humidity_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `humidifying_relative_humidity_setpoint_schedule_name`')

        self._data["Humidifying Relative Humidity Setpoint Schedule Name"] = value

    @property
    def dehumidifying_relative_humidity_setpoint_schedule_name(self):
        """Get dehumidifying_relative_humidity_setpoint_schedule_name

        Returns:
            str: the value of `dehumidifying_relative_humidity_setpoint_schedule_name` or None if not set
        """
        return self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"]

    @dehumidifying_relative_humidity_setpoint_schedule_name.setter
    def dehumidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `dehumidifying_relative_humidity_setpoint_schedule_name`
        hourly schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `dehumidifying_relative_humidity_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dehumidifying_relative_humidity_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dehumidifying_relative_humidity_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dehumidifying_relative_humidity_setpoint_schedule_name`')

        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = value

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

class ZoneControlThermostat(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat`
        Define the Thermostat settings for a zone or list of zones.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    
    """
    internal_name = "ZoneControl:Thermostat"
    field_count = 11
    required_fields = ["Name", "Zone or ZoneList Name", "Control Type Schedule Name", "Control 1 Object Type", "Control 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Control Type Schedule Name"] = None
        self._data["Control 1 Object Type"] = None
        self._data["Control 1 Name"] = None
        self._data["Control 2 Object Type"] = None
        self._data["Control 2 Name"] = None
        self._data["Control 3 Object Type"] = None
        self._data["Control 3 Name"] = None
        self._data["Control 4 Object Type"] = None
        self._data["Control 4 Name"] = None
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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_type_schedule_name = None
        else:
            self.control_type_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_1_object_type = None
        else:
            self.control_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_1_name = None
        else:
            self.control_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_2_object_type = None
        else:
            self.control_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_2_name = None
        else:
            self.control_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_3_object_type = None
        else:
            self.control_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_3_name = None
        else:
            self.control_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_4_object_type = None
        else:
            self.control_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.control_4_name = None
        else:
            self.control_4_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def control_type_schedule_name(self):
        """Get control_type_schedule_name

        Returns:
            str: the value of `control_type_schedule_name` or None if not set
        """
        return self._data["Control Type Schedule Name"]

    @control_type_schedule_name.setter
    def control_type_schedule_name(self, value=None):
        """  Corresponds to IDD Field `control_type_schedule_name`
        This schedule contains appropriate control types for thermostat.
        Control types are integers: 0 - Uncontrolled (floating, no thermostat), 1 = ThermostatSetpoint:SingleHeating,
        2 = ThermostatSetpoint:SingleCooling, 3 = ThermostatSetpoint:SingleHeatingOrCooling, 4 = ThermostatSetpoint:DualSetpoint

        Args:
            value (str): value for IDD Field `control_type_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_type_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_type_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_type_schedule_name`')

        self._data["Control Type Schedule Name"] = value

    @property
    def control_1_object_type(self):
        """Get control_1_object_type

        Returns:
            str: the value of `control_1_object_type` or None if not set
        """
        return self._data["Control 1 Object Type"]

    @control_1_object_type.setter
    def control_1_object_type(self, value=None):
        """  Corresponds to IDD Field `control_1_object_type`

        Args:
            value (str): value for IDD Field `control_1_object_type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_1_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `control_1_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Control 1 Object Type"] = value

    @property
    def control_1_name(self):
        """Get control_1_name

        Returns:
            str: the value of `control_1_name` or None if not set
        """
        return self._data["Control 1 Name"]

    @control_1_name.setter
    def control_1_name(self, value=None):
        """  Corresponds to IDD Field `control_1_name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `control_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_1_name`')

        self._data["Control 1 Name"] = value

    @property
    def control_2_object_type(self):
        """Get control_2_object_type

        Returns:
            str: the value of `control_2_object_type` or None if not set
        """
        return self._data["Control 2 Object Type"]

    @control_2_object_type.setter
    def control_2_object_type(self, value=None):
        """  Corresponds to IDD Field `control_2_object_type`

        Args:
            value (str): value for IDD Field `control_2_object_type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_2_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `control_2_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Control 2 Object Type"] = value

    @property
    def control_2_name(self):
        """Get control_2_name

        Returns:
            str: the value of `control_2_name` or None if not set
        """
        return self._data["Control 2 Name"]

    @control_2_name.setter
    def control_2_name(self, value=None):
        """  Corresponds to IDD Field `control_2_name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `control_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_2_name`')

        self._data["Control 2 Name"] = value

    @property
    def control_3_object_type(self):
        """Get control_3_object_type

        Returns:
            str: the value of `control_3_object_type` or None if not set
        """
        return self._data["Control 3 Object Type"]

    @control_3_object_type.setter
    def control_3_object_type(self, value=None):
        """  Corresponds to IDD Field `control_3_object_type`

        Args:
            value (str): value for IDD Field `control_3_object_type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_3_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `control_3_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Control 3 Object Type"] = value

    @property
    def control_3_name(self):
        """Get control_3_name

        Returns:
            str: the value of `control_3_name` or None if not set
        """
        return self._data["Control 3 Name"]

    @control_3_name.setter
    def control_3_name(self, value=None):
        """  Corresponds to IDD Field `control_3_name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `control_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_3_name`')

        self._data["Control 3 Name"] = value

    @property
    def control_4_object_type(self):
        """Get control_4_object_type

        Returns:
            str: the value of `control_4_object_type` or None if not set
        """
        return self._data["Control 4 Object Type"]

    @control_4_object_type.setter
    def control_4_object_type(self, value=None):
        """  Corresponds to IDD Field `control_4_object_type`

        Args:
            value (str): value for IDD Field `control_4_object_type`
                Accepted values are:
                      - ThermostatSetpoint:SingleHeating
                      - ThermostatSetpoint:SingleCooling
                      - ThermostatSetpoint:SingleHeatingOrCooling
                      - ThermostatSetpoint:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_4_object_type`')
            vals = {}
            vals["thermostatsetpoint:singleheating"] = "ThermostatSetpoint:SingleHeating"
            vals["thermostatsetpoint:singlecooling"] = "ThermostatSetpoint:SingleCooling"
            vals["thermostatsetpoint:singleheatingorcooling"] = "ThermostatSetpoint:SingleHeatingOrCooling"
            vals["thermostatsetpoint:dualsetpoint"] = "ThermostatSetpoint:DualSetpoint"
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
                                     'field `control_4_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Control 4 Object Type"] = value

    @property
    def control_4_name(self):
        """Get control_4_name

        Returns:
            str: the value of `control_4_name` or None if not set
        """
        return self._data["Control 4 Name"]

    @control_4_name.setter
    def control_4_name(self, value=None):
        """  Corresponds to IDD Field `control_4_name`
        Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating)
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `control_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `control_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `control_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `control_4_name`')

        self._data["Control 4 Name"] = value

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

class ZoneControlThermostatOperativeTemperature(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:OperativeTemperature`
        This object can be used with the ZoneList option on a thermostat or with one
        of the zones on that list (but you won't be able to use the object list to
        pick only one of those zones.  Thermostat names are <Zone Name> <global Thermostat name> internally.
    
    """
    internal_name = "ZoneControl:Thermostat:OperativeTemperature"
    field_count = 4
    required_fields = ["Thermostat Name", "Radiative Fraction Input Mode"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:OperativeTemperature`
        """
        self._data = OrderedDict()
        self._data["Thermostat Name"] = None
        self._data["Radiative Fraction Input Mode"] = None
        self._data["Fixed Radiative Fraction"] = None
        self._data["Radiative Fraction Schedule Name"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.thermostat_name = None
        else:
            self.thermostat_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.radiative_fraction_input_mode = None
        else:
            self.radiative_fraction_input_mode = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fixed_radiative_fraction = None
        else:
            self.fixed_radiative_fraction = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.radiative_fraction_schedule_name = None
        else:
            self.radiative_fraction_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def thermostat_name(self):
        """Get thermostat_name

        Returns:
            str: the value of `thermostat_name` or None if not set
        """
        return self._data["Thermostat Name"]

    @thermostat_name.setter
    def thermostat_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_name`
        Enter the name of a ZoneControl:Thermostat object.
        This object modifies a ZoneControl:Thermostat object to add a
        radiative fraction.

        Args:
            value (str): value for IDD Field `thermostat_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermostat_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_name`')

        self._data["Thermostat Name"] = value

    @property
    def radiative_fraction_input_mode(self):
        """Get radiative_fraction_input_mode

        Returns:
            str: the value of `radiative_fraction_input_mode` or None if not set
        """
        return self._data["Radiative Fraction Input Mode"]

    @radiative_fraction_input_mode.setter
    def radiative_fraction_input_mode(self, value=None):
        """  Corresponds to IDD Field `radiative_fraction_input_mode`

        Args:
            value (str): value for IDD Field `radiative_fraction_input_mode`
                Accepted values are:
                      - Constant
                      - Scheduled
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `radiative_fraction_input_mode`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `radiative_fraction_input_mode`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `radiative_fraction_input_mode`')
            vals = {}
            vals["constant"] = "Constant"
            vals["scheduled"] = "Scheduled"
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
                                     'field `radiative_fraction_input_mode`'.format(value))
            value = vals[value_lower]

        self._data["Radiative Fraction Input Mode"] = value

    @property
    def fixed_radiative_fraction(self):
        """Get fixed_radiative_fraction

        Returns:
            float: the value of `fixed_radiative_fraction` or None if not set
        """
        return self._data["Fixed Radiative Fraction"]

    @fixed_radiative_fraction.setter
    def fixed_radiative_fraction(self, value=None):
        """  Corresponds to IDD Field `fixed_radiative_fraction`

        Args:
            value (float): value for IDD Field `fixed_radiative_fraction`
                value >= 0.0
                value < 0.9
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `fixed_radiative_fraction`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `fixed_radiative_fraction`')
            if value >= 0.9:
                raise ValueError('value need to be smaller 0.9 '
                                 'for field `fixed_radiative_fraction`')

        self._data["Fixed Radiative Fraction"] = value

    @property
    def radiative_fraction_schedule_name(self):
        """Get radiative_fraction_schedule_name

        Returns:
            str: the value of `radiative_fraction_schedule_name` or None if not set
        """
        return self._data["Radiative Fraction Schedule Name"]

    @radiative_fraction_schedule_name.setter
    def radiative_fraction_schedule_name(self, value=None):
        """  Corresponds to IDD Field `radiative_fraction_schedule_name`
        Schedule values of 0.0 indicate no operative temperature control

        Args:
            value (str): value for IDD Field `radiative_fraction_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `radiative_fraction_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `radiative_fraction_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `radiative_fraction_schedule_name`')

        self._data["Radiative Fraction Schedule Name"] = value

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

class ZoneControlThermostatThermalComfort(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:ThermalComfort`
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    
    """
    internal_name = "ZoneControl:Thermostat:ThermalComfort"
    field_count = 15
    required_fields = ["Name", "Zone or ZoneList Name", "Minimum Dry-Bulb Temperature Setpoint", "Maximum Dry-Bulb Temperature Setpoint", "Thermal Comfort Control Type Schedule Name", "Thermal Comfort Control 1 Object Type", "Thermal Comfort Control 1 Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:ThermalComfort`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Averaging Method"] = None
        self._data["Specific People Name"] = None
        self._data["Minimum Dry-Bulb Temperature Setpoint"] = None
        self._data["Maximum Dry-Bulb Temperature Setpoint"] = None
        self._data["Thermal Comfort Control Type Schedule Name"] = None
        self._data["Thermal Comfort Control 1 Object Type"] = None
        self._data["Thermal Comfort Control 1 Name"] = None
        self._data["Thermal Comfort Control 2 Object Type"] = None
        self._data["Thermal Comfort Control 2 Name"] = None
        self._data["Thermal Comfort Control 3 Object Type"] = None
        self._data["Thermal Comfort Control 3 Name"] = None
        self._data["Thermal Comfort Control 4 Object Type"] = None
        self._data["Thermal Comfort Control 4 Name"] = None
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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.averaging_method = None
        else:
            self.averaging_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.specific_people_name = None
        else:
            self.specific_people_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_drybulb_temperature_setpoint = None
        else:
            self.minimum_drybulb_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.maximum_drybulb_temperature_setpoint = None
        else:
            self.maximum_drybulb_temperature_setpoint = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_type_schedule_name = None
        else:
            self.thermal_comfort_control_type_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_1_object_type = None
        else:
            self.thermal_comfort_control_1_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_1_name = None
        else:
            self.thermal_comfort_control_1_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_2_object_type = None
        else:
            self.thermal_comfort_control_2_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_2_name = None
        else:
            self.thermal_comfort_control_2_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_3_object_type = None
        else:
            self.thermal_comfort_control_3_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_3_name = None
        else:
            self.thermal_comfort_control_3_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_4_object_type = None
        else:
            self.thermal_comfort_control_4_object_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.thermal_comfort_control_4_name = None
        else:
            self.thermal_comfort_control_4_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def averaging_method(self):
        """Get averaging_method

        Returns:
            str: the value of `averaging_method` or None if not set
        """
        return self._data["Averaging Method"]

    @averaging_method.setter
    def averaging_method(self, value="PeopleAverage"):
        """  Corresponds to IDD Field `averaging_method`
        The method used to calculate thermal comfort dry-bulb temperature setpoint
        for multiple people objects in a zone

        Args:
            value (str): value for IDD Field `averaging_method`
                Accepted values are:
                      - SpecificObject
                      - ObjectAverage
                      - PeopleAverage
                Default value: PeopleAverage
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `averaging_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `averaging_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `averaging_method`')
            vals = {}
            vals["specificobject"] = "SpecificObject"
            vals["objectaverage"] = "ObjectAverage"
            vals["peopleaverage"] = "PeopleAverage"
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
                                     'field `averaging_method`'.format(value))
            value = vals[value_lower]

        self._data["Averaging Method"] = value

    @property
    def specific_people_name(self):
        """Get specific_people_name

        Returns:
            str: the value of `specific_people_name` or None if not set
        """
        return self._data["Specific People Name"]

    @specific_people_name.setter
    def specific_people_name(self, value=None):
        """  Corresponds to IDD Field `specific_people_name`
        Used only when Averaging Method = SpecificObject in the previous field.

        Args:
            value (str): value for IDD Field `specific_people_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `specific_people_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `specific_people_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `specific_people_name`')

        self._data["Specific People Name"] = value

    @property
    def minimum_drybulb_temperature_setpoint(self):
        """Get minimum_drybulb_temperature_setpoint

        Returns:
            float: the value of `minimum_drybulb_temperature_setpoint` or None if not set
        """
        return self._data["Minimum Dry-Bulb Temperature Setpoint"]

    @minimum_drybulb_temperature_setpoint.setter
    def minimum_drybulb_temperature_setpoint(self, value=0.0 ):
        """  Corresponds to IDD Field `minimum_drybulb_temperature_setpoint`

        Args:
            value (float): value for IDD Field `minimum_drybulb_temperature_setpoint`
                Units: C
                Default value: 0.0
                value >= 0.0
                value <= 50.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `minimum_drybulb_temperature_setpoint`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `minimum_drybulb_temperature_setpoint`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `minimum_drybulb_temperature_setpoint`')

        self._data["Minimum Dry-Bulb Temperature Setpoint"] = value

    @property
    def maximum_drybulb_temperature_setpoint(self):
        """Get maximum_drybulb_temperature_setpoint

        Returns:
            float: the value of `maximum_drybulb_temperature_setpoint` or None if not set
        """
        return self._data["Maximum Dry-Bulb Temperature Setpoint"]

    @maximum_drybulb_temperature_setpoint.setter
    def maximum_drybulb_temperature_setpoint(self, value=50.0 ):
        """  Corresponds to IDD Field `maximum_drybulb_temperature_setpoint`

        Args:
            value (float): value for IDD Field `maximum_drybulb_temperature_setpoint`
                Units: C
                Default value: 50.0
                value >= 0.0
                value <= 50.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `maximum_drybulb_temperature_setpoint`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `maximum_drybulb_temperature_setpoint`')
            if value > 50.0:
                raise ValueError('value need to be smaller 50.0 '
                                 'for field `maximum_drybulb_temperature_setpoint`')

        self._data["Maximum Dry-Bulb Temperature Setpoint"] = value

    @property
    def thermal_comfort_control_type_schedule_name(self):
        """Get thermal_comfort_control_type_schedule_name

        Returns:
            str: the value of `thermal_comfort_control_type_schedule_name` or None if not set
        """
        return self._data["Thermal Comfort Control Type Schedule Name"]

    @thermal_comfort_control_type_schedule_name.setter
    def thermal_comfort_control_type_schedule_name(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_type_schedule_name`
        The Thermal Comfort Control Type Schedule contains values that are appropriate control types.
        Thermal Comfort Control types are integers: 0 - Uncontrolled (floating),
        1 = ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
        2 = ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
        3 = ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
        4 = ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint

        Args:
            value (str): value for IDD Field `thermal_comfort_control_type_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_type_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_type_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_type_schedule_name`')

        self._data["Thermal Comfort Control Type Schedule Name"] = value

    @property
    def thermal_comfort_control_1_object_type(self):
        """Get thermal_comfort_control_1_object_type

        Returns:
            str: the value of `thermal_comfort_control_1_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 1 Object Type"]

    @thermal_comfort_control_1_object_type.setter
    def thermal_comfort_control_1_object_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_1_object_type`

        Args:
            value (str): value for IDD Field `thermal_comfort_control_1_object_type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_1_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_1_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_1_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `thermal_comfort_control_1_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Thermal Comfort Control 1 Object Type"] = value

    @property
    def thermal_comfort_control_1_name(self):
        """Get thermal_comfort_control_1_name

        Returns:
            str: the value of `thermal_comfort_control_1_name` or None if not set
        """
        return self._data["Thermal Comfort Control 1 Name"]

    @thermal_comfort_control_1_name.setter
    def thermal_comfort_control_1_name(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_1_name`
        Control type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `thermal_comfort_control_1_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_1_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_1_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_1_name`')

        self._data["Thermal Comfort Control 1 Name"] = value

    @property
    def thermal_comfort_control_2_object_type(self):
        """Get thermal_comfort_control_2_object_type

        Returns:
            str: the value of `thermal_comfort_control_2_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 2 Object Type"]

    @thermal_comfort_control_2_object_type.setter
    def thermal_comfort_control_2_object_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_2_object_type`

        Args:
            value (str): value for IDD Field `thermal_comfort_control_2_object_type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_2_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_2_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_2_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `thermal_comfort_control_2_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Thermal Comfort Control 2 Object Type"] = value

    @property
    def thermal_comfort_control_2_name(self):
        """Get thermal_comfort_control_2_name

        Returns:
            str: the value of `thermal_comfort_control_2_name` or None if not set
        """
        return self._data["Thermal Comfort Control 2 Name"]

    @thermal_comfort_control_2_name.setter
    def thermal_comfort_control_2_name(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_2_name`
        Control Type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `thermal_comfort_control_2_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_2_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_2_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_2_name`')

        self._data["Thermal Comfort Control 2 Name"] = value

    @property
    def thermal_comfort_control_3_object_type(self):
        """Get thermal_comfort_control_3_object_type

        Returns:
            str: the value of `thermal_comfort_control_3_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 3 Object Type"]

    @thermal_comfort_control_3_object_type.setter
    def thermal_comfort_control_3_object_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_3_object_type`

        Args:
            value (str): value for IDD Field `thermal_comfort_control_3_object_type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_3_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_3_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_3_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `thermal_comfort_control_3_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Thermal Comfort Control 3 Object Type"] = value

    @property
    def thermal_comfort_control_3_name(self):
        """Get thermal_comfort_control_3_name

        Returns:
            str: the value of `thermal_comfort_control_3_name` or None if not set
        """
        return self._data["Thermal Comfort Control 3 Name"]

    @thermal_comfort_control_3_name.setter
    def thermal_comfort_control_3_name(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_3_name`
        Control type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `thermal_comfort_control_3_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_3_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_3_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_3_name`')

        self._data["Thermal Comfort Control 3 Name"] = value

    @property
    def thermal_comfort_control_4_object_type(self):
        """Get thermal_comfort_control_4_object_type

        Returns:
            str: the value of `thermal_comfort_control_4_object_type` or None if not set
        """
        return self._data["Thermal Comfort Control 4 Object Type"]

    @thermal_comfort_control_4_object_type.setter
    def thermal_comfort_control_4_object_type(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_4_object_type`

        Args:
            value (str): value for IDD Field `thermal_comfort_control_4_object_type`
                Accepted values are:
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling
                      - ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_4_object_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_4_object_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_4_object_type`')
            vals = {}
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheating"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
            vals["thermostatsetpoint:thermalcomfort:fanger:singlecooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:singleheatingorcooling"] = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
            vals["thermostatsetpoint:thermalcomfort:fanger:dualsetpoint"] = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
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
                                     'field `thermal_comfort_control_4_object_type`'.format(value))
            value = vals[value_lower]

        self._data["Thermal Comfort Control 4 Object Type"] = value

    @property
    def thermal_comfort_control_4_name(self):
        """Get thermal_comfort_control_4_name

        Returns:
            str: the value of `thermal_comfort_control_4_name` or None if not set
        """
        return self._data["Thermal Comfort Control 4 Name"]

    @thermal_comfort_control_4_name.setter
    def thermal_comfort_control_4_name(self, value=None):
        """  Corresponds to IDD Field `thermal_comfort_control_4_name`
        Control type names are names for individual control type objects.
        Schedule values in these objects list actual setpoint temperatures for the control types

        Args:
            value (str): value for IDD Field `thermal_comfort_control_4_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermal_comfort_control_4_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermal_comfort_control_4_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermal_comfort_control_4_name`')

        self._data["Thermal Comfort Control 4 Name"] = value

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

class ZoneControlThermostatTemperatureAndHumidity(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:TemperatureAndHumidity`
        This object modifies a ZoneControl:Thermostat object to effect temperature control based on
        zone air humidity conditions.
    
    """
    internal_name = "ZoneControl:Thermostat:TemperatureAndHumidity"
    field_count = 7
    required_fields = ["Thermostat Name", "Dehumidifying Relative Humidity Setpoint Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:TemperatureAndHumidity`
        """
        self._data = OrderedDict()
        self._data["Thermostat Name"] = None
        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = None
        self._data["Dehumidification Control Type"] = None
        self._data["Overcool Range Input Method"] = None
        self._data["Overcool Constant Range"] = None
        self._data["Overcool Range Schedule Name"] = None
        self._data["Overcool Control Ratio"] = None
        self.accept_substring = False

    def read(self, vals, accept_substring=True):
        """ Read values

        Args:
            vals (list): list of strings representing values
        """
        self.accept_substring = accept_substring
        i = 0
        if len(vals[i]) == 0:
            self.thermostat_name = None
        else:
            self.thermostat_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = None
        else:
            self.dehumidifying_relative_humidity_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.dehumidification_control_type = None
        else:
            self.dehumidification_control_type = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_range_input_method = None
        else:
            self.overcool_range_input_method = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_constant_range = None
        else:
            self.overcool_constant_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_range_schedule_name = None
        else:
            self.overcool_range_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.overcool_control_ratio = None
        else:
            self.overcool_control_ratio = vals[i]
        i += 1
        if i >= len(vals):
            return

    @property
    def thermostat_name(self):
        """Get thermostat_name

        Returns:
            str: the value of `thermostat_name` or None if not set
        """
        return self._data["Thermostat Name"]

    @thermostat_name.setter
    def thermostat_name(self, value=None):
        """  Corresponds to IDD Field `thermostat_name`
        Enter the name of a ZoneControl:Thermostat object whose operation is to be modified to
        effect temperature control based on zone air humidity conditions. If the ZoneControl:
        Thermostat object references a ZoneList, simply enter the name of the ZoneControl:Thermostat
        object and this temperature and humidity thermostat control will be applied to all zones
        in the ZoneList. If the ZoneControl:Thermostat object references a ZoneList but it is
        desired that only a single zone within the ZoneList be controlled based on temperature and
        humidity control, then the name to be put here is <Zone Name> <Thermostat Name> where the
        Thermostat Name is the the name of the ZoneControl:Thermostat object.

        Args:
            value (str): value for IDD Field `thermostat_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `thermostat_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `thermostat_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `thermostat_name`')

        self._data["Thermostat Name"] = value

    @property
    def dehumidifying_relative_humidity_setpoint_schedule_name(self):
        """Get dehumidifying_relative_humidity_setpoint_schedule_name

        Returns:
            str: the value of `dehumidifying_relative_humidity_setpoint_schedule_name` or None if not set
        """
        return self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"]

    @dehumidifying_relative_humidity_setpoint_schedule_name.setter
    def dehumidifying_relative_humidity_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `dehumidifying_relative_humidity_setpoint_schedule_name`
        Schedule values should be in Relative Humidity (percent)

        Args:
            value (str): value for IDD Field `dehumidifying_relative_humidity_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dehumidifying_relative_humidity_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dehumidifying_relative_humidity_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dehumidifying_relative_humidity_setpoint_schedule_name`')

        self._data["Dehumidifying Relative Humidity Setpoint Schedule Name"] = value

    @property
    def dehumidification_control_type(self):
        """Get dehumidification_control_type

        Returns:
            str: the value of `dehumidification_control_type` or None if not set
        """
        return self._data["Dehumidification Control Type"]

    @dehumidification_control_type.setter
    def dehumidification_control_type(self, value="Overcool"):
        """  Corresponds to IDD Field `dehumidification_control_type`

        Args:
            value (str): value for IDD Field `dehumidification_control_type`
                Accepted values are:
                      - Overcool
                      - None
                Default value: Overcool
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `dehumidification_control_type`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `dehumidification_control_type`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `dehumidification_control_type`')
            vals = {}
            vals["overcool"] = "Overcool"
            vals["none"] = "None"
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
                                     'field `dehumidification_control_type`'.format(value))
            value = vals[value_lower]

        self._data["Dehumidification Control Type"] = value

    @property
    def overcool_range_input_method(self):
        """Get overcool_range_input_method

        Returns:
            str: the value of `overcool_range_input_method` or None if not set
        """
        return self._data["Overcool Range Input Method"]

    @overcool_range_input_method.setter
    def overcool_range_input_method(self, value="Constant"):
        """  Corresponds to IDD Field `overcool_range_input_method`

        Args:
            value (str): value for IDD Field `overcool_range_input_method`
                Accepted values are:
                      - Constant
                      - Scheduled
                Default value: Constant
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `overcool_range_input_method`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `overcool_range_input_method`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `overcool_range_input_method`')
            vals = {}
            vals["constant"] = "Constant"
            vals["scheduled"] = "Scheduled"
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
                                     'field `overcool_range_input_method`'.format(value))
            value = vals[value_lower]

        self._data["Overcool Range Input Method"] = value

    @property
    def overcool_constant_range(self):
        """Get overcool_constant_range

        Returns:
            float: the value of `overcool_constant_range` or None if not set
        """
        return self._data["Overcool Constant Range"]

    @overcool_constant_range.setter
    def overcool_constant_range(self, value=1.7 ):
        """  Corresponds to IDD Field `overcool_constant_range`
        Maximum Overcool temperature range for cooling setpoint reduction.
        Used with Dehumidification Control Type = Overcool.
        A value of 0.0 indicates no zone temperature overcooling will be provided to
        gain additional dehumidification.

        Args:
            value (float): value for IDD Field `overcool_constant_range`
                Units: deltaC
                Default value: 1.7
                value >= 0.0
                value <= 3.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `overcool_constant_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `overcool_constant_range`')
            if value > 3.0:
                raise ValueError('value need to be smaller 3.0 '
                                 'for field `overcool_constant_range`')

        self._data["Overcool Constant Range"] = value

    @property
    def overcool_range_schedule_name(self):
        """Get overcool_range_schedule_name

        Returns:
            str: the value of `overcool_range_schedule_name` or None if not set
        """
        return self._data["Overcool Range Schedule Name"]

    @overcool_range_schedule_name.setter
    def overcool_range_schedule_name(self, value=None):
        """  Corresponds to IDD Field `overcool_range_schedule_name`
        Schedule values of 0.0 indicates no zone temperature overcooling will be
        provided to gain additional dehumidification.
        Schedule values should be >= 0 and <= 3 (deltaC).

        Args:
            value (str): value for IDD Field `overcool_range_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `overcool_range_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `overcool_range_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `overcool_range_schedule_name`')

        self._data["Overcool Range Schedule Name"] = value

    @property
    def overcool_control_ratio(self):
        """Get overcool_control_ratio

        Returns:
            float: the value of `overcool_control_ratio` or None if not set
        """
        return self._data["Overcool Control Ratio"]

    @overcool_control_ratio.setter
    def overcool_control_ratio(self, value=3.6 ):
        """  Corresponds to IDD Field `overcool_control_ratio`
        The value of this input field is used to adjust the cooling setpoint temperature
        (established by the associated ZoneControl:Thermostat object) downward based on the
        difference between the zone air relative humidity level and the dehumidifying
        relative humidity setpoint.

        Args:
            value (float): value for IDD Field `overcool_control_ratio`
                Units: percent/K
                Default value: 3.6
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
                                 'for field `overcool_control_ratio`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `overcool_control_ratio`')

        self._data["Overcool Control Ratio"] = value

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

class ThermostatSetpointSingleHeating(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeating`
        Used for a heating only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only heating is allowed with this control type.
    
    """
    internal_name = "ThermostatSetpoint:SingleHeating"
    field_count = 2
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:SingleHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
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
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

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

class ThermostatSetpointSingleCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleCooling`
        Used for a cooling only thermostat. The setpoint can be scheduled and varied throughout
        the simulation but only cooling is allowed.
    
    """
    internal_name = "ThermostatSetpoint:SingleCooling"
    field_count = 2
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:SingleCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
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
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

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

class ThermostatSetpointSingleHeatingOrCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:SingleHeatingOrCooling`
        Used for a heating and cooling thermostat with a single setpoint. The setpoint can be
        scheduled and varied throughout the simulation for both heating and cooling.
    
    """
    internal_name = "ThermostatSetpoint:SingleHeatingOrCooling"
    field_count = 2
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:SingleHeatingOrCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Setpoint Temperature Schedule Name"] = None
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
            self.setpoint_temperature_schedule_name = None
        else:
            self.setpoint_temperature_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def setpoint_temperature_schedule_name(self):
        """Get setpoint_temperature_schedule_name

        Returns:
            str: the value of `setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Setpoint Temperature Schedule Name"]

    @setpoint_temperature_schedule_name.setter
    def setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `setpoint_temperature_schedule_name`')

        self._data["Setpoint Temperature Schedule Name"] = value

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

class ThermostatSetpointDualSetpoint(object):
    """ Corresponds to IDD object `ThermostatSetpoint:DualSetpoint`
        Used for a heating and cooling thermostat with dual setpoints. The setpoints can be
        scheduled and varied throughout the simulation for both heating and cooling.
    
    """
    internal_name = "ThermostatSetpoint:DualSetpoint"
    field_count = 3
    required_fields = ["Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Heating Setpoint Temperature Schedule Name"] = None
        self._data["Cooling Setpoint Temperature Schedule Name"] = None
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
            self.heating_setpoint_temperature_schedule_name = None
        else:
            self.heating_setpoint_temperature_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_setpoint_temperature_schedule_name = None
        else:
            self.cooling_setpoint_temperature_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def heating_setpoint_temperature_schedule_name(self):
        """Get heating_setpoint_temperature_schedule_name

        Returns:
            str: the value of `heating_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Heating Setpoint Temperature Schedule Name"]

    @heating_setpoint_temperature_schedule_name.setter
    def heating_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heating_setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `heating_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_setpoint_temperature_schedule_name`')

        self._data["Heating Setpoint Temperature Schedule Name"] = value

    @property
    def cooling_setpoint_temperature_schedule_name(self):
        """Get cooling_setpoint_temperature_schedule_name

        Returns:
            str: the value of `cooling_setpoint_temperature_schedule_name` or None if not set
        """
        return self._data["Cooling Setpoint Temperature Schedule Name"]

    @cooling_setpoint_temperature_schedule_name.setter
    def cooling_setpoint_temperature_schedule_name(self, value=None):
        """  Corresponds to IDD Field `cooling_setpoint_temperature_schedule_name`

        Args:
            value (str): value for IDD Field `cooling_setpoint_temperature_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_setpoint_temperature_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_setpoint_temperature_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_setpoint_temperature_schedule_name`')

        self._data["Cooling Setpoint Temperature Schedule Name"] = value

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

class ThermostatSetpointThermalComfortFangerSingleHeating(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        Used for heating only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only heating is allowed with this control type.
    
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating"
    field_count = 2
    required_fields = ["Name", "Fanger Thermal Comfort Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None
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
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_schedule_name(self):
        """Get fanger_thermal_comfort_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fanger_thermal_comfort_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fanger_thermal_comfort_schedule_name`')

        self._data["Fanger Thermal Comfort Schedule Name"] = value

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

class ThermostatSetpointThermalComfortFangerSingleCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        Used for cooling only thermal comfort control. The PMV setpoint can be scheduled and
        varied throughout the simulation but only cooling is allowed with this control type.
    
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling"
    field_count = 2
    required_fields = ["Name", "Fanger Thermal Comfort Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None
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
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_schedule_name(self):
        """Get fanger_thermal_comfort_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fanger_thermal_comfort_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fanger_thermal_comfort_schedule_name`')

        self._data["Fanger Thermal Comfort Schedule Name"] = value

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

class ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        Used for heating and cooling thermal comfort control with a single setpoint. The PMV
        setpoint can be scheduled and varied throughout the simulation for both heating and
        cooling.
    
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling"
    field_count = 2
    required_fields = ["Name", "Fanger Thermal Comfort Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Schedule Name"] = None
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
            self.fanger_thermal_comfort_schedule_name = None
        else:
            self.fanger_thermal_comfort_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_schedule_name(self):
        """Get fanger_thermal_comfort_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Schedule Name"]

    @fanger_thermal_comfort_schedule_name.setter
    def fanger_thermal_comfort_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fanger_thermal_comfort_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fanger_thermal_comfort_schedule_name`')

        self._data["Fanger Thermal Comfort Schedule Name"] = value

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

class ThermostatSetpointThermalComfortFangerDualSetpoint(object):
    """ Corresponds to IDD object `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        Used for heating and cooling thermal comfort control with dual setpoints. The PMV
        setpoints can be scheduled and varied throughout the simulation for both heating and
        cooling.
    
    """
    internal_name = "ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint"
    field_count = 3
    required_fields = ["Name", "Fanger Thermal Comfort Heating Schedule Name", "Fanger Thermal Comfort Cooling Schedule Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Fanger Thermal Comfort Heating Schedule Name"] = None
        self._data["Fanger Thermal Comfort Cooling Schedule Name"] = None
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
            self.fanger_thermal_comfort_heating_schedule_name = None
        else:
            self.fanger_thermal_comfort_heating_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.fanger_thermal_comfort_cooling_schedule_name = None
        else:
            self.fanger_thermal_comfort_cooling_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def fanger_thermal_comfort_heating_schedule_name(self):
        """Get fanger_thermal_comfort_heating_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_heating_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Heating Schedule Name"]

    @fanger_thermal_comfort_heating_schedule_name.setter
    def fanger_thermal_comfort_heating_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fanger_thermal_comfort_heating_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_heating_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_heating_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_heating_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fanger_thermal_comfort_heating_schedule_name`')

        self._data["Fanger Thermal Comfort Heating Schedule Name"] = value

    @property
    def fanger_thermal_comfort_cooling_schedule_name(self):
        """Get fanger_thermal_comfort_cooling_schedule_name

        Returns:
            str: the value of `fanger_thermal_comfort_cooling_schedule_name` or None if not set
        """
        return self._data["Fanger Thermal Comfort Cooling Schedule Name"]

    @fanger_thermal_comfort_cooling_schedule_name.setter
    def fanger_thermal_comfort_cooling_schedule_name(self, value=None):
        """  Corresponds to IDD Field `fanger_thermal_comfort_cooling_schedule_name`
        Schedule values should be Predicted Mean Vote (PMV)

        Args:
            value (str): value for IDD Field `fanger_thermal_comfort_cooling_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `fanger_thermal_comfort_cooling_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `fanger_thermal_comfort_cooling_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `fanger_thermal_comfort_cooling_schedule_name`')

        self._data["Fanger Thermal Comfort Cooling Schedule Name"] = value

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

class ZoneControlThermostatStagedDualSetpoint(object):
    """ Corresponds to IDD object `ZoneControl:Thermostat:StagedDualSetpoint`
        Define the Thermostat StagedDualSetpoint settings for a zone or list of zones.
        If you use a ZoneList in the Zone or ZoneList name field then this definition applies
        to all the zones in the ZoneList.
    
    """
    internal_name = "ZoneControl:Thermostat:StagedDualSetpoint"
    field_count = 16
    required_fields = ["Name", "Zone or ZoneList Name", "Number of Heating Stages", "Stage 1 Heating Temperature Offset", "Number of Cooling Stages", "Stage 1 Cooling Temperature Offset"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:Thermostat:StagedDualSetpoint`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone or ZoneList Name"] = None
        self._data["Number of Heating Stages"] = None
        self._data["Heating Temperature Setpoint Schedule Name"] = None
        self._data["Heating Throttling Temperature Range"] = None
        self._data["Stage 1 Heating Temperature Offset"] = None
        self._data["Stage 2 Heating Temperature Offset"] = None
        self._data["Stage 3 Heating Temperature Offset"] = None
        self._data["Stage 4 Heating Temperature Offset"] = None
        self._data["Number of Cooling Stages"] = None
        self._data["Cooling Temperature Setpoint Base Schedule Name"] = None
        self._data["Cooling Throttling Temperature Range"] = None
        self._data["Stage 1 Cooling Temperature Offset"] = None
        self._data["Stage 2 Cooling Temperature Offset"] = None
        self._data["Stage 3 Cooling Temperature Offset"] = None
        self._data["Stage 4 Cooling Temperature Offset"] = None
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
            self.zone_or_zonelist_name = None
        else:
            self.zone_or_zonelist_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_heating_stages = None
        else:
            self.number_of_heating_stages = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_temperature_setpoint_schedule_name = None
        else:
            self.heating_temperature_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.heating_throttling_temperature_range = None
        else:
            self.heating_throttling_temperature_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_1_heating_temperature_offset = None
        else:
            self.stage_1_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_2_heating_temperature_offset = None
        else:
            self.stage_2_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_3_heating_temperature_offset = None
        else:
            self.stage_3_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_4_heating_temperature_offset = None
        else:
            self.stage_4_heating_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.number_of_cooling_stages = None
        else:
            self.number_of_cooling_stages = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_temperature_setpoint_base_schedule_name = None
        else:
            self.cooling_temperature_setpoint_base_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.cooling_throttling_temperature_range = None
        else:
            self.cooling_throttling_temperature_range = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_1_cooling_temperature_offset = None
        else:
            self.stage_1_cooling_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_2_cooling_temperature_offset = None
        else:
            self.stage_2_cooling_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_3_cooling_temperature_offset = None
        else:
            self.stage_3_cooling_temperature_offset = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.stage_4_cooling_temperature_offset = None
        else:
            self.stage_4_cooling_temperature_offset = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def zone_or_zonelist_name(self):
        """Get zone_or_zonelist_name

        Returns:
            str: the value of `zone_or_zonelist_name` or None if not set
        """
        return self._data["Zone or ZoneList Name"]

    @zone_or_zonelist_name.setter
    def zone_or_zonelist_name(self, value=None):
        """  Corresponds to IDD Field `zone_or_zonelist_name`

        Args:
            value (str): value for IDD Field `zone_or_zonelist_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `zone_or_zonelist_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `zone_or_zonelist_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `zone_or_zonelist_name`')

        self._data["Zone or ZoneList Name"] = value

    @property
    def number_of_heating_stages(self):
        """Get number_of_heating_stages

        Returns:
            int: the value of `number_of_heating_stages` or None if not set
        """
        return self._data["Number of Heating Stages"]

    @number_of_heating_stages.setter
    def number_of_heating_stages(self, value=None):
        """  Corresponds to IDD Field `number_of_heating_stages`
        Enter the number of the following sets of data for heating temperature offset

        Args:
            value (int): value for IDD Field `number_of_heating_stages`
                value >= 1
                value <= 4
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
                                 'for field `number_of_heating_stages`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_heating_stages`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_heating_stages`')

        self._data["Number of Heating Stages"] = value

    @property
    def heating_temperature_setpoint_schedule_name(self):
        """Get heating_temperature_setpoint_schedule_name

        Returns:
            str: the value of `heating_temperature_setpoint_schedule_name` or None if not set
        """
        return self._data["Heating Temperature Setpoint Schedule Name"]

    @heating_temperature_setpoint_schedule_name.setter
    def heating_temperature_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `heating_temperature_setpoint_schedule_name`

        Args:
            value (str): value for IDD Field `heating_temperature_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `heating_temperature_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `heating_temperature_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `heating_temperature_setpoint_schedule_name`')

        self._data["Heating Temperature Setpoint Schedule Name"] = value

    @property
    def heating_throttling_temperature_range(self):
        """Get heating_throttling_temperature_range

        Returns:
            float: the value of `heating_throttling_temperature_range` or None if not set
        """
        return self._data["Heating Throttling Temperature Range"]

    @heating_throttling_temperature_range.setter
    def heating_throttling_temperature_range(self, value=1.1 ):
        """  Corresponds to IDD Field `heating_throttling_temperature_range`

        Args:
            value (float): value for IDD Field `heating_throttling_temperature_range`
                Units: deltaC
                Default value: 1.1
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
                                 'for field `heating_throttling_temperature_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `heating_throttling_temperature_range`')

        self._data["Heating Throttling Temperature Range"] = value

    @property
    def stage_1_heating_temperature_offset(self):
        """Get stage_1_heating_temperature_offset

        Returns:
            float: the value of `stage_1_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 1 Heating Temperature Offset"]

    @stage_1_heating_temperature_offset.setter
    def stage_1_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_1_heating_temperature_offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 1 value and greater than
        Stage 2 value, the stage number is 1.

        Args:
            value (float): value for IDD Field `stage_1_heating_temperature_offset`
                Units: deltaC
                value <= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `stage_1_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `stage_1_heating_temperature_offset`')

        self._data["Stage 1 Heating Temperature Offset"] = value

    @property
    def stage_2_heating_temperature_offset(self):
        """Get stage_2_heating_temperature_offset

        Returns:
            float: the value of `stage_2_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 2 Heating Temperature Offset"]

    @stage_2_heating_temperature_offset.setter
    def stage_2_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_2_heating_temperature_offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 2 value and greater than
        Stage 3 value, the stage number is 2.
        The value of this field has to be less the value at the previous field.

        Args:
            value (float): value for IDD Field `stage_2_heating_temperature_offset`
                Units: deltaC
                value <= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `stage_2_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `stage_2_heating_temperature_offset`')

        self._data["Stage 2 Heating Temperature Offset"] = value

    @property
    def stage_3_heating_temperature_offset(self):
        """Get stage_3_heating_temperature_offset

        Returns:
            float: the value of `stage_3_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 3 Heating Temperature Offset"]

    @stage_3_heating_temperature_offset.setter
    def stage_3_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_3_heating_temperature_offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 3 value and greater than
        Stage 4 value, the stage number is 3.
        The value of this field has to be less the value at the previous field.

        Args:
            value (float): value for IDD Field `stage_3_heating_temperature_offset`
                Units: deltaC
                value <= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `stage_3_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `stage_3_heating_temperature_offset`')

        self._data["Stage 3 Heating Temperature Offset"] = value

    @property
    def stage_4_heating_temperature_offset(self):
        """Get stage_4_heating_temperature_offset

        Returns:
            float: the value of `stage_4_heating_temperature_offset` or None if not set
        """
        return self._data["Stage 4 Heating Temperature Offset"]

    @stage_4_heating_temperature_offset.setter
    def stage_4_heating_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_4_heating_temperature_offset`
        The heating temperature offset is used to determine heating stage number for
        multi stage equipment.
        When the temperature difference of the heating setpoint and the controlled zone
        temperature at previous time step is less than Stage 4 value, the stage number is 4.
        The value of this field has to be less the value at the previous field.

        Args:
            value (float): value for IDD Field `stage_4_heating_temperature_offset`
                Units: deltaC
                value <= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except:
                raise ValueError('value {} need to be of type float '
                                 'for field `stage_4_heating_temperature_offset`'.format(value))
            if value > 0.0:
                raise ValueError('value need to be smaller 0.0 '
                                 'for field `stage_4_heating_temperature_offset`')

        self._data["Stage 4 Heating Temperature Offset"] = value

    @property
    def number_of_cooling_stages(self):
        """Get number_of_cooling_stages

        Returns:
            int: the value of `number_of_cooling_stages` or None if not set
        """
        return self._data["Number of Cooling Stages"]

    @number_of_cooling_stages.setter
    def number_of_cooling_stages(self, value=None):
        """  Corresponds to IDD Field `number_of_cooling_stages`
        Enter the number of the following sets of data for cooling temperature offset

        Args:
            value (int): value for IDD Field `number_of_cooling_stages`
                value >= 1
                value <= 4
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
                                 'for field `number_of_cooling_stages`'.format(value))
            if value < 1:
                raise ValueError('value need to be greater or equal 1 '
                                 'for field `number_of_cooling_stages`')
            if value > 4:
                raise ValueError('value need to be smaller 4 '
                                 'for field `number_of_cooling_stages`')

        self._data["Number of Cooling Stages"] = value

    @property
    def cooling_temperature_setpoint_base_schedule_name(self):
        """Get cooling_temperature_setpoint_base_schedule_name

        Returns:
            str: the value of `cooling_temperature_setpoint_base_schedule_name` or None if not set
        """
        return self._data["Cooling Temperature Setpoint Base Schedule Name"]

    @cooling_temperature_setpoint_base_schedule_name.setter
    def cooling_temperature_setpoint_base_schedule_name(self, value=None):
        """  Corresponds to IDD Field `cooling_temperature_setpoint_base_schedule_name`

        Args:
            value (str): value for IDD Field `cooling_temperature_setpoint_base_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `cooling_temperature_setpoint_base_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `cooling_temperature_setpoint_base_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `cooling_temperature_setpoint_base_schedule_name`')

        self._data["Cooling Temperature Setpoint Base Schedule Name"] = value

    @property
    def cooling_throttling_temperature_range(self):
        """Get cooling_throttling_temperature_range

        Returns:
            float: the value of `cooling_throttling_temperature_range` or None if not set
        """
        return self._data["Cooling Throttling Temperature Range"]

    @cooling_throttling_temperature_range.setter
    def cooling_throttling_temperature_range(self, value=1.1 ):
        """  Corresponds to IDD Field `cooling_throttling_temperature_range`

        Args:
            value (float): value for IDD Field `cooling_throttling_temperature_range`
                Units: deltaC
                Default value: 1.1
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
                                 'for field `cooling_throttling_temperature_range`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `cooling_throttling_temperature_range`')

        self._data["Cooling Throttling Temperature Range"] = value

    @property
    def stage_1_cooling_temperature_offset(self):
        """Get stage_1_cooling_temperature_offset

        Returns:
            float: the value of `stage_1_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 1 Cooling Temperature Offset"]

    @stage_1_cooling_temperature_offset.setter
    def stage_1_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_1_cooling_temperature_offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 1 value and less than
        Stage 2 value, the stage number is 1.

        Args:
            value (float): value for IDD Field `stage_1_cooling_temperature_offset`
                Units: deltaC
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
                                 'for field `stage_1_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `stage_1_cooling_temperature_offset`')

        self._data["Stage 1 Cooling Temperature Offset"] = value

    @property
    def stage_2_cooling_temperature_offset(self):
        """Get stage_2_cooling_temperature_offset

        Returns:
            float: the value of `stage_2_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 2 Cooling Temperature Offset"]

    @stage_2_cooling_temperature_offset.setter
    def stage_2_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_2_cooling_temperature_offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 2 value and less than
        Stage 3 value, the stage number is 2.
        The value of this field has to be greater than the value at the previous field.

        Args:
            value (float): value for IDD Field `stage_2_cooling_temperature_offset`
                Units: deltaC
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
                                 'for field `stage_2_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `stage_2_cooling_temperature_offset`')

        self._data["Stage 2 Cooling Temperature Offset"] = value

    @property
    def stage_3_cooling_temperature_offset(self):
        """Get stage_3_cooling_temperature_offset

        Returns:
            float: the value of `stage_3_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 3 Cooling Temperature Offset"]

    @stage_3_cooling_temperature_offset.setter
    def stage_3_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_3_cooling_temperature_offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 3 value and less than
        Stage 4 value, the stage number is 3.
        The value of this field has to be greater than the value at the previous field.

        Args:
            value (float): value for IDD Field `stage_3_cooling_temperature_offset`
                Units: deltaC
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
                                 'for field `stage_3_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `stage_3_cooling_temperature_offset`')

        self._data["Stage 3 Cooling Temperature Offset"] = value

    @property
    def stage_4_cooling_temperature_offset(self):
        """Get stage_4_cooling_temperature_offset

        Returns:
            float: the value of `stage_4_cooling_temperature_offset` or None if not set
        """
        return self._data["Stage 4 Cooling Temperature Offset"]

    @stage_4_cooling_temperature_offset.setter
    def stage_4_cooling_temperature_offset(self, value=None):
        """  Corresponds to IDD Field `stage_4_cooling_temperature_offset`
        The cooling temperature offset is used to determine cooling stage number for
        multi stage equipment.
        When the temperature difference of the cooling setpoint and the controlled zone
        temperature at previous time step is greater than Stage 4 value, the stage number is 4.
        The value of this field has to be greater than the value at the previous field.

        Args:
            value (float): value for IDD Field `stage_4_cooling_temperature_offset`
                Units: deltaC
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
                                 'for field `stage_4_cooling_temperature_offset`'.format(value))
            if value < 0.0:
                raise ValueError('value need to be greater or equal 0.0 '
                                 'for field `stage_4_cooling_temperature_offset`')

        self._data["Stage 4 Cooling Temperature Offset"] = value

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

class ZoneControlContaminantController(object):
    """ Corresponds to IDD object `ZoneControl:ContaminantController`
        Used to control a zone to a specified indoor level of CO2 or generic contaminants, or
        to specify minimum CO2 concentration schedule name for a zone.
    
    """
    internal_name = "ZoneControl:ContaminantController"
    field_count = 7
    required_fields = ["Name", "Controlled Zone Name"]

    def __init__(self):
        """ Init data dictionary object for IDD  `ZoneControl:ContaminantController`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Controlled Zone Name"] = None
        self._data["Carbon Dioxide Control Availability Schedule Name"] = None
        self._data["Carbon Dioxide Setpoint Schedule Name"] = None
        self._data["Minimum Carbon Dioxide Concentration Schedule Name"] = None
        self._data["Generic Contaminant Control Availability Schedule Name"] = None
        self._data["Generic Contaminant Setpoint Schedule Name"] = None
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
            self.controlled_zone_name = None
        else:
            self.controlled_zone_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.carbon_dioxide_control_availability_schedule_name = None
        else:
            self.carbon_dioxide_control_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.carbon_dioxide_setpoint_schedule_name = None
        else:
            self.carbon_dioxide_setpoint_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.minimum_carbon_dioxide_concentration_schedule_name = None
        else:
            self.minimum_carbon_dioxide_concentration_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.generic_contaminant_control_availability_schedule_name = None
        else:
            self.generic_contaminant_control_availability_schedule_name = vals[i]
        i += 1
        if i >= len(vals):
            return
        if len(vals[i]) == 0:
            self.generic_contaminant_setpoint_schedule_name = None
        else:
            self.generic_contaminant_setpoint_schedule_name = vals[i]
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
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `name`')

        self._data["Name"] = value

    @property
    def controlled_zone_name(self):
        """Get controlled_zone_name

        Returns:
            str: the value of `controlled_zone_name` or None if not set
        """
        return self._data["Controlled Zone Name"]

    @controlled_zone_name.setter
    def controlled_zone_name(self, value=None):
        """  Corresponds to IDD Field `controlled_zone_name`

        Args:
            value (str): value for IDD Field `controlled_zone_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `controlled_zone_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `controlled_zone_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `controlled_zone_name`')

        self._data["Controlled Zone Name"] = value

    @property
    def carbon_dioxide_control_availability_schedule_name(self):
        """Get carbon_dioxide_control_availability_schedule_name

        Returns:
            str: the value of `carbon_dioxide_control_availability_schedule_name` or None if not set
        """
        return self._data["Carbon Dioxide Control Availability Schedule Name"]

    @carbon_dioxide_control_availability_schedule_name.setter
    def carbon_dioxide_control_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `carbon_dioxide_control_availability_schedule_name`
        Availability schedule name for CO2 controller. Schedule value > 0 means the CO2
        controller is enabled. If this field is blank, then CO2  controller is always enabled.

        Args:
            value (str): value for IDD Field `carbon_dioxide_control_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `carbon_dioxide_control_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `carbon_dioxide_control_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `carbon_dioxide_control_availability_schedule_name`')

        self._data["Carbon Dioxide Control Availability Schedule Name"] = value

    @property
    def carbon_dioxide_setpoint_schedule_name(self):
        """Get carbon_dioxide_setpoint_schedule_name

        Returns:
            str: the value of `carbon_dioxide_setpoint_schedule_name` or None if not set
        """
        return self._data["Carbon Dioxide Setpoint Schedule Name"]

    @carbon_dioxide_setpoint_schedule_name.setter
    def carbon_dioxide_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `carbon_dioxide_setpoint_schedule_name`
        Schedule values should be carbon dioxide concentration in parts per million (ppm)

        Args:
            value (str): value for IDD Field `carbon_dioxide_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `carbon_dioxide_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `carbon_dioxide_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `carbon_dioxide_setpoint_schedule_name`')

        self._data["Carbon Dioxide Setpoint Schedule Name"] = value

    @property
    def minimum_carbon_dioxide_concentration_schedule_name(self):
        """Get minimum_carbon_dioxide_concentration_schedule_name

        Returns:
            str: the value of `minimum_carbon_dioxide_concentration_schedule_name` or None if not set
        """
        return self._data["Minimum Carbon Dioxide Concentration Schedule Name"]

    @minimum_carbon_dioxide_concentration_schedule_name.setter
    def minimum_carbon_dioxide_concentration_schedule_name(self, value=None):
        """  Corresponds to IDD Field `minimum_carbon_dioxide_concentration_schedule_name`
        Schedule values should be carbon dioxide concentration in parts per
        million (ppm)
        This field is used when the field System Outdoor Air Method =
        ProportionalControl in Controller:MechanicalVentilation

        Args:
            value (str): value for IDD Field `minimum_carbon_dioxide_concentration_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `minimum_carbon_dioxide_concentration_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `minimum_carbon_dioxide_concentration_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `minimum_carbon_dioxide_concentration_schedule_name`')

        self._data["Minimum Carbon Dioxide Concentration Schedule Name"] = value

    @property
    def generic_contaminant_control_availability_schedule_name(self):
        """Get generic_contaminant_control_availability_schedule_name

        Returns:
            str: the value of `generic_contaminant_control_availability_schedule_name` or None if not set
        """
        return self._data["Generic Contaminant Control Availability Schedule Name"]

    @generic_contaminant_control_availability_schedule_name.setter
    def generic_contaminant_control_availability_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generic_contaminant_control_availability_schedule_name`
        Availability schedule name for generic contaminant controller. Schedule value > 0 means
        the generic contaminant controller is enabled. If this field is blank, then generic
        contaminant controller is always enabled.

        Args:
            value (str): value for IDD Field `generic_contaminant_control_availability_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generic_contaminant_control_availability_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generic_contaminant_control_availability_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `generic_contaminant_control_availability_schedule_name`')

        self._data["Generic Contaminant Control Availability Schedule Name"] = value

    @property
    def generic_contaminant_setpoint_schedule_name(self):
        """Get generic_contaminant_setpoint_schedule_name

        Returns:
            str: the value of `generic_contaminant_setpoint_schedule_name` or None if not set
        """
        return self._data["Generic Contaminant Setpoint Schedule Name"]

    @generic_contaminant_setpoint_schedule_name.setter
    def generic_contaminant_setpoint_schedule_name(self, value=None):
        """  Corresponds to IDD Field `generic_contaminant_setpoint_schedule_name`
        Schedule values should be generic contaminant concentration in parts per
        million (ppm)
        This field is used when the field System Outdoor Air Method =
        IndoorAirQualityProcedureGenericContaminant in Controller:MechanicalVentilation

        Args:
            value (str): value for IDD Field `generic_contaminant_setpoint_schedule_name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except:
                raise ValueError('value {} need to be of type str '
                                 'for field `generic_contaminant_setpoint_schedule_name`'.format(value))
            if ',' in value:
                raise ValueError('value should not contain a comma '
                                 'for field `generic_contaminant_setpoint_schedule_name`')
            if '!' in value:
                raise ValueError('value should not contain a ! '
                                 'for field `generic_contaminant_setpoint_schedule_name`')

        self._data["Generic Contaminant Setpoint Schedule Name"] = value

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