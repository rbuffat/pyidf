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
    def outdoor_air_method(self):
        """Get outdoor_air_method

        Returns:
            str: the value of `outdoor_air_method` or None if not set
        """
        return self._data["Outdoor Air Method"]

    @outdoor_air_method.setter
    def outdoor_air_method(self, value="Flow/Person"):
        """  Corresponds to IDD Field `Outdoor Air Method`
        Flow/Person => Outdoor Air Flow per Person * Occupancy = Design Flow Rate,
        Flow/Area => Outdoor Air Flow per Zone Floor Area * Zone Floor Area = Design Flow Rate,
        Flow/Zone => Outdoor Air Flow per Zone = Design Flow Rate,
        AirChanges/Hour => Outdoor Air Flow Air Changes per Hour * Zone Volume adjusted for m3/s = Design Flow Rate

        Args:
            value (str): value for IDD Field `Outdoor Air Method`
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
            except ValueError:
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
    def outdoor_air_flow_per_person(self, value=0.00944):
        """  Corresponds to IDD Field `Outdoor Air Flow per Person`
        0.00944 m3/s is equivalent to 20 cfm per person
        This input should be used if the field Outdoor Air Method is Flow/Person.
        This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Person`
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
            except ValueError:
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
    def outdoor_air_flow_per_zone_floor_area(self, value=0.0):
        """  Corresponds to IDD Field `Outdoor Air Flow per Zone Floor Area`
        This input should be used if the field Outdoor Air Method is Flow/Area.
        This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Zone Floor Area`
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
            except ValueError:
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
    def outdoor_air_flow_per_zone(self, value=0.0):
        """  Corresponds to IDD Field `Outdoor Air Flow per Zone`
        This input should be used if the field Outdoor Air Method is Flow/Zone.
        This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum

        Args:
            value (float): value for IDD Field `Outdoor Air Flow per Zone`
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
            except ValueError:
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
    def outdoor_air_flow_air_changes_per_hour(self, value=0.0):
        """  Corresponds to IDD Field `Outdoor Air Flow Air Changes per Hour`
        This input should be used if the field Outdoor Air Method is AirChanges/Hour.
        This input is used if the field Outdoor Air Method is AirChanges/Hour, Sum, or Maximum

        Args:
            value (float): value for IDD Field `Outdoor Air Flow Air Changes per Hour`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Outdoor Air Flow Rate Fraction Schedule Name`
        Schedule values are multiplied by the Outdoor Air Flow rate calculated using
        the previous four inputs. Schedule values are limited to 0 to 1.

        Args:
            value (str): value for IDD Field `Outdoor Air Flow Rate Fraction Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def zone_air_distribution_effectiveness_in_cooling_mode(self):
        """Get zone_air_distribution_effectiveness_in_cooling_mode

        Returns:
            float: the value of `zone_air_distribution_effectiveness_in_cooling_mode` or None if not set
        """
        return self._data["Zone Air Distribution Effectiveness in Cooling Mode"]

    @zone_air_distribution_effectiveness_in_cooling_mode.setter
    def zone_air_distribution_effectiveness_in_cooling_mode(self, value=1.0):
        """  Corresponds to IDD Field `Zone Air Distribution Effectiveness in Cooling Mode`

        Args:
            value (float): value for IDD Field `Zone Air Distribution Effectiveness in Cooling Mode`
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
            except ValueError:
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
    def zone_air_distribution_effectiveness_in_heating_mode(self, value=1.0):
        """  Corresponds to IDD Field `Zone Air Distribution Effectiveness in Heating Mode`

        Args:
            value (float): value for IDD Field `Zone Air Distribution Effectiveness in Heating Mode`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Air Distribution Effectiveness Schedule Name`
        optionally used to replace Zone Air Distribution Effectiveness in Cooling and
        Heating Mode

        Args:
            value (str): value for IDD Field `Zone Air Distribution Effectiveness Schedule Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def zone_secondary_recirculation_fraction(self, value=0.0):
        """  Corresponds to IDD Field `Zone Secondary Recirculation Fraction`

        Args:
            value (float): value for IDD Field `Zone Secondary Recirculation Fraction`
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
            except ValueError:
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
    def heating_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Heating Sizing Factor`

        Args:
            value (float): value for IDD Field `Heating Sizing Factor`
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
            except ValueError:
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
    def cooling_sizing_factor(self, value=1.0):
        """  Corresponds to IDD Field `Cooling Sizing Factor`

        Args:
            value (float): value for IDD Field `Cooling Sizing Factor`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Timesteps in Averaging Window`
        blank => set the timesteps in averaging window to
        Number of Timesteps per Hour resulting in a 1 hour averaging window
        default is number of timesteps for 1 hour averaging window

        Args:
            value (int): value for IDD Field `Timesteps in Averaging Window`
                value >= 1
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = int(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone or ZoneList Name`

        Args:
            value (str): value for IDD Field `Zone or ZoneList Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Cooling Design Supply Air Temperature Input Method`

        Args:
            value (str): value for IDD Field `Zone Cooling Design Supply Air Temperature Input Method`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Cooling Design Supply Air Temperature`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Cooling Design Supply Air Temperature Difference`
        Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be subtracted from the zone temperature
        at peak load to calculate the Zone Cooling Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Temperature Difference`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Heating Design Supply Air Temperature Input Method`

        Args:
            value (str): value for IDD Field `Zone Heating Design Supply Air Temperature Input Method`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Heating Design Supply Air Temperature`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = SupplyAirTemperature

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Heating Design Supply Air Temperature Difference`
        Zone Heating Design Supply Air Temperature is only used when Zone Heating Design
        Supply Air Temperature Input Method = TemperatureDifference
        The absolute value of this field will be added to the zone temperature
        at peak load to calculate the Zone Heating Design Supply Air Temperature.

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Temperature Difference`
                Units: deltaC
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Cooling Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Zone Cooling Design Supply Air Humidity Ratio`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Heating Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Zone Heating Design Supply Air Humidity Ratio`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Design Specification Outdoor Air Object Name`

        Args:
            value (str): value for IDD Field `Design Specification Outdoor Air Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Heating Sizing Factor`
        if blank or zero, global heating sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `Zone Heating Sizing Factor`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Zone Cooling Sizing Factor`
        if blank or zero, global cooling sizing factor from Sizing:Parameters is used.

        Args:
            value (float): value for IDD Field `Zone Cooling Sizing Factor`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Cooling Design Air Flow Method`
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
            except ValueError:
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
    def cooling_design_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Cooling Design Air Flow Rate`
        This input is used if Cooling Design Air Flow Method is Flow/Zone
        This value will be multiplied by the global or zone sizing factor and
        by zone multipliers.

        Args:
            value (float): value for IDD Field `Cooling Design Air Flow Rate`
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
            except ValueError:
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
    def cooling_minimum_air_flow_per_zone_floor_area(self, value=0.000762):
        """  Corresponds to IDD Field `Cooling Minimum Air Flow per Zone Floor Area`
        default is .15 cfm/ft2
        This input is used if Cooling Design Air Flow Method is DesignDayWithLimit

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow per Zone Floor Area`
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
            except ValueError:
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
    def cooling_minimum_air_flow(self, value=0.0):
        """  Corresponds to IDD Field `Cooling Minimum Air Flow`
        This input is used if Cooling Design Air Flow Method is DesignDayWithLimit

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow`
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
            except ValueError:
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
    def cooling_minimum_air_flow_fraction(self, value=0.0):
        """  Corresponds to IDD Field `Cooling Minimum Air Flow Fraction`
        fraction of the Cooling design Air Flow Rate
        This input is currently used in sizing the Fan minimum Flow Rate.
        It does not currently affect other component autosizing.

        Args:
            value (float): value for IDD Field `Cooling Minimum Air Flow Fraction`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Heating Design Air Flow Method`
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
            except ValueError:
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
    def heating_design_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Heating Design Air Flow Rate`
        This input is used if Heating Design Air Flow Method is Flow/Zone.
        This value will be multiplied by the global or zone sizing factor and
        by zone multipliers.

        Args:
            value (float): value for IDD Field `Heating Design Air Flow Rate`
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
            except ValueError:
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
    def heating_maximum_air_flow_per_zone_floor_area(self, value=0.002032):
        """  Corresponds to IDD Field `Heating Maximum Air Flow per Zone Floor Area`
        default is .40 cfm/ft2
        This field is used to size the heating design flow rate when Heating Design Air Flow Method = Flow/Zone.
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow per Zone Floor Area`
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
            except ValueError:
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
    def heating_maximum_air_flow(self, value=0.1415762):
        """  Corresponds to IDD Field `Heating Maximum Air Flow`
        default is 300 cfm
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow`
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
            except ValueError:
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
    def heating_maximum_air_flow_fraction(self, value=0.3):
        """  Corresponds to IDD Field `Heating Maximum Air Flow Fraction`
        fraction of the Heating Design Air Flow Rate
        This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.

        Args:
            value (float): value for IDD Field `Heating Maximum Air Flow Fraction`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Design Specification Zone Air Distribution Object Name`

        Args:
            value (str): value for IDD Field `Design Specification Zone Air Distribution Object Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
    def cooling_design_air_flow_method(self):
        """Get cooling_design_air_flow_method

        Returns:
            str: the value of `cooling_design_air_flow_method` or None if not set
        """
        return self._data["Cooling Design Air Flow Method"]

    @cooling_design_air_flow_method.setter
    def cooling_design_air_flow_method(self, value="SupplyAirFlowRate"):
        """  Corresponds to IDD Field `Cooling Design Air Flow Method`
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
            value (str): value for IDD Field `Cooling Design Air Flow Method`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Supply Air Flow Rate`
        Enter the magnitude of supply air volume flow rate during cooling operation.
        Required field when Supply air Flow Rate Method During Cooling Operation is SupplyAirFlowRate.
        This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Supply Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Cooling Design Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Supply Air Flow Rate Per Floor Area`
        Enter the cooling supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method During Cooling Operation is FlowPerFloorArea.
        This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Cooling Design Supply Air Flow Rate Per Floor Area`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Cooling Design Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FractionOfAutosizedCoolingAirflow.
        This field may be blank if a cooling coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Supply Air Flow Rate`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity`
        Enter the cooling supply air volume flow rate unit cooling capacity.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FlowPerCoolingCapacity. This field may be blank if a cooling coil is not
        included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Cooling Design Supply Air Flow Rate Per Unit Cooling Capacity`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Supply Air Flow Rate Method When No Cooling or Heating is Required`
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
            value (str): value for IDD Field `Supply Air Flow Rate Method When No Cooling or Heating is Required`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Supply Air Flow Rate When No Cooling or Heating is Required`
        Enter the magnitude of the supply air volume flow rate during when no cooling or heating
        is required. Required field when Supply air Flow Rate Method When No Cooling or Heating
        is Required is SupplyAirFlowRate.

        Args:
            value (float or "Autosize"): value for IDD Field `Supply Air Flow Rate When No Cooling or Heating is Required`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Supply Air Flow Rate When No Cooling or Heating is Required"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required`
        Enter the supply air volume flow rate per total floor area.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required
        is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area When No Clg or Htg is Required`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required
        is FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Design Cooling Supply Air Flow Rate When No Clg or Htg Required`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method When No Cooling or Heating is Required
        is FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Design Heating Supply Air Flow Rate When No Clg or Htg Required`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Air Flow Method`
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
            value (str): value for IDD Field `Heating Design Air Flow Method`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Supply Air Flow Rate`
        Enter the magnitude of the supply air volume flow rate during heating operation.
        Required field when Supply air Flow Rate Method During Heating Operation is SupplyAirFlowRate.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Supply Air Flow Rate`
                Units: m3/s
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Supply Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Supply Air Flow Rate Per Floor Area`
        Enter the heating supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method During Heating Operation is FlowPerFloorArea.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Heating Design Supply Air Flow Rate Per Floor Area`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Heating Design Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method During Heating Operation is
        FractionOfAutosizedHeatingAirflow.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Fraction of Heating Design Supply Air Flow Rate`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Supply Air Flow Rate Per Unit Heating Capacity`
        Enter the supply air volume flow rate per unit heating capacity.
        Required field when Supply air Flow Rate Method During Heating Operation is
        FlowPerHeatingCapacity.
        This field may be blank if a heating coil is not included in the Zone HVAC equipment.

        Args:
            value (float): value for IDD Field `Heating Design Supply Air Flow Rate Per Unit Heating Capacity`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Capacity Method`
        Enter the method used to determine the cooling design capacity for scalable sizing.
        None is used when a cooling coils is not included in the Zone HVAC Equipment or
        this field may be blank. If this input field is left blank, then the design cooling
        capacity is set to zero. CoolingDesignCapacity => selected when the design cooling capacity
        value is specified or auto-sized. CapacityPerFloorArea => selected when the design cooling
        capacity is determine from user specified cooling capacity per floor area and zone floor area.
        FractionOfAutosizedCoolingCapacity => is selected when the design cooling capacity is
        determined from a user specified fraction and the auto-sized design cooling capacity.

        Args:
            value (str): value for IDD Field `Cooling Design Capacity Method`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Capacity`
        Enter the design cooling capacity. Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Cooling Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Capacity Per Floor Area`
        Enter the cooling design capacity per zone floor area. Required field when the cooling design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Cooling Design Capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Capacity`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Capacity Method`
        Enter the method used to determine the heating design capacity for scalable sizing.
        None is used when a heating coil is not included in the Zone HVAC Equipment or
        this field may be blank. If this input field is left blank, then the design heating
        capacity is set to zero. HeatingDesignCapacity => selected when the design heating capacity
        value is specified or auto-sized. CapacityPerFloorArea => selected when the design cooling
        capacity is determine from user specified heating capacity per flow area and zone floor area.
        FractionOfAutosizedHeatingCapacity => is selected when the design heating capacity is
        determined from a user specified fraction and the auto-sized design heating capacity

        Args:
            value (str): value for IDD Field `Heating Design Capacity Method`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity. Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area. Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `AirLoop Name`

        Args:
            value (str): value for IDD Field `AirLoop Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Type of Load to Size On`
        Specifies the basis for sizing the system supply air flow rate
        Sensible and VentilationRequirement are the only available options
        Sensible uses the zone design air flow rates
        VentilationRequirement uses the system ventilation requirement

        Args:
            value (str): value for IDD Field `Type of Load to Size On`
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
            except ValueError:
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
    def design_outdoor_air_flow_rate(self, value="autosize"):
        """  Corresponds to IDD Field `Design Outdoor Air Flow Rate`

        Args:
            value (float or "Autosize"): value for IDD Field `Design Outdoor Air Flow Rate`
                Units: m3/s
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Design Outdoor Air Flow Rate"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Minimum System Air Flow Ratio`

        Args:
            value (float): value for IDD Field `Minimum System Air Flow Ratio`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Preheat Design Temperature`

        Args:
            value (float): value for IDD Field `Preheat Design Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Preheat Design Humidity Ratio`

        Args:
            value (float): value for IDD Field `Preheat Design Humidity Ratio`
                Units: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Precool Design Temperature`

        Args:
            value (float): value for IDD Field `Precool Design Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Precool Design Humidity Ratio`

        Args:
            value (float): value for IDD Field `Precool Design Humidity Ratio`
                Units: kgWater/kgDryAir
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Central Cooling Design Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Central Cooling Design Supply Air Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Central Heating Design Supply Air Temperature`

        Args:
            value (float): value for IDD Field `Central Heating Design Supply Air Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Sizing Option`

        Args:
            value (str): value for IDD Field `Sizing Option`
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
            except ValueError:
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
        """  Corresponds to IDD Field `100% Outdoor Air in Cooling`

        Args:
            value (str): value for IDD Field `100% Outdoor Air in Cooling`
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
            except ValueError:
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
        """  Corresponds to IDD Field `100% Outdoor Air in Heating`

        Args:
            value (str): value for IDD Field `100% Outdoor Air in Heating`
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
            except ValueError:
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
    def central_cooling_design_supply_air_humidity_ratio(self, value=0.008):
        """  Corresponds to IDD Field `Central Cooling Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Central Cooling Design Supply Air Humidity Ratio`
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
            except ValueError:
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
    def central_heating_design_supply_air_humidity_ratio(self, value=0.008):
        """  Corresponds to IDD Field `Central Heating Design Supply Air Humidity Ratio`

        Args:
            value (float): value for IDD Field `Central Heating Design Supply Air Humidity Ratio`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Cooling Design Air Flow Method`
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
            except ValueError:
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
    def cooling_design_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Cooling Design Air Flow Rate`
        This input is used if Cooling Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `Cooling Design Air Flow Rate`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Supply Air Flow Rate Per Floor Area During Cooling Operation`
        Enter the cooling supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method during cooling operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area During Cooling Operation`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method during cooling operation is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Design Supply Air Flow Rate Per Unit Cooling Capacity`
        Enter the supply air volume flow rate per unit cooling capacity.
        Required field when Supply air Flow Rate Method During Cooling Operation is
        FlowPerCoolingCapacity.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit Cooling Capacity`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Air Flow Method`

        Args:
            value (str): value for IDD Field `Heating Design Air Flow Method`
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
            except ValueError:
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
    def heating_design_air_flow_rate(self, value=0.0):
        """  Corresponds to IDD Field `Heating Design Air Flow Rate`
        This input is used if Heating Design Air Flow Method is Flow/System
        This value will *not* be multiplied by any sizing factor or by zone multipliers.
        If using zone multipliers, this value must be large enough to serve the multiplied zones.

        Args:
            value (float): value for IDD Field `Heating Design Air Flow Rate`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Supply Air Flow Rate Per Floor Area During Heating Operation`
        Enter the heating supply air volume flow rate per total conditioned floor area.
        Required field when Supply air Flow Rate Method during heating operation is FlowPerFloorArea.

        Args:
            value (float): value for IDD Field `Supply Air Flow Rate Per Floor Area During Heating Operation`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Design Heating Supply Air Flow Rate`
        Enter the supply air volume flow rate as a fraction of the heating supply air flow rate.
        Required field when Supply air Flow Rate Method during heating operation is
        FractionOfAutosizedHeatingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Heating Supply Air Flow Rate`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate v3`
        Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate.
        Required field when Supply air Flow Rate Method during heating operation is
        FractionOfAutosizedCoolingAirflow.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Design Cooling Supply Air Flow Rate v3`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Design Supply Air Flow Rate Per Unit Heating Capacity`
        Enter the heating supply air volume flow rate per unit heating capacity.
        Required field when Supply air Flow Rate Method during heating operation is
        FlowPerHeatingCapacity.

        Args:
            value (float): value for IDD Field `Design Supply Air Flow Rate Per Unit Heating Capacity`
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
            except ValueError:
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
        """  Corresponds to IDD Field `System Outdoor Air Method`

        Args:
            value (str): value for IDD Field `System Outdoor Air Method`
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
            except ValueError:
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
    def zone_maximum_outdoor_air_fraction(self, value=1.0):
        """  Corresponds to IDD Field `Zone Maximum Outdoor Air Fraction`

        Args:
            value (float): value for IDD Field `Zone Maximum Outdoor Air Fraction`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Capacity Method`
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
            value (str): value for IDD Field `Cooling Design Capacity Method`
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
            except ValueError:
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
    def cooling_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Cooling Design Capacity`
        Enter the design cooling capacity. Required field when the cooling design capacity method
        CoolingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Cooling Design Capacity`
                Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Cooling Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Cooling Design Capacity Per Floor Area`
        Enter the cooling design capacity per total floor area of cooled zones served by an airloop.
        Required field when the cooling design capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Cooling Design Capacity Per Floor Area`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Cooling Design Capacity`
        Enter the fraction of auto-sized cooling design capacity. Required field when the cooling
        design capacity method field is FractionOfAutosizedCoolingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Cooling Design Capacity`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Capacity Method`
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
            value (str): value for IDD Field `Heating Design Capacity Method`
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
            except ValueError:
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
    def heating_design_capacity(self, value="autosize"):
        """  Corresponds to IDD Field `Heating Design Capacity`
        Enter the design heating capacity. Required field when the heating design capacity method
        HeatingDesignCapacity.

        Args:
            value (float or "Autosize"): value for IDD Field `Heating Design Capacity`
                Units: W
                Default value: "autosize"
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value_lower = str(value).lower()
                if value_lower == "autosize":
                    self._data["Heating Design Capacity"] = "Autosize"
                    return
            except ValueError:
                pass
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Heating Design Capacity Per Floor Area`
        Enter the heating design capacity per zone floor area. Required field when the heating design
        capacity method field is CapacityPerFloorArea.

        Args:
            value (float): value for IDD Field `Heating Design Capacity Per Floor Area`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Fraction of Autosized Heating Design Capacity`
        Enter the fraction of auto-sized heating design capacity. Required field when capacity the
        heating design capacity method field is FractionOfAutosizedHeatingCapacity.

        Args:
            value (float): value for IDD Field `Fraction of Autosized Heating Design Capacity`
                value >= 0.0
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Plant or Condenser Loop Name`
        Enter the name of a PlantLoop or a CondenserLoop object

        Args:
            value (str): value for IDD Field `Plant or Condenser Loop Name`
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = str(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Loop Type`

        Args:
            value (str): value for IDD Field `Loop Type`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Design Loop Exit Temperature`

        Args:
            value (float): value for IDD Field `Design Loop Exit Temperature`
                Units: C
                if `value` is None it will not be checked against the
                specification and is assumed to be a missing value

        Raises:
            ValueError: if `value` is not a valid value
        """
        if value is not None:
            try:
                value = float(value)
            except ValueError:
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
        """  Corresponds to IDD Field `Loop Design Temperature Difference`

        Args:
            value (float): value for IDD Field `Loop Design Temperature Difference`
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
            except ValueError:
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
        """  Corresponds to IDD Field `Column Separator`

        Args:
            value (str): value for IDD Field `Column Separator`
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
            except ValueError:
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