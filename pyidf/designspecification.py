from collections import OrderedDict

class DesignSpecificationOutdoorAir(object):
    """ Corresponds to IDD object `DesignSpecification:OutdoorAir`
        This object is used to describe general outdoor air requirements which
        are referenced by other objects.
    """
    internal_name = "DesignSpecification:OutdoorAir"
    field_count = 7

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DesignSpecification:OutdoorAir`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Outdoor Air Method"] = None
        self._data["Outdoor Air Flow per Person"] = None
        self._data["Outdoor Air Flow per Zone Floor Area"] = None
        self._data["Outdoor Air Flow per Zone"] = None
        self._data["Outdoor Air Flow Air Changes per Hour"] = None
        self._data["Outdoor Air Flow Rate Fraction Schedule Name"] = None

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
            self.outdoor_air_method = None
        else:
            self.outdoor_air_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_per_person = None
        else:
            self.outdoor_air_flow_per_person = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_per_zone_floor_area = None
        else:
            self.outdoor_air_flow_per_zone_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_per_zone = None
        else:
            self.outdoor_air_flow_per_zone = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_air_changes_per_hour = None
        else:
            self.outdoor_air_flow_air_changes_per_hour = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.outdoor_air_flow_rate_fraction_schedule_name = None
        else:
            self.outdoor_air_flow_rate_fraction_schedule_name = vals[i]
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
            vals = set()
            vals.add("Flow/Person")
            vals.add("Flow/Area")
            vals.add("Flow/Zone")
            vals.add("AirChanges/Hour")
            vals.add("Sum")
            vals.add("Maximum")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `outdoor_air_method`'.format(value))

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
                Unit: m3/s-person
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
                Unit: m3/s-m2
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
                Unit: m3/s
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
                Unit: 1/hr
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

        self._data["Outdoor Air Flow Rate Fraction Schedule Name"] = value

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
        out.append(self._to_str(self.outdoor_air_method))
        out.append(self._to_str(self.outdoor_air_flow_per_person))
        out.append(self._to_str(self.outdoor_air_flow_per_zone_floor_area))
        out.append(self._to_str(self.outdoor_air_flow_per_zone))
        out.append(self._to_str(self.outdoor_air_flow_air_changes_per_hour))
        out.append(self._to_str(self.outdoor_air_flow_rate_fraction_schedule_name))
        return ",".join(out)

class DesignSpecificationZoneAirDistribution(object):
    """ Corresponds to IDD object `DesignSpecification:ZoneAirDistribution`
        This object is used to describe zone air distribution in terms of air distribution
        effectiveness and secondary recirculation fraction. It is referenced by Sizing:Zone
        and Controller:MechanicalVentilation objects
    """
    internal_name = "DesignSpecification:ZoneAirDistribution"
    field_count = 5

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DesignSpecification:ZoneAirDistribution`
        """
        self._data = OrderedDict()
        self._data["Name"] = None
        self._data["Zone Air Distribution Effectiveness in Cooling Mode"] = None
        self._data["Zone Air Distribution Effectiveness in Heating Mode"] = None
        self._data["Zone Air Distribution Effectiveness Schedule Name"] = None
        self._data["Zone Secondary Recirculation Fraction"] = None

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
            self.zone_air_distribution_effectiveness_in_cooling_mode = None
        else:
            self.zone_air_distribution_effectiveness_in_cooling_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_air_distribution_effectiveness_in_heating_mode = None
        else:
            self.zone_air_distribution_effectiveness_in_heating_mode = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_air_distribution_effectiveness_schedule_name = None
        else:
            self.zone_air_distribution_effectiveness_schedule_name = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.zone_secondary_recirculation_fraction = None
        else:
            self.zone_secondary_recirculation_fraction = vals[i]
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
                Unit: dimensionless
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
                Unit: dimensionless
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
                Unit: dimensionless
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
        out.append(self._to_str(self.zone_air_distribution_effectiveness_in_cooling_mode))
        out.append(self._to_str(self.zone_air_distribution_effectiveness_in_heating_mode))
        out.append(self._to_str(self.zone_air_distribution_effectiveness_schedule_name))
        out.append(self._to_str(self.zone_secondary_recirculation_fraction))
        return ",".join(out)

class DesignSpecificationZoneHvacSizing(object):
    """ Corresponds to IDD object `DesignSpecification:ZoneHVAC:Sizing`
        This object is used to describe general scalable zone HVAC equipment sizing which
        are referenced by other objects.
    """
    internal_name = "DesignSpecification:ZoneHVAC:Sizing"
    field_count = 24

    def __init__(self):
        """ Init data dictionary object for EPW IDD  `DesignSpecification:ZoneHVAC:Sizing`
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
            self.cooling_design_air_flow_method = None
        else:
            self.cooling_design_air_flow_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_supply_air_flow_rate = None
        else:
            self.cooling_design_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_supply_air_flow_rate_per_floor_area = None
        else:
            self.cooling_design_supply_air_flow_rate_per_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_supply_air_flow_rate = None
        else:
            self.fraction_of_autosized_cooling_design_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_supply_air_flow_rate_per_unit_cooling_capacity = None
        else:
            self.cooling_design_supply_air_flow_rate_per_unit_cooling_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_required = None
        else:
            self.supply_air_flow_rate_when_no_cooling_or_heating_is_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required = None
        else:
            self.supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required = None
        else:
            self.fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required = None
        else:
            self.fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_air_flow_method = None
        else:
            self.heating_design_air_flow_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_supply_air_flow_rate = None
        else:
            self.heating_design_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_supply_air_flow_rate_per_floor_area = None
        else:
            self.heating_design_supply_air_flow_rate_per_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_heating_design_supply_air_flow_rate = None
        else:
            self.fraction_of_heating_design_supply_air_flow_rate = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_supply_air_flow_rate_per_unit_heating_capacity = None
        else:
            self.heating_design_supply_air_flow_rate_per_unit_heating_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_capacity_method = None
        else:
            self.cooling_design_capacity_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_capacity = None
        else:
            self.cooling_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.cooling_design_capacity_per_floor_area = None
        else:
            self.cooling_design_capacity_per_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_cooling_design_capacity = None
        else:
            self.fraction_of_autosized_cooling_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_capacity_method = None
        else:
            self.heating_design_capacity_method = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_capacity = None
        else:
            self.heating_design_capacity = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.heating_design_capacity_per_floor_area = None
        else:
            self.heating_design_capacity_per_floor_area = vals[i]
        i += 1
        if len(vals[i]) == 0:
            self.fraction_of_autosized_heating_design_capacity = None
        else:
            self.fraction_of_autosized_heating_design_capacity = vals[i]
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
            vals = set()
            vals.add("None")
            vals.add("SupplyAirFlowRate")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedCoolingAirflow")
            vals.add("FlowPerCoolingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_design_air_flow_method`'.format(value))

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
                Unit: m3/s
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
                Unit: m3/s-m2
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
                Unit: m3/s-W
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
            vals = set()
            vals.add("None")
            vals.add("SupplyAirFlowRate")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedCoolingAirflow")
            vals.add("FractionOfAutosizedHeatingAirflow")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `supply_air_flow_rate_method_when_no_cooling_or_heating_is_required`'.format(value))

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
                Unit: m3/s
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
                Unit: m3/s-m2
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
            vals = set()
            vals.add("None")
            vals.add("SupplyAirFlowRate")
            vals.add("FlowPerFloorArea")
            vals.add("FractionOfAutosizedHeatingAirflow")
            vals.add("FlowPerHeatingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_design_air_flow_method`'.format(value))

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
                Unit: m3/s
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
                Unit: m3/s-m2
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
                Unit: m3/s-W
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
            vals = set()
            vals.add("None")
            vals.add("CoolingDesignCapacity")
            vals.add("CapacityPerFloorArea")
            vals.add("FractionOfAutosizedCoolingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `cooling_design_capacity_method`'.format(value))

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
                Unit: W/m2
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
            vals = set()
            vals.add("None")
            vals.add("HeatingDesignCapacity")
            vals.add("CapacityPerFloorArea")
            vals.add("FractionOfAutosizedHeatingCapacity")
            if value not in vals:
                raise ValueError('value {} is not an accepted value for '
                                 'field `heating_design_capacity_method`'.format(value))

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
                Unit: W/m2
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
        out.append(self._to_str(self.cooling_design_air_flow_method))
        out.append(self._to_str(self.cooling_design_supply_air_flow_rate))
        out.append(self._to_str(self.cooling_design_supply_air_flow_rate_per_floor_area))
        out.append(self._to_str(self.fraction_of_autosized_cooling_design_supply_air_flow_rate))
        out.append(self._to_str(self.cooling_design_supply_air_flow_rate_per_unit_cooling_capacity))
        out.append(self._to_str(self.supply_air_flow_rate_method_when_no_cooling_or_heating_is_required))
        out.append(self._to_str(self.supply_air_flow_rate_when_no_cooling_or_heating_is_required))
        out.append(self._to_str(self.supply_air_flow_rate_per_floor_area_when_no_clg_or_htg_is_required))
        out.append(self._to_str(self.fraction_of_design_cooling_supply_air_flow_rate_when_no_clg_or_htg_required))
        out.append(self._to_str(self.fraction_of_design_heating_supply_air_flow_rate_when_no_clg_or_htg_required))
        out.append(self._to_str(self.heating_design_air_flow_method))
        out.append(self._to_str(self.heating_design_supply_air_flow_rate))
        out.append(self._to_str(self.heating_design_supply_air_flow_rate_per_floor_area))
        out.append(self._to_str(self.fraction_of_heating_design_supply_air_flow_rate))
        out.append(self._to_str(self.heating_design_supply_air_flow_rate_per_unit_heating_capacity))
        out.append(self._to_str(self.cooling_design_capacity_method))
        out.append(self._to_str(self.cooling_design_capacity))
        out.append(self._to_str(self.cooling_design_capacity_per_floor_area))
        out.append(self._to_str(self.fraction_of_autosized_cooling_design_capacity))
        out.append(self._to_str(self.heating_design_capacity_method))
        out.append(self._to_str(self.heating_design_capacity))
        out.append(self._to_str(self.heating_design_capacity_per_floor_area))
        out.append(self._to_str(self.fraction_of_autosized_heating_design_capacity))
        return ",".join(out)